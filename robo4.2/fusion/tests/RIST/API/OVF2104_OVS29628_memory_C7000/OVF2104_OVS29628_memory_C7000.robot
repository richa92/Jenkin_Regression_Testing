*** Settings ***
Documentation                   C7k Server memory inventory tests
...                               -  Gen10, Gen9
...                               -  Remove Base Resources

Library				FusionLibrary
Library             RoboGalaxyLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library             XML
Library             String
Library  			Dialogs

Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${DATA_FILE}

Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
#${APPLIANCE_IP}		16.114.209.223
#${DATA_FILE}        ./Regression_Data.py

*** Test Cases ***
TestCase Verify Gen10 server memory
   [Tags]    OVF2104-C7k-MC
   Should Match Gen10 Servers Memory   ${ris_nodes}

TestCase Verify Gen10 server memory after power on
   [Tags]    OVF2104-C7k-5-1-5-2-5-3-5-6-5-7
   Power off Servers in Profiles    ${gen10_server_profiles}
   Create Gen10 Server Profiles
   Power on Servers in Profiles    ${gen10_server_profiles}
   Refresh Servers in Profiles    ${gen10_server_profiles}
   Should Match Gen10 Servers Memory   ${ris_nodes}
   Reset Server  ${ENC1SHBAY16}  powerControl=Reset
   Reset Server Hardware iLO via cpqlocfg and Wait for Refresh to Finish  ${ENC1SHBAY16}
   Should Match Gen10 Server Memory   ${ris_node2}
   Reset Server  ${ENC2SHBAY16}  powerControl=Reset
   Reset Server Hardware iLO via cpqlocfg and Wait for Refresh to Finish  ${ENC2SHBAY16}
   Should Match Gen10 Server Memory   ${ris_node3}
   Power off Servers in Profiles    ${gen10_server_profiles}
   Should Match Gen10 Servers Memory   ${ris_nodes}

TestCase Verify Gen9 server memory
   [Tags]    OVF2104-C7k-5-4
   Power on Server  ${ENC1SHBAY5}
   Verify c7k Gen9 server memory
   Power on Server  ${ENC1SHBAY5}
   ${resp} =  Refresh Server Hardware  ${ENC1SHBAY5}
   Wait for task2  ${resp}
   Verify c7k Gen9 server memory

*** Keywords ***
Setup
    [Documentation]  Setup
    Set Log Level  TRACE
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Power off Servers in Profiles    ${gen10_server_profiles}
    ${resp} =    Remove Server Profiles from variable    ${gen10_server_profiles}
    Wait For Task2    ${resp}	   timeout=2400	interval=15

Clean Up
    [Documentation]  Clean Up
    Power off Servers in Profiles    ${gen10_server_profiles}
    ${resp} =    Remove Server Profiles from variable    ${gen10_server_profiles}
    Wait For Task2    ${resp}	   timeout=2400	interval=15
    Remove All Server Profile Templates
    Fusion Api Logout Appliance

Verify c7k Gen10 servers memory
    [Documentation]  Verify c7k Gen10 servers memory
    :FOR    ${ris}    IN    @{ris_nodes}
    \      Verify Gen10 server memory   ${ris}

Verify c7k Gen9 server memory
    [Documentation]  Verify c7k Gen9 server memory
    Run Keyword If    ${verify_gen9_servers} is not ${None}        Verify Resources For list    ${verify_gen9_servers}

Create Gen10 Server Profiles
    [Documentation]  Create Gen10 Server Profiles
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{gen10_server_profiles}
    \      ${resp} =     Add Server Profile    ${server_profile}
    \      log to console        ${resp}
    \      Append To List    ${responses}    ${resp}

    Wait For Task2    ${responses}    timeout=2400    interval=15