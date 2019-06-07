*** Settings ***
Documentation   Create SP with proper connection and is configured to Primary boot - with Managed Volume - private volume with OS

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown	Clear Profile And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_DA/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Create SP with proper connection and is configured to Primary boot - with Managed volume Private volume with OS. Delete the SP and create another SP with same configuration
    ${rc}                               Fusion UI Create Server Profile                     @{TestData.F221UI020.Create}
    Should Be True                      ${rc}   msg=Failed to create server profile

    ${rc}                               Fusion UI Delete All Appliance Server Profiles
    Should Be True                      ${rc}   msg=Failed to delete server profile

    ${rc}                               Fusion UI Create Server Profile                     @{TestData.F221UI020.Create}
    Should Be True                      ${rc}   msg=Failed to create server profile with same configuration