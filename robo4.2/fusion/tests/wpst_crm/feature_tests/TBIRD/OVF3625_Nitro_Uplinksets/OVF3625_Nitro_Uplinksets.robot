*** Settings ***
Documentation        OVF3625 Nitro Uplinksets
...   OVF3625 Nitro Uplinksets feature test
...   Usage:
...   robot -V data_variables.py -v APPLIANCE_IP:15.245.131.125 OVF3625_Nitro_Uplinksets.robot

Resource        ../../../../../Resources/api/fusion_api_resource.txt
Variables       data_variables.py

Suite Setup        Run FTS and test-specific setup
#Suite Teardown        Teardown

# Setup\Teardown for ALL test cases
Test Setup       Common Test Setup
Test Teardown    Common Test Teardown

Library             Dialogs

*** Variables ***
${VM}
${SSH_USER}                     root
${SSH_PASS}                     hpvse1
${FUSION_IP}                    ${APPLIANCE_IP}
${SKIPSETUP}                    ${False}
${SKIPTEARDOWN}                 ${False}

*** Test Cases ***
Should be able to create an LIG with one Ethernet uplinkset that uses all 6 Q ports
    [Documentation]   ...
    [Tags]   1    POS
    Add LIG from variable    ${pos_ligs['${LIG1}']}

Should be able to create an LIG with one Ethernet uplinkset that uses 16 uplink ports
    [Documentation]   ...
    [Tags]   2    POS
    Add LIG from variable    ${pos_ligs['${LIG2}']}

Should not be able to create an LIG with one Ethernet uplinkset that uses more than 16 uplink ports
    [Documentation]   ...
    [Tags]   3    NEG
    ${body} =      Build LIG body     ${neg_ligs['${NLIG1}']}
    ${task} =      Fusion Api Create LIG    ${body}
    ${resp} =      Wait for Task2      ${task}    2m
    ...                                           5
    ...                                           errorMessage=CRM_PORTS_EXCEED_MAX_PER_UPLINKSET
    ...                                           PASS=Error

Should be able to create an LIG with multiple Ethernet uplinksets that use mixed port types 
    [Documentation]   ...
    [Tags]   4    POS
    Add LIG from variable    ${pos_ligs['${LIG9}']}


Should not be able to create an LIG with one Ethernet uplinkset that uses mixed port types 
    [Documentation]   ...
    [Tags]   45    POS
    #Add LIG from variable    ${neg_ligs['${NLIG14}']}
    ${body} =      Build LIG body     ${neg_ligs['${NLIG14}']}
    ${task} =      Fusion Api Create LIG    ${body}
    ${resp} =      Wait for Task2      ${task}    2m
    ...                                           5
    ...                                           errorMessage=CRM_BOTH_SPLIT_AND_UNSPLIT_PORTS_USED_IN_UPLINK_SETS
    ...                                           PASS=Error

Should not be able to create an LIG with Ethernet uplinkset that uses port Q7
    [Documentation]   ...
    [Tags]   7    NEG
    ${body} =      Build LIG body     ${neg_ligs['${NLIG5}']}
    ${task} =      Fusion Api Create LIG    ${body}
    ${resp} =      Wait for Task2      ${task}    2m
    ...                                           5
    ...                                           errorMessage=CRM_INVALID_UPLINK_SET_PORT
    ...                                           PASS=Error

Should not be able to create an LIG with Ethernet uplinkset that uses port Q8
    [Documentation]   ...
    [Tags]   8    NEG
    ${body} =      Build LIG body     ${neg_ligs['${NLIG6}']}
    ${task} =      Fusion Api Create LIG    ${body}
    ${resp} =      Wait for Task2      ${task}    2m
    ...                                           5
    ...                                           errorMessage=CRM_INVALID_UPLINK_SET_PORT
    ...                                           PASS=Error

Should not be able to create an LIG with Ethernet uplinkset that uses port X1
    [Documentation]   ...
    [Tags]   9    NEG
    ${body} =      Build LIG body     ${neg_ligs['${NLIG7}']}
    ${task} =      Fusion Api Create LIG    ${body}
    ${resp} =      Wait for Task2      ${task}    2m
    ...                                           5
    ...                                           errorMessage=CRM_INVALID_UPLINK_PORT_FOR_I3S
    ...                                           PASS=Error

Should not be able to create an LIG with Ethernet uplinkset that uses port X2
    [Documentation]   ...
    [Tags]   10    NEG
    ${body} =      Build LIG body     ${neg_ligs['${NLIG8}']}
    ${task} =      Fusion Api Create LIG    ${body}
    ${resp} =      Wait for Task2      ${task}    2m
    ...                                           5
    ...                                           errorMessage=CRM_INVALID_UPLINK_PORT_FOR_I3S
    ...                                           PASS=Error

