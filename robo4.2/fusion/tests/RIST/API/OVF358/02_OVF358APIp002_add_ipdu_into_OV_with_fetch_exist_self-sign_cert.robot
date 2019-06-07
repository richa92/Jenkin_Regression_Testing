*** Settings ***
Documentation        Use POST /rest/certificates/ to import self-signed certificate

Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ../../../../Resources/api/settings/security.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py

*** Variables ***
${APPLIANCE_IP}         unknown
${FUSION_IP}            ${APPLIANCE_IP}


*** Test Cases ***
02_OVF358APIp002_add_ipdu_into_OV_with_fetch_exist_self-sign_cert
    [Documentation]  with POST API /rest/certificates

    Log to Console and Logfile    \n- Logging in OneView appliance
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Verify Client Certificate Exist In Baseappliancejks    ${IPDU_SERVER_SELF_SIGN}  True
    Log To Console And Logfile    \n-Import ${IPDU_SERVER_SELF_SIGN} exist certificate...

    ${body}=  Generate Certificate Payload     ${IPDU_SERVER_SELF_SIGN}   ${CERTIFICATE}   ${IPDU_SERVER_SELF_SIGN}
    ${resp}=  Fusion Api Import Client Certificate   ${body}
    Should Be Equal As Integers   ${resp['status_code']}  409   msg="\n-Import exist cert!"
    Should Be Equal   ${resp['errorCode']}  IMPORT_SERVERCERT_EXISTS_ALREADY    msg="\n-Import cert again, this is not right!"
    Log To Console And Logfile   \n-Not Import exist cert...

    Log To Console And Logfile   \n-Verify certificate info...
    Verify Client Certificate Exist In Baseappliancejks    ${IPDU_SERVER_SELF_SIGN}
    Verify Client Certificate Exist By Aliasname   ${IPDU_SERVER_SELF_SIGN}
    Verify Client Certificate Trust Status    ${IPDU_SERVER_SELF_SIGN}

    Log To Console And Logfile  \n-This iPDU certificate is already in store

    Log to Console and Logfile    \n-Logging out OneView appliance
    Fusion Api Logout Appliance
