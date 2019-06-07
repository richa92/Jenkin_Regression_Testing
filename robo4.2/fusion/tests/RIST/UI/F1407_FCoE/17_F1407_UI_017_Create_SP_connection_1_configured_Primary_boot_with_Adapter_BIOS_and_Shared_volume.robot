*** Settings ***
Documentation   Validation of server profile creation when connection 1 is configured to Primary boot -Adapter BIOS - Shared volume

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FCoE/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Validation of server profile creation when connection 1 is configured to Primary boot - with Managed volume - Shared volume
    ${rc}                                   Fusion UI Create Server Profile                     @{TestData.F1407UI017.Create}
    Should Be True                          ${rc}   msg=Failed to validate server profile creation with connection primary boot -Adapter BIOS - shared volume

    ${rc}                                   Fusion UI Verify Server Profile SAN Storage Info    @{TestData.F1407UI017.Create}
    Should Be True                          ${rc}   msg=Failed to verify the shared volume in the server profile
