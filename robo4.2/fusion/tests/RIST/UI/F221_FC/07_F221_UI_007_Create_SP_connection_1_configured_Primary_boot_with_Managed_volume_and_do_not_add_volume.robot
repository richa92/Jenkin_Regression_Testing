*** Settings ***
Documentation   Validation of  server profile creation when connection 1 is configured to Primary boot - with Managed volume - Do not add volume

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown	Clear Profile And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_FC/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Create SP with connection 1 is configured to Primary boot - with Managed volume - Do not add volume
    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToAddProfileErrMessage}   ${nonManagedVolumeIsSelectedErrMsg}
    Run Keyword and Expect Error   ${expectedErrorMessage}  Fusion UI create Server Profile     @{TestData.F221UI007.Create}