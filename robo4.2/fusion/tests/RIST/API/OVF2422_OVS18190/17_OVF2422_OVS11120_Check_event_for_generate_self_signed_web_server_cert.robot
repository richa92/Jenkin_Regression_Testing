*** Settings ***
Documentation        Should send correct event message for generate self singed web server cert
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
Check event for generate self signed web server cert
    [Documentation]    Check whether the event message for generate self signed web server cert is correct
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${current_webservercert} =  Fusion Api Get Appliance Certificate
    Should Not Be Empty    ${current_webserver_cert}
    ${web_server_body}=    Create Self Signed Web Server Certificate Body    ${basic_body}
    log    ${web_server_body}
    ${create_web_server_cert} =  Fusion Api Import Appliance Certificate    body=${web_server_body}
    Should be equal    '${create_web_server_cert['status_code']}'    '202'    msg=Fail to generate self signed web server cert
    Wait For Task2    ${Create_web_server_cert}    5min    5
    ${new_webservercert} =  Fusion Api Get Appliance Certificate
    Should Not Be Empty    ${new_webservercert['base64Data']}    msg=Cannot retrieve web server certificate
    Should Not Be Equal    '${current_webservercert['serialNumber']}'    '${new_webservercert['serialNumber']}'    msg=Web server certificate is not changed
    ${resp} =  Fusion Api Get Task    uri=${create_web_server_cert['uri']}
    Should be equal    '${resp['name']}'    '${alert_messages['Create_Selfsigned_Appliance_Cert_Name']}'    msg=Incorrect message for importing self-signed web server cert
    Dictionary Should Contain Item    ${resp['progressUpdates'][0]}    statusUpdate    ${alert_messages['Create_Selfsigned_Appliance_Cert']}
    Fusion Api Logout Appliance
