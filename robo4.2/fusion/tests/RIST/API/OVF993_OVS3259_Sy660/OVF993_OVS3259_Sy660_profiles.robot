*** Settings ***
Documentation                   Sy660 Gen10 Condor Server profiles with backplane connections to Mezz1 from SPT,
...                             connections, Local storage, edit Bios, edit Boot, move
...                            -  Add Base Resources networks
...                            -  Add Potash LIG, SAS LIG, create EG, and LE
...                            -  Gen10 Condor with backplane connections to Mezz1, create with external and internal LS
...                            -  Remove Base Resources

Library				FusionLibrary
Library             RoboGalaxyLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library             XML
Library             String
Library  			Dialogs

Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${DATA_FILE}

Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}		16.114.209.223
${DATA_FILE}        ./Regression_Data.py

*** Test Cases ***
OVS3259 TestCase Create Gen10 SY660 SPT with external, internal, LD, LJBOD, Mezz1, Mezz4 Local storage
    [Documentation]  Create Gen10 SY660 SPT with external, internal, LD, LJBOD, Mezz1, Mezz4 Local storage
    [Tags]    OVF993-SPT
    Create Gen10 SY660 Server Profile Template

OVS3259 TestCase Create Gen10 Sy660 profile from template
     [Documentation]  Create Gen10 Sy660 profile from template
    [Tags]    OVF993-SP    Performance    server_profiles-condition-jbods
    Create Gen10 Server Profile 660 from Template

OVS3259 Verify Internal External Storage with RIS
    [Documentation]  Verify Internal External Storage with RIS
    [Tags]    OVF993-RIS
    Verify Internal External Storage with RIS

OVS3259 TestCase Edit Gen10-Sy660 SP Change LS Boot BIOS
   [Documentation]  Edit Gen10-Sy660 SP Change LS Boot BIOS
   [Tags]    OVF993-EDIT-SP    Performance    server_profiles-condition-jbods
   Edit Gen10-Sy660 Server Profile

*** Keywords ***
Setup
    [Documentation]  Setup
    Set Log Level  DEBUG
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Power off Servers in Profiles    ${server_profile}
    ${resp} =    Remove Server Profiles from variable    ${server_profile}
    Wait For Task2    ${resp}	   timeout=2400	interval=15

Create Gen10 SY660 Server Profile Template
    [Documentation]  Create Gen10 profile template
    @{responses} =    Create List
    :FOR	${profile_template}	IN	@{sy660_gen10_backplane_templates}
	\      ${resp} = 	Add Server Profile Template	${profile_template}
	\      log to console		${resp}
	\      Append To List    ${responses}    ${resp}
	Wait For Task2	${responses}	   timeout=60	interval=5

Create Gen10 Server Profile 660 from Template
    [Documentation]  create gen10 profile from template
    @{responses} =    Create List
    :FOR	${profile}	IN	@{server_profile}
	\		${resp} = 	Add Server Profile	${profile}
	\      log to console		${resp}
	\      Append To List    ${responses}    ${resp}
	Wait For Task2	${responses}	   timeout=600	interval=15

Verify Internal External Storage with RIS
    [Documentation]  Verify Internal (With I) and external Storage drives details with RIS
    Power on Servers in Profiles  ${server_profile}
    Run Keyword and Ignore Error    Wait for Servers in Profiles to reach POST State  ${server_profile}
    Verify RIS Nodes for List  ${ris_nodes_create}

Edit Gen10-Sy660 Server Profile
    [Documentation]  Edit profile, add more LS options
    Power off Servers in Profiles    ${server_profile}
	${resp} = 	Edit Server Profile	${edit_profile_add_moreLS}
	log to console		${resp}
	Wait For Task2	${resp}	   timeout=2400	interval=15

Clean Up
    [Documentation]  cleanup
    ${resp} =    Remove Server Profiles from variable    ${server_profile}
    Wait For Task2    ${resp}	   timeout=2400	interval=15
    Remove All Server Profile Templates
    Fusion Api Logout Appliance