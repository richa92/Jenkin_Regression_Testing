*** Settings ***
Documentation        Check whether the event message for generate internal ca signed rabbitmq client cert is correct
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
Check event for generate internal ca signed rabbitmq client cert
    [Documentation]    Should show event for generate internal ca signed rabbitmq client cert
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  Fusion Api Get Rabbitmq Client Certificate    /default
    Pass Execution If    '${resp['status_code']}'=='200'    rabbitmq client cert is already existed
    ${resp} =  Fusion Api Create Rabbitmq Client Certificate    ${rabbitmq_client_cert_body}
    Wait For Task2    ${resp}    2min    5
    ${task_info} =  Fusion Api Get Task    uri=${resp['headers']['Location']}
    Should Be Equal    '${task_info['name']}'    '${alert_messages['Create_rabbitmq_client_cert']}'    msg=Show incorrect event for crate internal ca signed rabbitmq client cert
    Dictionary Should Contain Item    ${task_info['progressUpdates'][0]}    statusUpdate    ${alert_messages['Create_rabbitmq_client_cert_details']}
    Fusion Api Logout Appliance