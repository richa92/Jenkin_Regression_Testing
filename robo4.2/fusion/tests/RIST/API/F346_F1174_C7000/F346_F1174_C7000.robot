*** Settings ***
Documentation       F346 F1174 offload iSCSI boot on C7000 with CHAP and MCHAP
Suite Setup         F346 F1174 C7000 Setup
Library				Collections
Library             json
Library  			Dialogs
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

*** Test Cases ***
F346 F1174 C7000 Initialize the Variables
    [Tags]    F346-F1174-C7k-1
    Set Log Level	TRACE
    log variables

F346 F1174 C7000 Create the Negative Profiles
    [Tags]    F346-F1174-C7k-2
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    Power Off Servers in Profiles  ${all_profiles}
    Run Negative Tasks for List  ${negative_profile_tasks}

F346 F1174 C7000 Create the Profiles
    [Tags]    F346-F1174-C7k-3
    Power Off Servers in Profiles  ${create_profiles}
    ${resplist}=  Add Server Profiles from variable	 ${create_profiles}
    Wait for Task2  ${resplist}  timeout=3600  interval=10

F346 F1174 C7000 Verify Blade CLP after Create
    [Tags]    F346-F1174-C7k-4
    Run Keyword for List with kwargs  ${CLP_after_create}  OA CLI Verify Blade CLP

F346 F1174 C7000 Power on the Servers and Boot to POST after Create
    [Tags]    F346-F1174-C7k-5
    Power on Servers in Profiles  ${create_profiles_bootable}
    Wait for Servers in Profiles to reach POST State  ${create_profiles_bootable}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

F346 F1174 C7000 Check Volume Connected Sessions after Create
    [Tags]    F346-F1174-C7k-6
    CLIQ Check Volume Connected Sessions in profiles  ${create_profiles}  timeout=10m  interval=10s

F346 F1174 C7000 Get the Volume Info after Create
    [Tags]    F346-F1174-C7k-7
    CLIQ Get Volume Info in profiles  ${create_profiles}

F346 F1174 C7000 Verify PersistentBootConfigOrder on Gen9 after Create
    [Tags]    F346-F1174-C7k-8
    Contain String in PersistentBootConfigOrder for List  ${ris_nodes_after_create}  CONTAIN=True

F346 F1174 C7000 Edit the Profiles
    [Tags]    F346-F1174-C7k-9
    Power Off Servers in Profiles  ${edit_profiles}
    ${resplist}=  Edit Server Profiles from variable	 ${edit_profiles}
    Wait for Task2  ${resplist}  timeout=3600  interval=10

F346 F1174 C7000 Verify Blade CLP after Edit
    [Tags]    F346-F1174-C7k-10
    Run Keyword for List with kwargs  ${CLP_after_edit}  OA CLI Verify Blade CLP

