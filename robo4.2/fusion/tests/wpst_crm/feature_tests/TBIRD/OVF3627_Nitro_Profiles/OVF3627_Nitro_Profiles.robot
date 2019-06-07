*** Settings ***
Documentation        OVF3627 Nitro Profiles
...   OVF3627 Nitro Uplinksets feature test
...   Usage:
...   robot -V data_variables.py -v APPLIANCE_IP:15.245.131.125 OVF3625_Nitro_Profiles.robot

Resource        ../../../../../Resources/api/fusion_api_resource.txt
Variables       data_variables.py

Suite Setup        Run FTS and test-specific setup
#Suite Teardown        Teardown

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
Should be able to create server profiles
    [Documentation]   ...
    [Tags]   1    POS
    ${server_profiles} =    Get Variable Value    ${server_profiles}
    ${tasks} =    Run Keyword If    ${server_profiles} is not ${null}        Add Server Profiles from variable    ${server_profiles}
    Wait For Task2    ${tasks}    15m    15
	Power On All Servers
	Sleep  5m

Should be able to exercise East West traffic
    [Documentation]   ...
    [Tags]   2    POS
    ping east west

Should be able to exercise North South traffic
    [Documentation]   ...
    [Tags]   3    POS
    ping north south

Should be able to unassign and reassign profiles
    [Documentation]   ...
    [Tags]   4    POS
    Power off ALL servers
    ${pros} =    fusion api get server profiles
    ${ps} =      Copy dictionary    ${pros}
    ${tasks} =   Create List
    # unassign
    :FOR    ${p}    IN    @{pros['members']}
    \   set to dictionary    ${p}   serverHardwareUri=${None}
    \   set to dictionary    ${p}   enclosureBay=${None}
    \   set to dictionary    ${p}   enclosureUri=${None}
    \   ${resp} =   fusion api edit server profile    uri=${p['uri']}   body=${p}
    \   Append to list   ${tasks}   ${resp}
    Wait for Task2    ${tasks}    25m   15
    # reassign
    ${tasks} =   Create List
    :FOR    ${p}    IN    @{ps['members']}
    \   ${headers} =    fusion api get headers
    \   set to dictionary    ${headers}    If-Match    *
    \   ${resp} =   fusion api edit server profile    uri=${p['uri']}   body=${p}   headers=${headers}
    \   Append to list   ${tasks}   ${resp}
    Wait for Task2    ${tasks}    25m   15
    # poweron
    Power on all servers
  	Sleep  5m

    # ping
    wait until keyword succeeds    7m    30s    ping north south
    wait until keyword succeeds    2m    15s    ping east west

*** Keywords ***
ping east west
    [Documentation]    ...
    SSH to host and ping x    root    hpvse1    ${ENC1_BAY1_IPS[0]}    ${ENC1_BAY2_IPS[1]}
    SSH to host and ping x    root    hpvse1    ${ENC1_BAY2_IPS[0]}    ${ENC1_BAY1_IPS[1]}

ping north south
    [Documentation]    ...
    Run Keyword for List    ${ENC1_BAY1_IPS}   Wait For Appliance To Become Pingable
    Run Keyword for List    ${ENC1_BAY2_IPS}   Wait For Appliance To Become Pingable

SSH to host and ping x
    [Documentation]    SSH's to a given host, then pings an IP from that host
    [Arguments]	       ${usr}    ${pass}    ${HOST}    ${HOST2}
    Open Connection And Log In      ${HOST}    ${usr}    ${pass}
    ${Output}=    Execute Command    ping -c 4 ${HOST2}    return_stdout=True    return_rc=False
    Log to console and logfile    ${Output}
    Should Contain    ${Output}    ttl=
    Close All Connections

