*** Settings ***
Documentation        OVF266 SmartLink
...   OVF266 SmartLink feature test
...   Usage:
...   robot -V data_variables.py -v APPLIANCE_IP:16.114.208.62 OVF266_SmartLink.robot

Resource        ../../../../../Resources/api/fusion_api_resource.txt
Variables       data_variables.py
Library         Dialogs

#Suite Setup        Test Specific setup
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
${skipsetup}                    ${False}

*** Test Cases ***
Should be able to create a new Tagged Ethernet network with SmartLink
    [Documentation]    Should be able to create a new Ethernet network with SmartLink
    [Tags]             Networks    Positive    001
    ${resp}            fusion api create ethernet network    ${nets['net_2001']}
    Wait For Task2     ${resp}

Should be able to edit a Tagged Ethernet network and enable SmartLink
    [Documentation]    Should be able to edit an Ethernet network and enable SmartLink
    [Tags]             Networks    Positive    002
    ${uri}             Common URI lookup by name   ETH:net_2000
    ${net}             Get Resource by URI   ${uri}
    Set to Dictionary         ${net}    smartLink   ${True}
    Remove from Dictionary    ${net}    status_code   headers
    ${resp}            fusion api edit ethernet network    uri=${uri}   body=${net}
    Wait For Task2     ${resp}

Should be able to edit a Tagged Ethernet network and disable SmartLink
    [Documentation]           Should be able to edit an Ethernet network and disable SmartLink
    [Tags]                    Networks    Positive    003
    ${uri}                    Common URI lookup by name   ETH:net_2000
    ${net}                    Get Resource by URI   ${uri}
    Set to Dictionary         ${net}    smartLink   ${False}
    Remove from Dictionary    ${net}    status_code   headers
    ${resp}                   fusion api edit ethernet network    uri=${uri}   body=${net}
    Wait For Task2            ${resp}

Should not be able to create an FCoE network with SmartLink
    [Documentation]     Should not be able to create an FCoE network with SmartLink
    [Tags]              Networks    Negative    004
    ${resp}             fusion api create fcoe network    body=${nets['fcoe']}
    ${valDict}          Create Dictionary    status_code=${400}
    ...                                     errorCode=UNRECOGNIZED_JSON_FIELD
    Validate Response   ${resp}   ${valDict}

Should not be able to create an FC network with SmartLink
    [Documentation]    Should not be able to create an FCoE network with SmartLink
    [Tags]             Networks    Negative    005
    ${resp}            fusion api create fc network    body=${nets['fc']}
    ${valDict}         Create Dictionary    status_code=${400}
    ...                                     errorCode=UNRECOGNIZED_JSON_FIELD
    Validate Response  ${resp}   ${valDict}

Should be able to create a new Untagged Ethernet network with SmartLink
    [Documentation]    Should be able to create a new Untagged Ethernet network with SmartLink
    [Tags]             Networks    Positive    006
    ${resp}            fusion api create ethernet network    ${nets['untagged']}
    Wait For Task2     ${resp}

Should be able to create a new Tunnel Ethernet network with SmartLink
    [Documentation]    Should be able to create a new Tunnel Ethernet network with SmartLink
    [Tags]             Networks    Positive    007
    ${resp}            fusion api create ethernet network    ${nets['tunnel']}
    Wait For Task2     ${resp}

Should be able to shutdown A-side BAGG on ToR to trigger SmartLink
    [Documentation]    Should be able to bring down A-side BAGG on ToR and get SmartLink to fire.
    ...    Pings should continue to work.
    [Tags]             Positive   dlink  aside    008
    # Start pinging

    #pause execution    message=show blade teams are up and up

    wait until keyword succeeds    15min    15s    Downlink status should be   ${ENC1_BAY1_DLINKS['aside']['icm']}    ${ENC1_BAY1_DLINKS['aside']['port']}    Linked
    wait until keyword succeeds    15min    15s    Subport status should be    ${ENC1_BAY1_DLINKS['aside']['icm']}    ${ENC1_BAY1_DLINKS['aside']['port']}    ${ENC1_BAY1_DLINKS['aside']['up']}

    wait until keyword succeeds    10min   15s   ConnectionInstance Alert Count is zero should Be ${True}
    #pause execution    message=about to bring down A side - Alerts will fire, subports will go down, OS team half down

    Change BAGG    ${tor['ipv4']}    ${tor['user']}    ${tor['pass']}    ${tor['config1']['aside_bagg']['name']}    shutdown
    wait until keyword succeeds    10min   15s   ConnectionInstance Alert Count is zero should Be ${False}
    wait until keyword succeeds    15min   15s    Downlink status should be   ${ENC1_BAY1_DLINKS['aside']['icm']}    ${ENC1_BAY1_DLINKS['aside']['port']}    Linked
    wait until keyword succeeds    15min    15s    Subport status should be    ${ENC1_BAY1_DLINKS['aside']['icm']}    ${ENC1_BAY1_DLINKS['aside']['port']}    ${ENC1_BAY1_DLINKS['aside']['down']}
    # pinging should still be working

