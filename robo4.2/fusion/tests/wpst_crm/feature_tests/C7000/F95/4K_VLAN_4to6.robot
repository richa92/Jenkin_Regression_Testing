*** Settings ***
Documentation		F95 C7K 4K VLAN - 4. LIG with uplink/internal networks can contain no more than 1000 Ethernet networks.
...                 F95 C7K 4K VLAN - 5. LI uplink/internal networks 1000 limitation; Port mirror XNET is not included in the maximum number of networks on VC LI.
...					F95 C7K 4K VLAN - 6. Delete network belongs to uplink set/internal networks will not cause consistence problem between LIG and LI.
Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary
Variables		data_variables.py
Resource        ../../../resources/resource.txt

*** Test cases ***
### Pre-Conditions - Login to Appliance ###
1.Create SessionID through API
	Set Log Level    TRACE
    ${Login_response} =    Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	Run keyword unless	${Login_response[0]['status_code']}== 200    Fail    ${Login_response[0]['message']}
	Log to console and logfile    Test Step-1 completed successfully

2.Creating LIG	
	${enc_resp}=    Fusion Api Import Server Hardware Type For Enclosure    ${Preview_body}    ${Preview_uri}
	${interconnectMapTemplate}      Set Variable    ${enc_resp['logicalInterconnectGroup']['interconnectMapTemplate']}
	Set Global Variable   ${interconnectMapTemplate_Global}    ${interconnectMapTemplate} 
	Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
	${resp_lig} = 	Fusion Api Create LIG	${lig_body1}
	Run keyword unless	${resp_lig['status_code']}== 202    Fail    ${resp_lig['message']}
	${task} =	Wait For Task 	${resp_lig} 	120s	2s
	Log to console and logfile    LIG created successfully
	${uri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri
	Set Global Variable    ${LIG_uri}    ${uri}
	Log to console and logfile    ${LIG_uri}
	
3.Creating EG	
	${Test_dict} =    Create Dictionary
	:FOR	${x}	IN RANGE    0    8
	\    ${permittedInterconnectTypeUri} =    Get From Dictionary    ${interconnectMapTemplate_Global['interconnectMapEntryTemplates'][${x}]}	permittedInterconnectTypeUri
	\    Run Keyword If    '${interconnectMapTemplate_Global['interconnectMapEntryTemplates'][${x}]['logicalLocation']['locationEntries'][0]['type']}'=='Bay'
	\    ...    Set To Dictionary    ${Test_dict}    ${interconnectMapTemplate_Global['interconnectMapEntryTemplates'][${x}]['logicalLocation']['locationEntries'][0]['relativeValue']}    ${permittedInterconnectTypeUri}
	\    Run Keyword If    '${interconnectMapTemplate_Global['interconnectMapEntryTemplates'][${x}]['logicalLocation']['locationEntries'][1]['type']}'=='Bay'
	\    ...    Set To Dictionary    ${Test_dict}    ${interconnectMapTemplate_Global['interconnectMapEntryTemplates'][${x}]['logicalLocation']['locationEntries'][1]['relativeValue']}    ${permittedInterconnectTypeUri}
	Log to console and logfile    ${Test_dict}    
	
	${Keys}=    Get Dictionary Keys    ${Test_dict}
	Log to console and logfile    ${Keys}
	${Values}=    Get Dictionary Values    ${Test_dict}
	Log to console and logfile    ${Values} 
	:FOR	${y}	IN RANGE	0    8
	\    Set To Dictionary    ${eg_body1['interconnectBayMappings'][${y}]}    interconnectBay    ${Keys[${y}]}
	\    Run Keyword If    '${Values[${y}]}' != 'None'    Set To Dictionary    ${eg_body1['interconnectBayMappings'][${y}]}    logicalInterconnectGroupUri    ${LIG_uri}
	Log to console and logfile    ${eg_body1}
	
	${eg_resp}=    Fusion Api Create Enclosure Group    ${eg_body1}
	Run keyword unless	${eg_resp['status_code']}== 201    Fail    ${eg_resp['message']}  
	Set Global Variable    ${EG_uri}    ${eg_resp['uri']}
	Log to console and logfile    EG created successfully
	
4.Importing Enclosure
	Set To Dictionary    ${enc_body1}    enclosureGroupUri    ${EG_uri}
    ${resp_enc}=    Fusion Api Add Enclosure    ${enc_body1}
    Run keyword unless	${resp_enc['status_code']}== 202    Fail    ${resp_lig['message']}
	${task} =	Wait For Task 	${resp_enc} 	500s	30s
	Log to console and logfile    Enclosure imported successfully

5.Creating 1001 networks	
	Set To Dictionary    ${Bulk_enet_body}    vlanIdRange    1-1001
	${create_resp1}=    Fusion Api Create Ethernet Bulk Networks    ${Bulk_enet_body}
    Run keyword unless	${create_resp1['status_code']}== 202    Fail    ${create_resp1['message']}
    ${task} =	Wait For Task 	${create_resp1} 	2000s	100s
	Log to console and logfile    Bulk networks A (1 to 1001) created successfully

6.Editing LIG to add 1000 internal networks	
	${Test_list} =    Create List
	:FOR	${x}	IN RANGE	1    1001
	\    ${resp} 	Fusion Api Get Ethernet Networks    param=?filter="'name'=='${Bulk_enet_body['namePrefix']}_${x}'"
	\    Append To List    ${Test_list}    ${resp['members'][0]['uri']}
	Set Global Variable    ${internalNetworkUris}    ${Test_list}
	Set To Dictionary    ${lig_body1}    internalNetworkUris    ${internalNetworkUris}
	${resp} = 	Fusion Api Edit Lig    ${lig_body1}    ${LIG_uri}
	${task} =	Wait For Task 	${resp} 	120s	2s
	Log to console and logfile    LIG edited successfully
	
7.Editing LIG to add the 1001st network and validating the error message
	${internalNetworkUris_1001} =	Copy List	${internalNetworkUris}
    ${resp} 	Fusion Api Get Ethernet Networks    param=?filter="'name'=='${Bulk_enet_body['namePrefix']}_1001'"
	Append To List    ${internalNetworkUris_1001}    ${resp['members'][0]['uri']}
	Set To Dictionary    ${lig_inet_body}    internalNetworkUris    ${internalNetworkUris_1001}
	${edit_resp} =    Fusion Api Import Server Hardware Type For Enclosure    ${lig_inet_body}    ${lig_inet_uri}
	Should Be Equal As Strings    ${edit_resp['message']}    ${error_msg_4}	
	Log to console and logfile    Test case - 4A completed successfully
	
8.Editing LIG to add an uplink set with 1001 networks and validating the error message.
    Remove From Dictionary    ${lig_body1}    internalNetworkUris
    Set To Dictionary    ${lig_us_body1}    networkUris    ${lig_inet_body['internalNetworkUris']}
    Append To List    ${lig_body1['uplinkSets']}    ${lig_us_body1}
	${edit_resp} =    Fusion Api Edit Lig    ${lig_body1}    ${LIG_uri}
	Sleep    20s
	${task_resp} =    Fusion Api Get Task    uri=${edit_resp['uri']}
	Run keyword unless	${task_resp['status_code']}== 200    Fail    ${task_resp['message']}
	Should Be Equal As Strings    ${task_resp['taskErrors'][0]['message']}    ${error_msg_5}
	Log to console and logfile    Test case - 4B completed successfully
	
9.LI update from Group
	${li_resp} =    Fusion Api Get Li
	Log to console and logfile    ${li_resp['members'][0]['uri']}
	Set Global Variable    ${LI_uri}    ${li_resp['members'][0]['uri']}
	${resp_update} =    Fusion Api Update From Group    ${LI_uri}
	Run keyword unless	${resp_update['status_code']}== 202    Fail    ${resp_update['message']}
	${task} =	Wait For Task 	${resp_update} 	300s	30s
	Log to console and logfile    LI updated from group successfully.
	
10.Edit LI to add 1001st network and validate the error message.	
    ${resp_li} =    Fusion Api Update LI Internal Networks    ${lig_inet_body['internalNetworkUris']}    ${LI_uri}
	Run keyword unless	${resp_li['status_code']}== 400    Fail    ${resp_li['message']}
	Should Be Equal As Strings    ${resp_li['message']}    ${error_msg_4}	
	Log to console and logfile    Test case - 5A completed successfully
	
11.Edit LI to add an uplink set with 1001 networks and validate the error message.
    Set To Dictionary    ${li_us_body1}    networkUris    ${lig_inet_body['internalNetworkUris']}
	${enc_uri} =    Get Enclosure Uri    ${Enclosure_Name}
	Set To Dictionary    ${li_us_body1['portConfigInfos'][0]['location']['locationEntries'][2]}    value    ${enc_uri}
	Set To Dictionary    ${li_us_body1}    logicalInterconnectUri    ${LI_uri}
	${resp_li} =    Fusion Api Create Uplink Set    ${li_us_body1}
	Run keyword unless	${resp_li['status_code']}== 400    Fail    ${resp_li['message']}
	Should Be Equal As Strings    ${resp_li['message']}    ${error_msg_5}	
	Log to console and logfile    Test case - 5B completed successfully
	
12.Create an uplink set with 1 ethernet network
    :FOR	${x}	IN RANGE	1000    -1    -1
	\    Remove From List	${li_us_body1['networkUris']}    ${x}
    ${resp} 	Fusion Api Get Ethernet Networks    param=?filter="'name'=='${Bulk_enet_body['namePrefix']}_${Tagged_VLAN}'"
    Insert Into List    ${li_us_body1['networkUris']}    0    ${resp['members'][0]['uri']}    
    Set To Dictionary    ${li_us_body1['portConfigInfos'][0]['location']['locationEntries'][0]}    value    ${normal_ports_f95[1]}
    ${resp_li} =    Fusion Api Create Uplink Set    ${li_us_body1}
	Run keyword unless	${resp_li['status_code']}== 202    Fail    ${resp_li['message']}
		
13.Create server profile with the created uplink set
    ${sh_resp} = 	Fusion Api Get Server Hardware    param=?filter="'name'=='${Enclosure_Name}, bay ${server_f95}'"
    Set Global Variable    ${sh_uri}    ${sh_resp['members'][0]['uri']} 
	Set to Dictionary    ${SP_body1}    serverHardwareUri    ${sh_uri}
	Set to Dictionary    ${SP_body1}    enclosureGroupUri    ${sh_resp['members'][0]['serverGroupUri']}
	Set to Dictionary    ${SP_body1}    serverHardwareTypeUri    ${sh_resp['members'][0]['serverHardwareTypeUri']}
	${resp} 	Fusion Api Get Ethernet Networks    param=?filter="'name'=='${Bulk_enet_body['namePrefix']}_${Tagged_VLAN}'"
	Set to Dictionary    ${SP_body1['connections'][0]}    networkUri    ${resp['members'][0]['uri']}
	${SP_resp} =    Fusion Api Create Server Profile    ${SP_body1}
	${task} =	Wait For Task 	${SP_resp} 	300s	30s
	Log to console and logfile    Server profile created successfully.
	
14.Power on the server
	${body} = 	Create Dictionary	powerState=On
	...								powerControl=MomentaryPress
	${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri}
	${task} =	Wait For Task 	${resp} 	240s	10s
	Sleep    ${Server_power_on_sleep_time}
	Log to console and logfile    Server powered on successfully.
	
15.Configure port monitoring in the XNET that does not belongs to uplink set.
    ${ic_resp} = 	Fusion Api Get Interconnect    param=?filter="'name'=='${Enclosure_Name}, interconnect ${server_f95}'"
    ${len}=    Get Length    ${ic_resp['members'][0]['ports']}
    :FOR	${x}	IN RANGE	0    ${len}
    \    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['bayNumber']}'=='${bay_f95}' and '${ic_resp['members'][0]['ports'][${x}]['portName']}'== '${normal_ports_f95[1]}'
    \    ...    Set to Dictionary    ${pmoni_body1['analyzerPort']}    portUri    ${ic_resp['members'][0]['ports'][${x}]['uri']}
    \    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['bayNumber']}'=='${bay_f95}' and '${ic_resp['members'][0]['ports'][${x}]['portName']}'== 'd${server_f95}'
    \    ...    Set to Dictionary    ${pmoni_body1['monitoredPorts'][0]}    portUri    ${ic_resp['members'][0]['ports'][${x}]['uri']}
    ${pmoni_resp}=    Fusion Api Update LI Port Monitor Configuration    ${pmoni_body1}    ${LI_uri}
    Should Be Equal As Strings    ${pmoni_resp['message']}    ${error_msg_6}
    Log to console and logfile    Unable to add the port which is already used for the profile connection. 
    
    :FOR	${x}	IN RANGE	0    ${len}
    \    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['bayNumber']}'=='${bay_f95}' and '${ic_resp['members'][0]['ports'][${x}]['portName']}'== '${normal_ports_f95[0]}'
    \    ...    Set to Dictionary    ${pmoni_body1['analyzerPort']}    portUri    ${ic_resp['members'][0]['ports'][${x}]['uri']}
    \    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['bayNumber']}'=='${bay_f95}' and '${ic_resp['members'][0]['ports'][${x}]['portName']}'== 'd${server_f95}'
    \    ...    Set to Dictionary    ${pmoni_body1['monitoredPorts'][0]}    portUri    ${ic_resp['members'][0]['ports'][${x}]['uri']}
    ${pmoni_resp}=    Fusion Api Update LI Port Monitor Configuration    ${pmoni_body1}    ${LI_uri}
    Run keyword unless	${pmoni_resp['status_code']}== 202    Fail    ${pmoni_resp['message']}
    ${task} =	Wait For Task 	${pmoni_resp} 	120s	10s
    Log to console and logfile    Test Case - 5C completed successfully
    
