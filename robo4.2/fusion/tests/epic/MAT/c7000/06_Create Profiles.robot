*** Settings ***
Documentation
...     This Test Suite uses Server Administrator credentials to add Enclosure, Server Profiles with BIOS Settings and Verify Network connectivity.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SERVER
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${serveradmin_credentials}
Suite Teardown                  MAT Suite Teardown

*** Test Cases ***

Add Server Profile with BIOS Settings
    [Tags]    ADDSERVERPROFILE
    [Documentation]     Create Server Profiles
    Power off Servers in Profiles   ${server_profiles}
    ${responses}=  Add Server Profiles from variable  ${server_profiles}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=4000    interval=10
    Verify Resources for List  ${expected_server_profiles}
