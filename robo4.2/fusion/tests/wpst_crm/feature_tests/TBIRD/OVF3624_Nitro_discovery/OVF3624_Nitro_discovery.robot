*** Settings ***
Documentation        OVF3624 Nitro Discovery
...   OVF3624 Nitro Discovery feature test
...   Usage:
...   robot -V data_variables.py -v APPLIANCE_IP:15.245.131.125 OVF3624_Nitro_discovery.robot

Resource        ../../../../../Resources/api/fusion_api_resource.txt
Variables       data_variables.py
Library         Dialogs

Suite Setup        Run FTS and test-specific setup
Suite Teardown        Teardown

# Setup\Teardown for ALL test cases
Test Setup       Common Test Setup
Test Teardown    Common Test Teardown

*** Variables ***
${VM}
${SSH_USER}                     root
${SSH_PASS}                     hpvse1
${FUSION_IP}                    ${APPLIANCE_IP}
${SKIPSETUP}                    ${False}
${SKIPTEARDOWN}                 ${False}

*** Test Cases ***
Create LIGs, EG, LE and verify Nitro modules
    [Documentation]   1.   Create LIGs for 1 FRAME SE A side Redundant LIG for each bay set IBS1, IBS2, IBS3
    ...   2. Create Enclosure Group that uses IBS3 LIG
    ...   3. Check that Nitro module is in 'Monitored' state
    ...   4. Create Logical Enclosure
    ...   5. Check that Nitro module is imported correctly and correct name and part numbers appear
    ...   6. Check that Nitro module is in 'Configured' state
    [Tags]   1
    Run Keyword for Dict    ${ligs}          Add LIG from variable
    Run Keyword for Dict    ${enc_groups}    Add Enclosure Group from variable
    ${les} =    Copy Dictionary          ${les}
    Run Keyword for Dict    ${les}           Add Logical Enclosure from variable

	${icms} =       Get IC   ${NITRO_MODEL}
	${valDict} = 	Create Dictionary	partNumber=${NITRO_PART}
	...                                 model=${NITRO_MODEL}
	...                                 state=Configured
	...                                 status=OK
    Verify ICM data   ${icms}   ${valDict}

Power off and on Nitro Interconnects
    [Documentation]   Power Off Nitro modules, wait for it to become 'Powered Off'
    ...   Power On Nitro modules, wait for it to become 'Powered On'
    [Tags]   2
	${icms} =   Get IC   ${NITRO_MODEL}
	Power ICMs    ${icms}

Rip and Replace Nitro Interconnects with LI
    [Documentation]   EfuseOn Nitro modules, wait for it to become 'Absent'
    ...   EfuseOff Nitro module, wait for it to become 'Configured'
    [Tags]   4
	${icms} =   Get IC   ${NITRO_MODEL}
	Efuse ICMs    ${icms}

Remove LE and verify
    [Documentation]   Remove the Logical Enclosure and verify it is removed successfully
    [Tags]   5
    Power off all servers
    Remove All Server Profiles
    Remove All LEs
    ${icms} =   Get IC   ${NITRO_MODEL}
	${valDict} = 	Create Dictionary	state=Monitored
	...                                 status=OK
    Verify ICM data   ${icms}   ${valDict}

Add LE then Remove LE 10 times
    [Documentation]   Add\Remove the Logical Enclosure and verify it is added\removed successfully
    [Tags]    6
    ${les} =    Copy Dictionary          ${les}
    :FOR	${x}	IN RANGE	0	10
    \   Run Keyword for Dict    ${les}           Add Logical Enclosure from variable
    \   ${icms} =   Get IC   ${NITRO_MODEL}
	\   ${valDict} = 	Create Dictionary	state=Configured
	\   ...                                 status=OK
    \   Verify ICM data   ${icms}   ${valDict}
    \   Remove All LEs
    \   ${icms} =   Get IC   ${NITRO_MODEL}
	\   ${valDict} = 	Create Dictionary	state=Monitored
	\   ...                                 status=OK
    \   Verify ICM data   ${icms}   ${valDict}