F346 F1174 C7000 Power on the Servers and Boot to POST after Edit
    [Tags]    F346-F1174-C7k-11
    Power on Servers in Profiles  ${edit_profiles}
    Wait for Servers in Profiles to reach POST State  ${edit_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

F346 F1174 C7000 Check Volume Connected Sessions after Edit
    [Tags]    F346-F1174-C7k-12
    CLIQ Check Volume Connected Sessions in profiles  ${edit_profiles}  timeout=10m  interval=10s

F346 F1174 C7000 Get the Volume Info after Edit
    [Tags]    F346-F1174-C7k-13
    CLIQ Get Volume Info in profiles  ${edit_profiles}

F346 F1174 C7000 Verify PersistentBootConfigOrder on Gen9 after Edit
    [Tags]    F346-F1174-C7k-14
    Contain String in PersistentBootConfigOrder for List  ${ris_nodes_after_edit}  CONTAIN=True

F346 F1174 C7000 Move the Profiles
    [Tags]    F346-F1174-C7k-15
    Power Off Servers in Profiles  ${edit_profiles}
    Power Off Servers in Profiles  ${move_profiles}
    ${resplist}=  Edit Server Profiles from variable	 ${move_profiles}
    Wait for Task2  ${resplist}  timeout=3600  interval=10

F346 F1174 C7000 Verify Blade CLP after move
    [Tags]    F346-F1174-C7k-16
    Run Keyword for List with kwargs  ${CLP_after_move}  OA CLI Verify Blade CLP

F346 F1174 C7000 Power on the Servers and Boot to POST after Move
    [Tags]    F346-F1174-C7k-17
    Power on Servers in Profiles  ${move_profiles}
    Wait for Servers in Profiles to reach POST State  ${move_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

F346 F1174 C7000 Check Volume Connected Sessions after Move
    [Tags]    F346-F1174-C7k-18
    CLIQ Check Volume Connected Sessions in profiles  ${move_profiles}  timeout=10m  interval=10s

F346 F1174 C7000 Get the Volume Info after Move
    [Tags]    F346-F1174-C7k-19
    CLIQ Get Volume Info in profiles  ${move_profiles}

F346 F1174 C7000 Verify PersistentBootConfigOrder on Gen9 after Move
    [Tags]    F346-F1174-C7k-20
    Power on Servers in Profiles  ${gen9_move_profiles}
    Wait for Servers in Profiles to reach POST State  ${gen9_move_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s
    Contain String in PersistentBootConfigOrder for List  ${ris_nodes_after_move}  CONTAIN=True

F346 F1174 C7000 Delete the profiles
    [Tags]    F346-F1174-C7k-21
    Power off Servers in Profiles  ${delete_profiles}
    ${resplist}=  Remove Server Profiles from variable	 ${delete_profiles}  force=${True}
    Wait for Task2  ${resplist}  timeout=3600  interval=10

F346 F1174 C7000 Verify Blade CLP after Delete
    [Tags]    F346-F1174-C7k-22
    Run Keyword for List with kwargs  ${CLP_after_delete}  OA CLI Verify Blade CLP

F346 F1174 C7000 Get the volume info after Delete
    [Tags]    F346-F1174-C7k-23
    CLIQ Get Volume Info in profiles  ${all_profiles}

F346 F1174 C7000 Verify PersistentBootConfigOrder on Gen9 after Delete
    [Tags]    F346-F1174-C7k-24
    Power on Servers in Profiles  ${gen9_delete_profiles}
    Wait for Servers in Profiles to reach POST State  ${gen9_delete_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s
    Contain String in PersistentBootConfigOrder for List  ${ris_nodes_after_delete}  CONTAIN=False

F346 F1174 C7000 Gen10 profiles
    [Tags]    F346-F1174-C7k-25
    Power Off Servers in Profiles  ${create_gen10_profiles}
    ${resplist}=  Add Server Profiles from variable	 ${create_gen10_profiles}
    Wait for Task2  ${resplist}  timeout=3600  interval=10
    Run Keyword for List with kwargs  ${CLP_after_create_gen10}  OA CLI Verify Blade CLP
    Power on Servers in Profiles  ${create_gen10_profiles}
    CLIQ Get Volume Info in profiles  ${create_gen10_profiles}
    Power Off Servers in Profiles  ${edit_gen10_profiles}
    ${resplist}=  Edit Server Profiles from variable	 ${edit_gen10_profiles}
    Wait for Task2  ${resplist}  timeout=3600  interval=10
    Power off Servers in Profiles  ${delete_gen10_profiles}
    ${resplist}=  Remove Server Profiles from variable	 ${delete_gen10_profiles}  force=${True}
    Wait for Task2  ${resplist}  timeout=3600  interval=10

F346 F1174 C7000 Power Off the Servers
    [Tags]    F346-F1174-C7k-26
    Power off Servers in Profiles  ${all_profiles}
    Fusion Api Logout Appliance

*** Keywords ***
F346 F1174 C7000 Setup
    [Documentation]    F346 F1174 C7000 Setup
    Set Log Level	TRACE
    ${feature} =  set variable  F346 F1174
    Log    ${feature} Suite Setup : Start check preconditions    console=true
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

    # Verify the interconnects state
    Log    ${feature} Suite Setup: Start verify the interconnects state    console=true
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    Verify Interconnects from list  ${interconnects_expected}  state=Configured
    Log    ${feature} Suite Setup : Finish verify the interconnects state    console=true

    # Verify the servers state
    Log    ${feature} Suite Setup: Start verify servers state    console=true
    :FOR    ${profile}  IN  @{all_profiles}
    \   ${status}  ${return} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  serverHardwareUri
	\   ${name} =  set variable if  '${status}'=='PASS'  ${return}  ${None}
	\   CONTINUE FOR LOOP IF    '${name}'=='None'
	\   ${name} =  Add Category  ${name}  SH
	\   ${ilo} =  Get Server Hardware iLO IP  ${name}
	\   ${uri} =  Common URI lookup by name  ${name}
	\   ${start_state} =  Get Resource Attribute  ${name}  state
	\   Log    ${feature} Suite Setup : The server ${name} start state is ${start_state}    console=true
	\   Run keyword if  '${start_state}'!= 'NoProfileApplied'  Run cpqlocfg and Reset iLO  ${ilo}
	\   Run keyword if  '${start_state}'!= 'NoProfileApplied'  Refresh Server Hardware  ${name}
	\   Run keyword if  '${start_state}'!= 'NoProfileApplied'  Check Resource Attribute	 ${name}  state  NoProfileApplied
    Log    ${feature} Suite Setup : Finish verify servers state    console=true

    Log    ${feature} Suite Setup: Finish check preconditions    console=true
#	Fusion Api Logout Appliance
