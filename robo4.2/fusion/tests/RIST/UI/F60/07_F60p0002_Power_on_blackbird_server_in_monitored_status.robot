*** Settings ***
Documentation    Power on blackbird server in monitored status

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
As an Administrator I want to power on blackbird server in monitored status
    ${rc}                               Fusion UI Delete Logical Enclosure      @{TestData.Tbird14LogicalEnclosure}
    Should be True                      ${rc}   msg=Failed to delete logical enclosure
    ${rc}                               Fusion UI Validate Server Hardware Monitored        @{TestData.Tbird14Blackbays}
    should be true                      ${rc}   msg=Failed to validate server hardware is monitored

    Fusion UI Power off all Server Hardware
    #Ensure Server Power is off before powering on
    ${rc}=                              Fusion UI Power on Server Hardware      @{TestData.Tbird14Blackbays}
    Should be True                      ${rc}   msg=Failed to power on blackbird server in monitored status