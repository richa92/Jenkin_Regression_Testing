*** Settings ***
Documentation    Execute Rack Servers (DL) Actions
Resource                ../resource.txt

Variables                       ../Common.py
Variables                       ../${DATA_FILE}

Suite Setup                     QUAL Suite Setup    ${ADMIN_CREDENTIALS}
Suite Teardown                  QUAL Suite Teardown

*** Test Cases ***
Refresh Fabric
    [Tags]    TEST    65    REFRESH_FABRIC
    ${task} =    Refresh Fabric    ${FABRIC_NAME}
    Wait For Task2    ${task}    timeout=60    interval=5

Reapply Fabric
    [Tags]    TEST    65    REAPPLY_FABRIC
    ${task} =    Reapply Fabric    ${FABRIC_NAME}
    Wait For Task2    ${task}    timeout=60    interval=5
