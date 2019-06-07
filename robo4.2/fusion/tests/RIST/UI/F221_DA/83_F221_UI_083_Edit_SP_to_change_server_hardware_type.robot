*** Settings ***
Documentation   Edit Server Profile to change server hardware type

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
Edit Server Profile to change server hardware type
    ${rc}                               Fusion UI Create Server Profile                               @{TestData.F221UI083.Create}
    Should Be True                      ${rc}   msg=Failed to Craete enclosure group
    ${rc}                               Fusion UI Edit Server Profile                                 @{TestData.F221UI083.Edit}
    Should Be True                      ${rc}   msg=Failed to Edit Server Profile to change server hardware type
