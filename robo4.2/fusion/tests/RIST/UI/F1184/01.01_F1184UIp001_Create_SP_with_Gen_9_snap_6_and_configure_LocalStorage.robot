*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser Then Login
Test Teardown   Remove Profiles and Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F1184/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F1184UIp001 Create SP with Gen 9 snap 6 and configure LocalStorage
    Fusion UI Create Server Profile      @{TestData.snap6lsprofile}
    Fusion UI Validate Server Profile Task Step     @{TestData.snap6lsprofile}
    ${rc}   Fusion UI Validate Server Profile Status     OK   @{TestData.snap6lsprofile}
    Should Be True                      ${rc}   msg=Some server profile cannot be found
