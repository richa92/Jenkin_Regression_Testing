*** Settings ***
Documentation   Edit SP with Port parameter from Auto to None
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
Edit SP with Port parameter from Auto to None
    ${rc}                               Fusion UI Create Server Profile                             @{TestData.F221UI100.Create}
    Should Be True                      ${rc}   msg=Failed to Create Server Profile with Port parameter - auto

    ${expectedErrorMessage}=  catenate   ${nonConnectionIsConfigurededErrMsgPart1}  ${TestData.F221UI100.Volname}   ${nonConnectionIsConfigurededErrMsgPart3}
    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToEditProfileErrMessage}    ${expectedErrorMessage}
    Run Keyword and Expect Error   ${expectedErrorMessage}  Fusion UI Edit Server Profile             @{TestData.F221UI100.Edit}