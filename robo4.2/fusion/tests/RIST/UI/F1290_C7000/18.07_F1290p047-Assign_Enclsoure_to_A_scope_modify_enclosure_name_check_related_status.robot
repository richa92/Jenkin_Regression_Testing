*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Reset Enclosure Name Remove Scope And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1290_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Assign Enclsoure to A scope, modify enclosure name, check related status
    ${data}=    Get Data By Xpath    //enclosures/enclosure[@for='Assign Enclsoure to A scope, do enclosure refresh, check related status']
    Fusion UI Edit Enclosure		@{data.enclosure}
    ${data}=    Get Data By Xpath    //scopes/scope[@for='Assign Enclsoure to A scope, modify enclosure name, check related status']
    Fusion UI Validate Resource Assigned To Scope		@{data.scope}
