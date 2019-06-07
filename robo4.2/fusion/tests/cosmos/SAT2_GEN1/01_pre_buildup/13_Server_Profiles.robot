*** Settings ***
Documentation
...     This Test Suite uses AD server Group User credentials to create Server Profile from Server Profile Template.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                   SP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${ad_server_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Create Server Profiles From Template
    [Tags]    SP-SPT  T-BIRD  C7000
    [Documentation]    Add Server Profiles from Templates
    Power off Servers in Profiles   ${server_profiles_from_spt}
    ${resp_list}=  Add Server Profiles from variable  ${server_profiles_from_spt}
    Run Keyword If  ${resp_list} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2  ${resp_list}
    ...  timeout=1200  interval=5

Power On Servers
   [Tags]    SP-ON  T-BIRD  C7000
   [Documentation]    Power On Servers In Server Profile
   Power on Servers in Profiles   ${server_profiles_from_spt}