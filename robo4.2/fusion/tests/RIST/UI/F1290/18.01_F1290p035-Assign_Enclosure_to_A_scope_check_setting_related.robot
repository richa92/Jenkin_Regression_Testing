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
Assign Enclosure to A scope, check setting related
    Fusion UI Create Scope      @{TestData.remove_scopes}
    ${data}=    Get Data By Xpath    //enclosures/enclosure[@for='Assign Enclosure to A scope, check setting related']
	Fusion UI Edit Scope For Enclosure      @{data.enclosure}
    ${data}=    Get Data By Xpath    //scopes/scope[@for='Assign Enclosure to A scope, check setting related']
    Fusion UI Validate Resource Assigned To Scope		@{data.scope}
