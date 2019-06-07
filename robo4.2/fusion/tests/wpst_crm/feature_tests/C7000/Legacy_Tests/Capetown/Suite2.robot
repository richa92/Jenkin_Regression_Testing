*** Settings ***
Documentation      Test cases for Capetown that involve BFS and 362/367

Library             FusionLibrary
Library             RoboGalaxyLibrary
Library				SSHLibrary
Library				Telnet
Library				String
Library             data_variables
Variables           data_variables.py
Resource			../../../../resources/resource.txt

Suite Teardown    Cleanup For Suite

*** Test Cases ***
1.Create SessionID through API
	Set Log Level    TRACE
    ${Login_response} =    Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	Run keyword unless    ${Login_response[0]['status_code']}== 200    Fail    ${Login_response[0]['message']}
	Log to console and logfile    Test Step-1 completed successfully

2.Code to get uris of all the resources.
    ${eth_resp} = 	Fusion Api Get Ethernet Networks    param=?filter="'name'=='${Enet_body['name']}'"
    Set Global Variable    ${enet_uri}    ${eth_resp['members'][0]['uri']}
	Log to console and logfile    The ethernet network uri is ${enet_uri}
	
	:FOR	${x}	IN RANGE	1	7
	\    ${fcda_resp} = 	Fusion Api Get FC Networks    param=?filter="'name'=='FC_da${x}'"
	\    Set Global Variable    ${FC_da${x}_uri}    ${fcda_resp['members'][0]['uri']}
	\    Log to console and logfile    The fc network FC_da${x} uri is ${FC_da${x}_uri}
	
	:FOR	${x}	IN RANGE	1	7
	\    ${fcfa_resp} = 	Fusion Api Get FC Networks    param=?filter="'name'=='FC_fa${x}'"
	\    Set Global Variable    ${FC_fa${x}_uri}    ${fcfa_resp['members'][0]['uri']}
	\    Log to console and logfile    The fc network FC_fa${x} uri is ${FC_fa${x}_uri}
	
	:FOR	${x}	IN RANGE	1	7
	\    Append To List    ${lig_us_body1[${x}]['networkUris']}    ${FC_da${x}_uri}
	:FOR	${x}	IN RANGE	1	7
	\    Append To List    ${lig_us_body1[${x}+6]['networkUris']}    ${FC_fa${x}_uri}
	Append To List    ${lig_us_body1[0]['networkUris']}    ${enet_uri}
	Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
	
	${enc_resp}=    Fusion Api Import Server Hardware Type For Enclosure    ${Preview_body}    ${Preview_uri}
	${interconnectMapTemplate}      Set Variable    ${enc_resp['logicalInterconnectGroup']['interconnectMapTemplate']}
	Set Global Variable   ${interconnectMapTemplate_Global}    ${interconnectMapTemplate} 
	Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
	
	${lig_resp} = 	Fusion Api Get Lig    param=?filter="'name'=='${lig_body1['name']}'"
    Set Global Variable    ${LIG_uri}    ${lig_resp['members'][0]['uri']}
	Log to console and logfile    The LIG uri is ${LIG_uri}
	
	${eg_resp} = 	Fusion Api Get Enclosure Groups    param=?filter="'name'=='${eg_body1['name']}'"
    Set Global Variable    ${EG_uri}    ${eg_resp['members'][0]['uri']}
	Log to console and logfile    The EG uri is ${EG_uri}
	
	${li_uri} = 	Get LI URI   ${Enclosure_Name}-${lig_body1['name']}
    Set Global Variable    ${LI_uri}    ${li_uri}
	Log to console and logfile    The LI uri is ${LI_uri}
	
	${enc_resp} = 	Fusion Api Get Enclosures    param=?filter="'name'=='${Enclosure_Name}'"
    Set Global Variable    ${ENC_uri}    ${enc_resp['members'][0]['uri']}
	Log to console and logfile    The enclosure uri is ${ENC_uri}
	
    :FOR	${x}	IN RANGE	1	4
	\    ${sh_resp} = 	Fusion Api Get Server Hardware    param=?filter="'name'=='${Enclosure_Name}, bay ${Server_bays[${x}-1]}'"
    \    Set Global Variable    ${sh_uri_${x}}    ${sh_resp['members'][0]['uri']}
	\    Log to console and logfile    The server hardware ${x} uri is ${sh_uri_${x}}
		
	:FOR	${x}	IN RANGE	1	4
	\    ${sp_resp} = 	Fusion Api Get Server Profiles    param=?filter="'name'=='SP_${x}'"
    \    Set Global Variable    ${SP_${x}_uri}    ${sp_resp['members'][0]['uri']}
	\    Log to console and logfile    The server profile ${x} uri is ${SP_${x}_uri}
