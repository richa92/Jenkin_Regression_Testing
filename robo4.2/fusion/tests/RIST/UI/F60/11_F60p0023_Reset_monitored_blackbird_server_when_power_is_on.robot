*** Settings ***
Documentation   Reset monitored blackbird server when power is on

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause and close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F60/tbird-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
As an Administrator I want to reset monitored balckbird server when power is on
    Fusion ui power on all servers
    #Ensure Server Power is on before resetting
    ${rc}                               Fusion ui reset server              @{TestData.Tbird14Blackbays}
    should be true                      ${rc}   msg=Fail to reset monitored balckbird server when power is on

    ${rc}                               Fusion ui cold boot server          @{TestData.Tbird14Blackbays}
    should be true                      ${rc}   msg=Fail to cool boot monitored balckbird server when power is on