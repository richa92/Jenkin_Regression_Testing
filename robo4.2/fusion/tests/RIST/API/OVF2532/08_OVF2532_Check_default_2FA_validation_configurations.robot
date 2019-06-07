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
    ${resp} =  Fusion Api Get Login Domains Login Certificates
    Remove From Dictionary    ${resp}    eTag    created    headers    modified    status_code
    Dictionaries Should Be Equal    ${resp}    ${default_2FA_validation}
    Fusion Api Logout Appliance
