*** Settings ***
Documentation        Use Post / rest / certificates / validator to check single self - signed LEAF certifcate is leaf certificate

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
OVF2422_OVS16243_Post_rest_certificates_validator_to_check_single_leaf_certifcate
    [Documentation]  Post_rest_certificates_validator_to_check_single_leaf_certifcate.robot
    Log    check Post rest/certificates/validator to check single leaf certifcate    console=True
    Set To Dictionary   ${VALIDATOR_CERT}    base64Data     ${ROOT_2_INTE_LEAF}
    Validator Certificate As Expected Type LEAF   ${VALIDATOR_CERT}    LEAF_CERT_TYPE

