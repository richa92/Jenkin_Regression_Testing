*** Settings ***
Documentation       F648 hardware iSCSI boot on Tbird with CHAP/MCHCAP support
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Resource            ../global_variables.robot
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Login the Appliance
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
...                 AND     Remove all Profiles and Templates
Suite Teardown      Run Keywords    Remove all Profiles and Templates
...                 AND     Fusion Api Logout Appliance

*** Variables ***
#${DATA_FILE}         Regression_Data.py
#${X_API_VERSION}     500

*** Test Cases ***
TS0 Create the Negative Profiles
    [Tags]  SP  NEGATIVE  TS0
    Power off All Servers  control=PressAndHold
    Run Negative Tasks for List  ${negative_profile_tasks}

TS1 Cleanup Power on the Servers and Boot to POST
    [Tags]  SP  CLEANUP  TS1
    Power on Servers in Profiles  ${ts1_all_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts1_all_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

TS1 Cleanup Power Off the Servers
    [Tags]  SP  CLEANUP  TS1
    Power off Servers in Profiles  ${ts1_all_profiles}  powerControl=PressAndHold

TS1 Create the Profiles
    [Tags]  Performance  server_profiles-condition-hw_iscsi  SP  TS1
    Power off Servers in Profiles  ${ts1_create_profiles}  powerControl=PressAndHold
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${list}=  Add Server Profiles from variable	 ${ts1_create_profiles}
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}

TS1 Power on the Servers and Boot to POST after Create
    [Tags]  SP  TS1
    Power on Servers in Profiles  ${ts1_create_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts1_create_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

TS1 Verify Adapter Settings after Create
    [Tags]  SP  TS1
    Verify iSCSI Adapter Settings with hpMCTP for List  ${ts1_hpMCTP_after_create}

TS1 Check Volume Connected Sessions after Create
    [Tags]  SP  TS1
    CLIQ Check Volume Connected Sessions in profiles  ${ts1_create_profiles}  timeout=10m  interval=10s

TS1 Get the Volume Info after Create
    [Tags]  SP  TS1
    CLIQ Get Volume Info in profiles  ${ts1_create_profiles}

TS1 Edit the Profiles First Time
    [Tags]  Performance  server_profiles-condition-hw_iscsi  SP  TS1
    Power off Servers in Profiles  ${ts1_edit_profiles_1}  powerControl=PressAndHold
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${list}=  Edit Server Profiles from variable	 ${ts1_edit_profiles_1}
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}

TS1 Power on the Servers and Boot to POST after Edit First Time
    [Tags]  SP  TS1
    Power on Servers in Profiles  ${ts1_edit_profiles_1}
    Wait for Servers in Profiles to reach POST State  ${ts1_edit_profiles_1}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

TS1 Verify Adapter Settings after Edit First Time
    [Tags]  SP  TS1
    Verify iSCSI Adapter Settings with hpMCTP for List  ${ts1_hpMCTP_after_edit_1}

TS1 Check Volume Connected Sessions after Edit First Time
    [Tags]  SP  TS1
    CLIQ Check Volume Connected Sessions in profiles  ${ts1_edit_profiles_1}  timeout=10m  interval=10s

TS1 Get the Volume Info after Edit First Time
    [Tags]  SP  TS1
    CLIQ Get Volume Info in profiles  ${ts1_edit_profiles_1}

TS1 Edit the Profiles Second Time
    [Tags]  Performance  server_profiles-condition-hw_iscsi  SP  TS1
    Power off Servers in Profiles  ${ts1_edit_profiles_2}  powerControl=PressAndHold
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${list}=  Edit Server Profiles from variable	 ${ts1_edit_profiles_2}
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}

TS1 Power on the Servers and Boot to POST after Edit Second Time
    [Tags]  SP  TS1
    Power on Servers in Profiles  ${ts1_edit_profiles_2}
    Wait for Servers in Profiles to reach POST State  ${ts1_edit_profiles_2}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

TS1 Verify Adapter Settings after Edit Second Time
    [Tags]  SP  TS1
    Verify iSCSI Adapter Settings with hpMCTP for List  ${ts1_hpMCTP_after_edit_2}

