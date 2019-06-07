*** Settings ***
Documentation       Retrieve correct login details when smart card only login is enabled
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
Resource            ./../../../../Resources/api/common/common.txt
Resource            ./keywords.txt
Variables           ${DATA_FILE}


*** Variables ***
${authentication_item}    strictTwoFactorAuthentication

*** Test Cases ***
Retrieve login details when smart card only login is enabled
    [Documentation]    Can retrieve login details correctly when smart card only login is enabled
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${AD_user}

    Log    \n-Enable smart card only login    console=yes
    ${authenticaiton_body} =  Update Authentication Body    ${enable_smart_card_only_login7}
    ${resp} =  Fusion Api Edit Login Domains Global Settings    ${authenticaiton_body}
    Should be equal    '${resp['status_code']}'    '200'    msg=Fail to enable smart card only login
    Check Authentication Settings    ${authentication_item}    True

    Log    \n-Retrieve login details    console=yes
    ${login_details} =  Fusion Api Get Login Details
    Should be equal    '${login_details['status_code']}'    '200'    msg=Fail to retrieve correct login details
    Should be equal    '${login_details['${authentication_item}']}'    'True'    msg=Fail to retrieve incorrect smart card only login status
    Fusion Api Logout Appliance

    ${auth} =  2FA Login
    should not be empty    ${auth}
    Disable smart card only login via curl    ${auth}    ${current_auth_body}
