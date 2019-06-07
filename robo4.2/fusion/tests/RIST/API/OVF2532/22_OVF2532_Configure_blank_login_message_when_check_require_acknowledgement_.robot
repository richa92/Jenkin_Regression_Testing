*** Settings ***
Documentation         Cannot configure blank login message when check require acknowledgement
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
Configure blank login message when check require acknowledgement
    [Documentation]    Can configure blank login message when check require acknowledgement
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred_ack}
    ${Edit_loginmessage_body} =  Get Global Setting Body With New Login Message    ${login_message_item1}    ${login_message['value3']}
    log     ${Edit_loginmessage_body}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${Edit_loginmessage_body}
    Should be equal    '${resp['status_code']}'    '400'    msg=Cannot configure blank login message when check require acknowledgement
    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Blank_login_message']}'    msg=Show incorrect error message for fail to configure blank login message when check require acknowledgement

    ${Edit_loginmessage_body} =  Get Global Setting Body With New Login Message    ${login_message_item1}    ${login_message['value4']}
    log     ${Edit_loginmessage_body}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${Edit_loginmessage_body}
    Should be equal    '${resp['status_code']}'    '400'    msg=Cannot configure blank login message when check require acknowledgement
    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Blank_login_message']}'    msg=Show incorrect error message for fail to configure blank login message when check require acknowledgement

    Fusion Api Logout Appliance
