*** Settings ***
Documentation       Can enable smart card only login when enable emergency login is disabled
Library             FusionLibrary
Library             RoboGalaxyLibrary
Library             OperatingSystem
Library             Process
Library             SSHLibrary
Library             String
Library             Dialogs
Library             BuiltIn
Library             json
Library             Collections
Resource            ./keywords.txt
Variables           ${DATA_FILE}


*** Variables ***
${authentication_item}    strictTwoFactorAuthentication


*** Test Cases ***
Enable smart card only login when enable emergency login is disabled
    [Documentation]    when emergency local login is disabled , it should success to enable smart card only login,
    ...                when smart card only login is enabled , it will fail to login with username/password
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}
    ${authenticaiton_body} =  Update Authentication Body    ${enable_smart_card_only_login3}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to enable smart card only login
    Check Authentication Settings    ${authentication_item}    True
    Fusion Api Logout Appliance

    ${auth} =  2FA Login
    Should not be empty    ${auth}
    Disable smart card only login via curl    ${auth}    ${current_auth_body}
