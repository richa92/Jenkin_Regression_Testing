*** Settings ***
Resource             ../Fusion_Env_Setup/keywords.txt
Resource             ./keywords.txt
Resource             ../../../../Resources/api/fusion_api_resource.txt
Variables            ${DATA_FILE}

Suite Setup     Precondition Setup
Suite Teardown  Clear Setup

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA

*** Keywords ***
Precondition Setup
    [Documentation]  Setup environment for 2FA API test: add Active Directory with SA binding type, enable 2FA flag.
    Set Log Level           TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n-Import Root CA certificate ...    console=true
    ${cert_body}=  Generate Certifiate Payload    ${CERT_BODY}  ${ROOT_CERTIFICATE}  ${ALIAS_NAME}
    ${resp}=  fusion api import external ca certificates    ${cert_body}
    Wait For Task2       ${resp}     50    5

    Log    \n-Add directory ...    console=true
    ${direct_body}=  Generate Logindomain Payload     ${LOGINDOMAIN}
    ${resp}=  fusion api add directory  ${direct_body}
    Wait For Task2       ${resp}     50    5

    Log    \n-Enable 2FA flag ...    console=true
    ${resp}=  fusion api get login domains global settings
    ${setting_body}=  Copy Dictionary  ${resp}
    Run Keyword If  ${setting_body['twoFactorAuthenticationEnabled']} != ${True}    set to dictionary  ${setting_body}    twoFactorAuthenticationEnabled    ${True}
    remove from dictionary    ${setting_body}    status_code
    remove from dictionary    ${setting_body}    headers
    ${resp}=  fusion api edit login domains global settings    ${setting_body}

    Fusion Api Logout Appliance

Clear Setup
    [Documentation]  clean up environment for 2FA API test: disable 2FA flag, delete Active Directory with SA binding type, and remove root CA.
    Set Log Level           TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n-Disable 2FA flag ...    console=true
    ${resp}=  fusion api get login domains global settings
    ${body}=  Copy Dictionary  ${resp}
    Run Keyword If  ${body['twoFactorAuthenticationEnabled']}==${True}    set to dictionary  ${body}    twoFactorAuthenticationEnabled    ${False}
    remove from dictionary    ${body}    status_code
    remove from dictionary    ${body}    headers
    fusion api edit login domains global settings    ${body}

    Log    \n-Delete directory ...    console=true
    ${name}=  Get Directoy Logindomain Id By Name   ${LOGINDOMAIN}
    ${resp}=  fusion api delete directory    uri=/rest/logindomains/${name}
    Wait For Task2       ${resp}     50    5

    Log    \n-Remove root CA certificate ...    console=true
    ${resp}=  fusion api remove external ca certificates    ${ALIAS_NAME}
    Wait For Task2       ${resp}     50    5

    Fusion Api Logout Appliance
