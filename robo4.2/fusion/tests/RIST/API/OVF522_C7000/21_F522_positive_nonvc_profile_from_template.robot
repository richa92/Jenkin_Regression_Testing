*** Settings ***
Documentation   Positive tests: Create a template with a non-VC volume attachment and create a profile from it.

Library  	        BuiltIn
Library		        FusionLibrary
Library		        Collections
Library             json
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ./../global_variables.robot
Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Initialize the Variables and Log In
...                 AND     Set Suite Variable      ${WFT2_CONTINUE_ON_ERROR}   ${TRUE}

Suite Teardown      Run Keywords    Fusion Api Logout Appliance

*** Variables ***
${APPLIANCE_IP}     ${None}
${DATA_FILE}        ${None}

*** Test Cases ***
TS0 Create Server Profile Template
    ${resp} =    Add Server Profile Templates from variable  ${profile_templates}
    log to console  ${resp}
	Wait For Task2  ${resp}     timeout=2400    interval=2

TS1 Verify the Template
    Verify Server Profile Templates  ${profile_templates}

TS2 Create a Profile from the Template
    ${resps} =    Add Server Profiles from variable    ${create_profile}
	Wait for Task2  ${resps}  timeout=1500  interval=10

TS3 Verify the Profile
    Verify Server Profile  ${verify_profile_dto}

*** Keywords ***
Initialize the Variables and Log In
    [Documentation]  Set the log level to TRACE, log the variables and login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Validate Server Profile Applied Successfully
    [Arguments]    ${resps}
    [Documentation]    Validate Server Profile Applied Successfully
    :FOR    ${resp}    IN    @{resps}
    \    log to console   resp_is_${resp}
    \    ${task} =    Wait For Task    ${resp}    20min    5s
    \    ${taskState} =    Get From Dictionary    ${task}    taskState
    \    Should Match    ${taskState}    Completed
    \    ${taskUri} =    Get From Dictionary    ${task}    uri
    \    ${result} =    Validate Successfully Applied Server Settings For Profile     ${taskUri}
    \    Should Be True    ${result}

Validate Successfully Applied Server Settings For Profile
    [Arguments]    ${taskUri}
    [Documentation]    Validate Successfully Applied Server Settings For Profile
    ${task} =    Get Task By Param    param=?filter='parentTaskUri'='${taskUri}'&sort=created:descending&count=1
    ${status} =    Get From Dictionary    ${task}    taskStatus
    Log To Console    Create_Server_Profile_Task_Status_is:_${status}
    @{status_list} =    Split String    ${status}    :
    ${result_string} =    Get From List    ${status_list}    0
    ${profile_name} =    Get From List    ${status_list}    1
    Run Keyword If      '${result_string}'!='Successfully applied server settings for profile '
    ...                  FAIL   Profile failed to apply to server
    [Return]    True