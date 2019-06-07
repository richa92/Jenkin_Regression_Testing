*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Variables   ./Regression_Data.py

Suite Setup  Precondition ENV Setup


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${admin_credentials}            ${TBirdEnvSetup.${Team_Name}.Common.admin_credentials}
${Ring}                         TBird14
${Add_LE}                       true
${Add_Storage}                  false


*** Keywords ***
Precondition ENV Setup
    Set Log Level       TRACE

