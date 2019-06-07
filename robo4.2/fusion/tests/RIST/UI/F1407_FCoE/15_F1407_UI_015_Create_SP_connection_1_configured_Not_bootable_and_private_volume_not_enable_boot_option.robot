*** Settings ***
Documentation   Validation of server profile creation when connection 1 is configured to NOT BOOTABLE - with Managed volume - Private volume - Do not enable boot option

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
Validation of server profile creation when connection 1 is configured to NOT BOOTABLE - with Managed volume - Private volume - Do not enable boot option
    ${rc}                               Fusion UI Create Server Profile                     @{TestData.F1407UI015.Create}
    Should Be True                      ${rc}   msg=Failed to validate server profile creation with connection not bootable and Managed volume - Private volume - Do not enable boot option

    ${rc}                               Fusion UI Verify Server Profile SAN Storage Info    @{TestData.F1407UI015.Create}
    Should Be True                      ${rc}   msg=Failed to verify the private volume in the server profile
