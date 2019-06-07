*** Settings ***
Documentation        Cannot connect to rabbitmq server using incorrect client files when appliance cert is self signed one
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
Connect To Rabbitmq server using incorrect client files when appliance cert is self signed one
    [Documentation]    When the appliance cert is the self signed one, it cannot connect to rabbitmq server by using correct
    ...                internal ca signed rabbitmq client cert and its key and incorrect internal root ca cert
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Get rabbitmq client cert and its key , and internal root CA cert to client side    console=yes
    ${resp} =  Get Client Files For Internal Ca Signed Rabbitmq Client Cert    ${files_for_ca_signed_appliance_cert[3]}
    Should Be True    ${resp}    msg=Fail to get client files for internal ca signed rabbitmq client cert

    Log    \n-Change the rootca file in the client side    console=yes
    Remove File    ${CURDIR}/caroot.pem
    Create File    ${CURDIR}/caroot.pem    ${incorrect_rootca}

    Log    \n-Establish connection to rabbitmq server    console=yes
    ${handle} =  robot.libraries.Process.Start Process    python  ${CURDIR}\\SCMBListener.py  --ht  ${APPLIANCE_IP}  --li  \#    alias=scmb
    Sleep    2min

    Log    \n-Check whether the current process is stopped    console=yes
    ${resp} =  Run Keyword And Return Status    robot.libraries.Process.Process Should Be Stopped    scmb
    Should Be True    ${resp}    msg=Can establish connection to rabbitmq server with incorrect client files

    Fusion Api Logout Appliance
