*** Settings ***
Documentation    Run hfsh (aka OneView shell, aka bcmsh) commands and record the output.
...              This requires SSH access to your Hafnium module.
...              This requires data variable file (see resources/run-hfsh-data_variable_template.py for example).

Resource            ../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../resources/common.robot
Library             Collections
Library             ../resources/robustness-helper.py


*** Variables ***
${CYCLES}                       3600
${FUSION_IP}                    ${APPLIANCE_IP}


*** Test Cases ***
Run Hf OneView Shell Commands From Variable File
    Run Keyword If   "${APPLIANCE_IP}" == "${EMPTY}"   Fail   msg=There was a validation error. Please check the validation test case(s) and try again.
    Log Variables
    Cycle


*** Keywords ***
Cycle
    [Documentation]   Run Hf OneView Shell Commands.
    ${icmBay} =   Fetch From Right   ${ICM_NAME}   ${SPACE}
    ${encICMPasswd} =   Get Variable Value   ${ENC_ICM_PASSWD}
    ${encICMPasswd} =   Run Keyword If   ${encICMPasswd} is ${null}   Get Interconnect OneView Credential   ${ENC_SERIAL}   ${icmBay}
    ...                           ELSE   Set Variable   ${encICMPasswd}
    Log To Console   Opening connection to ${encICMPasswd['${ENC_SERIAL}_${icmBay}']['ipv6LinkLocal']}...   no_newline=${True}
    Open Connection   ${encICMPasswd['${ENC_SERIAL}_${icmBay}']['ipv6LinkLocal']}%${SRC_INTERFACE}   timeout=15m
    Log To Console   [OK]
    Log To Console   Logging in as ${HF_USERNAME}/${HF_PASSWORD}...   no_newline=${True}
    Login   ${HF_USERNAME}   ${HF_PASSWORD}
    Log To Console   [OK]
    Log To Console   Switching to Hafnium shell...   no_newline=${True}
    Write   bcmsh
    ${o} =   Read Until Regexp   OneView[\>|\#]
    Log To Console   [OK]
    Write   set cli pagination off
    ${o} =   Read Until Regexp   OneView[\>|\#]
    :FOR   ${x}   IN RANGE   1   ${CYCLES}+1
    \   Log   \n Cycle: ${x} of ${CYCLES}   console=${True}
    \   Run Hafnium OneView Shell Commands   ${HFSH_COMMANDS}
    Close All Connections

