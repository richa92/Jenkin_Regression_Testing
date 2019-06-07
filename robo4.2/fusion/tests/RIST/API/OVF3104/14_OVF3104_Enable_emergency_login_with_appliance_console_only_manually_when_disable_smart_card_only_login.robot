*** Settings ***
Documentation       Can enable emergency login with appliance console only manually when smart card only login is disabled
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
${authentication_item1}    emergencyLocalLoginEnabled
${authentication_item2}    emergencyLocalLoginType
${emergency_type}          APPLIANCE_CONSOLE_ONLY

*** Test Cases ***
Enable emergency login with appliance console only manually when smart card only login is disabled
    [Documentation]      when disable smart card only login , user can enable emergency login with appliance console manually
    ...                  and it should work fine
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}
    ${authenticaiton_body} =  Update Authentication Body    ${enable_emergency_login1}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to enable emergency login with appliance console only manually when smart card only login is disabled
    Check Authentication Settings    ${authentication_item1}    True
    Check Authentication Settings    ${authentication_item2}    ${emergency_type}
    Fusion Api Logout Appliance

    Log    \n-Login appliance with emergency user    console=yes
    ${local_login} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Should be equal    '${local_login[0]['status_code']}'    '400'    msg=Cannot login using local user when enable emergency local login
    Should be equal    '${local_login[0]['details']}'    '${errorMessages['Fail_Local_login2']}'    msg=Error message is not correct when fail to login with emergency user

    Log    \n-Login appliance with ordinary user    console=yes
    ${local_login2} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${ordinary_user}
    Should be equal    '${local_login2[0]['status_code']}'    '400'    msg=Cannot login with ordinary user when enable emergency login with appliance console only manually
    Should be equal    '${local_login2[0]['details']}'    '${errorMessages['Fail_Local_login2']}'    msg=Show incorrect error message when fail to login with noemergency user

    Log    \n-Login appliance with directory user    console=yes
    ${ad_login} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}
    Should be equal    '${ad_login[0]['status_code']}'    '200'    msg=Fail to login with directroy user
    Fusion Api Logout Appliance