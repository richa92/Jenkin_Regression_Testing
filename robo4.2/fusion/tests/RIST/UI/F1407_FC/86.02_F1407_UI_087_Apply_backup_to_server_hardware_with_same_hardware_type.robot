*** Settings ***
Documentation   Apply backup to server hardware with same hardware type

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FC/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
As an Administrator I want to apply backup to server hardware with same hardware type
    ${rc}                               Fusion UI Edit Server Profile           @{TestData.F1407UI087.Edit}
    Should Be True                      ${rc}   msg=Failed to apply backup to server hardware with same hardware type

    Fusion UI Delete Server Profile By Name                                     ${TestData.F1407UI087.Delete[0].name}