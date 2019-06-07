*** Settings ***
Documentation
...     This Test Suite uses Server Administrator credentials to add Enclosure, Server Profiles with BIOS Settings and Verify Network connectivity.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SERVER
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
Variables                       ./data_variables.py

*** Test Cases ***

Add Server Profile with BIOS Settings
    [Tags]    ADDSERVERPROFILE
    [Documentation]     Create Server Profiles
    Power off Servers in Profiles   ${server_profiles}
    ${responses}=  Add Server Profiles from variable  ${server_profiles}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=2000    interval=5
    Verify Resources for List  ${expected_server_profiles}

Add Server Profile Templates
    [Tags]    SPT
    [Documentation]        Add Server Profiles templates for servers
    ${responses}=  Add Non Existing Server Profile Templates  ${server_profile_templates}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=600    interval=5
    Verify Resources for List      ${server_profile_templates}

Create Server Profiles From Template
    [Tags]    SP-SPT
    [Documentation]        Add Server Profiles from Templates
    Power off Servers in Profiles   ${server_profiles_from_spt}
    ${responses} =  Add Server Profiles from variable   ${server_profiles_from_spt}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=600    interval=10
    Verify Resources for List  ${expected_server_profiles_from_spt}
