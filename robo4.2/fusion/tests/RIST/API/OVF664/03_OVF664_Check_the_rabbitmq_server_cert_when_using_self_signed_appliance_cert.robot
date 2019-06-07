*** Settings ***
Documentation        OV should has an internal-CA-signed RabbitMQ server certificate when the appliance cert is the self signed one
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


*** Test Cases ***
Check rabbitmq server cert when using self signed appliance cert
    [Documentation]    When the appliance cert is the self signed one, the rabbitmq server cert should be signed by the internal root ca
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  fusion api get appliance certificate
    Should Be Equal    '${resp['status_code']}'    '200'    msg=Fail to retrieve the appliance cert
    Should Be Equal    '${resp['commonName']}'    '${resp['issuer']}'    msg=The current applaince cert is not the self signed one

    ${rabbitmq_server_cert} =  Run SSH CMD2    ${remote_server_IP}    ${APPLIANCE_IP}    ${ssh_cred}    ${cmd}
    Log    ${rabbitmq_server_cert}
    Should Contain    ${rabbitmq_server_cert}    ${internal_rabbitmq_server_cert_issuer}    msg=The rabbitmq server cert is not signed by the internal root ca when using self signed appliance cert

    Fusion Api Logout Appliance
