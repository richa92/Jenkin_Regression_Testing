*** Setting ***
Documentation   Create Server Profile from template for a blackbird server

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown	Pause And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F228/tbird-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
As an Administrator I want to create server profile template for a blackbird server
    ${rc}                               Fusion UI Create Server Profile from Template                   @{TestData.CreateSPForBL}
    should be true                      ${rc}   msg=Failed to create server profile template for a blackbird server