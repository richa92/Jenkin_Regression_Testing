*** Settings ***
Documentation        Can configure Subject cert owner with values existed in Subject field
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
Configure Subject certificate owner with values existed in Subject field
    [Documentation]    Configure Subject cert owner with correct values , it should success
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    :For    ${item}    In    @{Subject_certowner_info1}
    \    ${validation_body} =  Update 2FA Validation Values    ${Subject_certowner}    ${item}
    \    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    \    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to configure valid Subject certificate values
    \    Check updated 2FA validation configurations    ${Subject_certowner}    ${item}
    Fusion Api Logout Appliance
