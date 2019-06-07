*** Settings ***
Documentation    Add Rack Servers (DL) to OneView
Resource                ../resource.txt

Variables                       ../Common.py
Variables                       ../${DATA_FILE}

Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown

*** Variables ***
${ADD_DL_RANDOM_MODE}       True  #  When True uses randome mode to add, otherwise specify specific index from @{add_mode} 0, 1, 2

*** Test Cases ***
Insure Rack Servers Not Claimed
    [Documentation]    Execute cpqlocfg to Delete Remote Manager Configuration
    [Tags]    40    DELETE_RMC

    # Currently not checking ${output} of cpqlocfg for script status.  If it failed, probably due to
    # ilO wasn't being remotely managed to begin with
    :FOR    ${ilo_ip}    IN    @{DL_SERVER_IPs}
    \    ${output} =    Run cpqlocfg and Delete Remote Manager Configuration    ${ilo_ip}    # True

Select Add Mode and Add Rack Servers
    [Documentation]    Selects an Add mode based on random int.
    [Tags]    40    ADD_DL
    Run Keyword If    '${ADD_DL_RANDOM_MODE}'=='False'    Log    Random Add Mode disabled. Intentional?    level=WARN
    ${random_index} =    Evaluate    random.randint(0, 2)    modules=random
    ${index} = 	  Run Keyword If    '${ADD_DL_RANDOM_MODE}'=='True'    Set Variable    ${random_index}
    ...    ELSE    Set Variable    ${ADD_DL_RANDOM_MODE}
    @{add_mode} =    Create List
    ...    Add Rack Server Async
    ...    Add Rack Server By Ranges
    ...    Add Rack Server By List

    Log    index selected is ${index}    console=${CONSOLE}
    Log    Will add server hardware using ${add_mode[${index}]}    console=${CONSOLE}
    Run Keyword    ${add_mode[${index}]}

Power Off and Check Status
    [Tags]   40    POWER_OFF_CHECK_STATUS
    Power off ALL servers
    ${expected_rack_servers} =    Get Variable Value    ${EXPECTED_RACK_SERVERS}
    Run Keyword If    ${expected_rack_servers} is ${null}    Pass Execution    No expected_rack_servers data thus not able to Verify Resources for List
    ${servers_ok} =    Run Keyword And Return Status    Verify Resources for List    ${expected_rack_servers}    status=${DL_ADD_STATUS}
    Run Keyword If    ${servers_ok}==${False}    Run Keywords
    ...    Refresh Critical Server Hardware
    ...    AND    Verify Resources for List    ${expected_rack_servers}    status=${DL_ADD_STATUS}

*** Keywords ***
Add Rack Server Async
    [Documentation]  Add Rack Server to OneView each as seperate Task
    ${rackservers} =    Get Variable Value    ${RACKSERVERS}
    Run Keyword If    ${rackservers} is ${null}    Run Keywords
    ...    Log   No rack servers to add    level=WARN    console=${CONSOLE}
    ...    AND    Return From Keyword

    Add Server hardware from variable async    ${rackservers}

Add Rack Server By Ranges
    [Documentation]  Add Rack Server to OneView using Range
    ${rack_server_ranges} =    Get Variable Value    ${RACK_SERVER_RANGES}
    Run Keyword If    ${rack_server_ranges} is ${null}    Run Keywords
    ...    Log No rack server range to add    level=WARN    console=tru
    ...    AND    Return From Keyword

    ${resp} =    Add Multiple Server Hardware    ${rack_server_ranges}
    Wait For Task2    ${resp}    timeout=300    interval=10

Add Rack Server By List
    [Documentation]  Add Rack Server to OneView using List
    ${rack_server_list} =    Get Variable Value    ${RACK_SERVER_LIST}
    Run Keyword If    ${rack_server_list} is ${null}    Run Keywords
    ...    Log    No rack server list to add    Level=WARN    console=${CONSOLE}
    ...    AND    Return From Keyword

    ${resp} =    Add Multiple Server Hardware    ${rack_server_list}
    Wait For Task2    ${resp}    timeout=300    interval=10

Refresh Critical Server Hardware
    [Documentation]    Refresh Server Hardware that are status Critical
    Log     Will Refresh Critical Servers    console=${CONSOLE}
    @{tasks} =    Create List
    ${servers} =     Fusion Api Get Server Hardware
    :FOR    ${server}    IN    @{servers['members']}
    \    Continue For Loop If    '${server['status']}'!='Critical'
    \    Log    Refreshing ${server['name']}    console=${CONSOLE}
    \    ${task} =    Refresh Server Hardware    ${server['name']}
    \    Append To List    ${tasks}    ${task}

    Wait For Task2    ${tasks}    timeout=120    interval=10