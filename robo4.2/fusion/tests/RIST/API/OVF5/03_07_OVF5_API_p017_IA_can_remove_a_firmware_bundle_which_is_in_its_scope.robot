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
IA can remove a firmware bundle which is in its scope
    Log    \n IA can remove a firmware bundle which is in its scope    console=true
    ${firmware} =    Get Firmware Bundle By Version  ${Upload_SPP_Version}
    ${scopes} =  Create List
    :FOR    ${scope_name}    IN    @{ia_user_scopes}
    \    ${scope} =    Get Scope URI By Name    ${scope_name}
    \    Append To List    ${scopes}    ${scope}
    ${resp} =    Edit Resource Scope    ${firmware}    ${scopes}
    Wait For Task2    ${resp}

    Fusion Api Logout Appliance
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${ia_credentials}
    ${resp} =    Remove Firmware Bundle By Version    ${Upload_SPP_Version}
    Wait For Task2    ${resp}
