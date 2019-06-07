*** Settings ***
Resource    ./keywords.txt
Variables    ${DATA_FILE}

Suite Setup  Precondition Setup
Suite Teardown    Logout Appliance

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one

*** Keywords ***
Precondition Setup
    [Documentation]  Precondition Setup
    Set Log Level           TRACE
    Log    Logging in OneView appliance    console=True
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    ${resp}=  Fusion Api Get Current Security Mode
    Set Global Variable    ${SECURITY_MODE}  ${resp['modeName']}

Logout Appliance
    [Documentation]   Log out Appliance
    Log    Logging out OneView appliance    console=True
    Fusion Api Logout Appliance