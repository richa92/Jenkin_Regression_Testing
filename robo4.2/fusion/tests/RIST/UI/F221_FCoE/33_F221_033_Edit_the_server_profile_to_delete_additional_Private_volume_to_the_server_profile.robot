*** Settings ***

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup          Load Test Data and Open Browser and Login
Test Teardown       Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_FCoE/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Edit the server profile to delete additional Private volume to the server profile
    ${rc} =    Fusion Ui Create Server Profile     @{TestData.F221P033.Create}
    Should Be True    ${rc}   msg=Failed to create the server profile
    ${rc} =    Fusion Ui Edit Server Profile     @{TestData.F221P033.Edit}
    Should Be True    ${rc}   msg=Failed to remove the private volume in the server profile
    ${rc} =    Fusion UI Verify Server Profile SAN Storage Info    @{TestData.F221P033.Edit}
    Should Be True    ${rc}   msg=Failed to verify the private volume in the server profile
    ${rc} =    Fusion UI Verify Server Profile Connections Info    @{TestData.F221P033.Edit}
    Should Be True    ${rc}   msg=Failed to verify the connections info in the server profile