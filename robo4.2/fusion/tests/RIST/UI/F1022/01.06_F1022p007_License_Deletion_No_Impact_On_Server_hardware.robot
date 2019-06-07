*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1022/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}


*** Test Cases ***
Validate license deletion does not impact server hardware
    Clean Uplink Sets In LIG     ${TestData.ligs[0].name}
    fusion ui update logical interconnect from group   @{TestData.li}
    CLear Environment    ${TestData}
    ${ret} =  Fusion Ui Validate No Fc License
    Should Be True  ${ret}  msg=Failed to validate no fc license
    ${ret} =  Fusion Ui Validate No License On Server Hardware      @{TestData.server_hardwares}
    Should Be True  ${ret}  msg=Failed to validate no license on server hardware