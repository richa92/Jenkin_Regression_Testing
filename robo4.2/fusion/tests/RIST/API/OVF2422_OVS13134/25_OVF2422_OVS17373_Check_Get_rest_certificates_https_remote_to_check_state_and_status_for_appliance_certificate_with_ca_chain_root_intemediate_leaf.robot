*** Settings ***
Documentation    OVF2422_OVS17373_Check_Get_rest_certificates_https_remote_to_check_state_and_status_for_appliance_certificate_with_ca_chain_root_intemediate_leaf

Library    FusionLibrary
Library    RoboGalaxyLibrary
Resource    ../../../../Resources/api/fusion_api_resource.txt
Resource    ./keywords.txt
Variables    ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
OVF2422_OVS17373_Check_Get_rest_certificates_https_remote_to_check_state_and_status_for_appliance_certificate_with_ca_chain_root_intemediate_leaf
    [Documentation]  OVF2422_OVS17373_Check_Get_rest_certificates_https_remote_to_check_state_and_status_for_appliance_certificate_with_ca_chain_root_intemediate_leaf
    Log     use get /rest/certificate/https/remote to check appliance cert status   console=True
    Validator Fetch Certificate State And Status   ${APPLIANCE_CHAIN_CERT}    Untrusted     CRITICAL     'state:Untrusted'   'status:CRITICAL'  'state:Untrusted'   'status:CRITICAL'
