*** Setting ***
Documentation   Create SP from SPT for unassigned server

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
As an Administrator I want to create SP from SPT for unassigned server
    Fusion UI Create Server Profile Template                            @{TestData.CreateSPT}
    ${rc}                               Fusion UI Create Server Profile from Template                               @{TestData.apply}
    should be true                      ${rc}   msg=Fail to create SP from SPT for unassigned server by overriding and not overriding
