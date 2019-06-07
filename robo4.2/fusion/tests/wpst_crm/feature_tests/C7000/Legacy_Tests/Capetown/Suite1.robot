*** Settings ***
Documentation      Test cases for Capetown includes pre-setup also

Library             FusionLibrary
Library             RoboGalaxyLibrary
Library				SSHLibrary
Library				Telnet
Library				String
Library				Dialogs
Library             data_variables
Variables           data_variables.py
Resource			../../../../resources/resource.txt

Suite Setup    Cleanup For Suite

*** Test Cases ***
1.Create SessionID through API
	Set Log Level    TRACE
    ${Login_response} =    Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	Run keyword unless	${Login_response[0]['status_code']}== 200    Fail    ${Login_response[0]['message']}
	Log to console and logfile    Test Step-1 completed successfully

2.Create Ethernet Networks
    ${enet_resp} =    Fusion Api Create Ethernet Network    ${Enet_body}
	Run keyword unless	${enet_resp['status_code']}== 202    Fail    ${enet_resp['message']}
	${uri} =    Get From Dictionary    ${enet_resp['associatedResource']}    resourceUri
	Set Global Variable    ${enet_uri}    ${uri}
	Log to console and logfile    ${enet_uri}
	
3.Create 6 FC-DA Networks
	Set To Dictionary    ${Fc_body}    fabricType    DirectAttach
	:FOR	${x}	IN RANGE	1	7
	\    Set To Dictionary    ${Fc_body}    name    FC_da${x}
	\    ${resp} =    Fusion Api Create Fc Network    ${Fc_body}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${uri} =    Get From Dictionary    ${resp['associatedResource']}    resourceUri
	\    Set Global Variable    ${FC_da${x}_uri}    ${uri}
	\    Log to console and logfile    ${FC_da${x}_uri}
	
4.Create 6 FC-FA Networks
    Set To Dictionary    ${Fc_body}    fabricType    FabricAttach
	:FOR	${x}	IN RANGE	1	7
	\    Set To Dictionary    ${Fc_body}    name    FC_fa${x}
	\    ${resp} =    Fusion Api Create Fc Network    ${Fc_body}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${uri} =    Get From Dictionary    ${resp['associatedResource']}    resourceUri
	\    Set Global Variable    ${FC_fa${x}_uri}    ${uri}
	\    Log to console and logfile    ${FC_fa${x}_uri}


5.Creating LIG	
	${enc_resp}=    Fusion Api Import Server Hardware Type For Enclosure    ${Preview_body}    ${Preview_uri}
	${interconnectMapTemplate}      Set Variable    ${enc_resp['logicalInterconnectGroup']['interconnectMapTemplate']}
	Set Global Variable   ${interconnectMapTemplate_Global}    ${interconnectMapTemplate} 
	Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
	
	:FOR	${x}	IN RANGE	1	7
	\    Append To List    ${lig_us_body1[${x}]['networkUris']}    ${FC_da${x}_uri}
	:FOR	${x}	IN RANGE	1	7
	\    Append To List    ${lig_us_body1[${x}+6]['networkUris']}    ${FC_fa${x}_uri}
	Append To List    ${lig_us_body1[0]['networkUris']}    ${enet_uri}
	Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
	#Append To List    ${lig_body1['uplinkSets']}    ${lig_us_body1}
	
	${resp_lig} = 	Fusion Api Create LIG	${lig_body1}
	Run keyword unless	${resp_lig['status_code']}== 202    Fail    ${resp_lig['message']}
	${task} =	Wait For Task 	${resp_lig} 	120s	2s
	Log to console and logfile    LIG created successfully
	${uri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri
	Set Global Variable    ${LIG_uri}    ${uri}
	Log to console and logfile    ${LIG_uri}

6.Creating EG	
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
	
7.Importing Enclosure
	Set To Dictionary    ${enc_body1}    enclosureGroupUri    ${EG_uri}
    ${resp_enc}=    Fusion Api Add Enclosure    ${enc_body1}
    Run keyword unless	${resp_enc['status_code']}== 202    Fail    ${resp_lig['message']}
	${task} =	Wait For Task 	${resp_enc} 	500s	30s
	Log to console and logfile    Enclosure imported successfully
	
	${enc_resp} = 	Fusion Api Get Enclosures    param=?filter="'name'=='${Enclosure_Name}'"
    Set Global Variable    ${ENC_uri}    ${enc_resp['members'][0]['uri']}
	Log to console and logfile    The enclosure uri is ${ENC_uri}
	
8.Creating Server Profiles
	Set To Dictionary    ${SP_body1['connections'][0]}    networkUri    ${enet_uri}
	:FOR	${x}	IN RANGE	1	4
	\    ${sh_resp} = 	Fusion Api Get Server Hardware    param=?filter="'name'=='${Enclosure_Name}, bay ${Server_bays[${x}-1]}'"
    \    Set Global Variable    ${sh_uri_${x}}    ${sh_resp['members'][0]['uri']} 
	\    Set to Dictionary    ${SP_body1}    serverHardwareUri    ${sh_uri_${x}}
	\    Set to Dictionary    ${SP_body1}    enclosureGroupUri    ${sh_resp['members'][0]['serverGroupUri']}
	\    Set to Dictionary    ${SP_body1}    serverHardwareTypeUri    ${sh_resp['members'][0]['serverHardwareTypeUri']}
	\    Set Network Uri For FC Connections    ${x}
	\    Set To Dictionary    ${SP_body1}    name    SP_${x}
	\    ${resp} =    Fusion Api Create Server Profile    ${SP_body1}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${task} =	Wait For Task 	${resp} 	300s	30s
	\    ${uri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri
	\    Set Global Variable    ${SP_${x}_uri}    ${uri}
	\    Log to console and logfile    ${SP_${x}_uri}
	\	 ${body} = 	Create Dictionary	powerState=On
	\	 ...							powerControl=MomentaryPress
	\	 ${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri_${x}}
	\	 ${task} =	Wait For Task 	${resp}    240s    10s 
	
	sleep    ${Server_power_on_sleep_time}

9.LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
10.LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
11.LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3} 

#Test case - 347	
Verify port speed
	SSHLibrary.Open Connection    ${FC_Switch_IP}
	SSHLibrary.Login    ${FC_Switch_USERNAME}    ${FC_Switch_PASSWORD}
	:FOR	${x}	IN RANGE	0	6
    \    ${output}=      SSHLibrary.Execute Command    portshow ${Switch_ports[${x}]}    
    \    log to console    ${output}
    \    ${portspeed}=    Get Lines Matching Regexp    ${output}    Gbps.*    case-sensitive 
    \    @{words} = 	Split String	${portspeed}
	\    Run keyword unless    '${words[-1]}' == '${exp_output_speed[${x}]}'    Fail    Log to console and logfile    The port speed doesn't match

#Test case - 356
356.A) Reboot server
	
	:FOR	${x}	IN RANGE	1	4
    \	 ${body} = 	Create Dictionary	powerState=Off
	\	 ...							powerControl=PressAndHold
	\	 ${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri_${x}}
	\	 ${task} =	Wait For Task 	${resp}    300s    20s
	
	Sleep    100
	
    :FOR	${x}	IN RANGE	1	4
    \	 ${body} = 	Create Dictionary	powerState=On
	\	 ...							powerControl=MomentaryPress
	\	 ${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri_${x}}
	\	 ${task} =	Wait For Task 	${resp}    300s    20s 
	
	Sleep    ${Server_power_on_sleep_time}
	
