*** Settings ***
Documentation       OVF2161 Secure Boot in SPT and SP
Suite Setup         OVF2161 Synergy Setup
Suite Teardown      OVF2161 Synergy Teardown
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Resource            ../global_variables.robot
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

${DATA_FILE}         Regression_Data.py

*** Test Cases ***
OVF2161 Synergy TS0 Login the Appliance
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

OVF2161 Synergy NTS1 Create the Negative SPT and Fail Validation
    Run Negative Tasks for List  ${nts1_negative_spt_tasks}  timeout=120    interval=10

OVF2161 Synergy NTS1 Cleanup
    ${resplist}=  Remove All Server Profile Templates
    Wait for Task2  ${resplist}    timeout=60    interval=10

OVF2161 Synergy NTS2 Create the SPT
    ${resp}=  Add Server Profile Template  ${nts2_spt_create}
    Wait for Task2  ${resp}     timeout=120    interval=10

OVF2161 Synergy NTS2 Edit the SPT to Fail Validation
    Run Negative Tasks for List  ${nts2_negative_spt_tasks}  timeout=120    interval=10

OVF2161 Synergy NTS2 Delete the SPT
    ${resplist}=  Remove All Server Profile Templates
    Wait for Task2  ${resplist}    timeout=60    interval=10

OVF2161 Synergy NTS3 Create the Profiles to Fail Validation
    Power Off Server  ${NTS3_PROFILE1_SERVER}  powerControl=PressAndHold
    Power Off Server  ${NTS3_PROFILE2_SERVER}  powerControl=PressAndHold
    Power Off Server  ${NTS3_PROFILE3_SERVER}  powerControl=PressAndHold
    Run Negative Tasks for List  ${nts3_negative_profile_tasks}  timeout=900    interval=10

OVF2161 Synergy NTS3 Cleanup
    ${resplist} =  Remove All Server Profiles Async  force=${True}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF2161 Synergy NTS4 Create the Profile
    Power Off Server  ${NTS4_PROFILE_SERVER}  powerControl=PressAndHold
    ${resp}=  Add Server Profile  ${nts4_profile_create}
    Wait for Task2  ${resp}     timeout=600    interval=10

OVF2161 Synergy NTS4 Edit the Profile to Fail Validation
    Run Negative Tasks for List  ${nts4_negative_profile_tasks}  timeout=120    interval=10

OVF2161 Synergy NTS4 Delete the Profiles
    Power Off Server  ${NTS4_PROFILE_SERVER}  powerControl=PressAndHold
    ${resp}=  Remove Server Profile  ${nts4_profile_create}
    Wait for Task2  ${resp}    timeout=60    interval=10

OVF2161 Synergy PTS1 Create the SPTs
    ${resplist}=  Add Server Profile Templates from variable	 ${pts1_spts_create}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF2161 Synergy PTS1 Verify the SPTs after Create
    Verify Server Profile Templates  ${pts1_spts_create}