Should be able to shutdown B-side BAGG on ToR to trigger SmartLink
    [Documentation]    Should be able to bring down B-side BAGG on ToR and get SmartLink to fire.
    ...    Pinging should fail since both sides are now down.
    [Tags]             Positive   dlink    bside    009
    #Start pinging
    wait until keyword succeeds    15min    15s    Downlink status should be   ${ENC1_BAY1_DLINKS['bside']['icm']}    ${ENC1_BAY1_DLINKS['bside']['port']}    Linked
    wait until keyword succeeds    15min    15s    Subport status should be    ${ENC1_BAY1_DLINKS['bside']['icm']}    ${ENC1_BAY1_DLINKS['bside']['port']}    ${ENC1_BAY1_DLINKS['bside']['up']}
    ${alerts} =    ConnectionInstance Alert Count is zero should Be ${False}

    #pause execution    message=about to bring down B side - Alerts will fire, subports will go down, OS team all down

    Change BAGG    ${tor['ipv4']}    ${tor['user']}    ${tor['pass']}    ${tor['config1']['bside_bagg']['name']}    shutdown
    wait until keyword succeeds    10min   15s   ConnectionInstance Alert Count should be greater than ${alerts}
    wait until keyword succeeds    15min    15s    Downlink status should be   ${ENC1_BAY1_DLINKS['bside']['icm']}    ${ENC1_BAY1_DLINKS['bside']['port']}    Linked
    wait until keyword succeeds    15min    15s    Subport status should be    ${ENC1_BAY1_DLINKS['bside']['icm']}    ${ENC1_BAY1_DLINKS['bside']['port']}    ${ENC1_BAY1_DLINKS['bside']['down']}
    #pinging should fail

Should be able to bring both A and B sides BAGG on ToR back up to trigger SmartLink
    [Documentation]    Should be able to bring down B-side BAGG on ToR and get SmartLink to fire.
    ...    Pinging should fail since both sides are down, but then start working when they are brought up.
    [Tags]             Positive   baggup  dlink   both    010
    #Start pinging, should be failing

    #pause execution    message=about to bring down AB up - Alerts will clear, subports will go up, OS team all up

    Change BAGG    ${tor['ipv4']}    ${tor['user']}    ${tor['pass']}    ${tor['config1']['aside_bagg']['name']}    undo shutdown
    Change BAGG    ${tor['ipv4']}    ${tor['user']}    ${tor['pass']}    ${tor['config1']['bside_bagg']['name']}    undo shutdown
    wait until keyword succeeds    10min   15s   ConnectionInstance Alert Count is zero should Be ${True}
    wait until keyword succeeds    15min    15s    Downlink status should be   ${ENC1_BAY1_DLINKS['aside']['icm']}    ${ENC1_BAY1_DLINKS['aside']['port']}    Linked
    wait until keyword succeeds    15min    15s    Subport status should be    ${ENC1_BAY1_DLINKS['aside']['icm']}    ${ENC1_BAY1_DLINKS['aside']['port']}    ${ENC1_BAY1_DLINKS['aside']['up']}
    wait until keyword succeeds    15min    15s    Downlink status should be   ${ENC1_BAY1_DLINKS['bside']['icm']}    ${ENC1_BAY1_DLINKS['bside']['port']}    Linked
    wait until keyword succeeds    15min    15s    Subport status should be    ${ENC1_BAY1_DLINKS['bside']['icm']}    ${ENC1_BAY1_DLINKS['bside']['port']}    ${ENC1_BAY1_DLINKS['bside']['up']}
    #pinging should succeed

    #pause execution    message=everything should be happy again at this point


