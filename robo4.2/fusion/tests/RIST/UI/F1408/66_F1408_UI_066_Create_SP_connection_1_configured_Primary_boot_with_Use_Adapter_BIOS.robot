*** Settings ***
Documentation  Validation of server profile creation when connection 1 is configured to Primary boot - Adapter BIOS - Private volume - not enable boot option

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1408/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Validation of server profile creation when connection 1 is configured to Primary boot - with Adapter BIOS - Private volume - Not enable boot option
    ${rc}                                   Fusion UI Create Server Profile                     @{TestData.F1408UI066.Create}
    Should Be True                          ${rc}   msg=Failed to validate server profile creation with connection primary boot -Adapter BIOS - Private volume - Not enable boot option

    ${rc}                                   Fusion UI Verify Server Profile SAN Storage Info    @{TestData.F1408UI066.Create}
    Should Be True                          ${rc}   msg=Failed to verify the shared volume in the server profile