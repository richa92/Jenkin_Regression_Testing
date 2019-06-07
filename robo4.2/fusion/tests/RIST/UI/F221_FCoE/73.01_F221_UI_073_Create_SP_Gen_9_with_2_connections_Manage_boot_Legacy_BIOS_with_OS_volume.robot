*** Settings ***
Documentation   Create SP on Gen 9 server with 2 connections - Boot settings - Manage boot mode - Select boot mode as "Legacy BIOS" - with OS volume

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
Create SP on Gen 9 server with 2 connections - Boot settings - Manage boot mode - Select boot mode as "Legacy BIOS" - with OS volume
    ${rc}                               Fusion UI Create Server Profile                               @{TestData.F221UI073.Create}
    Should Be True                      ${rc}   msg=Failed to Create SP on Gen 9 with 2 connections - Boot settings - Manage boot mode - Select boot mode as Legacy BIOS - with OS volume

    ${rc}                               Fusion UI Verify Server Profile San Storage Info              @{TestData.F221UI073.Create}
    Should Be True                      ${rc}   msg=Failed to verify Server Profile San Storage info