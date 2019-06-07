*** Settings ***
Documentation		 ROLES.1 - Verify Admin level user has RW access to Hill in OneView
Library		json
Library		collections
Library 	BuiltIn
Library		String
Library		FusionLibrary
Variables	data_variables.py
Library		OperatingSystem
Library		String
Resource		resource.txt

Suite Setup    Cleanup For Suite
Suite Teardown    Cleanup For Suite

*** Test Cases ***
#####Verify Admin user has read-only access to Hill in OneView######
1. Log-in to the appliance
	Set Log Level    TRACE
    ${Login_response} =		Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}	
	Run keyword unless	${Login_response[0]['status_code']}== 200    Fail    "Unable to Login"
	Precheck for IC in OA
	Log to console and logfile    \n\nTest Step-1 executed Successfully

###Inital Cleanup###
2. Initial Cleanup
    Remove ALL Enclosures
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Remove ALL Ethernet Networks
    Remove ALL FC Networks
	Remove All Users
	
3. Create Network
	${Response}     fusion api create ethernet network		${enet_hill}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Create Ethernet network"
	Add FC Networks from variable    ${fcNet_hill}
	Log to console and logfile    \n\nNetworks Created Successfully!!
	
4. Create LIG,EG and Import Enclosure
	${body} =   Build LIG body      ${lig_hill}
	${resp_lig} = 	Fusion Api Create LIG	${body}
	Run keyword unless	${resp_lig['status_code']}== 202	Fail	"Unable to Create LIG"
	${task} =	Wait For Task 	${resp_lig} 	120s	2s
	Log to console and logfile    \n\nLIG created successfully!!

	${Enc_Grp_Resp} =    Add Enclosure Group from variable		${enc_group_hill}
	Run keyword unless	${Enc_Grp_Resp['status_code']}== 201	Fail	"Unable to Create Enclosure Group"
	Log to console and logfile    \n\nEG created succesfully!!
	
	${Enc_Resp} =    Add Enclosures from variable     ${encs}
	Run keyword unless	${Enc_Resp['status_code']}== 202	Fail	"Unable to Create Ethernet network"
	Log to console and logfile    \n\nEnclosure imported succesfully!!
	

	
5. Create Different Users
	:FOR	${i}	IN	@{users}
	\	${Response}     Fusion Api Add User    ${i}
	\	Run keyword unless	${Response['status_code']}== 200	Fail	"Unable to Create users"
	\	Log To Console    \n${Response['userName']} created Successfully
	
6. Verifying the Write Access to HILL in OV
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}	
	${us} = 		Copy Dictionary	${uplink_sets['us_fc']}
	${body} = 		Build US body 	${us}	${li_uri}
	${resp} = 		Fusion Api Create Uplink Set	body=${body}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	Run keyword unless	${resp['status_code']}== 202    Fail    "Admin level user has no WRITE Access To HILL"
	Log To Console    \n\n${admin_credentials['userName']} has WRITE Access to Hill

7. Verifying the Read Access to HILL in OV
	${Response} = 	Fusion Api Get Li
	Run keyword unless	${Response['status_code']}== 200    Fail    "Admin level user has no READ Access To HILL"
	Log To Console    \n\n${admin_credentials['userName']} has READ Access to Hill
	
8.Log-out from the appliance 
	${Logout_response}		Fusion Api Logout Appliance
	Run keyword unless	${Logout_response['status_code']}== 204    Fail    "Unable to Logout"
	Log To Console    \n\nLogged_Out from Appliance as ${admin_credentials['userName']}
			
9. Log-in as Network Admin

	${Login_response}     Fusion Api Login Appliance    ${APPLIANCE_IP}        ${network_admin}
	Run keyword unless	${Login_response[0]['status_code']}== 200    Fail    "Unable to Login"
	Log To Console    \n\nLogged in as ${network_admin['userName']}
	
	Log To Console    \n\nVerifying WRITE Access for ${network_admin['userName']}
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}	
	${us} = 		Copy Dictionary	${uplink_sets['us_fc_1']}
	${body} = 		Build US body 	${us}	${li_uri}
	${resp} = 		Fusion Api Create Uplink Set	body=${body}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	Run keyword unless	${resp['status_code']}== 202    Fail    "Network Admin user has no WRITE Access To HILL"
	Log To Console    \n\n${network_admin['userName']} has WRITE Access to Hill    

	Log to Console    \n\nVerifying the READ Access for ${network_admin['userName']}
	${Response} = 	Fusion Api Get Li
	Run keyword unless	${Response['status_code']}== 200	Fail    "Network Admin user has no READ Access To HILL"
	Log To Console    \n\n${network_admin['userName']} has READ Access to Hill 
		
	${Logout_response}		Fusion Api Logout Appliance
	Run keyword unless	${Logout_response['status_code']}== 204    Fail    "Unable to Logout"
	Log To Console    \n\nLogged_Out from Appliance as ${network_admin['userName']}
	
####Verify non-Admin level user has read-only access to Hill in OneView####

