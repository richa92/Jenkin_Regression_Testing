*** Settings ***
Documentation                   F963 Simplified iSCSI Boot


Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Resource            ../global_variables.robot
#Resource            ../OVF929/OVF929.robot
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Initialize the Variables and Log In
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
...                 AND     Add Existing Storage Volumes to OV
Suite Teardown      Run Keywords    Remove all Profiles
...                 AND     Remove Existing Storage Volumes from OV only
...                 AND     Fusion Api Logout Appliance

*** Variables ***
#${APPLIANCE_IP}		16.114.213.91
#${DATA_FILE}         dcs_variables.py
#${ovf929}            ${True}

*** Test Cases ***
Negative Profile Validation Tests
    [Documentation]  Run negative profile validation tests
    # For negative_sp_8
    Set Test Variable    ${VOLUME}    ${PROFILE1_EXISTING_VOLUME}
    Run Negative Tasks for List  ${negative_sp_tasks}

Create Server Profiles
    [Documentation]  Create both SW iSCSI and HW iSCSI Profiles
    Power Off Servers in Profiles  ${create_profiles}
    ${resplist} =  Add Server Profiles from variable  ${create_profiles}
#    ${ovf929_status}  ${ovf959_test_response} =    Run Keyword If    '${ovf929}'=='${True}'    Run Keyword and Ignore Error    Check Gen10 BootSources and Verify that CQTDISC EV is Not Set    ${gen10_create_profiles}  ${ris_ovf929_gen10_create_profiles}
    Wait for Task2   ${resplist}  timeout=1500  interval=10
    :FOR    ${profile}  IN  @{create_profiles}
    \   Verify Server Profile  ${profile}
#    Run Keyword If    '${ovf929}'=='${True}' and '${ovf929_status}'=='FAIL'   Fail    ${ovf959_test_response}

Get the SW iSCSI Pending Settings after Create
    [Documentation]  Get the pending SW iSCSI Settings after the profile create
    Run Keyword for List with kwargs  ${ris_nodes_iscsi_settings_create}  Get Ris Node  VERBOSE=True

