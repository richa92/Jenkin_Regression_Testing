*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser Then Login
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F607/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F607UIp009 Error message shown and indicate power off listed servers if SH power on

    Fusion ui Power on all Servers

    ${expectedErrorMessage1}=  catenate    ${ServersarePoweronErrMsgPart1}  ${TestData.SHS.servername}  ${ServersarePoweronErrMsgPart2}
    ${expectedErrorMessage}=  catenate     SEPARATOR=  ${UnabletoUpdateFirmware}  ${expectedErrorMessage1}  ${UpdatefirmwareResolution}
    Run Keyword and Expect Error   ${expectedErrorMessage}  Fusion Ui Logical Enclosure Firmware Update    @{TestData.editsnap6LEParallel}
    ${rc}=   Fusion Ui Delete Logical Enclosure      @{TestData.nosetLE}
    Should Be True                      ${rc}   msg=Remove logical enclosure failed, error message:${rc}
