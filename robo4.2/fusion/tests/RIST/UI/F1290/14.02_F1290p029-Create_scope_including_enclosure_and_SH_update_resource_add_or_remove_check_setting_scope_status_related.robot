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
Create scope including enclosure and SH, update resource, add or remove, check setting scope status related
    Fusion UI Edit Scope		@{TestData.remove_enclsoure_hardware_scopes}
	Fusion UI Validate Scope Assigned To Enclosure      @{TestData.base_enclosures}
	Fusion UI Validate Scope Assigned To Server Hardware      @{TestData.base_hardwares}