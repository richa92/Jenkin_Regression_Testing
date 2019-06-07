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

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF5/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
IA cannot create custom spp and assign scope with invalid uri
    Log    \n IA cannot create custom spp and assign scope with invalid uri    console=true
    ${spp} =    Get Firmware Bundle By Version  ${SPPVersion}
    ${hotfix} =    Get Firmware Bundle By Version  ${HotFixVersion}
    ${scopes} =  Create List
    :FOR    ${scope_name}    IN    @{ia_user_scopes}
    \    ${scope} =    Get Scope URI By Name    ${scope_name}
    \    Append To List    ${scopes}    ${scope}
    ${resp} =    Edit Resource Scope    ${spp}    ${scopes}
    Wait For Task2    ${resp}
    ${resp} =    Edit Resource Scope    ${hotfix}    ${scopes}
    Wait For Task2    ${resp}

    Fusion Api Logout Appliance
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${ia_credentials}

    ${hotfixs} =  Create List    ${hotfix}

    ${scopes} =  Create List    ${invalidScope}

    ${resp} =    Create Custom SPP    ${custom_spp_name}    ${spp}   ${hotfixs}    ${scopes}
    Wait For Task2    ${resp}    600    10    PASS=Error    errorMessage=${creation_not_authorized_error}    VERBOSE=True
