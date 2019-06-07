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
Edit the server profile to Add one more connection, select Primary boot and Use Adapter BIOS
    ${rc} =    Fusion Ui Create Server Profile     @{TestData.F221P051.Create}
    Should Be True    ${rc}   msg=Failed to create the server profile
    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToEditProfileErrMessage}   ${multipleIscsiPrimaryBootErrMsg}
    Run Keyword and Expect Error   ${expectedErrorMessage}    Fusion Ui Edit Server Profile     @{TestData.F221P051.Edit}
