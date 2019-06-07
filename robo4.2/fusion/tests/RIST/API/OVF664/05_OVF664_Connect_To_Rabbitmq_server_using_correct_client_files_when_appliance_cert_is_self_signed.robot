*** Settings ***
Documentation        Can connect to rabbitmq server using correct client files when appliance cert is self signed one
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
Connect To Rabbitmq server using correct client files when appliance cert is self signed one
    [Documentation]    When the appliance cert is the self signed one, it can connect to rabbitmq server by using correct
    ...                internal ca signed rabbitmq client cert and its key and internal root ca cert
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Get rabbitmq client cert and its key , and internal root CA cert to client side    console=yes
    ${resp} =  Get Client Files For Internal Ca Signed Rabbitmq Client Cert    ${files_for_ca_signed_appliance_cert[3]}
    Should Be True    ${resp}    msg=Fail to get client files for internal ca signed rabbitmq client cert

    Log    \n-Establish connection to rabbitmq server    console=yes
    ${handle} =  robot.libraries.Process.Start Process    python  ${CURDIR}\\SCMBListener.py  --ht  ${APPLIANCE_IP}  --li  \#    alias=scmb
    Sleep    2min

    ${resp} =  Handle Running Process    scmb
    Should Be True    ${resp}    msg=Fail to connect to rabbitmq server with correct client files

    Fusion Api Logout Appliance
