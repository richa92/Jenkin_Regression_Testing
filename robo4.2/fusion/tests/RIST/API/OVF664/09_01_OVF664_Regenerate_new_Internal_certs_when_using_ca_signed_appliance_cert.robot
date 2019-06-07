*** Settings ***
Documentation        OV should regenerate new internal root ca cert , internal ca signed rabbitmq client cert
...                  excepet rabbitmq server cert vai Delete /rest/certificates/ca/default when using ca signed appliance cert
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
${regenerate_new_internal_certs_param}    default

*** Test Cases ***
Regenerate new internal certs when using ca signed appliance cert
    [Documentation]    When the appliance cert is the ca signed one, OV should regenerate new internal root ca cert
    ...               and internal root ca signed rabbitmq client cert except rabbitmq server cert
    ...               when run Delete /rest/certificates/ca/default
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Check whether the current appliance cert is the ca signed one    console=yes
    ${resp} =  fusion api get appliance certificate
    Should Be Equal    '${resp['status_code']}'    '200'    msg=Fail to retrieve the appliance cert
    Should Not Be Equal    '${resp['commonName']}'    '${resp['issuer']}'    msg=The current applaince cert is not the ca signed one

    Log    \n-Get the current internal ca signed rabbitmq client cert and its key, rabbitmq server cert and internal root ca cert    console=yes
    ${current_rabbitmq_internalRootCA_certs} =  Get Rabbitmq Certs And Internal Root CA    ${rabbitmq_client_cert_param}    ${internal_root_ca_param}
    Log    ${current_rabbitmq_internalRootCA_certs}

    Log    \n-Regenerate new internal certs via Delete /rest/certificates/ca/default    console=yes
    ${resp} =  Fusion Api Remove External Ca Certificates    aliasName=${regenerate_new_internal_certs_param}
    Should Be Equal    '${resp['status_code']}'    '204'    msg=Fail to regenerate new internal certs

    Log    \n-Get the new internal certs    console=yes
    ${new_rabbitmq_internalRootCA_certs} =  Get Rabbitmq Certs And Internal Root CA    ${rabbitmq_client_cert_param}    ${internal_root_ca_param}
    Log    ${new_rabbitmq_internalRootCA_certs}

    Log    \n-Check whether the related certs are changed    console=yes
    ${resp} =  Check Changed Rabbitmq Certs    ${new_rabbitmq_internalRootCA_certs}    ${current_rabbitmq_internalRootCA_certs}    3
    Should Be True    ${resp}    mag=Fail to regenerate new certs after running Delete /rest/certificates/ca/default
    Should Be Equal    ${new_rabbitmq_internalRootCA_certs[3]}    ${current_rabbitmq_internalRootCA_certs[3]}    msg=External ca signed rabbtimq server cert is changed

    Fusion Api Logout Appliance