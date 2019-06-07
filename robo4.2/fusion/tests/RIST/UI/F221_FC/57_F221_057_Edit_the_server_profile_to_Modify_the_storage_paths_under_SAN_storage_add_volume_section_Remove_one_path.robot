*** Settings ***

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup          Load Test Data and Open Browser and Login
Test Teardown       Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_FC/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Edit the server profile to Modify the storage paths under SAN storage --> add volume section Remove one path
    ${rc} =    Fusion Ui Create Server Profile     @{TestData.F221P057.Create}
    Should Be True    ${rc}   msg=Failed to create the server profile
    ${rc} =    Fusion Ui Edit Server Profile     @{TestData.F221P057.Edit}
    Should Be True    ${rc}   msg=Failed to Remove the Remove one path in the server profile

