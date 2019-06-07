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
${CSRrootca_uri}    /rest/certificates/ca/CSRrootca

*** Test Cases ***
Check untrusted alert for CA signed web server cert
    [Documentation]    Should show untrusted alert for CA signed web server cert when remove its parent CA certs
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  Fusion Api Remove External CA Certificates    CSRrootca
    Should Be Equal    '${resp['status_code']}'    '202'    msg=Fail to remove root CA cert
    Wait For Task2    ${resp}    2min    5
  #  ${resp} =  Fusion Api Remove External CA Certificates    HP TestHead Certificate Authority
  #  Should Be Equal    '${resp['status_code']}'    '202'    msg=Fail to remove CA cert named HP TestHead Certificate Authority
  #  Wait For Task2    ${resp}    2min    5

    ${resp} =  Fusion Api Get Appliance Certificate
    Should Be Equal    '${resp['status_code']}'    '200'    msg=Fail to retrieve appliance certificate
    Should Not Be Empty    ${resp['base64Data']}    msg=Appliance certificate existed
    ${server_alert} =  Server Alert With Aliasname    ${resp['commonName']}    ${server_alerts['part4']}
    Check Alert    ${server_alert[0]}    ${alert_messages['Untrusted_Resolution']}

    Fusion Api Logout Appliance
