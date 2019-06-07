*** Settings ***
Resource    ../../API/Fusion_Env_Setup/keywords.txt
Resource    ./keyword.txt
Variables   ./Regression_Data.py

Suite Setup  Precondition Setup For F607
Suite Teardown  Clear Env For F607

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${admin_credentials}            ${TBirdEnvSetup.${Team_Name}.Common.admin_credentials}
${Ring}                         TBird13
${Add_LE}                       false
${Add_Storage}                  false

*** Keywords ***
Precondition Setup For F607
    Set Log Level	TRACE
    Log To Console And Logfile      \nRemove All LEs and EGs, then add an empty EG
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Remove All Firmware Bundles
    Wait For ALL Server Profile In Normal State
    Power off ALL servers   PressAndHold
    Wait For ALL Servers Complete Refresh
    Remove All Server Profiles
    Remove All Server Profile Templates
    Setup Env For TBird    ${Ring}  ${Add_LE}  ${Add_Storage}  ${Team_Name}
    Remove All LEs
    Remove All Enclosure Groups     True
	Run Keyword If	        ${EG} is not ${null}
	...                     Run Keyword And Ignore Error
	...                     Run Keyword for List                ${EG}
	...                     Add Enclosure Group from variable

Clear Env For F607
    Remove All Server Profile Templates
    Remove All Server Profiles
    Remove All LEs
    Remove All Enclosure Groups     True
    Remove All Firmware Bundles
