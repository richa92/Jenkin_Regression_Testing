*** Settings ***
Documentation        Can configure SAN cert owner with duplicated values existed in SAN cert owner filed
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
Configure SAN certificate owner with duplicated values existed in SAN field
    [Documentation]    Can configure SAN cert owner with duplicated values existed in SAN cert owner filed
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${validation_body} =  Update 2FA validation values    ${SAN_certowner}    ${SAN_certowner_info3[0]}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to configure SAN cert owner with duplicated values
    Check updated 2FA validation configurations    ${SAN_certowner}    ${SAN_certowner_info3[1]}
    Fusion Api Logout Appliance
