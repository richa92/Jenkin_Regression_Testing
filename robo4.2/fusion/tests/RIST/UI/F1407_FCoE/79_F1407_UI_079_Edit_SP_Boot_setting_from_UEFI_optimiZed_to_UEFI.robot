*** Settings ***
Documentation  Edit Server Profile Boot Setting from UEFI OptimiZed to UEFI mode

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FCoE/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Edit Server Profile Boot Setting from UEFI OptimiZed to UEFI mode
    ${rc}                               Fusion UI Edit Server Profile                                 @{TestData.F1407UI079.Edit}
    Should Be True                      ${rc}   msg=Failed to Edit Server Profile Boot Setting from UEFI OptimiZed to UEFI mode

    ${rc}                               Fusion UI Verify Server Profile San Storage Info              @{TestData.F1407UI079.Verify}
    Should Be True                      ${rc}   msg=Failed to verify Server Profile San Storage info