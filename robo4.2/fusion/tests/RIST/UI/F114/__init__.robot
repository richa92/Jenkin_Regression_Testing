*** Settings ***
Resource    ../../API/Fusion_Env_Setup/keywords.txt
Resource    ./keyword.txt
Variables   ./Regression_Data.py

Suite Setup       Precondition Setup For F114
Suite Teardown    Clear F114 Server Profiles


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${admin_credentials}            ${TBirdEnvSetup.${Team_Name}.Common.admin_credentials}
${Ring}                         TBird14
${Add_LE}                       true
${Add_Storage}                  false
${timeout}                      7200
${VERIFY}                       False

*** Keywords ***
Precondition Setup For F114
    Set Log Level	TRACE
    Log To Console And Logfile      \nPrepare LIG env for F114
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Setup Env For TBird    ${Ring}  ${Add_LE}  ${Add_Storage}  ${Team_Name}
    Edit LIG      ${LIG[0]}       ${LIG1}
    Log To Console And Logfile       \nStart to update LI to keep the consistency
    Update Logical Interconnect from Group    ${LI}          ${VERIFY}              ${timeout}

Clear F114 Server Profiles
    Power off ALL servers   PressAndHold
    Wait For ALL Servers Complete Refresh
    Remove All Server Profiles