Change LIGs, ToR config and Profiles for remaining tests
    [Documentation]    ...
    [Tags]             Positive    011
    #* Change config file to needed config for the remaining tests
    Load 5900 configuration    ${tor['ipv4']}    ${tor['user']}    ${tor['pass']}   ${tor['config2']['cfg_file']}
    Wait For Appliance To Become Pingable     ${tor['ipv4']}

    Set to dictionary    ${ligs['${LIG2}']}    uplinkSets   ${aside_uplink_sets2}
    Edit LIG    ${LIG2}    ${ligs['${LIG2}']}

    Set to dictionary    ${ligs['${LIG3}']}    uplinkSets   ${bside_uplink_sets2}
    Edit LIG    ${LIG3}    ${ligs['${LIG3}']}

    # LE Update from Group
    Update Logical Enclosure from Group    ${les['${LE1}']}    verify=True
    # change profiles for bay 1/2
    Run keyword for list    ${SERVERS}    Power off server
    ${resp} =    Edit Connections    ${ENC1}bay1    ${edit_conns['bay1a']}    15m   15s
    ${resp} =    Edit Connections    ${ENC1}bay2    ${edit_conns['bay2a']}    15m   15s
    Run keyword for list    ${SERVERS}    Power on server


Check subports after US-2 connectivity is lost
    [Documentation]    ...
    [Tags]             Positive    012
    #* When UplinkSet-1 connectivity is okay, the S-Channel-3 and S-Channel-4 should be up.
    wait until keyword succeeds    10min   15s   ConnectionInstance Alert Count is zero should Be ${True}
    wait until keyword succeeds    15min    15s    Subport status should be    ${ENC1_BAY1_DLINKS2['aside']['icm']}    ${ENC1_BAY1_DLINKS2['aside']['port']}    ${ENC1_BAY1_DLINKS2['aside']['up']}
    wait until keyword succeeds    15min    15s    Subport status should be    ${ENC1_BAY1_DLINKS2['bside']['icm']}    ${ENC1_BAY1_DLINKS2['bside']['port']}    ${ENC1_BAY1_DLINKS2['bside']['up']}
    wait until keyword succeeds    15min    15s    Subport status should be    ${ENC1_BAY2_DLINKS2['aside']['icm']}    ${ENC1_BAY2_DLINKS2['aside']['port']}    ${ENC1_BAY2_DLINKS2['aside']['up']}
    wait until keyword succeeds    15min    15s    Subport status should be    ${ENC1_BAY2_DLINKS2['bside']['icm']}    ${ENC1_BAY2_DLINKS2['bside']['port']}    ${ENC1_BAY2_DLINKS2['bside']['up']}
    #* When UplinkSet-2 connectivity is lost, the S-Channel-4 should be up, S-Channel-3 (Net-D) should be down.
    Change BAGG    ${tor['ipv4']}    ${tor['user']}    ${tor['pass']}    ${tor['config2']['bside_bagg2']['name']}    shutdown
    wait until keyword succeeds    10min   15s   ConnectionInstance Alert Count is zero should Be ${False}
    wait until keyword succeeds    15min    15s    Subport status should be    ${ENC1_BAY2_DLINKS2['bside']['icm']}    ${ENC1_BAY2_DLINKS2['bside']['port']}    ${ENC1_BAY2_DLINKS2['bside']['down']}
    # Bring BAGGs back up
    Change BAGG    ${tor['ipv4']}    ${tor['user']}    ${tor['pass']}    ${tor['config2']['bside_bagg2']['name']}    undo shutdown
    wait until keyword succeeds    10min   15s   ConnectionInstance Alert Count is zero should Be ${True}
    wait until keyword succeeds    15min    15s    Subport status should be    ${ENC1_BAY2_DLINKS2['bside']['icm']}    ${ENC1_BAY2_DLINKS2['bside']['port']}    ${ENC1_BAY2_DLINKS2['bside']['up']}

