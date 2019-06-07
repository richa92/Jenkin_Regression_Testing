*** Settings ***
Documentation  Verification of the option where user can manually enter the WWN details - Users specified IDs section

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1408/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Verification of the option where user can manually enter the WWN details - Users specified IDs section
    ${rc}                               Fusion UI Create Server Profile                     @{TestData.F1408UI006.Create}
    Should Be True                      ${rc}   msg=Failed to validate WWN details and Users specified IDs section

    ${rc}                               Fusion UI Verify Server Profile Connections Info    @{TestData.F1408UI006.Create}
    Should Be True                      ${rc}   msg=Failed to verify server profile connections info
