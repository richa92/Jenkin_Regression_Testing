*** Settings ***
Documentation   Create SP with managed LUN and with storage paths disabled

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown	Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_FCoE/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Create SP with managed LUN and with storage paths disabled
    ${expectedErrorMessage}=  catenate    ${StoragePathIsDisabledErrMsgPart1}    ${TestData.F221UI026.Volname}   ${StoragePathIsDisabledErrMsgPart2}
    ${expectedErrorMessage}=  catenate  SEPARATOR=  ${unableToAddProfileErrMessage}    ${expectedErrorMessage}
    Run Keyword and Expect Error   ${expectedErrorMessage}  Fusion UI Create Server Profile     @{TestData.F221UI026.Create}