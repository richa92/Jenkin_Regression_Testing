*** Settings ***
Resource    ../../API/Fusion_Env_Setup/keywords.txt

Suite Setup  Setup ENV Before F1290 Test cases


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring}                         WPST22
${FTS}                          false
${Add_Storage}                  false
${Add_Enclosure}                true
${TEST_NAME}                    F1290 Scope Test

*** Keywords ***
Setup ENV Before F1290 Test cases
    Set Log Level	TRACE
    Setup Env For C7000             WPST22   ${FTS}      ${Add_Enclosure}      ${Add_Storage}      ${Team_Name}
    Setup Env For C7000             WPST23   ${FTS}      ${Add_Enclosure}      ${Add_Storage}      ${Team_Name}
    Setup Env For C7000             WPST26   ${FTS}      ${Add_Enclosure}      ${Add_Storage}      ${Team_Name}
