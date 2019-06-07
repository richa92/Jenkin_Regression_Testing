*** Settings ***
Resource    ./keyword.txt

Suite Setup  Precondition Setup


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one

*** Keywords ***
Precondition Setup
    [Documentation]  Precondition Setup
    Set Log Level           TRACE
