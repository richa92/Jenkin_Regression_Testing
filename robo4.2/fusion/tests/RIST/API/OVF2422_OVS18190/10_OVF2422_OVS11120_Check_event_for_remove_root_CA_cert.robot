*** Settings ***
Documentation        Should show correct event message for remove root CA cert
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
Check event for remove root CA cert
    [Documentation]    Check whether the event message for remove root CA cert is correct
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  Fusion Api Remove External CA Certificates    rootca
    Should Be Equal    '${resp['status_code']}'    '202'    msg=Fail to remove root CA cert
    Wait For Task2    ${resp}    2min    5
    ${get_cert} =  Fusion Api Get CA Certificate    ${rootca_uri}
    Should Be Equal    '${get_cert['status_code']}'    '404'    msg=Fail to retrieve root CA cert
    Should Be Equal    ${get_cert['message']}    ${CA_cert_error}    msg=Cannot find root CA cert
    ${resp} =  Fusion Api Get Task    uri=${resp${TASK_URI}}
    Should Be Equal    '${resp['name']}'    '${alert_messages['Remove_Cert_Name']}'    msg=Incorrect message for removing root CA cert
    Dictionary Should Contain Item    ${resp['progressUpdates'][0]}    statusUpdate    ${alert_messages['Remove_root_CA']}
    Fusion Api Logout Appliance
