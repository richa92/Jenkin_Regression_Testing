*** Settings ***
Documentation        OVF688_OVS6749 Validate the Rest API to fetch and trust any server certificate
Resource    ./keyword.txt
Variables   ${DATA_FILE}

Suite Setup    Setup ENV Before OVF688_OVS6749 Test cases
Test Teardown  Remove All Directories Async

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one


*** Keywords ***
Setup ENV Before OVF688_OVS6749 Test cases
    [Documentation]   Precondition Setup
    Set Log Level   TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    ${resp}=  Fusion Api Get Current Security Mode
    Set Global Variable    ${SECURITY_MODE}  ${resp['modeName']}
