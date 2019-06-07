*** Settings ***
Documentation       OVF2422_OVS16444_CA_signed_leaf certificate(without EKU = Server Authentication) should be validate/post successfully
...                 OVF2422_OVS16444_CA_signed_leaf certificate(without EKU = Server Authentication) should fetched successfully

Library    FusionLibrary
Library    RoboGalaxyLibrary
Resource    ../../../../Resources/api/fusion_api_resource.txt
Resource    ./keywords.txt
Variables    ${DATA_FILE}

Test Teardown    Clear env     root   ${ALIASNAME}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}
${ALIASNAME}          root_ca_external

*** Test Cases ***
OVF2422_OVS16444_CA_signed_leaf_without_EKU_equal_Server_Authentication_should_be_validate_post_successfully
    [Documentation]  OVF2422_OVS16444_CA_signed_leaf_without_EKU_equal_Server_Authentication_should_be_validate_post_successfully

    #OVF2422_OVS16444_CA_signed_leaf_certificate_without_EKU_Server_Authentication_should_fetched_successfully
    ${resp} =  Fusion Api Get Remote Certificate  ${REMOTE_SERVER_CA_SIGN_WIHTOUT_EKU_SERVERAUTH}
    Should Be Equal As Strings  ${resp['status_code']}   200   msg =  Fetch certificate fail$
    #OVF2422_OVS16444_CA_signed_leaf certificate(without EKU = Server Authentication) should be validate/post successfully
    ${LEAF} =  Set Variable   ${resp['certificateDetails'][0]['base64Data']}
    Log    Fetch CA signed leaf certifciate (without EKU=Server_Authentication)successfully    console=True
    ${CA_CHAIN} =   Catenate  SEPARATOR=    ${ROOT}  ${LEAF}
    Set To Dictionary   ${VALIDATOR_CERT}    base64Data     ${CA_CHAIN}
    Validator Certificate As Expected Type LEAF   ${VALIDATOR_CERT}    LEAF_CERT_TYPE
    #OVF2422_OVS16444_CA_signed_leaf certificate(without EKU = Server Authentication) should be validate/post successfully
    Verify Server Certificate Trust Status  ${REMOTE_SERVER_CA_SIGN_WIHTOUT_EKU_SERVERAUTH}   False
    Log    \n - Import root + leaf certificate    console=True
    ${body} =  Generate Certificate Chain Payload   ${REMOTE_SERVER_CA_SIGN_WIHTOUT_EKU_SERVERAUTH}   ${CERTIFICATE_CHAIN}   ${ROOT}   ${ALIASNAME}
    ${resp} =  Fusion Api Import Server Certificate    ${body}
    Wait For Task2       ${resp}     50    5
    Log    \n - Verify certificate info...    console=True
    Verify Server Certificate Trust Status     ${REMOTE_SERVER_CA_SIGN_WIHTOUT_EKU_SERVERAUTH}   True
    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'   Verify Server Certificate Exist In Allcertificates   ${REMOTE_SERVER_CA_SIGN_WIHTOUT_EKU_SERVERAUTH}   False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'  Verify Server Certificate Exist In Allcertificates   ${REMOTE_SERVER_CA_SIGN_WIHTOUT_EKU_SERVERAUTH}   False
    Log    \n - Delete certificate...    console=True
    #OVF2422_OVS16444_CA_signed_leaf certificate(without EKU = Server Authentication) should be deleted successfully
    Remove Root Certificate By Aliasname  ${ALIASNAME}
