*** Settings ***
Documentation   Edit server profile template

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
As an Administrator I want to edit server profile template
    #Ensure Server Profile Template has been created
    ${rc}                               Fusion UI Edit Server Profile Template                          @{TestData.EditSPT}
    Should be true                      ${rc}   msg=Failed to edit server profile template