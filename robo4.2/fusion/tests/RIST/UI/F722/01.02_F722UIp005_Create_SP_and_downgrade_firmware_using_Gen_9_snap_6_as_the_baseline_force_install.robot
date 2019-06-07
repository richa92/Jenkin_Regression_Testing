*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser Then Login      OldSnap6
Test Teardown   Remove Profiles and Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F722/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F722UIp005 Create SP and downgrade firmware using Gen 9 snap 6 as the baseline(force install)
    Fusion UI Create Server Profile      @{TestData.snap6profile}
    Fusion UI Validate Server Profile Task Step     @{TestData.snap6profile}
    ${rc}   Fusion UI Validate Server Profile Status     OK   @{TestData.snap6profile}
    Should Be True                      ${rc}   msg=Some server profile cannot be found

