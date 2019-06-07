*** Settings ***
Documentation   Validation of server profile creation when connection 1 is configured to Primary boot - with Managed volume - Private volume - enable boot option

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown	Clear Profile And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FC/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Create SP with connection 1 is configured to Primary boot - with Managed volume - Private volume - enable boot option
    ${expectedErrorMessage}=  catenate        ${nonConnectionIsConfigurededErrMsgPart1}    ${TestData.F1407UI019.Volname}    ${nonConnectionIsConfigurededErrMsgPart2}
    ${expectedErrorMessage}=  catenate  SEPARATOR=   ${unableToAddProfileErrMessage}    ${expectedErrorMessage}
    Run Keyword and Expect Error   ${expectedErrorMessage}  Fusion UI Create Server Profile     @{TestData.F1407UI019.Create}