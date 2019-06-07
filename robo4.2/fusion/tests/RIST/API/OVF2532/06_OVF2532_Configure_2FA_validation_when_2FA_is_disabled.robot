*** Settings ***
Documentation         Cannot configure 2FA validations when 2FA is disabled
Library               FusionLibrary
Library               RoboGalaxyLibrary
Library               OperatingSystem
Library               Process
Library               SSHLibrary
Library               String
Library               Dialogs
Library               BuiltIn
Library               json
Library               Collections
Resource              ./keywords.txt
Variables             ${DATA_FILE}


*** Variables ***
${2FA_switch}    twoFactorAuthenticationEnabled
${cert_OID}    validationOids


*** Test Cases ***
Configure 2FA validation when 2FA is disabled
    [Documentation]    Cannot configure 2FA validations when 2FA is disabled
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${validation_body} =  Update 2FA Validation Values    ${cert_OID}    ${OIDs[3:4]}
    ${resp} =  Fusion Api Edit Login Domains Login Certificates    ${validation_body}
    Should be equal    '${resp['status_code']}'    '404'    msg=Shouldn't configure 2FA validation when 2FA is disabled
    Should be equal    '${resp['details']}'    '${TwoFA_errorMessages['Fail_edit_2FA']}'    msg=Show incorrect error message for fail to configure 2FA validation when 2FA disabled
    Fusion Api Logout Appliance
