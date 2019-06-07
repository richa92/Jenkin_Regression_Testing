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
IA cannot edit SP and using SPP which is not in its scope to do firmware offline update
    set log level    TRACE

    ${resp} =    Add Server Profile With Spcopes   ${server_profile}    ${ia_part_scopes}
    Wait For Task2    ${resp}   3000

    ${spp} =    Get Firmware Bundle By Version  ${Gen10Firmware}
    ${scopes} =  Create List
    :FOR    ${scope_name}    IN    @{ia_except_scopes}
    \    ${scope} =    Get Scope URI By Name    ${scope_name}
    \    Append To List    ${scopes}    ${scope}
    ${resp} =    Edit Resource Scope    ${spp}    ${scopes}
    Wait For Task2    ${resp}

    Fusion Api Logout Appliance
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${ia_credentials}

    ${resp}=  Edit Server Profile with FW    ${Gen10Firmware}   ${online_type}    ${server_profile}
    Wait For Task2    ${resp}    600    10    PASS=Error    errorMessage=${association_error}    VERBOSE=True