*** Comments ***
Boot From SAN	
    ${sh_resp} = 	Fusion Api Get Server Hardware    param=?filter="'name'=='${Enclosure_Name}, bay ${Server_bays[3]}'"
    Set Global Variable    ${sh_uri}    ${sh_resp['members'][0]['uri']} 
	Set to Dictionary    ${SP_body2}    serverHardwareUri    ${sh_uri}
	Set to Dictionary    ${SP_body2}    enclosureGroupUri    ${sh_resp['members'][0]['serverGroupUri']}
	Set to Dictionary    ${SP_body2}    serverHardwareTypeUri    ${sh_resp['members'][0]['serverHardwareTypeUri']}
	Set To Dictionary    ${SP_body2}    name    sp4
	
	:FOR	${x}	IN RANGE	0	4 
	\   ${sh_resp} 	  fusion_api_get_fc_networks    param=?filter="'name'=='${FCnets_bfs[${x}]}'"
	\	Set to Dictionary    ${SP_body2['connections'][0]}    networkUri    ${sh_resp['members'][0]['uri']}
	\	Set to Dictionary    ${SP_body2['connections'][0]['boot']['targets'][0]}    arrayWwpn    ${arrayWwpn[${x}]}    
	\	${resp} =    Fusion Api Create Server Profile    ${SP_body2}
	\	Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\	${task} =	Wait For Task 	${resp} 	300s	30s
	\	${body} = 	Create Dictionary	powerState=On
	     ...							powerControl=MomentaryPress
	\   ${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri}
	\	${task} =	Wait For Task 	${resp}    240s    10s
	\	Log to console and logfile    powered on successfully
	\	${uri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri
	\	Set Global Variable    ${SP_uri}    ${uri}
	\	Log to console and logfile    ${SP_uri}
	\	Sleep    ${Server_power_on_sleep_time}    
	
	\	${output}=    Get Linux LUN Count    ${oa_details}    ${Server_bay_num}    ${bfs_server_details}   
	\	Log to console and logfile    ${output}
	\   Run keyword unless    ${output} > 0    Fail    Log to console and logfile    The count of available LUN is ${output}
	
	\	${body} = 	Create Dictionary	powerState=Off
	     ...							powerControl=PressAndHold
	\   ${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri}
	\	${task} =	Wait For Task 	${resp}    240s    10s
	\	Fusion Api Delete Server Profile    sp4	
	\	sleep    100s
	\	Log to console and logfile    Server profile deleted successfully
	
	Log to console and logfile    Boot From SAN checked successfully.
*** Test Cases ***
#Test case - 362/367
10.Deleting the FC networks
	${Response}     fusion api delete fc network    FC_da1
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	${task} =	Wait For Task 	${Response} 	120s	2s
	${Response}     fusion api delete fc network    FC_da4
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	${task} =	Wait For Task 	${Response} 	120s	2s
	${Response}     fusion api delete fc network    FC_fa1
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	${task} =	Wait For Task 	${Response} 	120s	2s
	${Response}     fusion api delete fc network    FC_fa4
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	${task} =	Wait For Task 	${Response} 	120s	2s
	Sleep    120s
	
362.10A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 0    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}

