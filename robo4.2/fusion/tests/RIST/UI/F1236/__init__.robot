*** Settings ***
Resource    ../../API/Fusion_Env_Setup/keywords.txt

Suite Setup  Setup ENV Before F1236 Test cases


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${admin_credentials}            ${TBirdEnvSetup.${Team_Name}.Common.admin_credentials}
${Ring}                         TBird13
${Add_LE}                       true
${Add_Storage}                  false

*** Keywords ***
Setup ENV Before F1236 Test cases
    Set Log Level	TRACE
	Fusion Api Login Appliance 		                            ${APPLIANCE_IP}		            ${admin_credentials}
    Setup Env For TBird    ${Ring}  ${Add_LE}  ${Add_Storage}  ${Team_Name}
    Power off ALL servers   PressAndHold
    Wait For ALL Servers Complete Refresh
    Remove All Server Profiles