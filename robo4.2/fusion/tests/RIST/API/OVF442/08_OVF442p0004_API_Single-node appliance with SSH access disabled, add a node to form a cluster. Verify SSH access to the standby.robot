*** Settings ***
Documentation        On a single-node appliance with SSH access disabled, add a node to form a cluster. Verify SSH access to the standby is unsuccessful
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
${name}      Jerry

*** Test Cases ***
On a single-node appliance with SSH access disabled, add a node to form a cluster. Verify SSH access to the standby is unsuccessful
    [Documentation]  OVF442p0004- On a single-node appliance with SSH access disabled, add a node to form a cluster.
    ...              Verify SSH access to the standby is unsuccessful
    Log    \n- Logging in OneView appliance
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Edit Ssh Access    ${enable_ssh_body}
    Config CIM iLo    ${APPLIANCE_IP}    ${MAINTENANCE_CREDENTIALS}
    Sleep    30s
    Ensure CIM Can be Ping Through

    Log    \n- Disable the ssh access from appliance
    ${resp}=  Get Appliance Ssh Access
    Run Keyword If                ${resp["allowSshAccess"]}==${True}    Edit Ssh Access  ${disable_ssh_body}

    Log    \n- Take the standby node online
    Power On HA Node And Wait For Success  ${CIM_HOSTS["standby"]}
    Wait For Appliance Became HA Cluster  role=Standby

    Log    \n- Getting the ssh access from appliance
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
