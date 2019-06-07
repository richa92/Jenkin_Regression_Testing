*** Settings ***
Documentation                   Set VPN
...                               Used to set VPN on appliance to access 10 network

Library        FusionLibrary
Library        BuiltIn
Library        Collections
Library        json
Library        Dialogs
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables                ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}        16.114.209.223
${DATA_FILE}        ./Regression_Data.py


*** Test Cases ***
Set VPN
    Set Log Level	TRACE
    Log    Start to configure VPN on appliance    console=true
    Run Multi Cmd   ${APPLIANCE_IP}    ${ssh_username}    ${ssh_password}    ${commands}
    ${output} =   Run Multi Cmd   ${APPLIANCE_IP}    ${ssh_username}    ${ssh_password}    ${verify_cmd}
    Should Contain      ${output}    ${verify_output}      Set VPN failed!\n${output}
    Log    Configure VPN on appliance complete    console=true
