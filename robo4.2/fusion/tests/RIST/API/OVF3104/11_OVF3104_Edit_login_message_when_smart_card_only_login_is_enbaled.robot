*** Settings ***
Documentation       Can edit login message when smart card only login is enabled
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
${authentication_item1}    loginMessage']['acknowledgment
${authentication_item2}    loginMessage']['message


*** Test Cases ***
Edit login message when smart card only login is enabled
    [Documentation]    When smart card only login is enabled , it will success to edit login message
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}

    Log    \n-Edit login message    console=yes
    ${authenticaiton_body} =  Update Authentication Body    ${edit_login_message1}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to edit login message when smart card only login is enabled
    Check Authentication Settings    ${authentication_item1}    True
    Check Authentication Settings    ${authentication_item2}    ${edit_login_message1['loginMessage']['message']}

    Log    \n-Reset login message    console=yes
    ${authenticaiton_body} =  Update Authentication Body    ${reset_login_message}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to reset login message
    Check Authentication Settings    ${authentication_item1}    False
    Check Authentication Settings    ${authentication_item2}    ${reset_login_message['loginMessage']['message']}

    Fusion Api Logout Appliance