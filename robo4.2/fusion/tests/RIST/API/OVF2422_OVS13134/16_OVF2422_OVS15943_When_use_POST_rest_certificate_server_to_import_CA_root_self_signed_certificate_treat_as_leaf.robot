*** Settings ***
Documentation        OVF2422_OVS15943_When_use_POST_rest_certificate_server_to_import_CA_root(self - signed)_certificate_treat as leaf
...                  OVF2422_OVS15943_Get / rest / certificate / server should list CA root(self - signed) certificate, treat as leaf
...                  OVF2422_OVS15943_DELETE / rest / certificate / server should delete CA root(self - signed) certificate, treat as leaf

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}
Test Teardown        Clear env     server   ${ALIASNAME}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}
${ALIASNAME}            root_ca_for_test


*** Test Cases ***
OVF2422_OVS15943_When_use_POST_rest_certificate_server_to_import_CA_root(self - signed)_certificate_treat as leaf
    [Documentation]  OVF2422_OVS15943_When_use_POST_rest_certificate_server_to_import_CA_root(self - signed)_certificate_treat as leaf.robot

    Log    check if post /rest/certificate/server import root ca as leaf     console=True

    Set To Dictionary    ${CERTIFICATE['certificateDetails'][0]}    base64Data    ${ROOT_CA_CERT}
    Set to Dictionary    ${CERTIFICATE['certificateDetails'][0]}  aliasName   ${ALIASNAME}

    ${resp} =  Fusion Api Import Server Certificate   ${CERTIFICATE}
    Wait For Task2       ${resp}     50    5

    Verify Leaf Certificate Exist By Aliasname   ${ALIASNAME}  True
    Log    \n - Delete certificate...
    Remove Server Certificate By Aliasname  ${ALIASNAME}
    Verify Leaf Certificate Exist By Aliasname   ${ALIASNAME}  False
