*** Settings ***
Documentation
...     This Test Suite uses AD Server Group User credentials for Server profile template Tests.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SPT
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${ad_server_credentials}
#Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
#...                             AND  Regression Test Teardown
Suite Teardown                  Regression Test Teardown

*** Test cases ***
Add Server Profile Templates
    [Tags]    SPT  T-BIRD  C7000
    [Documentation]    Add Server Profiles templates for servers
    ${responses}=  Add Non Existing Server Profile Templates  ${server_profile_templates_data}
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure     Wait For Task2   ${responses}   timeout=600    interval=5
    Verify Resources for List  ${expected_server_profile_templates}

Create Server Profiles From Template
    [Tags]    SP-SPT  T-BIRD  C7000
    [Documentation]    Add Server Profiles from Templates
    Power off Servers in Profiles   ${server_profiles_from_spt}
    ${resp_list}=  Add Server Profiles from variable  ${server_profiles_from_spt}
    Run Keyword If  ${resp_list} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2  ${resp_list}
    ...  timeout=1200  interval=5
    Verify Resources for List  ${expected_server_profiles_from_spt}
    Get Task Tree From Post Response  ${resp_list}