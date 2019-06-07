** Settings ***
Documentation
...     This Test Suite uses AD Server Group User credentials for Server Profile Tests.
...     TAGS:                   UPDATE-SP, EDIT-SPT, SP-SPT, SP, SP-UNASSIGN
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${ad_server_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Update Server Profile BIOS Settings
    [Tags]    UPDATE-SP  T-BIRD  C7000
    [Documentation]    Update server profiles post upgrade
    ${responses}=   Edit Server Profiles from variable   ${edit_server_profiles}
    Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=1800    interval=5
    Verify Resources for List  ${expected_edit_server_profiles}

Edit Server Profile Template Ethernet settings
    [Tags]    EDIT-SPT  T-BIRD  C7000
    [Documentation]    Update server profiles post upgrade
    ${resplist}=  Edit Server Profile Templates from variable    ${edit_server_profiles_template}
    Wait for Task2  ${resplist}     timeout=120    interval=10

Update Server Profiles From Template
    [Tags]    SP-SPT  T-BIRD  C7000
    [Documentation]    Add Server Profiles from Templates during Post upgrade
    Power off Servers in Profiles   ${update_server_profiles_from_spt}
    ${resp_list}=  Update Server Profiles from Template  ${update_server_profiles_from_spt}
    Run Keyword If  ${resp_list} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2  ${resp_list}
    ...  timeout=1200  interval=5

Create Server Profiles From Updated Template
    [Tags]    SP  T-BIRD  C7000
    [Documentation]    Add Server Profiles from Updated Templates
    Power off Servers in Profiles   ${server_profiles_from_spt_system_validation}
    ${resp_list}=  Add Server Profiles from variable  ${server_profiles_from_spt_system_validation}
    Run Keyword If  ${resp_list} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2  ${resp_list}
    ...  timeout=1200  interval=5

UnAssign an existing Server Profile from a Server
    [Tags]    SP-UNASSIGN  T-BIRD  C7000
    [Documentation]    UnAssign an existing Server Profile from a Server
    ${responses}=   Edit Server Profiles from variable    ${unassign_server_profile}
    Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=3000    interval=5