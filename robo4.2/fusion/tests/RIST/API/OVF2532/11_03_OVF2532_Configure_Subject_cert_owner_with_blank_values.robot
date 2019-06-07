*** Settings ***
Documentation       Cannot configure Subject cert owner with blank values
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
${Subject_certowner}    subjectPatterns


*** Test Cases ***
Configure Subject certificate owenr with blank values
    [Documentation]    Configure Subject cert owner with blank values , it should fail
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    :For    ${item}    In    @{blank_values_list}
    \    ${validation_body} =  Update 2FA Validation Values    ${Subject_certowner}    ${item}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '400'    msg=Shouldn't configure blank certificate owner pattern.
    \    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Empty_Subject_cert_owner_error']}'    msg=Show incorrect error message when configure blank certificate owner pattern
    Fusion Api Logout Appliance
