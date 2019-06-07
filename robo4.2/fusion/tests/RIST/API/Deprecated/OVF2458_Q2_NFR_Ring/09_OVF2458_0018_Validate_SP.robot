*** Settings ***
Documentation   Validate Server Profiles
...             Connections, Local Storage, SAN Storage.

Resource        ../../../../Resources/api/fusion_api_resource.txt

#Variables       ./build_volAttach.py

Library         ./pythonHelperFunctionsCGW.py
Variables 		./data_variables_ftc.py

Suite Setup       Run Keyword    Set Log Level    DEBUG
Suite Teardown    Fusion Api Logout Appliance

*** Variables ***
# used for development on Daisy
&{P1}                      name=CN754406WS_Bay_9_480_1
&{P2}                      name=MXQ7100868_Bay_7_480_1
&{P3}                      name=CN754404R9_Bay_3_480_1
@{members}                  ${P1}    ${P2}    ${P3}

*** Test Cases ***
OVF2458 Validate Server Profiles
    [Documentation]    Validate Server Profiles
    [Setup]                           Run Keyword and Ignore Error    Write To ciDebug Log

#   If executed via __init__.robot, will be logged in thus don't login again.
    ${active} =    Run Keyword and Return Status    Fusion Api Get Active User
    Run Keyword if    '${active}'=='False'    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Validate Server Profiles
#    [Teardown]                        Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

*** Keywords ***
Validate Server Profiles
	[Documentation]	Validate Server Profiles:  Connections, Local Storage, SAN Storage etc.

    Set Suite Variable    ${VALIDATE_ENTIRE_DTO}    ${TRUE}
    Set Test Variable    ${wordy}    True

    ${resp} =    Fusion Api Get Appliance Api Versions

    ${connections} =    Expected Connections    ${conns}
    ${spt480} =    Expected SP From SPT    ${spts['480_1']}    ${resp['currentVersion']}
    ${spt660} =    Expected SP From SPT    ${spts['660_1']}    ${resp['currentVersion']}
    Set Test Variable    ${spt480}    ${spt480}
    Set Test Variable    ${spt660}    ${spt660}

    # Validate Volumes
    Log    Validate Volumes
    ${expected_volumes} =    Create Expected Volumes    ${existing_volumes}    ${profile_sanStorage}
    Log    ${expected_volumes}
    ${volumes} =    Fusion Api Get Storage Volumes
    ${result} =   Fusion Api Validate Response Follow    ${expected_volumes}    ${volumes}    wordy=${wordy}
    Run Keyword And Continue On Failure    Should Be Equal As Strings    ${result}    True

    ${profiles} =     Fusion Api Get Server Profiles  param=?sort=name:ascending
    :FOR    ${member}     in    @{profiles['members']}
    \    Log    profile: ${member['name']}    console=yes
    \    ${exp_sanStorage} =    Massage Expected SanStorage    ${profile_sanStorage['${member['name']}']['sanStorage']}    ${STORAGE_TARGETS_REGEXP}
    \    Log    ${exp_sanStorage}
    \    # Validate SAN Storage
    \    Log    Validate SAN Storage
    \    ${res_sanStorage} =    Get Volume Name For Sorted By volumeURI    ${member['sanStorage']}
    \    Log    ${res_sanStorage}
    \    ${result} =   Fusion Api Validate Response Follow    ${exp_sanStorage}    ${res_sanStorage}    wordy=${wordy}
    \    Run Keyword And Continue On Failure    Should Be Equal As Strings    ${result}    True
    \    # Validate Local Storage
    \    Log    Validate Local Storage
    \    ${localStorage} =    Expected Local Storage    ${member['name']}    ${spts}
    \    ${result} =   Fusion Api Validate Response Follow    ${localStorage}    ${member['localStorage']}    wordy=${wordy}
    \    Run Keyword And Continue On Failure    Should Be Equal As Strings    ${result}    True
    \    # Validate Connections
    \    Log    Validate Connections
    \    ${result} =   Fusion Api Validate Response Follow    ${connections}    ${member}    wordy=${wordy}
    \    Run Keyword And Continue On Failure    Should Be Equal As Strings    ${result}    True
    \    # Validate SPT stuff
    \    Log    Validate SPT settings
    \    ${result} =    Validate SPT Settings    ${member}
    \    Run Keyword And Continue On Failure    Should Be Equal As Strings    ${result}    True


Validate SPT Settings
    [Documentation]    Can't do in :For loop so do here
    [Arguments]    ${member}
    ${is480} =    Run Keyword and Return Status    Should Match Regexp    ${member['name']}    480_1
    ${result} =    Run Keyword If    '${is480}'=='True'    Fusion Api Validate Response Follow    ${spt480}    ${member}    wordy=${wordy}
    ...    ELSE    Fusion Api Validate Response Follow    ${spt660}    ${member}    wordy=${wordy}
    [return]    ${result}

Get Errors
    [Documentation]    Get Errors
    ${ERRORS} =   Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}
