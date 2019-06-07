*** Settings ***
Documentation        LE Big Bang FW update Shared Infra to work using Gen10 SPP
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
LE Big Bang FW update Shared Infra to work using Gen10 SPP
    Log    \n Starting update LE firmware    console=true
    Update Logical Enclosure Firmware       ${le_name}  ${FirmwareVersion}
