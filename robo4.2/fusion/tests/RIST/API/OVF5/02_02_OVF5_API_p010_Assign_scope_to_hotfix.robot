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
Assign scope to hotfix
    Log    \n Assign scope to hotfix    console=true
    ${firmwares} =  Create List
    ${scope} =    Generate Scope body    ${scope_name_b}    ${firmwares}
    ${resp} =    Create Scope    ${scope}
    Wait For Task2    ${resp}
    ${firmware} =    Get Firmware Bundle By Version  ${HotfixVersion}
    ${scope} =    Get Scope URI By Name    ${scope_name_b}
    ${scopes} =  Create List    ${scope}
    ${resp} =    Edit Resource Scope    ${firmware}    ${scopes}
    Wait For Task2    ${resp}
    ${scope} =    Get Scope URI By Name    ${scope_name_b}
    Validate Resource Assign To Scope    ${scope}    ${firmware}

