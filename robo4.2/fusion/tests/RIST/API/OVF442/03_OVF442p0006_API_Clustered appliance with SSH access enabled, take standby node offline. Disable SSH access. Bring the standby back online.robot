*** Settings ***
Documentation        Take the standby node offline. Disable SSH access. Bring the standby back online. Verify SSH access to the standby is unsuccessful

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
Take the standby node offline. Disable SSH access. Bring the standby back online. Verify SSH access to the standby is unsuccessful
    [Documentation]  OVF442p0006- Take the standby node offline. Disable SSH access. Bring the standby back online. Verify SSH access to the standby is unsuccessful

    Log    \n- Logging in OneView appliance
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n- Enable the ssh access before testing
    Edit Ssh Access               ${enable_ssh_body}

    Log    \n- Get the ssh access from appliance
    ${resp}=  Get Appliance Ssh Access
    Should Be True                ${resp["allowSshAccess"]}

    Log    Checking the active maintenance console by ssh
    ${connected}=  Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["active"]}
    ...                                    ${MAINTENANCE_CREDENTIALS["username"]}
    ...                                    ${MAINTENANCE_CREDENTIALS["password"]}
    Should Be True                ${connected}

    Log    Checking the standby maintenance console by ssh
    ${connected}=  Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["standby"]}
    ...                                    ${MAINTENANCE_CREDENTIALS["username"]}
    ...                                    ${MAINTENANCE_CREDENTIALS["password"]}
    Should Be True                ${connected}

    Log    Checking the active serial console by ssh
    ${connected}=  Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["active"]}
    ...                                    ${ADMIN_CREDENTIALS["userName"]}
    ...                                    ${ADMIN_CREDENTIALS["password"]}
    Should Be True    ${connected}

    Log    Checking the standby serial console by ssh
    ${connected}=  Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["standby"]}
    ...                                    ${ADMIN_CREDENTIALS["userName"]}
    ...                                    ${ADMIN_CREDENTIALS["password"]}
    Should Not Be True    ${connected}

    Log    Take the standby node offline
    Power Off HA Node And Wait For Success  ${CIM_HOSTS["standby"]}

    Log    \n- Enable the ssh access before testing
    Edit Ssh Access               ${disable_ssh_body}

    Log    \n- Get the ssh access from appliance
    ${resp}=  Get Appliance Ssh Access
    Should Not Be True            ${resp["allowSshAccess"]}

    Log    \n- Take the standby node online
    Power On HA Node And Wait For Success  ${CIM_HOSTS["standby"]}
    Wait For Appliance Became HA Cluster  role=Standby

    Log    \n- Checking the active maintenance console by ssh
    ${connected}=   Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["active"]}
    ...                           ${MAINTENANCE_CREDENTIALS["username"]}
    ...                           ${MAINTENANCE_CREDENTIALS["password"]}
    Should Not Be True    ${connected}

    Log    \n- Checking the standby maintenance console by ssh
    ${connected}=   Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["standby"]}
    ...                           ${MAINTENANCE_CREDENTIALS["username"]}
    ...                           ${MAINTENANCE_CREDENTIALS["password"]}
    Should Not Be True    ${connected}

    Log    \n- Checking the active serial console by ssh
    ${connected}=   Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["active"]}
    ...                           ${ADMIN_CREDENTIALS["userName"]}
    ...                           ${ADMIN_CREDENTIALS["password"]}
    Should Not Be True    ${connected}

    Log    \n- Checking the standby serial console by ssh
    ${connected}=  Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["standby"]}
    ...                           ${ADMIN_CREDENTIALS["userName"]}
    ...                           ${ADMIN_CREDENTIALS["password"]}
    Should Not Be True    ${connected}

    Log    \n- Logging out OneView appliance
    Fusion Api Logout Appliance