Should be able to create an I3S LIG with ImageStreamer uplinkset using X1 X2
    [Documentation]   ...
    [Tags]   11    POS
    Add LIG from variable    ${pos_ligs['${LIG4}']}

Should not be able to create an I3S LIG with ImageStreamer uplinkset using Q1 - Q8
    [Documentation]   ...
    [Tags]   12    NEG
    ${body} =      Build LIG body     ${neg_ligs['${NLIG9}']}
    ${task} =      Fusion Api Create LIG    ${body}
    ${resp} =      Wait for Task2      ${task}    2m
    ...                                           5
    ...                                           errorMessage=CRM_INVALID_INTERNAL_OS_DEPLOYMENT_PORT
    ...                                           PASS=Error

Should be able to create an LIG with 3966 internalVlans
    [Documentation]   ...
    [Tags]   13    POS
    Add LIG from variable    ${pos_ligs['${LIG3}']}

Should not be able to edit an LIG and add ports to an US that will exceed 16
    [Documentation]   ...
    [Tags]   15    NEG
    Add LIG from variable    ${pos_ligs['${LIG8}']}
    ${task} =      Edit LIG    ${LIG8}    ${neg_ligs['${NLIG11}']}
    ${resp} =      Wait for Task2      ${task}    2m
    ...                                           5
    ...                                           errorMessage=CRM_PORTS_EXCEED_MAX_PER_UPLINKSET
    ...                                           PASS=Error

Create EG, LE and verify Nitro modules go from Monitored to Configured state
    [Documentation]    ...
    [Tags]   18    POS
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

Should not be able to edit an LI US and exceed 16 ports in one US 
    [Documentation]    ...
    [Tags]   19    NEG
    ${us} =        Copy Dictionary   ${neg_li_us['24ports']}
    ${task} =      Edit uplinkset    16ports - Q1.1 - Q4.4   ${us}    ${LE1}-${LIG2}
    ${resp} =      Wait for Task2   ${task}    PASS=Error    errorMessage=CRM_PORTS_EXCEED_MAX_PER_UPLINKSET

Should be able to edit an LI US and remove ports and trigger out of compliance
    [Documentation]    ...
    [Tags]   20    POS
    ${LE1}-${LIG2} consistencyStatus should be CONSISTENT
    ${us} =        Copy Dictionary   ${pos_li_us['12ports']}
    ${task} =      Edit uplinkset    16ports - Q1.1 - Q4.4   ${us}    ${LE1}-${LIG2}
    ${resp} =      Wait for Task2   ${task}    20m    20
    wait until keyword succeeds     60s    5s    ${LE1}-${LIG2} consistencyStatus should be NOT_CONSISTENT

Should be able to edit an LIG US and remove ports and trigger compliance
    [Documentation]    ...
    [Tags]   21    POS
    ${LE1}-${LIG2} consistencyStatus should be NOT_CONSISTENT
    ${task} =      Edit LIG    ${LIG2}    ${pos_ligs['${LIG5}']}
    ${resp} =      Wait for Task2   ${task}    20m    20
    wait until keyword succeeds     60s    5s    ${LE1}-${LIG5} consistencyStatus should be CONSISTENT

Should be able to edit an LI US and remove networks and trigger out of compliance
    [Documentation]    ...
    [Tags]   22    POS
    ${LE1}-${LIG5} consistencyStatus should be CONSISTENT
    ${task} =      Edit uplinkset    12ports - Q1.1 - Q3.4   ${pos_li_us['12ports2']}    ${LE1}-${LIG5}
    ${resp} =      Wait for Task2   ${task}    20m    20
    #TODO   check that networks go to internal
    wait until keyword succeeds     60s    5s    ${LE1}-${LIG5} consistencyStatus should be NOT_CONSISTENT

Should be able to edit an LIG US and remove networks and trigger compliance
    [Documentation]    ...
    [Tags]   23    POS
    ${LE1}-${LIG5} consistencyStatus should be NOT_CONSISTENT
    ${task} =      Edit LIG    ${LIG5}    ${pos_ligs['${LIG6}']}
    ${resp} =      Wait for Task2   ${task}    20m    20
    wait until keyword succeeds     60s    5s    ${LE1}-${LIG6} consistencyStatus should be CONSISTENT

Should be able to create an LI US and add ports and networks
    [Documentation]    ...
    [Tags]   24    POS
    ${LE1}-${LIG6} consistencyStatus should be CONSISTENT
    ${task} =      Create uplinkset    ${pos_li_us['Q4subs']}    ${LE1}-${LIG6}
    ${resp} =      Wait for Task2      ${task}    20m    20
    wait until keyword succeeds     60s    5s    LI ${LE1}-${LIG6} consistencyStatus should be NOT_CONSISTENT

