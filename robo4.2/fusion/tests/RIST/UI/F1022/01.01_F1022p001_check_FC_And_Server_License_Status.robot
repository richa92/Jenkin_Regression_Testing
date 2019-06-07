*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1022/Regression_data.xml  # Data File Location
${ApplianceUrl}    https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Validate the License available is None and Add option is available in license
    Clean Uplink Sets In LIG     ${TestData.ligs[0].name}
    fusion ui update logical interconnect from group   @{TestData.li}
    CLear Environment    ${TestData}
    ${ret} =  Fusion Ui Validate No FC License
    Should Be True  ${ret}  msg=Failed to validate no FC license
    ${ret} =  Fusion Ui Validate Add Button Exists On License Page
    Should Be True  ${ret}  msg=Failed to validate add button exists on license page
    ${ret} =  Fusion Ui Validate No License On Server Hardware      @{TestData.server_hardwares}
    Should Be True  ${ret}  msg=Failed to validate no license on server hardware
