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
F458Tp005 Create LE with firmware baseline not set, EM and iLO firmware are at or or above the minimum supported version
    Fusion UI Create TBird Logical Enclosure      @{TestData.nosetLE}
    Fusion Ui Validate Logical Enclosure Firmware    @{TestData.nosetLE}
    ${rc}=   Fusion Ui Delete Logical Enclosure      @{TestData.nosetLE}
    Should Be True                      ${rc}   msg=Remove logical enclosure failed, error message:${rc}