356.B) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
356.C) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
356.C) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}
	
#Test case - 349
*** Comments ***
#Commented since the servers get ip from ICM1
349.1A) ICM1 poweroff
    OA CLI DEVICE POWEROFF    ${oa_details['oa_ip']}    ${oa_details['username']}    ${oa_details['password']}    INTERCONNECT    ${Supershaw_DA['bay_num']}
	Sleep    100s
	
349.1B) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    #Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
349.1C) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	#Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
349.1D) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	#Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3} 

*** Test Cases ***
349.2A) ICM2 poweroff
	OA CLI DEVICE POWEROFF    ${oa_details['oa_ip']}    ${oa_details['username']}    ${oa_details['password']}    INTERCONNECT    ${Supershaw_FA['bay_num']}
	Sleep    100s
	
349.2B) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 5    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
349.2C) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 5    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
349.2D) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 4    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3} 

349.3A) ICM3 poweroff	
	OA CLI DEVICE POWEROFF    ${oa_details['oa_ip']}    ${oa_details['username']}    ${oa_details['password']}    INTERCONNECT    ${Sheppard_DA['bay_num']}
	Sleep    100s
	
349.3B) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 4    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
349.3C) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 4    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
349.3D) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 4    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3} 
	
349.4A) ICM4 poweroff
	OA CLI DEVICE POWEROFF    ${oa_details['oa_ip']}    ${oa_details['username']}    ${oa_details['password']}    INTERCONNECT    ${Sheppard_FA['bay_num']}
	Sleep    100s
	
349.4B) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 2    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
349.4C) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 2    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
349.4D) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 2    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3} 
	
349.5A) ICMs - poweron
    OA CLI DEVICE POWERON    ${oa_details['oa_ip']}    ${oa_details['username']}    ${oa_details['password']}    INTERCONNECT    ${Supershaw_DA['bay_num']}
	OA CLI DEVICE POWERON    ${oa_details['oa_ip']}    ${oa_details['username']}    ${oa_details['password']}    INTERCONNECT    ${Supershaw_FA['bay_num']}
	OA CLI DEVICE POWERON    ${oa_details['oa_ip']}    ${oa_details['username']}    ${oa_details['password']}    INTERCONNECT    ${Sheppard_DA['bay_num']}
	OA CLI DEVICE POWERON    ${oa_details['oa_ip']}    ${oa_details['username']}    ${oa_details['password']}    INTERCONNECT    ${Sheppard_FA['bay_num']}
	Sleep    500s
	
349.5B) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
349.5C) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
349.5D) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}


#Test case - 351, 352   
351.A) Editing LIG from da to fa and fa to da AND LI update
	:FOR	${x}	IN RANGE    1    7
	\	 Remove From List    ${lig_us_body1[${x}]['networkUris']}    0  
	\    Append To List    ${lig_us_body1[${x}]['networkUris']}    ${FC_fa${x}_uri}  	
	:FOR	${x}	IN RANGE	1	7
	\	 Remove From List    ${lig_us_body1[${x}+6]['networkUris']}    0
	\    Append To List    ${lig_us_body1[${x}+6]['networkUris']}    ${FC_da${x}_uri}
	Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}	
	${resp}=    Fusion Api Edit Lig    ${lig_body1}    ${LIG_uri}
	Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited with uplinkport successfully
	${task} =	Wait For Task    ${resp} 	300s	30s
	${li_resp} =    Fusion Api Get Li
	Log to console and logfile    ${li_resp['members'][0]['uri']}
	Set Global Variable    ${LI_uri}    ${li_resp['members'][0]['uri']}
	${resp_update} =    Fusion Api Update From Group    ${LI_uri}
	Run keyword unless	${resp_update['status_code']}== 202    Fail    ${resp_update['message']}
	${task} =	Wait For Task    ${resp_update} 	300s	30s
	Log to console and logfile    LI updated from group successfully.
	Sleep    ${Server_power_on_sleep_time}    

