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
F1540UIp024 – Import Gen8 DL with iLO version less than minimum when Gen10 SPP in repo(Firmware should be updated)
    Log to console and logfile  \nTest to downgrade DL server ilo and add it to appliance
    Reset iLO and Update Server ILO Firmware      ${G8DLServer}
    Run Keyword And Ignore Error    Fusion UI Add Server Hardware   @{TestData.Gen8DLServers}
    ${rc}   Fusion UI Validate Server Sub Task      @{TestData.ValidateGen8DLUpdate}
    Should Be True                      ${rc}   msg=Some servers cannot be found
