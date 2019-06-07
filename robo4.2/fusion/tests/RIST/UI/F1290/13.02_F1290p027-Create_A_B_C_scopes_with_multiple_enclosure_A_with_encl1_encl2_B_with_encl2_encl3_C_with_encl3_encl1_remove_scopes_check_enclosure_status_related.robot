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
Create A/B/C scopes, with multiple enclosure, A with enclosure1&enclsoure2, B with enclosure2&enclosure3, C with enclosure3&enclosure1, remove scopes, check enclosure status related
    Fusion UI Delete Scope      @{TestData.create_enclsoure_scopes}
	Fusion UI Validate Scope Assigned To Enclosure      @{TestData.base_enclosures}