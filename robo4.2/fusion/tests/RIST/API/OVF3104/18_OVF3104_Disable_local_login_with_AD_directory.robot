*** Settings ***
Documentation       Can disable local login when default directory is AD directory
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
${local_login_item}    allowLocalLogin

*** Test Cases ***
Disable Local Login With AD Directory
    [Documentation]    Can disable local login when default directory is AD directory
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}
    ${authenticaiton_body} =  Update Authentication Body    ${disable_local_login1}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to disable local login when default directory is not LOCAL
    Check Authentication Settings    ${local_login_item}    False
    Fusion Api Logout Appliance

    Log    \n-Login appliance with local user    console=yes
    ${local_login} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Should be equal    '${local_login[0]['status_code']}'    '400'    msg=Cannot login using local user when disable local login
    Should be equal    '${local_login[0]['details']}'    '${errorMessages['Fail_Local_login2']}'    msg=Error message is not correct when fail to login with local user user

    Log    \n-Login appliance with directory user    console=yes
    ${ad_login} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}
    Should be equal    '${ad_login[0]['status_code']}'    '200'    msg=Fail to login with directroy user
    Fusion Api Logout Appliance