*** Settings ***
Documentation        Use POST /rest/certificates/ to import self-signed certificate

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ../../../../Resources/api/settings/security.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}
Test Setup           Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}         unknown
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
05_01_OVF354APIn005_import_iPDU_cert_with_invalid_aliasName_specialCharacter
    [Documentation]  with POST API /rest/certificates

    Log    \n- Logging in OneView appliance    console=True

    Verify Server Certificate Exist In Leafcertbks    ${IPDU_SERVER_CA_SIGN}  False

    Log    \n-Import ${IPDU_SERVER_CA_SIGN} certificate...    console=True

    ${body}=  Generate Invalid Certificate Payload    ${IPDU_SERVER_CA_SIGN}   ${CERTIFICATE}   "test!@#$%^&*()"
    ${resp}=  Fusion Api Import Server Certificate   ${body}
    Should Be Equal As Integers   ${resp['status_code']}  400   msg="\n-Import invalid cert fail!"

    Log    \n-Verify certificate info...    console=True
    Verify Server Certificate Exist In Leafcertbks    ${IPDU_SERVER_CA_SIGN}   False
    Verify Leaf Certificate Exist By Aliasname   ${IPDU_SERVER_CA_SIGN}    False

    Log    \n-Logging out OneView appliance    console=True
    Fusion Api Logout Appliance
