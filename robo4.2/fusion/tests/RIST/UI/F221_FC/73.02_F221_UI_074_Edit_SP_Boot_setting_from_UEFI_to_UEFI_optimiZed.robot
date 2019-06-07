*** Settings ***
Documentation  Edit Server Profile Boot Setting from UEFI to UEFI_OptimiZed

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_FC/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Edit Server Profile Boot Setting from UEFI to UEFI_OptimiZed
    ${rc}                               Fusion UI Edit Server Profile                                 @{TestData.F221UI074.Edit}
    Should Be True                      ${rc}   msg=Failed to Edit Server Profile Boot Setting from UEFI to UEFI_OptimiZed

    ${rc}                               Fusion UI Verify Server Profile San Storage Info              @{TestData.F221UI074.Verify}
    Should Be True                      ${rc}   msg=Failed to verify Server Profile San Storage info