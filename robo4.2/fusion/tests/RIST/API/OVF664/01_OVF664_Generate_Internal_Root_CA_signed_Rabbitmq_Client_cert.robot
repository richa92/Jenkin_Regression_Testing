*** Settings ***
Documentation        OV should generate internal ca signed rabbitmq client certificate if not existed
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
Library              robot.libraries.Process
Resource             ./../../../../Resources/api/activity/tasks.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py

*** Variables ***
${rabbitmq_client_cert_param}    /default

*** Test Cases ***
Generate internal root ca signed rabbitmq client cert
    [Documentation]    OV should generate internal ca signed rabbitmq client cert if not existed
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  Fusion Api Get Rabbitmq Client Certificate    param=${rabbitmq_client_cert_param}
    Pass Execution If    '${resp['status_code']}'=='200'    Internal CA signed rabbitmq client cert is existred
    ${resp} =  Fusion Api Create Rabbitmq Client Certificate    ${rabbitmq_client_cert_body}
    Wait For Task2    ${resp}    2min    5
    ${resp} =  Fusion Api Get Rabbitmq Client Certificate    param=${rabbitmq_client_cert_param}
    Should Be Equal    '${resp['status_code']}'    '200'    msg=Fail to generate internal root ca signed rabbitmq client cert
    Should Not Be Empty    ${resp['base64SSLCertData']}    msg=Internal root ca signed rabbitmq client cert is generated failed
    Fusion Api Logout Appliance
