*** Settings ***
Documentation        OV should send correct event message for add root CA cert
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
${rootca_uri}    /rest/certificates/ca/rootca

*** Test Cases ***
Check event for add root CA cert
    [Documentation]    Check whether the event for add root CA cert is correct
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Log    \n-Add root CA certificate to OV    console=yes
    Set to Dictionary    ${ca_cert_body['members'][0]['certificateDetails']}    base64Data    ${all_related_certs[0]}
    Set to Dictionary    ${ca_cert_body['members'][0]['certificateDetails']}    aliasName    rootca
    Log    ${ca_cert_body}
    ${add_rootca} =  Fusion Api Import External Ca Certificates    ${ca_cert_body}
    Wait For Task2    ${add_rootca}    300    5
    ${retrieve_rootca} =  Run Keyword And Return Status    Fusion Api Get CA Certificate    ${rootca_uri}
    Should Be Equal    '${retrieve_rootca}'    '${True}'    msg=Cannot find the root CA certificate
    ${resp} =  Fusion Api Get Task    uri=${add_rootca${TASK_URI}}
    Should be equal    '${resp['name']}'    '${alert_messages['Add_Cert_Name']}'    msg=Incorrect message for adding root CA cert
    Dictionary Should Contain Item    ${resp['progressUpdates'][0]}    statusUpdate    ${alert_messages['Add_CA_Cert']}
    Fusion Api Logout Appliance
