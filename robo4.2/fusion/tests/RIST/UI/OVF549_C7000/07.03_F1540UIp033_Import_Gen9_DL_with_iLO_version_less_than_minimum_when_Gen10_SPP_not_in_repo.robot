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

Test Setup      Load Test Data and Open Browser then Remove All Hardwares
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF549_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F1540UIp033 – Import Gen9 DL with iLO version less than minimum when Gen10 SPP not in repo(Error message and resulotion should be shown)
    Log to console and logfile  \nTest to downgrade DL ILO firmware and add it to appliance
    Reset iLO and Update Server ILO Firmware      ${G9DLServer}
    ${msg} =   Run Keyword and Expect Error   *    Fusion UI Add Server Hardware   @{TestData.Gen9DLServers}
    Should Contain   ${msg}   ${DLFirmwareError}
    Should Contain   ${msg}   ${DLFirmwareResolution}
