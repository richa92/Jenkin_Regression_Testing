*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Resource    ./keywords.txt
Variables   ./Regression_Data.py


Suite Setup  Precondition Setup
Suite Teardown  Clear Profile And Firmware Bundle


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring}                         TBird13
${Add_LE}                       true
${Add_Storage}                  false
${Add_Enclosure}                true

*** Keywords ***
Precondition Setup
    [Documentation]   Precondition Setup
    Set Log Level           TRACE
    ${resp}  ${sessionID}=  Fusion Api Login Appliance
    ...                     ${APPLIANCE_IP}         ${admin_credentials}
    Reset iLO and Update Server ILO Firmware      ${Gen10SYServerFW}

    Setup Env For TBird     ${Ring}     ${Add_LE}      ${Add_Storage}

    Run Keyword And Ignore Error    Wait For ALL Server Profile In Normal State
    Run Keyword And Ignore Error    Wait For ALL Servers Complete Refresh
    Run Keyword And Ignore Error    Power off ALL servers   PressAndHold
    Run Keyword And Ignore Error    Remove All Server Profiles
    Run Keyword And Ignore Error    Remove All Firmware Bundles

    Run Keyword If  '${fw_bundle_lower}' != '${False}'
    ...        Upload Firmware Bundle By Curl    fw_absolute_path=${fw_bundle_lower}
    ...        ELSE  fail  msg=Upload firmware failed, please check
    Run Keyword If  '${fw_bundle_higher}' != '${False}'
    ...        Upload Firmware Bundle By Curl    fw_absolute_path=${fw_bundle_higher}
    ...        ELSE  fail  msg=Upload firmware failed, please check
#    Run Keyword If  '${fw_bundle}' != '${False}'
#    ...        Upload Firmware Bundle By Curl    fw_absolute_path=${fw_bundle}
#    ...        ELSE  fail  msg=Upload firmware failed, please check

Clear Profile And Firmware Bundle
    [Documentation]   Clear Profile And Firmware Bundle
    Run Keyword And Ignore Error    Clear Test Environtment
    Run Keyword And Ignore Error    Remove All Server Profiles
    Run Keyword And Ignore Error    Remove All Firmware Bundles
