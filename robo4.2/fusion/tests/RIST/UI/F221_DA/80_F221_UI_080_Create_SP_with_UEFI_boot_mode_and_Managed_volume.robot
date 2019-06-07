*** Settings ***
Documentation   Create SP with UEFI boot mode and managed volume

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_DA/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Create SP with UEFI boot mode and managed volume
    ${rc}                               Fusion UI Create Server Profile                                 @{TestData.F221UI080.Create}
    should be true                      ${rc}   msg=Failed to Create SP with UEFI boot mode and managed volume

