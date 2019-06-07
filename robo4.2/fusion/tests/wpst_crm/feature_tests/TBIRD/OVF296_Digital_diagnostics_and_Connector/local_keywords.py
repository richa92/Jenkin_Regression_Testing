'''
This python module contains local keywords for validating the outputs
'''
from data_variables import *
import json

def validate_connector_info(connector, output,lower_api=False):
	
	flag = True
	out = None
	output = json.loads(output)
	try:
		for i in output:
			if i['portName'] == connector['portName']:		
				out = i

		for j in out.keys():
			if j == 'digitalDiagnostics':
				if connector[j].keys()  != out[j].keys():
					return False, "Digital diagnostics keys are not same"
				if None in connector.values():
					return False, "Digital diagnostics values are not available"
					
			elif j == "speed" or j == "extIdentifier":
				continue
			elif out[j] != connector[j]:
				print out[j]
				flag= False
				break
		if flag:
			if lower_api:
				if "digitalDiagnostics" not in out.keys():
					return True, "Successfully verified only COnnector information is available not Digital Diagnostics"
				else:
					return False, "Digital Diagnostics information is available for the API passed!!"
			return True, "Digital diagnostics keys and Connector infomrations are verified successfully"
			#return True
		else:
			return (False, "Connector values are not matching with expected output")
		#return False
	except	AttributeError as e:
		return	"Off", "No Content available for Connector and digital diagnostics"

'''
def main():

	a = [
	{"portName":"1","vendorName":"HP-A     BROCADE","vendorPartNumber":"QK724A","vendorRevision":"A","speed":"null","vendorOui":"00:05:1e","extIdentifier":"null","digitalDiagnostics":{"temperature":"30","voltage":"3316.100","rxPower":"-2.937","txPower":"-2.708","current":"7.282"},"serialNumber":"HAA115466085Z32","identifier":"SFP","connector":"LC"},{"portName":"2","vendorName":"HP-A     BROCADE","vendorPartNumber":"QK724A","vendorRevision":"A","speed":"null","vendorOui":"00:05:1e","extIdentifier":"null","digitalDiagnostics":{"temperature":"30","voltage":"3316.200","rxPower":"-2.829","txPower":"-2.161","current":"7.080"},"serialNumber":"HAA114376005TH5","identifier":"SFP","connector":"LC"}]
	s,mk = validate_connector_info(sfp_connector, a)
#	s = validate_connector_info(sfp_connector, a)
	print s, mk
	
#main()
'''