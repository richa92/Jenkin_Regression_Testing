*** Settings ***
Documentation        Can connect to rabbitmq server after backup restore when using external ca signed rabbitmq client cert
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
Connect To Rabbitmq server after backup restore when using external ca signed rabbitmq client cert
    [Documentation]    When using the external ca signed rabbitmq client cert, it can connect to rabbitmq server again after backup restore by using correct
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

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

    Log    \n-Establish connection to rabbitmq server    console=yes
    ${handle} =  robot.libraries.Process.Start Process    python  ${CURDIR}\\SCMBListener.py  --ht  ${APPLIANCE_IP}  --li  \#    alias=scmb
    Sleep    2min

    ${resp} =  Handle Running Process    scmb
    Should Be True    ${resp}    msg=Fail to connect to rabbitmq server with correct client files

    Fusion Api Logout Appliance
