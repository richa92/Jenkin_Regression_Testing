*** Settings ***
Documentation        Can connect to rabbitmq server with correct extrernal ca signed rabbtimq client cert
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
Connect To Rabbitmq server with correct extrernal ca signed rabbitmq client cert
    [Documentation]    Can connect to rabbitmq server with correct extrernal ca signed rabbtimq client cert
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Get the internal root ca cert    console=yes
    ${internal_rootca_cert} =  Fusion Api Get Ca Certificate    param=Infrastructure Management Certificate Authority-internalroot
    Should Be Equal    '${internal_rootca_cert['status_code']}'    '200'    msg=Fail to get internal root ca cert

    Log    \n-Get the client files for external ca signed rabbitmq client cert    console=yes
    ${resp} =  Change Client Files For External Ca Signed Rabbitmq Client Cert    ${client_files[0]}    ${client_files[1]}    ${internal_rootca_cert['certificateDetails']['base64Data']}    ${client_files[3]}
    Should Be True    ${resp}    msg=Fail to get client files for external ca signed rabbitmq client cert

    Log    \n-Establish connection to rabbitmq server    console=yes
    ${handle} =  robot.libraries.Process.Start Process    python  ${CURDIR}\\SCMBListener.py  --ht  ${APPLIANCE_IP}  --li  \#    alias=scmb
    Sleep    2min

    ${resp} =  Handle Running Process    scmb
    Should Be True    ${resp}    msg=Fail to connect to rabbitmq server with correct client files

    Fusion Api Logout Appliance
