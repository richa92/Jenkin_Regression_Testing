*** Settings ***

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup          Load Test Data and Open Browser and Login
Test Teardown       Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FC/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Edit the server profile to Change Connection from Not bootbale to Primary Boot
    ${rc} =    Fusion Ui Create Server Profile     @{TestData.F1407P062.Create}
    Should Be True    ${rc}   msg=Failed to create the server profile
    ${rc} =    Fusion Ui Edit Server Profile     @{TestData.F1407P062.Edit}
    Should Be True    ${rc}   msg=Failed to Change Connection from Not bootbale to Primary Boot in the server profile
    ${rc} =    Fusion UI Verify Server Profile Connections Info    @{TestData.F1407P062.Edit}
    Should Be True    ${rc}   msg=Failed to verify the connections info in the server profile
