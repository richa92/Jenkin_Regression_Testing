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
F1540UIp027 – Import C7000 enclosure with Gen7 blade iLO version less than minimum when Gen10 SPP not in repo(Error message and resulotion should be shown)
    Log to console and logfile  \nTest to downgrade C7000 OA/ILO/VC firmware and add it to appliance
    Remove All Firmware Bundles
    Clear Multi OA VC Mode            ${Wpst32}
    Reset iLO and Update Server ILO Firmware        ${G8BLServer}
    Reset iLO and Update Server ILO Firmware        ${G9BLServer}
    Run Keyword And Ignore Error    Fusion Ui Add Enclosure           @{TestData.Wpst32}
