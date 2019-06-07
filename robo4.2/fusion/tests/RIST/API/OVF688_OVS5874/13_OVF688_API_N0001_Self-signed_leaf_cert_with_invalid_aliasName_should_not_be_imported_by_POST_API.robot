*** Settings ***
Documentation        OVF688(ovs5874)_API_N0001_Self - signed leaf cert with invalid aliasName should not be imported by POST API / rest / certificates / servers/

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

Test Setup           Start remote SSL Server    ${REMOTE_SERVER_SELF_SIGN}

*** Variables ***
${FUSION_IP}            ${APPLIANCE_IP}
${ALIASNAME}            _test$+?~''[}!:

*** Test Cases ***
Self signed leaf cert with invalid aliasName should not be imported by POST API
    Log   Self - signed leaf cert with invalid aliasName should not be imported by POST API    console=True
    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'      Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_SELF_SIGN}   False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'      Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_SELF_SIGN}   False
    Log    \n - Import ${REMOTE_SERVER_SELF_SIGN} certificate    console=True
    ${body} =  Generate Certificate Payload    ${REMOTE_SERVER_SELF_SIGN}   ${CERTIFICATE}   ${ALIASNAME}
    ${resp} =  Fusion Api Import Server Certificate    ${body}
    Wait For Task2    ${resp}     300    3     PASS=Error    errorMessage=Invalid_Cert_Alias_Name
    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'       Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_SELF_SIGN}   False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'       Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_SELF_SIGN}   False
    Log    \n - Invalid aliasname should not be imported    console=True