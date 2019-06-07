*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Remove Scope And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1290_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Remove scope, check scope related in Server Hardware scope
    ${data}=    Get Data By Xpath    //hardwares/hardware[@for='Remove scope, check scope related in Server Hardware scope']
	Fusion UI Validate Scope Assigned To Server Hardware      @{data.hardware}