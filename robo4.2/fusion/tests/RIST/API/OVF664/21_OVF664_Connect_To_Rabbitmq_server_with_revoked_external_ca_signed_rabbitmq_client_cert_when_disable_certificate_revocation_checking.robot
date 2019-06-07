*** Settings ***
Documentation        Can connect to rabbitmq server with reovked extrernal ca signed rabbtimq client cert when disable certificate revocation checking
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
Connect To Rabbitmq server with revoked external ca signed rabbitmq client cert when disable certificate revocation checking
    [Documentation]    Can connect to rabbitmq server with reovked extrernal ca signed rabbtimq client cert when disable certificate revocation checking
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Disable certificate revocation checking    console=yes
    ${resp} =  Update Certificate Validation Configuration    ${disable_certificate_revocation_checking}
    Should Be True    ${resp}    msg=Fail to update certtificate validation configuration

    Fusion Api Logout Appliance

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Check whether the certificate revocation checking is disabled    console=yes
    ${get_validation_configuration} =  fusion api get certificate validation configuration
    Should Be Equal    '${get_validation_configuration['status_code']}'    '200'    msg=Fail to retrieve the current certificate validation configuration
    Should Be Equal    '${get_validation_configuration['certValidationConfig']['global.checkCertificateRevocation']}'    '${False}'    msg=Fail to disable certificate revocation checking

    Log    \n-Establish connection to rabbitmq server    console=yes
    ${handle} =  robot.libraries.Process.Start Process    python  ${CURDIR}\\SCMBListener.py  --ht  ${APPLIANCE_IP}  --li  \#    alias=scmb
    Sleep    2min

    ${resp} =  Handle Running Process    scmb
    Should Be True    ${resp}    msg=Fail to connect to rabbitmq server with correct client files

    Fusion Api Logout Appliance
