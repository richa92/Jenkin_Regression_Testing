*** Settings ***
Documentation    Common keywords for BIOS settings CDP
...              Author : Yogeshwar.V

Resource         ./../../../../Resources/api/fusion_api_resource.txt

*** Keywords ***

Add dicts to list
    [Documentation]     Adds two dictionaries and place it into a list and returns the list
    [Arguments]     ${dict1}     ${dict2}
    &{dict} =     Create Dictionary
    Set To Dictionary       ${dict}       &{dict1}
    Set To Dictionary       ${dict}       &{dict2}
    @{lst} =    Create List
    Append To List  ${lst}   ${dict}
    [Return]     ${lst}

Create Server Profile Template
    [Documentation]  Create  Server Profile Template
    [Arguments]     ${spts}
    @{responses} =    Create List
    :FOR    ${profile_template}    IN    @{spts}
    \      ${resp} =     Add Server Profile Template    ${profile_template}
    \      Run Keyword If       '${resp['status_code']}'=='202'     Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}       timeout=80    interval=5

Delete Profile Template
    [Documentation]  Create  Server Profile Template
    [Arguments]     ${spts}
    @{responses} =    Create List
    :FOR    ${profile_template}    IN    @{spts}
    \      ${resp} =     Remove Server Profile Template     ${profile_template}
    \      Run Keyword If       '${resp['status_code']}'=='202'     Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}       timeout=80    interval=5

Create Server Profiles
    [Documentation]  Create  Server Profiles
    [Arguments]     ${profiles}
    Power off Servers in Profiles  ${profiles}
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{profiles}
    \      ${resp} =     Add Server Profile    ${server_profile}    param=?force=ignoreServerHealth
    \      Run Keyword If       '${resp['status_code']}'=='202'     Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}    timeout=2600    interval=15

Create Server Profiles Unassigned
    [Documentation]  Create  Server Profiles
    [Arguments]     ${profiles}
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{profiles}
    \      ${resp} =     Add Server Profile    ${server_profile}    param=?force=ignoreServerHealth
    \      Run Keyword If       '${resp['status_code']}'=='202'     Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}    timeout=2600    interval=15

Edit Server Profiles
    [Documentation]  Edit  Server Profiles
    [Arguments]     ${profiles}
    Power off Servers in Profiles  ${profiles}
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{profiles}
    \      ${resp} =     Edit Server Profile    ${server_profile}    param=?force=ignoreServerHealth
    \      Run Keyword If       '${resp['status_code']}'=='202'     Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}    timeout=2400    interval=15

Edit Server Profiles Unassign
    [Documentation]  Edit  Server Profiles
    [Arguments]     ${profiles}
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{profiles}
    \      ${resp} =     Edit Server Profile    ${server_profile}    param=?force=ignoreServerHealth
    \      Run Keyword If       '${resp['status_code']}'=='202'     Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}    timeout=2400    interval=15

Delete Server Profiles
    [Documentation]  Delete  Server Profiles
    [Arguments]     ${profiles}
    Power off Servers in Profiles  ${profiles}
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{profiles}
    \      ${resp} =     Remove Server Profile    ${server_profile}    force=False
    \      Run Keyword If       '${resp['status_code']}'=='202'     Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}    timeout=2400    interval=15

Power on Server and check if its ON
    [Documentation]     Power On the given server and check if it is powered On
    [Arguments]         ${server}
    Power On Server     ${server}
    ${power_state}=    Get Server Power    ${server}
    Run keyword if    '${power_state}'!='On'    FAIL    Server power on failed
