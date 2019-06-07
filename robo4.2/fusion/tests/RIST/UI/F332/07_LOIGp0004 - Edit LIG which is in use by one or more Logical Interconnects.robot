*** Settings ***
Resource        ../resource.txt

Test Setup      Load Test Data And Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}                 F332/Regression_data.xml  # Data File Location
${ApplianceUrl}             https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
LOIGp0004 - Edit LIG which is in use by one or more Logical Interconnects
    Log Into Fusion Appliance As Administrator

    ${expectedWarningMessage}=  catenate  SEPARATOR=  ${InconsistencyWarningMsgSummary}   ${InconsistencyWarningMsgDetailsPart1}
    ${expectedWarningMessage}=  catenate  ${expectedWarningMessage}    ${TestData.LOIGp0003.li}    ${InconsistencyWarningMsgDetailsPart2}

    Run Keyword and Expect Error  ${expectedWarningMessage}  Fusion Ui Validate Warning Message When Edit Logical Interconnect Group  @{TestData.LOIGp0003.ligs2}