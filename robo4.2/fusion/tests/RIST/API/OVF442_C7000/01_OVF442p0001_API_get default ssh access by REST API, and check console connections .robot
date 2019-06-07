*** Settings ***
Documentation        Get default ssh access by REST API, and check console connections

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt

Variables            ./Regression_Data.py

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
Get default ssh access by REST API, and check console connections
    [Documentation]  OVF442p0001- get default ssh access by REST API, and check console connections

    Log    \n- Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    - Get the ssh access from appliance    console=true
    ${resp}=  Get Appliance Ssh Access
    Should Be True                ${resp["allowSshAccess"]}
    Should Be Equal As Strings    ${resp["type"]}  SshAccess

    Log    Checking the maintenance console by ssh    console=true
    ${connected}=  Check Ssh To Console    ${APPLIANCE_IP}
    ...                                    ${CONSOLE_CREDENTIALS["username"]}
    ...                                    ${CONSOLE_CREDENTIALS["password"]}
    Should Be True                ${connected}

    Log    \n- Logging out OneView appliance    console=true
    Fusion Api Logout Appliance
