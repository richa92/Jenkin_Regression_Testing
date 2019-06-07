*** Settings ***
Documentation   Apply backup to server hardware with different hardware type

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FCoE/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
As an Administrator I want to apply backup to server hardware with different hardware type
    ${rc}                               Fusion UI Edit Server Profile                               @{TestData.F1407UI088.Edit}
    Should Be True                      ${rc}   msg=Failed to apply backup to server hardware with different hardware type