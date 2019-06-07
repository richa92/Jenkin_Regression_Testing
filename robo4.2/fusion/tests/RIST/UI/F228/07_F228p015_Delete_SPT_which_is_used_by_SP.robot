*** Settings ***
Documentation   Delete server profile template which is used by server profile

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
As an Administrator I want to delete server profile template which is used by server profile
    ${rc}                               Fusion UI Validate Server Profile Template In Use Cannot Be Deleted                @{TestData.delete}
    should be true                      ${rc}   msg=Failed to validate server profile template in use cannot be deleted