*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Resource    ./OVF1166.txt
Variables   ${DATA_FILE}

Suite Setup      Precondition ENV Setup
Suite Teardown   After Test

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring}                         TBird15
${Add_LE}                       true
${Add_Storage}                  true
${Add_Existing_Storage}         false

*** Keywords ***
Precondition ENV Setup
    [Documentation]     Environment Setup Pre Test
    Set Log Level       TRACE
    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Setup Env For TBird    ${Ring}  ${Add_LE}  ${Add_Storage}  ${Team_Name}  ${Add_Existing_Storage}