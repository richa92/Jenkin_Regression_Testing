*** Settings ***
Documentation         Show correct default 2FA validation configurations
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


*** Test Cases ***
Check default 2FA validation configurations
    [Documentation]    Check default 2FA validation configurations when 2FA is enabled
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${resp} =  fusion api get login domains global settings
    Log    ${resp}
    Remove From Dictionary    ${resp['loginMessage']}    eTag    created    modified
    Remove From Dictionary    ${resp['defaultLoginDomain']}    eTag    created    modified
    Remove From Dictionary    ${resp}    headers    status_code
    Dictionaries Should Be Equal    ${resp}    ${default_login_domains_global_settings}
    Fusion Api Logout Appliance
