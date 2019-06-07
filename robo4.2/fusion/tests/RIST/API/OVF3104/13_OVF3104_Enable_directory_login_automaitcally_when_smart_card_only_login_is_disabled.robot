*** Settings ***
Documentation       Can enable directory login automaitcally when smart card only login is disabled
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
Enable directory login automaitcally when smart card only login is disabled
    [Documentation]    When smart card only login is enabled and then disabled , login based on ED credentials will be enabled automaticaill,
    ...                but local login and emergency login are still disabled
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}
    ${authenticaiton_body1} =  Update Authentication Body    ${enable_smart_card_only_login7}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body1}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to enable smart card only login
    Check Authentication Settings    ${authentication_item}    True

    ${authenticaiton_body2} =  Update Authentication Body    ${disable_smart_card_only_login}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body2}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to disable smart card only login
    Check Authentication Settings    ${authentication_item}    False

    Fusion Api Logout Appliance

    Log    \n-Login appliance with local user    console=yes
    ${local_login} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Should be equal    '${local_login[0]['status_code']}'    '400'    msg=Local login should not be enabled automatically when disable smart card only login
    Should be equal    '${local_login[0]['recommendedActions'][0]}'    '${errorMessages['Fail_Local_login1']}'    msg=Show incorrect error message when fail to login with local user

    Log    \n-Login appliance with directory user    console=yes
    ${ad_login} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}
    Should be equal    '${ad_login[0]['status_code']}'    '200'    msg=Fail to login with directroy user
    Fusion Api Logout Appliance