*** Settings ***
Documentation		Validating the Port Monitoring for F110 with Potash and Chloride 10 with redundancy as ASide

Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary

#Variables		data_redundant_variables.py

Resource        resource.txt
Library			Collections
Library			port_monitor_support_module

#Resource            ../../../../../Resource/fusion_api_all_resource_files.txt
Resource            ../../../../../../Resources/api/fusion_api_resource.txt

Suite Setup		Suite Setup Tasks
#Suite Teardown	Suite Teardown Tasks
Suite Teardown	Teardown

*** Test Cases ***
    
1. Aside Create the server profiles
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

	Add Server Profiles from variable   ${server_profiles_Aside}
	Log to Console		Waiting	${\n}
	Log to Console		Waiting OVer		${\n}
	#Power on server     ${ENC1}, bay 1
    Power on server     ${ENC1}, bay 1
	Sleep   600
	Log to console and logfile  	Waiting 10 minutes for server to boot...

	#Create Different Users

	:FOR	${i}	IN	@{users}
	\	${Response}     Fusion Api Add User    ${i}
	\	Run keyword unless	${Response['status_code']}== 200	Fail	"Unable to Create users"
	\	Log To Console    \n${Response['userName']} created Successfully

2. Aside Log-in as Server Admin

	${Logout_response}		Fusion Api Logout Appliance
	Run keyword unless	${Logout_response['status_code']}== 204    Fail    "Unable to Logout"
	Log To Console    \n\nLogged_Out from Appliance as ${admin_credentials['userName']}
    
	${Login_response}     Fusion Api Login Appliance    ${APPLIANCE_IP}        ${serveradmin}
	Run keyword unless	${Login_response[0]['status_code']}== 200    Fail    "Unable to Login"
	Log To Console    \n\nLogged in as ${serveradmin['userName']}
    
3. Aside Enable Port Monitoring with Unauthorized User

    ${resp}=    Configuring Port Monitoring in LI   ${interconnects[0]}    ${analyzer_port}    true	${LIA}
    Log to Console  ${resp}
    Run Keyword If  ${resp['status_code']} !=401    fail    Warning !!! Unauthorized user have access for Port Monitor ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    
    
4. Aside Log-out from the appliance

	${Logout_response}		Fusion Api Logout Appliance
	Run keyword unless	${Logout_response['status_code']}== 204    Fail    "Unable to Logout"
	Log To Console    \n\nLogged_Out from Appliance as serveradmin
    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}


5. Aside Positive : Enable Port Monitoring with Authorized User using port Q2.3

    ${resp}=    Configuring Port Monitoring in LI   ${interconnects[0]}    ${analyzer_port}    true	${LIA}
    Run Keyword If  ${resp['status_code']} !=202    fail    Port Monitoring failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     200s    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring !!
    Verify Port Monitoring in IC     ${analyzer_port}  ${analyzer_dport}    ${interconnects[0]}
   
    
6. Aside Negative : Create Uplinkset using the analyzerPort Q2.3

    ${li_uri} = 	Get LI URI   ${LE}-${LIGA}
	${us1} = 		Copy Dictionary	${us['us-eth']}
	${body} = 		Build US body 	${us1}	${li_uri}
    Log to Console  ${body}
	${resp} = 		Fusion Api Create Uplink Set	body=${body}
    Run Keyword If  ${resp['status_code']} ==400    Log to Console  As expected Uplink set is not able to created using analyzer port
    Sleep      ${pm_timer}

    
7. Aside Negative : Enable Port Monitoring with uplink port in the Uplinkset

    ${resp}=    Configuring Port Monitoring in LI   ${interconnects[0]}    ${used_uplink_port}     true	${LIA}
    Run Keyword If  ${resp['status_code']} ==202    fail    Enabling Port Monitor is succeed for Uplinkport for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    Sleep      ${pm_timer}


8. Aside Negative : Enable Port Monitoring with an uplink port that is an Fiber channel US using port "Q1"

   ${resp}=    Configuring Port Monitoring in LI   ${interconnects[0]}    ${fc_uplink_port}   true	${LIA}
   Log to Console      ${resp}     ${\n}   
   Run Keyword If  ${resp['status_code']} !=400    fail   Enabling Port Monitor is Success for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}


9. Aside Negative : Enable Port Monitoring with a stacking port as the analyzerPort

    ${resp}=    Configuring Port Monitoring in LI   ${interconnects[0]}    ${stacking_port}    true	${LIA}
    Run Keyword If  ${resp['status_code']} ==202    fail    As Expected Enabling Port Monitor is failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    Sleep      ${pm_timer}
    
10. Aside Positive : Disable Port Monitoring with Authorized Users

    ${resp}=    Configuring Port Monitoring in LI   ${interconnects[0]}    ${analyzer_port}    false	${LIA}
    Run Keyword If  ${resp['status_code']} !=202    fail    Failed to Disable Port Monitor for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     ${pm_timer}    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring !!!

11. Aside Switch from ports Q2.3 to Q6

    ${resp}=    Configuring Port Monitoring in LI   ${interconnects[0]}    ${analyzer_port_2}    true	${LIA}
    Run Keyword If  ${resp['status_code']} !=202    fail    Swirching to port & Enabling Port Monitor is failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     300s    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring !!!
    
    Verify Port Monitoring in IC     ${analyzer_port_2}  ${analyzer_dport}  ${interconnects[0]}
    
