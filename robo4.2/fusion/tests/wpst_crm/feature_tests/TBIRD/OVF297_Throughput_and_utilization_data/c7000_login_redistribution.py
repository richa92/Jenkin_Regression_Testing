import httplib2
import json
import threading
from time import sleep
import logging

# Hardcoded Header input for the rest call
inter_headers = {'X-Api-Version': '400', 'Accept-Language': 'en',
                 'auth': u'LTY5MDY3OTcwMzI2UcaDwrvfZaZ5gJo68IngzQSxgk-v5ybx',
                 'Accept': 'application/json',
                 'Content-Type': 'application/json'}
login_header = {'X-Api-Version': '400', "Content-Type": "application/json"}
login_payload = {"password":"hpvse123","userName":"Administrator",
                 "loginMsgAck":"true"}		                            # Login payload

http = httplib2.Http(disable_ssl_certificate_validation=True)		    # skip the SSL validation for the appliance


def login_app(app_ip):

	'''
    Perform the appliance login session through the rest call
    return SessionID on success, None on failure
    '''

	try:
		headd, cont = http.request('https://'+app_ip+'/rest/login-sessions',
								   'POST',headers=login_header,
								   body=json.dumps(login_payload))
		if headd['status'] == '200':
			session_id = json.loads(cont)['sessionID']
			inter_headers['auth'] = session_id
			return session_id
	
	except Exception as e:
		return("Had trouble in : %s" % e)
		
def get_logical_interconnect(app_ip, li_uri, ports, output):
	'''
	This method will get the interconnect details and validate the login counts 
	as passed as the argument
	'''
	try:
		interconnect_uri_list = dict()
		uri = 'https://'+app_ip+\
		'/rest/interconnects/?count=10&filter=%22logicalInterconnectId=%27'+\
		li_uri.split('/')[-1]+'%27'
		headd, cont = http.request(uri,'GET',headers=inter_headers)
		
		if headd['status'] == '401':
			return headd['status']
		if headd['status'] == '200':
		    json_data = json.loads(cont)
		    logins = {i['name'].split()[-1]+'.'+\
			j['portName']:j['fcPortProperties']['loginsCount'] \
			for bay in ports.keys() for por in ports[bay] \
			for i in json_data['members'] if i['name'] == 'enc1, interconnect '+\
			str(bay) for j in i['ports'] if j['portName'] == str(por)}
			
		    if logins == output:
		        return True, logins
		    else:
		        return False, logins
		else:
			return headd
	except Exception as e:
		print("Had trouble: %s" % e)
		

def verify_login_count(app_ip, li_uri, ports, output):
	'''
	This method will get the login counts from the LI
	'''
	
	try:
		login_status = login_app(app_ip)
		if login_status == None:
			return "Error is login"
		login_count_status, logins = get_logical_interconnect(app_ip,\
		li_uri, ports, output)
		return login_count_status, logins
	except Exception as e:
		print ("Had Trouble in: %s" %e)
		
def get_port_uri(data, ports):
	'''
	This method is used to get teh 
	'''
						
	e={str(name)+'.'+j['portName']:j['uri'] for name in ports.keys() \
	for i in data['members'] for po in ports[name] for j in i['ports']\
	if j['interconnectName'].split()[-1] == str(name) and j['portName'] == str(po)}
	return e
	
def edit_interconnect(app_ip, uri, payload):

    '''
	This method will edit the interconnect and enable or disable the ports 
	'''
    try:
		login_status = login_app(app_ip)
		if login_status == None:
			return "Login Error"
		uri = 'https://'+app_ip+uri
		headd, cont = http.request(uri,'PUT',headers=inter_headers,\
		body=json.dumps(payload))
		print headd
		print cont
		if headd['status'] == '401':
			return headd['status']
		if headd['status'] == 202:
		    json_data = json.loads(cont)
		    return json_data['status']
		else:
			return headd
    except Exception as e:
        print("Had trouble: %s" % e)

		
def manual_login_redistribution(app_ip,uri,payload,uplinkset_name):
	'''
	This method will perform the login redistribution 
	'''
	
	try:
		mlr_payload={'uplinkSets':[i['uri'] for i in payload['members'] \
		for j in uplinkset_name if j == i['name']]}
		login_status = login_app(app_ip)
		if login_status == None:
			return "Login Error"
		uri = 'https://'+app_ip+uri+'/redistributeLogins'
		headd, cont = http.request(uri,'PUT',headers=inter_headers,\
		body=json.dumps(mlr_payload))
		
		if headd['status'] == '401':
			return headd['status']
		if headd['status'] == 202:
		    json_data = json.loads(cont)
		    return json_data['status']
		else:
			return headd
	except Exception as e:
		print("Had trouble: %s" % e)
	
def build_edit_interconnect_payload(output, interconnect_keys, flag):
	'''
	This method will build payload needed for the robot framework keyword
	'''
	temp_dict =  {key:output[key] for key in interconnect_keys}
	temp_dict['enabled'] = flag
	return [temp_dict]

def enclosure_preview(app_ip,payload):

	'''
    Post the enclosure Preivew and return the output 
    '''
	try:
		login_status = login_app(app_ip)
		if login_status == None:
			return "Error is login"
		resp = http.request('https://'+app_ip+'/rest/enclosure-preview',
								   'POST',headers=inter_headers,
								   body=json.dumps(payload))
		if resp[0]['status'] == '200':
			return json.loads(resp[1])
	except Exception as e:
		return("Had trouble in : %s" % e)
				


if __name__ == "__main__":
	try:
		uri = "/rest/logical-interconnects/63e3a8eb-7b6f-482b-b9a8-7ea8ce89a1ce/telemetry-configurations/6b28a3da-2116-4ad9-b477-4910ec131ed1"
		body = {"type":"telemetry-configuration","enableTelemetry":"true","sampleCount":10,"sampleInterval":6}
		resp = edit_interconnect("15.186.9.20",uri,body)
	except Exception as e:
		print("Had trouble: %s" % e)
	#enclosure_previ = {"hostname":"15.186.27.232","username":"Administrator","password":"compaq","ligPrefix":"LIG_Hill","force":True,"logicalInterconnectGroupNeeded":True}

	#res  = enclosure_preview('15.186.25.114',enclosure_previ)

	#print res['logicalInterconnectGroup']
