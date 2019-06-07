*** Settings ***
Documentation        Use POST /rest/certificates/ to import self-signed certificate

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ../../../../Resources/api/settings/security.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}
Test Setup           Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}         unknown
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
02_02_OVF354APIn004_import_iPDU_cert_with_exist_cert_but_different_aliasName
    [Documentation]  with POST API /rest/certificates

    Log    \n- Logging in OneView appliance    console=True

    Verify Server Certificate Exist In Leafcertbks    ${IPDU_SERVER_CA_SIGN}    False
    Verify Leaf Certificate Exist By Aliasname   ${IPDU_SERVER_CA_SIGN}    False

    Log    \n-Import Same Cert with different Name ${IPDU_SERVER_CA_SIGN_2NAME} certificate...    console=True
    ${body}=  Generate Certificate Payload    ${IPDU_SERVER_CA_SIGN}   ${CERTIFICATE}   ${IPDU_SERVER_CA_SIGN_2NAME}
    ${resp}=  Fusion Api Import Server Certificate   ${body}
    Should Be Equal As Integers   ${resp['status_code']}  202   msg="\n-Import cert fail, WRONG!"

    Log    \n-Verify certificate info...    console=true
    ${resp} =   Fusion Api Get Server Certificate  ${IPDU_SERVER_CA_SIGN_2NAME}
    Should Be Equal As Integers   ${resp['status_code']}   404     msg=No such name certificate
    Should Contain   ${resp['message']}     Unable to retrieve the input certificate. No matching certificate found for the specified alias.
    Verify Leaf Certificate Exist By Aliasname   ${IPDU_SERVER_CA_SIGN_2NAME}    False

    Log    \n-Logging out OneView appliance    console=True
    Fusion Api Logout Appliance
