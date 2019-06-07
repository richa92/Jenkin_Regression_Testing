*** Settings ***
Documentation  Edit Server Profile Boot Setting from Legacy BIOS to UEFI OptimiZed mode

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_FCoE/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Edit Server Profile Boot Setting from Legacy BIOS to UEFI OptimiZed mode
    ${rc}                               Fusion UI Edit Server Profile                                 @{TestData.F221UI077.Edit}
    Should Be True                      ${rc}   msg=Failed to Edit Server Profile Boot Setting from Legacy BIOS to UEFI OptimiZed mode

    ${rc}                               Fusion UI Verify Server Profile San Storage Info              @{TestData.F221UI077.Verify}
    Should Be True                      ${rc}   msg=Failed to verify Server Profile San Storage info