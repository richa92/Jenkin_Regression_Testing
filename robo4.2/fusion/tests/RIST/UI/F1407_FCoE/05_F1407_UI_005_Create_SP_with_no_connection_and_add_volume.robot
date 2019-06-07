*** Settings ***
Documentation   Create SP with no connections and add volumes

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
Create SP with no connections and add volumes
    ${expectedErrorMessage}=  catenate  ${nonStoragePathSpecifiedErrMsgPart1}   ${TestData.F1407UI005.Volname}
    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${reviewIndicatedWarningsErrMsg}    ${expectedErrorMessage}    ${nonStoragePathSpecifiedErrMsgPart2}
    Run Keyword and Expect Error   ${expectedErrorMessage}  Fusion UI Create Server Profile     @{TestData.F1407UI005.Create}
