*** Settings ***
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keyword.txt
Variables            ./Regression_Data.py

Test Setup      Load Test Data and Open Browser then Login
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF549_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F1540UIp019 – Import C7000 enclosure with Gen8 blade iLO version higher than minimum and select Gen10 SPP with force install(Firmware should not be updated)
    ${rc}   Fusion UI Validate Enclosure Sub Task      @{TestData.ValidateGen8BLnotUpdate}
    Should Be True                      ${rc}   msg=Some enclosures cannot be found
