*** Settings ***
Documentation         Cannot configure login message with invalid values
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
Configure login message with invalid values
    [Documentation]    Cannot configure login message with invalid values
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    :For    ${item}    IN    @{invalid_login_message}
    \    ${Edit_loginmessage_body} =  Get Global Setting Body With New Login Message    ${login_message_item1}    ${item}
    \    log     ${Edit_loginmessage_body}
    \    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${Edit_loginmessage_body}
    \    Should be equal    '${resp['status_code']}'    '400'    msg=Shouldn't configure login message with invalid characters
    \    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Login_message_error2']}'    msg=Show incorrect error message for configure login message with invalid characters
    Fusion Api Logout Appliance
