*** Settings ***
Documentation        OV should send revoked alert for external CA signed rabbitmq server cert
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
${CSRrootca_uri}    /rest/certificates/ca/CSRrootca

*** Test Cases ***
Check revoked alert for external CA signed rabbtimq server cert
    [Documentation]    Should show revoked alert for external CA signed rabbtimq server cert
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${get_appliance_cert} =  Fusion Api Get Appliance Certificate
    Should Not Be Equal    ${get_appliance_cert['commonName']}    ${get_appliance_cert['issuer']}    msg=The current appliance cert is self-signed
    ${server_alert} =  Server Alert With Aliasname    ${get_appliance_cert['commonName']}    ${server_alerts['part3']}
    Check Alert    ${server_alert[1]}    ${alert_messages['Revoked_Resolution']}

    Log    \n-Removing Revoked CSR root CA certificate to OV    console=yes
    ${resp} =  Fusion Api Remove External CA Certificates    CSRrootca
    Should Be Equal    '${resp['status_code']}'    '202'    msg=Fail to remove root CA cert
    Wait For Task2    ${resp}    2min    5

    Log    \n-Add valid CSR root CA certificate to OV    console=yes
    Log    ${ca_csr_cert_body}
    Set to Dictionary    ${ca_csr_cert_body['members'][0]['certificateDetails']}    base64Data    ${all_related_certs[3]}
    ${add_CSRrootca} =  Fusion Api Import External Ca Certificates    ${ca_csr_cert_body}
    Wait For Task2    ${add_CSRrootca}    300    5
    ${retrieve_rootca} =  Run Keyword And Return Status    Fusion Api Get CA Certificate    ${CSRrootca_uri}
    Should Be Equal    '${retrieve_rootca}'    '${True}'    msg=Cannot find the CSR root CA certificate
    ${resp} =  Fusion Api Get Task    uri=${add_CSRrootca${TASK_URI}}
    Fusion Api Logout Appliance
