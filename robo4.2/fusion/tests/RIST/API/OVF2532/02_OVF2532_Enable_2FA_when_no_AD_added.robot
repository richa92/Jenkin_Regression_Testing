*** Settings ***
Documentation        Cannot enable 2FA when there is no directory added to appliance
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
${2FA_switch}    twoFactorAuthenticationEnabled
${cert_OID}    validationOids


*** Test Cases ***
Enable 2FA when no AD added
    [Documentation]    Cannot enable 2FA switch when there is no directory added to appliance
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${authentication_body} =  Edit authentication switch    ${2FA_switch}    ${True}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authentication_body}
    Should be equal    '${resp['status_code']}'    '400'    msg=Shouldn't enable 2FA without AD server
    Should be equal    '${resp['message']}'    '${TwoFA_errorMessages['Fail_Enable_2FA']}'    msg=Show incorrect error message when fail to enable 2FA without AD server
    Fusion Api Logout Appliance
