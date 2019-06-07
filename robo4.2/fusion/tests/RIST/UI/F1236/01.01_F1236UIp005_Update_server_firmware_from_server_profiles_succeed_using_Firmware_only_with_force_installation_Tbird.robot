*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser Then Login
Test Teardown   Remove Profiles and Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F1236/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F1236UIp005  Update server firmware from server profiles succeed using “Firmware only” with force installation Tbird
    ${rc} =   Fusion UI Create Server Profile      @{TestData.RBForceProfile}
    Should Be True                      ${rc}   msg=Some server profile cannot be created

