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
F1540UIp034 – Upload a Gen10 SPP and check firmware component
    Remove All Firmware Bundles
    Log to console and logfile  \nTest to upload firmware bunlde and check component
    Fusion UI Add Latest Firmware Bundle    @{TestData.spps}
    Fusion UI Validate Firmware Bundle Component   @{TestData.spps}