11.Deleting SP_1
    ${sh_resp} = 	Fusion Api Get Server Hardware    param=?filter="'name'=='${Enclosure_Name}, bay ${Server_bays[0]}'"
    Set Global Variable    ${sh_uri_1}    ${sh_resp['members'][0]['uri']}
	${body} = 	Create Dictionary	powerState=Off
	...								powerControl=PressAndHold
	${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri_1}
	${task} =	Wait For Task 	${resp} 	120s	10s
	Log to console and logfile    Server powered off successfully.
	${resp}=    Fusion Api Get Server Profiles    param=?filter="'name'=='SP_1'
	Set Global Variable    ${sp_uri}    ${resp['members'][0]['uri']}
	${resp}=    Fusion Api Delete Server Profile    SP_1    ${sp_uri}
	${task} =	Wait For Task    ${resp} 	300s	30s
	Log to console and logfile    Server profile deleted successfully 

13.Create FC-DA Networks
	Log to Console    \n@{fc_connection['sp1']}
    Set To Dictionary    ${Fc_body1}    fabricType    DirectAttach
	:FOR	${x}	IN    @{fc_connection['sp1']}
	\    Log to console    \n${x}
	\    Set To Dictionary    ${Fc_body1}    name    FC_da${x}
	\    Log to console   \nfcbody is ${Fc_body1}
	\    ${resp} =    Fusion Api Create Fc Network    ${Fc_body1}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${uri} =    Get From Dictionary    ${resp['associatedResource']}    resourceUri
	\    Set Global Variable    ${FC_danew_${x}_uri}    ${uri}
	\    Log to console and logfile    ${FC_danew_${x}_uri}

14.Create FC-FA Networks
    Log to Console    \n@{fc_connection['sp1']}
    Set To Dictionary    ${Fc_body1}    fabricType    FabricAttach
	:FOR	${x}	IN    @{fc_connection['sp1']}
	\    Log to console    \n${x}
	\    Set To Dictionary    ${Fc_body1}    name    FC_fa${x}
	\    Log to console   \nfcbody is ${Fc_body1}
	\    ${resp} =    Fusion Api Create Fc Network    ${Fc_body1}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${uri} =    Get From Dictionary    ${resp['associatedResource']}    resourceUri
	\    Set Global Variable    ${FC_fanew_${x}_uri}    ${uri}
	\    Log to console and logfile    ${FC_fanew_${x}_uri}

15.Edit LIG and add networks 
	Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    :FOR	${x}	IN    @{fc_connection['sp1']}
    \    Remove From List    ${lig_us_body1[${x}]['networkUris']}    0
	\    Append To List    ${lig_us_body1[${x}]['networkUris']}    ${FC_danew_${x}_uri}
	:FOR	${x}	IN    @{fc_connection['sp1']}
	\    Remove From List    ${lig_us_body1[${x}+6]['networkUris']}    0
	\    Append To List    ${lig_us_body1[${x}+6]['networkUris']}    ${FC_fanew_${x}_uri}
	Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
	Log to Console    \nlig body is ${lig_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited successfully
    ${task} =	Wait For Task 	${resp} 	120s    2s
    Sleep    120s

16.LI update
    Perform an LI Update From Group    ${LI_uri}
	Log to console and logfile    LI updated from group successfully.
	Sleep    30s

17.Create Server Profile 1
    Set To Dictionary    ${SP_body1['connections'][0]}    networkUri    ${enet_uri}
    ${sh_resp} = 	Fusion Api Get Server Hardware    param=?filter="'name'=='${Enclosure_Name}, bay ${Server_bays[0]}'"
    Set Global Variable    ${sh_uri_1}    ${sh_resp['members'][0]['uri']} 
	Set to Dictionary    ${SP_body1}    serverHardwareUri    ${sh_uri_1}
	Set to Dictionary    ${SP_body1}    enclosureGroupUri    ${sh_resp['members'][0]['serverGroupUri']}
	Set to Dictionary    ${SP_body1}    serverHardwareTypeUri    ${sh_resp['members'][0]['serverHardwareTypeUri']}
	Set Network Uri For FCs Connections    1
	Set To Dictionary    ${SP_body1}    name    SP_1
	${resp} =    Fusion Api Create Server Profile    ${SP_body1}
	Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	${task} =	Wait For Task 	${resp} 	300s    30s
	${uri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri
	Set Global Variable    ${SP_1_uri}    ${uri}
	Log to console and logfile    ${SP_1_uri}  
	${body} = 	Create Dictionary	powerState=On
	     ...							powerControl=MomentaryPress
	${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri_1}
	${task} =	Wait For Task 	${resp}    240s    10s 
    Sleep    ${Server_power_on_sleep_time}	

362.18) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}
	
