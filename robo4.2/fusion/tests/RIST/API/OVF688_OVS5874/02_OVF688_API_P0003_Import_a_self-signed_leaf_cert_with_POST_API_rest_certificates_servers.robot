*** Settings ***
Documentation        Use POST / rest / certificates / servers to import self - signed leaf certificate

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ../../../../Resources/api/settings/security.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

Test Setup           Start remote SSL Server    ${REMOTE_SERVER_SELF_SIGN}
Test Teardown        Clear env     server   ${ALIASNAME}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}
${ALIASNAME}            self_signed_certificate_1


*** Test Cases ***
Import a self signed leaf cert with POST API rest certificates servers and Delete leaf cert with DELETE rest certificates servers aliasName
    [Documentation]  OVF688(ovs5874)_API_P0003_Import a self - signed leaf cert with POST API / rest / certificates / servers OVF688(ovs5874)_API_P0005_Delete_leaf_cert_with_DELETE_rest_certificates_servers_aliasName
    Log  Use POST /rest/certificates/servers to import self - signed leaf certificate    console=True

    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'   Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_SELF_SIGN}  False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'  Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_SELF_SIGN}  False
    Log     \n - Import ${REMOTE_SERVER_SELF_SIGN} certificate...    console=True

    ${body} =  Generate Certificate Payload     ${REMOTE_SERVER_SELF_SIGN}   ${CERTIFICATE}   ${ALIASNAME}
    ${resp} =  Fusion Api Import Server Certificate   ${body}
    Wait For Task2       ${resp}     50    5

    Log    \n - Verify certificate info...    console=True

    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'   Verify Server Certificate Exist In Leafcertbks    ${REMOTE_SERVER_SELF_SIGN}
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'  Verify Server Certificate Exist In Leafcertbks    ${REMOTE_SERVER_SELF_SIGN}
    Verify Leaf Certificate Exist By Aliasname   ${ALIASNAME}
    Verify Server Certificate Trust Status    ${REMOTE_SERVER_SELF_SIGN}    True

    Log   \n - Delete certificate...    console=True
    Remove Server Certificate By Aliasname  ${ALIASNAME}

    Log   \n - Verify certificate info after deleting ...    console=True

    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'   Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_SELF_SIGN}  False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'  Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_SELF_SIGN}  False
    Verify Server Certificate Trust Status  ${REMOTE_SERVER_SELF_SIGN}    False