*** Settings ***
Documentation        Can enable local login when 2FA disabled
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              Process
Library              SSHLibrary
Library              robot.libraries.String
Library              String
Library              Dialogs
Library              BuiltIn
Library              json
Library              Collections
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}


*** Variables ***
${2FA_switch}    twoFactorAuthenticationEnabled
${local_login_switch}    allowLocalLogin

*** Test Cases ***
Enable local login when 2FA disabled
    [Documentation]    Can enable local login when 2FA is disabled
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${ad_user}
    ${authentication_body} =  Edit Authentication Switch    ${local_login_switch}    ${True}
    ${disbale_local_login} =  Fusion Api Edit Login Domains Global Settings    ${authentication_body}
    Should Be Equal    '${disbale_local_login['status_code']}'    '200'    msg=Fail to enable local login
    Check updated 2FA authentication settings    ${local_login_switch}    ${True}
    Fusion Api Logout Appliance

    Log    \n-Login appliance with local user    console=yes
    ${local_login} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Should be equal    '${local_login[0]['status_code']}'    '200'    msg=Fail to login with local user
    Fusion Api Logout Appliance