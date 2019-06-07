*** Settings ***
Documentation         Can configure blank login message when uncheck require acknowledgement
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
${login_message_item3}        message
${login_message_item4}       loginMessage']['message



*** Test Cases ***
Configure blank login message when uncheck require acknowledgement
    [Documentation]    Can configure blank login message when uncheck require acknowledgement
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred_ack}

    Log    \n-Uncheck require acknowledgement when login message is not blank    console=yes
    ${Edit_loginmessage_body} =  Get Global Setting Body With New Login Message    ${login_message_item1}    ${False}
    log     ${Edit_loginmessage_body}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${Edit_loginmessage_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to uncheck require acknowledgemnet with unblank login message
    Check updated 2FA authentication settings    ${login_message_item2}    ${False}

    Log    \n-Configure blank login message when uncheck require acknowledgement    console=yes
    ${Edit_loginmessage_body} =  Get Global Setting Body With New Login Message    ${login_message_item3}    ${login_message['value3']}
    log     ${Edit_loginmessage_body}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${Edit_loginmessage_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to configure blank login message when uncheck require acknowledgement
    Check updated 2FA authentication settings    ${login_message_item4}    ${login_message['value3']}

    Log    \n-Configure blank login message when uncheck require acknowledgement    console=yes
    ${Edit_loginmessage_body} =  Get Global Setting Body With New Login Message    ${login_message_item3}    ${login_message['value4']}
    log     ${Edit_loginmessage_body}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${Edit_loginmessage_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to configure blank login message when uncheck require acknowledgement
    Check updated 2FA authentication settings    ${login_message_item4}    ${login_message['value3']}

    Fusion Api Logout Appliance
