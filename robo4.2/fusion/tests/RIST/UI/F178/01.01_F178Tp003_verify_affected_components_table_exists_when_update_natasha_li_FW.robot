*** Settings ***
Resource        ../resource.txt

Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}                 F178/Regression_data.xml  # Data File Location
${ApplianceUrl}             https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***

F178Tp003, check affected components table exists in update natasha LI firmware dialog
    Log Into Fusion Appliance As Administrator
    ${Status}=    Fusion UI Update Firmware Tbird Natasha Li Validate Affected Components     @{TestData.f178}
    Should Be True                  ${Status}   msg=Affected components table does not exists

