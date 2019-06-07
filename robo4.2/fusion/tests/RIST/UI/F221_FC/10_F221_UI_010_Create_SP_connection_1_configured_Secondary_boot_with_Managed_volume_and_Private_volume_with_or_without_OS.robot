*** Settings ***
Documentation  Validation of server profile creation when connection 1 is configured to Secondary boot - with Managed volume - Private Volume with/without OS.

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_FC/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Validation of server profile creation when connection 1 is configured to Secondary boot - with Managed volume - Private Volume with/without OS.
    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToAddProfileErrMessage}   ${onlyIscsiSecondaryBootErrMsg}
    Run Keyword and Expect Error   ${expectedErrorMessage}  Fusion UI Create Server Profile     @{TestData.F221UI010.Create}