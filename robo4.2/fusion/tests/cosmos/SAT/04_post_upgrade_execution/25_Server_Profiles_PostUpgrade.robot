** Settings ***
Documentation
...     This Test Suite uses AD server Group User credentials for Server Profile with local disk, san storage with legacy and UEFI Tests.
...     Update BIOS settings for existing server profile
...     Un-assign and Re-assign server profiles
...     Edit and Update server profile connection
...     Copy server profile
...     Edit and validate server hardware name
...     Test Data is defined in Python Data Variable file.
...     TAGS:                   SP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${ad_server_credentials}
#Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
#...                             AND  Regression Test Teardown
Suite Teardown                  Regression Test Teardown

*** Test Cases ***

Update Server Profile BIOS Settings
    [Tags]    UPDATE-SP  T-BIRD  C7000
    [Documentation]    Update server profiles post upgrade
    Power off Servers in Profiles   ${edit_server_profiles}
    ${responses}=   Edit Server Profiles from variable   ${edit_server_profiles}
    Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=1800    interval=5
    Verify Resources for List  ${expected_edit_server_profiles}

Create Server Profile
    [Tags]    SP  T-BIRD  C7000
    [Documentation]    Create server profiles post upgrade
    Power off Servers in Profiles   ${server_profiles_postupgrade}
    ${responses}=   Add Server Profiles from variable   ${server_profiles_postupgrade}
    Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=${server_profile_timeout}    interval=${server_profile_interval}
    Verify Resources for List  ${expected_server_profiles_postupgrade}

UnAssign an existing Server Profile from a Server
    [Tags]    SP-UNASSIGN  T-BIRD  C7000
    [Documentation]    UnAssign an existing Server Profile from a Server
    ${responses}=   Edit Server Profiles from variable    ${unassign_server_profile}
    Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=3000    interval=5

Update connections details in Server Profile
    [Tags]    SP-UPDATE-CONN  T-BIRD  C7000
    [Documentation]    Update connections details in Server Profile
    # Update the connection changes to the  profile
    ${profile_info} =  Copy Dictionary  ${unassign_server_profile[0]}
    ${connections} =   Get Variable Value   ${profile_info['connectionSettings']['connections']}
    ${connectionsLength} =   Get Length   ${connections}
    # Change the Port ID info
    ${port_chng}=   Set Variable    Auto
    :FOR    ${conn}    IN    @{connections}
    \    ${netname}=     Get From Dictionary     ${conn}    name
    \    ${port}=     Get From Dictionary     ${conn}    portId
    \    Set To Dictionary     ${conn}     portId    ${port_chng}
    Set to Dictionary     ${profile_info['connectionSettings']}    connections     ${connections}

    # Server profile connections updated with port ID
    ${responses}=    Edit Server Profile    ${profile_info}
    Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=3000    interval=5

Delete a connection from Server Profile
    [Tags]    SP-DEL-CONN  T-BIRD  C7000
    [Documentation]    Delete a connection from Server Profile
    ${profile_info} =  Copy Dictionary  ${unassign_server_profile[0]}

    # Create data to delete a Connection
    ${add_conn} =  Create List
    ${connections} =   Get Variable Value   ${profile_info['connectionSettings']['connections']}
    Should Not Be Empty    ${connections}    msg=connection not available
   # Delete a connection - Connection 1 with port ID assigned to 3:1a
   ${name} =   Get Variable Value   ${connections[1]['name']}
    :FOR    ${conn}    IN    @{connections}
    \    ${netname}=     Get From Dictionary     ${conn}    name
    \    Run keyword If    '${netname}'!= '${name}'    Append To List   ${add_conn}    ${conn}

    Set to Dictionary     ${profile_info['connectionSettings']}    connections     ${add_conn}
    # Server profile updated with deleted connection
    ${responses}=    Edit Server Profile    ${profile_info}
    Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=3000    interval=5

Delete all connections from Server Profile
    [Tags]    SP-DELETE-ALL-CONN  T-BIRD  C7000
    [Documentation]    Delete all connections from Server Profile
    ${profile_info} =  Copy Dictionary  ${unassign_server_profile[0]}
    # Create data to delete all Connections
    ${conn} =  Create List
    Set to Dictionary     ${profile_info['connectionSettings']}    connections     ${conn}

    # Server profile updated with connections excluding deleted connection
    ${responses}=    Edit Server Profile    ${profile_info}
    Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=3000    interval=5

