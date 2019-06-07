*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser Then Login
Test Teardown   Remove Profiles and Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F722/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F722UIn008 Assign SP with downgrade firmware using Gen 9 snap 6 as the baseline to a hardware
    Fusion UI Create Server Profile      @{TestData.unassignednoforceprofile}
    Fusion UI Edit Server Profile        @{TestData.assignednoforceprofile}
    Fusion UI Validate Server Profile Task Step     @{TestData.assignednoforceprofile}
    ${rc}   Fusion UI Validate Server Profile Status     OK   @{TestData.assignednoforceprofile}
    Should Be True                      ${rc}   msg=Some server profile cannot be found

