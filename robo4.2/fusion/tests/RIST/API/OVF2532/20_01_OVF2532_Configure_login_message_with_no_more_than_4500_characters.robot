*** Settings ***
Documentation         Can configure login message with no more than 4500 characters
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
${login_message_item2}       loginMessage']['message

*** Test Cases ***
Configure login message with no more then 4500 characters
    [Documentation]    Can configure login message with no more than 4500 characters
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${Edit_loginmessage_body} =  Get Global Setting Body With New Login Message    ${login_message_item1}    ${login_message['value1']}
    log     ${Edit_loginmessage_body}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${Edit_loginmessage_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to configura login message with no more than 4500 characters
    Check updated 2FA authentication settings    ${login_message_item2}    ${login_message['value1']}
    Fusion Api Logout Appliance