*** Settings ***
Documentation        OVF691:[2FA] Enable OneView to use service account credentials to bind to an enterprise directory
...                  OVF691_API_P001_add Active Directory via service accout binding type
Library              FusionLibrary
Library              RoboGalaxyLibrary
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}         unknown


*** Test Cases ***
OVF691_API_P001_add Active Directory via service accout binding type
    [Documentation]  OVF691_API_P001_add Active Directory via service accout binding type
    Set Log Level           TRACE
    Log    \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.139'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n-Create directory info...    console=true
    ${body}=  Generate Logindomain Payload     ${LOGINDOMAIN_NEW}
    ${resp}=  fusion api add directory  ${body}
    Wait For Task2       ${resp}     50    5

    Log    \n-Delete directory ...    console=true
    ${name}=  Get Directoy Logindomain Id By Name     ${LOGINDOMAIN_NEW}
    ${resp}=  fusion api delete directory    uri=/rest/logindomains/${name}
    Wait For Task2       ${resp}     50    5

    Log    \n-Logging out OneView appliance    console=true
    Fusion Api Logout Appliance