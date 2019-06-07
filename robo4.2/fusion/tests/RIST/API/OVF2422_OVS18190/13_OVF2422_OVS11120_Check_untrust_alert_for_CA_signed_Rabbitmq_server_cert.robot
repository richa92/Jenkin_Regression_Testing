*** Settings ***
Documentation        OV should send untrusted alert for CA signed web server cert when remove its parent CA certs
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              Process
Library              SSHLibrary
Library              String
Library              Dialogs
Library              BuiltIn
Library              json
Library              Collections
Resource             ./../../../../Resources/api/activity/tasks.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}


*** Variables ***


*** Test Cases ***
Check untrusted alert for CA signed web server cert
    [Documentation]    Should show untrusted alert for CA signed web server cert when remove its parent CA certs
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  Fusion Api Get Appliance Certificate
    Should Be Equal    '${resp['status_code']}'    '200'    msg=Fail to retrieve appliance certificate
    Should Not Be Empty    ${resp['base64Data']}    msg=Appliance certificate existed
    ${server_alert} =  Server Alert With Aliasname    ${resp['commonName']}    ${server_alerts['part4']}
    Check Alert    ${server_alert[1]}    ${alert_messages['Untrusted_Resolution']}
    Fusion Api Logout Appliance

