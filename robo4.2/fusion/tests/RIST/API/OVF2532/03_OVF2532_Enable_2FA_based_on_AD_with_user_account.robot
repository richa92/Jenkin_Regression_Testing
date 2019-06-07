*** Settings ***
Documentation        Cannot enabled 2FA based on AD with user account
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
Resource             ./../../../../Resources/api/activity/tasks.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}



*** Variables ***
${2FA_switch}    twoFactorAuthenticationEnabled


*** Test Cases ***
Enable 2FA based on AD with user account
    [Documentation]    Cannot enabled 2FA based on AD with user account
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${add_directory} =  Fusion Api Add Directory    ${user_ad}
    Should be equal    '${add_directory['status_code']}'    '201'    msg=Fail to add AD with user account to OV
    ${mappingrole} =  Fusion Api Assign Roles To Directory Group    ${userad_mapping_role}
    Wait For Task2    ${mappingrole}    2min    5
    ${authentication_body} =  Edit authentication switch    ${2FA_switch}    ${True}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authentication_body}
    Should be equal    '${resp['status_code']}'    '400'    msg=Shouldn't enable 2FA based on AD with user account
    Should be equal    '${resp['message']}'    '${TwoFA_errorMessages['Fail_Enable_2FA']}'    msg=Show incorrect error message when fail to enable 2FA based on AD with user account
    Fusion Api Logout Appliance
