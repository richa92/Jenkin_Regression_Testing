*** Settings ***
Documentation         Imports Rackmanager on OV and verifies refresh and remove operation
Library               FusionLibrary
Library               json
Library               RoboGalaxyLibrary
Resource            ../../../Resources/api/fusion_api_resource.txt
Variables             ov_variables.py
Suite Setup           Setup
Suite Teardown        Fusion Api Logout Appliance

*** Variables ***
${APPLIANCE_IP}         ${FUSION_IP}
${DATA_FILE}        ./data/ov_variables.py
&{admin_credentials}         userName=${FUSION_ADMIN_LOGIN}         password=${FUSION_ADMIN_PASSWORD}

*** Test Cases ***
Validate import operation on RMC
    [Documentation]    Validation of import operation on RMC
    ${task_response}=    Add RackManagers from variable    ${rmc_details}
    ${task_state}=    Get From Dictionary    ${task_response}    taskState
    Run Keyword If    '${task_state}' == 'Error'    FAIL   msg=${task_response['taskErrors'][0]['message']}

Validate refresh operation on RMC
    [Documentation]    Validation of normal refresh operation on RMC
    ${uri}=    Get RackManager URI
    ${task_response}=    Refresh Rack Manager    ${uri}
    ${get_state}=    Get Rack Manager State    ${uri}
    ${task_state}=    Get From Dictionary    ${task_response}    taskState
    Run Keyword If    '${task_state}' == 'Error'    FAIL    msg=${task_response['taskErrors'][0]['message']}

Validate remove operation on RMC
    [Documentation]    Validation of remove operation on RMC
    ${uri}=    Get RackManager URI
    ${task_response}=    Delete Rack Manager    ${uri}
    ${task_state}=    Get From Dictionary    ${task_response}    taskState
    Run Keyword If    '${task_state}' == 'Error'    FAIL    msg=${task_response['taskErrors'][0]['message']}

Validate force remove operation on RMC
    [Documentation]    Validation of force remove operation on RMC
    ${task_response}=    Add RackManagers from variable    ${rmc_details}
    ${uri}=    Get RackManager URI
    ${task_responses Force Delete Rack Manager    ${uri}    param=?force=True
    ${task_state}=    Get From Dictionary    ${task_response}    taskState
    Run Keyword If    '${task_state}' == 'Error'    FAIL    msg=${task_response['taskErrors'][0]['message']}

*** Keywords ***
Setup
    [Documentation]  Setup
    Set Log Level  TRACE
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}