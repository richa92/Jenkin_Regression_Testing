*** Settings ***
Documentation        OVF688(OVS5874)_API_P0008_Replace leaf cert with the same aliasName by PUT / rest / certificates / servers / {aliasName}

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ../../../../Resources/api/settings/security.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

Test Setup           Start remote SSL Server    ${REMOTE_SERVER_SELF_SIGN_1}    ${START_SERVER9}    ${START_SERVER2}
Test Teardown        Clear env    server   ${ALIASNAME}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}
${ALIASNAME}            test_self_signed_leaf_certificate

*** Test Cases ***
Replace leaf cert with the same aliasName by PUT
    Log  Replace leaf cert with the same aliasName by PUT API   console=True


    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'   Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_SELF_SIGN}  False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'  Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_SELF_SIGN}  False


    Log     \n - Import ${REMOTE_SERVER_SELF_SIGN} certificate    console=True
    ${body} =  Generate Certificate Payload    ${REMOTE_SERVER_SELF_SIGN}   ${CERTIFICATE}   ${ALIASNAME}
    ${resp} =  Fusion Api Import Server Certificate    ${body}
    Wait For Task2       ${resp}     50    5

    ${resp} =  Get Server Certificate Status By Aliasname  ${ALIASNAME}
    Should Be Equal As Strings  ${resp['trusted']}   True    msg = certificate was not trusted

    Log    \n - Replace certificate...    console=True
    ${body} =  Generate Certificate Payload   ${REMOTE_SERVER_SELF_SIGN_1}   ${CERTIFICATE}   ${ALIASNAME}
    ${resp} =  Fusion Api Update Server Certificate   ${ALIASNAME}  ${body}
    Wait For Task2       ${resp}     50    5

    Log     \n - Verify certificate info...    console=True
    Verify server certificate trust status  ${REMOTE_SERVER_SELF_SIGN}    False
    Verify server certificate trust status  ${REMOTE_SERVER_SELF_SIGN_1}  True

    Log   \n - Delete certificate...    console=True
    Remove Server Certificate By Aliasname   ${ALIASNAME}

    Log   \n - Verify certificate info after deleting ...    console=True
    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'   Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_SELF_SIGN}  False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'  Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_SELF_SIGN}  False

    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'    Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_SELF_SIGN_1}  False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'   Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_SELF_SIGN_1}  False
