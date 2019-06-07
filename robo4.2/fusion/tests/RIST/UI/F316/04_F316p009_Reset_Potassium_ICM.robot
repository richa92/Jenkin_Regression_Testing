*** Settings ***
Resource    ../resource.txt
Resource    ./keywords.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F316/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
Reset Potassium ICM
    ${rc}               Fusion Ui Interconnect Reset     @{TestData.Interconnect}
    should be true      ${rc}       msg=Failed to Reset Potassium Interconnect
