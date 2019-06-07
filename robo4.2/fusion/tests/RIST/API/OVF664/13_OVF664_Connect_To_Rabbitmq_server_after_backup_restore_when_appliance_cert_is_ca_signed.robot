*** Settings ***
Documentation        Can connect to rabbitmq server using correct client files after backup restore when appliance cert is ca signed one
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
Connect To Rabbitmq server after backup restore when appliance cert is ca signed one
    [Documentation]    When the appliance cert is the ca signed one, it can connect to rabbitmq server after backup restore by using correct
    ...                internal ca signed rabbitmq client cert and its key and internal root ca cert
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Import CA signed appliance cert    console=yes
    Set to Dictionary    ${ca_signed_appliance_cert}    base64Data    ${files_for_ca_signed_appliance_cert[2]}
    Log    ${ca_signed_appliance_cert}
    ${resp} =  Fusion Api Import Appliance Certificate    body=${ca_signed_appliance_cert}
    Wait For Task2    ${resp}    200    5
    Fusion Api Logout Appliance

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Get rabbitmq client cert and its key , and internal root CA cert to client side    console=yes
    ${resp} =  Get Client Files For Internal Ca Signed Rabbitmq Client Cert    ${files_for_ca_signed_appliance_cert[3]}
    Should Be True    ${resp}    msg=Fail to get client files for internal ca signed rabbitmq client cert

    Log    \n-Get current rabbitmq server cert    console=yes
    ${current_rabbitmq_server_cert} =  Run SSH CMD2    ${remote_server_IP}    ${APPLIANCE_IP}    ${ssh_cred}    ${cmd}
    Log    ${current_rabbitmq_server_cert}
    Should Not Contain    ${current_rabbitmq_server_cert}    ${internal_rabbitmq_server_cert_issuer}    msg=The current rabbitmq server cert is not signed by the external ca cert

    Log    \n-Establish connection to rabbitmq server    console=yes
    ${handle} =  robot.libraries.Process.Start Process    python  ${CURDIR}\\SCMBListener.py  --ht  ${APPLIANCE_IP}  --li  \#    alias=scmb
    Sleep    2min

    ${resp} =  Handle Running Process    scmb
    Should Be True    ${resp}    msg=Fail to connect to rabbitmq server with correct client files

    Log    \n-Create backup file    console=yes
    Create Backup

    Log    \n-Restore appliance    console=yes
    Restore Appliance

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Get the new rabbitmq server cert after backup restore    console=yes
    ${new_rabbitmq_server_cert} =  Run SSH CMD2    ${remote_server_IP}    ${APPLIANCE_IP}    ${ssh_cred}    ${cmd}
    Log    ${new_rabbitmq_server_cert}

    Log    \n-Check whether the rabbitmq server cert is changed    console=yes
    Should Not Be Equal    ${new_rabbitmq_server_cert}    ${current_rabbitmq_server_cert}    msg=The rabbitmq server cert is not changed
    Should Contain    ${new_rabbitmq_server_cert}    ${internal_rabbitmq_server_cert_issuer}    msg=The new rabbitmq server cert is signed by the internal root ca cert

    Log    \n-Get rabbitmq client cert and its key , and internal root CA cert to client side    console=yes
    ${resp} =  Get Client Files For Internal Ca Signed Rabbitmq Client Cert    ${files_for_ca_signed_appliance_cert[3]}
    Should Be True    ${resp}    msg=Fail to get client files for internal ca signed rabbitmq client cert

    Log    \n-Establish connection to rabbitmq server    console=yes
    ${handle} =  robot.libraries.Process.Start Process    python  ${CURDIR}\\SCMBListener.py  --ht  ${APPLIANCE_IP}  --li  \#    alias=scmb
    Sleep    2min

    ${resp} =  Handle Running Process    scmb
    Should Be True    ${resp}    msg=Fail to connect to rabbitmq server with correct client files

    Fusion Api Logout Appliance
