*** Settings ***
Documentation        Can edit 2FA validation when 2FA is enabled
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
Configure 2FA validation when 2FA is enabled
    [Documentation]    Can edit 2FA validaton when 2FA is enabled
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${validation_body} =  Update 2FA Validation Values    ${Subject_certowner}    ${Subject_certowner_info1[0]}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    log    ${resp}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to configure 2FA validation when 2FA enabled
    Check updated 2FA validation configurations    ${Subject_certowner}    ${Subject_certowner_info1[0]}
    Fusion Api Logout Appliance
