*** Setting ***
Documentation   Refresh blackbird server in monitored status

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F60/tbird-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
As an Administrator I want to refresh blackbird server in monitored status
    ${rc}                               Fusion UI Refresh Server                      @{TestData.Tbird14Blackbays}
    should be true                      ${rc}   msg=Failed to refresh blackbird server in monitored status