*** Settings ***
Documentation
...     This Test Suite uses Server Administrator credentials to add Enclosure, Server Profiles with BIOS Settings and Verify Network connectivity.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SERVER
Resource                        ./resource_tbird.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
#Variables                       ./data_variables_tbird.py

*** Test Cases ***

Health Status
    [Tags]   HealthStatus
    [Documentation]  Interconnect and SAS Interconnect health status check before profile creation
    All Interconnects Status Should Be OK or Warning
    All SAS Interconnects Status Should Be OK or Warning

Add Server Profile with BIOS Settings
    [Tags]    ADDSERVERPROFILE
    [Documentation]        Create Server Profiles for BL servers with and without SAN Storage
    Power off Servers in Profiles   ${server_profiles}
    ${responses}=  Add Server Profiles from variable   ${server_profiles}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2  ${responses}   timeout=1800    interval=60
    Run Keyword If    ${expected_server_profiles} is not ${null}     Verify Resources for List  ${expected_server_profiles}

#Add Server Profile Templates
#    [Tags]    SPT
#    [Documentation]        Add Server Profiles templates for servers
#    ${responses}=  Add Non Existing Server Profile Templates  ${server_profile_templates}
#    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=600    interval=5
#    Verify Resources for List    ${server_profile_templates}

#Create Server Profiles From Template
#    [Tags]    SP-SPT
#    [Documentation]        Add Server Profiles from Templates
#    Power off Servers in Profiles   ${server_profiles_from_spt}
#    ${responses} =  Add Server Profiles from variable   ${server_profiles_from_spt}
#    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=1200    interval=60
#    Verify Resources for List  ${expected_server_profiles_from_spt}

Get LE Support Dump
    [Tags]    LE-SUPPORT-DUMP
    [Documentation]        Create and Download LE Support Dump
    Create And Download Logical Enclosure Support Dump  ${le_support_dump}  ${VERIFY}