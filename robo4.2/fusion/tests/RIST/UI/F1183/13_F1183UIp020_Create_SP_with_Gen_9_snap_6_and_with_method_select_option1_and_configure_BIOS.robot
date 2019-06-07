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
F1183UIp020 Create SP with Gen 9 snap 6 and with method select option1 and configure BIOS
    Fusion UI Create Server Profile      @{TestData.F1183p020}
    Fusion UI Validate Server Profile Task Step     @{TestData.F1183p020}
    ${rc}   Fusion UI Validate Server Profile Status     WARNING  @{TestData.F1183p020}
    Should Be True                      ${rc}   msg=Some server profile cannot be found