Rip and Replace Nitro Interconnects without LI
    [Documentation]   EfuseOn Nitro modules, wait for it to become 'Absent'
    ...   EfuseOff Nitro module, wait for it to become 'Monitored'
    [Tags]   7
	${icms} =   Get IC   ${NITRO_MODEL}
	Efuse ICMs    ${icms}

*** Keywords ***
Enable feature toggle
    [Documentation]    Enables the feature toggle, waits 10 min, then pings appliance
    [Arguments]    ${feature}
    Log    Enabling ${feature} feature toggle    console=True
    ${Id} =         Open Connection    ${APPLIANCE_IP}
    ${Output} =     Login              root     hpvse1
    ${stdout}    ${stderr}    ${rc}=    Execute Command    ${feature_toggle}    return_stderr=True    return_rc=True
    Log    ${stdout}    console=True
    Close Connection
    Sleep    10min
    Wait For Appliance To Become Pingable    ${APPLIANCE_IP}
    Wait For Appliance To Be Ready           ${APPLIANCE_IP}

Get Errors
    [Documentation]     ...
    ${ERRORS}=   Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}

Common Test Setup
    [Documentation]    Pre-conditions for ALL test cases
    Set Log Level    TRACE
    Run Keyword and Ignore Error    Write To ciDebug Log
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

Common Test Teardown
    [Documentation]    Post-conditions for ALL test cases
    fusion api logout appliance
    Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

Run FTS and test-specific setup
    [Documentation]     ...
    Return from keyword if   ${SKIPSETUP} is ${True}
    Set Log Level    TRACE
    #Enable feature toggle   ${feature}
    FTS
    Test Specific Setup

FTS
    [Documentation]     ...
    [Tags]  FTS
    Set Log Level    DEBUG
    log variables
    First Time Setup    DATAFILE=${null}   password=${admin_credentials['password']}    interfaces=bond0

Test Specific Setup
    [Documentation]     ...
    [Tags]  TSS     Setup
    Set Log Level    TRACE
    Run Keyword and Ignore Error    Write To ciDebug Log
    log    [TEST-SPECIFIC SETUP]  console=True
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

    ${users} =                Get Variable Value    ${users}
    Run Keyword If    ${users} is not ${null}    Add Users from variable                ${users}

    ${ethernet_networks} =    Get Variable Value    ${ethernet_networks}
    Run Keyword If    ${ethernet_networks} is not ${null}     Add Ethernet Networks from variable   ${ethernet_networks}

    ${fcoe_networks} =          Get Variable Value        ${fcoe_networks}
    Run Keyword If    ${fcoe_networks} is not ${null}            Add FCoE Networks from variable          ${fcoe_networks}

    ${network_sets} =    Get Variable Value        ${network_sets}
    Run Keyword If    ${network_sets} is not ${null}          Add Network Sets from variable          ${network_sets}

    ${fc_networks} =    Get Variable Value        ${fc_networks}
    Run Keyword If    ${fc_networks} is not ${null}           Add FC Networks from variable          ${fc_networks}

Verify ICM data
    [Documentation]     ...
    [Arguments]     ${icms}   ${valDict}
	:FOR	${ic}	IN      @{icms}
	\ 	Validate Response	${ic}	${valDict}

Efuse ICMs
    [Documentation]     ...
    [Arguments]     ${icms}
	Set Log Level	TRACE
	${l} = 	Get Length	${icms}
	:FOR	${x}	IN RANGE	0	${l}
    \   ${ic} =     Get From List   ${icms}    ${x}
    \   Log to console      ${ic['name']} ${ic['uri']}
    \   ${enc} =    Fetch from left     ${ic['name']}    ,
    \   ${bay} =    Fetch from right    ${ic['name']}    ${SPACE}
    \   Get EM IP       ${enc}
    \   Get EM Token    ${enc}
	\   Log    \t Waiting for ICM in Bay:${bay} to reach state:Configured|Monitored   console=True
    \   Wait Until Keyword Succeeds     3 min   5s      IC reached state    ${ic['uri']}    Configured|Monitored
    \   Run Keyword and Ignore Error    Write To ciDebug Log    [EFUSE ON via RIS (REMOVE ICM)]
    \   Efuse ICM   EFuseOn     ${bay}
	\   Log    \t Waiting for ICM in Bay:${bay} to reach state:Absent    console=True
    \   Wait Until Keyword Succeeds     10 min   15s      IC reached state    ${ic['uri']}    Absent
    \   Run Keyword and Ignore Error    Write To ciDebug Log    [EFUSE OFF via RIS (INSERT ICM)]
    \   Efuse ICM   EFuseOff    ${bay}
	\   Log    \t Waiting for ICM in Bay:${bay} to reach state:Configured|Monitored    console=True
    \   Wait Until Keyword Succeeds     35 min   15s      IC reached state    ${ic['uri']}    Configured|Monitored

