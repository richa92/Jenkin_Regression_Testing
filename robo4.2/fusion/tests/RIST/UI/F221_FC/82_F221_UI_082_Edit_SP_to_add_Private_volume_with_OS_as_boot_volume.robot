*** Settings ***
Documentation   Edit Server Profile to add private volume with OS as boot volume

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_FC/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
As an Administrator I want to Edit Server Profile to add private volume with OS as boot volume
    ${rc}                               Fusion UI Edit Server Profile               @{TestData.F221UI082.Edit}
    Should Be True                      ${rc}   msg=Failed to edit server profile to add private volume with OS as boot volume
