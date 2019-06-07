'''

This module is used to include some helper function for Port Monitoring

'''

def set_networkuri_lig(data_variable, get_output):
	'''
	Build the network URI's from the network Name and form the 
	LIG body 
	'''
	temp = data_variable
	for i in range(len(temp['uplinkSets'])):
		for j in range(len(temp['uplinkSets'][i]['networkUris'])):
			for x in get_output['members']:
				if temp['uplinkSets'][i]['networkUris'][j] == x['name']:
					temp['uplinkSets'][i]['networkUris'][j] = x['uri']
	return temp