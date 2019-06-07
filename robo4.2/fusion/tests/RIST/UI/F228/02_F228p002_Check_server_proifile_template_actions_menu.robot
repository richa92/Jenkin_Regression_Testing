*** Setting ***
Documentation       Check Server Profile Template actions menu

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
As an Administrator I want to check Server Profile Templates actions menu
    ${rc}                               Fusion UI Validate Server Profile Templates Actions Menu
    should be true                      ${rc}   msg=Failed to verify profile templates action menu correct