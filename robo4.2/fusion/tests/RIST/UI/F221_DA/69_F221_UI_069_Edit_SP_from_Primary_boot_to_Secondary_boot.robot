*** Settings ***
Documentation   Edit a Server Profile from Primary boot to Secondary boot

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_DA/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Edit SP from Primary boot to Secondary boot
    ${rc}                               Fusion UI Create Server Profile                 @{TestData.F221UI069.Create}
    Should Be True                      ${rc}   msg=Failed to create SP - Primary boot - Use Adapter BIOS

    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToEditProfileErrMessage}     ${onlyIscsiSecondaryBootErrMsg}
    Run Keyword and Expect Error   ${expectedErrorMessage}  Fusion UI Edit Server Profile     @{TestData.F221UI069.Edit}
