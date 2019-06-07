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
Create A/B/C scopes, with multiple SH, A with bay1&bay2, B with bay2&bay3, C with bay3&bay1, remove resource, check SH status related
    ${data}=    Get Data By Xpath    //scopes/scope[@for='Create A/B/C scopes, with multiple SH, A with bay1bay2, B with bay2bay3, C with bay3bay1, remove resource, check SH status related']
    Fusion UI Edit Scope		@{data.scope}
	Fusion UI Validate Scope Assigned To Server Hardware      @{TestData.base_hardwares}