Power on the Servers and Boot to POST after Create
    [Documentation]  Power on the servers with iSCSI profiles and boot to POST
    Power on Servers in Profiles  ${create_profiles}
    Wait for Servers in Profiles to reach POST State  ${create_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

Get HW iSCSI Adapter Settings after Create
    [Documentation]  Get the the HW iSCSI Adapter Settings and print to the log & console
    Get iSCSI Adapter Settings with hpMCTP for List  ${get_hpMCTP}

Get the SW iSCSI Current Settings after Create
    [Documentation]  Get the  SW iSCSI Settings after the profile create and the server has booted to POST
    Run Keyword for List with kwargs  ${ris_nodes_iscsi_settings_create}  Get Ris Node  VERBOSE=True

Check Volume Connected Sessions after Create
    [Documentation]  Check that the volumes are connected for each iSCSI profile
    :FOR  ${profile}  IN  @{create_profiles}
    \   ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  name
    \   ${uri} =  Get Server Profile URI  ${name}
    \   ${resp} =  fusion api get server profiles  ${uri}
    \   CLIQ Check Volume Connected Sessions in profile  ${resp}  timeout=10m  interval=10s

Get the Volume Info after Create
    [Documentation]  Get the volume info for each connection in the iSCSI profile
    :FOR  ${profile}  IN  @{create_profiles}
    \   ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  name
    \   ${uri} =  Get Server Profile URI  ${name}
    \   ${resp} =  fusion api get server profiles  ${uri}
    \   CLIQ Get Volume Info in profile  ${resp}

Add secondary iSCSI boot connections using edit
    [Documentation]  Edit the Server Profiles and a secondary boot connection
    Power Off Servers in Profiles  ${sp_edit_add_secondary_connection}
    ${resplist} =  Edit Server Profiles from variable  ${sp_edit_add_secondary_connection}
#    ${ovf929_status}  ${ovf959_test_response} =    Run Keyword If    '${ovf929}'=='${True}'    Run Keyword and Ignore Error    Check Gen10 BootSources and Verify that CQTDISC EV is Not Set    ${gen10_edit1_profiles}  ${ris_ovf929_gen10_edit1_profiles}
    Wait for Task2  ${resplist}  timeout=1500  interval=5
    :FOR  ${profile}  IN  @{sp_edit_add_secondary_connection}
    \   Verify Server Profile  ${profile}
#    Run Keyword If    '${ovf929}'=='${True}' and '${ovf929_status}'=='FAIL'   Fail    ${ovf959_test_response}

Get the SW iSCSI Pending Settings after First Edit
    [Documentation]  Get the pending SW iSCSI Settings after the profile edit
    Run Keyword for List with kwargs  ${ris_nodes_iscsi_settings_create}  Get Ris Node  VERBOSE=True

Power on the Servers and Boot to POST after First Edit
    [Documentation]  Power on the servers with iSCSI profiles and boot to POST
    Power on Servers in Profiles  ${sp_edit_add_secondary_connection}
    Wait for Servers in Profiles to reach POST State  ${sp_edit_add_secondary_connection}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

Get HW iSCSI Adapter Settings after First Edit
    [Documentation]  Get the the HW iSCSI Adapter Settings and print to the log & console
    Get iSCSI Adapter Settings with hpMCTP for List  ${get_hpMCTP}

Get the SW iSCSI Current Settings after First Edit
    [Documentation]  Get the  SW iSCSI Settings after the profile edit and the server has booted to POST
    Run Keyword for List with kwargs  ${ris_nodes_iscsi_settings_create}  Get Ris Node  VERBOSE=True

Check Volume Connected Sessions after First Edit
    [Documentation]  Check that the volumes are connected for each iSCSI profile
    :FOR  ${profile}  IN  @{sp_edit_add_secondary_connection}
    \   ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  name
    \   ${uri} =  Get Server Profile URI  ${name}
    \   ${resp} =  fusion api get server profiles  ${uri}
    \   CLIQ Check Volume Connected Sessions in profile  ${resp}  timeout=10m  interval=10s

Get the Volume Info after First Edit
    [Documentation]  Get the volume info for each connection in the iSCSI profile
    :FOR  ${profile}  IN  @{sp_edit_add_secondary_connection}
    \   ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  name
    \   ${uri} =  Get Server Profile URI  ${name}
    \   ${resp} =  fusion api get server profiles  ${uri}
    \   CLIQ Get Volume Info in profile  ${resp}

Edit iSCSI Profile Boot Volume
    [Documentation]  Edit iSCSI Server Profiles and change to a different managed volume
    Power Off Servers in Profiles  ${sp_iscsi_edit_boot_volume}
    ${resplist} =  Edit Server profiles from variable  ${sp_iscsi_edit_boot_volume}
#    ${ovf929_status}  ${ovf959_test_response} =    Run Keyword If    '${ovf929}'=='${True}'    Run Keyword and Ignore Error    Check Gen10 BootSources and Verify that CQTDISC EV is Not Set    ${gen10_sw_edit2_profiles}  ${ris_ovf929_gen10_sw_edit2_profiles}
    Wait for Task2  ${resplist}  timeout=1500  interval=10
    :FOR  ${profile}  IN  @{sp_iscsi_edit_boot_volume}
    \   Verify Server Profile  ${profile}
#    Run Keyword If    '${ovf929}'=='${True}' and '${ovf929_status}'=='FAIL'   Fail    ${ovf959_test_response}

Get the SW iSCSI Pending Settings after Second Edit
    [Documentation]  Get the pending SW iSCSI Settings after the profile edit
    Run Keyword for List with kwargs  ${ris_nodes_iscsi_settings_create}  Get Ris Node  VERBOSE=True

Power on the Servers and Boot to POST after Second Edit
    [Documentation]  Power on the servers with iSCSI profiles and boot to POST
    Power on Servers in Profiles  ${sp_edit2}
    Wait for Servers in Profiles to reach POST State  ${sp_edit2}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

Get HW iSCSI Adapter Settings after Second Edit
    [Documentation]  Get the the HW iSCSI Adapter Settings and print to the log & console
    Get iSCSI Adapter Settings with hpMCTP for List  ${get_hpMCTP}

Get the SW iSCSI Current Settings after Second Edit
    [Documentation]  Get the  SW iSCSI Settings after the profile edit and the server has booted to POST
    Run Keyword for List with kwargs  ${ris_nodes_iscsi_settings_create}  Get Ris Node  VERBOSE=True

Check Volume Connected Sessions after Second Edit
    [Documentation]  Check that the volumes are connected for each iSCSI profile
    :FOR  ${profile}  IN  @{sp_edit2}
    \   ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  name
    \   ${uri} =  Get Server Profile URI  ${name}
    \   ${resp} =  fusion api get server profiles  ${uri}
    \   CLIQ Check Volume Connected Sessions in profile  ${resp}  timeout=10m  interval=10s

Get the Volume Info after Second Edit
    [Documentation]  Get the volume info for each connection in the iSCSI profile
    :FOR  ${profile}  IN  @{sp_edit2}
    \   ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  name
    \   ${uri} =  Get Server Profile URI  ${name}
    \   ${resp} =  fusion api get server profiles  ${uri}
    \   CLIQ Get Volume Info in profile  ${resp}

Delete Server Profiles and Volumes
    [Documentation]  Remove all the server profiles and then remove the existing volumes from OV only
    Power Off Servers in Profiles  ${sp_edit2}
    ${resplist} =  Remove Server Profiles from variable  ${sp_edit2}
    Wait for Task2  ${resplist}  timeout=1500  interval=10
    ${resplist} =  Remove Storage Volumes Async  ${existing_volumes}  param=?suppressDeviceUpdates=true
    Wait For Task2  ${resplist}  timeout=30  interval=10

*** Keywords ***
Initialize the Variables and Log In
    [Documentation]  Set the log level to TRACE, log the variables and login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Remove all Profiles
    [Documentation]  Remove all Server Profiles
    Power off ALL servers
    ${resplist} =    Remove All Server Profiles Async    force=${True}
    Wait For Task2    ${resplist}    timeout=1500    interval=5

Add Existing Storage Volumes to OV
    [Documentation]  Add Existing Storage Volumes to OV
    ${resplist} =  Add Existing Storage Volumes Async  ${existing_volumes}
    Wait for Task2  ${resplist}  timeout=30  interval=10

Remove Existing Storage Volumes from OV only
    [Documentation]  Removes Existing Storage Volumes from OV only
    ${resplist} =  Remove Storage Volumes Async  ${existing_volumes}  param=?suppressDeviceUpdates=true
    Wait For Task2  ${resplist}  timeout=30  interval=10