Add a connection to Server Profile
   [Tags]    SP-ADD-CONN   T-BIRD  C7000
   [Documentation]    Add a connection to Server Profile
   ${uri}=  Get Server Profile Uri  ${serverprofile_name}
   ${profile_info1} =  Fusion Api Get Server profiles  ${uri}
   ${profile_info} =  Copy Dictionary  ${unassign_server_profile[0]}

    # Create data to delete a Connection
    ${add_conn} =  Create List
    ${connections} =   Get Variable Value   ${profile_info['connectionSettings']['connections']}
    Should Not Be Empty    ${connections}    msg=connection not available
   # Add a connection - Connection with port ID assigned to 3:1a
    ${name} =   Get Variable Value   ${connections[0]['name']}
    :FOR    ${conn}    IN    @{connections}
    \    ${netname}=     Get From Dictionary     ${conn}    name
    \    Run keyword If    '${netname}'== '${name}'    Append To List   ${add_conn}    ${conn}
    Set to Dictionary     ${profile_info['connectionSettings']}    connections     ${add_conn}

    # Server profile updated with connections excluding deleted connection
    ${responses}=    Edit Server Profile    ${profile_info}
    Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=3000    interval=5

ReAssign an existing Server Profile to a Server
    [Tags]    SP-REASSIGN  T-BIRD  C7000
    [Documentation]    ReAssign an existing Server Profile to a Server
    ${responses}=   Edit Server Profile  ${re_assign_server_profile}
    Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=3000    interval=5
    Verify Resource  ${expected_server_profiles_postupgrade[2]}

Server Profile Transformation DTO and Create Profile
   [Tags]    COPY-SP    T-BIRD  C7000
   [Documentation]    Get Transformation server profile URI and create profile with verified tranformed data
   ${uri}=     Get Server Profile Transformation URI     @{server_profile_to_transform}
   ${transformation_dto}=    Get Server Profile Transformation     ${uri}
   Remove From Dictionary    ${transformation_dto}      name    created     modified     status    state    status_code    headers     osDeploymentSettings    serverHardwareUri    # These needs to be removed from payload
   Set to Dictionary    ${transformation_dto}    name    ${transformed_profile_data[0]['name']}
   ${name} =  replace string using regexp  ${transformed_profile[0]['serverHardwareUri']}  SH:  ${EMPTY}
   ${hardwareuri} =    Get Server Hardware URI    ${name}
   Set to Dictionary    ${transformation_dto}    serverHardwareUri    ${hardwareuri}
   #Verify Server Profile Transformation DTO     @{transformed_profile}     ${transformation_dto}
   ${responses}=   Add Server Profiles from variable       ${server_profile_to_copy}
   Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=1200    interval=5\
   Verify Resources for List  ${server_profile_to_copy}

Server Name Change From ILO And Verify The Change in OneView
    [Tags]    SH-NAME  T-BIRD  C7000
    [Documentation]   Server Name change from ilo and verify the change in OneView
    :FOR  ${sh}  IN  @{server_hardwares}
    \  ${resp} =   Get Resource    SH:${sh['name']}
    \  ${ip}=  Fetch ipv4 address  ${resp['mpHostInfo']['mpIpAddresses']}
    \  ${status}   ${resp}=    Run Keyword And Ignore Error    Open Connection    ${ip}  timeout=300s
    \  Run Keyword If  '${status}'=='FAIL'     Fail    Failed to Open SSH Connection for ${ip}
    \  ${newstatus}    ${resp}=    Run Keyword And Ignore Error    Login    ${ilo_credentials['username']}    ${ilo_credentials['password']}
    \  Run Keyword If  '${newstatus}'=='FAIL'      Fail    Failed to do SSH Login for ${ip}
    \  ${result}=  Execute Command      cd /system1
    \  Set server name and verify in Oneview  ${sh['name']}  ${sh['new_hostname']}  ${sh['old_hostname']}  ${sh['new_hostname']}
    \  Set server name and verify in Oneview  ${sh['name']}  ${sh['old_hostname']}  ${sh['new_hostname']}  ${sh['old_hostname']}

Power On Servers
    [Tags]    SP-ON  C7000
    [Documentation]    Power On Servers In Server Profile
    Power on Servers in Profiles   ${server_profiles_postupgrade}

Power On Pre Buildup Servers
    [Tags]    SP-ON  C7000  T-BIRD
    [Documentation]    Power On Servers In Server Profile
    Power on Servers in Profiles   ${server_profiles}
