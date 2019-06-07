*** Settings ***
Resource    ../../API/Fusion_Env_Setup/keywords.txt
Resource    ./keyword.txt

Suite Setup  Setup ENV Before F722 Test cases
Suite Teardown  Clear Profile And Firmware Bundle


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${admin_credentials}            ${TBirdEnvSetup.${Team_Name}.Common.admin_credentials}
${Ring}                         WPST32
${FTS}                          false
${Add_Storage}                  false
${Add_Enclosure}                true
${UIDataFile}                   F722_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}                 https://${APPLIANCE_IP}     # Appliance Url

*** Keywords ***
Setup ENV Before F722 Test cases
    Set Log Level           TRACE
    ${resp}  ${sessionID}=  Fusion Api Login Appliance
    ...                     ${APPLIANCE_IP}         ${admin_credentials}
	Setup Env For C7000     ${Ring}     ${FTS}      ${Add_Enclosure}        ${Add_Storage}

	Run Keyword And Ignore Error    Wait For ALL Server Profile In Normal State
	Run Keyword And Ignore Error    Wait For ALL Servers Complete Refresh
    Run Keyword And Ignore Error    Power off ALL servers   PressAndHold
	Run Keyword And Ignore Error    Remove All Server Profiles
	Run Keyword And Ignore Error    Remove All Firmware Bundles

Clear Profile And Firmware Bundle
    Clear Test Environtment
    Remove All Firmware Bundles