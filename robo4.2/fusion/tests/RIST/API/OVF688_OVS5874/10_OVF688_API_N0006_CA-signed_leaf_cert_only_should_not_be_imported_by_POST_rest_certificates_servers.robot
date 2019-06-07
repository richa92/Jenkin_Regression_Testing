*** Settings ***
Documentation        OVF688(ovs5874)_API_N0006_CA - signed leaf cert only should not be imported by POST / rest / certificates / servers

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

Test Setup           Start remote SSL Server    ${REMOTE_SERVER_CA_SIGN}    ${START_SERVER7}    ${START_SERVER2}

*** Variables ***
${FUSION_IP}          ${APPLIANCE_IP}


*** Test Cases ***
Signed leaf cert only should not be imported by POST
    Log   \n - Logging in OneView appliance    console=True

    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'     Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_CA_SIGN}   False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'    Verify Server Certificate Exist In Leafcertbks   ${REMOTE_SERVER_CA_SIGN}   False

    Log    \n - Import ${REMOTE_SERVER_CA_SIGN} certificate    console=True
    ${body} =  Generate Certificate Payload     ${REMOTE_SERVER_CA_SIGN}   ${CERTIFICATE}
    ${resp} =  Fusion Api Import Server Certificate    ${body}
    Wait For Task2       ${resp}     100    5   PASS=Error    errorMessage=CA_Signed_Leaf_Not_Import
    Run Keyword If  '${SECURITY_MODE}' == 'LEGACY'     Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_CA_SIGN}   False
    Run Keyword If  '${SECURITY_MODE}' == 'FIPS'    Verify Server Certificate Exist In Leafcertbks  ${REMOTE_SERVER_CA_SIGN}   False
    Log     \n - CA - signed leaf only should not be imported    console=True