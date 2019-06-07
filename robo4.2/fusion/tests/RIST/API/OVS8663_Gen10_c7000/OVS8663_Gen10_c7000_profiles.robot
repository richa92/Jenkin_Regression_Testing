*** Settings ***
Documentation                   Gen10 Server profiles connections, Local storage, edit Bios, edit Boot
...                               -  Add Base Resources networks
...                               -  Add LIG, create EG, and LE
...                               -  Create Gen10 BL460c Server profiles with connections, Local storage, edit Bios, edit Boot, move
...                               -  Remove Base Resources

Library             FusionLibrary
Library             RoboGalaxyLibrary
Library             BuiltIn
Library             Collections
Library             json
Library             XML
Library             String
Library             Dialogs

Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables           ${DATA_FILE}

#Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
#Resource            ../global_variables.robot
#Variables             ${CURDIR}\\${DATA_FILE}

Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}     $(None}

*** Test Cases ***
Add Licenses
    Add Licenses

TestCase Verify Gen10 server hardware-Patch UID-ON-Reset-Off
    Verify Gen10 server hardware Power Reset

TestCase Create Gen10 SPT
    Create Gen10 Server Profile Template

TestCase Create Gen10-BL460c Server profile with LS RAID1 UEFI and BIOS custom message
    [Tags]    Performance    server_profiles-condition-jbods
    Create Gen10 Server Profiles with Local storage

TestCase Edit Gen10-660 SP Change LS to Raid0 changed to Legacy
    [Tags]    Performance    server_profiles-condition-jbods
    Edit Gen10 Server Profile

TestCase Move profile from Enc1 to Enc2 same SHT
    Move profile from Enc1 to Enc2 same SHT

*** Keywords ***
Setup
    [Documentation]    OVS8663 Gen10 Setup
    Set Log Level  DEBUG
    ${admin_session} =    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    Power off ALL Servers    PressAndHold
    ${resp} =    Remove All Server Profiles Async
    Wait For Task2    ${resp}    timeout=2400    interval=15

Clean Up
    [Documentation]    OVS8663 Gen10 Teardown
    Power off Servers in Profiles    ${gen10_server_profiles}
    ${resp} =    Remove All Server Profiles Async
    Wait For Task2    ${resp}       timeout=2400    interval=15
    Remove All Server Profile Templates
    Fusion Api Logout Appliance

Verify Gen10 server hardware Power Reset
    [Documentation]    Verify Gen10 server hardware Power Reset
    Run Keyword If    ${verify_gen10_servers} is not ${None}        Verify Resources For list    ${verify_gen10_servers}
    Patch Server Hardware  ${ENC1SHBAY16}  op=replace  path=/uidState  value=On
    Patch Server Hardware  ${ENC1SHBAY16}  op=replace  path=/uidState  value=Off
    Power on Server  SH:${ENC1SHBAY16}
    Reset Server  ${ENC1SHBAY16}  powerControl=Reset
    Power off Server  ${ENC1SHBAY16}  powerControl=PressAndHold
    Power on Server  SH:${ENC1SHBAY16}
    Power off Server  ${ENC1SHBAY16}  powerControl=PressAndHold

Create Gen10 Server Profile Template
    [Documentation]    Create Gen10 Server Profile Template
    @{responses} =    Create List
    :FOR    ${profile_template}    IN    @{gen10_profile_templates}
    \      ${resp} =     Add Server Profile Template    ${profile_template}
    \      log to console    ${resp}
    \      Append To List    ${responses}    ${resp}

    Wait For Task2    ${responses}       timeout=60    interval=5

Create Gen10 Server Profiles with Local storage
    [Documentation]    Create Gen10 Server Profiles with Local storage
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{gen10_server_profiles}
    \      ${resp} =     Add Server Profile    ${server_profile}
    \      log to console        ${resp}
    \      Append To List    ${responses}    ${resp}

    Wait For Task2    ${responses}    timeout=2400    interval=15

Edit Gen10 Server Profile
    [Documentation]    Edit Gen10 Server Profile
    Power off Servers in Profiles  ${gen10_server_profiles}
    ${resp} =     Edit Server Profile    ${edit_gen10_profile_boot_bios}
    log to console        ${resp}
    Wait For Task2    ${resp}       timeout=2400    interval=15

Move profile from Enc1 to Enc2 same SHT
    [Documentation]    Move profile from Enc1 to Enc2 same SHT
    ${resp}=     Edit Server Profile    ${move_profile_from_enc1_to_enc2}
    log to console        ${resp}
    Wait For Task2    ${resp}       timeout=2400    interval=15

Add Licenses
    [Documentation]    Add licenses
    Log    Adding new licenses    console=true
    Add Licenses From Variable    ${licenses}
