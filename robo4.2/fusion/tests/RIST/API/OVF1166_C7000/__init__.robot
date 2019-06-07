*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Resource    ./OVF1166_C7000.txt
Variables   ${DATA_FILE}

Suite Setup      Precondition ENV Setup
Suite Teardown   After Test

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring}                         WPST23
${FTS}                          false
${Add_Storage}                  true
${Add_Enclosure}                true


*** Keywords ***
Precondition ENV Setup
    [Documentation]     Environment Setup Pre Test
    Set Log Level       TRACE
    Setup Env For C7000     ${Ring}     ${FTS}      ${Add_Enclosure}        ${Add_Storage}
	