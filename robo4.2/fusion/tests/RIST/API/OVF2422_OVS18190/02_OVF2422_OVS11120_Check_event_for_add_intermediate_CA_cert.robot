*** Settings ***
Documentation        OV should send correct event message for add intermediate CA cert
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
Variables            ../dto.py
Variables            ${DATA_FILE}


*** Variables ***
${intermediateca_uri}    /rest/certificates/ca/intermediateca

*** Test Cases ***
Check event for add intermediate CA cert
    [Documentation]    Check whether the event for add intermediate CA cert is correct
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Set to Dictionary    ${ca_cert_body['members'][0]['certificateDetails']}    base64Data    ${all_related_certs[1]}
    Set to Dictionary    ${ca_cert_body['members'][0]['certificateDetails']}    aliasName    intermediateca
    Log    ${ca_cert_body}
    ${add_intermediateca} =  Fusion Api Import External Ca Certificates    ${ca_cert_body}
    Wait For Task2    ${add_intermediateca}    300    5
    ${retrieve_intermediateca} =  Run Keyword And Return Status    Fusion Api Get CA Certificate    ${intermediateca_uri}
    Should Be Equal    '${retrieve_intermediateca}'    '${True}'    msg=Cannot find the intermediate CA certificate
    ${resp} =  Fusion Api Get Task    uri=${add_intermediateca${TASK_URI}}
    Should be equal    '${resp['name']}'    '${alert_messages['Add_Cert_Name']}'    msg=Incorrect message for adding intermediate CA cert
    Dictionary Should Contain Item    ${resp['progressUpdates'][0]}    statusUpdate    ${alert_messages['Add_CA_Cert']}
    Fusion Api Logout Appliance
