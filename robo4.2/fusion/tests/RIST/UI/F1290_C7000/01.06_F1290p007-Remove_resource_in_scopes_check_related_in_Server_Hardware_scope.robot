*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1290_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Remove resource in scopes, check related in Server Hardware scope
    ${data}=    Get Data By Xpath    //scopes/scope[@for='Remove resource in scopes, check related in Server Hardware scope']
    Fusion UI Edit Scope		@{data.scope}
    ${data}=    Get Data By Xpath    //hardwares/hardware[@for='Remove resource in scopes, check related in Server Hardware scope']
    Fusion UI Validate Scope Assigned To Server Hardware      @{data.hardware}
