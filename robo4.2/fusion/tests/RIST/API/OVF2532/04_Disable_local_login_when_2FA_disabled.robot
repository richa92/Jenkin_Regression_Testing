*** Settings ***
Documentation        Can disable local login when 2FA disabled
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              Process
Library              SSHLibrary
Library              String
Library              Dialogs
Library              BuiltIn
Library              json
Library              Collections
Resource             ./keywords.txt
Variables            ${DATA_FILE}


*** Variables ***
${2FA_switch}    twoFactorAuthenticationEnabled
${local_login_switch}    allowLocalLogin

*** Test Cases ***
Disable local login when 2FA disabled
    [Documentation]    Can disable local login when 2FA is disabled
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  Run Keyword And Return Status    Set directory server login domain as default    configuredLoginDomains    defaultLoginDomain    userad
    Should be equal    ${resp}    ${True}    meg=Fail to set directory server login domain as default
    ${authentication_body} =  Edit Authentication Switch    ${local_login_switch}    ${False}
    ${disbale_local_login} =  Fusion Api Edit Login Domains Global Settings    ${authentication_body}
    Should Be Equal    '${disbale_local_login['status_code']}'    '200'    msg=Fail to disable local login
    Check updated 2FA authentication settings    ${local_login_switch}    ${False}
    Fusion Api Logout Appliance

    Log to console    \n-Login appliance with local user    console=yes
    ${local_login} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Should be equal    '${local_login[0]['status_code']}'    '400'    msg=Cannot login using username/password when disable local login while disable 2FA
    Should Be Equal    '${local_login[0]['details']}'    '${TwoFA_errorMessages['Fail_local_login']}'    msg=Show incorrect error message for fail to local login with local user

    Log    \nLogin appliance with directory user    console=yes
    ${ad_login} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${ad_user}
    Should be equal    '${ad_login[0]['status_code']}'    '200'    msg=Fail to login with directroy user
    Fusion Api Logout Appliance
