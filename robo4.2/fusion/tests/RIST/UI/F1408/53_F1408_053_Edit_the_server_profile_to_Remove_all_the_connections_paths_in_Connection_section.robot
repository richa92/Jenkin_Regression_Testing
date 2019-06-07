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
${Volname}          F1408_VOL_FC_1_Private


*** Test Cases ***
Edit the server profile to Remove all the connections paths in Connection section
    ${rc} =    Fusion Ui Create Server Profile     @{TestData.F1408P053.Create}
    Should Be True    ${rc}   msg=Failed to create the server profile
    ${expectedErrorMessage}=  catenate  ${nonConnectionIsConfigurededErrMsgPart1}   ${TestData.F1408P058.Volname}    ${nonConnectionIsConfigurededErrMsgPart2}
    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToEditProfileErrMessage}   ${expectedErrorMessage}
    Run Keyword and Expect Error   ${expectedErrorMessage}    Fusion Ui Edit Server Profile     @{TestData.F1408P053.Edit}