*** Settings ***
Documentation        Disable SSH access on single-node. SSH connections to the appliance can not be connected

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
Disable SSH access on single-node. SSH connections to the appliance can not be connected
    [Documentation]  OVF442p0002- Disable SSH access on single-node. SSH connections to the appliance can not be connected

    Log    \n- Logging in OneView appliance
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n- Disable the ssh access from appliance
    Edit Ssh Access               ${disable_ssh_body}

    Log    \n- Get the ssh access from appliance
    ${resp}=  Get Appliance Ssh Access
    Should Not Be True            ${resp["allowSshAccess"]}

    Log    Checking the maintenance console by ssh
    ${connected}=   Check Ssh To Console    ${APPLIANCE_IP}
    ...                           ${MAINTENANCE_CREDENTIALS["username"]}
    ...                           ${MAINTENANCE_CREDENTIALS["password"]}
    Should Not Be True    ${connected}


    Log    Checking the serial console by ssh
    ${connected}=   Check Ssh To Console    ${APPLIANCE_IP}
    ...                           ${ADMIN_CREDENTIALS["userName"]}
    ...                           ${ADMIN_CREDENTIALS["password"]}
    Should Not Be True    ${connected}


    Log    \n- Logging out OneView appliance
    Fusion Api Logout Appliance