351.B) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 0    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
351.C) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 0    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
351.D) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 0    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3} 
   
351.E) Editing LIG to get the orginal state AND LI update
	:FOR	${x}	IN RANGE    1    7
	\	 Remove From List    ${lig_us_body1[${x}]['networkUris']}    0  
	\    Append To List    ${lig_us_body1[${x}]['networkUris']}    ${FC_da${x}_uri}  	
	:FOR	${x}	IN RANGE	1	7
	\	 Remove From List    ${lig_us_body1[${x}+6]['networkUris']}    0
	\    Append To List    ${lig_us_body1[${x}+6]['networkUris']}    ${FC_fa${x}_uri}
	Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}	
	${resp}=    Fusion Api Edit Lig    ${lig_body1}    ${LIG_uri}
	sleep    200s
	${li_resp} =    Fusion Api Get Li
	Log to console and logfile    ${li_resp['members'][0]['uri']}
	Set Global Variable    ${LI_uri}    ${li_resp['members'][0]['uri']}
	${resp_update} =    Fusion Api Update From Group    ${LI_uri}
	Run keyword unless	${resp_update['status_code']}== 202    Fail    ${resp_update['message']}
	${task} =	Wait For Task    ${resp_update} 	300s	30s
	Log to console and logfile    LI updated from group successfully.
	Sleep    300s

351.F) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
351.F) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
351.G) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}

#Test case - 350 and 353
353.A) Create 2 FC-DA Networks
    Set To Dictionary    ${Fc_body}    fabricType    DirectAttach
    :FOR    ${x}    IN RANGE    0    2
	\    Set To Dictionary    ${Fc_body}    name    fc-da${x}
	\    ${resp} =    Fusion Api Create Fc Network    ${Fc_body}
	\    Run keyword unless    ${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${uri} =    Get From Dictionary    ${resp['associatedResource']}    resourceUri
	\    Set Global Variable    ${fc-da${x}_uri}    ${uri}
	\    Log to console and logfile    ${fc-da${x}_uri}


353.B) Edit LI to add 2 uplink set
  	${st1_resp}    Fusion Api Get Li    
  	Set Global Variable    ${LI_uri}    ${st1_resp['members'][0]['uri']}
  	Log to console and logfile    ${LI_uri}    
  	:FOR	${x}	IN RANGE    0    2
  	\    Set To Dictionary    ${li_body4[${x}]}    logicalInterconnectUri    ${LI_uri} 
  	\    Append To List    ${li_body4[${x}]['fcNetworkUris']}    ${fc-da${x}_uri}    
  	\    ${st_resp} =    Fusion Api Create Uplink Set    ${li_body4[${x}]}         
	\    Run Keyword If    ${st_resp['status_code']} != 202    Fail	   ELSE     Log to console and logfile    \ncreated uplink in li	
	\    ${task} =    Wait For Task    ${st_resp}    200s    20s
	\    Log to console and logfile    successfully edited
	
353.C) Check Alerts	 
    Sleep    100s   
	${US_resp} =    Fusion Api Get Uplink Set    param=?filter="'name'=='${li_body4[0]['name']}'"
	Run keyword unless    '${US_resp['members'][0]['state']}' == 'Failed' and '${US_resp['members'][0]['status']}' == 'Critical'    Fail
	Log to console and logfile    ${li_body4[0]['name']} is connected to a non-DA array
	
	${US_resp} =    Fusion Api Get Uplink Set    param=?filter="'name'=='${li_body4[1]['name']}'"
	${Port_resp} =    Fusion Api Get Uplink Set    uri=${US_resp['members'][0]['portConfigInfos'][0]['portUri']}    
	Run keyword unless    '${Port_resp['portStatus']}' == 'Linked' and '${Port_resp['connectorType']}' == 'SFP-FC'   Fail
	Log to console and logfile    ${li_body4[1]['name']} is connected to a different array
	
353.D) Delete Uplink set	
    :FOR	${y}	IN RANGE	0	2
	\    ${US_del_resp} =    Fusion Api Delete Uplink Set    ${li_body4[${y}]['name']}
	\    Run keyword unless    ${US_del_resp['status_code']}== 202    Fail    ${US_del_resp['message']}	
	Log to console and logfile    Uplink sets deleted successfully

353.E) Delete new FC networks	
	:FOR	${x}	IN RANGE	0	2
	\    ${FC_del_resp} =    Fusion Api Delete Fc Network    fc-da${x}
	\    Run keyword unless    ${FC_del_resp['status_code']}== 202    Fail    ${FC_del_resp['message']}	
	Log to console and logfile    Networks deleted successfully

# Test Case - 364	
364.1A) Get logicalPortConfigInfos from data
    ${logicalPortConfigInfos}    Create List
    Set Global Variable    ${logicalPortConfigInfos}
    :FOR	${x}	IN RANGE	1	13
    \    ${logicalPortConfig}    Get From List    ${lig_us_body1[${x}]['logicalPortConfigInfos']}    0
    \    Append to List    ${logicalPortConfigInfos}    ${logicalPortConfig}

