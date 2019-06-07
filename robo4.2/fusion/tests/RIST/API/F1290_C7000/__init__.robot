*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Variables   ./Regression_Data.py

Suite Setup  Precondition ENV Setup


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring}                         WPST22
${FTS}                          false
${Add_Storage}                  false
${Add_Enclosure}                true

*** Keywords ***
Precondition ENV Setup
    Set Log Level       TRACE
    Setup Env For C7000     ${Ring}     ${FTS}      ${Add_Enclosure}        ${Add_Storage}
