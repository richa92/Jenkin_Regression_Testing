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
Update empty scopes, check availablity in Server Hardware scope
	Fusion UI Edit Scope		@{TestData.edit_hardware_scopes}
	Fusion UI Validate Scope Assigned To Server Hardware      @{TestData.scope_hardwares}