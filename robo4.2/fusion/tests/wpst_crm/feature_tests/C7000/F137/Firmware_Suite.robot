*** Settings ***
Documentation		Verify Firmware update is possible with Hill module.
Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary
Library			OperatingSystem
Library			String
Variables		data_variables.py
Resource        resource.txt

Suite Setup    Cleanup For Suite
Suite Teardown    Cleanup For Suite

*** Test Cases ***

1.Create SessionID through API
	Set Log Level    TRACE
    ${Login_response} =	Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	Run keyword unless	${Login_response[0]['status_code']}== 200	Fail	"Unable to Login"
	Precheck for IC in OA
	Log to console and logfile    Test Step-1 completed successfully
	
2.Create LIG, EG and import enclosure with firmware upgrade (Big Bang method)
	${body} =   Build LIG body      ${lig_hill}
	${resp_lig} = 	Fusion Api Create LIG	${body}
	${task} =	Wait For Task 	${resp_lig} 	120s	2s
	Log to console and logfile    LIG created successfully
	${uri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri
	Log to console and logfile    ${uri}
		
	${resp_eg}=    Add Enclosure Group from variable		${enc_group_hill}
	Run keyword unless	${resp_eg['status_code']}== 201	Fail	"Unable to Create EG"
	Log to console and logfile    EG created succesfully
	${resp_import} =    Add Enclosures from variable     ${encs_fwupdate}
	Run keyword unless	${resp_import['status_code']}== 202	Fail	"Unable to import enclosure"
	Log to console and logfile    Enclosure imported succesfully with firmware update
	
3.Validate interconnect firmware version	
	${resp} = 	Fusion Api Get Interconnect  		param=?filter="'name' = '${interconnectname_1}'"
	${firmwareVersion_1} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion 
	Log to console and logfile    ${firmwareVersion_1}
	Run keyword unless    ${firmwareVersion_1} == ${fc_firmwareVersion_snap6}	Fail	"Firmware version mismatch"
	
	${resp} = 	Fusion Api Get Interconnect  		param=?filter="'name' = '${interconnectname_2}'"
	${firmwareVersion_2} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion 
	Log to console and logfile    ${firmwareVersion_2}
	Run keyword unless    ${firmwareVersion_2} == ${fc_firmwareVersion_snap6}	Fail	"Firmware version mismatch	
	Log to console and logfile    Test Step-3 completed successfully

4.Downgrade firmware through LI page
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	${response}=    Fusion Api LI Upgrade Firmware    ${liupdate_body}    ${li_uri}
	Run Keyword If    ${response['status_code']} == 202    Wait For Task LI Update	
	Log to console and logfile    Test Step-4 completed successfully
	
5.Validate interconnect firmware version after LI update
	${resp} = 	Fusion Api Get Interconnect  		param=?filter="'name' = '${interconnectname_1}'"
	${firmwareVersion_1} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion 
	Log to console and logfile    ${firmwareVersion_1}
	Run keyword unless    ${firmwareVersion_1} == ${fc_firmwareVersion_snap5}	Fail	"Firmware version mismatch"
	
	${resp} = 	Fusion Api Get Interconnect  		param=?filter="'name' = '${interconnectname_2}'"
	${firmwareVersion_2} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion 
	Log to console and logfile    ${firmwareVersion_2}
	Run keyword unless    ${firmwareVersion_2} == ${fc_firmwareVersion_snap5}	Fail	"Firmware version mismatch	
	Log to console and logfile    Test Step-5 completed successfully
	
6.Update firmware through LE page	
	${resp} =    Fusion Api Get Logical Enclosure    param=?filter="'name' = '${ENC1}'"
	${uri} =    Get From Dictionary    ${resp['members'][0]}    uri
    ${resp_1} =    fusion_api_get_headers    
	Log to console and logfile    ${resp_1}
	Set To Dictionary    ${resp_1}    ${key}    ${value}
    ${resp_head}    Copy Dictionary    ${resp_1} 
	Log to console and logfile    ${resp_head}
	${response}=    Fusion Api Le Firmware Update    ${leupdate_body}	headers=${resp_head}    uri=${uri}
	Run Keyword If	${response['status_code']} == 202	Wait For Task LE Update
	Log to console and logfile    Test Step-6 completed successfully
	
7.Validate interconnect firmware version after LE update
	${resp} = 	Fusion Api Get Interconnect  		param=?filter="'name' = '${interconnectname_1}'"
	${firmwareVersion_1} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion 
	Log to console and logfile    ${firmwareVersion_1}
	Run keyword unless    ${firmwareVersion_1} == ${fc_firmwareVersion_snap6}	Fail	"Firmware version mismatch"
	
	${resp} = 	Fusion Api Get Interconnect  		param=?filter="'name' = '${interconnectname_2}'"
	${firmwareVersion_2} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion 
	Log to console and logfile    ${firmwareVersion_2}
	Run keyword unless    ${firmwareVersion_2} == ${fc_firmwareVersion_snap6}	Fail	"Firmware version mismatch	
	Log to console and logfile    Test Step-7 completed successfully
		
###Proceeding with cleanup###
8.Teardown (a) Cleanup
	${encs} = 	Fusion Api Get Enclosures
	${resp}		fusion API Remove Enclosure		uri=${encs['members'][0]['uri']}
	${task} =	Wait For Task1 	${resp}
	
	${resp}=	fusion api delete enclosure group		name=${enc_group_hill['name']}
	Run keyword unless	${resp['status_code']}== 204	Fail	"Unable to delete the Enclosure Group"
	
	${resp}=	fusion api delete lig		name=${lig_hill['name']}
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete the Enclosure Group"
	Log to console and logfile    Test Step-8 completed successfully