*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser Then Login
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F607/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F607UIp001 Update server firmware by creating LE with single enclosure without force installation
    Fusion UI Create TBird Logical Enclosure      @{TestData.snap6LE}
    ${rc}=  Fusion Ui Validate Logical Enclosure Firmware    @{TestData.snap6LE}
    Should Be True                      ${rc}   msg=Some logical enclosure firmware update unsuccessfully

