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

*** Test Cases ***

Update Server Profile Templates
    [Tags]    SP-SPT  T-BIRD  C7000
    [Documentation]    Update Server Profile Templates
    ${resplist}=  Edit Server Profile Templates from variable    ${spts_edit}
    Wait for Task2  ${resplist}     timeout=120    interval=10
    Verify Resources for List  ${expected_spts_edit}

Create Server Profiles From Template
    [Tags]    SP-SPT  T-BIRD  C7000
    [Documentation]    Add Server Profiles from Templates during Post upgrade
    Power off Servers in Profiles   ${server_profiles_from_spt_postupgrade}
    ${resp_list}=  Add Server Profiles from variable  ${server_profiles_from_spt_postupgrade}
    Run Keyword If  ${resp_list} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2  ${resp_list}
    ...  timeout=1200  interval=5
    Verify Resources for List  ${expected_server_profiles_from_spt_postupgrade}

Update Server Profiles From Template
    [Tags]    SP-SPT  C7000
    [Documentation]    Update Server Profiles from Templates during Post upgrade
    Power off Servers in Profiles   ${server_profiles_from_spt}
    ${resp_list}=  Update Server Profiles from Template  ${server_profiles_from_spt}
    Run Keyword If  ${resp_list} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2  ${resp_list}
    ...  timeout=1200  interval=5