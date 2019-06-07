*** Settings ***
Documentation        OVF2422_OVS15943_rest_certificates_server_should_not_Get_Delete_update_ROOT_and_intemediate_certificate_import_not_by_SERVER_API

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

Test Teardown        Clear env    root   ${ALIASNAME}
*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}
${ALIASNAME}            root_ca_for_qa_test


*** Test Cases ***
OVF2422_OVS15943_rest_certificates_server_should_not_Get_Delete_update_ROOT_and_intemediate_certificate_import_not_by_SERVER_API
    [Documentation]  rest_certificates_server_should_not_Get_Delete_update_ROOT_and_intemediate_certificate_import_not_by_SERVER_API.robot
    ...              here focus on get delete
    Set to Dictionary    ${CA_CERTIFICATE['members'][0]['certificateDetails']}  aliasName   ${ALIASNAME}
    Set to Dictionary    ${CA_CERTIFICATE['members'][0]['certificateDetails']}   base64Data   ${ROOT_CA_CERT}
    ${resp} =  Fusion Api Import External Ca Certificates    ${CA_CERTIFICATE}
    Wait For Task2         ${resp}       50      5

    ${resp} =  Fusion Api Get Server Certificate   ${ALIASNAME}
    Should Not Be Equal As Integers   ${resp['status_code']}    200      msg = get / rest / certificates / serevrs can get CA certificate succesffully
    Should Contain    ${resp['recommendedActions'][0]}       Please supply valid alias name
    Log       server Get api can not get root certificate    console=True

    ${resp} =  Fusion Api Delete Server Certificate   ${ALIASNAME}
    Wait For Task2    ${resp}     50    5     PASS=Error    errorMessage=Delete_Cert_Error
    Log    \n - Delete certificate...    console=True
    Fusion Api Remove External CA Certificates   ${ALIASNAME}