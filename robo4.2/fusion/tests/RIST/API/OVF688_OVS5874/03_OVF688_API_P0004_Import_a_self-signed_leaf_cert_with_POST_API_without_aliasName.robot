*** Settings ***
Documentation        Use POST / rest / certificates / servers to import self - signed leaf certificate to all-certificates bks without aliasname in body

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ../../../../Resources/api/settings/security.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

Test Teardown        Clear env   server   ${COMMON_NAME}

*** Variables ***
${FUSION_IP}         ${APPLIANCE_IP}
${COMMON_NAME}       f


*** Test Cases ***
Import a self signed leaf cert with POST API without aliasName
    [Documentation]  OVF688(ovs5874)_API_P0004_Import a self - signed leaf cert with POST API / rest / certificates / servers / without aliasName

    Log  Use POST/rest/certificates/servers to import self signed leaf certificate without aliasname    console=True

    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'   Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_SELF_SIGN}  False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'  Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_SELF_SIGN}  False

    Log     \n - Import ${REMOTE_SERVER_SELF_SIGN} certificate...    console=True
    ${body} =  Generate Certificate Payload    ${REMOTE_SERVER_SELF_SIGN}   ${CERTIFICATE}
    ${resp} =  Fusion Api Import Server Certificate   ${body}
    Wait For Task2       ${resp}     50    5

    Log   \n - Verify certificate info...    console=True
    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'   Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_SELF_SIGN}
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'  Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_SELF_SIGN}

    Verify Server Certificate Trust Status       ${REMOTE_SERVER_SELF_SIGN}    True

    Log   \n - Delete certificate by common name...    console=True
    Remove Server Certificate By Aliasname   ${COMMON_NAME}

    Log   \n - Verify certificate info after deleting ...    console=True

    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'   Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_SELF_SIGN}  False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'  Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_SELF_SIGN}  False
    Verify Server Certificate Trust Status  ${REMOTE_SERVER_SELF_SIGN}   False