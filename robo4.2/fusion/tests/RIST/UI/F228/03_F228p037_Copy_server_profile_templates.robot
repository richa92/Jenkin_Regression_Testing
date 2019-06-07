*** Settings ***
Documentation   Copy server profile templates

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
As an Administrator I want to copy server profile templates
    #Ensure Server Profile Template has been created
    ${rc}                               Fusion UI Copy Server Profile Template                          @{TestData.CopySPT}
    Should be true                      ${rc}   msg=Failed to copy server profile template
    ${rc}                               Fusion UI Verify Server Profile Template General Info           @{TestData.CopySPT}
    Should be true                      ${rc}   msg=Failed to verify server profile template