364.2) Edit LIG and remove uplink port and verify LUN
    Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    Remove From List    ${lig_us_body1[1]['logicalPortConfigInfos']}    0
    Remove From List    ${lig_us_body1[4]['logicalPortConfigInfos']}    0
    Remove From List    ${lig_us_body1[7]['logicalPortConfigInfos']}    0
    Remove From List    ${lig_us_body1[10]['logicalPortConfigInfos']}    0
    Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited without uplinkport successfully
    ${task} =	Wait For Task    ${resp} 	300s	30s
    ${li_uri} = 	Get LI URI   ${LE}-${lig_body1['name']}
	Set Global Variable    ${LI_uri}    ${li_uri}
	Perform an LI Update From Group    ${LI_uri}
    Sleep    60sec

364.2A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 0    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
364.2B) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 8    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
364.2C) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}

364.3) Edit LIG and add uplink port and verify LUN
    Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    Append To List    ${lig_us_body1[1]['logicalPortConfigInfos']}    ${logicalPortConfigInfos[0]}
    Append To List    ${lig_us_body1[4]['logicalPortConfigInfos']}    ${logicalPortConfigInfos[3]}
    Append To List    ${lig_us_body1[7]['logicalPortConfigInfos']}    ${logicalPortConfigInfos[6]}
    Append To List    ${lig_us_body1[10]['logicalPortConfigInfos']}    ${logicalPortConfigInfos[9]}
    Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited with uplinkport successfully
	${task} =	Wait For Task    ${resp} 	300s	30s
    
	Perform an LI Update From Group    ${LI_uri}
    Sleep    60sec

364.3A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
364.3B) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
364.3C) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}

364.4) Edit LIG and remove uplink port and verify LUN
    Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    Remove From List    ${lig_us_body1[2]['logicalPortConfigInfos']}    0
    Remove From List    ${lig_us_body1[5]['logicalPortConfigInfos']}    0
    Remove From List    ${lig_us_body1[8]['logicalPortConfigInfos']}    0
    Remove From List    ${lig_us_body1[11]['logicalPortConfigInfos']}    0
    Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited without uplinkport successfully

    ${task} =	Wait For Task    ${resp} 	300s	30s
	Perform an LI Update From Group    ${LI_uri}
    Sleep    60sec

364.4A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 8    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
364.4B) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 0    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
364.4C) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}

364.5) Edit LIG and add uplink port and verify LUN
    Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    Append To List    ${lig_us_body1[2]['logicalPortConfigInfos']}    ${logicalPortConfigInfos[1]}
    Append To List    ${lig_us_body1[5]['logicalPortConfigInfos']}    ${logicalPortConfigInfos[4]}
    Append To List    ${lig_us_body1[8]['logicalPortConfigInfos']}    ${logicalPortConfigInfos[7]}
    Append To List    ${lig_us_body1[11]['logicalPortConfigInfos']}    ${logicalPortConfigInfos[10]}
    Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited with uplinkport successfully    
	${task} =	Wait For Task    ${resp} 	300s	30s
	
	Perform an LI Update From Group    ${LI_uri}
    Sleep    60sec

364.5A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
364.5B) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
364.5C) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}

364.6) Edit LIG and remove uplink port and verify LUN
    Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    Remove From List    ${lig_us_body1[3]['logicalPortConfigInfos']}    0
    Remove From List    ${lig_us_body1[6]['logicalPortConfigInfos']}    0
    Remove From List    ${lig_us_body1[9]['logicalPortConfigInfos']}    0
    Remove From List    ${lig_us_body1[12]['logicalPortConfigInfos']}    0
    Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited without uplinkport successfully
	${task} =	Wait For Task    ${resp} 	300s	30s

	Perform an LI Update From Group    ${LI_uri}
    Sleep    60sec

364.6A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
364.6B) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
364.6C) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 0    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}

364.7) Edit LIG and add uplink port and verify LUN
    Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    Append To List    ${lig_us_body1[3]['logicalPortConfigInfos']}    ${logicalPortConfigInfos[2]}
    Append To List    ${lig_us_body1[6]['logicalPortConfigInfos']}    ${logicalPortConfigInfos[5]}
    Append To List    ${lig_us_body1[9]['logicalPortConfigInfos']}    ${logicalPortConfigInfos[8]}
    Append To List    ${lig_us_body1[12]['logicalPortConfigInfos']}    ${logicalPortConfigInfos[11]}
    Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited with uplinkport successfully
	${task} =	Wait For Task    ${resp} 	300s	30s

	Perform an LI Update From Group    ${LI_uri}
    Sleep    60sec

364.7A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
364.7B) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
364.7C) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}

#Test Case - 365
365.1) Edit LIG and remove network and verify LUN
    Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    Remove From List    ${lig_us_body1[1]['networkUris']}    0
    Remove From List    ${lig_us_body1[4]['networkUris']}    0
    Remove From List    ${lig_us_body1[7]['networkUris']}    0
    Remove From List    ${lig_us_body1[10]['networkUris']}    0
    Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited without network successfully
    ${task} =	Wait For Task    ${resp} 	300s	30s
    
	Perform an LI Update From Group    ${LI_uri}
    Sleep    60sec

365.2A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 0    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
365.2B) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 8    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
365.2C) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}    

365.3) Edit LIG and Add network
    Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    Append To List    ${lig_us_body1[1]['networkUris']}    ${FC_da1_uri}
    Append To List    ${lig_us_body1[4]['networkUris']}    ${FC_da4_uri}
    Append To List    ${lig_us_body1[7]['networkUris']}    ${FC_fa1_uri}
    Append To List    ${lig_us_body1[10]['networkUris']}    ${FC_fa4_uri}
    Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited with network successfully
	${task} =	Wait For Task    ${resp} 	300s	30s

	Perform an LI Update From Group    ${LI_uri}
    Sleep    60sec

