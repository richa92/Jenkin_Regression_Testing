*** Settings ***
Documentation       Cannot set smart card only login to be null
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
Set smart card only login to be null
    [Documentation]    it will fail to configure smart card only login with null
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}
    ${authenticaiton_body} =  Update Authentication Body    ${invalid_smart_card_only_login}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body}
    Should be equal    '${resp['status_code']}'    '400'    msg=Cannot set smart card only login to be null
    Should be equal    '${resp['details']}'    '${errorMessages['Null_smart_card_only_login_error']}'    msg=Error message is not correct for set smart card only login to be null
    Fusion Api Logout Appliance