16.Delete a network and check the consistency status between LI/LIG
    ${resp_update} =    Fusion Api Update From Group    ${LI_uri}
	Run keyword unless	${resp_update['status_code']}== 202    Fail    ${resp_update['message']}
	${task} =	Wait For Task 	${resp_update} 	300s	30s
    ${Response}     fusion api delete ethernet network		${Bulk_enet_body['namePrefix']}_${Tagged_VLAN}
	Run keyword unless	${Response['status_code']}== 202	Fail	${Response['message']}
	${LI_resp} =    Fusion Api Get Li    ${LI_uri}
    Should Be Equal As Strings    ${LI_resp['consistencyStatus']}    CONSISTENT
    Log to console and logfile    Test Case - 6 completed successfully
    
###Proceeding with cleanup###
Local Cleanup
	Power off ALL servers
	${resp}=	Fusion Api Delete Server Profile	${SP_body1['name']}
	Run keyword unless	${resp['status_code']}== 202	Fail	${resp['message']}
	${task} =	Wait For Task 	${resp} 	120s	10s
		
	${encs} = 	Fusion Api Get Enclosures
	${resp}		fusion API Remove Enclosure		uri=${encs['members'][0]['uri']}
	Run keyword unless	${resp['status_code']}== 202	Fail	${resp['message']}
	${task} =	Wait For Task 	${resp}    300s    30s
	
	${resp}=	Fusion Api Delete Enclosure Group		name=${eg_body1['name']}
	Run keyword unless	${resp['status_code']}== 204	Fail	${resp['message']}
	
	${resp}=	Fusion Api Delete Lig		name=${lig_body1['name']}
	Run keyword unless	${resp['status_code']}== 202	Fail	${resp['message']}