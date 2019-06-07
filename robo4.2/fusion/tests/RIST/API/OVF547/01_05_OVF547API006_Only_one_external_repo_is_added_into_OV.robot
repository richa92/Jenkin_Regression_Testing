*** Settings ***
Documentation        Only one external repo is added into OV
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
${DataFile}         OVF547/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
Only one external repo is added into OV
    Log    \n Starting add web server as external repo${Http_repo_with_password}    console=true
    ${resp} =   Add Repository       ${Http_repo_with_password}
    ${task} =   Wait For Task2           ${resp}     50    5     errorMessage=${add_multi_error}
