*** Settings ***
Documentation        OVF2422_OVS17373_Check_Get_rest_certificates_https_remote_to_check_state_and_status_self_signed_server

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
OVF2422_OVS17373_Check_Get_rest_certificates_https_remote_to_check_state_and_status_self_signed_server
    [Documentation]   OVF2422_OVS17373_Check_Get_rest_certificates_https_remote_to_check_state_and_status_self_signed_server
    Log     use get /rest/certificate/https/remote to check self signed cert status   console=True
    Validator Fetch Certificate State And Status   ${REMOTE_SERVER_SELF_SIGN}    Untrusted     OK     'state:OK'   'status:OK'
