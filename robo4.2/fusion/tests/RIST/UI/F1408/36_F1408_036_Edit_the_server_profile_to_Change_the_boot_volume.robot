*** Settings ***
Documentation    "Edit the server profile to Change the boot volume - With 2 primary volumes, one with OS, other without OS. Change the boot volume from OS volume to NON OS volume."

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup          Load Test Data and Open Browser and Login
Test Teardown       Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1408/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Edit the server profile to Change the boot volume from OS to Non-OS
    ${rc} =    Fusion Ui Create Server Profile     @{TestData.F1408P036.Create}
    Should Be True    ${rc}   msg=Failed to create the server profile
    ${rc} =    Fusion Ui Edit Server Profile     @{TestData.F1408P036.Edit}
    Should Be True    ${rc}   msg=Failed to change the boot volume in the server profile
    ${rc} =    Fusion UI Verify Server Profile SAN Storage Info    @{TestData.F1408P036.Edit}
    Should Be True    ${rc}   msg=Failed to verify boot volume changed in the server profile
    ${rc} =    Fusion UI Verify Server Profile Connections Info    @{TestData.F1408P036.Edit}
    Should Be True    ${rc}   msg=Failed to verify the connections info in the server profile