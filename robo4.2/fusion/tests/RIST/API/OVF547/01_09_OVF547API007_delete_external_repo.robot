*** Settings ***
Documentation        Delete external repo
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
Test Setup      Run Keyword And Ignore Error     Remove Repository

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF547/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Delete external repo
    Log    \n Starting delete external repo    console=true
    ${resp} =   Remove Repository By Name     ${delete_name}
    ${task} =   Wait For Task2           ${resp}     50    5
    Verify Firmwares Exist    ${ValidateFirmwares}    ${False}