Power ICMs
    [Documentation]     ...
    [Arguments]     ${icms}
    Set Log Level	TRACE
    ${icm_len} = 	Get Length	${icms}
    :FOR	${x}	IN RANGE	0	${icm_len}
    \   ${ic} =     Get From List   ${icms}    ${x}
    \   Log to console      ${ic['name']} ${ic['uri']}
    \   ${uri} =    Get From IC     ${ic}   uri
    \   Power request    ${uri}   Off
	\   Log    \t Waiting for ${uri} to reach state:Maintenance    console=True
    \   Wait Until Keyword Succeeds     60 min   30s      IC reached state    ${ic['uri']}    Maintenance
    \   Power request    ${uri}   On
	\   Log    \t Waiting for ${uri} to reach state:Configured    console=True
    \   Wait Until Keyword Succeeds     60 min   30s      IC reached state    ${ic['uri']}    Configured

Power request
    [Documentation]     ...
    [Arguments]     ${uri}    ${power}
    ${data} =   Create Dictionary   op=replace
    ...                             path=/powerState
    ...                             value=${power}
    ${body} =   Create List     ${data}
    Run Keyword and Ignore Error    Write To ciDebug Log    \nPowering ${power}: ${uri}
    ${resp} =   fusion api patch interconnect   body=${body}    uri=${uri}
    ${task} =   Wait for Task   ${resp}  5m   10s
    ${valDict} =    Create Dictionary       status_code=${200}
    ...                                 taskState=Completed
    Validate Response       ${task}   ${valDict}
	Log    \t Waiting for ${uri} to reach powerState:${power}    console=True
    Wait Until Keyword Succeeds     10 min   20s      IC reached powerState    ${uri}    ${power}

IC reached state
    [Documentation]     ...
	[Arguments]	    ${uri}  ${state}
	Set Log Level	TRACE
    ${resp} =   fusion api get resource     ${uri}
	Log    \t ${uri}: ${resp['state']}    console=True
	Should Match Regexp 	${resp['state']}    ${state}
	[Return]	${resp}

IC reached powerState
    [Documentation]     ...
	[Arguments]	    ${uri}  ${state}
	Set Log Level	TRACE
    ${resp} =   fusion api get resource     ${uri}
	Log    \t ${uri}: ${resp['powerState']}    console=True
	Should Match Regexp 	${resp['powerState']}    ${state}
	[Return]	${resp}

Get IC
    [Documentation]     ...
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
    [Documentation]     ...
	[Arguments]	    ${uri}  ${port}
    ${resp} =   fusion api get interconnect ports    uri=${uri}
    ${ics} =     Get From Dictionary     ${resp}    members
	:FOR	${ic}	IN      @{ics}
	\ 	${return} =    Run Keyword If 	'${ic['portName']}' == '${port}'		set variable     ${ic}
	\ 	Exit for loop if  	'${ic['portName']}' == '${port}'
    [Return]    ${return}

Get from IC
    [Documentation]     ...
    [Arguments]     ${ic}   ${element}
    ${return} =     Get From Dictionary     ${ic}   ${element}
    [Return]    ${return}

Teardown
    [Documentation]     ...
    Set Log Level    TRACE
    Return from keyword if   ${SKIPTEARDOWN} is ${True}
    Log    \n[TEARDOWN]   console=True
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Power off ALL Servers
    Remove All Server Profiles
    Remove ALL LS
    Remove ALL LSGs
    Remove All LEs
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Remove All SAS LIGs
    Remove ALL Ethernet Networks
    Remove ALL FC Networks
    Remove ALL FCoE Networks
    Remove ALL Network Sets
    Remove ALL Users
