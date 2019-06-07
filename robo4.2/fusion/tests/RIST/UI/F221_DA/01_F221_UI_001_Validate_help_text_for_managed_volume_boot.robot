*** Settings ***
Documentation   Validation of help text for managed volume boot option on Add connection

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear Profile and Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_DA/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Validation of help text for managed volume boot option on add connection
    ${rc}                                   Fusion UI Validate Help Text For Managed Volume on Add Connection Dialog                     @{TestData.F221UI001.Create}
    Should Be True                          ${rc}   msg=Failed to validate help text for managed volume boot
