*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Remove Scope And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1290_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Filter from SH resource, check result
    ${data}=    Get Data By Xpath    //scopes/scope[@for='Assign SH to A scope, update A scope item, remove item SH, check setting related status, filter']
    Fusion UI Validate Resource Assigned To Scope		@{data.scope}