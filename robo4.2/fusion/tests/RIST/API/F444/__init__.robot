*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Resource    ./keywords.txt
Variables   ${DATA_FILE}

Suite Setup  Precondition ENV Setup For F444
Suite Teardown    Clear Test Environment
*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${admin_credentials}            ${C7000EnvSetup.${Team_Name}.Common.admin_credentials}
${Ring}                         WPST23A
${FTS}                          false
${Add_Storage}                  false
${Add_Enclosure}                true
${Ssh_User}                     root
${Ssh_Password}                 hpvse1



*** Keywords ***
Precondition ENV Setup For F444
    [Documentation]   Precondition ENV Setup For F444
    Set Log Level       TRACE
	Setup Env For C7000   ${Ring}  ${FTS}  ${Add_Enclosure}  ${Add_Storage}  ${Team_Name}
