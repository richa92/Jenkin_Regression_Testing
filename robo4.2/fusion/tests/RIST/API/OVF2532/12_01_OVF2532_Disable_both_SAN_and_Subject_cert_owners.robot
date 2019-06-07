*** Settings ***
Documentation        Cannnot disable both SAN and Subject cert owners
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
Resource             ./keywords.txt
Variables            ${DATA_FILE}


*** Variables ***
${SAN_certowner}    subjectAlternateNamePatterns
${Subject_certowner}    subjectPatterns


*** Test Cases ***
Disable both SAN and Subject cert owners
    [Documentation]    Disable SAN cert owner and Subject cert owner at the same time , it should fail
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${validation_body} =  Update 2FA Validation Values    ${SAN_certowner}    ${blank_list}
    Set To Dictionary    ${validation_body}    ${Subject_certowner}    ${blank_list}
    log    ${validation_body}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '400'    msg=Canot disable both SAN and Subject certificate owners
    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Disable_both_cert_owners']}'    msg=Show incorrect error message when fail to disbale both two cert owner options
    Fusion Api Logout Appliance