19.Deleting the FC networks
	${Response}     fusion api delete fc network    FC_da2
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	${task} =	Wait For Task 	${Response} 	120s	2s
	${Response}     fusion api delete fc network    FC_da5
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	${task} =	Wait For Task 	${Response} 	120s	2s
	${Response}     fusion api delete fc network    FC_fa2
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	${task} =	Wait For Task 	${Response} 	120s	2s
	${Response}     fusion api delete fc network    FC_fa5
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	${task} =	Wait For Task 	${Response} 	120s	2s
	Sleep    120s

362.20) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 0    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 

21.Deleting SP_2
    ${sh_resp} = 	Fusion Api Get Server Hardware    param=?filter="'name'=='${Enclosure_Name}, bay ${Server_bays[1]}'"
    Set Global Variable    ${sh_uri_2}    ${sh_resp['members'][0]['uri']}
	${body} = 	Create Dictionary	powerState=Off
	...								powerControl=PressAndHold
	${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri_2}
	${task} =	Wait For Task 	${resp}    120s    10s
	Log to console and logfile    Server powered off successfully.
	${resp}=    Fusion Api Get Server Profiles    param=?filter="'name'=='SP_2'
	Set Global Variable    ${sp_uri}    ${resp['members'][0]['uri']}
	${resp}=    Fusion Api Delete Server Profile    SP_2    ${sp_uri}
	${task} =	Wait For Task    ${resp} 	300s	30s
	Log to console and logfile    Server profile deleted successfully 

22.Create FC-DA Networks
	Log to Console    \n@{fc_connection['sp2']}
    Set To Dictionary    ${Fc_body1}    fabricType    DirectAttach
	:FOR	${x}	IN    @{fc_connection['sp2']}
	\    Log to console    \n${x}
	\    Set To Dictionary    ${Fc_body1}    name    FC_da${x}
	\    Log to console   \nfcbody is ${Fc_body1}
	\    ${resp} =    Fusion Api Create Fc Network    ${Fc_body1}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${uri} =    Get From Dictionary    ${resp['associatedResource']}    resourceUri
	\    Set Global Variable    ${FC_danew_${x}_uri}    ${uri}
	\    Log to console and logfile    ${FC_danew_${x}_uri}

23.Create FC-FA Networks
    Log to Console    \n@{fc_connection['sp2']}
    Set To Dictionary    ${Fc_body1}    fabricType    FabricAttach
	:FOR	${x}	IN    @{fc_connection['sp2']}
	\    Log to console    \n${x}
	\    Set To Dictionary    ${Fc_body1}    name    FC_fa${x}
	\    Log to console   \nfcbody is ${Fc_body1}
	\    ${resp} =    Fusion Api Create Fc Network    ${Fc_body1}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${uri} =    Get From Dictionary    ${resp['associatedResource']}    resourceUri
	\    Set Global Variable    ${FC_fanew_${x}_uri}    ${uri}
	\    Log to console and logfile    ${FC_fanew_${x}_uri}

