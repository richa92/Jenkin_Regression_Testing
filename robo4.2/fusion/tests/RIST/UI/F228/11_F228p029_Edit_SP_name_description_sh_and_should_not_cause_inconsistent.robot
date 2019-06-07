*** Settings ***
Documentation   Edit server profile(name,description,serverhardware) and should not cause inconsistent

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F228/tbird-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Validate that SP consistency state should not change when server profile(name,description,serverhardware) changed.
    ${rc}                               Fusion UI Edit Server Profile                                   @{TestData.EditSPForConsistency}
    should be true                      ${rc}   msg=Failed to edit server profile
    ${rc}                               Fusion UI Validate Server Profile Consistency State               @{TestData.CheckSPForConsistency}
    should be true                      ${rc}   msg=Failed to verify server profile consistency state