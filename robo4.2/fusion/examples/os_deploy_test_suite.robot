*** Settings ***
Documentation   Example test suite for executing OS Deployment keywords

Library         RoboGalaxyLibrary
Library         FusionLibrary

Variables       os_deploy_data_file.py

Suite Setup     Prepare Test Env


*** Variables ***
${OV_IP}        10.1.2.107
&{OV_CRED}      userName=Administrator      password=admin123
${SRV_URI}      /rest/server-profiles/10b38748-0c44-4ec6-b6b2-81e0b8ac329b
${SRV_URI_1}    /rest/server-profiles/1c9e0329-ad24-47bf-8b70-a9a0714fe258


*** Keywords ***
Prepare Test Env
    [Documentation]     Prepares the testing environment by logging to the appliances
    Set Log Level   Trace
    CPT Login       ${cpt_host['host']}     ${cpt_host['user']}     ${cpt_host['password']}
    ${r}    ${s}=    Fusion Api Login Appliance  ${OV_IP}  ${OV_CRED}
    Run Keyword If  ${r['status_code']} is not 200    Fail      Unable to login


*** Test Cases ***
Test Single node OS Deployment
    [Documentation]     Verifies provisioning of OS on the system
    &{pay}=     Create CPT Payload For OS Deployment    ${SRV_URI}      ${ESXi65}
    ${fn}=      CPT Deploy OS      ${pay}
    Should Not Be Equal     ${fn}   ${None}     "Encountered an error during deploy"
    ${out}=     CPT Wait On Task    ${fn}
    Should Not Be Equal     ${out}  ${Empty}      "Unable to monitor task"
    Should Be Equal     "${out['status']}"      "Success"       "Provisioning task has failed."

Test Multiple nodes OS Deployment
    [Documentation]     Verifies multiple provisioning of OSes on different systems
    @{I1}=      Create List     ${SRV_URI}      ${ESXi65}
    @{I2}=      Create List     ${SRV_URI_1}    ${ESXi65}
    @{SR1}=     Create List     ${I1}       ${I2}
    &{pay}=     Create CPT Payload For Bulk OS Deployment     ${SR1}
    ${fn}=      CPT Deploy OS      ${pay}
    Should Not Be Equal     ${fn}   ${None}     "Encountered an error during deploy"
    ${out}=     CPT Wait On Task    ${fn}
    Should Not Be Equal     ${out}  ${Empty}      "Unable to monitor task"
    Should Be Equal     "${out['nodes'][1]['status']}"      "Success"       "Provisioning task has failed."