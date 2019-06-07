*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser Then Login
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F458/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F458Tp009 Create LE with a firmware bundle, EM and iLO firmware are same with or higher than FB
    Fusion UI Create TBird Logical Enclosure      @{TestData.snap6LE}
    Fusion Ui Validate Logical Enclosure Firmware    @{TestData.snap6LE}

