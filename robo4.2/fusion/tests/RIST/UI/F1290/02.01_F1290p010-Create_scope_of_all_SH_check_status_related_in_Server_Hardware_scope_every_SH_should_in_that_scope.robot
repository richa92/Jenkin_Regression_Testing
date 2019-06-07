*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1290/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Create scope of all SH, check status related in Server Hardware scope, every SH should in that scope.
    Fusion UI Create Scope		@{TestData.create_hardware_scopes}
	Fusion UI Validate Scope Assigned To Server Hardware      @{TestData.scope_hardwares}