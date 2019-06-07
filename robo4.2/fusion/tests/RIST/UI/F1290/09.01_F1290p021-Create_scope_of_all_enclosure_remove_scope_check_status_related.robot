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
Create scope of all enclosure, remove scope, check status related.
    Fusion UI Create Scope		@{TestData.create_enclsoure_scopes}
    Fusion UI Delete Scope		@{TestData.remove_scopes}
    ${data}=    Get Data By Xpath    //enclosures/enclosure[@for='Remove scope, check scope related in Enclosure scope']
	Fusion UI Validate Scope Assigned To Enclosure      @{data.enclosure}