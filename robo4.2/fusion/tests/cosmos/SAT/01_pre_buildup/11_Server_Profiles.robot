*** Settings ***
Documentation
...     This Test Suite uses AD server Group User credentials for Server Profile with local disk, san storage with legacy and UEFI Tests.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                   SP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${ad_server_credentials}
#Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
#...                             AND  Regression Test Teardown
Suite Teardown                  Regression Test Teardown

*** Test Cases ***
Create Server Profile
   [Tags]    SP  T-BIRD  C7000
   [Documentation]    Create server profiles
   Power off Servers in Profiles   ${server_profiles}
   ${responses}=   Add Server Profiles from variable   ${server_profiles}
   Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=${server_profile_timeout}    interval=${server_profile_interval}
   Verify Resources for List  ${expected_server_profiles}

Power On Servers
   [Tags]    SP-ON  T-BIRD  C7000
   [Documentation]    Power On Servers In Server Profile
   Power on Servers in Profiles   ${server_profiles}