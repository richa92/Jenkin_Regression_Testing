*** Settings ***
Documentation		OVF269: TAA support for VC Interconnects
...					Usage: robot -V data_variables.py -v APPLIANCE_IP:15.199.232.97 OVF269.robot
...

Suite Setup   		Run FTS and test-specific setup
Suite Teardown		Suite Teardown

Resource            ../../../../resource/fusion_api_all_resource_files.txt

Library				Collections
Library             Dialogs
*** Variables ***
${SSH_PASS}                     hpvse1
${VM}
${SS_MODEL}                     HP VC FlexFabric-20/40 F8 Module
${SS_MODEL_TAA}                 HP VC FlexFabric-20/40 F8 Module  #The FRU on real hardware does NOT say TAA
${SS_PART}                      691367-B21
${SS_PART_TAA}                  691367-B21    #The FRU on real hardware does not show this
${FUSION_IP}                    ${APPLIANCE_IP}
#TODO              Put the correct work product here!
${RALLYWORKPRODUCT}             OVS4774

*** Test Cases ***
Create LIG, EG, import enclosure and verify TAA module
    [Documentation]   Create LIG (MIXED_TAA_SS) SuperShaw TAA bay 1, non TAA bay 2
    ...   ENC 1: Bay 1 SS TAA, Bay 6 SS NON-TAA
    ...   Ethernet only ULS using 1000 Ethernet on both SS modules (BigPipe)
    ...   Converged ULS using 32 FCoE, Ethernet on ENC 1 Bay 1 TAA module (TAA_CONVERGED)
    ...   Create Enclosure Group that uses (MIXED_TAA_SS) LIG
    ...   Import Enclosure
    ...   Check that TAA modules are imported correctly and correct name and part numbers appear
    ...   Create profiles that have connections which use networks on each of the TAA modules
    [Tags]  1

   	Set Log Level	TRACE
	Run Keyword and Ignore Error    Write To ciDebug Log
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

    ${body} =       Build LIG body      ${ligs['${LIG1}']}
	${resp} = 	    Fusion Api Create LIG	${body}
	${task} =	    Wait For Task	${resp} 	60s	2s
	${valDict} = 	Create Dictionary	status_code=${200}
	...                                 taskState=Completed
	Validate Response	${task}	${valDict}

	Run Keyword for List	${enc_groups}	Add Enclosure Group from variable

    #Import Enclosure
	${task} =       Add Enclosures from variable     ${encs}

    #Check that TAA modules are imported correctly and correct name and part numbers appear
    Log    For Delhi, SuperShaw modules are basically not supported. This test will need to be enabled in the future!   level=WARN
    #Check that TAA modules are imported correctly and correct name and part numbers appear
	#${icms} =   Get IC   ${SS_MODEL_TAA}
	#${valDict} = 	Create Dictionary	partNumber=${SS_PART_TAA}
	#...                                 model=${SS_MODEL_TAA}
    #Verify ICM data   ${icms}   ${valDict}

    #Create profiles that have connections which use networks on each of the TAA modules
    Power off all servers
	Add Server Profiles from variable   ${server_profiles}    25m    1m

Rip and Replace TAA Interconnects
    [Documentation]   EfuseOn ENC 1 Bay 1 TAA SS module, wait for it to become 'Absent'
    ...   EfuseOff ENC 1 Bay 1 TAA SS module, wait for it to become 'Configured'
    [Tags]  2
	Run Keyword and Ignore Error    Write To ciDebug Log
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
	${icms} =   Get IC    ${SS_MODEL_TAA}
	Efuse ICMs    ${icms}

Power off and on TAA Interconnects
    [Documentation]   Power Off ENC 1 Bay 1 TAA SS module, wait for it to become 'Powered Off'
    ...   Power On ENC 1 Bay 1 TAA SS module, wait for it to become 'Powered On'
    [Tags]  3
	Run Keyword and Ignore Error    Write To ciDebug Log
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
	${icms} =   Get IC    ${SS_MODEL_TAA}
	Power ICMs    ${icms}