365.3A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
365.3B) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
365.3C) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3} 

365.4) Edit LIG and remove network
    Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    Remove From List    ${lig_us_body1[2]['networkUris']}    0
    Remove From List    ${lig_us_body1[5]['networkUris']}    0
    Remove From List    ${lig_us_body1[8]['networkUris']}    0
    Remove From List    ${lig_us_body1[11]['networkUris']}    0
    Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited without network successfully
	${task} =	Wait For Task    ${resp} 	300s	30s

	Perform an LI Update From Group    ${LI_uri}
    Sleep    60sec

365.4A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 8    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
365.4B) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 0    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
365.4C) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}   

365.5) Edit LIG and Add network
    Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    Append To List    ${lig_us_body1[2]['networkUris']}    ${FC_da2_uri}
    Append To List    ${lig_us_body1[5]['networkUris']}    ${FC_da5_uri}
    Append To List    ${lig_us_body1[8]['networkUris']}    ${FC_fa2_uri}
    Append To List    ${lig_us_body1[11]['networkUris']}    ${FC_fa5_uri}
    Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited with network successfully
	${task} =	Wait For Task    ${resp} 	300s	30s

	Perform an LI Update From Group    ${LI_uri}
    Sleep    60sec

365.5A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
365.5B) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
365.5C) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}    

365.6) Edit LIG and remove network
    Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    Remove From List    ${lig_us_body1[3]['networkUris']}    0
    Remove From List    ${lig_us_body1[6]['networkUris']}    0
    Remove From List    ${lig_us_body1[9]['networkUris']}    0
    Remove From List    ${lig_us_body1[12]['networkUris']}    0
    Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited without network successfully
	${task} =	Wait For Task    ${resp} 	300s	30s

	Perform an LI Update From Group    ${LI_uri}
    Sleep    60sec

365.6A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
365.6B) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
365.6C) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 0    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}    

365.7) Edit LIG and add network
    Set To Dictionary    ${lig_body1}    interconnectMapTemplate    ${interconnectMapTemplate_Global}
    Append To List    ${lig_us_body1[3]['networkUris']}    ${FC_da3_uri}
    Append To List    ${lig_us_body1[6]['networkUris']}    ${FC_da6_uri}
    Append To List    ${lig_us_body1[9]['networkUris']}    ${FC_fa3_uri}
    Append To List    ${lig_us_body1[12]['networkUris']}    ${FC_fa6_uri}
    Set To Dictionary    ${lig_body1}    uplinkSets    ${lig_us_body1}
    ${resp} = 	Fusion Api Edit LIG	    ${lig_body1}    ${LIG_uri}
    Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-LIG is edited with network successfully
	${task} =	Wait For Task    ${resp} 	300s	30s

	Perform an LI Update From Group    ${LI_uri}
    Sleep    60sec

365.7A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
365.7B) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
365.7C) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3} 
	
358.1)Code to disable ports on Supershaw_DA
	${ic_resp} = 	Fusion Api Get Interconnect    param=?filter="'name'=='${Enclosure_Name}, interconnect ${Supershaw_DA['bay_num']}'"
    Set Global Variable    ${IC_Supershaw_DA_uri}    ${ic_resp['members'][0]['uri']}
	Log to console and logfile    The interconnect uri is ${IC_Supershaw_DA_uri}
	
	${len}=    Get Length    ${ic_resp['members'][0]['ports']}
	Log to console and logfile    ${len}
	
	:FOR	${x}	IN RANGE	0	${len}
	\    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['name']}'== '${Supershaw_DA['Act_ports'][0]}'    Set Global Variable    ${port1_uri}    ${ic_resp['members'][0]['ports'][${x}]['uri']}
	\    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['name']}'== '${Supershaw_DA['Act_ports'][1]}'    Set Global Variable    ${port2_uri}    ${ic_resp['members'][0]['ports'][${x}]['uri']}
	\    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['name']}'== '${Supershaw_DA['Act_ports'][2]}'    Set Global Variable    ${port3_uri}    ${ic_resp['members'][0]['ports'][${x}]['uri']}
	
	:FOR	${y}	IN RANGE	1	4
	\    ${ic_port_resp} = 	Fusion Api Get Interconnect    uri=${port${y}_uri}
	\    Set To Dictionary    ${ic_disable_body[0]}    associatedUplinkSetUri    ${ic_port_resp['associatedUplinkSetUri']}
	\    Set To Dictionary    ${ic_disable_body[0]}    interconnectName    ${ic_port_resp['interconnectName']}
	\    Set To Dictionary    ${ic_disable_body[0]}    portId    ${ic_port_resp['portId']}
	\    Set To Dictionary    ${ic_disable_body[0]}    portName    ${ic_port_resp['portName']}
	\    ${resp} =    Fusion Api Edit Interconnect Ports    uri=${IC_Supershaw_DA_uri}    body=${ic_disable_body}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${task} =    Wait For Task 	${resp} 	120s	10s
	Sleep    100
	
358.1A)LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 6    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
358.1B)LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 6    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
358.1C)LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3} 
	
