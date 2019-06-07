*** Settings ***
Documentation        OVF688(ovs5874)_API_N0005_Same certificate should not be imported by POST / rest / certificates / servers

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ../../../../Resources/api/settings/security.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

Test Setup           Start remote SSL Server    ${REMOTE_SERVER_SELF_SIGN}
Test Teardown        Clear env    server   ${ALIASNAME}
*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}
${ALIASNAME}            test_self_signed_leaf_certificate

*** Test Cases ***
Same certificate should not be imported by POST
    Log     Same certificate should not be imported by POST /rest/certificates/servers    console=True
    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'    Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_SELF_SIGN}   False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'   Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_SELF_SIGN}   False
    Log    \n - Import ${REMOTE_SERVER_SELF_SIGN} certificate    console=True

    ${body} =  Generate Certificate Payload    ${REMOTE_SERVER_SELF_SIGN}   ${CERTIFICATE}   ${ALIASNAME}
    ${resp} =  Fusion Api Import Server Certificate    ${body}
    Wait For Task2       ${resp}     50    5
    ${resp} =  Get Server Certificate Status By Aliasname  ${ALIASNAME}
    Should Be Equal As Strings  ${resp['trusted']}   True    msg = certificate was not trusted

    Log   \n - Import same certificate again    console=True
    ${resp} =  Fusion Api Import Server Certificate    ${body}
    Wait For Task2       ${resp}     50    5   PASS=Error     errorMessage=Same_Cert_Can_Not_Import
    Log   \n - Certificate already exists    console=True

    Log   \n - Delete certificate...    console=True
    Remove Server Certificate By Aliasname   ${ALIASNAME}

    Log   \n - Verify certificate info after deleting ...    console=True

    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'    Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_SELF_SIGN}   False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'   Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_SELF_SIGN}   False
    Verify Server Certificate Trust Status  ${REMOTE_SERVER_SELF_SIGN}    False