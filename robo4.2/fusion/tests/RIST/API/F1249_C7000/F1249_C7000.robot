*** Settings ***
Documentation       F1249 DHCP iSCSI boot support for C7000
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Resource            ../global_variables.robot
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Login to the Appliance
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
...                 AND     Add Existing Storage Volumes to OV
#Suite Teardown      Run Keywords    Delete Created Resources
#...                 AND     Fusion Api Logout Appliance

*** Variables ***
#${DATA_FILE}         Regression_Data.py
#${X_API_VERSION}     500

*** Test Cases ***
Create the Negative Profiles
    [Documentation]  Negative profile validation tests
    [Tags]    F1249-C7k-1
    Power off Servers in Profiles  ${create_profiles}
    Power off Servers in Profiles  ${create_gen10_profiles}
    Run Negative Tasks for List  ${negative_profile_tasks}

Cleanup Power on the Servers and Boot to POST
    [Documentation]  Power on the servers without any profiles
    [Tags]    F1249-C7k-2
    Power on Servers in Profiles  ${create_profiles}
    Wait for Servers in Profiles to reach POST State  ${create_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

Cleanup Power Off the Servers
    [Documentation]  Power off the servers
    [Tags]    F1249-C7k-3
    Power off Servers in Profiles  ${create_profiles}

Create the Profiles
    [Documentation]  Create the Profiles
    [Tags]    F1249-C7k-4  Performance  server_profiles-condition-hw_iscsi
    Power Off Servers in Profiles  ${create_profiles}
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${resplist}=  Add Server Profiles from variable	 ${create_profiles}
    Wait For Task2  ${resplist}  timeout=${timeout}  interval=${interval}

Verify Blade CLP after Create
    [Documentation]  Verify the blades CLP after the profile create
    [Tags]    F1249-C7k-5
    Run Keyword for List with kwargs  ${CLP_after_create}  OA CLI Verify Blade CLP

Power on the Servers and Boot to POST after Create
    [Documentation]  Power on the servers with profiles and wait until they have booted to POST
    [Tags]    F1249-C7k-6
    Power on Servers in Profiles  ${create_profiles}
    Wait for Servers in Profiles to reach POST State  ${create_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

Check Volume Connected Sessions after Create
    [Documentation]  Check that the iSCSI volumes are connected in the profiles
    [Tags]    F1249-C7k-7
    :FOR  ${profile}  IN  @{create_profiles}
    \   ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  name
    \   ${uri} =  Get Server Profile URI  ${name}
    \   ${resp} =  fusion api get server profiles  ${uri}
    \   CLIQ Check Volume Connected Sessions in profile  ${resp}  timeout=10m  interval=10s

Get the Volume Info after Create
    [Documentation]  Get the iSCSI volume info for all profile connections
    [Tags]    F1249-C7k-8
    :FOR  ${profile}  IN  @{create_profiles}
    \   ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  name
    \   ${uri} =  Get Server Profile URI  ${name}
    \   ${resp} =  fusion api get server profiles  ${uri}
    \   CLIQ Get Volume Info in profile  ${resp}

Edit the Profiles First Time
    [Documentation]  Edit the existing iSCSI profiles
    [Tags]    F1249-C7k-9  Performance  server_profiles-condition-hw_iscsi
    Power Off Servers in Profiles  ${edit_profiles}
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${resplist}=  Edit Server Profiles from variable	 ${edit_profiles}
    Wait For Task2  ${resplist}  timeout=${timeout}  interval=${interval}

Verify Blade CLP after Edit First Time
    [Documentation]  Verify the blades CLP after the first edit
    [Tags]    F1249-C7k-10
    Run Keyword for List with kwargs  ${CLP_after_edit}  OA CLI Verify Blade CLP

Power on the Servers and Boot to POST after Edit First Time
    [Documentation]  Power on the servers and boot to POST after the first edit
    [Tags]    F1249-C7k-11
    Power on Servers in Profiles  ${edit_profiles}
    Wait for Servers in Profiles to reach POST State  ${edit_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

Check Volume Connected Sessions after Edit First Time
    [Documentation]  Check that the iSCSI volumes are connected after the edit
    [Tags]    F1249-C7k-12
    set test variable  &{cliq_credentials}  &{user_specified_cliq_credentials}
    CLIQ Check Volume Connected Sessions in profiles  ${edit_profiles}  timeout=10m  interval=10s

Get the Volume Info after Edit First Time
    [Documentation]  Get the iSCSI volume info for all profile connections
    [Tags]    F1249-C7k-13
    set test variable  &{cliq_credentials}  &{user_specified_cliq_credentials}
    CLIQ Get Volume Info in profiles  ${edit_profiles}

Edit the Profiles Second Time
    [Documentation]  Edit the iSCSI profiles a second time
    [Tags]    F1249-C7k-14  Performance  server_profiles-condition-hw_iscsi
    Power Off Servers in Profiles  ${edit_profiles2}
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${resplist}=  Edit Server Profiles from variable	 ${edit_profiles2}
    Wait For Task2  ${resplist}  timeout=${timeout}  interval=${interval}

Verify Blade CLP after Edit Second Time
    [Documentation]  Verify the blades CLP settings after the second edit
    [Tags]    F1249-C7k-15
    Run Keyword for List with kwargs  ${CLP_after_edit2}  OA CLI Verify Blade CLP

Power on the Servers and Boot to POST after Edit Second Time
    [Documentation]  Power on the servers and boot to POST after the second edit
    [Tags]    F1249-C7k-16
    Power on Servers in Profiles  ${edit_profiles2}
    Wait for Servers in Profiles to reach POST State  ${edit_profiles2}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

Check Volume Connected Sessions after Edit Second Time
    [Documentation]  Check that the iSCSI volumes are connected after the second edit
    [Tags]    F1249-C7k-17
    :FOR  ${profile}  IN  @{edit_profiles2}
    \   ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  name
    \   ${uri} =  Get Server Profile URI  ${name}
    \   ${resp} =  fusion api get server profiles  ${uri}
    \   CLIQ Check Volume Connected Sessions in profile  ${resp}  timeout=10m  interval=10s

Get the Volume Info after Edit Second Time
    [Documentation]  Get the iSCSI volume info for all profile connections
    [Tags]    F1249-C7k-18
    :FOR  ${profile}  IN  @{edit_profiles2}
    \   ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  name
    \   ${uri} =  Get Server Profile URI  ${name}
    \   ${resp} =  fusion api get server profiles  ${uri}
    \   CLIQ Get Volume Info in profile  ${resp}

Move the Profile
    [Documentation]  Move sever profiles to blades of a different SHT
    [Tags]    F1249-C7k-19  Performance  server_profiles-condition-hw_iscsi
    Power Off Servers in Profiles  ${all_profiles}
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${resplist}=  Edit Server Profiles from variable	 ${move_profiles}
    Wait For Task2  ${resplist}  timeout=${timeout}  interval=${interval}

Verify Blade CLP after Move
    [Documentation]  Verify the blades CLP settings after the move
    [Tags]    F1249-C7k-20
    Run Keyword for List with kwargs  ${CLP_after_move}  OA CLI Verify Blade CLP

Power on the Servers and Boot to POST after Move
    [Documentation]  Power on the servers and boot to POST after the move
    [Tags]    F1249-C7k-21
    Power on Servers in Profiles  ${move_profiles}
    Wait for Servers in Profiles to reach POST State  ${move_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=30s

Check Volume Connected Sessions after Move
    [Documentation]  Check that the iSCSI volumes are connected after the the move
    [Tags]    F1249-C7k-22
    :FOR  ${profile}  IN  @{move_profiles}
    \   ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  name
    \   ${uri} =  Get Server Profile URI  ${name}
    \   ${resp} =  fusion api get server profiles  ${uri}
    \   CLIQ Check Volume Connected Sessions in profile  ${resp}  timeout=10m  interval=10s

Get the Volume Info after Move
    [Documentation]  Get the iSCSI volume info for all profile connections
    [Tags]    F1249-C7k-23
    :FOR  ${profile}  IN  @{move_profiles}
    \   ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  name
    \   ${uri} =  Get Server Profile URI  ${name}
    \   ${resp} =  fusion api get server profiles  ${uri}
    \   CLIQ Get Volume Info in profile  ${resp}

Delete the Profiles
    [Documentation]  Delete the profiles
    [Tags]    F1249-C7k-24
    Power off Servers in Profiles  ${delete_profiles}
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${resplist}=  Remove Server Profiles from variable	 ${delete_profiles}  force=${True}
    Wait For Task2  ${resplist}  timeout=${timeout}  interval=${interval}

Verify Blade CLP after Delete
    [Documentation]  Verify the blades CLP settings after the delete
    [Tags]    F1249-C7k-25
    Run Keyword for List with kwargs  ${CLP_after_delete}  OA CLI Verify Blade CLP

Power Off the Servers
    [Documentation]  Power off all servers used so far
    [Tags]    F1249-C7k-26
    Power off Servers in Profiles  ${all_profiles}

Create Server Profile Template
    [Documentation]  Create SPT's with iSCSI connections
    [Tags]    F1249-C7k-27
    ${timeout} =  set variable  30
    ${interval} =  set variable  10
    ${resplist} =  Add Server Profile Templates from variable  ${create_profile_templates}
    Wait For Task2  ${resplist}  timeout=${timeout}  interval=${interval}
    Verify Server Profile Templates  ${create_profile_templates}

Edit Server Profile Templates
    [Documentation]  Edit the SPT's
    [Tags]    F1249-C7k-28
    ${timeout} =  set variable  30
    ${interval} =  set variable  10
    ${resplist} =  Edit Server Profile Templates from variable  ${edit_profile_templates}
    Wait For Task2  ${resplist}  timeout=${timeout}  interval=${interval}
    Verify Server Profile Templates  ${edit_profile_templates}

Edit Server Profile Templates a Second Time
    [Documentation]  Edit the SPT's a second time
    [Tags]    F1249-C7k-29
    ${timeout} =  set variable  30
    ${interval} =  set variable  10
    ${resplist} =  Edit Server Profile Templates from variable  ${edit_profile_templates2}
    Wait For Task2  ${resplist}  timeout=${timeout}  interval=${interval}
    Verify Server Profile Templates  ${edit_profile_templates2}

Clean Up Templates
    [Documentation]  Delete all SPT's
    [Tags]    F1249-C7k-30
    :FOR   ${profile_name}  IN  @{delete_profile_templates}
    \      Fusion Api Delete Server Profile Template  ${profile_name}

#Create DHCP Server Profile Using API v300
#    ${resp} =  Create DHCP Server Profile v300  ${negative_create_profile_with_v300}
#    Should be Equal  ${resp}  PASS  msg=Server Profile creation did not return an error
#
#Verify DHCP Server Profile using API v300
#    Power Off Servers in Profiles  ${create_profile_for_v300_verify}
#    ${timeout} =  set variable  3600
#    ${interval} =  set variable  10
#    ${resplist}=  Add Server Profiles from variable	 ${create_profile_for_v300_verify}
#    Wait For Task2  ${resplist}  timeout=${timeout}  interval=${interval}
#    ${version300_payload} =  Create Server Profile PUT Payload  ${get_300_profile}
#    Verify Resource  ${version300_payload}  api=300
#
#Delete the Profiles after version control test
#    Power off Servers in Profiles  ${create_profile_for_v300_verify}
#    ${timeout} =  set variable  3600
#    ${interval} =  set variable  10
#    ${resplist}=  Remove Server Profiles from variable	 ${create_profile_for_v300_verify}  force=${True}
#    Wait For Task2  ${resplist}  timeout=${timeout}  interval=${interval}

Negative SPT Tests
    [Documentation]  Run Negative SPT validation tasks
    [Tags]    F1249-C7k-31
    Run Negative Tasks for List  ${negative_profile_template_tasks}

F1249 C7000 Gen10 profiles
    [Tags]    F1249-C7k-32
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${resplist} =  Add Server Profile Templates from variable  ${create_gen10_profile_template}
    Wait For Task2  ${resplist}  ${timeout}  ${interval}
    Verify Server Profile Templates  ${create_gen10_profile_template}
    Power Off Servers in Profiles  ${create_gen10_profiles}
    ${resplist}=  Add Server Profiles from variable	 ${create_gen10_profiles}
    Wait for Task2  ${resplist}  ${timeout}  ${interval}
    CLIQ Get Volume Info in profiles  ${create_gen10_profiles}
    Power Off Servers in Profiles  ${edit_gen10_profile}
    ${resplist}=  Edit Server Profiles from variable	 ${edit_gen10_profile}
    Wait For Task2  ${resplist}  ${timeout}  ${interval}
    ${resplist}=  Remove Server Profiles from variable	 ${create_gen10_profiles}  force=${True}
    Wait For Task2  ${resplist}  ${timeout}  ${interval}
    Remove All Server Profile Templates

*** Keywords ***
Login to the Appliance
    [Documentation]  Log into the appliance as administrator
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Remove all Profiles and Templates
    [Documentation]  Remove all server profiles and server profile templates
    Power off ALL servers
    ${resplist} =    Remove All Server Profiles Async    force=${True}
    Wait For Task2    ${resplist}    timeout=600    interval=5
    ${sptlist} =    Remove All Server Profile Templates
    Wait For Task2    ${sptlist}    timeout=600    interval=5

Create DHCP Server Profile v300
    [Documentation]  Check for error message when assigning an iSCSI profile with api=300 and the dto at api=400
    [arguments]  ${server_profiles}
    ${responses} = 	Add Server Profiles from variable     ${server_profiles}  api=300
	:FOR	${resp}	IN	@{responses}
	\   log to console		${resp}
	\   ${x} =  set variable if  '${resp['errorCode']}'=='UNRECOGNIZED_JSON_FIELD'  PASS  error
	[return]  ${x}

Delete Created Resources
    [Documentation]  Remove all Server Profile Templates, Server Profiles, and Storage Volumes added by this test suite
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    :FOR   ${spt_name}  IN  @{delete_profile_templates}
    \      Fusion Api Delete Server Profile Template  ${spt_name}
    Power off Servers in Profiles  ${all_profiles}
#    Power off Servers in Profiles  ${create_profile_for_v300_verify}
#    ${resplist}=  Remove Server Profiles from variable	 ${create_profile_for_v300_verify}  force=${True}
#    Wait For Task2  ${resplist}  timeout=${timeout}  interval=${interval}
     ${resplist}=  Remove Server Profiles from variable	 ${all_profiles}  force=${True}
    Wait For Task2  ${resplist}  timeout=${timeout}  interval=${interval}
    ${resplist} =  Remove Storage Volumes Async  ${existing_volumes}  param=?suppressDeviceUpdates=true
    Wait For Task2  ${resplist}  timeout=30  interval=10

Add Existing Storage Volumes to OV
    [Documentation]  Add Existing Storage Volumes to OV
    ${resplist} =  Add Existing Storage Volumes Async  ${existing_volumes}
    Wait for Task2  ${resplist}  timeout=30  interval=10
