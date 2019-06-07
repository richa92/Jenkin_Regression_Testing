*** Settings ***
Resource    ../../API/Fusion_Env_Setup/keywords.txt
Resource    ./keyword.txt
Resource    ../../UI/resource.txt
Variables   ./Regression_Data.py

Suite Setup  Precondition Setup
Suite Teardown  Clear Environtment And Firmware Bundle


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring26}                       WPST26
${Ring32}                       WPST32
${DataFile}                   OVF549_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}                 https://${APPLIANCE_IP}     # Appliance Url


*** Keywords ***
Precondition Setup
    Set Log Level           TRACE
    ${resp}  ${sessionID}=  Fusion Api Login Appliance
    ...                     ${APPLIANCE_IP}         ${admin_credentials}

	Run Keyword And Ignore Error    Wait For ALL Server Profile In Normal State
	Run Keyword And Ignore Error    Wait For ALL Servers Complete Refresh
    Run Keyword And Ignore Error    Power off ALL servers   PressAndHold
	Run Keyword And Ignore Error    Remove All Server Profiles
	Run Keyword And Ignore Error    Remove All Server Profile Templates
	Run Keyword And Ignore Error    Remove All Enclosures
	Run Keyword And Ignore Error    Remove All DL Server Hardware Async
	Run Keyword And Ignore Error    Remove All Firmware Bundles

    Setup Env For C7000     ${Ring32}

	Load Test Data and Open Browser
    Log into Fusion appliance as Administrator
    Fusion UI Add Latest Firmware Bundle    @{TestData.spps}

Clear Environtment And Firmware Bundle
    ${resp}  ${sessionID}=  Fusion Api Login Appliance
    ...                     ${APPLIANCE_IP}         ${admin_credentials}
    Run Keyword And Ignore Error       Remove All Enclosures    param=?force=true
    Run Keyword And Ignore Error       Remove All DL Server Hardware Async     ServerTypes=DL
    Run Keyword And Ignore Error       Remove All Firmware Bundles
