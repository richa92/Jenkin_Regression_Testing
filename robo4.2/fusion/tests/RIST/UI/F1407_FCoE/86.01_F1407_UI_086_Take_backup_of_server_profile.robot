*** Settings ***
Documentation   Take backup of server profile

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FCoE/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
As an Administrator I want to take backup of the server profile
    ${rc}                               Fusion UI Create Server Profile                             @{TestData.F1407UI086.Create}
    Should Be True                      ${rc}   msg=Failed to create server profile

    ${rc}                               Fusion UI Copy Server Profile                               @{TestData.F1407UI086.Copy}
    Should Be True                      ${rc}   msg=Failed to take backup of the server profile

    Fusion UI Delete Server Profile By Name                                 ${TestData.F1407UI086.Delete[0].name}