10. Log-in as Server Admin

	${Login_response}     Fusion Api Login Appliance    ${APPLIANCE_IP}        ${serveradmin_credentials}
	Run keyword unless	${Login_response[0]['status_code']}== 200    Fail    "Unable to Login"
	Log To Console    \n\nLogged in as ${serveradmin_credentials['userName']}

	
	Log To Console    \n\nVerifying WRITE Access for ${serveradmin_credentials['userName']}
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}	
	${us} = 		Copy Dictionary	${uplink_sets['us_fc3']}
	${body} = 		Build US body 	${us}	${li_uri}
	${resp} = 		Fusion Api Create Uplink Set	body=${body}
		
	Run Keyword If  '${resp['status_code']}' == '401'    Log to console  \n Expected Failure! \nStatus Code: ${resp['status_code']}
	...             ELSE    FAIL
	Run Keyword If  '${resp['errorCode']}' == 'AUTHORIZATION'    Log to console  \n Expected Failure! \n\nError: No ${resp['errorCode']} \nDetails: ${resp['message']}\n
	...             ELSE    FAIL
	
	Log to Console    \n\nVerifying the READ Access for ${serveradmin_credentials['userName']}
	${Response} = 	Fusion Api Get Li
	Run keyword unless	${Response['status_code']}== 200	Fail    "Network Admin user has no READ Access To HILL"
	Log To Console    \n\n${serveradmin_credentials['userName']} has READ Access to Hill 
		
	${Logout_response}		Fusion Api Logout Appliance
	Run keyword unless	${Logout_response['status_code']}== 204    Fail    "Unable to Logout"
	Log To Console    \n\nLogged_Out from Appliance as ${serveradmin_credentials['userName']}

11. Log-in as Backup Admin

	${Login_response}     Fusion Api Login Appliance    ${APPLIANCE_IP}        ${backup_admin}
	Run keyword unless	${Login_response[0]['status_code']}== 200    Fail    "Unable to Login"
	Log To Console    \n\nLogged in as ${backup_admin['userName']}

	Log To Console    \n\nVerifying WRITE Access for ${backup_admin['userName']}
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}	
	${us} = 		Copy Dictionary	${uplink_sets['us_fc4']}
	${body} = 		Build US body 	${us}	${li_uri}
	${resp} = 		Fusion Api Create Uplink Set	body=${body}
		
	Run Keyword If  '${resp['status_code']}' == '401'    Log to console  \n Expected Failure! \nStatus Code: ${resp['status_code']}
	...             ELSE    FAIL
	Run Keyword If  '${resp['errorCode']}' == 'AUTHORIZATION'    Log to console  \n Expected Failure! \n\nError: No ${resp['errorCode']} \nDetails: ${resp['message']}\n
	...             ELSE    FAIL
	
	${Response} = 	Fusion Api Get Li
	Run keyword unless	${Response['status_code']}== 200    Fail    "Admin level user has no READ Access To HILL"
	Log To Console    \n\n${backup_admin['userName']} user has READ Access to Hill
	
	${Logout_response}		Fusion Api Logout Appliance
	Run keyword unless	${Logout_response['status_code']}== 204    Fail    "Unable to Logout"
	Log To Console    \n\nLogged_Out from Appliance as ${backup_admin['userName']}

12. Log-in as ReadOnly User

	${Login_response}     Fusion Api Login Appliance    ${APPLIANCE_IP}        ${readonly_user}
	Run keyword unless	${Login_response[0]['status_code']}== 200    Fail    "Unable to Login"
	Log To Console    \n\nLogged in as ${readonly_user['userName']}

	Log To Console    \n\nVerifying WRITE Access for ${readonly_user['userName']}
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}	
	${us} = 		Copy Dictionary	${uplink_sets['us_eth']}
	${body} = 		Build US body 	${us}	${li_uri}
	${resp} = 		Fusion Api Create Uplink Set	body=${body}
			
	Run Keyword If  '${resp['status_code']}' == '401'    Log to console  \n Expected Failure! \nStatus Code: ${resp['status_code']}
	...             ELSE    FAIL
	Run Keyword If  '${resp['errorCode']}' == 'AUTHORIZATION'    Log to console  \n Expected Failure! \n\nError: No ${resp['errorCode']} for ${readonly_user['userName']}\nDetails: ${resp['message']}\n
	...             ELSE    FAIL
	
	${Response} = 	Fusion Api Get Li
	Run keyword unless	${Response['status_code']}== 200    Fail    "ReadOnly User has no READ Access To HILL"
	Log To Console    \n\n${readonly_user['userName']} user has READ Access to Hill
	
	${Logout_response}		Fusion Api Logout Appliance
	Run keyword unless	${Logout_response['status_code']}== 204    Fail    "Unable to Logout"
	Log To Console    \n\nLogged_Out from Appliance as ${readonly_user['userName']}
	
###Proceeding with cleanup###
TEARDOWN
	Login to OneView via REST
    ${encs} = 	Fusion Api Get Enclosures
	${resp}		fusion API Remove Enclosure		uri=${encs['members'][0]['uri']}
	${task} =	Wait For Task1 	${resp}	
	${resp}=	fusion api delete enclosure group		name=${enc_group_hill['name']}
	Run keyword unless	${resp['status_code']}== 204	Fail	"Unable to delete the Enclosure Group"
	
	${resp}=	fusion api delete lig		name=${lig_hill['name']}
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete the LIG"
    Log to console and logfile    Test Suite ROLES for hill module completed successfully