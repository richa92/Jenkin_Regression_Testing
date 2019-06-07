*** Settings ***
Documentation		F95 C7K 4K VLAN - 1. Bulk network creation
...                 F95 C7K 4K VLAN - 2. Ethernet and FCoE Dual Hop - maximum limit of 8192 defined
...					F95 C7K 4K VLAN - 3. FC/FCoE bridged (FCFA) separate limit of 255 defined not include in 8192 limitation
Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary
Variables		data_variables.py
Resource        resource.txt

Suite Setup    Cleanup For Suite
Suite Teardown    Cleanup For Suite

*** Test cases ***
### Pre-Conditions - Login to Appliance ###
1.Create SessionID through API
	Set Log Level    TRACE
    ${Login_response} =    Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	Run keyword unless	${Login_response[0]['status_code']}== 200    Fail    ${Login_response[0]['message']}
	Log to console and logfile    Test Step-1 completed successfully
	
### Test Case -1 ###	
1.Bulk Network Creation and Validation.
    ${create_resp1}=    Fusion Api Create Ethernet Bulk Networks    ${Bulk_enet_body}
    Run keyword unless	${create_resp1['status_code']}== 202    Fail    ${create_resp1['message']}
    ${task} =	Wait For Task 	${create_resp1} 	2000s	100s
	Log to console and logfile    Bulk networks A (1 to 4094) created successfully
    Set To Dictionary    ${Bulk_enet_body}    namePrefix    NETB
    ${create_resp2}=    Fusion Api Create Ethernet Bulk Networks    ${Bulk_enet_body}
    Run keyword unless	${create_resp2['status_code']}== 202    Fail    ${create_resp2['message']}
    ${task2} =	Wait For Task 	${create_resp2} 	2000s	100s
	Log to console and logfile    Bulk networks B (1 to 4094) created successfully

1A.Validation and proceed	
	${resp}=    Fusion Api Get Ethernet Networks
	Run keyword unless	${resp['total']}== 8188    Fail    ${resp['message']}
	
	:FOR	${x}	IN RANGE	1    5
	\    Set To Dictionary    ${Fcoe_body}    name    NET${x}
	\    ${resp} =    Fusion Api Create Fcoe Network    ${Fcoe_body}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	
	${error_resp} =    Fusion Api Create Ethernet Network    ${Enet_body}
	Run keyword unless	${error_resp['status_code']}== 400    Fail    ${error_resp['message']}
	Log to console and logfile    ${error_resp}
	Should Be Equal As Strings    ${error_resp['message']}    ${error_msg_1}	
	Log to console and logfile    Test case - 1 completed successfully
	
2.FCOE network validation
	Set To Dictionary    ${Fcoe_body}    name    NET
	${error_resp} =    Fusion Api Create Fcoe Network    ${Fcoe_body}
	Run keyword unless	${error_resp['status_code']}== 400    Fail    ${error_resp['message']}
	Log to console and logfile    ${error_resp}
	Should Be Equal As Strings    ${error_resp['message']}    ${error_msg_2}	
	Log to console and logfile    Test case - 2 completed successfully
	
3.Fc/Fcoe bridged - FCFA 255 limit validation
	:FOR	${x}	IN RANGE	1	256
	\    Set To Dictionary    ${Fc_body}    name    FCNET${x}
	\    ${resp} =    Fusion Api Create Fc Network    ${Fc_body}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	
	Set To Dictionary    ${Fc_body}    name    FCnet
	${error_resp} =    Fusion Api Create Fc Network    ${Fc_body}
	Run keyword unless	${error_resp['status_code']}== 400    Fail    ${error_resp['message']}
	Log to console and logfile    ${error_resp}
	Should Be Equal As Strings    ${error_resp['message']}    ${error_msg_3}	
	Log to console and logfile    Test case - 3 completed successfully