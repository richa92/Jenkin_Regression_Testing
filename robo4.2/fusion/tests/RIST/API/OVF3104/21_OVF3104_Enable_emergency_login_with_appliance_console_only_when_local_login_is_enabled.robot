*** Settings ***
Documentation       Cannot enable emergency login with appliance console only when local login is enabled
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
Enable emergency login with appliance console only when local login is enabled
    [Documentation]    When local login is enabled , it will fail to enable emergency login with appliance console only
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${authenticaiton_body} =  Update Authentication Body    ${enable_emergency_login1}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body}
    Should be equal    '${resp['status_code']}'    '400'    msg=Cannot enable emergency login with appliance console only when local login is enabled
    Should be equal    '${resp['details']}'    '${errorMessages['Fail_Enable_Emergency_Login']}'    msg=Error message is not correct when fail to enable emergency login with appliance console only
    Fusion Api Logout Appliance
