*** Settings ***
Documentation		Edit-All-Ethernet  -  Quickly written to disable smart link.

Variables           ../resources/data_variables.py
Resource            ../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../resources/common.robot
Library             ../resources/robustness-helper.py
Library		    Collections
Library             OperatingSystem

*** Variables ***
${FUSION_IP}                    ${APPLIANCE_IP}
${NEW_SMART_LINK}               ${True}
${tbirdEnv}                     None

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Edit Network
    ${resp} =   Fusion Api Get Ethernet Networks
    :FOR   ${e}   IN   @{resp['members']}
    \   Set To Dictionary  ${e}   smartLink  ${NEW_SMART_LINK}
    \   Log To Console   Setting ${e['name']} smartLink to ${NEW_SMART_LINK}...
    \   ${eresp} =   Fusion Api Edit Ethernet Network   ${e}   ${e['uri']}
    \   Exit For Loop
    \   Sleep And Log Reason To Console   1s   reason=Sleeping 1s after edit network.