Check subports when US1 and US2 are lost
    [Documentation]    ...
    [Tags]             Positive    013
    wait until keyword succeeds    10min   15s   ConnectionInstance Alert Count is zero should Be ${True}
    wait until keyword succeeds    15min   15s    Subport status should be    ${ENC1_BAY1_DLINKS2['aside']['icm']}    ${ENC1_BAY1_DLINKS2['aside']['port']}    ${ENC1_BAY1_DLINKS2['aside']['up']}
    wait until keyword succeeds    15min   15s    Subport status should be    ${ENC1_BAY1_DLINKS2['bside']['icm']}    ${ENC1_BAY1_DLINKS2['bside']['port']}    ${ENC1_BAY1_DLINKS2['bside']['up']}
    wait until keyword succeeds    15min   15s    Subport status should be    ${ENC1_BAY2_DLINKS2['aside']['icm']}    ${ENC1_BAY2_DLINKS2['aside']['port']}    ${ENC1_BAY2_DLINKS2['aside']['up']}
    wait until keyword succeeds    15min   15s    Subport status should be    ${ENC1_BAY2_DLINKS2['bside']['icm']}    ${ENC1_BAY2_DLINKS2['bside']['port']}    ${ENC1_BAY2_DLINKS2['bside']['up']}
    #if UplinkSet-1 connectivity is lost, the S-Channel-4(NetSetAD)  should be down and S-Channel-3(Net-C) should be up.
    #if UplinkSet-2 connectivity is lost, the S-Channel-4 (NetSetABC) should be up and S-Channel-3 should be down.
    Change BAGG    ${tor['ipv4']}    ${tor['user']}    ${tor['pass']}    ${tor['config2']['aside_bagg1']['name']}    shutdown
    sleep    5s
    Change BAGG    ${tor['ipv4']}    ${tor['user']}    ${tor['pass']}    ${tor['config2']['aside_bagg2']['name']}    shutdown
    wait until keyword succeeds    10min   15s   ConnectionInstance Alert Count is zero should Be ${False}
    wait until keyword succeeds    15min   15s    Subport status should be    ${ENC1_BAY1_DLINKS2['aside']['icm']}    ${ENC1_BAY1_DLINKS2['aside']['port']}    ${ENC1_BAY1_DLINKS2['aside']['down2']}
    wait until keyword succeeds    15min   15s    Subport status should be    ${ENC1_BAY2_DLINKS2['aside']['icm']}    ${ENC1_BAY2_DLINKS2['aside']['port']}    ${ENC1_BAY2_DLINKS2['aside']['down2']}
    # Bring BAGGs back up
    Change BAGG    ${tor['ipv4']}    ${tor['user']}    ${tor['pass']}    ${tor['config2']['aside_bagg1']['name']}    undo shutdown
    sleep    5s
    Change BAGG    ${tor['ipv4']}    ${tor['user']}    ${tor['pass']}    ${tor['config2']['aside_bagg2']['name']}    undo shutdown
    wait until keyword succeeds    10min   15s   ConnectionInstance Alert Count is zero should Be ${True}
    wait until keyword succeeds    15min   15s    Subport status should be    ${ENC1_BAY1_DLINKS2['aside']['icm']}    ${ENC1_BAY1_DLINKS2['aside']['port']}    ${ENC1_BAY1_DLINKS2['aside']['up']}
    wait until keyword succeeds    15min   15s    Subport status should be    ${ENC1_BAY1_DLINKS2['bside']['icm']}    ${ENC1_BAY1_DLINKS2['bside']['port']}    ${ENC1_BAY1_DLINKS2['bside']['up']}
    wait until keyword succeeds    15min   15s    Subport status should be    ${ENC1_BAY2_DLINKS2['aside']['icm']}    ${ENC1_BAY2_DLINKS2['aside']['port']}    ${ENC1_BAY2_DLINKS2['aside']['up']}
    wait until keyword succeeds    15min   15s    Subport status should be    ${ENC1_BAY2_DLINKS2['bside']['icm']}    ${ENC1_BAY2_DLINKS2['bside']['port']}    ${ENC1_BAY2_DLINKS2['bside']['up']}

