*** Settings ***
Documentation                   OVF1086/OVS3803/F1321 Simplified iSCSI Boot Server Profile Templates for Tbird

Library             FusionLibrary
Library             BuiltIn
Library             Collections
Library             json
Library             Dialogs
Resource            ../global_variables.robot
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Initialize the Variables and Log In as Administrator
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
...                 AND     Add Existing Storage Volumes to OV
Suite Teardown      Run Keywords    Delete Created Resources
...                 AND     Fusion Api Logout Appliance

*** Variables ***
#${DATA_FILE}         tbird9_static_initiator_hw_iscsi_variables.py
#${X_API_VERSION}     500

*** Test Cases ***
Create the Profile Templates
    [Documentation]  Add Server Profile Templates
    ${resp_list} =  Add Server Profile Templates from variable  ${create_templates}
    Wait For Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${create_templates}

Create the Negative Profile Templates
    [Documentation]  Run negative Server Profile Template validation tasks
    Run Negative Tasks for List  ${negative_spt_tasks}

Edit the Profile Templates First Time
    [Documentation]  Edit the SPT's
    ${resp_list} =  Edit Server Profile Templates from variable  ${edit_templates1}
    Wait For Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${edit_templates1}

Edit the Profile Templates Second Time
    [Documentation]  Edit the SPT's a second time
    ${resp_list} =  Edit Server Profile Templates from variable  ${edit_templates2}
    Wait For Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${edit_templates2}

Create the Negative profiles from SPT
    [Documentation]  Run negative SP from SPT validation tasks
    Run Negative Tasks for List  ${negative_sp_tasks}

Create Profile from Template using Template Defined Volumes
    [Documentation]  Create Server Profiles from the Templates and create new private volumes with iSCSI connections
    [Tags]  Performance  server_profiles-condition-iscsi_managed_volume
    Power Off Servers in Profiles  ${create_sp_from_spt}  powerControl=PressAndHold
    ${resp_list}=  Add Server Profiles from variable  ${create_sp_from_spt}
    Wait For Task2  ${resp_list}  timeout=1500  interval=10
    :FOR  ${profile}  IN  @{verify_create_sp_from_spt}
    \   Verify Server Profile  ${profile}

Verify Profile Compliance after Create
    [Documentation]  Verify SP/SPT's are compliant
    :FOR  ${profile}  IN  @{sp_compliance}
    \   Verify Server Profile Compliance  ${profile}

Edit Profile from Template to use Existing Volume
    [Documentation]  Edit the SP's to boot from existing volumes with OS's already installed
    [Tags]  Performance  server_profiles-condition-iscsi_managed_volume
    Power Off Servers in Profiles  ${edit_sp_from_spt}  powerControl=PressAndHold
    ${resp_list}=  Edit Server Profiles from variable  ${edit_sp_from_spt}
    Wait For Task2  ${resp_list}  timeout=1500  interval=10
    :FOR  ${profile}  IN  @{edit_sp_from_spt}
    \   Verify Server Profile  ${profile}

Verify Profile Compliance after Edit
    [Documentation]  Verify the SP/SPT's are compliant
    :FOR  ${profile}  IN  @{sp_compliance}
    \   Verify Server Profile Compliance  ${profile}

Power on Servers and Boot to POST after Edit Profile from Template Existing Volumes
    [Documentation]  Power on the servers and wait until they have reached POST
    Power on Servers in Profiles  ${edit_sp_from_spt}
    Wait for Servers in Profiles to reach POST State  ${edit_sp_from_spt}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

Check Volume Connected Sessions after Edit Profile from Template Existing Volumes
    [Documentation]  Check that the iSCSI volumes are connected
    :FOR  ${profile}  IN  @{edit_sp_from_spt}
    \   ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  name
    \   ${uri} =  Get Server Profile URI  ${name}
    \   ${resp} =  fusion api get server profiles  ${uri}
    \   CLIQ Check Volume Connected Sessions in profile  ${resp}  timeout=10m  interval=10s

Get the Volume Info after Edit Profile from Template Existing Volumes
    [Documentation]  Get the iSCSI volume info for each connection in the profiles
    :FOR  ${profile}  IN  @{edit_sp_from_spt}
    \   ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  name
    \   ${uri} =  Get Server Profile URI  ${name}
    \   ${resp} =  fusion api get server profiles  ${uri}
    \   CLIQ Get Volume Info in profile  ${resp}

