*** Settings ***
Documentation        Can configure SAN cert owner with correct values
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


*** Test Cases ***
Configure SAN certificate owner with values existed in SAN field
    [Documentation]    Set SAN certificate owner with correct values, it should success
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    :For    ${item}    In    @{SAN_certowner_info1}
    \    ${validation_body} =  Update 2FA validation values    ${SAN_certowner}    ${item}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to configure SAN cert owner
    \    Check updated 2FA validation configurations    ${SAN_certowner}    ${item}
    Fusion Api Logout Appliance
