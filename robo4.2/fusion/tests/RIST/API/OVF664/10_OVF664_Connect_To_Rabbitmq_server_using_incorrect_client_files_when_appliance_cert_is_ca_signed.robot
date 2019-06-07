*** Settings ***
Documentation        Cannot connect to rabbitmq server using incorrect client files when appliance cert is ca signed one
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
Connect To Rabbitmq server using incorrect client files when appliance cert is ca signed one
    [Documentation]    When the appliance cert is the ca signed one, it cannot connect to rabbitmq server by using correct
    ...                internal ca signed rabbitmq client cert and its key and incorrect ca cert file
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Establish connection to rabbitmq server    console=yes
    ${handle} =  robot.libraries.Process.Start Process    python  ${CURDIR}\\SCMBListener.py  --ht  ${APPLIANCE_IP}  --li  \#    alias=scmb
    Sleep    2min

    Log    \n-Check whether the current process is stopped    console=yes
    ${resp} =  Run Keyword And Return Status    robot.libraries.Process.Process Should Be Stopped    scmb
    Should Be True    ${resp}    msg=Cannot connect to rabbitmq server with incorrect client cert

    Fusion Api Logout Appliance
