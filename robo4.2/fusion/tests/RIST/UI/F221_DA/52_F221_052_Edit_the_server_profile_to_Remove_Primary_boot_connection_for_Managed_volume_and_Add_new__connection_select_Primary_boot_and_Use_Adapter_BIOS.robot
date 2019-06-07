*** Settings ***

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup          Load Test Data and Open Browser and Login
Test Teardown       Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F221_DA/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url
${Volname}          F221_VOL_DA_1_Private


*** Test Cases ***
Edit the server profile to Remove Primary boot connection for Managed volume and Add new connection, select Primary boot and Use Adapter BIOS
    ${rc} =    Fusion Ui Create Server Profile     @{TestData.F221P052.Create}
    Should Be True    ${rc}   msg=Failed to create the server profile
    ${expectedErrorMessage}=  catenate  ${nonConnectionIsConfigurededErrMsgPart1}   ${TestData.F221P058.Volname}    ${nonConnectionIsConfigurededErrMsgPart2}
    ${expectedErrorMessage}=  catenate  SEPARATOR=    ${unableToEditProfileErrMessage}   ${expectedErrorMessage}
    Run Keyword and Expect Error   ${expectedErrorMessage}    Fusion Ui Edit Server Profile     @{TestData.F221P052.Edit}
