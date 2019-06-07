*** Settings ***
Documentation    OVF423 Firmware-SPT SBAC test
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py

Test Setup       Run Keywords    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
...              AND     Remove All Server Profile Templates Async
...              AND     Remove All Server Profiles
...              AND     Power Off All Servers    PressAndHold
Test Teardown    Run Keywords    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
...              AND     Remove All Server Profile Templates Async
...              AND     Remove All Server Profiles


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF423_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
SA cannot create SPT from SP and using SPP which is not in selected scope to do firmware online update
    ${firmware} =  Generate Firmware Body
    Set To Dictionary    ${server_profile}    firmware    ${firmware}
    ${resp} =    Add Server Profile With Scopes   ${server_profile}    ${ia_user_scopes}
    Wait For Task2    ${resp}    300    5

    ${spp} =    Get Firmware Bundle By Version  ${FirmwareVersion}
    ${scope} =    Get Scope URI By Name    ${ia_minor_scope}
    ${scopes} =  Create List    ${scope}
    ${resp} =    Edit Resource Scope    ${spp}    ${scopes}
    Wait For Task2    ${resp}

    Fusion Api Logout Appliance
    Fusion Api Login Appliance   ${APPLIANCE_IP}        ${sa_credentials}

    ${resp} =    Create Server Profile Template from Profile    ${server_profile}    ${SPT_name}    ${ia_part_scopes}
    Wait For Task2    ${resp}    600    10    PASS=Error    errorMessage=${not_authorized_error}    VERBOSE=True