24.Edit LIG and add networks 
	Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    :FOR	${x}	IN    @{fc_connection['sp2']}
    \    Remove From List    ${lig_us_body1[${x}]['networkUris']}    0
	\    Append To List    ${lig_us_body1[${x}]['networkUris']}    ${FC_danew_${x}_uri}
	:FOR	${x}	IN    @{fc_connection['sp2']}
	\    Remove From List    ${lig_us_body1[${x}+6]['networkUris']}    0
	\    Append To List    ${lig_us_body1[${x}+6]['networkUris']}    ${FC_fanew_${x}_uri}
	Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
	Log to Console    \nlig body is ${lig_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited successfully
	${task} =	Wait For Task 	${resp} 	120s    2s
	Sleep    120s

25.LI update
    Perform an LI Update From Group    ${LI_uri}
	Log to console and logfile    LI updated from group successfully.
	Sleep    100s

26.Create Server Profile 2
    Set To Dictionary    ${SP_body1['connections'][0]}    networkUri    ${enet_uri}
    ${sh_resp} = 	Fusion Api Get Server Hardware    param=?filter="'name'=='${Enclosure_Name}, bay ${Server_bays[1]}'"
    Set Global Variable    ${sh_uri_2}    ${sh_resp['members'][0]['uri']} 
	Set to Dictionary    ${SP_body1}    serverHardwareUri    ${sh_uri_2}
	Set to Dictionary    ${SP_body1}    enclosureGroupUri    ${sh_resp['members'][0]['serverGroupUri']}
	Set to Dictionary    ${SP_body1}    serverHardwareTypeUri    ${sh_resp['members'][0]['serverHardwareTypeUri']}
	Set Network Uri For FCs Connections    2
	Set To Dictionary    ${SP_body1}    name    SP_2
	${resp} =    Fusion Api Create Server Profile    ${SP_body1}
	Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	${task} =	Wait For Task 	${resp} 	300s    30s
	${uri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri
	Set Global Variable    ${SP_2_uri}    ${uri}
	Log to console and logfile    ${SP_2_uri}     
	${body} = 	Create Dictionary	powerState=On
	...						        powerControl=MomentaryPress
	${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri_2}
	${task} =	Wait For Task 	${resp}    240s    10s 
	Sleep    ${Server_power_on_sleep_time}

362.27) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 

28.Deleting the FC networks
	${Response}     fusion api delete fc network    FC_da3
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	${task} =	Wait For Task 	${Response} 	120s	2s
	${Response}     fusion api delete fc network    FC_da6
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	${task} =	Wait For Task 	${Response} 	120s	2s
	${Response}     fusion api delete fc network    FC_fa3
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	${task} =	Wait For Task 	${Response} 	120s	2s
	${Response}     fusion api delete fc network    FC_fa6
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	${task} =	Wait For Task 	${Response} 	120s	2s
	Sleep    120s

362.29) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 0    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}

30. Deleting SP_3
    ${sh_resp} = 	Fusion Api Get Server Hardware    param=?filter="'name'=='${Enclosure_Name}, bay ${Server_bays[2]}'"
    Set Global Variable    ${sh_uri_3}    ${sh_resp['members'][0]['uri']}
	${body} = 	Create Dictionary	powerState=Off
	...								powerControl=PressAndHold
	${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri_3}
	${task} =	Wait For Task 	${resp}    120s    10s
	Log to console and logfile    Server powered off successfully.
	${resp}=    Fusion Api Get Server Profiles    param=?filter="'name'=='SP_3'
	Set Global Variable    ${sp_uri}    ${resp['members'][0]['uri']}
	${resp}=    Fusion Api Delete Server Profile    SP_3    ${sp_uri}
	${task} =	Wait For Task    ${resp} 	300s	30s
	Log to console and logfile    Server profile deleted successfully 

