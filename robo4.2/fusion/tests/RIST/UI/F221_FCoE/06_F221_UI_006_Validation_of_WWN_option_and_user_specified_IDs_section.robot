*** Settings ***
Documentation   Verification of the option where user can manually enter the WWN details - Users specified IDs section

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_FCoE/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Verification of the option where user can manually enter the WWN details - Users specified IDs section
    ${rc}                               Fusion UI Create Server Profile                     @{TestData.F221UI006.Create}
    Should Be True                      ${rc}   msg=Failed to validate WWN details and Users specified IDs section

    ${rc}                               Fusion UI Verify Server Profile Connections Info    @{TestData.F221UI006.Create}
    Should Be True                      ${rc}   msg=Failed to vefify