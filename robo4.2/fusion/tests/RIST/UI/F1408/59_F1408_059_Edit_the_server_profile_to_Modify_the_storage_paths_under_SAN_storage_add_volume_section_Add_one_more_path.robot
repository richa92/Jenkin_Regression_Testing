*** Settings ***

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup          Load Test Data and Open Browser and Login
Test Teardown       Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1408/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Edit the server profile to Modify the storage paths under SAN storage --> add volume section Add one more path
    ${rc} =    Fusion Ui Create Server Profile     @{TestData.F1408P059.Create}
    Should Be True    ${rc}   msg=Failed to create the server profile
    ${rc} =    Fusion Ui Edit Server Profile     @{TestData.F1408P059.Edit}
    Should Be True    ${rc}   msg=Failed to Add one more path in the server profile
    Close Browser
    Open Browser  ${ApplianceUrl}  ${Browser}
    Maximize Browser Window
    Run Keyword If  "${Browser}" == "ie"   Go To  javascript:document.getElementById('overridelink').click()
    Set Selenium Speed  ${SeleniumSpeed}
    Log into Fusion appliance as Administrator
    ${rc} =    Fusion UI Verify Server Profile SAN Storage Info    @{TestData.F1408P059.Edit}
    Should Be True    ${rc}   msg=Failed to verify the private volume in the server profile
    ${rc} =    Fusion UI Verify Server Profile Connections Info    @{TestData.F1408P059.Edit}
    Should Be True    ${rc}   msg=Failed to verify the connections info in the server profile
