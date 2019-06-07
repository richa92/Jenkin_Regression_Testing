*** Settings ***
Documentation        On a single-node appliance with SSH access enabled, perform a backup. Disable SSH access. Restore from backup. Verify SSH access is successful
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
On a single-node appliance with SSH access enabled, perform a backup. Disable SSH access. Restore from backup. Verify SSH access is successful
    [Documentation]  OVF442p0009- On a single-node appliance with SSH access enabled, perform a backup. Disable SSH access. Restore from backup. Verify SSH access is successful

    Log    \n- Logging in OneView appliance
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.209.231'
    ${resp}  ${session}=    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    log to console  ${session}

    Log    \n- Enable the ssh access from appliance
    Edit Ssh Access               ${enable_ssh_body}

    Log    \n- Get the ssh access from appliance
    ${resp}=  Get Appliance Ssh Access
    Should Be True                ${resp["allowSshAccess"]}

    Log    \n- Checking the maintenance console by ssh
    ${connected}=  Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["active"]}
    ...                                    ${MAINTENANCE_CREDENTIALS["username"]}
    ...                                    ${MAINTENANCE_CREDENTIALS["password"]}
    Should Be True                ${connected}

    Log    \n- Checking the serial console by ssh
    ${connected}=  Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["active"]}
    ...                                    ${ADMIN_CREDENTIALS["userName"]}
    ...                                    ${ADMIN_CREDENTIALS["password"]}
    Should Be True    ${connected}

    Log    \n- Backup the appliance
    Create Backup

    Log    \n- Disable the ssh access from appliance
    Edit Ssh Access               ${disable_ssh_body}

    Log    \n- Get the ssh access from appliance
    ${resp}=  Get Appliance Ssh Access
    Should Not Be True            ${resp["allowSshAccess"]}

    Log    \n- Checking the maintenance console by ssh
    ${connected}=   Check Ssh To Console    ${APPLIANCE_IP}
    ...                           ${MAINTENANCE_CREDENTIALS["username"]}
    ...                           ${MAINTENANCE_CREDENTIALS["password"]}
    Should Not Be True    ${connected}

    Log    \n- Checking the serial console by ssh
    ${connected}=   Check Ssh To Console    ${APPLIANCE_IP}
    ...                           ${ADMIN_CREDENTIALS["userName"]}
    ...                           ${ADMIN_CREDENTIALS["password"]}
    Should Not Be True    ${connected}

    Log    \n- Restore the appliance from backup
    Restore Appliance

    Log    \n- Checking the maintenance console by ssh
    ${connected}=  Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["active"]}
    ...                                    ${MAINTENANCE_CREDENTIALS["username"]}
    ...                                    ${MAINTENANCE_CREDENTIALS["password"]}
    Should Be True                ${connected}

    Log    \n- Checking the serial console by ssh
    ${connected}=  Check Ssh To Console    ${MAINTENANCE_CREDENTIALS["host"]["active"]}
    ...                                    ${ADMIN_CREDENTIALS["userName"]}
    ...                                    ${ADMIN_CREDENTIALS["password"]}
    Should Be True    ${connected}

    Log    \n- Get the ssh access from appliance
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    ${resp}=  Get Appliance Ssh Access
    Should Be True                ${resp["allowSshAccess"]}

    Log    \n- Logging out OneView appliance
    Fusion Api Logout Appliance