12. Aside Disable Port Monitoring with the port Q6

    ${resp}=    Configuring Port Monitoring in LI   ${interconnects[0]}    ${analyzer_port_2}    false	${LIA}
    Run Keyword If  ${resp['status_code']} !=202    fail    Swirching to port & Enabling Port Monitor is failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     ${pm_timer}    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring !!!
    
13. Aside Switch the ports from Port Q6 to Q2.4

    ${resp}=    Configuring Port Monitoring in LI   ${interconnects[0]}    ${analyzer_port_3}    true	${LIA}
    Run Keyword If  ${resp['status_code']} !=202    fail    Swirching to port & Enabling Port Monitor is failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     ${pm_timer}    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring !!!
    Verify Port Monitoring in IC     ${analyzer_port_3}  ${analyzer_dport}  ${interconnects[0]}

14. Aside Disable the port monitoring with port Q4.1

    ${resp}=    Configuring Port Monitoring in LI   ${interconnects[0]}    ${analyzer_port_3}    false	${LIA}
    Run Keyword If  ${resp['status_code']} !=202    fail    Swirching to port & Enabling Port Monitor is failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     ${pm_timer_q5}    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring !!! 
    
15. Aside Switch the ports from Port Q2.4 to Q2.3

    ${resp}=    Configuring Port Monitoring in LI   ${interconnects[0]}    ${analyzer_port}    true	${LIA}
    Run Keyword If  ${resp['status_code']} !=202    fail    Swirching to port & Enabling Port Monitor is failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     ${pm_timer_q5}    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring !!!
    Verify Port Monitoring in IC     ${analyzer_port}  ${analyzer_dport}    ${interconnects[0]}
    
16. Aside Disable the port monitoring with port Q4.4

    ${resp}=    Configuring Port Monitoring in LI   ${interconnects[0]}    ${analyzer_port}    false	${LIA}
    Run Keyword If  ${resp['status_code']} !=202    fail    Swirching to port & Enabling Port Monitor is failed for ${LI}\nErrorCode:${resp['errorCode']}\nMessage:${resp['message']}
    ${task} =   Wait For Task   ${resp}     ${pm_timer_q5}    2s
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    Configure port monitoring creation failed\nTaskErrorCode:${task['taskErrors'][0]['errorCode']}\nTaskStatus:${task['taskErrors'][0]['message']}
    ...         ELSE    Log to console and logfile  \n Successfully configured the port monitoring !! 

***keywords***

Teardown
	Set Log Level	TRACE
	Log to console and logfile	[TEARDOWN]
#	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
	Power off ALL Servers
	Remove All Server Profiles
    Remove All LEs
#	Remove All Logical Enclosures
	Remove ALL Enclosure Groups
	Remove ALL LIGs
    Remove All Network Sets
	Remove ALL Ethernet Networks
	Remove ALL FCoE Networks
	Remove ALL FC Networks
	Remove ALL Users

Suite Teardown Tasks
	[Documentation]	Returns appliance to a 'clean' state by removing all resources\enclosures
	Log to console and logfile	[TEARDOWN]
	Run Keyword If All Tests Passed    Power off ALL Servers
	Run Keyword If All Tests Passed    Remove All Server Profiles
	Run Keyword If All Tests Passed    Remove All Logical Enclosures
	Run Keyword If All Tests Passed    Remove ALL Enclosure Groups
	Run Keyword If All Tests Passed    Remove ALL LIGs
	Run Keyword If All Tests Passed    Remove ALL LS
	Run Keyword If All Tests Passed    Remove ALL LSGs
	Run Keyword If All Tests Passed    Remove ALL Ethernet Networks
	Run Keyword If All Tests Passed    Remove ALL FC Networks
	Run Keyword If All Tests Passed    Remove ALL FCoE Networks
	Run Keyword If All Tests Passed    Remove ALL Network Sets
	Run Keyword If All Tests Passed    Remove ALL Users
    
Suite Setup Tasks

	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    ${frame_in} =	Get Variable Value	${frame}	None
	${frame_in} =	Set Variable If	${frame_in} != None	${frame_in}	3
	Set Suite Variable	${frame}	${frame_in}

	# Creating the Ethernet networks
	:FOR	${net}	IN	@{ethernet_network}
    \   ${Response}     fusion api create ethernet network		${net}
    \   Log to Console      ${Response}
	\   Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Create Ethernet network"
    Log to console and logfile		Ethernet Networks created success
	
	${fc_networks}=	Get Variable Value	${fcnets}
	Run Keyword If	${fc_networks} is not ${null}    Add FC Networks from variable		${fc_networks}

	#Create LIG, EG and LE

	${network}=	Fusion Api Get Ethernet Networks
	${lig_body}=	set_networkuri_lig	${Lig_tbird_Aside_Enc${frame}}	${network}
	${fc_network}=	Fusion Api Get FC Networks
	${lig_body}=	set_networkuri_lig	${Lig_tbird_Aside_Enc${frame}}	${fc_network}
	Log to Console	${lig_body}	${\n}
	${ligs}=  Create LIG TBird Payload   ${lig_body}
	
	${resp}=  fusion api create lig     ${ligs}
	Log to Console	${resp}	${\n}
	Sleep    50
	Run Keyword for List	${enc_groups_aside}	Add Enclosure Group from variable
	Add Logical Enclosure from variable		${les[0]}
	Sleep	${le_timer}

