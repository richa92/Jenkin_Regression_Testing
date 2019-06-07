*** Settings ***
Documentation   Validation of  server profile creation when connection 1 is configured to Not bootable - with Managed volume - Private volume - enable boot option

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
Create SP with connection 1 is configured to Not bootable - with Managed volume - Private volume - enable boot option
    ${expectedErrorMessage}=  catenate        ${nonConnectionIsConfigurededErrMsgPart1}    ${TestData.F221UI014.Volname}    ${nonConnectionIsConfigurededErrMsgPart2}
    ${expectedErrorMessage}=  catenate  SEPARATOR=   ${unableToAddProfileErrMessage}    ${expectedErrorMessage}
    Run Keyword and Expect Error   ${expectedErrorMessage}  Fusion UI Create Server Profile     @{TestData.F221UI014.Create}