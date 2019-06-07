*** Settings ***
Resource        ../resource.txt

Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F178/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***

F178Tp011, update natasha LI firmware with force parallel
    Log Into Fusion Appliance As Administrator
    ${Status}=    Fusion UI Update Firmware Tbird Natasha Logical Interconnect     @{TestData.f178_p011}
    Should Be True                  ${Status}   msg=Failed to update natasha li firmware
