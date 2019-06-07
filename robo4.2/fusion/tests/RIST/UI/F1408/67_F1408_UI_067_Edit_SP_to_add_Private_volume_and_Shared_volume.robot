*** Settings ***
Documentation  Edit SP to add one Private volume and one Shared volume

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
Edit SP to add one Private volume and one Shared volume
    ${rc}                               Fusion UI Edit Server Profile                               @{TestData.F1408UI067.Edit}
    Should Be True                      ${rc}   msg=Failed to edit the SP to add Private volume and Shared volume.

    ${rc}                               Fusion UI Verify Server Profile San Storage Info            @{TestData.F1408UI067.Edit}
    Should Be True                      ${rc}   msg=Failed to verify Server Profile San Storage info