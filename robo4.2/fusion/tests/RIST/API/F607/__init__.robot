*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Resource    ./keywords.txt
Variables   ./Regression_Data.py
Resource    ../../UI/resource.txt

Suite Setup  Precondition Setup
Suite Teardown  Clear Profile And Firmware Bundle


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring}                         TBird13
${Add_LE}                       false
${Add_Storage}                  false
${UIDataFile}                   F607/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Keywords ***
Precondition Setup
    Set Log Level           TRACE
    ${resp}  ${sessionID}=  Fusion Api Login Appliance
    ...                     ${APPLIANCE_IP}         ${admin_credentials}
	Setup Env For TBird     ${Ring}  ${Add_LE}      ${Add_Storage}          ${Team_Name}
	Run Keyword And Ignore Error    Wait For ALL Server Profile In Normal State
	Run Keyword And Ignore Error    Wait For ALL Servers Complete Refresh
    Run Keyword And Ignore Error    Power off ALL servers   PressAndHold
	Run Keyword And Ignore Error    Remove All Server Profiles
	Run Keyword And Ignore Error    Remove All Firmware Bundles
	Run Keyword And Ignore Error    Wait For ALL Enclosures In OK Status
    Run Keyword And Ignore Error    Remove All LEs
    Remove All Enclosure Groups     True
	Run Keyword If	        ${EG} is not ${null}
	...                     Run Keyword And Ignore Error
	...                     Run Keyword for List                ${EG}
	...                     Add Enclosure Group from variable




Clear Profile And Firmware Bundle
    Clear Test Environtment
    Clear Base Resources
