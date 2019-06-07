*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser Then Login
Test Teardown   Remove Profiles and Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F1183/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F1183UIp006 Create SP with Gen 9 snap 6 and configure BIOS with valid value for input type settings
    Fusion UI Create Server Profile      @{TestData.F1183p006}
    Fusion UI Validate Server Profile Task Step     @{TestData.F1183p006}
    ${rc}   Fusion UI Validate Server Profile Status     OK   @{TestData.F1183p006}
    Should Be True                      ${rc}   msg=Some server profile cannot be found
