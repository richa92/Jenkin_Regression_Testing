*** Settings ***
Documentation    OVF5 Firmware SBAC test
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keyword.txt
Variables            ./Regression_Data.py

Test Setup      Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
Test Teardown   Remove Firmware Bundle By Name     ${custom_spp_name}

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF5/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
IA can create custom spp using a firmware bundle and hotfix which is in selected scope but have different scope
    Log    \n IA can create custom spp using a firmware bundle and hotfix which is in selected scope but have different scope    console=true
    ${firmware} =    Get Firmware Bundle By Version  ${HotFixVersion}
    ${scope} =    Get Scope URI By Name    ${ia_minor_scope}
    ${scopes} =  Create List    ${scope}
    ${resp} =    Edit Resource Scope    ${firmware}    ${scopes}
    Wait For Task2    ${resp}

    Fusion Api Logout Appliance
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${ia_credentials}

    ${spp} =    Get Firmware Bundle By Version  ${FirmwareVersion}

    ${hotfix} =    Get Firmware Bundle By Version  ${HotFixVersion}
    ${hotfixs} =  Create List    ${hotfix}

    ${scopes} =  Create List
    :FOR    ${scope_name}    IN    @{ia_user_scopes}
    \    ${scope} =    Get Scope URI By Name    ${scope_name}
    \    Append To List    ${scopes}    ${scope}

    ${resp} =    Create Custom SPP    ${custom_spp_name}    ${spp}   ${hotfixs}    ${scopes}
    Wait For Task2    ${resp}    1200    10