358.2)Code to enable ports on Supershaw_DA
	:FOR	${y}	IN RANGE	1	4
	\    ${ic_port_resp} = 	Fusion Api Get Interconnect    uri=${port${y}_uri}
	\    Set To Dictionary    ${ic_enable_body[0]}    associatedUplinkSetUri    ${ic_port_resp['associatedUplinkSetUri']}
	\    Set To Dictionary    ${ic_enable_body[0]}    interconnectName    ${ic_port_resp['interconnectName']}
	\    Set To Dictionary    ${ic_enable_body[0]}    portId    ${ic_port_resp['portId']}
	\    Set To Dictionary    ${ic_enable_body[0]}    portName    ${ic_port_resp['portName']}
	\    ${resp} =    Fusion Api Edit Interconnect Ports    uri=${IC_Supershaw_DA_uri}    body=${ic_enable_body}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${task} =    Wait For Task 	${resp} 	120s	10s
	Sleep    100
	
358.2A)LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
358.2B)LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
358.2C)LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}
	
358.3)Code to disable ports on Supershaw_FA
	${ic_resp} = 	Fusion Api Get Interconnect    param=?filter="'name'=='${Enclosure_Name}, interconnect ${Supershaw_FA['bay_num']}'"
    Set Global Variable    ${IC_Supershaw_FA_uri}    ${ic_resp['members'][0]['uri']}
	Log to console and logfile    The interconnect uri is ${IC_Supershaw_FA_uri}
	
	${len}=    Get Length    ${ic_resp['members'][0]['ports']}
	Log to console and logfile    ${len}
	
	:FOR	${x}	IN RANGE	0	${len}
	\    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['name']}'== '${Supershaw_FA['Act_ports'][0]}'    Set Global Variable    ${port1_uri}    ${ic_resp['members'][0]['ports'][${x}]['uri']}
	\    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['name']}'== '${Supershaw_FA['Act_ports'][1]}'    Set Global Variable    ${port2_uri}    ${ic_resp['members'][0]['ports'][${x}]['uri']}
	\    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['name']}'== '${Supershaw_FA['Act_ports'][2]}'    Set Global Variable    ${port3_uri}    ${ic_resp['members'][0]['ports'][${x}]['uri']}
	
	:FOR	${y}	IN RANGE	1	4
	\    ${ic_port_resp} = 	Fusion Api Get Interconnect    uri=${port${y}_uri}
	\    Set To Dictionary    ${ic_disable_body[0]}    associatedUplinkSetUri    ${ic_port_resp['associatedUplinkSetUri']}
	\    Set To Dictionary    ${ic_disable_body[0]}    interconnectName    ${ic_port_resp['interconnectName']}
	\    Set To Dictionary    ${ic_disable_body[0]}    portId    ${ic_port_resp['portId']}
	\    Set To Dictionary    ${ic_disable_body[0]}    portName    ${ic_port_resp['portName']}
	\    ${resp} =    Fusion Api Edit Interconnect Ports    uri=${IC_Supershaw_FA_uri}    body=${ic_disable_body}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${task} =    Wait For Task 	${resp} 	120s	10s
	Sleep    100
	
358.3A)LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 5    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
358.3B)LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 5   Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
358.3C)LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 4    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3} 
	
358.4)Code to enable ports on Supershaw_FA
	:FOR	${y}	IN RANGE	1	4
	\    ${ic_port_resp} = 	Fusion Api Get Interconnect    uri=${port${y}_uri}
	\    Set To Dictionary    ${ic_enable_body[0]}    associatedUplinkSetUri    ${ic_port_resp['associatedUplinkSetUri']}
	\    Set To Dictionary    ${ic_enable_body[0]}    interconnectName    ${ic_port_resp['interconnectName']}
	\    Set To Dictionary    ${ic_enable_body[0]}    portId    ${ic_port_resp['portId']}
	\    Set To Dictionary    ${ic_enable_body[0]}    portName    ${ic_port_resp['portName']}
	\    ${resp} =    Fusion Api Edit Interconnect Ports    uri=${IC_Supershaw_FA_uri}    body=${ic_enable_body}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${task} =    Wait For Task 	${resp} 	120s	10s
	Sleep    100
	
358.4A)LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
358.4B)LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
358.4C)LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}
	
358.5)Code to disable ports on Sheppard_DA
	${ic_resp} = 	Fusion Api Get Interconnect    param=?filter="'name'=='${Enclosure_Name}, interconnect ${Sheppard_DA['bay_num']}'"
    Set Global Variable    ${IC_Sheppard_DA_uri}    ${ic_resp['members'][0]['uri']}
	Log to console and logfile    The interconnect uri is ${IC_Sheppard_DA_uri}
	
	${len}=    Get Length    ${ic_resp['members'][0]['ports']}
	Log to console and logfile    ${len}
	
	:FOR	${x}	IN RANGE	0	${len}
	\    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['name']}'== '${Sheppard_DA['Act_ports'][0]}'    Set Global Variable    ${port1_uri}    ${ic_resp['members'][0]['ports'][${x}]['uri']}
	\    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['name']}'== '${Sheppard_DA['Act_ports'][1]}'    Set Global Variable    ${port2_uri}    ${ic_resp['members'][0]['ports'][${x}]['uri']}
	\    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['name']}'== '${Sheppard_DA['Act_ports'][2]}'    Set Global Variable    ${port3_uri}    ${ic_resp['members'][0]['ports'][${x}]['uri']}
	
	:FOR	${y}	IN RANGE	1	4
	\    ${ic_port_resp} = 	Fusion Api Get Interconnect    uri=${port${y}_uri}
	\    Set To Dictionary    ${ic_disable_body[0]}    associatedUplinkSetUri    ${ic_port_resp['associatedUplinkSetUri']}
	\    Set To Dictionary    ${ic_disable_body[0]}    interconnectName    ${ic_port_resp['interconnectName']}
	\    Set To Dictionary    ${ic_disable_body[0]}    portId    ${ic_port_resp['portId']}
	\    Set To Dictionary    ${ic_disable_body[0]}    portName    ${ic_port_resp['portName']}
	\    ${resp} =    Fusion Api Edit Interconnect Ports    uri=${IC_Sheppard_DA_uri}    body=${ic_disable_body}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${task} =    Wait For Task 	${resp} 	120s	10s
	Sleep    100
	
