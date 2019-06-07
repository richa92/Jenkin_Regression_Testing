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
Update empty scopes resource, check availablity related in Enclosure scope
	Fusion UI Edit Scope		@{TestData.edit_enclsoure_scopes}
	Fusion UI Validate Scope Assigned To Enclosure      @{TestData.scope_enclosures}
