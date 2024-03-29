*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Variables   ./Regression_Data.py
Suite Setup     Precondition ENV Setup
Suite Teardown  Clean Test Environment After Tests Done


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring}                         TBird15
${Add_LE}                       true
${Add_Storage}                  true
${Add_Existing_Storage}         false


*** Keywords ***
Precondition ENV Setup
    Set Log Level       TRACE
    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Setup Env For TBird    ${Ring}  ${Add_LE}  ${Add_Storage}  ${Team_Name}  ${Add_Existing_Storage}

Clean Test Environment After Tests Done
    [Documentation]     Clean and Remove Modified Volume After Test
    Clean Test Environment
    Remove All Storage Volumes Async

Clean Test Environment
    Log to console  \nPower Off Servers and remove all profiles
    Power off ALL servers   PressAndHold
    Wait For ALL Servers Complete Refresh
    Remove All Server Profiles


