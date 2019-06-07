*** Settings ***
Documentation       Cannot disable local login when default directory is LOCAL
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
Disable Local Login With Local Directory
    [Documentation]    Cannot disable local login when default directory is LOCAL
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${authenticaiton_body} =  Update Authentication Body    ${disable_local_login2}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body}
    Should be equal    '${resp['status_code']}'    '400'    msg=Should not disable local login when default directory is LOCAL
    Should be equal    '${resp['details']}'    '${errorMessages['Fail_disable_local_login']}'    msg=Show incorrect error message for fail to disable local login when default directory is LOCAL
    Fusion Api Logout Appliance
