*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1022/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Validate license addition does not impact server hardware
    ${ret} =  Fusion Ui Add FC Licenses      @{TestData.licenses}
    Should Be True  ${ret}  msg=Failed to add FC licenses
    ${ret} =  Fusion Ui Validate No License On Server Hardware      @{TestData.server_hardwares}
    Should Be True  ${ret}  msg=Failed to validate no license on server hardware