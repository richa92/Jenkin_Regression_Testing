*** Settings ***
Documentation   Validation of server profile creation when connection 1 is configured to Not bootable - Private volume & connection 2 is configured to Not bootable - Private Volume

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown	Clear Profile And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1408/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Validation of server profile creation when connection 1 is configured to Primary boot - Private volume & connection 2 is configured to Secondary boot - Private Volume
    ${expectedErrorMessage}=  catenate  ${nonConnectionIsConfigurededErrMsgPart1}    ${TestData.F1408UI022.Volname}    ${nonConnectionIsConfigurededErrMsgPart2}
    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToAddProfileErrMessage}    ${expectedErrorMessage}
    Run Keyword and Expect Error   ${expectedErrorMessage}  Fusion UI Create Server Profile     @{TestData.F1408UI022.Create}