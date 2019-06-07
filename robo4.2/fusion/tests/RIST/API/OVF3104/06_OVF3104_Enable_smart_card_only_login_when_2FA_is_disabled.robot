*** Settings ***
Documentation       Cannot enable smart card only login when 2FA is disabled
Library             FusionLibrary
Library             RoboGalaxyLibrary
Library             OperatingSystem
Library             Process
Library             SSHLibrary
Library             String
Library             Dialogs
Library             BuiltIn
Library             json
Library             Collections
Resource            ./keywords.txt
Variables           ${DATA_FILE}


*** Variables ***


*** Test Cases ***
Enable smart card only login when 2FA is disabled
    [Documentation]    When 2FA is disabled, it will fail to enable smart card only login
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${authenticaiton_body} =  Update Authentication Body    ${enable_smart_card_only_login6}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body}
    Should be equal    '${resp['status_code']}'    '400'    msg=Smart card only login cannot be enabled when two factor authentication is disabled
    Should be equal    '${resp['details']}'    '${errorMessages['Fail_Enable_2FA_only_login2']}'    msg=Error message is not correct when enable smart card only login failed.
    Fusion Api Logout Appliance