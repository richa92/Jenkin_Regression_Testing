*** Settings ***
Documentation    Edit Server Profiles
Resource                ../resource.txt

Variables                       ../Common.py
Variables                       ../${DATA_FILE}

Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown

*** Test Cases ***
Edit Profiles ONE
    [Tags]  TEST    54
    [Documentation]  Edit Server Profiles

    Run Keyword If    ${PAUSE_BEFORE_TEST_CASE}    Pause Execution    About to execute ${TEST NAME}, ready to Continue?
    ${profiles} =    Create List

    :FOR    ${sp}    IN   @{SERVER_PROFILES_ONE}
    \    ${profile} =    Fusion Api Get Server Profiles    param=?filter="'name'=='${sp["name"]}'"
    \    Log    Got profile: ${sp["name"]}    console=${CONSOLE}
    \    Remove From Dictionary    ${profile["members"][0]}    macType    wwnType    serialNumberType
    \    Remove From Dictionary    ${profile["members"][0]["connectionSettings"]["connections"][0]}    mac    macType    wwpnType
    \    Remove From Dictionary    ${profile["members"][0]["connectionSettings"]["connections"][1]}    mac    macType    wwpnType
    \    Append To List    ${profiles}    ${profile["members"][0]}

    :FOR    ${sp}    IN   @{ASSIGN_SERVER_PROFILES_ONE}
    \    ${profile} =    Fusion Api Get Server Profiles    param=?filter="'name'=='${sp["newName"]}'"
    \    Log    Got profile: ${sp["name"]}    console=${CONSOLE}
    \    Remove From Dictionary    ${profile["members"][0]}    macType    wwnType    serialNumberType
    \    Remove From Dictionary    ${profile["members"][0]["connectionSettings"]["connections"][0]}    mac    macType    wwpnType
    \    Remove From Dictionary    ${profile["members"][0]["connectionSettings"]["connections"][1]}    mac    macType    wwpnType
    \    Append To List    ${profiles}    ${profile["members"][0]}

    ${connectionSettings} =    Create List
    :FOR    ${profile}    IN    @{profiles}
    \    Append To List    ${connectionSettings}    ${profile["connectionSettings"]}

    # Shift the connectionSettings and names "up" and then reapply the profiles
    Set To Dictionary    ${profiles[0]}    connectionSettings     ${connectionSettings[1]}
    Set To Dictionary    ${profiles[1]}    connectionSettings     ${connectionSettings[2]}
    # Can't go from LAG to NONLAG thus need to enable LAG on connectionSettings[3] as profiles[2] was LAG1
    Set To Dictionary    ${connectionSettings[3]["connections"][0]}    lagName    LAG1
    Set To Dictionary    ${connectionSettings[3]["connections"][1]}    lagName    LAG1
    Set To Dictionary    ${profiles[2]}    connectionSettings     ${connectionSettings[3]}
    Set To Dictionary    ${profiles[3]}    connectionSettings     ${connectionSettings[0]}

    Set To Dictionary    ${profiles[0]}    name     ${DL_SP_EDIT_NAMES[0]}
    Set To Dictionary    ${profiles[1]}    name     ${DL_SP_EDIT_NAMES[1]}
    Set To Dictionary    ${profiles[2]}    name     ${DL_SP_EDIT_NAMES[2]}
    Set To Dictionary    ${profiles[3]}    name     ${DL_SP_EDIT_NAMES[3]}

    ${respList} =    Create List
    :FOR    ${profile}    In    @{profiles}
    \    ${resp} =    Fusion Api Edit Server Profile   body=${profile}    uri=${profile['uri']}?force=ignoreServerHealth
    \    Append To List    ${respList}    ${resp}

    Wait For Task2    ${respList}    timeout=600    interval=10

Confirm Server Profiles One in OneView
    [Documentation]   Confirms some GET values from profile in OneView
    [Tags]    TEST    54    CONFIRM_EDIT_SP_ONE

    Run Keyword If    ${PAUSE_BEFORE_TEST_CASE}    Pause Execution    About to execute ${TEST NAME}, ready to Continue?
    ${profiles} =    Get Variable Value    ${CONFIRM_SERVER_PROFILES_ONE}
    Run Keyword If    ${profiles} is ${null}    Fatal Error    What is the point if no profiles to confirm, not a good Qual test

    ${connectionSettings} =    Create List
    :FOR    ${profile}    IN    @{profiles}
    \    Append To List    ${connectionSettings}    ${profile["connectionSettings"]}

    # Shift the connectionSettings and names "up" and to verify the profiles
    Set To Dictionary    ${profiles[0]}    connectionSettings     ${connectionSettings[1]}
    Set To Dictionary    ${profiles[1]}    connectionSettings     ${connectionSettings[2]}
    Set To Dictionary    ${profiles[2]}    connectionSettings     ${connectionSettings[3]}
    Set To Dictionary    ${profiles[3]}    connectionSettings     ${connectionSettings[0]}

    Set To Dictionary    ${profiles[0]}    name     ${DL_SP_EDIT_NAMES[0]}
    Set To Dictionary    ${profiles[1]}    name     ${DL_SP_EDIT_NAMES[1]}
    Set To Dictionary    ${profiles[2]}    name     ${DL_SP_EDIT_NAMES[2]}
    Set To Dictionary    ${profiles[3]}    name     ${DL_SP_EDIT_NAMES[3]}

    # need to remove "mac" from ["connectionsSettings"]["connections"][0] and [1] as the "mac" doesn't change
    :FOR    ${sp}    IN    @{profiles}
    \    Remove From Dictionary    ${sp["connectionSettings"]["connections"][0]}    mac
    \    Remove From Dictionary    ${sp["connectionSettings"]["connections"][1]}    mac

    Confirm Server Profiles    ${profiles}

Get Locked and Active Alerts For Profiles and Hardware
    [Documentation]    Get the locked and active alerts for profiles to help with triage
    [Tags]    TEST    54    GET_ALERTS
    Get Locked and Active Alerts For Profiles and Hardware