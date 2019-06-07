*** Settings ***
Documentation        Use Post / rest / certificates / validator to check single CA root certifcate is root certificate

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
03_OVF2422_OVS16243_Post_rest_certificates_validator_to_check_single_CA_root_certifcate
    [Documentation]  Post_rest_certificates_validator_to_check_single_CA_root_certifcate
    Log    check Post rest/certificates/validator to check single CA root certifcate    console=True
    Set To Dictionary   ${VALIDATOR_CERT}    base64Data     ${ROOT_CA_CERT}
    Validator Certificate As Expected Type    ${VALIDATOR_CERT}     CUSTOM_ROOT_TYPE   1    0    0

