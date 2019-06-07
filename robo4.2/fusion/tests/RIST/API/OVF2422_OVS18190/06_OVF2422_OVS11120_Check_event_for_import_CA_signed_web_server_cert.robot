*** Settings ***
Documentation        Check whether the event message for import ca signed web server cert is correct
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
Resource             ./../../../../Resources/api/settings/security.txt
Resource             ./keywords.txt
Variables            ../dto.py
Variables            ${DATA_FILE}


*** Variables ***
${CSRrootca_uri}    /rest/certificates/ca/CSRrootca

*** Test Cases ***
Check event for import CA signed web server cert
    [Documentation]    Check whether the event message for import ca signed web server cert is correct

    #${retrieve_appliance_cert} =  Fusion Api Get Appliance Certificate
    #Log    \nGenerate certificate signing request    console=Yes
    #${generate_CSR} =  Create appliance signing request    ${appliance_cert_csr_body}
    #log    ${generate_CSR}
    #${resp} =  Fusion Api Get Task    uri=${generate_CSR[1]}
    #Should be equal    '${resp['name']}'    '${alert_messages['Create_csr_Name']}'    msg=Show incorrect event for create appliance certificate signing request
    #Dictionary Should Contain Item    ${resp['progressUpdates'][0]}    statusUpdate    ${alert_messages['Create_csr_statusUpdate']}    msg=Show incorrect event for create appliance certificate signing request
    #${cert} =  Generate Appliance Certificate by CSR    ${retrieve_appliance_cert['commonName']}    ${generate_CSR[0]}    ${remote_server_IP}    ${remote_server_cred}
    #Log    ${cert}    console=Yes

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Set Log level    TRACE
    Log    \n-Add CSR root CA certificate to OV    console=yes
    Log    ${ca_csr_cert_body}
    Set to Dictionary    ${ca_csr_cert_body['members'][0]['certificateDetails']}    base64Data    ${all_related_certs[3]}
    ${add_CSRrootca} =  Fusion Api Import External Ca Certificates    ${ca_csr_cert_body}
    Wait For Task2    ${add_CSRrootca}    300    5
    ${retrieve_rootca} =  Run Keyword And Return Status    Fusion Api Get CA Certificate    ${CSRrootca_uri}
    Should Be Equal    '${retrieve_rootca}'    '${True}'    msg=Cannot find the CSR root CA certificate
    #${resp} =  Fusion Api Get Task    uri=${add_CSRrootca['uri']}
    ${resp} =  Fusion Api Get Task    uri=${add_CSRrootca${TASK_URI}}

    Log    \n-Add CA signed appliance certificate to OV    console=yes
    Set to Dictionary    ${ca_signed_appliance_cert}    base64Data    ${all_related_certs[2]}
    ${resp} =  Fusion Api Import Appliance Certificate    body=${ca_signed_appliance_cert}
    Wait For Task2    ${resp}    200    5    msg=Fail to import ca signed appliance cert
    #${resp} =  Fusion Api Get Task    uri=${resp['uri']}
    ${resp} =  Fusion Api Get Task    uri=${resp${TASK_URI}}
    Should be equal    '${resp['name']}'    '${alert_messages['Import_casinged_appliancecert_Name']}'    msg=Show incorrect event for importing CA-signed web server cert
    Dictionary Should Contain Item    ${resp['progressUpdates'][0]}    statusUpdate    ${alert_messages['Import_casinged_appliancecert']}    msg=Show incorrect event for importing CA-signed web server cert
    Fusion Api Logout Appliance