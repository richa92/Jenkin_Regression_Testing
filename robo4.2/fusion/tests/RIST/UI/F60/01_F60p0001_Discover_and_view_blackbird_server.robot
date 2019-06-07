*** Settings ***
Documentation   Discover and view blackbird server

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown	Pause And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F60/tbird-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
As an Administrator I want to discover and view blackbird server
    ${rc}                               Fusion UI Validate Server Hardware Managed                   @{TestData.Tbird14Blackbays}
    should be true                      ${rc}   msg=Failed to validate server hardware is managed
    Fusion UI Power Off All Server Hardware
    ${rc}                               Fusion UI Validate Server Hardware Page Hardware             @{TestData.Tbird14BlackbirdForManaged}
    should be true                      ${rc}   msg=Failed to discover and view blackbird server