31.Create FC-DA Networks
	Log to Console    \n@{fc_connection['sp3']}
    Set To Dictionary    ${Fc_body1}    fabricType    DirectAttach
	:FOR	${x}	IN    @{fc_connection['sp3']}
	\    Log to console    \n${x}
	\    Set To Dictionary    ${Fc_body1}    name    FC_da${x}
	\    Log to console   \nfcbody is ${Fc_body1}
	\    ${resp} =    Fusion Api Create Fc Network    ${Fc_body1}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${uri} =    Get From Dictionary    ${resp['associatedResource']}    resourceUri
	\    Set Global Variable    ${FC_danew_${x}_uri}    ${uri}
	\    Log to console and logfile    ${FC_danew_${x}_uri}

32.Create FC-FA Networks
    Log to Console    \n@{fc_connection['sp3']}
    Set To Dictionary    ${Fc_body1}    fabricType    FabricAttach
	:FOR	${x}	IN    @{fc_connection['sp3']}
	\    Log to console    \n${x}
	\    Set To Dictionary    ${Fc_body1}    name    FC_fa${x}
	\    Log to console   \nfcbody is ${Fc_body1}
	\    ${resp} =    Fusion Api Create Fc Network    ${Fc_body1}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${uri} =    Get From Dictionary    ${resp['associatedResource']}    resourceUri
	\    Set Global Variable    ${FC_fanew_${x}_uri}    ${uri}
	\    Log to console and logfile    ${FC_fanew_${x}_uri}

33.Edit LIG and add networks 
	Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    :FOR	${x}	IN    @{fc_connection['sp3']}
    \    Remove From List    ${lig_us_body1[${x}]['networkUris']}    0
	\    Append To List    ${lig_us_body1[${x}]['networkUris']}    ${FC_danew_${x}_uri}
	:FOR	${x}	IN    @{fc_connection['sp3']}
	\    Remove From List    ${lig_us_body1[${x}+6]['networkUris']}    0
	\    Append To List    ${lig_us_body1[${x}+6]['networkUris']}    ${FC_fanew_${x}_uri}
	Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
	Log to Console    \nlig body is ${lig_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited successfully
	${task} =	Wait For Task 	${resp} 	120s    2s
	Sleep    120s

34.LI update
    Perform an LI Update From Group    ${LI_uri}
	Log to console and logfile    LI updated from group successfully.
	Sleep    100s

35.Create Server Profile 3
    Set To Dictionary    ${SP_body1['connections'][0]}    networkUri    ${enet_uri}
    ${sh_resp} = 	Fusion Api Get Server Hardware    param=?filter="'name'=='${Enclosure_Name}, bay ${Server_bays[2]}'"
    Set Global Variable    ${sh_uri_3}    ${sh_resp['members'][0]['uri']} 
	Set to Dictionary    ${SP_body1}    serverHardwareUri    ${sh_uri_3}
	Set to Dictionary    ${SP_body1}    enclosureGroupUri    ${sh_resp['members'][0]['serverGroupUri']}
	Set to Dictionary    ${SP_body1}    serverHardwareTypeUri    ${sh_resp['members'][0]['serverHardwareTypeUri']}
	Set Network Uri For FCs Connections    3
	Set To Dictionary    ${SP_body1}    name    SP_3
	${resp} =    Fusion Api Create Server Profile    ${SP_body1}
	Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	${task} =	Wait For Task 	${resp} 	300s    30s
	${uri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri
	Set Global Variable    ${SP_3_uri}    ${uri}
	Log to console and logfile    ${SP_3_uri}     
	${body} = 	Create Dictionary	powerState=On
	...							powerControl=MomentaryPress
	${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri_3}
	${task} =	Wait For Task 	${resp}    240s    10s 
    Sleep    ${Server_power_on_sleep_time}

362.36) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}
	
*** Keywords ***

