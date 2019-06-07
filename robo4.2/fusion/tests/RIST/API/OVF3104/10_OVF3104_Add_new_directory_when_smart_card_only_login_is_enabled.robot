*** Settings ***
Documentation       Can add new directory when smart card only login is enbaled
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
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ./keywords.txt
Variables           ${DATA_FILE}


*** Variables ***


*** Test Cases ***
Add new directory when smart card only login is enbaled
    [Documentation]    When smart card only login is enabled, Admin user can add new directory to appliance
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}

    Log    \n-Enable smart card only login    console=yes
    ${authenticaiton_body1} =  Update Authentication Body    ${enable_smart_card_only_login7}
    ${resp1} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body1}
    Should be equal    '${resp1['status_code']}'    '200'    msg=Fail to enable smart card only login

    Log    \n-Add new directory    console=yes
    ${resp2} =  Fusion Api Add Directory    ${user_ad}
    Wait For Task2    ${resp2}    300    5
    Should be equal    '${resp2['status_code']}'    '201'    msg=Fail to add new directory when smart card only login is enabled

    Log    \n-Disable smart card only login    console=yes
    ${authenticaiton_body2} =  Update Authentication Body    ${disable_smart_card_only_login}
    ${resp3} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body2}
    Should be equal    '${resp3['status_code']}'    '200'    msg=Fail to disable smart card only login

    Fusion Api Logout Appliance
