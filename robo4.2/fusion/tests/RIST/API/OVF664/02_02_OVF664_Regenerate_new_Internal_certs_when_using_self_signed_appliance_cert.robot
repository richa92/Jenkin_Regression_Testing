*** Settings ***
Documentation        OV should regenerate new internal root ca cert , internal ca signed rabbitmq client cert
...                  and internal ca signed rabbitmq server cert via Delete /rest/certificates/ca/default when
...                  the appliance cert is the self signed one
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
${rabbitmq_client_cert_param}    /keypair/default
${internal_root_ca_param}        Infrastructure Management Certificate Authority-internalroot
${regenerate_new_internal_certs_param}    rabbitmq_readonly

*** Test Cases ***
Regenerate new internal certs when using self signed appliance cert
    [Documentation]    When the appliance cert is the self signed one, OV should regenerate new internal root ca cert
    ...               and internal root ca signed rabbitmq client cert and rabbitmq server cert that signed by the internal root ca
    ...               when run Delete /rest/certificates/ca/rabbitmq_readonly
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Check whether the current appliance cert is the self signed one    console=yes
    ${resp} =  fusion api get appliance certificate
    Should Be Equal    '${resp['status_code']}'    '200'    msg=Fail to retrieve the appliance cert
    Should Be Equal    '${resp['commonName']}'    '${resp['issuer']}'    msg=The current applaince cert is not the self signed one

    Log    \n-Get the current internal ca signed rabbitmq client cert and its key , internal ca signed rabbitmq server cert and internal root ca cert    console=yes
    ${current_rabbitmq_internalRootCA_certs} =  Get Rabbitmq Certs And Internal Root CA    ${rabbitmq_client_cert_param}    ${internal_root_ca_param}
    Log    ${current_rabbitmq_internalRootCA_certs}

    Log    \n-Regenerate new internal root ca cert , internal ca signed rabbitmq client cert and rabbitmq server cert via Delete /rest/certificates/ca/rabbitmq_readonly    console=yes
    ${resp} =  Fusion Api Remove External Ca Certificates    aliasName=${regenerate_new_internal_certs_param}
    Should Be Equal    '${resp['status_code']}'    '204'    msg=Fail to regenerate new internal certs

    Log    \n-Get the new internal ca signed rabbitmq client cert and its key , internal ca signed rabbitmq server cert and internal root ca cert    console=yes
    ${new_rabbitmq_internalRootCA_certs} =  Get Rabbitmq Certs And Internal Root CA    ${rabbitmq_client_cert_param}    ${internal_root_ca_param}
    Log    ${new_rabbitmq_internalRootCA_certs}

    Log    \n-Check whether the related certs are changed    console=yes
    ${resp} =  Check Changed Rabbitmq Certs    ${new_rabbitmq_internalRootCA_certs}    ${current_rabbitmq_internalRootCA_certs}    4
    Should Be True    ${resp}    mag=Fail to regenerate new certs after running Delete /rest/certificates/ca/rabbitmq_readonly
    Fusion Api Logout Appliance
