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
F607UIp018 Create LE with a firmware bundle, force installation
    Fusion UI Create TBird Logical Enclosure      @{TestData.oldsnap6forceLE}
    ${rc}=   Fusion Ui Validate Logical Enclosure Firmware    @{TestData.oldsnap6forceLE}
    Should Be True                      ${rc}   msg=Some logical enclosure firmware update unsuccessfully
    ${rc}=   Fusion Ui Delete Logical Enclosure      @{TestData.oldsnap6forceLE}
    Should Be True                      ${rc}   msg=Remove logical enclosure failed, error message:${rc}
