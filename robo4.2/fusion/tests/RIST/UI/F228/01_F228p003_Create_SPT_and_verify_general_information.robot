*** Setting ***
Documentation       Create server profile template and verify general information

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
As an Administrator I want to create server profile template and verify general information
    Fusion UI Power Off All Servers
    # ensure aoo
    Fusion UI Create Server Profile Template                                                                @{TestData.CreateSPT}
    ${rc}                               Fusion UI Verify Server Profile Template General Info               @{TestData.CreateSPT}
    should be true                      ${rc}    msg=Failed to verify general informatin