*** Settings ***
Documentation  Edit Server Profile to change HOST OS TYPE

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FC/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Edit Server Profile to change HOST OS TYPE
    ${rc}                               Fusion UI Create Server Profile                               @{TestData.F1407UI085.Create}
    Should Be True                      ${rc}   msg=Failed to Create server profile
    ${rc}                               Fusion UI Edit Server Profile                                 @{TestData.F1407UI085.Edit}
    Should Be True                      ${rc}   msg=Failed to Edit Server Profile to change HOST OS TYPE