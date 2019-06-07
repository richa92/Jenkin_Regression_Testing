*** Settings ***
Documentation   Edit SP to change boot option from Managed wolume to Specify boot target
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
Edit SP to change boot option from Managed wolume to Specify boot target
    ${rc}                               Fusion UI Create Server Profile                             @{TestData.F1407UI098.Create}
    Should Be True                      ${rc}   msg=Failed to Create Server Profile with Boot option - Manged volume

    ${rc}                               Fusion UI Edit Server Profile                               @{TestData.F1407UI098.Edit}
    Should Be True                      ${rc}   msg=Failed to Edit Server Profile to change Boot option from Managed volume to Specify boot target
