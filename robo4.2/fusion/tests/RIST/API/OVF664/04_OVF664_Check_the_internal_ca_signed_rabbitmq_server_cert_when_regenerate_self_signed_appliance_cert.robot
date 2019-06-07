*** Settings ***
Documentation        Cannot change internal-CA-signed RabbitMQ server certificate when regenerate the self signed appliance cert,
...                  and cannot be changed when create new self signed appliance cert
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

    Log    \n-Get current rabbitmq server cert before create self signed appliance cert    console=yes
    ${rabbitmq_server_cert1} =  Run SSH CMD2    ${remote_server_IP}    ${APPLIANCE_IP}    ${ssh_cred}    ${cmd}
    Log    ${rabbitmq_server_cert1}
    Should Contain    ${rabbitmq_server_cert1}    ${internal_rabbitmq_server_cert_issuer}    msg=The rabbitmq server cert is not signed by the internal root ca when using self signed appliance cert

    Log    \n-Regenerate new self signed appliance cert    console=yes
    ${web_server_body}=  Create Self Signed Web Server Certificate Body    ${basic_body}
    ${create_web_server_cert} =  Fusion Api Import Appliance Certificate    body=${web_server_body}
    Wait For Task2    ${Create_web_server_cert}    3min    5

    Fusion Api Logout Appliance

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Get current rabbitmq server cert after create self signed appliance cert    console=yes
    ${rabbitmq_server_cert2} =  Run SSH CMD2    ${remote_server_IP}    ${APPLIANCE_IP}    ${ssh_cred}    ${cmd}
    Log    ${rabbitmq_server_cert2}

    Log    \n-Check whether the rabbitmq server cert is changed    console=yes
    Should Contain    ${rabbitmq_server_cert2}    ${internal_rabbitmq_server_cert_issuer}    msg=The rabbitmq server cert is not signed by the internal root ca when using self signed appliance cert
    Should Be Equal    ${rabbitmq_server_cert1}    ${rabbitmq_server_cert2}    msg=The internal ca signed rabbitmq server cert is changed after regenerate self signed appliance cert

    Fusion Api Logout Appliance
