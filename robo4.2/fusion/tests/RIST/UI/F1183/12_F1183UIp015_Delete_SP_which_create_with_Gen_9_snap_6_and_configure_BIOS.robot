*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser Then Login
Test Teardown   Remove Profiles and Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F1183/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F1183UIp015 Delete SP which create with Gen 9 snap 6 and configure BIOS
    ${Result} =  Fusion UI Create Server Profile      @{TestData.F1183p015.create}
    should be true   ${Result}   msg=Failed to create Server Profile
    ${Result} =  Fusion UI Delete Server Profile  @{TestData.F1183p015.Delete}
    should be true   ${Result}  msg=Failed to delete Server Profile
