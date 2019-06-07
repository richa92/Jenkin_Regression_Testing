*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Resource    ./keyword.txt
Resource    ../../UI/resource.txt
Variables   ./Regression_Data.py

Suite Setup  Precondition Setup
Suite Teardown  Clear Firmware Bundle


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring26}                       WPST26
${Ring32}                       WPST32
${FTS}                          false
${Add_Enclosure}                true


*** Keywords ***
Precondition Setup
    [Documentation]   Precondition Setup
    Set Log Level           TRACE
    ${resp}  ${sessionID}=  Fusion Api Login Appliance
    ...                     ${APPLIANCE_IP}         ${admin_credentials}
    Setup Env For C7000     ${Ring32}    ${FTS}    ${Add_Enclosure}

    Run Keyword And Ignore Error    Wait For ALL Server Profile In Normal State
    Run Keyword And Ignore Error    Wait For ALL Servers Complete Refresh
    Run Keyword And Ignore Error    Power off ALL servers   PressAndHold
    Run Keyword And Ignore Error    Remove All Server Profiles
    Run Keyword And Ignore Error    Remove All Server Profile Templates
    Run Keyword And Ignore Error    Remove All DL Server Hardware Async     ServerTypes=DL
    Run Keyword And Ignore Error    Remove All Firmware Bundles

    Run Keyword If  '${fw_bundle}' != '${False}'
    ...        Upload Firmware Bundle By Curl    fw_absolute_path=${fw_bundle}
    ...        ELSE  fail  msg=Upload firmware failed, please check

Clear Firmware Bundle
    [Documentation]  Clear ENV after test completed
    Run Keyword And Ignore Error    Wait For ALL Enclosures Complete Refresh
    Run Keyword And Ignore Error    Remove All Hardwares
    Run Keyword And Ignore Error    Remove All Firmware Bundles
