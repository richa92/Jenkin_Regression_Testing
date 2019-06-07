*** Settings ***
Documentation        Remove the standby node, verify SSH access to the former standby is successful

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
Remove the standby node, verify SSH access to the former standby is successful
    [Documentation]  OVF442p0005 - On a clustered appliance with SSH access disabled, remove the standby node,
    ...              verify SSH access to the former standby is successful.

    Log    \n- Logging in OneView appliance
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n- Disable the ssh access from appliance
    ${resp}=  Get Appliance Ssh Access
    Run Keyword If                ${resp["allowSshAccess"]}==${True}    Edit Ssh Access  ${disable_ssh_body}

    Remove Standby Node from HA Nodes

     Log    \n- Getting the ssh access from appliance
    ${resp}=  Get Appliance Ssh Access
    Should Not Be True            ${resp["allowSshAccess"]}

    Log    Checking the active maintenance console by ssh
    ${connected}=   Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["active"]}
    ...                           ${MAINTENANCE_CREDENTIALS["username"]}
    ...                           ${MAINTENANCE_CREDENTIALS["password"]}
    Should Not Be True    ${connected}

    Log    Checking the active serial console by ssh
    ${connected}=   Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["active"]}
    ...                           ${ADMIN_CREDENTIALS["userName"]}
    ...                           ${ADMIN_CREDENTIALS["password"]}
    Should Not Be True    ${connected}

    Log    \n- Logging out OneView appliance
    Fusion Api Logout Appliance