358.5A)LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 6    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
358.5B)LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 6    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
358.5C)LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3} 
	
358.6)Code to enable ports on Supershaw_DA
	:FOR	${y}	IN RANGE	1	4
	\    ${ic_port_resp} = 	Fusion Api Get Interconnect    uri=${port${y}_uri}
	\    Set To Dictionary    ${ic_enable_body[0]}    associatedUplinkSetUri    ${ic_port_resp['associatedUplinkSetUri']}
	\    Set To Dictionary    ${ic_enable_body[0]}    interconnectName    ${ic_port_resp['interconnectName']}
	\    Set To Dictionary    ${ic_enable_body[0]}    portId    ${ic_port_resp['portId']}
	\    Set To Dictionary    ${ic_enable_body[0]}    portName    ${ic_port_resp['portName']}
	\    ${resp} =    Fusion Api Edit Interconnect Ports    uri=${IC_Sheppard_DA_uri}    body=${ic_enable_body}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${task} =    Wait For Task 	${resp} 	120s	10s
	Sleep    100
	
358.6A)LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
358.6B)LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
358.6C)LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}
	
358.7)Code to disable ports on Sheppard_FA
	${ic_resp} = 	Fusion Api Get Interconnect    param=?filter="'name'=='${Enclosure_Name}, interconnect ${Sheppard_FA['bay_num']}'"
    Set Global Variable    ${IC_Sheppard_FA_uri}    ${ic_resp['members'][0]['uri']}
	Log to console and logfile    The interconnect uri is ${IC_Sheppard_FA_uri}
	
	${len}=    Get Length    ${ic_resp['members'][0]['ports']}
	Log to console and logfile    ${len}
	
	:FOR	${x}	IN RANGE	0	${len}
	\    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['name']}'== '${Sheppard_FA['Act_ports'][0]}'    Set Global Variable    ${port1_uri}    ${ic_resp['members'][0]['ports'][${x}]['uri']}
	\    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['name']}'== '${Sheppard_FA['Act_ports'][1]}'    Set Global Variable    ${port2_uri}    ${ic_resp['members'][0]['ports'][${x}]['uri']}
	\    Run keyword if    '${ic_resp['members'][0]['ports'][${x}]['name']}'== '${Sheppard_FA['Act_ports'][2]}'    Set Global Variable    ${port3_uri}    ${ic_resp['members'][0]['ports'][${x}]['uri']}
	
	:FOR	${y}	IN RANGE	1	4
	\    ${ic_port_resp} = 	Fusion Api Get Interconnect    uri=${port${y}_uri}
	\    Set To Dictionary    ${ic_disable_body[0]}    associatedUplinkSetUri    ${ic_port_resp['associatedUplinkSetUri']}
	\    Set To Dictionary    ${ic_disable_body[0]}    interconnectName    ${ic_port_resp['interconnectName']}
	\    Set To Dictionary    ${ic_disable_body[0]}    portId    ${ic_port_resp['portId']}
	\    Set To Dictionary    ${ic_disable_body[0]}    portName    ${ic_port_resp['portName']}
	\    ${resp} =    Fusion Api Edit Interconnect Ports    uri=${IC_Sheppard_FA_uri}    body=${ic_disable_body}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${task} =    Wait For Task 	${resp} 	120s	10s
	Sleep    100
	
358.7A)LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 5    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
358.7B)LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 5    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
358.7C)LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 4    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3} 
	
358.8)Code to enable ports on Supershaw_DA
	:FOR	${y}	IN RANGE	1	4
	\    ${ic_port_resp} = 	Fusion Api Get Interconnect    uri=${port${y}_uri}
	\    Set To Dictionary    ${ic_enable_body[0]}    associatedUplinkSetUri    ${ic_port_resp['associatedUplinkSetUri']}
	\    Set To Dictionary    ${ic_enable_body[0]}    interconnectName    ${ic_port_resp['interconnectName']}
	\    Set To Dictionary    ${ic_enable_body[0]}    portId    ${ic_port_resp['portId']}
	\    Set To Dictionary    ${ic_enable_body[0]}    portName    ${ic_port_resp['portName']}
	\    ${resp} =    Fusion Api Edit Interconnect Ports    uri=${IC_Sheppard_FA_uri}    body=${ic_enable_body}
	\    Run keyword unless	${resp['status_code']}== 202    Fail    ${resp['message']}
	\    ${task} =    Wait For Task 	${resp} 	120s	10s
	Sleep    100
	
358.8A)LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
358.8B)LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
358.8C)LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 6    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}
	
