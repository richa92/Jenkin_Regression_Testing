*** Settings ***
Documentation   Validation of user specified invisible during editing boot option

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear Profile and Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1408/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Validation of user specified invisible during editing boot option
    ${rc}                                   Fusion UI Create Server Profile                                 @{TestData.F1408UI097.Create}
    Should Be True                          ${rc}   msg=Failed to Create Server Profile

    ${rc}                                   Fusion UI Validate User Specified Invisible On Edit Connection Dialog                     @{TestData.F1408UI097.Edit}
    Should be true                          ${rc}   msg=Failed to validate user specified invisible during editing boot option