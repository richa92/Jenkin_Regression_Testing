*** Settings ***
Documentation        OVF2422_OVS16243_Post_rest_certificates_validator_to_check_cert_chain_root_inte_leaf.robot

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
OVF2422_OVS16243_Post_rest_certificates_validator_to_check_cert_chain_root_inte_leaf
    [Documentation]  Post_rest_certificates_validator_to_check_cert_chain_root_inte_leaf.robot
    Log    check Post rest/certificates/validator to check cert chain root_inte_leaf certifcate    console=True
    Set To Dictionary   ${VALIDATOR_CERT}    base64Data     ${ROOT_2_INTE_LEAF}
    Validator Certificate As Expected Type LEAF   ${VALIDATOR_CERT}    LEAF_CERT_TYPE