TS1 Check Volume Connected Sessions after Edit Second Time
    [Tags]  SP  TS1
    CLIQ Check Volume Connected Sessions in profiles  ${ts1_edit_profiles_2}  timeout=10m  interval=10s

TS1 Get the Volume Info after Edit Second Time
    [Tags]  SP  TS1
    CLIQ Get Volume Info in profiles  ${ts1_edit_profiles_2}

TS1 Delete the Profiles
    [Documentation]  Remove the profiles, Power on and off the servers to clear the iSCSI settings in RIS/RBSU.
    [Tags]  SP  TS1
    Power off Servers in Profiles  ${ts1_delete_profiles}  powerControl=PressAndHold
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${list}=  Remove Server Profiles from variable	 ${ts1_delete_profiles}  force=${True}
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}

TS1 Verify Adapter Settings after Delete
    [Tags]  SP  TS1
    Power on Servers in Profiles  ${ts1_all_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts1_all_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=30s
    Verify iSCSI Adapter Settings with hpMCTP for List  ${ts1_hpMCTP_after_delete}

TS1 Get the Volume Info after Delete
    [Tags]  SP  TS1
    CLIQ Get Volume Info in profiles  ${ts1_all_profiles}

TS1 Power Off the Servers
    [Tags]  SP  TS2
    Power off Servers in Profiles  ${ts1_all_profiles}  powerControl=PressAndHold

TS2 Create the Profiles
    [Tags]  Performance  server_profiles-condition-hw_iscsi  SP  TS2
    Power off Servers in Profiles  ${ts2_create_profiles}  powerControl=PressAndHold
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${list}=  Add Server Profiles from variable	 ${ts2_create_profiles}
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}

TS2 Power on the Servers and Boot to POST after Create
    [Tags]  SP  TS2
    Power on Servers in Profiles  ${ts2_create_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts2_create_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

TS2 Verify Adapter Settings after Create
    [Tags]  SP  TS2
    Verify iSCSI Adapter Settings with hpMCTP for List  ${ts2_hpMCTP_after_create}

TS2 Check Volume Connected Sessions after Create
    [Tags]  SP  TS2
    CLIQ Check Volume Connected Sessions in profiles  ${ts2_create_profiles}  timeout=10m  interval=10s

TS2 Get the Volume Info after Create
    [Tags]  SP  TS2
    CLIQ Get Volume Info in profiles  ${ts2_create_profiles}

TS2 Edit the Profiles First Time
    [Tags]  Performance  server_profiles-condition-hw_iscsi  SP  TS2
    Power off Servers in Profiles  ${ts2_edit_profiles_1}  powerControl=PressAndHold
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${list}=  Edit Server Profiles from variable	 ${ts2_edit_profiles_1}
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}

TS2 Power on the Servers and Boot to POST after Edit First Time
    [Tags]  SP  TS2
    Power on Servers in Profiles  ${ts2_edit_profiles_1}
    Wait for Servers in Profiles to reach POST State  ${ts2_edit_profiles_1}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

TS2 Verify Adapter Settings after Edit First Time
    [Tags]  SP  TS2
    Verify iSCSI Adapter Settings with hpMCTP for List  ${ts2_hpMCTP_after_edit_1}

TS2 Check Volume Connected Sessions after Edit First Time
    [Tags]  SP  TS2
    CLIQ Check Volume Connected Sessions in profiles  ${ts2_edit_profiles_1}  timeout=10m  interval=10s

TS2 Get the Volume Info after Edit First Time
    [Tags]  SP  TS2
    CLIQ Get Volume Info in profiles  ${ts2_edit_profiles_1}

TS2 Edit the Profiles Second Time
    [Tags]  Performance  server_profiles-condition-hw_iscsi  SP  TS2
    Power off Servers in Profiles  ${ts2_edit_profiles_2}  powerControl=PressAndHold
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${list}=  Edit Server Profiles from variable	 ${ts2_edit_profiles_2}
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}

TS2 Power on the Servers and Boot to POST after Edit Second Time
    [Tags]  SP  TS2
    Power on Servers in Profiles  ${ts2_edit_profiles_2}
    Wait for Servers in Profiles to reach POST State  ${ts2_edit_profiles_2}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