Verify Smartlink fires when ULS is in LAG mismatch with ToR
    [Documentation]    Create 2 uplink sets (US-1 & US-2 ) with 2 ports each and 1 SL enabled Ethernet network in each
    ...    Put all 4 ToR switch interfaces in the same LAG
    ...    Verify 1 uplink set is Active on both ports
    ...    Verify the other uplink set has both ports in standby
    ...    Verify smartlink shuts down the down port for the network that in the standby ULS
    ...    Identify the interfaces on the ToR which are used by the Standby ULS. Put these interfaces in their own LAG
    ...    Verify the ULS ports become Active- Verify smartlink re-enables the down port
    [Tags]             Positive   014
    Edit US    US1a    ${LE1}-${LIG2}    ${us['US1a']}
    Edit US    US2a    ${LE1}-${LIG2}    ${us['US2a']}
    Edit US    US1b    ${LE1}-${LIG3}    ${us['US1b']}
    Edit US    US2b    ${LE1}-${LIG3}    ${us['US2b']}

    Load 5900 configuration    ${tor['ipv4']}    ${tor['user']}    ${tor['pass']}   ${tor['config1']['cfg_file']}
    Wait For Appliance To Become Pingable     ${tor['ipv4']}
    wait until keyword succeeds    10min   15s   ConnectionInstance Alert Count is zero should Be ${False}
    wait until keyword succeeds    15min   15s    Uplink portStatusReason should be    ${ENC1}, interconnect 3    Q5:1    Active
    wait until keyword succeeds    15min   15s    Uplink portStatusReason should be    ${ENC1}, interconnect 3    Q5:2    Active
    wait until keyword succeeds    15min   15s    Uplink portStatusReason should be    ${ENC1}, interconnect 3    Q5:3    StandBy
    wait until keyword succeeds    15min   15s    Uplink portStatusReason should be    ${ENC1}, interconnect 3    Q5:4    StandBy
    wait until keyword succeeds    15min   15s    Subport status should be    ${ENC1_BAY2_DLINKS2['aside']['icm']}    ${ENC1_BAY2_DLINKS2['aside']['port']}    ${ENC1_BAY2_DLINKS2['aside']['down2']}

    Load 5900 configuration    ${tor['ipv4']}    ${tor['user']}    ${tor['pass']}   ${tor['config2']['cfg_file']}
    Wait For Appliance To Become Pingable     ${tor['ipv4']}
    wait until keyword succeeds    10min   15s   ConnectionInstance Alert Count is zero should Be ${True}
    wait until keyword succeeds    15min    15s    Uplink portStatusReason should be    ${ENC1}, interconnect 3    Q5:1    Active
    wait until keyword succeeds    15min    15s    Uplink portStatusReason should be    ${ENC1}, interconnect 3    Q5:2    Active
    wait until keyword succeeds    15min    15s    Uplink portStatusReason should be    ${ENC1}, interconnect 3    Q5:3    Active
    wait until keyword succeeds    15min    15s    Uplink portStatusReason should be    ${ENC1}, interconnect 3    Q5:4    Active
    wait until keyword succeeds    15min    15s    Subport status should be    ${ENC1_BAY2_DLINKS2['aside']['icm']}    ${ENC1_BAY2_DLINKS2['aside']['port']}    ${ENC1_BAY2_DLINKS2['aside']['up']}

*** Keywords ***
Enable feature toggle
    [Documentation]    Enables the feature toggle, waits 10 min, then pings appliance
    [Arguments]    ${feature}
    Log    Enabling ${feature} feature toggle    console=True
    ${Id} =         Open Connection    ${APPLIANCE_IP}
    ${Output} =     Login              root     hpvse1
    ${Command} =    set variable    /ci/bin/set-feature-toggles -e ${feature}
    ${stdout}    ${stderr}    ${rc}=    Execute Command    ${Command}    return_stderr=True    return_rc=True
    Log    ${stdout}    console=True
    Close Connection
    Sleep    10min
    Wait For Appliance To Become Pingable    ${APPLIANCE_IP}
    Wait For Appliance To Be Ready           ${APPLIANCE_IP}

