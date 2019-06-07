*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Resource    ./keywords.txt
Variables   ./Regression_Data.py

Suite Setup  Precondition ENV Setup
Suite Teardown  Clear Base Resources

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${admin_credentials}            ${C7000EnvSetup.${Team_Name}.Common.admin_credentials}
${Ring}                         WPST33
${FTS}                          false
${Add_Storage}                  false
${Add_Enclosure}                true


*** Keywords ***
Precondition ENV Setup
    Set Log Level       TRACE

