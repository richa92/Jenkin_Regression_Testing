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
Filter from enclosure resource, check result
    ${data}=    Get Data By Xpath    //scopes/scope[@for='Assign Enclosure to A scope, update A scope item, remove scope item enclosure, check setting related status, filter']
    Fusion UI Validate Resource Assigned To Scope		@{data.scope}