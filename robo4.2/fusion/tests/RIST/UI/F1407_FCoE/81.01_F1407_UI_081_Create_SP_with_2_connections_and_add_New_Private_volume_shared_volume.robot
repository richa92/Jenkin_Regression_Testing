*** Settings ***
Documentation   Create SP with 2 connections(primary boot and secondary boot), assign new private volume, add another shared volume

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FCoE/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Create SP with 2 connections(primary boot and secondary boot), assign new private volume, add another shared volume
    ${rc}                               Fusion UI Create Server Profile                                 @{TestData.F1407UI081.Create}
    Should Be True                      ${rc}   msg=Failed to Create Server Profile

    ${rc}                               Fusion UI Verify Server Profile San Storage Info                @{TestData.F1407UI081.Create}
    Should Be True                      ${rc}   msg=Failed to verify Server Profile San Storage info