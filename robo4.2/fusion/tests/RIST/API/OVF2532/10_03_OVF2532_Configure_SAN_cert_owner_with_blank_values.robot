*** Settings ***
Documentation        Cannot configure SAN cert owner with blank values
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
Configure SAN certificate owenr with blank values
    [Documentation]    Set SAN certificate owner with blank values, it should fail
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    :For    ${item}    In    @{blank_values_list}
    \    ${validation_body} =  Update 2FA validation values    ${SAN_certowner}    ${item}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '400'    msg=Cannot configure blank certificate owner pattern.
    \    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Empty_SAN_cert_owner_error']}'    msg=Show incorrect error message for configure blank certificate owner pattern
    Fusion Api Logout Appliance