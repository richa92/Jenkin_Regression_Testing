*** Settings ***
Documentation    OVF99 Firmware-SP SBAC test
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
Test Teardown    Run Keywords    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
...              AND     Remove All Server Profile Templates Async
...              AND     Remove All Server Profiles

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF99_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
IA cannot create SP using SPT and using SPP which is in another scope to do firmware online update
    set log level    TRACE
    ${spp} =    Get Firmware Bundle By Version  ${Gen10Firmware}
    ${scope} =    Get Scope URI By Name    ${ia_scope_scope}
    ${scopes} =  Create List    ${scope}
    ${resp} =    Edit Resource Scope    ${spp}    ${scopes}
    Wait For Task2    ${resp}

    ${firmware} =  Generate Firmware Body  ${Gen9Firmware}   ${online_type}
    Set To Dictionary    ${profile_template}    firmware    ${firmware}
    ${resp} =    Add Server Profile Template With Scopes   ${profile_template}    ${ia_anoher_scope}
    Wait For Task2    ${resp}

    Fusion Api Logout Appliance
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${ia_credentials}

    ${server_profile_template_uri} =    Get Server Profile Template URI    ${profile_template['name']}

    ${createBLProfileFromSPT} =    Set To Dictionary    ${createBLProfileFromSPT}    serverProfileTemplateUri    ${server_profile_template_uri}
    ${resp} =    Add Server Profile From SPT With Firmware and Scopes   ${createBLProfileFromSPT}    ${ia_anoher_scope}    ${Gen10Firmware}    ${online_type}    ${sp_param}
    Wait For Task2    ${resp}    600    10    PASS=Error    errorMessage=${association_error}    VERBOSE=True