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
Assign Enclosure to part of scopes, check setting related
    Fusion UI Create Scope		@{TestData.empty_scopes}
    ${data}=    Get Data By Xpath    //enclosures/enclosure[@for='Create A/B/C scopes, with multiple enclosure, A with enclosure1enclsoure2, B with enclosure2enclosure3, C with enclosure3enclosure1, check enclosure status related']
	Fusion UI Edit Scope For Enclosure      @{data.enclosure}
    ${data}=    Get Data By Xpath    //scopes/scope[@for='Create A/B/C scopes, with multiple enclosure, A with enclosure1enclsoure2, B with enclosure2enclosure3, C with enclosure3enclosure1, check enclosure status related']
    Fusion UI Validate Resource Assigned To Scope		@{data.scope}