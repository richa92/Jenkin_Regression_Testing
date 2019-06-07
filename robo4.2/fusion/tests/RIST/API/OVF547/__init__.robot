*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Resource    ./keyword.txt
Variables   ./Regression_Data.py

Suite Setup  Precondition Setup
Suite Teardown  Clear Profile And Firmware Bundle

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring}                         WPST32
${FTS}                          false
${Add_Storage}                  false
${Add_Enclosure}                true

*** Keywords ***
Precondition Setup
    [Documentation]    Precondition Setup
    Set Log Level           TRACE
    ${resp}  ${sessionID}=  Fusion Api Login Appliance
    ...                     ${APPLIANCE_IP}         ${admin_credentials}

	Run Keyword And Ignore Error    Wait For ALL Server Profile In Normal State
	Run Keyword And Ignore Error    Wait For ALL Servers Complete Refresh
    Run Keyword And Ignore Error    Power off ALL servers   PressAndHold
	Run Keyword And Ignore Error    Remove All Server Profiles
	Run Keyword And Ignore Error    Remove All Server Profile Templates
	Run Keyword And Ignore Error    Remove All Enclosures
	Run Keyword And Ignore Error    Remove All DL Server Hardware Async     ServerTypes=DL
	Run Keyword And Ignore Error    Remove All Repositories
	Run Keyword And Ignore Error    Remove All Firmware Bundles

	Setup Env For C7000     ${Ring}     ${FTS}      ${Add_Enclosure}        ${Add_Storage}

Clear Profile And Firmware Bundle
    [Documentation]    Clear Profile And Firmware Bundle
    Remove All Hardwares
    Run Keyword And Ignore Error    Remove All Firmware Bundles
