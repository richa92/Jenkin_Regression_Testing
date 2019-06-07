*** Settings ***

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup          Load Test Data and Open Browser and Login
Test Teardown       Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FCoE/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Edit the server profile to add one more Private volume to the server profile
    ${rc} =    Fusion Ui Create Server Profile     @{TestData.EmptyProfile}
    Should Be True    ${rc}   msg=Failed to create the server profile
    ${rc} =    Fusion Ui Edit Server Profile     @{TestData.F1407P031.Edit}
    Should Be True    ${rc}   msg=Failed to add the private volume in the server profile
    ${rc} =    Fusion UI Verify Server Profile SAN Storage Info    @{TestData.F1407P031.Edit}
    Should Be True    ${rc}   msg=Failed to verify the private volume in the server profile
    ${rc} =    Fusion UI Verify Server Profile Connections Info    @{TestData.F1407P031.Edit}
    Should Be True    ${rc}   msg=Failed to verify the connections info in the server profile