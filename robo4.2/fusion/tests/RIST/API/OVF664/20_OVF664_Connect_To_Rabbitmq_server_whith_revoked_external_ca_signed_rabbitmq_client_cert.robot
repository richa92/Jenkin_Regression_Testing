*** Settings ***
Documentation        Cannot connect to rabbitmq server when extrernal ca signed rabbtimq client cert is revoked
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
${external_rootca_uri}        /rest/certificates/ca/external_rootca

*** Test Cases ***
Connect To Rabbitmq server with revoked extrernal ca signed rabbitmq client cert
    [Documentation]    Cannot connect to rabbitmq server when extrernal ca signed rabbtimq client cert is revoked
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Check whether the external root ca cert is existed    console=yes
    ${external_rootca} =  Fusion Api Get Ca Certificate    ${external_rootca_uri}
    Should Be Equal    '${external_rootca['status_code']}'    '200'    msg=Fail to retrieve CA cert that signed rabbitmq client cert

    Log    \n-Upload the crl to revoke external ca signed rabbitmq client cert    console=yes
    ${upload_crl} =  Fusion Api Upload Crl By Aliasname    external_rootca    ${CURDIR}/revoke_rabbitmqclientcert.crl
    Should Be Equal    '${upload_crl['status_code']}'    '202'    msg=upload crl file to external_rootca fail

    Log    \n-Establish connection to rabbitmq server    console=yes
    ${handle} =  robot.libraries.Process.Start Process    python  ${CURDIR}\\SCMBListener.py  --ht  ${APPLIANCE_IP}  --li  \#    alias=scmb
    Sleep    2min

    Log    \n-Check whether the current process is stopped    console=yes
    ${resp} =  Run Keyword And Return Status    robot.libraries.Process.Process Should Be Stopped    scmb
    Should Be True    ${resp}    msg=Can establish connection to rabbitmq server with revoked external ca signed rabbitmq client cert

    Fusion Api Logout Appliance
