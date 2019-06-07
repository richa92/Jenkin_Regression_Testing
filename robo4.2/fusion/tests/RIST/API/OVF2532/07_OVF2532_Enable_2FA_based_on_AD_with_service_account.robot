*** Settings ***
Documentation        Can enable 2FA based on AD with service account
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
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}


*** Variables ***
${2FA_switch}    twoFactorAuthenticationEnabled

*** Test Cases ***
Enable 2FA based on AD with service account
    [Documentation]    Can enable 2FA based on AD with service account
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  Fusion Api Add Directory    ${service_ad}
    Should be equal    '${resp['status_code']}'    '201'    msg=Fail to Add AD with service account to OV
    ${mappingrole} =  Fusion Api Assign Roles To Directory Group    ${servicead_mapping_role}
    Wait For Task2    ${mappingrole}    2min    5
    ${authentication_body} =  Edit authentication switch    ${2FA_switch}    ${True}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authentication_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to enable 2FA
    Check updated 2FA authentication settings    ${2FA_switch}    True
    Fusion Api Logout Appliance
