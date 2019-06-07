*** Settings ***
Documentation        Delete SPP or hotfix which is present only in an external repo will not work
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
Delete SPP or hotfix which is present only in an external repo will not work
    Log    \n Starting delete SPP or hotfix which is present only in an external repo    console=true
    ${uri} =    Get Firmware Bundle By Version    ${hpsut_version}
    ${resp} =   Remove Firmware Bundle    ${uri}
    ${task} =   Wait For Task2           ${resp}     200    5     errorMessage=${remove_external_error}