TS2 Verify Adapter Settings after Edit Second Time
    [Tags]  SP  TS2
    Verify iSCSI Adapter Settings with hpMCTP for List  ${ts2_hpMCTP_after_edit_2}

TS2 Check Volume Connected Sessions after Edit Second Time
    [Tags]  SP  TS2
    CLIQ Check Volume Connected Sessions in profiles  ${ts2_edit_profiles_2}  timeout=10m  interval=10s

TS2 Get the Volume Info after Edit Second Time
    [Tags]  SP  TS2
    CLIQ Get Volume Info in profiles  ${ts2_edit_profiles_2}

TS2 Edit the Profiles Third Time
    [Tags]  Performance  server_profiles-condition-hw_iscsi  SP  TS2
    Power off Servers in Profiles  ${ts2_edit_profiles_3}  powerControl=PressAndHold
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${list}=  Edit Server Profiles from variable	 ${ts2_edit_profiles_3}
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}

TS2 Power on the Servers and Boot to POST after Edit Third Time
    [Tags]  SP  TS2
    Power on Servers in Profiles  ${ts2_edit_profiles_3}
    Wait for Servers in Profiles to reach POST State  ${ts2_edit_profiles_3}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

TS2 Verify Adapter Settings after Edit Third Time
    [Tags]  SP  TS2
    Verify iSCSI Adapter Settings with hpMCTP for List  ${ts2_hpMCTP_after_edit_3}

TS2 Check Volume Connected Sessions after Edit Third Time
    [Tags]  SP  TS2
    CLIQ Check Volume Connected Sessions in profiles  ${ts2_edit_profiles_3}  timeout=10m  interval=10s

TS2 Get the Volume Info after Edit Third Time
    [Tags]  SP  TS2
    CLIQ Get Volume Info in profiles  ${ts2_edit_profiles_3}

TS2 Move the Profile
    [Tags]  Performance  server_profiles-condition-hw_iscsi  SP  TS2
    Power off Servers in Profiles  ${ts2_all_profiles}  powerControl=PressAndHold
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${list}=  Edit Server Profiles from variable	 ${ts2_move_profiles}
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}

TS2 Power on the Servers and Boot to POST after Move
    [Tags]  SP  TS2
    Power on Servers in Profiles  ${ts2_move_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts2_move_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=30s

TS2 Verify Adapter Settings after Move
    [Tags]  SP  TS2
    Verify iSCSI Adapter Settings with hpMCTP for List  ${ts2_hpMCTP_after_move}

TS2 Check Volume Connected Sessions after Move
    [Tags]  SP  TS2
    CLIQ Check Volume Connected Sessions in profiles  ${ts2_move_profiles}  timeout=10m  interval=10s

TS2 Get the Volume Info after Move
    [Tags]  SP  TS2
    CLIQ Get Volume Info in profiles  ${ts2_move_profiles}

TS2 Delete the Profiles
    [Documentation]  Remove the profiles. power on and off the servers to clear the iSCSI settings in RIS/RBSU.
    [Tags]  SP  TS2
    Power off Servers in Profiles  ${ts2_delete_profiles}  powerControl=PressAndHold
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${list}=  Remove Server Profiles from variable	 ${ts2_delete_profiles}  force=${True}
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}

TS2 Verify Adapter Settings after Delete
    [Tags]  SP  TS2
    Power on Servers in Profiles  ${ts2_all_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts2_all_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=30s
    Verify iSCSI Adapter Settings with hpMCTP for List  ${ts2_hpMCTP_after_delete}

TS2 Get the Volume Info after Delete
    [Tags]  SP  TS2
    CLIQ Get Volume Info in profiles  ${ts2_all_profiles}

TS2 Power Off the Servers
    [Tags]  SP  TS2
    Power off Servers in Profiles  ${ts2_all_profiles}  powerControl=PressAndHold

Create Server Profile Template
    [Tags]  SPT
    ${timeout} =  set variable  30
    ${interval} =  set variable  10
    ${list} =  Add Server Profile Templates from variable  ${create_profile_templates}
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   should be equal  ${status}  PASS  msg=Failed to get task uri
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}
    Verify Server Profile Templates  ${create_profile_templates}
    Power off Servers in Profiles  ${sp_from_spt}  powerControl=PressAndHold
    ${resplist} =  Add Server Profiles from variable  ${sp_from_spt}
    Wait For Task2  ${resplist}  timeout=1500  interval=10
    Verify Server Profile  ${sp_from_spt_verify}