Set Network Uri For FC Connections
    [Documentation]    Sets the Fc network connection uris for the given server.
	[Arguments]		${con_num}
	${con_new_num}=    Evaluate    ${con_num}+3
	:FOR	${y}	IN RANGE	1	5
	\    Run Keyword If    ${y}==1    Set To Dictionary    ${SP_body1['connections'][${y}]}    networkUri    ${FC_da${con_num}_uri}
	\    Run Keyword If    ${y}==2    Set To Dictionary    ${SP_body1['connections'][${y}]}    networkUri    ${FC_da${con_new_num}_uri}
	\    Run Keyword If    ${y}==3    Set To Dictionary    ${SP_body1['connections'][${y}]}    networkUri    ${FC_fa${con_num}_uri}
	\    Run Keyword If    ${y}==4    Set To Dictionary    ${SP_body1['connections'][${y}]}    networkUri    ${FC_fa${con_new_num}_uri}
	
Set Network Uri For FCs Connections
	[Documentation]    Sets the Fc network connection uris for the given server.
	[Arguments]		${con_num}
	${con_new_num}=    Evaluate    ${con_num}+3
	:FOR	${y}	IN RANGE	1	5
	\    Run Keyword If    ${y}==1    Set To Dictionary    ${SP_body1['connections'][${y}]}    networkUri    ${FC_danew_${con_num}_uri}
	\    Run Keyword If    ${y}==2    Set To Dictionary    ${SP_body1['connections'][${y}]}    networkUri    ${FC_danew_${con_new_num}_uri}
	\    Run Keyword If    ${y}==3    Set To Dictionary    ${SP_body1['connections'][${y}]}    networkUri    ${FC_fanew_${con_num}_uri}
	\    Run Keyword If    ${y}==4    Set To Dictionary    ${SP_body1['connections'][${y}]}    networkUri    ${FC_fanew_${con_new_num}_uri}

	
Get Windows Server And Gateway IP 
	[Documentation]    Gets the valid ip and gateway ip of the server.
	[Arguments]		${oa_details}    ${Server_bay_num}
	SSHLibrary.Open Connection    ${oa_details['oa_ip']}
	SSHLibrary.Login    ${oa_details['username']}    ${oa_details['password']}
	
	SSHLibrary.Write    connect server ${Server_bay_num}
	Sleep    5
	SSHLibrary.Read Until    hpiLO->
	SSHLibrary.Write    stop /system1/oemhp_VSP1
	Sleep    5
	SSHLibrary.Write    vsp
	Sleep    5
	SSHLibrary.Read Until    SAC>
	Sleep    5
	SSHLibrary.Write    i
	Sleep    5
	${output1}=    SSHLibrary.Read
	${cmd_output}=    Get Regexp Matches    ${output1}    192\\.\\d+\\.\\d+\\.\\d+
	${Server_IP}=    convert_unicode_to_string    ${cmd_output[0]}
	${Gateway_IP}=    convert_unicode_to_string    ${cmd_output[1]}
	SSHLibrary.Close All Connections
	[Return]    ${Server_IP}    ${Gateway_IP}
	
Get Windows LUN Count
    [Documentation]    Gets the available lun counts from the server.
	[Arguments]		${Server_IP}    ${win_server_details}
	Telnet.Open Connection    ${Server_IP}    prompt=>     timeout=20s
	Sleep    5
	Telnet.Login    ${win_server_details['username']}    ${win_server_details['password']}    login_prompt=login:    password_prompt=password:
	Sleep    5
	Telnet.Write    powershell.exe Get-Disk -FriendlyName *3PARdata*
	Sleep    10
	${stdout} =  Telnet.Read
	#${list_disk}=    Telnet.Execute Command    list disk
	Log to console    \nlistdisk is ${stdout}
	${lines}=    Get Lines Containing String    ${stdout}    3PARdata
	${count}=    Get Line Count    ${lines}
	Telnet.Close All Connections
	[Return]    ${count}

