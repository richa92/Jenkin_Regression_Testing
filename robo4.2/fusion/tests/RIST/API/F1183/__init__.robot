*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Resource    ./keywords.txt
Resource    ../../../../Resources/api/fusion_api_resource.txt
Variables   ./Regression_Data.py

Suite Setup  Precondition Setup         ${Firmware_Bundles}
Suite Teardown  Clear Profile And Firmware Bundle

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring}                         WPST26
${FTS}                          false
${Add_Storage}                  false
${Add_Enclosure}                true
${UIDataFile}                   F1183/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Keywords ***
Precondition Setup
    [Documentation]  Prepare the enviromnet before test
    [Arguments]	            ${Firmware_Bundles}=${None}
    Set Log Level           TRACE
    ${resp}  ${sessionID}=  Fusion Api Login Appliance
    ...                     ${APPLIANCE_IP}         ${admin_credentials}
	Setup Env For C7000     ${Ring}     ${FTS}      ${Add_Enclosure}        ${Add_Storage}

	Wait For ALL Server Profile In Normal State
	Wait For ALL Servers Complete Refresh
	Remove All Server Profiles
	Remove All Firmware Bundles

    Upload Firmware Bundle By List    ${SPP_list}

Clear Profile And Firmware Bundle
    [Documentation]  Clear the enviromnet after test
    Clear Test Environtment
    Remove All Firmware Bundles