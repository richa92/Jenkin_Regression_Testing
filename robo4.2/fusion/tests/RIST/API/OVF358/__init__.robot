*** Settings ***
Documentation    OVF358 test
Resource    ../Fusion_Env_Setup/keywords.txt
Resource    ./keyword.txt
Variables   ./Regression_Data.py

Suite Setup  Precondition Setup

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one

*** Keywords ***
Precondition Setup
    [Documentation]   Precondition Setup
    Set Log Level           TRACE
