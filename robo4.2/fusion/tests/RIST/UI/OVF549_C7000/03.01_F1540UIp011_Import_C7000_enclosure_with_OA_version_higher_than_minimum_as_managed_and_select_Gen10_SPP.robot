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
F1540UIp011 – Import C7000 enclosure with OA version higher than minimum as managed and select Gen10 SPP(Firmware should be update unless not less than SPP)
    Run Keyword And Ignore Error    Fusion Ui Add Enclosure           @{TestData.Wpst32withSPP}
    ${rc}   Fusion UI Validate Enclosure Sub Task      @{TestData.ValidateOAnotUpdate}
    Should Be True                      ${rc}   msg=Some enclosures cannot be found