Edit Server Profiles to be Non-compliant
    [Documentation]  Edit the Server Profiles to be non-compliant with the SPT. Then verify the expected compliance messages are returned.
    Power Off Servers in Profiles  ${edit_compliance1_sp_from_spt}  powerControl=PressAndHold
    ${resp_list}=  Edit Server Profiles from variable  ${edit_compliance1_sp_from_spt}  param=?force=ignoreServerHealth,ignoreSANWarnings
    Wait For Task2  ${resp_list}  timeout=1500  interval=10
    :FOR  ${profile}  IN  @{verify_non_compliance_sp_from_spt}
    \    Verify Server Profile Compliance  ${profile}  True

Edit Server Profiles to be Compliant
    [Documentation]  Edit the Server Profiles to return them to compliance with the SPT. Then check that there are no complance messages.
    Power Off Servers in Profiles  ${edit_sp_from_spt}  powerControl=PressAndHold
    ${resp_list}=  Edit Server Profiles from variable  ${edit_sp_from_spt}
    Wait For Task2  ${resp_list}  timeout=1500  interval=10
    :FOR  ${profile}  IN  @{sp_compliance}
    \    Verify Server Profile Compliance  ${profile}

Edit Server Profile Templates to be Non-compliant
    [Documentation]  Edit the SPT's so that the SP's are no longer compliant with the SPT. Then verify the expected complance messages are returned.
    ${resp_list}=  Edit Server Profile Templates from variable  ${edit_compliance2_template}
    Wait For Task2  ${resp_list}  timeout=1500  interval=10
    :FOR  ${profile}  IN  @{verify_non_compliance_sp_from_spt2}
    \    Verify Server Profile Compliance  ${profile}  True

Edit Server Profile Templates to be Compliant
    [Documentation]  Edit the SPT's and then the SP's to return them to compliance with each other. Then check that there are no complance messages.
    ${resp_list}=  Edit Server Profile Templates from variable  ${edit_compliance3_template}
    Wait For Task2  ${resp_list}  timeout=1500  interval=10
    Power Off Servers in Profiles  ${edit_sp_from_spt}  powerControl=PressAndHold
    ${resp_list}=  Edit Server Profiles from variable  ${edit_sp_from_spt}
    Wait For Task2  ${resp_list}  timeout=1500  interval=10
    :FOR  ${profile}  IN  @{sp_compliance}
    \    Verify Server Profile Compliance  ${profile}

*** Keywords ***
Initialize the Variables and Log In as Administrator
    [Documentation]  Set the log level, log the variables and login to the appliance as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Delete Created Resources
    [Documentation]  Remove all Server Profile Templates, Server Profiles, and Storage Volumes added by this test suite
    Power Off Servers in Profiles  ${edit_sp_from_spt}  powerControl=PressAndHold
    ${resp_list}=  Remove Server Profiles from variable	 ${edit_sp_from_spt}  force=${True}
    Get Task and Wait for Completion  ${resp_list}  3600
    :FOR   ${spt_name}  IN  @{delete_profile_templates}
    \      Fusion Api Delete Server Profile Template  ${spt_name}
    ${resplist} =  Remove Storage Volumes Async  ${new_permanent_volumes}  param=?suppressDeviceUpdates=false
    Wait For Task2  ${resplist}  timeout=30  interval=10
    ${resplist} =  Remove Storage Volumes Async  ${existing_volumes}  param=?suppressDeviceUpdates=true
    Wait For Task2  ${resplist}  timeout=30  interval=10

Get Task and Wait for Completion
    [Documentation]  Get the task uri and then wait for Tasks
    [arguments]  ${resp_list}  ${timeout}=60  ${interval}=10
    :FOR    ${item}  IN  @{resp_list}
    \   ${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${item['headers']}  location
	\   CONTINUE FOR LOOP IF    '${status}'=='FAIL'
	\   Log    The task URI is ${task_uri}    console=true
	\   ${task} =  Fusion Api Get Task  uri=${task_uri}
    \   Wait For Task2  ${task}  timeout=${timeout}  interval=${interval}

Add Existing Storage Volumes to OV
    [Documentation]  Add Existing Storage Volumes to OV
    ${resplist} =  Add Existing Storage Volumes Async  ${existing_volumes}
    Wait for Task2  ${resplist}  timeout=30  interval=10