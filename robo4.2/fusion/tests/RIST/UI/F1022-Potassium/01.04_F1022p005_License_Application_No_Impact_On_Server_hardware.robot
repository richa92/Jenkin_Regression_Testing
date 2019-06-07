*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1022-Potassium/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Validate license applicationn does not impact server hardware
    Log To Console  ${TestData.potash[0].potash}
    Run Keyword If  ${TestData.potash[0].potash}      fusion ui create fc network      @{TestData.fc_networks}
    Run Keyword If  ${TestData.potash[0].potash}      fusion ui edit logical interconnect group tbird    @{TestData.ligs}
    Run Keyword If  ${TestData.potash[0].potash}      fusion ui update logical interconnect from group   @{TestData.li}
    Run Keyword Unless  ${TestData.potash[0].potash}  fusion ui edit potassium interconnect bay licensing    @{TestData.license_intents}
    Run Keyword Unless  ${TestData.potash[0].potash}  fusion ui validate potassium interconnect bay licensing    @{TestData.license_intents}
    ${ret} =  Fusion Ui Verify Licensed Fcupgrade Interconnects     ${TestData.license_type[0].number}
    Should Be True  ${ret}  msg=Failed to verify licensed fcupgrade interconnects
    ${ret} =   Fusion Ui Validate No License On Server Hardware      @{TestData.server_hardwares}
    Should Be True  ${ret}  msg=Failed to validate no license on server hardware

