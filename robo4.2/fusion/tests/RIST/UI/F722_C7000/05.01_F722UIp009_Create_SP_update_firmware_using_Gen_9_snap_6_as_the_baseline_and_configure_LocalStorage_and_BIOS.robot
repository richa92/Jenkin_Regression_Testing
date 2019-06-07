*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser Then Login
Test Teardown   Remove Profiles and Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F722_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F722UIp009 Create SP, update firmware using Gen 9 snap 6 as the baseline and configure LocalStorage and BIOS
    Fusion UI Create Server Profile      @{TestData.snap6lsprofile}
    Fusion UI Validate Server Profile Task Step     @{TestData.snap6lsprofile}
    ${rc}   Fusion UI Validate Server Profile Status     OK   @{TestData.snap6lsprofile}
    Should Be True                      ${rc}   msg=Some server profile cannot be found

