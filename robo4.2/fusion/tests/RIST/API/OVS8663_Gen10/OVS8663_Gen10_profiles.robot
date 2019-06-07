*** Settings ***
Documentation                   Gen10 Server profiles connections, Local storage, edit Bios, edit Boot
...                               -  Add Base Resources networks
...                               -  Add Potash LIG, create EG, and LE
...                               -  Create Gen10 both Harrier and Condor Server profiles with connections, Local storage, edit Bios, edit Boot, move
...                               -  Remove Base Resources

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

#Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
#Resource            ../global_variables.robot
#Variables 		    ${CURDIR}\\${DATA_FILE}

Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}		16.114.209.223
${DATA_FILE}        ./Regression_Data.py

*** Test Cases ***
Add Gen10 Licenses
    Add Licenses

TestCase Verify Gen10 server hardware-Patch UID-ON-Reset-Off
    [Tags]    OVS8663-Verify
    Verify Gen10 server hardware Power Reset

TestCase Create Gen10 SPT
    [Tags]    OVS8663-spt    Performance    server_profiles-condition-jbods
    Create Gen10 Server Profile Template

TestCase Create Gen10 SY480 with LS RAID, JBODs and Legacy Bios
    [Tags]    OVS8663-sp
    Create Gen10 Server Profile 480 with Integrated and with JBODs

TestCase Edit Gen10-480 SP Change LS edit Boot BIOS
    [Tags]    OVS8663-editSP    Performance    server_profiles-condition-jbods
    Edit Gen10 Server Profile

TestCase Move profile from Enc1 to Enc2 to differnt Gen10 SHT
    [Tags]    OVS8663-moveSP
    Move profile from Enc1 to Enc2 to differnt SHT

*** Keywords ***
Setup
    [Documentation]  Setup
    Set Log Level  DEBUG
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

Verify Gen10 server hardware Power Reset
    [Documentation]  Gen10 server hardware Power Reset
    Run Keyword If	${verify_gen10_servers} is not ${null}		Verify Resources For list	${verify_gen10_servers}
    Patch Server Hardware  ${ENC1SHBAY6}  op=replace  path=/uidState  value=On
    Patch Server Hardware  ${ENC1SHBAY6}  op=replace  path=/uidState  value=Off
    Patch Server Hardware  ${ENC1SHBAY8}  op=replace  path=/uidState  value=On
    Patch Server Hardware  ${ENC1SHBAY8}  op=replace  path=/uidState  value=Off
    Power on Server  SH:${ENC1SHBAY8}
    Reset Server  ${ENC1SHBAY8}  powerControl=Reset
    Power off Server  ${ENC1SHBAY8}  powerControl=PressAndHold
    Power on Server  SH:${ENC1SHBAY8}
    Power off Server  ${ENC1SHBAY8}  powerControl=PressAndHold

Create Gen10 Server Profile Template
    [Documentation]  Gen10 Server Profile Template
    @{responses} =    Create List
    :FOR	${profile_template}	IN	@{gen10_profile_templates}
	\      ${resp} = 	Add Server Profile Template	${profile_template}
	\      log to console		${resp}
	\      Append To List    ${responses}    ${resp}

	Wait For Task2	${responses}	   timeout=60	interval=5

Create Gen10 Server Profile 480 with Integrated and with JBODs
    [Documentation]  Create Gen10 Server Profile 480 with Integrated and with JBODs
    @{responses} =    Create List
    :FOR	${server_profile}	IN	@{gen10_server_profiles}
	\      ${resp} = 	Add Server Profile	${server_profile}
	\      log to console		${resp}
	\      Append To List    ${responses}    ${resp}

	Wait For Task2    ${responses}    timeout=2400	interval=15

Edit Gen10 Server Profile
    [Documentation]  Gen10 Server Profile
     Power off Servers in Profiles  ${gen10_server_profiles}
	 ${resp} = 	Edit Server Profile	${edit_gen10_profile_boot_bios}
	 log to console		${resp}
	 Wait For Task2	${resp}	   timeout=2400	interval=15

Move profile from Enc1 to Enc2 to differnt SHT
    [Documentation]  Move profile from Enc1 to Enc2 to differnt SHT
    ${resp} = 	Edit Server Profile	${move_profile_from_enc1_XL_Bay8_harrier_to_enc2_R6_Bay8_Harrier}
	 log to console		${resp}
	 Wait For Task2	${resp}	   timeout=2400	interval=15

Remove All Licenses
    [Documentation]  Remove All Licenses
    Log    Removing all licenses    console=true
    ${getlicresp}=    Fusion Api Get Licenses
    :FOR    ${eachlic}     IN    @{getlicresp['members']}
    \       Continue For Loop If   '${eachlic["product"]}' != '${licenses["licenseType"]}'
    \       ${delResp}=    Fusion Api Remove License  uri=${eachlic['uri']}
    \       Should Be Equal As Integers    ${delResp["status_code"]}   204

Add Licenses
    [Documentation]  Add Licenses
    Log    Adding new licenses    console=true
    ${validLicenses}=     Get From Dictionary  ${licenses}  license
    Add Licenses From Variable    ${validLicenses}