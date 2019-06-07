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
Test Teardown    Run Keywords    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
...              AND     Remove All Server Profile Templates Async

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF423_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
SA can edit SPT which have firmware baseline which is not in selected scope to unassign SPP
    ${firmware} =  Generate Firmware Body
    Set To Dictionary    ${profile_template}    firmware    ${firmware}
    ${resp} =    Add Server Profile Template With Scopes   ${profile_template}    ${ia_part_scopes}
    Wait For Task2    ${resp}

    ${spp} =    Get Firmware Bundle By Version  ${FirmwareVersion}
    ${scope} =    Get Scope URI By Name    ${ia_minor_scope}
    ${scopes} =  Create List    ${scope}
    ${resp} =    Edit Resource Scope    ${spp}    ${scopes}
    Wait For Task2    ${resp}

    Fusion Api Logout Appliance
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${ia_credentials}

    Set To Dictionary    ${profile_template}    firmware    ${empty_firmware_payload}
    ${resp} =    Edit Server Profile Template   ${profile_template}
    Wait For Task2    ${resp}

