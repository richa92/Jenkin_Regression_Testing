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
02_03_OVF354APIn012_remove_cert_with_invalid_cert_aliasName_is_wrong
    [Documentation]  with DELETE API /rest/certificates/aliasName

    Log    \n- Logging in OneView appliance    console=True

    Verify Server Certificate Trust Status   ${IPDU_SERVER_CA_SIGN}    True

    Log    \n-Remove certificate with wrong aliasName...    console=True
    ${resp}=  Fusion Api Delete Server Certificate   not_exist_name
    Should Be Equal As Integers   ${resp['status_code']}  202   msg="\n-Delete cert task fail!"
    Wait For Task2    ${resp}  timeout=40  interval=5  VERBOSE=True  PASS=Error    errorMessage=Cert.SSL_CERTIFICATE_MISSING_DELETE_ERROR

    Log    \n-Check no leaf cert stored...    console=True
    Verify Server Certificate Exist In Leafcertbks    ${IPDU_SERVER_CA_SIGN}    False
    Verify Leaf Certificate Exist By Aliasname        ${IPDU_SERVER_CA_SIGN}    False

    Log    \n-Logging out OneView appliance    console=True
    Fusion Api Logout Appliance
