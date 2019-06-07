*** Settings ***
Documentation        Check whether the event message for create appliance signing request is correct
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
Variables            ${DATA_FILE}


*** Variables ***

*** Test Cases ***
Check event for creat appliance signing request
    [Documentation]    Check whether the event message for create appliance signing request is correct
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Log    \nGenerate certificate signing request    console=Yes
    ${generate_CSR} =  Create appliance signing request    ${appliance_cert_csr_body}
    log    ${generate_CSR}
    ${resp} =  Fusion Api Get Task    uri=${generate_CSR[1]}
    Should be equal    '${resp['name']}'    '${alert_messages['Create_csr_Name']}'    msg=Show incorrect event for create appliance certificate signing request
    Dictionary Should Contain Item    ${resp['progressUpdates'][0]}    statusUpdate    ${alert_messages['Create_csr_statusUpdate']}    msg=Show incorrect event for create appliance certificate signing request
    Fusion Api Logout Appliance