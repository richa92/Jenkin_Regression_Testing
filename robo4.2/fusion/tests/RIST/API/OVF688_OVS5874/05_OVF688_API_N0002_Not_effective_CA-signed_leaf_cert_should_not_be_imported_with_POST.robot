*** Settings ***
Documentation        OVF688(ovs5874)_API_N0002_not_effective_CA - signed_leaf_cert_should_not_be_imported_with_POST

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

Test Setup           Start remote SSL Server    ${REMOTE_SERVER_CA_SIGN_NOT_EFFECTIVE}    ${START_SERVER6}    ${START_SERVER2}

*** Variables ***
${FUSION_IP}          ${APPLIANCE_IP}

*** Test Cases ***
Not effective CA signed leaf cert should not be imported with POST
    Log    not_effective_CA - signed_leaf_cert_should_not_be_imported_with_POST   console=True

    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'   Verify Server Certificate Exist In Leafcertbks      ${REMOTE_SERVER_CA_SIGN_NOT_EFFECTIVE}   False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'  Verify Server Certificate Exist In Leafcertbks      ${REMOTE_SERVER_CA_SIGN_NOT_EFFECTIVE}   False

    Verify Server Certificate Trust Status  ${REMOTE_SERVER_CA_SIGN_NOT_EFFECTIVE}      False

    Log   \n - Import root + leaf which was not effective certificate    console=True
    ${body} =  Generate Certificate Chain Payload  ${REMOTE_SERVER_CA_SIGN_NOT_EFFECTIVE}   ${CERTIFICATE_CHAIN}   ${ROOT_CERT_NOT_EFFECTIVE}
    ${resp} =  Fusion Api Import Server Certificate    ${body}
    Wait For Task2    ${resp}    100    5     PASS=Error    errorMessages=Not_Effective_cert
    Log   \n - Certificate is not effective    console=True
    Log   \n - Verify certificate info...    console=True

    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'   Verify Server Certificate Exist In Leafcertbks        ${REMOTE_SERVER_CA_SIGN_NOT_EFFECTIVE}   False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'  Verify Server Certificate Exist In Leafcertbks        ${REMOTE_SERVER_CA_SIGN_NOT_EFFECTIVE}   False

    Verify Server Certificate Trust Status  ${REMOTE_SERVER_CA_SIGN_NOT_EFFECTIVE}     False