*** Settings ***
Documentation   Edit SP to change boot option from Managed wolume to Specify boot target
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
Edit SP to change boot option from Managed wolume to Specify boot target
    ${rc}                               Fusion UI Create Server Profile                             @{TestData.F1407UI099.Create}
    Should Be True                      ${rc}   msg=Failed to Create Server Profile with Boot volume - private volume

    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToEditProfileErrMessage}   ${nonManagedVolumeIsSelectedErrMsg}
    Run Keyword and Expect Error   ${expectedErrorMessage}  Fusion UI Edit Server Profile           @{TestData.F1407UI099.Edit}