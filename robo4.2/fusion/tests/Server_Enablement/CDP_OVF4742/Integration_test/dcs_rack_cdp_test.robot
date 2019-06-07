*** Settings ***
Documentation                CDP integration test for DCS rack servers

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
Test case1 Import server
    [Documentation]     This testcase imports a rack server
    [Tags]         Import
    Import the server      ${rack_server_add}

Test case2 Create the server profile
    [Documentation]   Test case to create a server profile with delault BIOS and boot settings
    [Tags]     Createsp
    Create Server profile    ${Server_profile}

Test case3 Power on Server
    [Documentation]   Test case to power on the server hardware
    [Tags]        Poweron
    Power on the Server        ${rack_server_ilo_hostname}

Test case4 Edit the server profile ( Legacy Bios editing the bios settings)
    [Documentation]   Test case to edit a server profile
    [Tags]    editsp        Integrate_1        Integrate_2
    Edit the server profile        ${rack_Server_edit_profile}

Test case5 Edit the server profile with Firmware update
    [Documentation]   Test case to edit a server profile with firmware updates
    [Tags]    Firmware        Integrate_2
    Edit the server profile        ${rack_Server_edit_profile_with_firmware}

Test case6 Power off Server
    [Documentation]   Test case to power off the server hardware
    [Tags]        Poweroff        Integrate_1        Integrate_2
    Power off the Server        ${rack_server_ilo_hostname}

Test case7 Delete server profile
    [Documentation]   Test case to delete a server profile
    [Tags]        Deletesp        Integrate_1        Integrate_2
    Delete Server profile        ${Server_profile}

Test case8 Remove Server from OV
    [Documentation]     This testcase removes a rack server from OV
    [Tags]        Remove        Integrate_1        Integrate_2
    Remove All DL Server Hardware Async

*** Keywords ***
Setup
    [Documentation]    Setup
    Set Log Level  DEBUG
    ${admin_session} =    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${rack_admin_credentials}

Clean Up
    [Documentation]    Teardown
    Fusion Api Logout Appliance

Import the server
    [Documentation]        Adds a server
    [Arguments]        ${servers}
    ${resps}=    Add Server hardware from variable    ${servers}
    Wait For Task2    ${resps}  timeout=1200  interval=5

Create Server profile
     [Documentation]          Create  Server Profiles
    [Arguments]     ${profiles}
    Power off Servers in Profiles      ${profiles}
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{profiles}
    \      ${resp} =     Add Server Profile        ${server_profile}
    \      Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}    timeout=2600    interval=15

Edit the server profile
     [Documentation]           Edit Server Profiles
    [Arguments]     ${profiles}
    Power off Servers in Profiles      ${profiles}
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{profiles}
    \      ${resp} =     Edit Server Profile        ${server_profile}
    \      Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}    timeout=2600    interval=15

Power on the Server
    [Documentation]  Powering on server profile
    [Arguments]        ${server}
    Log    Powering on server        console=True
    Power on Server    ${server}
    ${power_state}=    Get Server Power    ${server}
    Run keyword if    '${power_state}'!='On'    FAIL    Server power on failed

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
