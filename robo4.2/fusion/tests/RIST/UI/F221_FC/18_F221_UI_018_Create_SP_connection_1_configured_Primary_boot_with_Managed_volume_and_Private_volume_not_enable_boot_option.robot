*** Settings ***
Documentation   Validation of  server profile creation when connection 1 is configured to Primary boot - with Managed volume - Private volume _ Do not enable bootoption

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown	Clear Profile And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_FC/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Create SP with connection 1 is configured to Primary boot - with Managed volume - Private volume - do not enable boot option
    ${rc}                                   Fusion UI Create Server Profile                     @{TestData.F221UI018.Create}
    Should Be True                          ${rc}   msg=Failed to create SP with connection 1 primary boot and managed private volume and boot option not enable

    ${rc}                                   Fusion UI Verify Server Profile SAN Storage Info    @{TestData.F221UI018.Create}
    Should Be True                          ${rc}   msg=Failed to verify the private volume in the server profile
