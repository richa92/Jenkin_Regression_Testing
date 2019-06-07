*** Settings ***

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup          Load Test Data and Open Browser and Login
Test Teardown       Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1408/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Edit the server profile to Unselect "Manage SAN Storage" in SAN storage section
    ${rc} =    Fusion Ui Create Server Profile     @{TestData.F1408P056.Create}
    Should Be True    ${rc}   msg=Failed to create the server profile
    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToEditProfileErrMessage}   ${nonManagedVolumeIsSelectedErrMsg}
    Run Keyword and Expect Error   ${expectedErrorMessage}    Fusion Ui Edit Server Profile     @{TestData.F1408P056.Edit}