*** Settings ***
Documentation  Edit Server Profile to change Enclosure group

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
Edit Server Profile to change Enclosure group
    ${rc}                               Fusion UI Create Server Profile                               @{TestData.F1407UI084.Create}
    Should Be True                      ${rc}   msg=Failed to Create Server Profile
    ${rc}                               Fusion UI Create Tbird Enclosure Group                        @{TestData.F1407UI084.CreateEG}
    Should Be True                      ${rc}   msg=Failed to Create enclosure group
    ${rc}                               Fusion UI Edit Server Profile                                 @{TestData.F1407UI084.Edit}
    Should Be True                      ${rc}   msg=Failed to Edit Server Profile to change enclosure group
    Fusion UI Delete All Appliance Server Profiles
    Fusion UI Delete Enclosure Group                @{TestData.F1407UI084.DeleteEG}