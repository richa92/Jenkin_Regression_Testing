*** Settings ***
Documentation   Create SP, with managed volume, Add New Volume instead of existing volume - permanent option is selected.

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown	Pause And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FC/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Create SP, with managed volume, Add New Volume instead of existing volume - permanent option is selected.
    ${rc}                               Fusion UI Create Server Profile             @{TestData.F1407UI027.Create}
    Should Be True                      ${rc}   msg=Failed to create SP with managed volume, Add New Volume instead of existing volume - permanent option is selected.