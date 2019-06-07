*** Settings ***
Resource    ../../API/Fusion_Env_Setup/keywords.txt

Suite Setup  Setup ENV Before F1183 Test cases
Suite Teardown  Remove All Firmware Bundles

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${admin_credentials}            ${TBirdEnvSetup.${Team_Name}.Common.admin_credentials}
${Ring}                         WPST26
${FTS}                          false
${Add_Storage}                  false
${Add_Enclosure}                true

*** Keywords ***
Setup ENV Before F1183 Test cases
    Set Log Level           TRACE
    ${resp}  ${sessionID}=  Fusion Api Login Appliance
    ...                     ${APPLIANCE_IP}         ${admin_credentials}
	Setup Env For C7000     ${Ring}     ${FTS}      ${Add_Enclosure}        ${Add_Storage}
	Wait For ALL Server Profile In Normal State
	Wait For ALL Servers Complete Refresh
	Power off ALL servers   PressAndHold
	Remove All Server Profiles
	Remove All Firmware Bundles


