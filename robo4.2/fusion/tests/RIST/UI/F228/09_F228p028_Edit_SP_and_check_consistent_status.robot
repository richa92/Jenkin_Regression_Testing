*** Settings ***
Documentation   Edit server profile and check consistent status

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
As an Administrator I want to edit server profile and check consistency state
    ${rc}                               Fusion UI Edit Server Profile                                   @{TestData.EditSPForInconsistency}
    ${rc}                               Fusion UI Validate Server Profile Consistency State               @{TestData.CheckSPForInconsistency}
    should be true                      ${rc}   msg=Failed to verify server profile consistency state