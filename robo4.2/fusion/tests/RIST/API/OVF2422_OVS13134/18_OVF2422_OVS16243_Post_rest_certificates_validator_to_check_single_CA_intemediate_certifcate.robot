*** Settings ***
Documentation        Use Post / rest / certificates / validator to check single CA intemediate certifcate is root certificate


Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

Test Teardown        Clear env    root   ${ALIASNAME}
*** Variables ***
${FUSION_IP}         ${APPLIANCE_IP}
${ALIASNAME}         root_ca_for_shqa_test


*** Test Cases ***
OVF2422_OVS16243_Post_rest_certificates_validator_to_check_single_CA_intemediate_certifcate
    [Documentation]  Post_rest_certificates_validator_to_check_single_CA_intemediate_certifcate.robot

    Log    check post /rest/certificate/validator for intermediate cert     console=True

    Set to Dictionary    ${CA_CERTIFICATE['members'][0]['certificateDetails']}  base64Data   ${ROOT_CA_CERT}
    Set to Dictionary    ${CA_CERTIFICATE['members'][0]['certificateDetails']}  aliasName   ${ALIASNAME}
    ${resp} =  Fusion Api Import External Ca Certificates    ${CA_CERTIFICATE}
    Wait For Task2       ${resp}     50    5

    Set To Dictionary   ${VALIDATOR_CERT}    base64Data     ${ROOT_INTE_CERT}
    Validator Certificate As Expected Type    ${VALIDATOR_CERT}     CUSTOM_ROOT_TYPE   0    1    0

    Log    \n - Delete certificate...    console=True
    Fusion Api Remove External CA Certificates   ${ALIASNAME}