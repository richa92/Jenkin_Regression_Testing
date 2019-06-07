*** Settings ***
Documentation    OVF2422_OVS17373_Check_Get_rest_certificates_https_remote_to_check_state_and_status_CA_not_effective

Library    FusionLibrary
Library    RoboGalaxyLibrary
Resource    ../../../../Resources/api/fusion_api_resource.txt
Resource    ./keywords.txt
Variables    ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
OVF2422_OVS17373_Check_Get_rest_certificates_https_remote_to_check_state_and_status_CA_signed_not_effective
    [Documentation]  OVF2422_OVS17373_Check_Get_rest_certificates_https_remote_to_check_state_and_status_CA_not_effective
    Log     use get /rest/certificate/https/remote to check ca signed not effective cert status   console=True
    Validator Fetch Certificate State And Status   ${REMOTE_SERVER_CA_SIGN_NOT_EFFECTIVE}    Invalid     CRITICAL     'state:Invalid'   'status:CRITICAL'

