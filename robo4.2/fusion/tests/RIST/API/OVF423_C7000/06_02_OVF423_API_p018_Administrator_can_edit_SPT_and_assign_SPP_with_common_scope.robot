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
Administrator can edit SPT and assign SPP with common scope
    ${resp} =    Add Server Profile Template With Scopes   ${empty_profile_template}    ${ia_user_scopes}
    Wait For Task2    ${resp}

    ${spp} =    Get Firmware Bundle By Version  ${FirmwareVersion}
    ${scopes} =  Create List
    :FOR    ${scope_name}    IN    @{ia_part_scopes}
    \    ${scope} =    Get Scope URI By Name    ${scope_name}
    \    Append To List    ${scopes}    ${scope}
    ${resp} =    Edit Resource Scope    ${spp}    ${scopes}
    Wait For Task2    ${resp}

    ${firmware} =  Generate Firmware Body
    Set To Dictionary    ${profile_template}    firmware    ${firmware}
    ${resp} =    Edit Server Profile Template   ${profile_template}
    Wait For Task2    ${resp}

