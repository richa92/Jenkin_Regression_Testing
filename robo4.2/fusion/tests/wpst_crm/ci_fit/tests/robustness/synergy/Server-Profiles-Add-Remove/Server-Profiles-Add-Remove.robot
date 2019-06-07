*** Settings ***
Documentation        Create and remove server profiles
...                  This script will use the data variable file from the setup script to create and remove the server profiles.
...                  Example:
...                          time pybot -d /tmp/logs/Server-Profiles-Add-Remove/ -LTRACE -v APPLIANCE_IP:15.186.9.62 -V /root/ci-fit/config_files/eagle62_basic_data-devt.py Server-Profiles-Add-Remove

Variables               ../../resources/data_variables.py
Resource                ../../../../../../resource/fusion_api_all_resource_files.txt
Resource		../../resources/common.robot
Library			Collections


*** Variables ***
${cycles}                        10
${X-API-VERSION}                 ${null}
${FUSION_PROMPT}                 \#
${FUSION_TIMEOUT}                60
${PROFILE_THROTTLE}              3
${PROFILE_ASSIGN_WAIT_TIMEOUT}   860m
${PROFILE_ASSIGN_WAIT_INTERVAL}  30s
${FORCE_PROFILE_APPLY}           all
${tbirdEnv}                      ${True}
${sleep}                         15m
${PROFILE_UNASSIGN_WAIT_TIMEOUT}   860m
${PROFILE_UNASSIGN_WAIT_INTERVAL}   30s

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login
    Run Keyword If   '${X-Api-Version}' == '${null}'   Set Api Version To Current

Power Off Servers
    [Documentation]   Poweroff servers.
    Power Off All Servers In Parallel

Begin Cycles
    Cycle   ${cycles}

*** Keywords ***
Cycle
    [Documentation]   Cycle up a test.
    [Arguments]     ${cycles}
    :FOR	${x}	IN RANGE	1	${cycles}+1
    \   Log To Console   Beginning cycle ${x} of ${cycles}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
 	\   Unassign All Server Profiles
    \   Remove All Server Profiles
    \   Remove All Server Profile Templates
    \   Sleep And Log Reason To Console   ${sleep}   reason=Sleeping ${sleep} to allow OneView to settle
    \   Add Server Profile Templates
    \   Add Server Profiles Using Templates
    \   Add Server Profiles No Hardware Assigned
    \   Assign Server Hardware To Profile
    \   Sleep And Log Reason To Console   ${sleep}   reason=Sleeping ${sleep} to allow OneView to settle

Add Server Profile Templates
    [Documentation]   Add server profile templates from variable.
    Log To Console   Adding Server Profile Templates
    ${server_profile_templates} =   Get Variable Value   ${server_profile_templates}
    Run Keyword If   ${server_profile_templates} is not ${null}   common.Add Server Profile Templates From Variable   ${server_profile_templates}   connectionSettingsApi=${500}

Add Server Profiles Using Templates
    [Documentation]   Add server profiles using templates from variable.
    Log To Console   Adding Server Profiles using templates
    ${server_profiles_using_template} =   Get Variable Value   ${server_profiles_using_template}
    Run Keyword If   ${server_profiles_using_template} is not ${null}   Add Server Profiles Using Template From Variable   ${server_profiles_using_template}   ${server_profile_to_bay_map}   connectionSettingsApi=${600}

Add Server Profiles No Hardware Assigned
    [Documentation]   Create server profiles from variable without assigning to server hardware.
    Log To Console   Adding Server Profile No Hardware Assigned
    ${server_profiles} =   Get Variable Value   ${server_profiles_nohw}
    Run Keyword If   ${server_profiles} is not ${null}   Add Unassigned Server Profiles   ${server_profiles}   ${server_profile_to_bay_map}

Assign Server Hardware To Profile
    [Documentation]   Assign the server hardware to a profile
	${server_profiles} =   Get Variable Value   ${server_profiles_nohw}
	Log To Console   Adding Server Hardware to Profiles
	Log   \n\nAssigning Server Hardware to Profiles   console=${True}
 	Run Keyword If	${server_profiles} is not ${null}		common.Assign Server Hardware To Existing Profiles From Variable	${server_profiles}   ${server_profile_to_bay_map}   timeout=${PROFILE_ASSIGN_WAIT_TIMEOUT}   interval=${PROFILE_ASSIGN_WAIT_INTERVAL}   waitForTask=${True}   forceProfileApply=${FORCE_PROFILE_APPLY}   throttle=${PROFILE_THROTTLE}

Unassign All Server Profiles
    [Documentation]   Query OneView for list of profiles then unassign server profiles from server hardware.
    Log To Console   Unassigning server profiles
    ${resp} =   Fusion Api Get Server Profiles
    ${profiles} =   Create List
    ${profile_list} =   Get From Dictionary   ${resp}   members
    common.Unassign Server Profiles   ${profile_list}   timeout=${PROFILE_UNASSIGN_WAIT_TIMEOUT}   interval=${PROFILE_UNASSIGN_WAIT_INTERVAL}   forceProfileApply=${FORCE_PROFILE_APPLY}   throttle=${PROFILE_THROTTLE}

Remove All Server Profiles
    [Documentation]   Remove all server profiles in parallel and fail on error.
    Log To Console   Removing server profiles
    Remove All Server Profiles In Parallel

Remove All Server Profile Templates
    [Documentation]   Removes all of the server profile templates
    Log To Console   Removing server profile templates
    Remove All Server Profile Templates In Parallel
