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

Test Setup      Fusion Api Login Appliance         ${APPLIANCE_IP}        ${ia_credentials}

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF5/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
IA can read a hotfix details which is not in its scope
    Log    \n IA can read a hotfix details which is not in its scope    console=true
    ${uri} =    Get Firmware Bundle By Version  ${HotFixVersion}
    ${hotfix} =    Get Firmware Bundle   ${uri}
    Should Be Equal    ${hotfix['version']}    ${HotFixVersion}
