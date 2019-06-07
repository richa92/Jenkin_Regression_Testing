*** Settings ***
Documentation         Cannot configure login message with more than 4500 characters
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
${login_message_item1}        message


*** Test Cases ***
Configure login message with more then 4500 characters
    [Documentation]    Cannot configure login message with more than 4500 characters
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${Edit_loginmessage_body} =  Get Global Setting Body With New Login Message    ${login_message_item1}    ${login_message['value2']}
    log     ${Edit_loginmessage_body}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${Edit_loginmessage_body}
    Should be equal    '${resp['status_code']}'    '400'    msg=Should not configure login message with more than 4500 characters
    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Login_message_error1']}'    msg=Show incorrect error message for configure login message with more than 4500 characters
    Fusion Api Logout Appliance
