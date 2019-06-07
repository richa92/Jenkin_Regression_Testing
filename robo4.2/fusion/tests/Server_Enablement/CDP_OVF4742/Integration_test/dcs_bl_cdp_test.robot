*** Settings ***
Documentation                    CDP integration test for DCS blade servers

Library             FusionLibrary
Library             RoboGalaxyLibrary
Library             SSHLibrary
Library             BuiltIn
Library             Collections
Library             json
Library             XML
Library             String
Library             Dialogs
Library             ./../../../../Resources/api/common/RisHelpers.py
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Variables           ./dcs_cdp.py
Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}     16.83.14.88

*** Test Cases ***

Test case2 Create the server profile
    [Documentation]   Test case to create a server profile with default BIOS and boot settings
    [Tags]     Createsp        Integrate_1        Integrate_2
    Create Server profile        ${bl_Server_profile}

Test case3 Power on Server
    [Documentation]   Test case to power on the server hardware
    [Tags]        Poweron        Integrate_1        Integrate_2
    Power on the Server        ${bl_server_ilo_hostname}

Test case4 Edit the server profile ( Legacy Bios editing the bios settings)
    [Documentation]   Test case to edit a server profile
    [Tags]    editsp        Integrate_1        Integrate_2
    Edit the server profile        ${bl_Server_edit_profile}

Test case5 Edit the server profile and flash firmware
    [Documentation]   Test case to edit a server profile with firmware update
    [Tags]    firmware    Integrate_2
    Edit the server profile        ${bl_Server_edit_profile_with_firmware}

Test case Power on Server
    [Documentation]   Test case to power on the server hardware
    [Tags]        Poweron        Integrate_1        Integrate_2
    Power on the Server        ${bl_server_ilo_hostname}

Test case6 Power off Server
    [Documentation]   Test case to power off the server hardware
    [Tags]        Poweroff        Integrate_1        Integrate_2
    Power off the Server        ${bl_server_ilo_hostname}

Test case7 Delete server profile
    [Documentation]   Test case to delete a server profile
    [Tags]        Deletesp        Integrate_1        Integrate_2
    Delete Server profile        ${bl_Server_profile}

*** Keywords ***
Setup
    [Documentation]    Setup
    Set Log Level  DEBUG
    ${admin_session} =    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${bl_admin_credentials}

Clean Up
    [Documentation]    Teardown
    Fusion Api Logout Appliance

Create Server profile
     [Documentation]          Create  Server Profiles
    [Arguments]     ${profiles}
    Power off Servers in Profiles      ${profiles}
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{profiles}
    \      ${resp} =     Add Server Profile        ${server_profile}
    \      Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}    timeout=2600    interval=15

Power on the Server
    [Documentation]     Powering on server profile
    [Arguments]        ${server}
    Log    Powering on server        console=True
    Power on Server    ${server}
    ${power_state}=    Get Server Power    ${server}
    Run keyword if    '${power_state}'!='On'    FAIL    Server power on failed

Edit the server profile
     [Documentation]          Edit Server Profiles
    [Arguments]     ${profiles}
    Power off Servers in Profiles      ${profiles}
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{profiles}
    \      ${resp} =     Edit Server Profile        ${server_profile}
    \      Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}    timeout=3800    interval=15

Power off the Server
    [Documentation]  Powering off server profile
    [Arguments]        ${server}
    Log    Powering off server        console=True
    Power off Server    ${server}
    ${power_state}=    Get Server Power    ${server}
    Run keyword if    '${power_state}'!='Off'    FAIL    Server power off failed

Delete Server profile
     [Documentation]        Delete  Server Profiles
    [Arguments]            ${profiles}
    Power off Servers in Profiles    ${profiles}
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{profiles}
    \      ${resp} =     Remove Server Profile    ${server_profile}    force=False
    \      Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}    timeout=2400    interval=15