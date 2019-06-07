*** Settings ***
Documentation    Power off(press and hold) blackbird server in managed status

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
As an Administrator I want to power off(Press and hold) blackbird server in managed status
    Fusion ui Power on all Servers
    #Ensure Server Power is on before powering off
    ${rc}=                              fusion ui power off server hardware                     @{TestData.Tbird14Blackbays}
    Should be True                      ${rc}   msg=Failed to power off(press and hold) blackbird server in managed status