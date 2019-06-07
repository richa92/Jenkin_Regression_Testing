*** Settings ***
Documentation   Assgin Server Profiles to Server Hardware from the data in the variable file

Resource        ../../../../Resources/api/fusion_api_resource.txt

Suite Setup       Run Keywords    Set Log Level    DEBUG
...               AND    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
...               AND    Power off ALL Servers
Suite Teardown    Fusion Api Logout Appliance

*** Test Cases ***
OVF2458 Assign Server Profiles to Server Hardware
    [Documentation]    Assign Server Profiles to Server Hardware and check for failures
   	[Tags]    Performance    server_profiles-condition-everything
    [Setup]                           Run Keyword and Ignore Error    Write To ciDebug Log
    ${server_profile_to_bay_map} =    Get Variable Value    ${server_profile_to_bay_map}
    ${tasks} =                        Run Keyword If   ${server_profile_to_bay_map} is not ${null}    Assign Server Hardware To Existing Profiles From Variable    ${server_profile_to_bay_map}
    Validate Task List                ${tasks}
    [Teardown]                        Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

*** Keywords ***
Assign Server Hardware To Existing Profiles From Variable
	[Documentation]	Update Server Profiles with server hardware assigned to profile from mapping variable
	[Arguments]    ${server_profile_to_bay_map}    ${concurrent_profiles}=24

	${existing_profiles} =    Fusion Api Get Server Profiles
    ${all_task_list} =    Create List
    ${these_assign_list} =    Create List
	:FOR    ${profile}    IN    @{existing_profiles['members']}
	\    Run Keyword If    '${profile['serverHardwareUri']}' != '${NULL}'    Log    ${profile['name']} is already assigned...skipping
	\    Continue For Loop If    '${profile['serverHardwareUri']}' != '${NULL}'
    \    Continue For Loop If   '${server_profile_to_bay_map['${profile['name']}']}' == '${null}'
	\	 ${shUri} = 	Get Server Hardware URI    ${server_profile_to_bay_map['${profile['name']}']}
	\    Set To Dictionary    ${profile}   serverHardwareUri=${shUri}
    \    Remove From Dictionary    ${profile}   status_code    headers
    \	 Log    Assigning server hardware URI \"${shUri}\" to profile \"${profile['name']}\"   console=True
    \    ${resp} =   Fusion Api Edit Server Profile    uri=${profile['uri']}   body=${profile}    param=?ignoreServerHealth=true
    \    Append To List    ${all_task_list}    ${resp}
    \    Append To List    ${these_assign_list}    ${resp}
    \    ${assigning} =    Get Length    ${these_assign_list}
    \    Run Keyword If    ${assigning}==${concurrent_profiles}    Wait For Assigning    ${these_assign_list}
    \    ${these_assign_list} =    Run Keyword If    ${assigning}==${concurrent_profiles}    Create List    ELSE    Set Variable    ${these_assign_list}

    # were there any not waited on?
    ${assigning} =    Get Length    ${these_assign_list}
    Run Keyword If    ${assigning}>0    Wait For Assigning    ${these_assign_list}

    [Return]   ${all_task_list}

Wait For Assigning
    [Documentation]     Wait For Assigning
    [Arguments]    ${tasks}    ${timeout}=45m    ${interval}=30
    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}    # so WFT2 processes all tasks, not stop on failure.
    Wait for Task2    ${tasks}    ${timeout}    ${interval}

Get Errors
    [Documentation]    Get Errors
    ${ERRORS} =   Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}