Edit Connections
    [Documentation]    Edits a profile's connections only
    [Arguments]    ${name}    ${conns}   ${timeout}   ${interval}
    ${profile} =          Get Resource  SP:${name}
    remove from dictionary    ${profile}    status_code    headers
    ${profile_uri} =      Get From Dictionary        ${profile}  uri
    ${connections} =      Lookup Connection Uris     ${conns}
    Set to Dictionary     ${profile['connectionSettings']}   connections   ${connections}
    ${resp} =     Fusion Api Edit Server Profile     body=${profile}        uri=${profile_uri}
    ${task} =     Wait for Task    ${resp}   timeout=${timeout}   interval=${interval}
    ${valDict} =    Create Dictionary   taskState=Completed
    Validate Response   ${task} ${valDict}
    [Return]  ${task}

Edit LIG
    [Documentation]    Edits the LIG
    [Arguments]    ${name}    ${body}
    ${body} =   Build LIG body      ${body}
    # Get info from the current LIG to apply edits to
    ${lig} =        Get LIG Member      ${name}
    ${lig_uri} =    Get LIG Uri         ${name}
    ${ethernetSettings} =   Get From Dictionary   ${lig}  ethernetSettings
    Set to dictionary   ${body}     ethernetSettings    ${ethernetSettings}
    ${resp} =   Fusion Api Edit LIG body=${body}    uri=${lig_uri}
    ${task} =   Wait For Task   ${resp}     120s    2s

Edit US
    [Documentation]    Edits the US
    [Arguments]    ${name}    ${li}    ${us}
    ${li_uri} =     Common URI lookup by name   LI:${li}
    ${body} =       Build US body   ${us}   ${li_uri}
    ${us_uri} =     Common URI lookup by name    US:${name}
    ${resp} =       Fusion Api Edit Uplink Set  body=${body}    uri=${us_uri}
    ${task} =       Wait For Task   ${resp}     5 min   5s
    ${valDict} =    Create Dictionary   taskState=Completed
    Validate Response    ${task}    ${valDict}

Common Test Setup
    [Documentation]    Pre-conditions for ALL test cases
    Set Log Level    TRACE
    Run Keyword and Ignore Error    Write To ciDebug Log
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

Common Test Teardown
    [Documentation]    Post-conditions for ALL test cases
    fusion api logout appliance
    Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

Get port
    [Documentation]    Retrieves the requested port data for the given interconnect uri
    ...     ex:   icm=CN75016BG8, interconnect 3   port=d1
    [Arguments]    ${icm}    ${port}
    ${uri} =     Create IC Port URI   ${icm}    ${port}
    ${resp} =    fusion api get resource    uri=${uri}
    [Return]    ${resp}

Downlink status should be
    [Documentation]    Compares downlink portStatus
    [Arguments]     ${icm}    ${port}   ${status}
    ${dlink} =    Get port    ${icm}    ${port}
    should be equal as strings    ${dlink['portStatus']}   ${status}

Uplink portStatusReason should be
    [Documentation]    Compares downlink portStatus
    [Arguments]     ${icm}    ${port}   ${status}
    ${dlink} =    Get port    ${icm}    ${port}
    should be equal as strings    ${dlink['portStatusReason']}   ${status}

Subport status should be
    [Documentation]    Compares downlink subport portStatus
    [Arguments]     ${icm}    ${port}   ${subports}
    ${dlink} =    Get port    ${icm}    ${port}
    lists should be equal    ${dlink['subports']}   ${subports}

Load 5900 configuration
    [Documentation]    Loads a given .cfg file that exists on the 5900 and reboots the switch
    [Arguments]        ${TOR_IPV4}    ${TOR_USER}    ${TOR_PASS}   ${CFG_FILE}
    Log   \nLoading: ${CFG_FILE} on TOR    console=True
    Open Connection And Log In      ${TOR_IPV4}    ${TOR_USER}    ${TOR_PASS}
    Write    startup saved-configuration ${CFG_FILE}\r
    sleep    5s
    ${output}=    Read
    #Should not contain    ${output}    The configuration file is invalid or not exist
    sleep    5s
    Write    reboot force
    sleep    5s
    ${output}=    Read
    Should contain    ${output}    This command will reboot the device. Continue? [Y/N]:
    Write    y
    sleep    5s
    ${output}=    Read
    Close All Connections
    log   ${output}    console=True
    sleep    4min
    [Return]     ${output}

