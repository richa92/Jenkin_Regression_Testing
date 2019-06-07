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
04_OVF358APIp005_check_refresh_ipdu_with_fetch_self-sign_cert
    [Documentation]  with PUT API /rest/power-devices/{ipdu}/refreshState

    Log to Console and Logfile    \n- Logging in OneView appliance
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Verify Client Certificate Exist In Baseappliancejks    ${IPDU_SERVER_SELF_SIGN}  True

    Log To Console And Logfile  \n-Refresh iPDU...

    ${resps}=    Refresh Power Device from variable    ${POWER_DEVICE_REFRESH_BODY}     ${IPDU_SERVER_SELF_SIGN}
    Wait For Task2    ${resps}  timeout=5m  interval=5
    Log to console and logfile  	Check power device is refreshed successfully
    #Wait Until Keyword Succeeds    60s    5s    Verify Resources for List   ${EXPECTED_POWER_DEVICE_DATA}

    Log to Console and Logfile    \n-Logging out OneView appliance
    Fusion Api Logout Appliance