360.9) Deleting network from server profile 
	:FOR	${x}	IN RANGE	1	4
	\	 ${body} = 	Create Dictionary	powerState=Off
		  ...							powerControl=PressAndHold
	\    ${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri_${x}}
	\	 ${task} =	Wait For Task 	${resp}    240s    10s
	\    ${sh_resp} = 	Fusion Api Get Server Hardware    param=?filter="'name'=='${Enclosure_Name}, bay ${Server_bays[${x}-1]}'"
	\    Set to Dictionary    ${SP_body1}    enclosureGroupUri    ${sh_resp['members'][0]['serverGroupUri']}
	\    Set to Dictionary    ${SP_body1}    serverHardwareTypeUri    ${sh_resp['members'][0]['serverHardwareTypeUri']}
	\    Set to Dictionary    ${SP_body1}    serverHardwareUri    ${sh_resp['members'][0]['uri']}
	\	 ${e_resp}=    Fusion Api Get Server Profiles    param=?filter="'name'=='SP_${x}'"   
	\	 Set to Dictionary    ${SP_body1}    eTag    ${e_resp['members'][0]['eTag']}
	\	 Set to Dictionary    ${SP_body1}    name    SP_${x}
	\    Set to Dictionary    ${SP_body1}    enclosureUri    ${ENC_uri}
	\	 Set to Dictionary    ${SP_body1}    uri    ${SP_${x}_uri}  
	#\	 Set to Dictionary    ${SP_body1}    connections    ${connections_edit_add}
	\	 Set To Dictionary    ${SP_body1['connections'][0]}    networkUri    ${enet_uri}
	
	\	 Remove From List    ${SP_body1['connections']}    4
	\	 Remove From List    ${SP_body1['connections']}    3
	\	 Remove From List    ${SP_body1['connections']}    2
	\	 Remove From List    ${SP_body1['connections']}    1
	\	 ${resp}=    Fusion Api Edit Server Profile    body=${SP_body1}    uri=${SP_${x}_uri}
	\	 ${task} =	Wait For Task 	${resp}    240s    10s
	\	 Set to Dictionary    ${SP_body1}    connections    ${connections_edit_add${x}}
	\	 ${body} = 	Create Dictionary	powerState=On
	\	 ...							powerControl=MomentaryPress
	\	 ${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri_${x}}
	\	 ${task} =	Wait For Task 	${resp}    240s    10s 
	
	sleep    ${Server_power_on_sleep_time}
	
360.9A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 0    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
360.9B) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 0    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
360.9C) LUN Discover server 3             
	${output3}=    Get Linux LUN Count    ${oa_details}    ${Server_bays[2]}    ${linux_server_details}
	Run keyword unless       ${output3}== 0    Fail    Log to console and logfile    The count of available LUN is ${output3}
	Log to console and logfile    ${output3}
	
360.10) Creating the network back in server profile
	:FOR	${x}	IN RANGE	1	4
	\	 ${body} = 	Create Dictionary	powerState=Off
		  ...							powerControl=PressAndHold
	\    ${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri_${x}}
	\	 ${task} =	Wait For Task 	${resp}    240s    10s
	\	 ${sh_resp} = 	Fusion Api Get Server Hardware    param=?filter="'name'=='${Enclosure_Name}, bay ${Server_bays[${x}-1]}'"
	
	\	 Set to Dictionary    ${SP_body1}    serverHardwareUri    ${sh_resp['members'][0]['uri']}
	\	 Set to Dictionary    ${SP_body1}    enclosureGroupUri    ${sh_resp['members'][0]['serverGroupUri']}
	\	 Set to Dictionary    ${SP_body1}    serverHardwareTypeUri    ${sh_resp['members'][0]['serverHardwareTypeUri']}
	\	 ${e_resp}=    Fusion Api Get Server Profiles    param=?filter="'name'=='SP_${x}'"
	\	 Log to console and logfile    ${e_resp['members'][0]['eTag']}
	\	 Set to Dictionary    ${SP_body1}    eTag    ${e_resp['members'][0]['eTag']}
	\	 Set to Dictionary    ${SP_body1}    enclosureUri    ${e_resp['members'][0]['enclosureUri']}
	\	 Set to Dictionary    ${SP_body1}    uri    ${SP_${x}_uri}
	\	 ${enet_resp} = 	Fusion Api Get Ethernet Networks    param=?filter="'name'=='${Enet_body['name']}'"
	\	 Set To Dictionary    ${SP_body1['connections'][0]}    networkUri    ${enet_resp['members'][0]['uri']}
	\	 Set Network Uri For FC Connections    ${x}   
	\	 Set To Dictionary    ${SP_body1}    name    SP_${x}
	\	 ${resp}=    Fusion Api Edit Server Profile    body=${SP_body1}    uri=${SP_${x}_uri}
	\	 ${task} =	Wait For Task 	${resp}    240s    10s
	\	 ${body} = 	Create Dictionary	powerState=On
	\	 ...							powerControl=MomentaryPress
	\	 ${resp} = 	Fusion Api Edit Server Hardware Power State		body=${body}	uri=${sh_uri_${x}}
	\	 ${task} =	Wait For Task 	${resp}    240s    10s 
	
	sleep    ${Server_power_on_sleep_time}
	
360.10A) LUN Discover server 1
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[0]}               
    ${output1}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
    Run keyword unless       ${output1}== 7    Fail    Log to console and logfile    The count of available LUN is ${output1}
	Log to console and logfile    ${output1}    
360.10B) LUN Discover server 2
	${Server_IP}    ${Gateway_IP}=    Get Windows Server And Gateway IP    ${oa_details}    ${Server_bays[1]}               
	${output2}=    Get Windows LUN Count    ${Server_IP}    ${win_server_details}
	Run keyword unless       ${output2}== 7    Fail    Log to console and logfile    The count of available LUN is ${output2}
	Log to console and logfile    ${output2} 
360.10C) LUN Discover server 3             
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
