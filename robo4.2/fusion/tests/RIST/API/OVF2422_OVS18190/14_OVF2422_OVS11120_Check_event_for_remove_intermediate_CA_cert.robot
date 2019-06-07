*** Settings ***
Documentation        Should show correct event message for remove intermediate CA cert
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
Check event for remove intermediate CA cert
    [Documentation]    Check whether the event message for remove intermediate CA cert is correct
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  Fusion Api Remove External CA Certificates    intermediateca
    Should Be Equal    '${resp['status_code']}'    '202'    msg=Fail to remove intermediate CA cert
    Wait For Task2    ${resp}    2min    5
    ${get_cert} =  Fusion Api Get CA Certificate    ${intermediateca_uri}
    Should Be Equal    '${get_cert['status_code']}'    '404'    msg=Fail to retrieve intermediate CA cert
    Should Be Equal    ${get_cert['message']}    ${CA_cert_error}    msg=Cannot find intermediate CA cert
    ${resp} =  Fusion Api Get Task    uri=${resp${TASK_URI}}
    Should Be Equal    '${resp['name']}'    '${alert_messages['Remove_Cert_Name']}'    msg=Incorrect message for removing intermediate CA cert
    Dictionary Should Contain Item    ${resp['progressUpdates'][0]}    statusUpdate    ${alert_messages['Remove_intermediate_CA']}
    Fusion Api Logout Appliance
