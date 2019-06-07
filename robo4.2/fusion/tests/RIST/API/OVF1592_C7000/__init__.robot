*** Settings ***
Resource    ./keywords.txt
Variables   ./Regression_Data.py

Suite Setup  Precondition Setup

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one

*** Keywords ***
Precondition Setup
    [Documentation]  The precondition Setup
    Set Log Level           TRACE
    Fusion Api Login Appliance     ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
    Prepare Environment for Test