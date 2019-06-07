*** Settings ***
Resource    ../../API/Fusion_Env_Setup/keywords.txt
Variables   ./Regression_Data.py

Suite Setup  Setup ENV Before F1236 Test cases


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${admin_credentials}            ${TBirdEnvSetup.${Team_Name}.Common.admin_credentials}
${Ring}                         WPST22
${FTS}                          false
${Add_Storage}                  false
${Add_Enclosure}                true

*** Keywords ***
Setup ENV Before F1236 Test cases
    Set Log Level	TRACE
	Fusion Api Login Appliance 		                            ${APPLIANCE_IP}		            ${admin_credentials}
    Setup Env For C7000    ${Ring}  ${FTS}  ${Add_Enclosure}  ${Add_Storage}  ${Team_Name}
    Add Server Hardware Async   ${GEN8DLServer}
    Add Server Hardware Async   ${GEN9DLServer}
    Power off ALL servers   PressAndHold
    Wait For ALL Servers Complete Refresh
    Remove All Server Profiles