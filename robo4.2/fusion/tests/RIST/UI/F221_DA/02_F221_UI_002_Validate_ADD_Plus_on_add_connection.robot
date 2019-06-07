*** Settings ***
Documentation   Validation of ADD plus in managed volume section

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
Validation of ADD plus in managed volume section
    ${rc}                                   Fusion UI Validate Add Plus on Add Connection Dialog                    @{TestData.F221UI002.Create}
    Should Be True                          ${rc}   msg=Failed to validate ADD plus in managed volume section