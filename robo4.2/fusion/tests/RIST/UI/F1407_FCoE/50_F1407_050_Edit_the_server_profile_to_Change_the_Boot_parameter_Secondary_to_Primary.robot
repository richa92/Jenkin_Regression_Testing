*** Settings ***

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup          Load Test Data and Open Browser and Login
Test Teardown       Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FCoE/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Edit the server profile to Change the Boot parameter - Secondary to Primary
    ${rc} =    Fusion Ui Create Server Profile     @{TestData.F1407P050.Create}
    Should Be True    ${rc}   msg=Failed to create the server profile
    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToEditProfileErrMessage}   ${multipleIscsiPrimaryBootErrMsg}
    Run Keyword and Expect Error   ${expectedErrorMessage}    Fusion Ui Edit Server Profile     @{TestData.F1407P050.Edit}
