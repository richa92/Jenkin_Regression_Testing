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
F1184UIp008 Update firmware with Gen 9 snap 6 by HPSUT online and configure local storage.
    Fusion UI Create Server Profile      @{TestData.snap6olprofile}
    Fusion UI Validate Server Profile Task Step     @{TestData.snap6olprofile}
    ${rc}   Fusion UI Validate Server Profile Status     OK,Warning   @{TestData.snap6olprofile}
    Should Be True                      ${rc}   msg=Some server profile cannot be found
