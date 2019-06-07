*** Settings ***
Documentation        OV should change the internal-CA-signed RabbitMQ server certificate to be the exrernal ca signed one
...                  when import ca signed appliance cert
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              Process
Library              SSHLibrary
Library              String
Library              robot.libraries.String
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
Check rabbitmq server cert when import ca signed appliance cert
    [Documentation]    When import ca signed appliance cert , the internal ca signed rabbitmq server cert will be changed to be the external ca signed one
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Get the internal ca signed rabbitmq server cert    console=yes
    ${current_rabbitmq_server_cert} =  Run SSH CMD2    ${remote_server_IP}    ${APPLIANCE_IP}    ${ssh_cred}    ${cmd}
    Log    ${current_rabbitmq_server_cert}
    Should Contain    ${current_rabbitmq_server_cert}    ${internal_rabbitmq_server_cert_issuer}    msg=The rabbitmq server cert is not signed by the internal root ca when using self signed appliance cert

    Log    \n-Add root CA certificate to OV    console=yes
    Set to Dictionary    ${ca_cert_body['members'][0]['certificateDetails']}    base64Data    ${files_for_ca_signed_appliance_cert[0]}
    Set to Dictionary    ${ca_cert_body['members'][0]['certificateDetails']}    aliasName    rootca
    Log    ${ca_cert_body}
    ${resp} =  Fusion Api Import External Ca Certificates    ${ca_cert_body}
    Wait For Task2    ${resp}    300    5

    Log    \n-Add intermediate CA certificate to OV    console=yes
    Set to Dictionary    ${ca_cert_body['members'][0]['certificateDetails']}    base64Data    ${files_for_ca_signed_appliance_cert[1]}
    Set to Dictionary    ${ca_cert_body['members'][0]['certificateDetails']}    aliasName    intermediateca
    Log    ${ca_cert_body}
    ${resp} =  Fusion Api Import External Ca Certificates    ${ca_cert_body}
    Wait For Task2    ${resp}    300    5

    Log    \n-Import CA signed appliance cert    console=yes
    Set to Dictionary    ${ca_signed_appliance_cert}    base64Data    ${files_for_ca_signed_appliance_cert[2]}
    Log    ${ca_signed_appliance_cert}
    ${resp} =  Fusion Api Import Appliance Certificate    body=${ca_signed_appliance_cert}
    Wait For Task2    ${resp}    300    5
    Fusion Api Logout Appliance

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Get the external ca signed rabbitmq server cert    console=yes
    ${new_rabbitmq_server_cert} =  Run SSH CMD2    ${remote_server_IP}    ${APPLIANCE_IP}    ${ssh_cred}    ${cmd}
    Log    ${new_rabbitmq_server_cert}

    Log    \n-Check whether the rabbitmq server cert is changed    console=yes
    Should Not Be Equal    ${new_rabbitmq_server_cert}    ${current_rabbitmq_server_cert}    msg=The rabbitmq server cert is not changed
    Should Not Contain    ${new_rabbitmq_server_cert}    ${internal_rabbitmq_server_cert_issuer}    msg=The new rabbitmq server cert is not signed by the external ca cert

    Fusion Api Logout Appliance