Change BAGG
    [Documentation]    Makes changes to the Bridge Aggregation Groups (BAGG) on 5900
    [Arguments]        ${TOR_IPV4}    ${TOR_USER}    ${TOR_PASS}   ${TOR_BAGG}    ${TOR_CMD}
    Log   \nRunning: ${TOR_CMD} on: ${TOR_BAGG}    console=True
    Open Connection And Log In      ${TOR_IPV4}    ${TOR_USER}    ${TOR_PASS}
    Write    sys
    Sleep    5s
    ${output}=    Read
    log   ${output}    console=True
    Write    int ${TOR_BAGG}
    Sleep    5s
    ${output}=    Read
    log   ${output}    console=True
    Write    ${TOR_CMD}
    Sleep    5s
    ${output}=    Read
    log   ${output}    console=True
    Close All Connections
    [Return]     ${output}

Get alert count
    [Documentation]   fetch ConnectionInstance alert count
    ${uri} =   set variable   /rest/alerts?filter="alertState='Active'"&filter="healthCategory='ConnectionInstance'"
    ${resp} =   fusion api get resource     ${uri}
    [Return]    ${resp['count']}

ConnectionInstance Alert Count is zero should be ${bool}
    [Documentation]   Check that ConnectionInstance SmartLink alerts are all cleared\not cleared
    ${count} =   Get alert count
    Run Keyword If    ${bool} is ${True}    should be equal as integers    ${count}    0
    ...   ELSE        should not be equal as integers    ${count}    0
    [Return]    ${count}

ConnectionInstance Alert Count should be greater than ${count}
    [Documentation]   Check that ConnectionInstance SmartLink alerts are greater than given count
    ${alerts} =   Get alert count
    Should be true    ${alerts} > ${count}

Get Errors
    [Documentation]     ...
    ${ERRORS}=   Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}

Run FTS and test-specific setup
    [Documentation]     ...
    Return from keyword if   ${skipsetup} is ${True}
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

    Load 5900 configuration    ${tor['ipv4']}    ${tor['user']}    ${tor['pass']}   ${tor['config1']['cfg_file']}
    Wait For Appliance To Become Pingable     ${tor['ipv4']}

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

    ${ligs} =           Get Variable Value        ${ligs}
    Run Keyword If    ${ligs} is not ${null}    Run Keyword for Dict    ${ligs}    Add LIG from variable

    ${enc_groups} =     Get Variable Value        ${enc_groups}
    Run Keyword for Dict    ${enc_groups}    Add Enclosure Group from variable

    ${les} =            Get Variable Value    ${les}
    Run Keyword If    ${les} is not ${null}                    Run Keyword for Dict    ${les}      Add Logical Enclosure from variable

    ${ranges} = Get Variable Value  ${ranges}
    ${pools} =  Run Keyword If  ${ranges} is not ${null}    Create List     /rest/id-pools/vmac /rest/id-pools/vwwn /rest/id-pools/vsn
    Run Keyword If  ${ranges} is not ${null}                Run Keyword for List    ${pools}    Disable ALL Generated ID Ranges
    Run Keyword If  ${ranges} is not ${null}                Add Ranges From variable    ${ranges}

    Run keyword for list    ${SERVERS}    Power off server

    ${server_profiles} =    Get Variable Value    ${server_profiles}
    Run Keyword If    ${server_profiles} is not ${null}        Add Server Profiles from variable    ${server_profiles}    25m    1m

    ${server_profiles} =    Get Variable Value  ${server_profiles_nohw}
    Run Keyword If  ${server_profiles} is not ${null}       Add Server Profiles from variable no hardware   ${server_profiles}   ${server_profile_to_bay_map}

    ${server_profiles_to_bay_map} =    Get Variable Value   ${server_profiles_to_bay_map}
    Log to console and logfile  Assigning Server Hardware to Profiles
    ${tasks} =                        Run Keyword If   ${server_profile_to_bay_map} is not ${null}    Assign Server Hardware To Existing Profiles From Variable    ${server_profile_to_bay_map}
    Validate Task List                ${tasks}

    Run keyword for list    ${SERVERS}    Power on server

