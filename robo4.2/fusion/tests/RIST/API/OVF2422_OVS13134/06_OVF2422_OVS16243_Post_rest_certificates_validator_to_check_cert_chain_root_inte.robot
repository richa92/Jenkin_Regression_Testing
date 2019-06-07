*** Settings ***
Documentation        OVF2422_OVS16243_Post_rest_certificates_validator_to_check_cert_chain_root_inte.robot

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
OVF2422_OVS16243_Post_rest_certificates_validator_to_check_cert_chain_root_inte
    [Documentation]  Post_rest_certificates_validator_to_check_cert_chain_root_inte.robot
    Log    check ost rest/certificates/validator to check cert chain root_inte certifcate    console=True
    Set To Dictionary   ${VALIDATOR_CERT}    base64Data     ${ROOT_2_INTE}
    Validator Certificate As Expected Type   ${VALIDATOR_CERT}    CUSTOM_ROOT_TYPE   1    2

