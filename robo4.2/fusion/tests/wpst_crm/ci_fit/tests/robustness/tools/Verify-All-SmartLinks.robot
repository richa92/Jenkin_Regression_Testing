*** Settings ***
Documentation		Verify-All-SmartLinks  -  Quickly written to verify smart links.

Variables           ../resources/data_variables.py
Resource            ../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../resources/common.robot
Library             ../resources/robustness-helper.py
Library		    Collections
Library             OperatingSystem

*** Variables ***
${FUSION_IP}                    ${APPLIANCE_IP}
${tbirdEnv}                     None

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Verify SmartLink
    ${resp} =   Fusion Api Get Ethernet Networks
    :FOR   ${e}   IN   @{resp['members']}
    \   Log To Console   Verifying ${e['name']}...   no_newline=${True}
    \   Run Keyword If   "${e['smartLink']}" == "${EXPECTED_SMART_LINK}"   Log To Console   [OK]
    \   ...       ELSE   Fail   [FAILED] Network "${e['name']}" has smartLink set to ${e['smarkLink']}.

