*** Settings ***
Documentation   Create SP with LUN number manually assigned

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown	Clear Profile And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FCoE/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Create SP with LUN manually addigned
    ${rc}                               Fusion UI Create Server Profile                     @{TestData.F1407UI024.Create}
    Should Be True                      ${rc}   msg=Failed to create SP with LUN number manually assigned

    ${rc}                               Fusion UI Verify Server Profile SAN Storage Info    @{TestData.F1407UI024.Create}
    Should Be True                      ${rc}   msg=Failed to verify the private volume in the server profile

    ${rc}                               Fusion UI Verify Server Profile Connections Info    @{TestData.F1407UI024.Create}
    Should Be True                      ${rc}   msg=Failed to verify the connections info in the server profile