Disable and enable uplink ports on TAA SS modules
    [Documentation]   Enable\disable an uplink port on Bay 1 TAA SS module and verify state changes
    [Tags]  4
	Run Keyword and Ignore Error    Write To ciDebug Log

    Set Log Level	TRACE

	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    ${ic_uri} =   Get IC URI     ${ENC1}, interconnect 1
	${resp} =     Get IC Port    uri=${ic_uri}   port=Q1.1
	Set to Dictionary   ${resp}   enabled    ${false}
    ${body} =    Create List
    Append to list    ${body}    ${resp}

	${resp} =     fusion api edit interconnect ports   uri=${ic_uri}   body=${body}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} =    Create Dictionary	status_code=${200}
	...                                 taskState=Completed
	Validate Response	${task}	${valDict}

	${resp} =     Get IC Port    uri=${ic_uri}   port=Q1.1
	Set to Dictionary   ${resp}   enabled    ${true}
    ${body} =    Create List
    Append to list    ${body}    ${resp}

	${resp} =     fusion api edit interconnect ports   uri=${ic_uri}   body=${body}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} =    Create Dictionary	status_code=${200}
	...                                 taskState=Completed
	Validate Response	${task}	${valDict}

Update from group LI and verify
    [Documentation]   Change LI Uplink set (remove a network)
    ...   Issue UFG LI
    ...   Verify the uplink set returns to correct state
    [Tags]  5
	Run Keyword and Ignore Error    Write To ciDebug Log
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
	${li_uri} = 	Get LI URI   ${LE1}-${LIG1}
	${us} = 		Copy Dictionary	${li_uplink_sets['${US1}']}
	${body} = 		Build US body 	${us}	${li_uri}
	${us_uri} = 	Get Uplinkset URI  	${US1}
	${resp} = 		Fusion Api Edit Uplink Set	body=${body}	uri=${us_uri}
	${task} =       Wait For Task 	${resp} 	15 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...                                 taskState=Completed
	Validate Response	${task}	${valDict}
    ${resp} =       fusion api update from group    ${li_uri}
	${task} =       Wait For Task 	${resp} 	15 min	15s
	${valDict} =    Create Dictionary	status_code=${200}
	...                                 taskState=Completed
	Validate Response	${task}	${valDict}

Update from group LE and verify
    [Documentation]   Change LI Uplink set (add an uplink port)
    ...   Issue UFG LE
    ...   Verify the uplink set returns to correct state
    [Tags]  6
	Run Keyword and Ignore Error    Write To ciDebug Log
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
	${li_uri} = 	Get LI URI   ${LE1}-${LIG1}
	${us} = 		Copy Dictionary	${li_uplink_sets['${US2}']}
	${body} = 		Build US body 	${us}	${li_uri}
	${us_uri} = 	Get Uplinkset URI  	${US2}
	${resp} = 		Fusion Api Edit Uplink Set	body=${body}	uri=${us_uri}
	${task} =       Wait For Task 	${resp} 	15 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...                                 taskState=Completed
	Validate Response	${task}	${valDict}
	${le_uri} =     Get LE URI    ${LE1}
    ${resp} =       fusion api update logical enclosure from group   uri=${le_uri}
	${task} =       Wait For Task 	${resp} 	40 min	15s
	${valDict} =    Create Dictionary	status_code=${200}
	...                                 taskState=Completed
	Validate Response	${task}	${valDict}

Remove Enclosure and verify
    [Documentation]   Remove the Enclosure and verify it is removed successfully
    [Tags]  7
	Run Keyword and Ignore Error    Write To ciDebug Log
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Power off all servers
    Remove All Server Profiles
    ${resp} =       fusion api remove enclosure    name=${ENC1}
	${task} =       Wait For Task 	${resp} 	10 min	5s
	${valDict} = 	Create Dictionary	status_code=${200}
	...                                 taskState=Completed
	Validate Response	${task}	${valDict}

