*** Settings ***
Library        FusionLibrary
Library        RoboGalaxyLibrary
Library        OperatingSystem
Library        Process
Library        SSHLibrary
Library        String
Library        robot.libraries.DateTime
Library        Dialogs
Library        BuiltIn
Library        json
Library        Collections
Resource       ./../../../../Resources/api/fusion_api_resource.txt
Resource       ./keywords.txt
Variables      ./Regression_Data.py

Suite Setup  Setup EVN before test
Suite Teardown  Clear EVN

*** Variables ***
${APPLIANCE_IP}        ${None}    #leave it as ${None} if you want this test to create a new one
${rabbitmq_client_cert_param}    /default


*** Keywords ***
Setup EVN before test
    [Documentation]    Setup evn before SCMB test
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Create self-signed appliance cert to make sure the current rabbitmq server cert is signed by internal root ca    console=yes
    ${web_server_body}=  Create Self Signed Web Server Certificate Body    ${basic_body}
    ${create_web_server_cert} =  Fusion Api Import Appliance Certificate    body=${web_server_body}
    Wait For Task2    ${Create_web_server_cert}    3min    5

    Fusion Api Logout Appliance

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Check the latest cert status to make sure the current appliance cert is valid    console=yes
    Wait Until Keyword Succeeds    5min    5s    Fusion Api Get Certificate Status

    Log    \n-Add at least 308 CA certs and leaf certs to appliance    console=yes
    Add Plenty Certs To OV    ${remote_server_IP}    ${ssh_cred}    96    221

    Log    \n-Create ca signed aplpliance cert in the remote server    console=yes
    ${generate_CSR} =  Generate Certificate Signing Request    ${appliance_cert_csr_body}
    ${create_appliance_cert} =  Get Certs Generated In Linux     ${generate_CSR}
    log    ${create_appliance_cert}
    Set Global Variable    ${files_for_ca_signed_appliance_cert}    ${create_appliance_cert}

    Log    \n-Get client files for external ca signed rabbitmq client cert    console=yes
    ${files_for_external_ca_signed_rabbitmq_client_cert} =  Get Client Files For External Ca Signed Rabbitmq Client Cert
    Set Global Variable    ${client_files}    ${files_for_external_ca_signed_rabbitmq_client_cert}

    Fusion Api Logout Appliance

Clear EVN
    [Documentation]    Clear data after test
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Enable certificate revocation checking    console=yes
    Update Certificate Validation Configuration    ${enable_certificate_revocation_checking}

    Fusion Api Logout Appliance

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Reset appliance cert to be the valid self signed one    console=yes
    ${web_server_body}=  Create Self Signed Web Server Certificate Body    ${basic_body}
    ${create_web_server_cert} =  Fusion Api Import Appliance Certificate    body=${web_server_body}
    Wait For Task2    ${Create_web_server_cert}    3min    5

    Fusion Api Logout Appliance

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Check the latest cert status to clear related cert alert    console=yes
    Wait Until Keyword Succeeds    5min    5s    Fusion Api Get Certificate Status

    Log    \n-Remove the external root CA used to signed rabbitmq client cert    console=yes
    ${resp} =  Fusion Api Remove External Ca Certificates    external_rootca
    Wait For Task2    ${resp}    3min    5

    Log    \n-Remove the CA certs used to signed appliance cert    console=yes
    ${resp} =  Fusion Api Remove External Ca Certificates    rootca
    Wait For Task2    ${resp}    3min    5
    ${resp} =  Fusion Api Remove External Ca Certificates    intermediateca
    Wait For Task2    ${resp}    3min    5

    Log    \n-Remove the generated files    console=yes
    OperatingSystem.Remove Files    ${CURDIR}/caroot.pem    ${CURDIR}/client.pem    ${CURDIR}/key.pem    ${CURDIR}/revoke_rabbitmqclientcert.crl

    Log    \n-Clear the data generated in the remote server    console=yes
    Clean EVN in Linux    ${remote_server_IP}    ${ssh_cred}

    Remove Plenty Certs From OV    96    221

    Fusion Api Logout Appliance
