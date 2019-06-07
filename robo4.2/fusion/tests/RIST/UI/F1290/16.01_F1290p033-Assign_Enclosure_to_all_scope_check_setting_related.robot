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
Assign Enclosure to all scope, check setting related
    Fusion UI Create Scope		@{TestData.empty_scopes}
    Fusion UI Edit Scope For Enclosure		@{TestData.scope_enclosures}
    Fusion UI Validate Resource Assigned To Scope		@{TestData.create_enclsoure_scopes}