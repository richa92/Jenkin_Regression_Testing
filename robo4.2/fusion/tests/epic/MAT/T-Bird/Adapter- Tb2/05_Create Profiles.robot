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

Health Status
    [Tags]   HealthStatus
    [Documentation]  Interconnect and SAS Interconnect health status check before profile creation
    All Interconnects Status Should Be OK or Warning

Add Server Profile FC
    [Tags]    ADDRUN1SERVERPROFILE
    [Documentation]     Create Server Profiles
    Power off Servers in Profiles   ${server_profiles_run1}
    ${responses}=  Add Server Profiles from variable  ${server_profiles_run1}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=2000    interval=5
    Verify Resources for List  ${expected_server_profiles_run1}

Unassign Server Profile
   [Tags]   UNASSIGN
   [Documentation]   Unassign server profile
   Unassign Server Profile   ${server_profiles_run1}     ${expected_unassign_server_profiles_run1}

Add Server Profile FCoE iSCSI
    [Tags]    ADDRUN2SERVERPROFILE
    [Documentation]     Create Server Profiles
    Power off Servers in Profiles   ${server_profiles_run2}
    ${responses}=  Add Server Profiles from variable  ${server_profiles_run2}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=2000    interval=5
    Verify Resources for List  ${expected_server_profiles_run2}
