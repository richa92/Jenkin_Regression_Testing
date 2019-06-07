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
IA cannot edit SPT and using SPP which is in selected scope to do firmware online update
    ${resp} =    Add Server Profile Template With Scopes   ${empty_profile_template}    ${ia_part_scopes}
    Wait For Task2    ${resp}

    ${spp} =    Get Firmware Bundle By Version  ${FirmwareVersion}
    ${scope} =    Get Scope URI By Name    ${ia_minor_scope}
    ${scopes} =  Create List    ${scope}
    ${resp} =    Edit Resource Scope    ${spp}    ${scopes}
    Wait For Task2    ${resp}

    Fusion Api Logout Appliance
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${ia_credentials}

    ${firmware} =  Generate Firmware Body
    Set To Dictionary    ${profile_template}    firmware    ${firmware}
    ${resp} =    Edit Server Profile Template   ${profile_template}
    Wait For Task2    ${resp}    600    10    PASS=Error    errorMessage=${association_error}    VERBOSE=True

