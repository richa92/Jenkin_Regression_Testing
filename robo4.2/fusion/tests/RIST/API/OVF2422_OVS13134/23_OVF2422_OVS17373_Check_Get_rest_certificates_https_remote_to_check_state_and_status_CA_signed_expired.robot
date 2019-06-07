*** Settings ***
Documentation    OVF2422_OVS17373_Check_Get_rest_certificates_https_remote_to_check_state_and_status_CA_signed_expired

Library    FusionLibrary
Library    RoboGalaxyLibrary
Resource    ../../../../Resources/api/fusion_api_resource.txt
Resource    ./keywords.txt
Variables    ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
OVF2422_OVS17373_Check_Get_rest_certificates_https_remote_to_check_state_and_status_CA_signed_expired
    [Documentation]   OVF2422_OVS17373_Check_Get_rest_certificates_https_remote_to_check_state_and_status_CA_signed_expired
    Log     use get /rest/certificate/https/remote to check ca signed expired cert status   console=True
    Validator Fetch Certificate State And Status   ${REMOTE_SERVER_CA_SIGN_EXPIRED}    Expired     CRITICAL     'state:Expired'   'status:CRITICAL'

