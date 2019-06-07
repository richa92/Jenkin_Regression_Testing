*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Resource    ./OVF2_C7000.txt
Variables   ${DATA_FILE}

Suite Setup  Precondition ENV Setup

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring}                         WPST23
${FTS}                          false
${Add_Enclosure}                true

*** Keywords ***
Precondition ENV Setup
    [Documentation]    Prepare test environment for test
    Set Log Level       TRACE
    Setup Env For C7000     ${Ring}     ${FTS}      ${Add_Enclosure}
