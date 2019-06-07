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
01_01_OVF354APIn006_import_iPDU_root+leaf_no_CA_cert_in_OV
    [Documentation]  with POST API /rest/certificates

    Log    \n- Logging in OneView appliance    console=True
    #Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

    Verify Server Certificate Exist In Leafcertbks    ${IPDU_SERVER_CA_SIGN}  False
    Log    \n-Import ${IPDU_SERVER_CA_SIGN} certificate...    console=True

    ${body} =  Generate Certificate Payload     ${IPDU_SERVER_CA_SIGN}   ${CERTIFICATE}   ${IPDU_SERVER_CA_SIGN}
    ${resp} =  Fusion Api Import Server Certificate   ${body}
    Wait For Task2    ${resp}    50    5     PASS=Error    errorMessage=CA_cert_Not_Import
    Log    \n - Certificate is not effective, The CA certificate is missing.    console=True


    Log    \n-Verify certificate info...    console=True
    Verify Server Certificate Exist In Leafcertbks    ${IPDU_SERVER_CA_SIGN}  False
    Verify Leaf Certificate Exist By Aliasname   ${IPDU_SERVER_CA_SIGN}    False

    Log    \n-Import iPDU...    console=True
    ${resps}=    Discover Power Device from variable    ${POWER_DEVICE_BODY_FORCE}
    Wait For Task2    ${resps}  timeout=80  interval=5  VERBOSE=True   PASS=Error    errorMessage=UNABLE_TO_VERIFY_CERTIFICATE
    Log    Check power device is not added successfully    console=True

    Log    \n-Verify certificate info...    console=True
    Verify Server Certificate Exist In Leafcertbks    ${IPDU_SERVER_CA_SIGN}  False
    Verify Leaf Certificate Exist By Aliasname   ${IPDU_SERVER_CA_SIGN}    False

    Log    \n-Logging out OneView appliance    console=True
    Fusion Api Logout Appliance