Should be able to edit an LIG US and add ports and networks
    [Documentation]    ...
    [Tags]   25    POS
    ${LE1}-${LIG6} consistencyStatus should be NOT_CONSISTENT
    ${task} =      Edit LIG    ${LIG6}    ${pos_ligs['${LIG7}']}
    ${resp} =      Wait for Task2   ${task}    20m    20

    wait until keyword succeeds     5m    5s    LI ${LE1}-${LIG7} consistencyStatus should be CONSISTENT
    LI ${LE1}-${LIG7} internalNetworkUris should be ${NULL}

Should not be able to create a single US that uses more than 16 ports
    [Documentation]    ...
    [Tags]   26    NEG
    Remove all uplinksets    20m    20
    ${task} =      Create uplinkset    ${neg_li_us['24ports']}    ${LE1}-${LIG7}
    ${resp} =      Wait for Task2      ${task}    20m    20   errorMessage=CRM_PORTS_EXCEED_MAX_PER_UPLINKSET

Should not be able to create a single US that uses mixed ports
    [Documentation]    ...
    [Tags]   27    NEG
    Remove all uplinksets    20m    20
    ${task} =      Create uplinkset    ${neg_li_us['mixed-ports']}    ${LE1}-${LIG7}
    ${resp} =      Wait for Task2   ${task}    20m    20   errorMessage=CRM_BOTH_SPLIT_AND_UNSPLIT_PORTS_USED_IN_UPLINK_SETS


Should not be able to edit an LI US to use mixed port types
    [Documentation]    ...
    [Tags]   28    POS
    Remove all uplinksets    20m    20
    ${task} =      Create uplinkset    ${pos_li_us['12ports']}    ${LE1}-${LIG7}
    ${resp} =      Wait for Task2      ${task}    20m    20
    ${task} =      edit uplinkset    12ports - Q1.1 - Q3.4     ${neg_li_us['mixed-ports']}    ${LE1}-${LIG7}
    ${resp} =      Wait for Task2   ${task}    20m    20   errorMessage=CRM_BOTH_SPLIT_AND_UNSPLIT_PORTS_USED_IN_UPLINK_SETS


#Should not be able to create a single US that uses more than 3966 vlans
#    [Documentation]    ...
#    [Tags]   28    NEG
#    Remove all uplinksets    20m    20
#    ${task} =      Create uplinkset    ${neg_li_us['Q5_3967nets']}    ${LE1}-${LIG7}
#    Log   This is passing and shouldn't be! The task should fail when I go to exceed 3966   console=True
#    ${resp} =      Wait for Task2      ${task}    2m
#    ...                                           20
#    ...                                           errorMessage=CRM_PORTS_EXCEED_MAX_PER_UPLINKSET
#    ...                                           PASS=((?i)Error)
#    ...                                           BREAK_LOOP_IF=((?i)Error|Terminated|Completed|Warning)

#Should not be able to create multiple US that use a total of more than 3966 vlans
#    [Documentation]    ...
#    [Tags]   29    NEG
#    Remove all uplinksets    20m    20
#    ${task} =      Create uplinkset    ${pos_li_us['12ports']}    ${LE1}-${LIG7}
#    ${resp} =      Wait for Task2      ${task}    20m    20
#    ${task} =      Create uplinkset    ${pos_li_us['Q6']}    ${LE1}-${LIG7}
#    ${resp} =      Wait for Task2      ${task}    20m    20   errorMessage=CRM_PORTS_EXCEED_MAX_PER_UPLINKSET    PASS=Error

*** Keywords ***
Edit LIG
    [Documentation]    ...
    [Arguments]     ${name}    ${lig}
    ${lig_uri} =    Get LIG Uri     ${name}
    ${body} =   Build LIG body      ${lig}
    ${resp} =   Fusion Api Edit LIG     body=${body}    uri=${lig_uri}
    [return]    ${resp}

Create uplinkset
    [Documentation]   Create an uplinkset
    [Arguments]    ${us}   ${li}
    ${us} =        Copy Dictionary    ${us}
    ${li_uri} =    Get LI URI    ${li}
    ${body} =      Build US body    ${us}    ${li_uri}
    ${resp} =      Fusion Api Create Uplink Set   body=${body}
    [Return]       ${resp}

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

    #update vlan-pool   ${4001}    ${60}

    ${ethernet_networks} =    Get Variable Value    ${ethernet_networks}
    Run Keyword If    ${ethernet_networks} is not ${null}     Add Ethernet Networks from variable   ${ethernet_networks}

    #update vlan-pool

    ${network_sets} =    Get Variable Value        ${network_sets}
    Run Keyword If    ${network_sets} is not ${null}          Add Network Sets from variable          ${network_sets}


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
