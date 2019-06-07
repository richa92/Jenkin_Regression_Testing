*** Settings ***
Documentation        OVF688(ovs5874)_API_N0002_Expired self - signed leaf cert should not be imported with POST / rest / certificates / servers/

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

Test Setup           Start remote SSL Server    ${REMOTE_SERVER_SELF_SIGN_EXPIRED}    ${START_SERVER5}    ${START_SERVER2}

*** Variables ***
${FUSION_IP}          ${APPLIANCE_IP}


*** Test Cases ***
Expired self signed leaf cert should not be imported with POST
    Log  Expired self - signed leaf cert should not be imported with POST /rest/certificates/servers/    console=True
    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'    Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_SELF_SIGN_EXPIRED}   False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'   Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_SELF_SIGN_EXPIRED}   False

    Log   \n - Import ${REMOTE_SERVER_SELF_SIGN_EXPIRED} certificate    console=True
    ${body} =  Generate Certificate Payload    ${REMOTE_SERVER_SELF_SIGN_EXPIRED}   ${CERTIFICATE}
    ${resp} =  Fusion Api Import Server Certificate    ${body}
    Wait For Task2       ${resp}     50    5   PASS=Error    errorMessage=Expired_Cert


    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'    Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_SELF_SIGN_EXPIRED}   False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'   Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_SELF_SIGN_EXPIRED}   False
    Log    \n - Expired certificate should not be imported    console=True