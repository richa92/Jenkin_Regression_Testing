*** Settings ***
Documentation        Disable SSH access on a cluster. SSH connections to the standby can not be connected

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt

Variables            ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
Disable SSH access on a cluster. SSH connections to the standby can not be connected
    [Documentation]  OVF442p0003- Disable SSH access on a cluster. SSH connections to the standby can not be connected.robot

    Log    \n- Logging in OneView appliance
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    - Disable the ssh access from appliance
    Edit Ssh Access               ${disable_ssh_body}

    Log    - Get the ssh access from appliance
    ${resp}=  Get Appliance Ssh Access
    Should Not Be True            ${resp["allowSshAccess"]}

    Log    Checking the active maintenance console by ssh
    ${connected}=   Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["active"]}
    ...                           ${MAINTENANCE_CREDENTIALS["username"]}
    ...                           ${MAINTENANCE_CREDENTIALS["password"]}
    Should Not Be True    ${connected}

    Log    Checking the standby maintenance console by ssh
    ${connected}=   Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["standby"]}
    ...                           ${MAINTENANCE_CREDENTIALS["username"]}
    ...                           ${MAINTENANCE_CREDENTIALS["password"]}
    Should Not Be True    ${connected}

    Log    Checking the active serial console by ssh
    ${connected}=   Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["active"]}
    ...                           ${ADMIN_CREDENTIALS["userName"]}
    ...                           ${ADMIN_CREDENTIALS["password"]}
    Should Not Be True    ${connected}

    Log    Checking the standby serial console by ssh
    ${connected}=   Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["standby"]}
    ...                           ${ADMIN_CREDENTIALS["userName"]}
    ...                           ${ADMIN_CREDENTIALS["password"]}
    Should Not Be True    ${connected}

    Log    \n- Logging out OneView appliance
    Fusion Api Logout Appliance
