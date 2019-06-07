*** Settings ***
Documentation        OVF688(ovs5874)_API_P0006_Import a CA - signed(root + leaf) leaf cert by POST / rest / certificates / servers

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ../../../../Resources/api/settings/security.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

Test Setup           Start remote SSL Server    ${REMOTE_SERVER_CA_SIGN}    ${START_SERVER7}    ${START_SERVER2}
Test Teardown        Clear env   root   ${ALIASNAME}

*** Variables ***
${FUSION_IP}          ${APPLIANCE_IP}
${ALIASNAME}          root_ca_external_import


*** Test Cases ***
Import a CA signed leaf cert by POST - root + leaf
    Log  Import a CA - signed(root + leaf) leaf cert by POST /rest/certificates/servers   console=True

    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'     Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_CA_SIGN}    False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'    Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_CA_SIGN}    False

    Verify Server Certificate Trust Status  ${REMOTE_SERVER_CA_SIGN}   False

    Log   \n - Import root + leaf certificate    console=True
    ${body} =  Generate Certificate Chain Payload   ${REMOTE_SERVER_CA_SIGN}   ${CERTIFICATE_CHAIN}  ${LINUX_ROOT_CERT}   ${ALIASNAME}
    ${resp} =  Fusion Api Import Server Certificate    ${body}
    Wait For Task2       ${resp}     100    5

    Log    \n - Verify certificate info...    console=True
    Verify Server Certificate Trust Status     ${REMOTE_SERVER_CA_SIGN}   True

    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'      Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_CA_SIGN}   False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'     Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_CA_SIGN}   False


    Log  \n - Delete certificate...    console=True
    Remove Root Certificate By Aliasname  ${ALIASNAME}