Create EG, LE and verify Nitro modules go from Monitored to Configured state
    [Documentation]    ...
    #${icms} =   Get IC   ${NITRO_MODEL}
    ${valDict} =     Create Dictionary    state=Monitored
    ...                                   status=OK
    Verify ICM data   ${NITRO_MODEL}   ${valDict}
    Run Keyword for Dict    ${enc_groups}    Add Enclosure Group from variable
    ${les} =    Copy Dictionary          ${les}
    Run Keyword for Dict    ${les}           Add Logical Enclosure from variable
    ${valDict} =     Create Dictionary    state=Configured
    ...                                   status=OK
    wait until keyword succeeds      5m    5s    Verify ICM data   ${NITRO_MODEL}   ${valDict}

Add Ethernet Networks from variable
    [Documentation]    Adds Ethernet networks to an appliance from a variable which contains a list of dicts with the entire payload
    [Arguments]        ${networks}
    Log    \nAdding ETHERNET NETWORKS    console=True
    :FOR    ${net}    IN    @{networks}
    \        ${resp} =     Fusion Api Create Ethernet Network        body=${net}

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
    ${ERRORS}=   Run Keyword and Ignore Error    Get from ciDebug Log     ...

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

    ${network_sets} =    Get Variable Value        ${network_sets}
    Run Keyword If    ${network_sets} is not ${null}          Add Network Sets from variable          ${network_sets}

    ${ligs} =      Get Variable Value   ${ligs}
    Run Keyword If     ${ligs} is not ${null}                 Run Keyword for dict    ${ligs}    Add LIG from variable

    Create EG, LE and verify Nitro modules go from Monitored to Configured state

	${ranges} =	Get Variable Value	${ranges}
	${pools} =  Run Keyword If	${ranges} is not ${null}	Create List		/rest/id-pools/vmac	/rest/id-pools/vwwn	/rest/id-pools/vsn
    Run Keyword If	${ranges} is not ${null}                Run Keyword for List	${pools}	Disable ALL Generated ID Ranges
	Run Keyword If	${ranges} is not ${null}				Add Ranges From variable	${ranges}

	Power Off All Servers

    #${server_profiles} =    Get Variable Value    ${server_profiles}
    #Run Keyword If    ${server_profiles} is not ${null}        Add Server Profiles from variable    ${server_profiles}


Verify ICM data
    [Documentation]     ...
    [Arguments]     ${model}   ${valDict}
    ${icms} =   Get IC   ${model}
    :FOR    ${ic}    IN      @{icms}
    \     Validate Response    ${ic}    ${valDict}

IC reached state
    [Documentation]     ...
    [Arguments]        ${uri}  ${state}
    Set Log Level    TRACE
    ${resp} =   fusion api get resource     ${uri}
    Log    \t ${uri}: ${resp['state']}    console=True
    Should Match Regexp     ${resp['state']}    ${state}
    [Return]    ${resp}

Get IC
    [Documentation]     ...
    [Arguments]        ${model}
    ${resp} =   fusion api get interconnect
    ${ic_list} =    Create List
    ${ics} =     Get From Dictionary     ${resp}    members
    ${l} =     Get Length    ${ics}
    :FOR    ${x}    IN RANGE    0    ${l}
    \   ${ic} =     Get From List   ${ics}    ${x}
    \     Run Keyword If     '${ic['model']}' != '${model}'        Continue For Loop
    \   Append to list      ${ic_list}  ${ic}
    #${ordered_list} =   helper.order_icms    ${ic_list}     ${ICM_ORDER}

    [Return]    ${ic_list}

Get IC Port
    [Documentation]     ...
    [Arguments]        ${uri}  ${port}
    ${resp} =   fusion api get interconnect ports    uri=${uri}
    ${ics} =     Get From Dictionary     ${resp}    members
    :FOR    ${ic}    IN      @{ics}
    \     ${return} =    Run Keyword If     '${ic['portName']}' == '${port}'        set variable     ${ic}
    \     Exit for loop if      '${ic['portName']}' == '${port}'
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
