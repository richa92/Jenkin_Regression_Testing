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
Assign SH to A scope, check setting related status
    Fusion UI Create Scope      @{TestData.remove_scopes}
    ${data}=    Get Data By Xpath    //hardwares/hardware[@for='Assign SH to A scope, check setting related status']
	Fusion UI Edit Scope For Server Hardware      @{data.hardware}
    ${data}=    Get Data By Xpath    //scopes/scope[@for='Assign SH to A scope, check setting related status']
    Fusion UI Validate Resource Assigned To Scope		@{data.scope}