Get Linux LUN Count
    [Documentation]    Gets the available lun counts from the server.
	[Arguments]    ${oa_details}    ${Server_bay_num}    ${linux_server_details}
	SSHLibrary.Open Connection    ${oa_details['oa_ip']}
	SSHLibrary.Login    ${oa_details['username']}    ${oa_details['password']}
   
	SSHLibrary.Write    connect server ${Server_bay_num}
	Sleep    5
	SSHLibrary.Read Until    hpiLO->
	SSHLibrary.Write    stop /system1/oemhp_VSP1
	Sleep    5
	SSHLibrary.Write    vsp
	Sleep    5
	SSHLibrary.Read Until    login:
	SSHLibrary.Write    ${linux_server_details['username']}
	Sleep    5
	SSHLibrary.Read Until    Password:
	SSHLibrary.Write    ${linux_server_details['password']}
	Sleep    5
	SSHLibrary.Set Client Configuration    prompt=#
	SSHLibrary.Read Until Prompt
	
	SSHLibrary.Write    lsscsi | grep VV
	Sleep    5
	SSHLibrary.Set Client Configuration    prompt=#
	${list_disk}=    SSHLibrary.Read Until Prompt
	${lines}=    Get Lines Containing String    ${list_disk}    dev/sd
	${count}=    Get Line Count    ${lines}
	SSHLibrary.Write    exit
	SSHLibrary.Close All Connections
	[Return]    ${count}

OA CLI DEVICE POWERON
    [Documentation]    issues an POWERON command to the given Device\Bay.
    ...   {DEVICE} = <SERVER | INTERCONNECT>
    ...   {BAY} = desired bay for given device  { ALL | <bay number> [{ , | - } <bay number>]}
    [Arguments]	       ${OA_HOST}    ${OA_USER}		${OA_PASS}    ${DEVICE}    ${BAY}
    SSHLibrary.Open Connection     ${OA_HOST}    
    SSHLibrary.Login               ${OA_USER}     ${OA_PASS}
    SSHLibrary.Write    POWERON ${DEVICE} ${BAY}
	Sleep    5
    SSHLibrary.Close All Connections

OA CLI DEVICE POWEROFF
    [Documentation]    issues an POWEROFF command to the given Device\Bay.
    ...   {DEVICE} = <SERVER | INTERCONNECT>
    ...   {BAY} = desired bay for given device  { ALL | <bay number> [{ , | - } <bay number>]}
    [Arguments]	       ${OA_HOST}    ${OA_USER}		${OA_PASS}    ${DEVICE}    ${BAY}
    SSHLibrary.Open Connection     ${OA_HOST}     
    SSHLibrary.Login               ${OA_USER}     ${OA_PASS}
    SSHLibrary.Write    POWEROFF ${DEVICE} ${BAY}
	Sleep    5
    SSHLibrary.Close All Connections
	
Get LI URI
	[Arguments]		${li}
	${resp} = 	Fusion Api Get LI
	${l} = 	Get Length	${resp['members']}
	:FOR	${x}	IN RANGE	0	${l}
	\ 	Run Keyword If 	'${resp['members'][${x}]['name']}' != '${li}'		Continue For Loop
	\	${uri} = 	Get From Dictionary		${resp['members'][${x}]}	uri
	[Return]	${uri}
	
Perform an LI Update From Group
    [Arguments]       ${li}     ${timeout}=10 min    ${interval}=15s
    ${resp} =       Fusion Api Update from group    ${li}
    ${task} =       Wait For Task       ${resp}     ${timeout}        ${interval}
    ${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response    ${task}    ${valDict}
	
Login to OneView via REST	
	[Documentation]		Login to the appliance with the cred
	[Tags]  add   POSITIVE
	Set Log Level    TRACE
	${resp}     Fusion Api Login Appliance    ${appliance_IP}        ${admin_credentials}

Logout OneView via REST
	[Documentation]	log out from the appliance
	Fusion Api Logout Appliance
	
Cleanup For Suite	
	[Documentation]	Returns appliance to a 'clean' state by removing all resources\enclosures
	Log to console and logfile	[Cleanup]
	Login to OneView via REST
	Power off ALL Servers
	Remove All Server Profiles
	Remove ALL Enclosures
	Remove ALL Enclosure Groups
	Remove ALL LIGs
	Remove ALL Ethernet Networks
	Remove ALL FC Networks
