*** Settings ***
Documentation       Can enable local login manually when smart card only login is disabled
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
${authentication_item}    allowLocalLogin


*** Test Cases ***
Enable local login manually when smart card only login is disabled
    [Documentation]    when disable smart card only login , user can enable local login manually and it should work fine
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}
    ${authenticaiton_body} =  Update Authentication Body    ${enable_local_login}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to enable local login when smart card only login is disabled
    Check Authentication Settings    ${authentication_item}    True
    Fusion Api Logout Appliance

    Log    \n-Login appliance with administrator user    console=yes
    ${local_login1} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Should be equal    '${local_login1[0]['status_code']}'    '200'    msg=Fail to login with administrator user successfully
    Fusion Api Logout Appliance

    Log    \n-Login appliance with ordinary user    console=yes
    ${local_login2} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${ordinary_user}
    Should be equal    '${local_login2[0]['status_code']}'    '200'    msg=Fail to login with ordinary user successfully
    Fusion Api Logout Appliance
