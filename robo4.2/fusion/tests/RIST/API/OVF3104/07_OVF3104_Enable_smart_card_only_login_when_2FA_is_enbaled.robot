*** Settings ***
Documentation       Cana enable smart card only login when 2FA is enabled
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
Resource            ./../../../../Resources/api/common/common.txt
Resource            ./keywords.txt
Variables           ${DATA_FILE}


*** Variables ***
${authentication_item}    strictTwoFactorAuthentication


*** Test Cases ***
Enable smart card only login when 2FA is enbaled
    [Documentation]    When 2FA is enabled , it will success to enable smart card only login
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}
    ${authenticaiton_body} =  Update Authentication Body    ${enable_smart_card_only_login7}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to enable smart card only login when 2FA is enabled
    Check Authentication Settings    ${authentication_item}    True
    Fusion Api Logout Appliance

    Log    \n-Login appliance with local user    console=yes
    ${local_login} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Should be equal    '${local_login[0]['status_code']}'    '400'    msg=Cannot login using username/password when enable smart card only login
    Should be equal    '${local_login[0]['recommendedActions'][0]}'    '${errorMessages['Fail_Local_login1']}'    msg=Error message is not correct when fail to login with local user

    Log    \n-Login appliance with directory user    console=yes
    ${ad_login} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}
    Should be equal    '${ad_login[0]['status_code']}'    '400'   msg=Cannot login using username/password when enable smart card only login
    Should be equal    '${ad_login[0]['details']}'    '${errorMessages['Directory_login_error']}'    msg=Error message is not correct when fail to login with directory user

    ${auth} =  2FA Login
    should not be empty    ${auth}
    Disable smart card only login via curl    ${auth}    ${current_auth_body}
