*** Settings ***
Documentation       Can change service credentials when smart card only login is enabled
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
Change service credentials when smart card only login is enabled
    [Documentation]    When smart card only login is enabled, Admin user can edit directory services credentials
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Enable smart card only login    console=yes
    ${authenticaiton_body1} =  Update Authentication Body    ${enable_smart_card_only_login7}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body1}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to enable smart card only login

    Log    \n-Change service credentials for AD server    console=yes
    ${resp} =  Fusion Api Edit Directory    ${change_ad}    ${resp['defaultLoginDomain']['uri']}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to change service credentials

    Log    \n-Disable smart card only login    console=yes
    ${authenticaiton_body2} =  Update Authentication Body    ${disable_smart_card_only_login}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body2}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to disable smart card only login
    Fusion Api Logout Appliance