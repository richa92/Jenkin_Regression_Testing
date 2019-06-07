*** Settings ***
Documentation                   Gen10 DL Server profiles Local storage, edit Bios, edit Boot
...                               -  DL180 - SA in Embedded - create profile with Reinitialize Rd0 with 1 drive with SATA Hdd, Legacy Bios boot mode, bios custom msg
...                                     - edit profile - change Rd0 to Rd1 with 2  drives. Remove profile, create profile with imported drives, verify RIS for drives
...                               -  Remove all DL profiles

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

Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}     $(None}

*** Test Cases ***
OVS8663-DL-Add Licenses
    [Tags]    Add-Lic
    Add Licenses

OVS8663-DL-TestCase Add DL380 Gen10 server as managed
    [Tags]    Add-DLs
    Add DL380 Gen10 server as managed

OVS8663-DL-TestCase Verify DL Gen10 server hardware
    [Tags]    Verify-DLs
    Verify DL Gen10 server hardware Power Reset

OVS8663-DL-TestCase Create DL Gen10 SPT
    [Tags]    Add-DL-Ts
    Create DL Gen10 Server Profile Template

OVS8663-DL-TestCase Create DL Gen10 Profiles with Local Storage
    [Tags]    Create-DL-SPs    Performance    server_profiles-condition-jbods
    Create DL Gen10 Server Profiles with Local storage

OVS8663-Verify Logical Drives with RIS
    [Tags]    Verify-CreateSP-Ris
    Power on Servers in Profiles  ${DL_gen10_server_profiles}
    Run Keyword and Ignore Error    Wait for Servers in Profiles to reach POST State  ${DL_gen10_server_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=7m
    Verify Servers PowerState in Profiles  ${DL_gen10_server_profiles}  On
    Wait Until Keyword Succeeds  1 min  5 sec  Verify RIS Nodes for List  ${ris_nodes_create}
    Power off Servers in Profiles    ${DL_gen10_server_profiles}

OVS8663-DL-TestCase Edit DL Gen10 SP
    [Tags]    Edit-DLs    Performance    server_profiles-condition-jbods
    Edit DL Gen10 Server Profiles

OVS8663-Remove Profiles, create profiles with imported drives
    [Tags]    Remove-SPs-Recreate
    ${resp} =    Remove Server Profiles from variable    ${DL_gen10_server_profiles}
    Wait For Task2    ${resp}	   timeout=2400	interval=15
    Create DL Gen10 profiles with imported drives

OVS8663-Verify Logical Drives with RIS After Import drives
    [Tags]    Verify-Ris
    Power on Servers in Profiles  ${DL_gen10_server_profiles}
    Run Keyword and Ignore Error    Wait for Servers in Profiles to reach POST State  ${DL_gen10_server_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=7m
    Run Keyword and Ignore Error    Wait for Servers in Profiles to reach POST State  ${DL_gen10_server_profiles}  post_state=FINISHED_POST  timeout=2m
    Verify Servers PowerState in Profiles  ${DL_gen10_server_profiles}  On
    Wait Until Keyword Succeeds  1 min  5 sec  Verify RIS Nodes for List  ${ris_nodes_after_import}
    Power off Servers in Profiles    ${DL_gen10_server_profiles}

*** Keywords ***
Setup
    [Documentation]    OVS8663 Gen10 Setup
    Set Log Level  DEBUG
    ${admin_session} =    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    ${resp} =    Remove Server Profiles from variable    ${DL_gen10_server_profiles}
    Wait For Task2    ${resp}	   timeout=2400	interval=15

Clean Up
    [Documentation]    OVS8663 Gen10 Teardown
    Power off Servers in Profiles    ${DL_gen10_server_profiles_imported_drives}
    ${resp} =    Remove Server Profiles from variable    ${DL_gen10_server_profiles_imported_drives}
    Wait For Task2    ${resp}       timeout=2400    interval=15
    Remove Server Profile Templates from variable  ${DL_gen10_profile_templates}
    Remove All DL Server Hardware Async
    Fusion Api Logout Appliance

Verify DL Gen10 server hardware Power Reset
    [Documentation]    Verify DL Gen10 server hardware Power Reset
    Run Keyword If    ${verify_DL_gen10_servers} is not ${null}        Verify Resources For list    ${verify_DL_gen10_servers}
    Power on Servers in Profiles  ${DL_gen10_server_profiles}
    @{responses} =    Create List
    :FOR    ${dl}    IN    @{Gen10_DLs_with_profiles}
    \      ${resp} =     Reset Server  ${dl}  powerControl=Reset
    \      log to console        ${resp}
    \      Append To List    ${responses}    ${resp}
    Power off Servers in Profiles  ${DL_gen10_server_profiles}

Create DL Gen10 Server Profile Template
    [Documentation]  Create DL Gen10 Server Profile Template
    @{responses} =    Create List
    :FOR    ${profile_template}    IN    @{DL_gen10_profile_templates}
    \      ${resp} =     Add Server Profile Template    ${profile_template}
    \      log to console        ${resp}
    \      Append To List    ${responses}    ${resp}

    Wait For Task2    ${responses}       timeout=60    interval=5

Create DL Gen10 Server Profiles with Local storage
    [Documentation]  Create DL Gen10 Server Profiles with Local storage
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{DL_gen10_server_profiles}
    \      ${resp} =     Add Server Profile    ${server_profile}
    \      log to console        ${resp}
    \      Append To List    ${responses}    ${resp}

    Wait For Task2    ${responses}    timeout=2400    interval=15

Edit DL Gen10 Server Profiles
    [Documentation]  Edit DL Gen10 Server Profiles
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{edit_DL_gen10_profiles}
    \      ${resp} =     Edit Server Profile    ${server_profile}
    \      log to console        ${resp}
    \      Append To List    ${responses}    ${resp}

    Wait For Task2    ${responses}    timeout=2400    interval=15

Add Licenses
    [Documentation]  Add Licenses
    Log    Adding new licenses    console=true
    ${validLicenses}=     Get From Dictionary  ${licenses}  license
    Add Licenses From Variable    ${validLicenses}

Add DL380 Gen10 server as managed
    [Documentation]    Add Gen10 DL servers as managed
    ${resps}=    Add Server hardware from variable    ${Gen10_DLs}
    Wait For Task2    ${resps}  timeout=10m  interval=5

Create DL Gen10 profiles with imported drives
    [Documentation]  Create DL Gen10 profiles with imported drives
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{DL_gen10_server_profiles_imported_drives}
    \      ${resp} =     Add Server Profile    ${server_profile}
    \      log to console        ${resp}
    \      Append To List    ${responses}    ${resp}

    Wait For Task2    ${responses}    timeout=2400    interval=15