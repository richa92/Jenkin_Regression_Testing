*** Settings ***
Resource             ./keywords.txt
Variables            ./Regression_Data.py

Suite Setup  Setup ENV Before OVF442 Test cases

Suite Teardown  Enable SSH Access On Applaince

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one

*** Keywords ***
Setup ENV Before OVF442 Test cases
    [Documentation]   Setup ENV Before OVF442 Test cases
    Set Log Level	TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    Edit Ssh Access    ${enable_ssh_body}

Enable SSH Access On Applaince
    [Documentation]   Set ssh access to enable before testing
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    Edit Ssh Access    ${enable_ssh_body}
    Fusion Api Logout Appliance