*** Keywords ***
Run FTS and test-specific setup
	Set Log Level	TRACE
    Run Keyword If	${appliance} is not ${null}   FTS
    Test Specific Setup

Set Metadata
    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    ${resp} =    Fusion Api Get Appliance Version
    Set Suite Metadata     OneView Version      ${resp['softwareVersion']}    top=True
	Set Suite Metadata     rallyWorkproduct      ${RALLYWORKPRODUCT}    top=True

FTS
    [Tags]  FTS
	Set Log Level	DEBUG
	log variables
    Get VM IP   ${VM}
	First Time Setup    password=hpvse123    interface=eth0

Test Specific Setup
    [Tags]  TSS     Setup
	Set Log Level	TRACE
	Set Suite Metadata     rallyWorkproduct      ${RALLYWORKPRODUCT}    top=True
	Run Keyword and Ignore Error    Write To ciDebug Log
	Log to console and logfile	[TEST-SPECIFIC SETUP]
    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
	${users} =	Get Variable Value	${users}
	Run Keyword If	${users} is not ${null}	Add Users from variable				${users}
	${ethernet_networks} =	Get Variable Value	${ethernet_networks}
	Run Keyword If	${ethernet_networks} is not ${null}	Add Ethernet Networks from variable	${ethernet_networks}
	${network_sets} =	Get Variable Value	${network_sets}
	Run Keyword If	${network_sets} is not ${null}	Add Network Sets from variable		${network_sets}
	${fc_networks} =	Get Variable Value	${fc_networks}
	Run Keyword If	${fc_networks} is not ${null}	Add FC Networks from variable		${fc_networks}
	${fcoe_networks} =	Get Variable Value	${fcoe_networks}
	Run Keyword If	${fcoe_networks} is not ${null}	Add FCoE Networks from variable		${fcoe_networks}
	${ranges} =	Get Variable Value	${ranges}
	${pools} =  Run Keyword If	${ranges} is not ${null}	Create List		/rest/id-pools/vmac	/rest/id-pools/vwwn	/rest/id-pools/vsn
    Run Keyword If	${ranges} is not ${null}                Run Keyword for List	${pools}	Disable ALL Generated ID Ranges
	Run Keyword If	${ranges} is not ${null}				Add Ranges From variable	${ranges}
	Power Off All Servers

Efuse ICMs
    [Arguments]     ${icms}
	Set Log Level	TRACE
	${l} = 	Get Length	${icms}
	:FOR	${x}	IN RANGE	0	${l}
    \   ${ic} =     Get From List   ${icms}    ${x}
    \   Log to console      ${ic['name']} ${ic['uri']}
    \   ${enc} =    Fetch from left     ${ic['name']}    ,
    \   ${bay} =    Fetch from right    ${ic['name']}    ${SPACE}
	\   fusion_api_appliance_setup.Log to console and logfile  	\t Waiting for ICM in Bay:${bay} to reach state:Configured|Monitored
    \   Wait Until Keyword Succeeds     3 min   5s      IC reached state    ${ic['uri']}    Configured|Monitored
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    [EFUSE OFF via OA]
    \   OA CLI EFUSE      ${OA1_HOST}    ${OA1_USER}		${OA1_PASS}    SWM    ${BAY}    OFF
	\   fusion_api_appliance_setup.Log to console and logfile  	\t Waiting for ICM in Bay:${bay} to reach state:Absent
    \   Wait Until Keyword Succeeds     10 min   15s      IC reached state    ${ic['uri']}    Absent
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    [EFUSE ON via OA]
    \   OA CLI EFUSE      ${OA1_HOST}    ${OA1_USER}		${OA1_PASS}    SWM    ${BAY}    ON
	\   fusion_api_appliance_setup.Log to console and logfile  	\t Waiting for ICM in Bay:${bay} to reach state:Configured|Monitored
    \   Wait Until Keyword Succeeds     35 min   15s      IC reached state    ${ic['uri']}    Configured|Monitored

