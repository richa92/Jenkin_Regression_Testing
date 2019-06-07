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
01_02_OVF354APIp001_import_iPDU_with_root+leaf
    [Documentation]  with POST API /rest/certificates

    Log    \n- Logging in OneView appliance    console=True

    Verify Server Certificate Exist In Leafcertbks    ${IPDU_SERVER_CA_SIGN}  False
    Verify Server Certificate Trust Status  ${IPDU_SERVER_CA_SIGN}   False

    Log    \n-Import root + leaf certificate...    console=True
    ${body} =  Generate Certificate Chain Payload   ${IPDU_SERVER_CA_SIGN}   ${CERTIFICATE_CHAIN}  ${IPDU_ROOT_CERT}   ${CA_CERT_NAME}
    ${resp} =  Fusion Api Import Server Certificate    ${body}
    Wait For Task2       ${resp}     50    5

    Log    \n-Verify certificate info...    console=True
    Verify Server Certificate Trust Status     ${IPDU_SERVER_CA_SIGN}   True
    Verify Server Certificate Exist In Leafcertbks   ${IPDU_SERVER_CA_SIGN}   False

    Log    \n-Import iPDU...    console=True
    ${resps}=    Discover Power Device from variable    ${POWER_DEVICE_BODY_FORCE}
    Wait For Task2    ${resps}  timeout=240  interval=5  VERBOSE=True

    Log    \n-Logging out OneView appliance    console=True
    Fusion Api Logout Appliance
