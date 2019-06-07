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
F1183UIp009 Edit SP with no SPP and configure BIOS, but Gen 9 snap 6 in repo, expect using HPSUTool
    Fusion UI Create Server Profile      @{TestData.emptyprofile}
    Fusion UI Edit Server Profile        @{TestData.F1183p009}
    Fusion UI Validate Server Profile Task Step     @{TestData.F1183p009}
    ${rc}   Fusion UI Validate Server Profile Status     OK   @{TestData.F1183p009}
    Should Be True                      ${rc}   msg=Some server profile cannot be found
