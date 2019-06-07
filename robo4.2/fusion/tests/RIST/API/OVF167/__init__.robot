*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Variables   ${DATA_FILE}
Resource    ./OVF167.txt

Suite Setup  Precondition ENV Setup


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring}                         TBird15


*** Keywords ***
Precondition ENV Setup
    [Documentation]    Prepare test environment before test
    Set Log Level       TRACE
    Fusion Api Login Appliance      ${APPLIANCE_IP}    ${admin_credentials}
    Setup Env For TBird    ${Ring}
