*** Settings ***
Documentation        OV should change the external ca signed rabbtimq server cert to be internal-CA-signed one
...                  when change the ca signed appliance cert to be the self signed one
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
Check rabbitmq server cert when change appliance cert to be self signed one
    [Documentation]    OV should change the external ca signed rabbtimq server cert to be internal-CA-signed one
    ...                when change the ca signed appliance cert to be the self signed one
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Check whether the current appliance cert is the ca signed one    console=yes
    ${get_appliance_cert} =  Fusion Api Get Appliance Certificate
    Should Be Equal    '${get_appliance_cert['status_code']}'    '200'    msg=Fail to retrieve the appliance cert
    Should Not Be Equal    '${get_appliance_cert['commonName']}'    '${get_appliance_cert['issuer']}'    msg=The current applaince cert is not the ca signed one

    Log    \n-Get the current rabbitmq server cert    console=yes
    ${current_rabbitmq_server_cert} =  Run SSH CMD2    ${remote_server_IP}    ${APPLIANCE_IP}    ${ssh_cred}    ${cmd}
    Log    ${current_rabbitmq_server_cert}
    Should Not Contain    ${current_rabbitmq_server_cert}    ${internal_rabbitmq_server_cert_issuer}    msg=The current rabbitmq server cert is not signed by the external ca cert

    Log    \n-Generate new self signed appliance cert    console=yes
    ${web_server_body}=  Create Self Signed Web Server Certificate Body    ${basic_body}
    ${create_web_server_cert} =  Fusion Api Import Appliance Certificate    body=${web_server_body}
    Wait For Task2    ${Create_web_server_cert}    3min    5

    Fusion Api Logout Appliance

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Get the new rabbitmq server cert    console=yes
    ${new_rabbitmq_server_cert} =  Run SSH CMD2    ${remote_server_IP}    ${APPLIANCE_IP}    ${ssh_cred}    ${cmd}
    Log    ${new_rabbitmq_server_cert}

    Log    \n-Check whether the rabbitmq server is changed    console=yes
    Should Not Be Equal    ${new_rabbitmq_server_cert}    ${current_rabbitmq_server_cert}    msg=Rabbitmq server cert is not changed
    Should Contain    ${new_rabbitmq_server_cert}    ${internal_rabbitmq_server_cert_issuer}    msg=The rabbitmq server cert is not signed by the internal root ca cert
    Fusion Api Logout Appliance
