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
Edit scope and remove hotfix
    Log    \n Create scope with hotfix    console=true
    ${firmware} =    Get Firmware Bundle By Version  ${HotFixVersion}
    ${firmwares} =  Create List    ${firmware}
    ${resp} =    Edit Scope    name=${scope_name_a}    removeresources=${firmwares}
    Wait For Task2    ${resp}
    ${scope} =    Get Scope URI By Name    ${scope_name_a}
    Validate Resource Not Assign To Scope    ${scope}    ${firmware}

