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
01_OVF358APIp001_add_ipdu_into_OV_with_fetch_self-sign_cert
    [Documentation]  with POST API /rest/certificates

    Log to Console and Logfile    \n- Logging in OneView appliance
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Verify Client Certificate Exist In Baseappliancejks    ${IPDU_SERVER_SELF_SIGN}  False
    Log To Console And Logfile    \n-Import ${IPDU_SERVER_SELF_SIGN} certificate...

    ${body}=  Generate Certificate Payload     ${IPDU_SERVER_SELF_SIGN}   ${CERTIFICATE}    ${IPDU_SERVER_SELF_SIGN}
     ${resp}=  Fusion Api Import Client Certificate   ${body}
    Should Be Equal As Integers   ${resp['status_code']}  200   msg="\n-Import cert fail!"

    Log To Console And Logfile   \n-Verify certificate info...
    Verify Client Certificate Exist In Baseappliancejks    ${IPDU_SERVER_SELF_SIGN}
    Verify Client Certificate Exist By Aliasname   ${IPDU_SERVER_SELF_SIGN}
    Verify Client Certificate Trust Status    ${IPDU_SERVER_SELF_SIGN}

    Log To Console And Logfile  \n-Import iPDU...

    Log To Console      \n-Import iPDU body is ${POWER_DEVICE_BODY}
    ${resps}=    Discover Power Device from variable    ${POWER_DEVICE_BODY}

    Wait For Task2    ${resps}  timeout=5m  interval=5

    Log to console and logfile  	Check power device is added successfully
    #Wait Until Keyword Succeeds    60s    5s    Verify Resources for List   ${EXPECTED_POWER_DEVICE_DATA}

    Log to Console and Logfile    \n-Logging out OneView appliance
    Fusion Api Logout Appliance
