*** Settings ***
Documentation  Validation of server profile creation when connection 1 is configured to Primary boot - with Managed volume Private Volume with OS.

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
Validation of server profile creation when connection 1 is configured to Primary boot - with Managed volume Private Volume with OS.
    ${rc}                               Fusion UI Create Server Profile                     @{TestData.F1408UI009.Create}
    Should Be True                      ${rc}   msg=Failed to validate server profile creation when connection 1 is configured to Primary boot - with Private Volume with OS.

    ${rc}                               Fusion UI Verify Server Profile SAN Storage Info    @{TestData.F1408UI009.Create}
    Should Be True                      ${rc}   msg=Failed to verify the private volume in the server profile

    ${rc}                               Fusion UI Verify Server Profile Connections Info    @{TestData.F1408UI009.Create}
    Should Be True                      ${rc}   msg=Failed to verify the connections info in the server profile
