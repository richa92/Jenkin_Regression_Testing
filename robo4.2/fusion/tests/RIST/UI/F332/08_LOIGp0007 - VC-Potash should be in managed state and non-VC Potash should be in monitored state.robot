*** Settings ***
Resource        ../resource.txt

Test Setup      Load Test Data And Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}                 F332/Regression_data.xml  # Data File Location
${ApplianceUrl}             https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
LOIGp0007 - VC-Potash should be in managed state and non-VC Potash should be in monitored state
    Log Into Fusion Appliance As Administrator

    Fusion Ui Validate Interconnect    @{TestData.LOIGp0007}