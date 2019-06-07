*** Settings ***
Resource    ./keywords.txt

Suite Setup  Precondition ENV Setup
Suite Teardown  Login Appliance and Revert ICM Power and UID Status

*** Variables ***
${APPLIANCE_IP}             ${None}         # leave it as ${None} if you want this test to create a new one
${ApplianceUrl}             https://${APPLIANCE_IP}
${DataFile}                 F316/Regression_data.xml

*** Keywords ***
Precondition ENV Setup
    Set Log Level       TRACE
    Load Test Data and Open Browser and Login
    Init ICM Power And UID Status

Login Appliance and Revert ICM Power and UID Status
    Load Test Data and Open Browser and Login
    Init ICM Power And UID Status

