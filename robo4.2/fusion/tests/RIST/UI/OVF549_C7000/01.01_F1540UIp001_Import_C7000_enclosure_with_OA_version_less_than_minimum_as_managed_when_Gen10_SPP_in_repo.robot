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
F1540UIp001 - Import C7000 enclosure with OA version less than minimum as managed when Gen10 SPP in repo(Firmware should be updated)
    Log to console and logfile  \nTest to downgrade C7000 OA/ILO/VC firmware and add it to appliance
    Clear Multi OA VC Mode            ${Wpst32}
    Reset iLO and Update Server ILO Firmware        ${G8BLServer}
    Reset iLO and Update Server ILO Firmware        ${G9BLServer}
    Update Multi OA Firmware          ${Wpst32}
    Run Keyword And Ignore Error    Fusion Ui Add Enclosure           @{TestData.Wpst32}
    ${rc}   Fusion UI Validate Enclosure Sub Task      @{TestData.ValidateOAUpdate}
    Should Be True                      ${rc}   msg=Some enclosures cannot be found
