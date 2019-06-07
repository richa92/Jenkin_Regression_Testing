*** Settings ***

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup          Load Test Data and Open Browser and Login
Test Teardown       Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_FC/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Edit the server profile to Change the boot volume from OS to OS
    ${rc} =    Fusion Ui Create Server Profile     @{TestData.F221P037.Create}
    Should Be True    ${rc}   msg=Failed to create the server profile
    ${rc} =    Fusion Ui Edit Server Profile     @{TestData.F221P037.Edit}
    Should Be True    ${rc}   msg=Failed to change the boot volume in the server profile
    ${rc} =    Fusion UI Verify Server Profile SAN Storage Info    @{TestData.F221P037.Edit}
    Should Be True    ${rc}   msg=Failed to verify boot volume changed in the server profile
    ${rc} =    Fusion UI Verify Server Profile Connections Info    @{TestData.F221P037.Edit}
    Should Be True    ${rc}   msg=Failed to verify the connections info in the server profile
