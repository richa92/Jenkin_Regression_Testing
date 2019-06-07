*** Settings ***
Documentation       F791 and F1174 software iSCSI boot on Tbird with CHAP/MCHCAP support
Suite Setup         F791 F1174 Synergy Setup
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
F791 F1174 Synergy TS0 Login the Appliance
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

F791 F1174 Synergy TS0 Create the Negative Profiles
    Power off All Servers  control=PressAndHold
    Run Negative Tasks for List  ${negative_profile_tasks}  timeout=120    interval=10

F791 F1174 Synergy TS1 Get the Interconnects Port Status
    Run Keyword for List    ${interconnects_expected}   Get Interconnect Port Status

F791 F1174 Synergy TS1 Create the Profiles
    Power Off Servers in Profiles  ${ts1_create_profiles}  powerControl=PressAndHold
    ${resplist}=  Add Server Profiles from variable	 ${ts1_create_profiles}
    Wait for Task2  ${resplist}  timeout=3600  interval=10

F791 F1174 Synergy TS1 Get the iSCSI Pending Settings after Create
    Run Keyword for List with kwargs  ${ris_nodes_iscsi_settings_create}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS1 Power on the Servers and Boot to POST after Create
    Power on Servers in Profiles  ${ts1_create_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts1_create_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

F791 F1174 Synergy TS1 Get the iSCSI Current Settings after Create
    Run Keyword for List with kwargs  ${ts1_ris_nodes_after_create}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS1 Verify iSCSI Current Settings after Create
    Verify RIS nodes for list  ${ts1_ris_nodes_after_create}

F791 F1174 Synergy TS1 Check Volume Connected Sessions after Create
    CLIQ Check Volume Connected Sessions in profiles  ${ts1_create_profiles}  timeout=10m  interval=10s

F791 F1174 Synergy TS1 Get the Volume Info after Create
    CLIQ Get Volume Info in profiles  ${ts1_create_profiles}

F791 F1174 Synergy TS1 Edit the Profiles First Time
    Power Off Servers in Profiles  ${ts1_edit_profiles_1}  powerControl=PressAndHold
    ${resplist}=  Edit Server Profiles from variable	 ${ts1_edit_profiles_1}
    Wait for Task2  ${resplist}  timeout=3600  interval=10

F791 F1174 Synergy TS1 Get the iSCSI Pending Settings after Edit First Time
    Run Keyword for List with kwargs  ${ris_nodes_iscsi_settings_create}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS1 Power on the Servers and Boot to POST after Edit First Time
    Power on Servers in Profiles  ${ts1_edit_profiles_1}
    Wait for Servers in Profiles to reach POST State  ${ts1_edit_profiles_1}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

F791 F1174 Synergy TS1 Get the iSCSI Current Settings after Edit First Time
    Run Keyword for List with kwargs  ${ts1_ris_nodes_after_edit_1}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS1 Verify iSCSI Current Settings after Edit First Time
    Verify RIS nodes for list  ${ts1_ris_nodes_after_edit_1}

F791 F1174 Synergy TS1 Check Volume Connected Sessions after Edit First Time
    CLIQ Check Volume Connected Sessions in profiles  ${ts1_edit_profiles_1}  timeout=10m  interval=10s

F791 F1174 Synergy TS1 Get the Volume Info after Edit First Time
    CLIQ Get Volume Info in profiles  ${ts1_edit_profiles_1}

F791 F1174 Synergy TS1 Edit the Profiles Second Time
    Power Off Servers in Profiles  ${ts1_edit_profiles_2}  powerControl=PressAndHold
    ${resplist}=  Edit Server Profiles from variable	 ${ts1_edit_profiles_2}
    Wait for Task2  ${resplist}  timeout=3600  interval=10

F791 F1174 Synergy TS1 Get the iSCSI Pending Settings after Edit Second Time
    Run Keyword for List with kwargs  ${ris_nodes_iscsi_settings_create}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS1 Power on the Servers and Boot to POST after Edit Second Time
    Power on Servers in Profiles  ${ts1_edit_profiles_2}
    Wait for Servers in Profiles to reach POST State  ${ts1_edit_profiles_2}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

F791 F1174 Synergy TS1 Get the iSCSI Current Settings after Edit Second Time
    Run Keyword for List with kwargs  ${ts1_ris_nodes_after_edit_2}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS1 Verify iSCSI Current Settings after Edit Second Time
    Verify RIS nodes for list  ${ts1_ris_nodes_after_edit_2}

F791 F1174 Synergy TS1 Check Volume Connected Sessions after Edit Second Time
    CLIQ Check Volume Connected Sessions in profiles  ${ts1_edit_profiles_2}  timeout=10m  interval=10s

F791 F1174 Synergy TS1 Get the Volume Info after Edit Second Time
    CLIQ Get Volume Info in profiles  ${ts1_edit_profiles_2}

F791 F1174 Synergy TS1 Delete the Profiles
    # remove the profiles. power on and off the servers to clear the iSCSI settings in RIS/RBSU.
    Power off Servers in Profiles  ${ts1_delete_profiles}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${ts1_delete_profiles}  force=${True}
    Wait for Task2  ${resplist}  timeout=3600  interval=10

F791 F1174 Synergy TS1 Verify iSCSI Current Settings after Delete
    Power on Servers in Profiles  ${ts1_all_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts1_all_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=30s
    Verify RIS nodes for list  ${ts1_ris_nodes_after_delete}

F791 F1174 Synergy TS1 Get the Volume Info after Delete
    CLIQ Get Volume Info in profiles  ${ts1_all_profiles}

F791 F1174 Synergy TS1 Power Off the Servers
    Power off Servers in Profiles  ${ts1_all_profiles}  powerControl=PressAndHold

F791 F1174 Synergy TS2 Get the Interconnects Port Status
    Run Keyword for List    ${interconnects_expected}   Get Interconnect Port Status

F791 F1174 Synergy TS2 Create the Profiles
    Power Off Servers in Profiles  ${ts2_create_profiles}  powerControl=PressAndHold
    ${resplist}=  Add Server Profiles from variable	 ${ts2_create_profiles}
    Run Keyword for List with kwargs  ${resplist}  Wait For Task2   timeout=3600    interval=10

F791 F1174 Synergy TS2 Get the iSCSI Pending Settings after Create
    Run Keyword for List with kwargs  ${ris_nodes_iscsi_settings_create}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS2 Power on the Servers and Boot to POST after Create
    Power on Servers in Profiles  ${ts2_create_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts2_create_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

F791 F1174 Synergy TS2 Get the iSCSI Current Settings after Create
    Run Keyword for List with kwargs  ${ts2_ris_nodes_after_create}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS2 Verify iSCSI Current Settings after Create
    Verify RIS nodes for list  ${ts2_ris_nodes_after_create}

F791 F1174 Synergy TS2 Check Volume Connected Sessions after Create
    CLIQ Check Volume Connected Sessions in profiles  ${ts2_create_profiles}  timeout=10m  interval=10s

F791 F1174 Synergy TS2 Get the Volume Info after Create
    CLIQ Get Volume Info in profiles  ${ts2_create_profiles}

F791 F1174 Synergy TS2 Edit the Profiles First Time
    Power Off Servers in Profiles  ${ts2_edit_profiles_1}  powerControl=PressAndHold
    ${resplist}=  Edit Server Profiles from variable	 ${ts2_edit_profiles_1}
    Wait for Task2  ${resplist}  timeout=3600  interval=10

F791 F1174 Synergy TS2 Get the iSCSI Pending Settings after Edit First Time
    Run Keyword for List with kwargs  ${ris_nodes_iscsi_settings_create}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS2 Power on the Servers and Boot to POST after Edit First Time
    Power on Servers in Profiles  ${ts2_edit_profiles_1}
    Wait for Servers in Profiles to reach POST State  ${ts2_edit_profiles_1}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

F791 F1174 Synergy TS2 Get the iSCSI Current Settings after Edit First Time
    Run Keyword for List with kwargs  ${ts2_ris_nodes_after_edit_1}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS2 Verify iSCSI Current Settings after Edit First Time
    Verify RIS nodes for list  ${ts2_ris_nodes_after_edit_1}

F791 F1174 Synergy TS2 Check Volume Connected Sessions after Edit First Time
    CLIQ Check Volume Connected Sessions in profiles  ${ts2_edit_profiles_1}  timeout=10m  interval=10s

F791 F1174 Synergy TS2 Get the Volume Info after Edit First Time
    CLIQ Get Volume Info in profiles  ${ts2_edit_profiles_1}

F791 F1174 Synergy TS2 Edit the Profiles Second Time
    Power Off Servers in Profiles  ${ts2_edit_profiles_2}  powerControl=PressAndHold
    ${resplist}=  Edit Server Profiles from variable	 ${ts2_edit_profiles_2}
    Wait for Task2  ${resplist}  timeout=3600  interval=10

F791 F1174 Synergy TS2 Get the iSCSI Pending Settings after Edit Second Time
    Run Keyword for List with kwargs  ${ris_nodes_iscsi_settings_create}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS2 Power on the Servers and Boot to POST after Edit Second Time
    Power on Servers in Profiles  ${ts2_edit_profiles_2}
    Wait for Servers in Profiles to reach POST State  ${ts2_edit_profiles_2}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

F791 F1174 Synergy TS2 Get the iSCSI Current Settings after Edit Second Time
    Run Keyword for List with kwargs  ${ts2_ris_nodes_after_edit_2}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS2 Verify iSCSI Current Settings after Edit Second Time
    Verify RIS nodes for list  ${ts2_ris_nodes_after_edit_2}

F791 F1174 Synergy TS2 Check Volume Connected Sessions after Edit Second Time
    CLIQ Check Volume Connected Sessions in profiles  ${ts2_edit_profiles_2}  timeout=10m  interval=10s

F791 F1174 Synergy TS2 Get the Volume Info after Edit Second Time
    CLIQ Get Volume Info in profiles  ${ts2_edit_profiles_2}

F791 F1174 Synergy TS2 Edit the Profiles Third Time
    Power Off Servers in Profiles  ${ts2_edit_profiles_3}  powerControl=PressAndHold
    ${resplist}=  Edit Server Profiles from variable	 ${ts2_edit_profiles_3}
    Wait for Task2  ${resplist}  timeout=3600  interval=10

F791 F1174 Synergy TS2 Get the iSCSI Pending Settings after Edit Third Time
    Run Keyword for List with kwargs  ${ris_nodes_iscsi_settings_create}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS2 Power on the Servers and Boot to POST after Edit Third Time
    Power on Servers in Profiles  ${ts2_edit_profiles_3}
    Wait for Servers in Profiles to reach POST State  ${ts2_edit_profiles_3}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

F791 F1174 Synergy TS2 Get the iSCSI Current Settings after Edit Third Time
    Run Keyword for List with kwargs  ${ts2_ris_nodes_after_edit_3}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS2 Verify iSCSI Current Settings after Edit Third Time
    Verify RIS nodes for list  ${ts2_ris_nodes_after_edit_3}

F791 F1174 Synergy TS2 Check Volume Connected Sessions after Edit Third Time
    CLIQ Check Volume Connected Sessions in profiles  ${ts2_edit_profiles_3}  timeout=10m  interval=10s

F791 F1174 Synergy TS2 Get the Volume Info after Edit Third Time
    CLIQ Get Volume Info in profiles  ${ts2_edit_profiles_3}

F791 F1174 Synergy TS2 Move the Profile
    Power Off Servers in Profiles  ${ts2_all_profiles}  powerControl=PressAndHold
    ${resplist}=  Edit Server Profiles from variable	 ${ts2_move_profiles}
    Wait for Task2  ${resplist}  timeout=3600  interval=10

F791 F1174 Synergy TS2 Get the iSCSI Pending Settings after Move
    Run Keyword for List with kwargs  ${ris_nodes_iscsi_settings_move}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS2 Power on the Servers and Boot to POST after Move
    Power on Servers in Profiles  ${ts2_move_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts2_move_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=30s

F791 F1174 Synergy TS2 Get the iSCSI Current Settings after Move
    Run Keyword for List with kwargs  ${ts2_ris_nodes_after_move}  Get Ris Node  VERBOSE=True

F791 F1174 Synergy TS2 Verify iSCSI Current Settings after Move
    Verify RIS nodes for list  ${ts2_ris_nodes_after_move}

F791 F1174 Synergy TS2 Check Volume Connected Sessions after Move
    CLIQ Check Volume Connected Sessions in profiles  ${ts2_move_profiles}  timeout=10m  interval=10s

F791 F1174 Synergy TS2 Get the Volume Info after Move
    CLIQ Get Volume Info in profiles  ${ts2_move_profiles}

F791 F1174 Synergy TS2 Delete the Profiles
    # remove the profiles. power on and off the servers to clear the iSCSI settings in RIS/RBSU.
    Power off Servers in Profiles  ${ts2_delete_profiles}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${ts2_delete_profiles}  force=${True}
    Wait for Task2  ${resplist}  timeout=3600  interval=10

F791 F1174 Synergy TS2 Verify iSCSI Current Settings after Delete
    Power on Servers in Profiles  ${ts2_all_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts2_all_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=30s
    Verify RIS nodes for list  ${ts2_ris_nodes_after_delete}

F791 F1174 Synergy TS2 Get the Volume Info after Delete
    CLIQ Get Volume Info in profiles  ${ts2_all_profiles}

F791 F1174 Synergy TS2 Power Off the Servers
    Power off Servers in Profiles  ${ts2_all_profiles}  powerControl=PressAndHold

*** Keywords ***
F791 F1174 Synergy Setup
    [Documentation]  F791 F1174 Synergy Setup
    Set Log Level	TRACE
    ${feature} =  set variable  F791 F1174
    log  ${feature} Suite Setup: Start check preconditions  console=True

    # Verify the interconnects linked ports
    log  ${feature} Suite Setup: Start verify the interconnects linked ports  console=True
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    Run Keyword for List  ${interconnects_linked_ports_expected}  check interconnect linked port status
    log  ${feature} Suite Setup : Finish verify the interconnects linked ports  console=True

    # Create the profiles to put the blades in UEFI and legacy BIOS mode, power on the servers, and delete the profiles
    log  ${feature} Suite Setup: Start create profiles to put the blades in UEFI mode and delete  console=True
    Power off Servers in Profiles  ${suite_setup_profiles}  powerControl=PressAndHold
    ${resplist}=  Add Server Profiles from variable	 ${suite_setup_profiles}
    Wait for Task2  ${resplist}  timeout=3600  interval=10
    Power on Servers in Profiles  ${suite_setup_profiles}
    Wait for Servers in Profiles to reach POST State  ${suite_setup_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s
    Power off Servers in Profiles  ${suite_setup_profiles}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${suite_setup_profiles}  force=${True}
    Wait for Task2  ${resplist}  timeout=3600  interval=10
    log  ${feature} Suite Setup: Finish create profiles to put the blades in UEFI mode and delete  console=True

	# Power on the servers and verify iSCSI Current Settings
	log  ${feature} Suite Setup: Start power on servers iLO and verify iSCSI current settings  console=True
	Power on Servers in Profiles  ${ts2_all_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts2_all_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s
    Verify RIS nodes for list  ${ts2_ris_nodes_after_delete}
	Power off Servers in Profiles  ${ts2_all_profiles}  powerControl=PressAndHold
	log  ${feature} Suite Setup: Finish power on servers iLO and verify iSCSI current settings  console=True

    # Get the iSCSI current settings
    log  ${feature} Suite Setup: Start get iSCSI current settings  console=True
    Run Keyword for List with kwargs  ${ts2_ris_nodes_after_delete}  Get Ris Node  VERBOSE=True
    log  ${feature} Suite Setup: Finish get iSCSI current settings  console=True

    # Get the volume info in profiles
    log  ${feature} Suite Setup: Start get volume info in profiles  console=True
    CLIQ Get Volume Info in profiles  ${ts2_all_profiles}
    log  ${feature} Suite Setup: Finish get volume info in profiles  console=True

    log  ${feature} Suite Setup: Finish check preconditions  console=True
	fusion api logout appliance
