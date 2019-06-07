*** Settings ***
Documentation		C7000 Fusion Appliance deployment and common resources setup (users, networks, SAN manager, etc.)
Resource            ../Fusion_Env_Setup/keywords.txt
Resource            ./keywords.txt
#Variables           ./data_variables.py

*** Variables ***
${APPLIANCE_IP}                 ${None}             # leave it as ${None} if you want this test to create a new one
${SSH_PASS}                     hpvse1
${Team_Name}                    SHQA
${VM_Owner}                     Alex-API-Env-Setup
${Fusion_Version}               3.0
${OVA_Type}                     SSH
${Pass_Build}                   true
${Build_Number_Filter}          NONE
${settings}                     ${C7000EnvSetup.${Team_Name}}
${admin_credentials}            ${settings.Common.admin_credentials}
${Ring}                         WPST9
${Add_Storage}                  true
${Add_Enclosure}                false
${FTS}                          false
${Env_Setup}                    false
*** Test Cases ***
Setup Fusion Environment - deploy fusion C7000 appliance, and add required resources
	Set Log Level	TRACE
    ${APPLIANCE_IP}=        Get Variable Value                  ${APPLIANCE_IP}                 ${None}
    ${APPLIANCE_IP}=        Run Keyword If                      '${APPLIANCE_IP}'=='${None}'    Deploy C7000 Appliance
    ...                     ELSE                                Set Variable                    ${APPLIANCE_IP}
    Set Global Variable     ${APPLIANCE_IP}                     ${APPLIANCE_IP}

    Set Global Variable     ${appliance}                        ${settings.Common.appliance}
    Set Global Variable     ${timeandlocale}                    ${settings.Common.timeandlocale}

	Run Keyword If          '${FTS}'=='true'
	...                     Log    [First Time Setup]    console=true
    Run Keyword If          '${FTS}'=='true'
    ...                     First Time Setup
    ...                     password=${settings.Common.admin_credentials['password']}

    Run Keyword If          '${FTS}'=='false'
    ...                     Console                             Skipped FTS since variable 'FTS' is '${FTS}'

    Pass Execution If       '${Env_Setup}'=='false'             Skipped Env Setup since variable 'Env_Setup' is '${Env_Setup}'
    Setup Env For C7000     ${Ring}
    ...                     ${FTS}
    ...                     ${Add_Enclosure}
    ...                     ${Add_Storage}