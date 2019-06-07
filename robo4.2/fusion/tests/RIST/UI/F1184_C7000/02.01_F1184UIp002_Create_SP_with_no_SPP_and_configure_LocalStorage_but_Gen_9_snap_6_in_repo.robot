*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser Then Login
Test Teardown   Remove Profiles and Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F1184_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F1184UIp002 Create SP with no SPP and configure LocalStorage, but Gen 9 snap 6 in repo
    Fusion UI Create Server Profile      @{TestData.lsprofile}
    Fusion UI Validate Server Profile Task Step     @{TestData.lsprofile}
    ${rc}   Fusion UI Validate Server Profile Status     OK   @{TestData.lsprofile}
    Should Be True                      ${rc}   msg=Some server profile cannot be found
