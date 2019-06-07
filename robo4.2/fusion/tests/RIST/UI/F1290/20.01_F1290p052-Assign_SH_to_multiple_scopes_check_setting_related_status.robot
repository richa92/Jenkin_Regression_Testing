*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Remove Scope And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1290/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Assign SH to multiple scopes, check setting related status
    Fusion UI Create Scope		@{TestData.empty_scopes}
    ${data}=    Get Data By Xpath    //hardwares/hardware[@for='Create A/B/C scopes, with multiple SH, A with bay1bay2, B with bay2bay3, C with bay3bay1, check SH status related']
	Fusion UI Edit Scope For Server Hardware      @{data.hardware}
    ${data}=    Get Data By Xpath    //scopes/scope[@for='Create A/B/C scopes, with multiple SH, A with bay1bay2, B with bay2bay3, C with bay3bay1, check SH status related']
    Fusion UI Validate Resource Assigned To Scope		@{data.scope}