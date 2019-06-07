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
01_04_OVF354APIp006_remove_iPDU_with_CA-signed_cert
    [Documentation]  with DELETE API /rest/certificates/aliasName

    Log    \n- Logging in OneView appliance    console=True

    Verify Server Certificate Trust Status  ${IPDU_SERVER_CA_SIGN}    True
    Verify Leaf Certificate Exist By Aliasname   ${CA_CERT_NAME}    False

    ${resps} =    Fusion Api Remove Power Device    ${IPDU_SERVER_CA_SIGN}, PDU 1
    Wait For Task2    ${resps}  timeout=240  interval=5  VERBOSE=True
    Log    Check power device is not deleted successfully    console=True

    Log    \n-Remove CA certificate from OV store    console=Ture
    ${resp} =  Fusion Api Remove External CA Certificates   ${CA_CERT_NAME}
    Should Be Equal As Integers   ${resp['status_code']}  202   msg="\n-Delete CA cert fail!"
    Wait For Task2    ${resp}  timeout=60  interval=5  VERBOSE=True

    Log    \n-Check if CA certificate not exist    console=Ture
    ${resp} =   Fusion Api Get Ca Certificate  param=${CA_CERT_NAME}
    Should Be Equal As Integers   ${resp['status_code']}   404     msg=CA certificate can be found
    Should Contain   ${resp['message']}     Unable to retrieve the input certificate. No matching certificate found for the specified alias.

    Log    \n-Logging out OneView appliance    console=True
    Fusion Api Logout Appliance
