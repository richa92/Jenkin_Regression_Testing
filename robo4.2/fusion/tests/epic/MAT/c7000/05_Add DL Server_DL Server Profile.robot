*** Settings ***
Documentation
...     This Test Suite uses Server Administrator credentials to add DL Server.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SERVER
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${serveradmin_credentials}
Suite Teardown                  MAT Suite Teardown

*** Test Cases ***

Add DL Sever
    [Tags]    ADDDLSERVER
    [Documentation]  Add Rack Server to OneView
    ${responses}=    Add Server hardware from variable   ${dl_servers}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=500    interval=5
    Verify Resources for List   ${expected_dl_servers}

Create DL Server Profile
    [Tags]  DLSERVERPROFILE
    Power off Servers in Profiles   ${dl_server_profiles}
    ${responses}=    Add Server Profiles from variable   ${dl_server_profiles}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=3000    interval=10
    Verify Resources for List  ${expected_dl_server_profiles}
