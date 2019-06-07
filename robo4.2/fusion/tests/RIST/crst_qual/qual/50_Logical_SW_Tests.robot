*** Settings ***
Documentation    Edit Resources, Update from Group
Resource                ../resource.txt

Variables                       ../Common.py
Variables                       ../${DATA_FILE}

Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown

*** Variables ***
${LSG_NEW_NAME}                 Name_Changed

*** Test Cases ***
Rename Logical Switch Group
    [Tags]  TEST    50    RENAME_LSG
    [Documentation]  Rename LSG to force inconsistency.
    ${lsg} =    Get Variable Value    ${LSG}
    ${orig_name} =    Get From Dictionary    ${lsg}    name
    Log    Renaming LSG from: ${orig_name} to: Name_Changed    console=${CONSOLE}

    ${lsg} =    Get Resource    LSG:${orig_name}
    Remove From Dictionary    ${lsg}    headers    status_code
    Set To Dictionary    ${lsg}    name    ${LSG_NEW_NAME}
    ${resp} =    Fusion Api Edit Lsg    ${lsg}    ${lsg["uri"]}
    Wait For Task2    ${resp}

Reset Logical Switch Group Name
    [Tags]  TEST    50    RESET_LSG_NAME
    [Documentation]  Reset LSG to original name to force inconsistency.
    ${lsg} =    Get Variable Value    ${LSG}
    ${orig_name} =    Get From Dictionary    ${lsg}    name
    Log    Renaming LSG from: Name_Changed to: ${orig_name}    console=${CONSOLE}

    ${lsg} =    Get Resource    LSG:${LSG_NEW_NAME}
    Remove From Dictionary    ${lsg}    headers    status_code
    Set To Dictionary    ${lsg}    name    ${orig_name}
    ${resp} =    Fusion Api Edit Lsg    ${lsg}    ${lsg["uri"]}
    Wait For Task2    ${resp}

Refresh Logical Switch after Reset
    [Documentation]    Refresh Logical Switch
    [Tags]    TEST    50    REFRESH_LS
    ${resp} =    Refresh Logical Switch    ${LS["logicalSwitch"]["name"]}
    Wait For Task2    ${resp}