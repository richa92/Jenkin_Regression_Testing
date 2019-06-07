*** Settings ***
Documentation    Add Profiles (Unassigned and assigned as data is defined)
Resource                ../resource.txt

Variables                       ../Common.py
Variables                       ../${DATA_FILE}

Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown

*** Test Cases ***
Add Server Profiles Neg
    [Documentation]    Attempts to add SP that should fail
    [Tags]    TEST    44    ADD_SP_NEG
    Run Keyword If    ${PAUSE_BEFORE_TEST_CASE}    Pause Execution    About to execute ${TEST NAME}, ready to Continue?
    ${server_profiles} =    Get Variable Value    ${SERVER_PROFILES_NEG_ONE}
    Run Keyword If    ${server_profiles} is ${null}    Run Keywords
    ...    Log    No defined Unassigned Server Profiles to add    level=WARN    console=${CONSOLE}
    ...    Pass Execution    No defined Unassigned Server Profiles to add

    Wait Until Keyword Succeeds    3 x    10 sec    Run Negative Tasks for List    ${server_profiles}

Add Unassigned Server Profiles
    [Documentation]  Add Profiles to Rack Server in OneView
    [Tags]    TEST    44    ADD_UN_SP_ONE
    Run Keyword If    ${PAUSE_BEFORE_TEST_CASE}    Pause Execution    About to execute ${TEST NAME}, ready to Continue?
    ${server_profiles} =    Get Variable Value    ${UNASSIGNED_SERVER_PROFILES_ONE}
    Run Keyword If    ${server_profiles} is ${null}    Run Keywords
    ...    Log    No defined Unassigned Server Profiles to add    level=WARN    console=${CONSOLE}
    ...    Pass Execution    {server_profiles} is ${null}    No defined Unassigned Server Profiles to add

    Add Server Profiles    ${server_profiles}

Add Assigned Server Profiles One
    [Documentation]  Add Profiles to Rack Server in OneView
    [Tags]    TEST    44    ADD_SP_ONE
    Run Keyword If    ${PAUSE_BEFORE_TEST_CASE}    Pause Execution    About to execute ${TEST NAME}, ready to Continue?
    ${server_profiles} =    Get Variable Value    ${SERVER_PROFILES_ONE}
    Run Keyword If    ${server_profiles} is ${null}    Fatal Error    What is the point if no profiles to add, not a good Qual test

    Power off Servers in Profiles    ${server_profiles}
    Add Server Profiles    ${server_profiles}

Assign Server Profiles One
    [Documentation]    Assigns server profiles to hardware
    [Tags]    TEST    44    ASSIGN_SP_ONE
    Run Keyword If    ${PAUSE_BEFORE_TEST_CASE}    Pause Execution    About to execute ${TEST NAME}, ready to Continue?
    ${server_profiles} =    Get Variable Value    ${ASSIGN_SERVER_PROFILES_ONE}
    Run Keyword If    ${server_profiles} is ${null}    Fatal Error    What is the point if no profiles to add, not a good Qual test

    ${respList} =    Create List
    :FOR    ${sp}    IN    @{server_profiles}
    \    Power off Server    ${sp["serverHardware"]}
    \    ${unassigned} =    Get Resource    SP:${sp["name"]}
    \    ${serverHardwareUri} =    Common URI lookup by name    ${sp["serverHardware"]}
    \    Set To Dictionary    ${unassigned}    serverHardwareUri    ${serverHardwareUri}
    \    Set To Dictionary    ${unassigned}    name    ${sp["newName"]}
    \    Remove From Dictionary  ${unassigned}  status_code  headers
    \    ${resp} =    Fusion Api Edit Server Profile   body=${unassigned}    uri=${unassigned['uri']}?force=ignoreServerHealth
    \    Append To List    ${respList}    ${resp}

    Wait For Task2    ${respList}    timeout=300    interval=20

Confirm Server Profiles One in OneView
    [Documentation]   Confirms some GET values from profile in OneView
    [Tags]    TEST    44    CONFIRM_SP_ONE
    Run Keyword If    ${PAUSE_BEFORE_TEST_CASE}    Pause Execution    About to execute ${TEST NAME}, ready to Continue?

    ${server_profiles} =    Get Variable Value    ${CONFIRM_SERVER_PROFILES_ONE}
    Run Keyword If    ${server_profiles} is ${null}    Fatal Error    What is the point if no profiles to confirm, not a good Qual test

    Confirm Server Profiles    ${server_profiles}

Get Locked and Active Alerts For Profiles and Hardware
    [Documentation]    Get the active alerts for profiles to help with triage
    [Tags]    TEST    44    GET_ACTIVE_ALERTS
    Get Locked and Active Alerts For Profiles and Hardware