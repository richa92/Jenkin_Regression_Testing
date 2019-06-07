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
check Potassium ICM UID power on/off
    ${rc}               Fusion Ui Turn On Interconnect UID     @{TestData.Interconnect}
    sleep   20s
    should be true      ${rc}==True    msg=Failed to power on UID Potassium Interconnect
    ${rc}               Fusion Ui Turn Off Interconnect UID     @{TestData.Interconnect}
    sleep   20s
    should be true      ${rc}==True     msg=Failed to power off UID Potassium Interconnect