Power ICMs
    [Arguments]     ${icms}
    Set Log Level	TRACE
    ${icm_len} = 	Get Length	${icms}
    :FOR	${x}	IN RANGE	0	${icm_len}
    \   ${ic} =     Get From List   ${icms}    ${x}
    \   Log to console      ${ic['name']} ${ic['uri']}
    \   ${uri} =    Get From IC     ${ic}   uri
    \   ${enc} =    Fetch from left     ${ic['name']}    ,
    \   ${bay} =    Fetch from right    ${ic['name']}    ${SPACE}
    \   OA CLI POWEROFF      ${OA1_HOST}    ${OA1_USER}		${OA1_PASS}    INTERCONNECT    ${BAY}
	\   fusion_api_appliance_setup.Log to console and logfile  	\t Waiting for ${uri} to reach powerState: Off
    \   Wait Until Keyword Succeeds     10 min   20s      IC reached powerState    ${uri}    Off
	\   fusion_api_appliance_setup.Log to console and logfile  	\t Waiting for ${uri} to reach state:Mointenance
    \   Wait Until Keyword Succeeds     60 min   30s      IC reached state    ${ic['uri']}    Maintenance
    \   sleep    1m
    \   OA CLI POWERON       ${OA1_HOST}    ${OA1_USER}		${OA1_PASS}    INTERCONNECT    ${BAY}
	\   fusion_api_appliance_setup.Log to console and logfile  	\t Waiting for ${uri} to reach powerState: On
    \   Wait Until Keyword Succeeds     10 min   20s      IC reached powerState    ${uri}    On
	\   fusion_api_appliance_setup.Log to console and logfile  	\t Waiting for ${uri} to reach state:Configured
    \   Wait Until Keyword Succeeds     60 min   30s      IC reached state    ${ic['uri']}    Configured

IC reached state
	[Arguments]	    ${uri}  ${state}
	Set Log Level	TRACE
    ${resp} =   fusion api get resource     ${uri}
	fusion_api_appliance_setup.Log to console and logfile  	\t ${uri}: ${resp['state']}
	Should Match Regexp 	${resp['state']}    ${state}
	[Return]	${resp}

IC reached powerState
	[Arguments]	    ${uri}  ${state}
	Set Log Level	TRACE
    ${resp} =   fusion api get resource     ${uri}
	fusion_api_appliance_setup.Log to console and logfile  	\t ${uri}: ${resp['powerState']}
	Should Match Regexp 	${resp['powerState']}    ${state}
	[Return]	${resp}

Get IC
	[Arguments]	    ${model}
    ${resp} =   fusion api get interconnect
    ${ic_list} =    Create List
    ${ics} =     Get From Dictionary     ${resp}    members
	${l} = 	Get Length	${ics}
	:FOR	${x}	IN RANGE	0	${l}
    \   ${ic} =     Get From List   ${ics}    ${x}
	\ 	Run Keyword If 	'${ic['model']}' != '${model}'		Continue For Loop
	\   Append to list      ${ic_list}  ${ic}
    #${ordered_list} =   helper.order_icms    ${ic_list}     ${ICM_ORDER}

    [Return]    ${ic_list}

Get IC Port
	[Arguments]	    ${uri}  ${port}
    ${resp} =   fusion api get interconnect ports    uri=${uri}
    ${ics} =     Get From Dictionary     ${resp}    members
	:FOR	${ic}	IN      @{ics}
	\ 	${return} =    Run Keyword If 	'${ic['portName']}' == '${port}'		set variable     ${ic}
	\ 	Exit for loop if  	'${ic['portName']}' == '${port}'
    [Return]    ${return}

Get from IC
    [Arguments]     ${ic}   ${element}
    ${return} =     Get From Dictionary     ${ic}   ${element}
    [Return]    ${return}

Verify ICM data
    [Arguments]     ${icms}   ${valDict}
	:FOR	${ic}	IN      @{icms}
	\ 	Validate Response	${ic}	${valDict}
