*** Settings ***
Documentation   Update from template foe a server profile

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
As an Administrator I want to update from template for a server profile
    ${rc}                               Fusion UI Update Profile From Template                  ${TestData.UpdateFromTemplate[0].name}
    should be true                      ${rc}   msg=Failed to update from template for a server profile