Power on the Servers and Boot to POST after Create SP from SPT
    [Tags]  SP-from-SPT
    Power on Servers in Profiles  ${sp_from_spt_power}
    Wait for Servers in Profiles to reach POST State  ${sp_from_spt_power}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=30s

Verify Adapter Settings after Create SP from SPT
    [Tags]  SP-from-SPT
    Verify iSCSI Adapter Settings with hpMCTP  ${F1162_hpMCTP_after_create_sp_from_spt}

Check Volume Connected Sessions after Create SP from SPT
    [Tags]  SP-from-SPT
    CLIQ Check Volume Connected Sessions in profiles  ${sp_from_spt}  timeout=10m  interval=10s

Get the Volume Info after Create SP from SPT
    [Tags]  SP-from-SPT
    CLIQ Get Volume Info in profiles  ${sp_from_spt}

Edit Server Profile Template
    [Tags]  SPT
    ${timeout} =  set variable  30
    ${interval} =  set variable  10
    ${list} =  Edit Server Profile Templates from Variable  ${edit_profile_templates}
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   should be equal  ${status}  PASS  msg=Failed to get task uri
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}
    Verify Server Profile Templates  ${edit_profile_templates}

Create the Negative Profile Templates
    [Tags]  SPT  NEGATIVE
    Run Negative Tasks for List  ${negative_spt_tasks}

Clean Up Templates
    [Tags]  SPT
    Power off Servers in Profiles  ${delete_sp_from_spt}  powerControl=PressAndHold
    ${resp} =  Remove Server Profile  @{sp_from_spt}[0]
    Wait for Task2  ${resp}  timeout=300
    :FOR   ${profile_name}  IN  @{delete_profile_templates}
    \      Fusion Api Delete Server Profile Template  ${profile_name}

Create Profile in API V500 Get with API V300
    [Tags]  BACKWARDS_COMPATIBILITY
    Power off Servers in Profiles  ${version500}  powerControl=PressAndHold
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${list}=  Add Server Profiles from variable	 ${version500}  api=500
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}
    ${300payload} =  Create Server Profile PUT Payload  ${profile300_verify}
    Verify Resource  ${300payload}  api=300


Delete the API V500 Profile
    [Documentation]  Remove the profiles. power on and off the servers to clear the iSCSI settings in RIS/RBSU.
    [Tags]  BACKWARDS_COMPATIBILITY
    Power off Servers in Profiles  ${version500}  powerControl=PressAndHold
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${list}=  Remove Server Profiles from variable	 ${version500}  force=${True}
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}

Create Profile in API V300 Get with API V500
    [Tags]  BACKWARDS_COMPATIBILITY
    Power off Servers in Profiles  ${version300}  powerControl=PressAndHold
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${list}=  Add Server Profiles from variable	 ${version300}  api=300
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}
    ${payload} =  Create Server Profile PUT Payload  ${profile1_one_connection_ip1_verify_v500}
    Verify Resource  ${payload}  api=500

Delete the API V300 Profile
    [Documentation]  Remove the profiles. power on and off the servers to clear the iSCSI settings in RIS/RBSU.
    [Tags]  BACKWARDS_COMPATIBILITY
    Power off Servers in Profiles  ${version300}  powerControl=PressAndHold
    ${timeout} =  set variable  3600
    ${interval} =  set variable  10
    ${list}=  Remove Server Profiles from variable	 ${version300}  force=${True}
    :FOR    ${item}  IN  @{list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}

*** Keywords ***
Login the Appliance
    [Documentation]  Set the log level, log the variables and login to the appliance as Administrator
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Remove all Profiles and Templates
    [Documentation]  Power off all servers, remove all SP's and, remove all SPT's
    Power off ALL servers
    ${resplist} =    Remove All Server Profiles Async    force=${True}
    Wait For Task2    ${resplist}    timeout=600    interval=5
    ${sptlist} =    Remove All Server Profile Templates
    Wait For Task2    ${sptlist}    timeout=600    interval=5