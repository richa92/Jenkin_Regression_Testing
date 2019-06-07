*** Settings ***
Documentation    Power off(Momentary press) blackbird server in monitored status

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and login
Test Teardown   Pause And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F60/tbird-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
As an Administrator I want to power off(Momentary press) blackbird server in monitored status
    Fusion UI Power on All Servers
    #Ensure Server Power is on before powering off
    ${rc}=                              Fusion UI Power Off Server Hardware               @{TestData.PowerOffMomentaryForTbird14}
    Should be True                      ${rc}   msg=Failed to power off(Momentary press) blackbird server in monitored status