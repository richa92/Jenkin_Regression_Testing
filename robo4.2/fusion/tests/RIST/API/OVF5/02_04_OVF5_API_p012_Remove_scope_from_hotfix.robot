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
Test Teardown   Remove Scope By Name    ${scope_name_b}

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF5/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
Remove scope from hotfix
    Log    \n Remove scope from hotfix    console=true
    ${firmware} =    Get Firmware Bundle By Version  ${HotfixVersion}
    ${scopes} =  Create List
    ${resp} =    Edit Resource Scope    ${firmware}    ${scopes}
    Wait For Task2    ${resp}
    ${scope} =    Get Scope URI By Name    ${scope_name_b}
    Validate Resource Not Assign To Scope    ${scope}    ${firmware}

