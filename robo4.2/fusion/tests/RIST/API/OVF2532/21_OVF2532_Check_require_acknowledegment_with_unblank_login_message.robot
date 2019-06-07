*** Settings ***
Documentation         Can check require acknowledgemnet with unblank login message
Library               FusionLibrary
Library               RoboGalaxyLibrary
Library               OperatingSystem
Library               Process
Library               SSHLibrary
Library               String
Library               Dialogs
Library               BuiltIn
Library               json
Library               Collections
Resource              ./keywords.txt
Variables             ${DATA_FILE}


*** Variables ***
${login_message_item1}        acknowledgment
${login_message_item2}       loginMessage']['acknowledgment

*** Test Cases ***
Check require acknowledgenment whit unblank login message
    [Documentation]    Can check require acknowledgemnet with unblank login message
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${Edit_loginmessage_body} =  Get Global Setting Body With New Login Message    ${login_message_item1}    ${True}
    log     ${Edit_loginmessage_body}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${Edit_loginmessage_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to check require acknowledgemnet with unblank login message
    Check updated 2FA authentication settings    ${login_message_item2}    ${True}
    Fusion Api Logout Appliance

    Log    \n-Local user login without ack permisson    console=yes
    ${resp} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    log    ${resp}
    Should be equal    '${resp[0]['status_code']}'    '400'    msg=Cannot login OV without ack permisson
    Should be equal    ${resp[0]['details']}    ${TwoFA_errorMessages['Fail_login_without_ack']}    msg=Show incorrect error message for fail to login OV without ack permisson

     Log    \n-Local user login with ack permisson    console=yes
    ${resp} =  Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred_ack}
    Should be equal    '${resp[0]['status_code']}'    '200'    msg=Fail to login OV with ack permisson