OVF2161 Synergy PTS1 Create the profiles from SPTs
    Power Off Servers in Profiles  ${pts1_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Add Server Profiles from variable	 ${pts1_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF2161 Synergy PTS1 Verify the Profiles after Create
    Run Keyword for List  ${pts1_profiles_create_expected}  Verify Server Profile

OVF2161 Synergy PTS1 Verify the Profiles Compliance after Create
    Run Keyword for List  ${pts1_profiles_compliant_compliance}  Verify Server Profile Compliance

OVF2161 Synergy PTS1 Verify RIS SecureBoot Settings after Create
    Verify RIS nodes for list  ${pts1_ris_nodes_after_create}

OVF2161 Synergy PTS1 Power On the Servers and Wait for POST
    Power On Servers in Profiles  ${pts1_profiles_create}
    Wait for Servers in Profiles to reach POST State  ${pts1_profiles_create}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF2161 Synergy PTS1 Verify RIS SecureBoot Settings after Power On
    Verify RIS nodes for list  ${pts1_ris_nodes_after_power_on_after_create}

OVF2161 Synergy PTS1 Power Off the Servers
    Power Off Servers in Profiles  ${pts1_profiles_create}  powerControl=PressAndHold

OVF2161 Synergy PTS1 Edit SecureBoot in SPT
    ${resplist}=  Edit Server Profile Templates from variable	 ${pts1_spts_edit}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF2161 Synergy PTS1 Verify the SPT after Edit
    Verify Server Profile Templates  ${pts1_spts_edit}

OVF2161 Synergy PTS1 Verify the Profiles Compliance after Edit
    Run Keyword for List  ${pts1_profiles_edit_compliance}  Verify Server Profile Compliance

OVF2161 Synergy PTS1 Update the Profiles From Template
    ${resplist}=  Update Server Profiles from Template  ${pts1_profiles_create}
    Wait For Task2  ${resplist}   timeout=600    interval=10

OVF2161 Synergy PTS1 Verify the Profiles after Patch
    Run Keyword for List  ${pts1_profiles_patch_expected}  Verify Server Profile

OVF2161 Synergy PTS1 Verify the Profiles Compliance after Patch
    Run Keyword for List  ${pts1_profiles_compliant_compliance}  Verify Server Profile Compliance

OVF2161 Synergy PTS1 Verify RIS SecureBoot Settings after Patch
    Verify RIS nodes for list  ${pts1_ris_nodes_after_patch}

OVF2161 Synergy PTS1 Power On the Servers after Patch
    Power On Servers in Profiles  ${pts1_profiles_create}
    Wait for Servers in Profiles to reach POST State  ${pts1_profiles_create}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF2161 Synergy PTS1 Verify RIS SecureBoot Settings after Power On after Patch
    Verify RIS nodes for list  ${pts1_ris_nodes_after_power_on_after_patch}

OVF2161 Synergy PTS1 Delete the profiles
    Power off Servers in Profiles  ${pts1_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts1_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF2161 Synergy PTS1 Remove the SPTs
    ${resplist} =  Remove Server Profile Templates from variable  ${pts1_spts_create}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF2161 Synergy PTS2 Create the profile
    Power Off Server  ${PTS2_PROFILE_SERVER}  powerControl=PressAndHold
    ${resp}=  Add Server Profile  ${pts2_profile_create}
    Wait For Task2  ${resp}   timeout=900    interval=10

OVF2161 Synergy PTS2 Verify the Profile after Create
    Verify Server Profile  ${pts2_profile_create}

OVF2161 Synergy PTS2 Verify RIS SecureBoot Settings after Create
     Verify RIS node  ${ris_node_sht_gen10_sy480_server1_secure_boot_enabled}

OVF2161 Synergy PTS2 Power On the Servers after Create
    Power On Servers in Profiles  ${pts2_profiles_create}
    Wait for Servers in Profiles to reach POST State  ${pts2_profiles_create}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF2161 Synergy PTS2 Verify RIS SecureBoot Settings after Power On after Create
    Verify RIS node  ${ris_node_sht_gen10_sy480_server1_secure_boot_enabled_power_on}

OVF2161 Synergy PTS2 Create SPT from SP
    ${resp} =  Create Server Profile Template from Profile  ${pts2_profile_create}  ${PTS2_SPT_FROM_SP_NAME}
    wait for task2  ${resp}  timeout=600  interval=10

OVF2161 Synergy PTS2 Verify SPT from SP
    Verify Server Profile Template  ${pts2_spt_from_sp_expected}

OVF2161 Synergy PTS2 Create SP from SPT
    Power Off Server  ${PTS2_SP_FROM_SPT_SERVER}  powerControl=PressAndHold
    ${resp}=  Add Server Profile  ${pts2_sp_from_spt}
    Wait For Task2  ${resp}   timeout=900    interval=10

OVF2161 Synergy PTS2 Verify SP from SPT
    Verify Server Profile  ${pts2_sp_from_spt_expected}

OVF2161 Synergy PTS2 Verify RIS SecureBoot Settings after Create SP from SPT
     Verify RIS node  ${ris_node_sht_gen10_sy480_server2_secure_boot_enabled}

OVF2161 Synergy PTS2 Power On the Servers after Create SP from SPT
    Power On Servers in Profiles  ${pts2_profiles_sp_from_spt}
    Wait for Servers in Profiles to reach POST State  ${pts2_profiles_sp_from_spt}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF2161 Synergy PTS2 Verify RIS SecureBoot Settings after Power On after Create SP from SPT
    Verify RIS node  ${ris_node_sht_gen10_sy480_server2_secure_boot_enabled_power_on}

OVF2161 Synergy PTS2 Delete the profiles
    Power off Servers in Profiles  ${pts2_profiles_delete}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts2_profiles_delete}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF2161 Synergy PTS2 Remove the SPTs
    ${resplist} =  Remove All Server Profile Templates
    wait for task2  ${resplist}  timeout=900  interval=10

OVF2161 Synergy PTS3 Create the Profile
    Power Off Server  ${PTS3_PROFILE_SERVER}  powerControl=PressAndHold
    ${resp}=  Add Server Profile  ${pts3_profile_create}
    Wait For Task2  ${resp}   timeout=900    interval=10

OVF2161 Synergy PTS3 Verify the Profile after Create
    Verify Server Profile  ${pts3_profile_create}

OVF2161 Synergy PTS3 Verify RIS SecureBoot Settings after Create
     Verify RIS node  ${ris_node_sht_gen10_sy480_server1_secure_boot_enabled}

OVF2161 Synergy PTS3 Power On the Servers after Create
    Power On Servers in Profiles  ${pts3_profiles_create}
    Wait for Servers in Profiles to reach POST State  ${pts3_profiles_create}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF2161 Synergy PTS3 Verify RIS SecureBoot Settings after Power On after Create
    Verify RIS node  ${ris_node_sht_gen10_sy480_server1_secure_boot_enabled_power_on}

OVF2161 Synergy PTS3 Move the Profile
    Power Off Server  ${PTS3_PROFILE_SERVER}  powerControl=PressAndHold
    Power Off Server  ${PTS3_PROFILE_MOVE_SERVER}  powerControl=PressAndHold
    ${resp}=  Edit Server Profile  ${pts3_profile_move}
    Wait For Task2  ${resp}   timeout=900    interval=10

OVF2161 Synergy PTS3 Verify the Profile after Move
    Verify Server Profile  ${pts3_profile_move}

OVF2161 Synergy PTS3 Verify RIS SecureBoot Settings after Move
     Verify RIS node  ${ris_node_sht_gen10_sy660_server1_secure_boot_enabled}

OVF2161 Synergy PTS3 Power On the Servers after Move
    Power On Servers in Profiles  ${pts3_profiles_move}
    Wait for Servers in Profiles to reach POST State  ${pts3_profiles_move}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF2161 Synergy PTS3 Verify RIS SecureBoot Settings after Power On after Move
    Verify RIS node  ${ris_node_sht_gen10_sy660_server1_secure_boot_enabled_power_on}

OVF2161 Synergy PTS3 Edit the Profile
    Power Off Server  ${PTS3_PROFILE_EDIT_SERVER}  powerControl=PressAndHold
    ${resp}=  Edit Server Profile  ${pts3_profile_edit}
    Wait For Task2  ${resp}   timeout=900    interval=10

OVF2161 Synergy PTS3 Verify the Profiles after Edit
    Verify Server Profile  ${pts3_profile_edit}

OVF2161 Synergy PTS3 Verify RIS SecureBoot Settings after Edit
     Verify RIS node  ${ris_node_sht_gen10_sy660_server1_secure_boot_disabled}

OVF2161 Synergy PTS3 Power On the Servers after Edit
    Power On Servers in Profiles  ${pts3_profiles_edit}
    Wait for Servers in Profiles to reach POST State  ${pts3_profiles_edit}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF2161 Synergy PTS3 Verify RIS SecureBoot Settings after Power On after Edit
    Verify RIS node  ${ris_node_sht_gen10_sy660_server1_secure_boot_disabled_power_on}

OVF2161 Synergy PTS3 Move Back the Profile
    Power Off Server  ${PTS3_PROFILE_EDIT_SERVER}  powerControl=PressAndHold
    Power Off Server  ${PTS3_PROFILE_MOVE_BACK_SERVER}  powerControl=PressAndHold
    ${resp}=  Edit Server Profile  ${pts3_profile_move_back}
    Wait For Task2  ${resp}   timeout=900    interval=10

OVF2161 Synergy PTS3 Verify the Profiles after Move Back
    Verify Server Profile  ${pts3_profile_move_back}

OVF2161 Synergy PTS3 Verify RIS SecureBoot Settings after Move Back
    Verify RIS node  ${ris_node_sht_gen10_sy480_server1_secure_boot_disabled}

OVF2161 Synergy PTS3 Power On the Servers after Move Back
    Power On Servers in Profiles  ${pts3_profiles_delete}
    Wait for Servers in Profiles to reach POST State  ${pts3_profiles_delete}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF2161 Synergy PTS3 Verify RIS SecureBoot Settings after Power On after Move Back
    Verify RIS node  ${ris_node_sht_gen10_sy480_server1_secure_boot_disabled_power_on}

OVF2161 Synergy PTS3 Delete the profiles
    Power off Servers in Profiles  ${pts3_profiles_delete}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts3_profiles_delete}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF2161 Synergy PTS4 Create the SPTs
    ${resplist}=  Add Server Profile Templates from variable	 ${pts4_spts_create}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF2161 Synergy PTS4 Verify the SPTs after Create
    Verify Server Profile Templates  ${pts4_spts_create}

OVF2161 Synergy PTS4 Create the profiles from SPTs
    Power Off Servers in Profiles  ${pts4_profiles_create}
    ${resplist}=  Add Server Profiles from variable	 ${pts4_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF2161 Synergy PTS4 Verify the Profiles after Create
    Run Keyword for List  ${pts4_profiles_create}  Verify Server Profile

OVF2161 Synergy PTS4 Verify RIS SecureBoot Settings after Create
    Verify RIS nodes for list  ${pts4_ris_nodes_after_create}

OVF2161 Synergy PTS4 Power On the Servers After Create
    Power On Servers in Profiles  ${pts4_profiles_create}
    Wait for Servers in Profiles to reach POST State  ${pts4_profiles_create}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF2161 Synergy PTS4 Verify RIS SecureBoot Settings after Power on after Create
    Verify RIS nodes for list  ${pts4_ris_nodes_after_power_on_after_create}

OVF2161 Synergy PTS4 Edit the profiles to associate with the SPTs
    Power Off Servers in Profiles  ${pts4_profiles_edit}
    ${resplist}=  Edit Server Profiles from variable	 ${pts4_profiles_edit}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF2161 Synergy PTS4 Verify the Profiles after Edit
    Run Keyword for List  ${pts4_profiles_edit}  Verify Server Profile

OVF2161 Synergy PTS4 Verify the Profiles Compliance after Edit
    Run Keyword for List  ${pts4_profiles_edit_compliance}  Verify Server Profile Compliance

OVF2161 Synergy PTS4 Verify RIS SecureBoot Settings after Edit
    Verify RIS nodes for list  ${pts4_ris_nodes_after_edit}

OVF2161 Synergy PTS4 Power On the Servers After Edit
    Power On Servers in Profiles  ${pts4_profiles_edit}
    Wait for Servers in Profiles to reach POST State  ${pts4_profiles_edit}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF2161 Synergy PTS4 Verify RIS SecureBoot Settings after Power On after Edit
    Verify RIS nodes for list  ${pts4_ris_nodes_after_power_on_after_edit}

OVF2161 Synergy PTS4 Update the Profiles From Template
    Power off Servers in Profiles  ${pts4_profiles_create}
    ${resplist}=  Update Server Profiles from Template  ${pts4_profiles_create}
    Wait For Task2  ${resplist}   timeout=600    interval=10

OVF2161 Synergy PTS4 Verify the Profiles after Patch
    Run Keyword for List  ${pts4_profiles_patch_expected}  Verify Server Profile

OVF2161 Synergy PTS4 Verify the Profiles Compliance after Patch
    Run Keyword for List  ${pts4_profiles_compliant_compliance}  Verify Server Profile Compliance

OVF2161 Synergy PTS4 Verify RIS SecureBoot Settings after Patch
    Verify RIS nodes for list  ${pts4_ris_nodes_after_patch}

OVF2161 Synergy PTS4 Power On the Servers After Patch
    Power On Servers in Profiles  ${pts4_profiles_create}
    Wait for Servers in Profiles to reach POST State  ${pts4_profiles_create}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF2161 Synergy PTS4 Verify RIS SecureBoot Settings after Power on after Patch
    Verify RIS nodes for list  ${pts4_ris_nodes_after_power_on_after_patch}

OVF2161 Synergy PTS4 Delete the profiles
    Power off Servers in Profiles  ${pts4_profiles_create}
    ${resplist}=  Remove Server Profiles from variable	 ${pts4_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF2161 Synergy PTS4 Remove the SPTs
    ${resplist} =  Remove Server Profile Templates from variable  ${pts4_spts_create}
    wait for task2  ${resplist}  timeout=900  interval=10

*** Keywords ***
OVF2161 Synergy Setup
    [Documentation]  OVF2161 Synergy Setup
    Set Log Level	TRACE
    ${feature} =  set variable  OVF2161 Synergy
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

    # Clean up profiles
    Power Off Servers in Profiles  ${suite_setup_profiles}  powerControl=PressAndHold
    ${resplist} =  Remove Server Profiles from variable  ${suite_setup_profiles}
    Wait for task2  ${resplist}  timeout=3600  interval=10

OVF2161 Synergy Teardown
    [Documentation]  OVF2161 Synergy Teardown
    Set Log Level	TRACE
    ${feature} =  set variable  OVF2161 Synergy
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

    # Create the profiles to put the blades in correct boot mode, power on the servers, and delete the profiles
    Log  ${feature} Suite Teardown: Start create profiles to put the blades in correct boot mode and delete the profiles  console=True
    Power Off Servers in Profiles  ${suite_teardown_profiles}  powerControl=PressAndHold
    ${resplist}=  Add Server Profiles from variable	 ${suite_teardown_profiles}
    Wait for Task2  ${resplist}  timeout=3600  interval=10
    Power on Servers in Profiles  ${suite_teardown_profiles}
    Wait for Servers in Profiles to reach POST State  ${suite_teardown_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s
    Power off Servers in Profiles  ${suite_teardown_profiles}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${suite_teardown_profiles}  force=${True}
    Wait for Task2  ${resplist}  timeout=3600  interval=10
    Log  ${feature} Suite Teardown: Finish create profiles to put the blades in UEFI mode and delete the profiles  console=True
