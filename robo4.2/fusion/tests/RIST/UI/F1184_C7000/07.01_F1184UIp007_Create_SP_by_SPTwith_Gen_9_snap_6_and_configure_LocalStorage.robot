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
F1184UIp007 Create SP by SPTwith Gen 9 snap 6 and configure LocalStorage
    Fusion UI Create Server Profile Template      @{TestData.snap6profiletemplate}
    Fusion UI Create Server Profile From Template        @{TestData.snap6profilefromtemplate}
    Fusion UI Validate Server Profile Task Step     @{TestData.snap6profilefromtemplate}
    ${rc}   Fusion UI Validate Server Profile Status     OK   @{TestData.snap6profilefromtemplate}
    Should Be True                      ${rc}   msg=Some server profile cannot be found