Add Server Profiles from variable no hardware
    [Documentation]    Adds Server Profiles to an appliance from a variable which contains a list of dicts with the entire payload
    [Arguments]     ${profiles}   ${server_profile_to_bay_map}
    Log     Adding SERVER PROFILES
    :FOR    ${profile}  IN  @{profiles}
    \   ${profile} =    Copy Dictionary     ${profile}
    \   ${resp} =   Run Keyword If   '${server_profile_to_bay_map['${profile['name']}']}' == '${null}'   Fusion Api Get Server Hardware
    \   ${shUri} =   Run Keyword If   ${resp} == ${null}   Get Server Hardware URI    ${server_profile_to_bay_map['${profile['name']}']}
    \   ...                    ELSE   Set Variable   ${resp['members'][0]['uri']}
    \   ${serverHW} =    Fusion Api Get Resource    uri=${shUri}
    \   Set To Dictionary    ${profile}   serverHardwareTypeUri=${serverHW['serverHardwareTypeUri']}
    \   ${eg} =     Get from Dictionary ${profile}  enclosureGroupUri
    \   @{words} =  Split String    ${eg}   :
    \   ${type} =   Get From List   ${words}    0
    \   ${eg} =     Get From List   ${words}    1
    \   ${uri} =    Get Enclosure Group URI ${eg}
    \   Set to Dictionary   ${profile}  enclosureGroupUri   ${uri}
    \
    \   # TODO  Need some logic to see if it has connections vs. connectionSettings
    \
    \   ${connections} =    Get From Dictionary ${profile['connectionSettings']}    connections
    \   ${connections} =    Lookup Connection Uris  ${connections}
    \   Set to Dictionary   ${profile['connectionSettings']}  connections     ${connections}
    \   ${resp} =   Fusion Api Create Server Profile        body=${profile}
    \   ${task} =   Wait For Task   ${resp}     timeout=15min       interval=10
    \   ${task_state} =     Get From dictionary     ${task}     taskState
    \   Should Match Regexp ${task_state}   ((?i)Warning|Completed)

Assign Server Hardware To Existing Profiles From Variable
    [Documentation]    Update Server Profiles with server hardware assigned to profile from mapping variable
    [Arguments]    ${server_profile_to_bay_map}    ${concurrent_profiles}=24
    [Tags]    Performance    server_profiles-condition-everything

    ${existing_profiles} =    Fusion Api Get Server Profiles
    ${all_task_list} =    Create List
    ${these_assign_list} =    Create List
    :FOR    ${profile}    IN    @{existing_profiles['members']}
    \    Run Keyword If    '${profile['serverHardwareUri']}' != '${NULL}'    Log    ${profile['name']} is already assigned...skipping
    \    Continue For Loop If    '${profile['serverHardwareUri']}' != '${NULL}'
    \    Continue For Loop If   '${server_profile_to_bay_map['${profile['name']}']}' == '${null}'
    \    ${shUri} =     Get Server Hardware URI    ${server_profile_to_bay_map['${profile['name']}']}
    \    Set To Dictionary    ${profile}   serverHardwareUri=${shUri}
    \    Remove From Dictionary    ${profile}   status_code    headers
    \    Log    Assigning server hardware URI \"${shUri}\" to profile \"${profile['name']}\"   console=True
    \    ${resp} =   Fusion Api Edit Server Profile    uri=${profile['uri']}   body=${profile}   param=?force=ignoreServerHealth
    \    Append To List    ${all_task_list}    ${resp}
    \    Append To List    ${these_assign_list}    ${resp}
    \    ${assigning} =    Get Length    ${these_assign_list}
    \    Run Keyword If    ${assigning}==${concurrent_profiles}    Wait For Assigning    ${these_assign_list}
    \    ${these_assign_list} =    Run Keyword If    ${assigning}==${concurrent_profiles}    Create List    ELSE    Set Variable    ${these_assign_list}

    # were there any not waited on?
    ${assigning} =    Get Length    ${these_assign_list}
    Run Keyword If    ${assigning}>0    Wait For Assigning    ${these_assign_list}

    [Return]   ${all_task_list}

Wait For Assigning
    [Documentation]     Wait For Assigning
    [Arguments]    ${tasks}    ${timeout}=45m    ${interval}=30
    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}    # so WFT2 processes all tasks, not stop on failure.
    Wait for Task2    ${tasks}    ${timeout}    ${interval}

Teardown
    [Documentation]     ...
    Set Log Level    TRACE
    log to console and logfile    [TEARDOWN]
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Power off ALL Servers    PressAndHold
    Remove All Server Profiles
    Remove All SPT
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
