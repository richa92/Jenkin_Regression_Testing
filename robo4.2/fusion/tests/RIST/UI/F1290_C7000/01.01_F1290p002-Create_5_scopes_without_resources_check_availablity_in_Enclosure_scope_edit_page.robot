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
Create scopes without resources, check availablity in Enclosure scope edit page
    Fusion UI Delete Scope      @{TestData.empty_scopes}
	Fusion UI Create Scope		@{TestData.empty_scopes}
	Fusion UI Validate Scope Can Be Assigned To Enclosure      @{TestData.scope_enclosures}

