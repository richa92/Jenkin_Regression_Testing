*** Settings ***
Documentation       F313
Suite Setup         Run Keywords    Set Log Level	TRACE
...          AND                Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
...          AND                Add Base resources
...          AND                Add and Edit the Storage Systems
...          AND                Edit the Storage Pools to Managed
...          AND                Create the Storage Volume Templates
...          AND                Create the Storage Volumes
Suite Teardown      Run Keywords    Set Log Level	TRACE
...          AND                Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
...          AND                Remove All Server Profiles
...          AND                Delete Base Storage Resources
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		16.114.209.223

${DATA_FILE}         Regression_Data.py
${SSH_PASS}          hpvse1
${FUSION_IP}         ${APPLIANCE_IP}

*** Test Cases ***
TS0 Login the Appliance
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    
Create a server Profile with StoreVirtual with unique volumes that has the same IQN(Multiple LUN Per Target)
    Power Off Servers in Profiles    ${Multiple_LUN_Per_Target}
    ${list}=  Add Server Profiles from variable	 ${Multiple_LUN_Per_Target}
    Run Keyword for List with kwargs  ${list}  Wait For Task2   timeout=3600    interval=10
    Verify Server Profile        ${verify_Multiple_LUN_Per_Target}

Remove blade by Efuse then validate profile
    #${blade_details}=    Get blade details by profile     ${verify_Multiple_LUN_Per_Target}
    ${name} =  Get From Dictionary  ${verify_Multiple_LUN_Per_Target}  name
    ${profile}=    Get Resource  SP:${name}
    Log to console and logfile  	\t Efuse On for profile ${name}
    Efuse blade by profile    ${verify_Multiple_LUN_Per_Target}    EFuseOn
    Log to console and logfile  	\t Waiting for profile to be in Updating state
    Wait Until Keyword Succeeds    10 min   2s        Profile In Updating State    ${profile}
    Wait Until Keyword Succeeds    10 min   2s        Profile In Normal State    ${profile}
    Log to console and logfile  	\t Waiting for profile to be in Critical Status
    Wait Until Keyword Succeeds    5 min   90s        Profile In Critical Status    ${profile}
    Log to console and logfile  	\t Verifying ${name} after server removed
    Sleep  20s
    Verify Server Profile        ${verify_efuse_on}

Reinsert blade by Efuse then validate profile   
    ${name} =  Get From Dictionary  ${verify_Multiple_LUN_Per_Target}  name
    ${profile}=    Get Resource  SP:${name} 
    Log to console and logfile  	\t Efuse Off for profile ${name}
    Efuse blade by profile    ${verify_Multiple_LUN_Per_Target}    EFuseOff
    Log to console and logfile  	\t Waiting for profile to be in Updating state
    Wait Until Keyword Succeeds    10 min   10s        Profile In Updating State    ${profile}
    Log to console and logfile  	\t Waiting for profile to be in Normal state
    Wait Until Keyword Succeeds    10 min   2s        Profile In Normal State    ${profile}
    Log to console and logfile  	\t Waiting for profile to be in OK state
    Wait Until Keyword Succeeds    10 min   20s        Profile In OK Status    ${profile}
    Sleep  20s
    Log to console and logfile  	\t Verifying ${name} after server inserted
    Verify Server Profile        ${verify_Multiple_LUN_Per_Target}

Delete Multiple_LUN_Per_Target Profile and validate volumes
    ${Ephemeral_vols}=    Get Ephemeral Volumes    ${verify_Multiple_LUN_Per_Target}
    ${perm_vols}=    Get Permanent Volumes    ${verify_Multiple_LUN_Per_Target}
    ${perm_count}=    Get Length    ${perm_vols}
    ${Ephemeral_count}=    Get Length    ${Ephemeral_vols}
    Power Off Servers in Profiles    ${Multiple_LUN_Per_Target}
    ${tasks}=  Remove Server Profile	 ${verify_Multiple_LUN_Per_Target}  force=${True}
    Wait For Task2  ${tasks}     timeout=900    interval=10
    Run keyword if   ${perm_count} > 0     Verify Permanent Volumes after profile delete    ${perm_vols}
    Run keyword if   ${Ephemeral_count} > 0    Verify Ephemaral Volumes removed after profile delete    ${Ephemeral_vols}

Create a Server Profile with a private/existing StoreVirtual Volume with ISCSI Function connection(Untagged)
    Power Off Servers in Profiles    ${isci_untagged}
    ${list}=  Add Server Profiles from variable	 ${isci_untagged}
    Run Keyword for List with kwargs  ${list}  Wait For Task2   timeout=3600    interval=10
    Verify Server Profile        ${verify_isci_untagged}

Delete isci_untagged Profile and validate volumes
    ${Ephemeral_vols}=    Get Ephemeral Volumes    ${verify_isci_untagged}
    ${perm_vols}=    Get Permanent Volumes    ${verify_isci_untagged}
    ${perm_count}=    Get Length    ${perm_vols}
    ${Ephemeral_count}=    Get Length    ${Ephemeral_vols}
    Power Off Servers in Profiles    ${Multiple_LUN_Per_Target}
    ${tasks}=  Remove Server Profile	 ${verify_isci_untagged}  force=${True}
    Wait For Task2  ${tasks}     timeout=900    interval=10
    Run keyword if   ${perm_count} > 0     Verify Permanent Volumes after profile delete    ${perm_vols}
    Run keyword if   ${Ephemeral_count} > 0    Verify Ephemaral Volumes removed after profile delete    ${Ephemeral_vols}

Create a Server Profile with a private/existing StoreVirtual Volume with Ethernet Function connection(Tunnel)
    Power Off Servers in Profiles    ${ethernet_tunnel}
    ${list}=  Add Server Profiles from variable    ${ethernet_tunnel}
    Run Keyword for List with kwargs  ${list}  Wait For Task2   timeout=3600    interval=10
    verify server profile    ${verify_ethernet_tunnel}
 
Delete ethernet_tunnel Profile and validate volumes
    ${Ephemeral_vols}=    Get Ephemeral Volumes    ${verify_ethernet_tunnel}
    ${perm_vols}=    Get Permanent Volumes    ${verify_ethernet_tunnel}
    ${perm_count}=    Get Length    ${perm_vols}
    ${Ephemeral_count}=    Get Length    ${Ephemeral_vols}
    Power Off Servers in Profiles    ${ethernet_tunnel}
    ${tasks}=  Remove Server Profile	 ${verify_ethernet_tunnel}  force=${True}
    Wait For Task2  ${tasks}     timeout=900    interval=10
    Run keyword if   ${perm_count} > 0     Verify Permanent Volumes after profile delete    ${perm_vols}
    Run keyword if   ${perm_count} > 0     Verify Ephemaral Volumes removed after profile delete    ${Ephemeral_vols}

Create a an unassigned server profile with StoreVirtual Volumes
    ${list}=  Add Server Profiles from variable	 ${unassigned_profile_new_n_existing_volumes}
    Run Keyword for List with kwargs  ${list}  Wait For Task2   timeout=3600    interval=10
    Verify Server Profile        ${verify_unassigned_profile_new_n_existing_volumes}

Assign server hardware to unassigned profile with StoreVirual Volumes
    ${list}=     Edit Server Profiles from variable    ${assigned_profile_new_n_existing_volumes}
    Power Off Servers in Profiles    ${assigned_profile_new_n_existing_volumes}
    Run Keyword for List with kwargs  ${list}  Wait For Task2   timeout=3600    interval=10
    Verify Server Profile    ${verify_assigned_profile_new_n_existing_volumes}

Move Server profile with existing StoreVirtual volumes
    ${list}=  Edit Server Profiles from variable    ${move_profile_new_and_existing_volumes}
    Run Keyword for List with kwargs  ${list}  Wait For Task2   timeout=3600    interval=10
    verify server profile    ${verify_move_profile_new_and_existing_volumes}

Delete move_profile and validate volumes
    ${Ephemeral_vols}=    Get Ephemeral Volumes    ${verify_move_profile_new_and_existing_volumes}
    ${perm_vols}=    Get Permanent Volumes    ${verify_move_profile_new_and_existing_volumes}
    ${perm_count}=    Get Length    ${perm_vols}
    ${Ephemeral_count}=    Get Length    ${Ephemeral_vols}
    Power Off Servers in Profiles    ${move_profile_new_and_existing_volumes}
    ${tasks}=  Remove Server Profile	 ${verify_move_profile_new_and_existing_volumes}  force=${True}
    Wait For Task2  ${tasks}     timeout=900    interval=10
    Run keyword if   ${perm_count} > 0     Verify Permanent Volumes after profile delete    ${perm_vols}
    Run keyword if   ${Ephemeral_count} > 0     Verify Ephemaral Volumes removed after profile delete    ${Ephemeral_vols}

Create a Server profile with an new Private and Shared StoreVirtual
    Power Off Servers in Profiles    ${new_private_share_sp}
    ${list}=  Add Server Profiles from variable	 ${new_private_share_sp}
    Run Keyword for List with kwargs  ${list}  Wait For Task2   timeout=3600    interval=10
    Verify Server Profile        ${verify_new_private_share_sp}

Delete new private_share Profile and validate volumes
    ${Ephemeral_vols}=    Get Ephemeral Volumes    ${verify_new_private_share_sp}
    ${perm_vols}=    Get Permanent Volumes    ${verify_new_private_share_sp}
    ${perm_count}=    Get Length    ${perm_vols}
    ${Ephemeral_count}=    Get Length    ${Ephemeral_vols}
    Power Off Servers in Profiles    ${new_private_share_sp}
    ${tasks}=  Remove Server Profile	 ${verify_new_private_share_sp}  force=${True}
    Wait For Task2  ${tasks}     timeout=900    interval=10
    Run keyword if   ${perm_count} > 0     Verify Permanent Volumes after profile delete    ${perm_vols}
    Run keyword if   ${Ephemeral_count} > 0     Verify Ephemaral Volumes removed after profile delete    ${Ephemeral_vols}

Create a Server profile with an existing Private and Shared StoreVirtual
    Power Off Servers in Profiles    ${existing_private_share_sp}
    ${list}=  Add Server Profiles from variable	 ${existing_private_share_sp}
    Run Keyword for List with kwargs  ${list}  Wait For Task2   timeout=3600    interval=10
    Verify Server Profile        ${verify_existing_private_share_sp}

Delete existing_private_share Profile and validate volumes
    ${Ephemeral_vols}=    Get Ephemeral Volumes    ${verify_existing_private_share_sp}
    ${perm_vols}=    Get Permanent Volumes    ${verify_existing_private_share_sp}
    ${perm_count}=    Get Length    ${perm_vols}
    ${Ephemeral_count}=    Get Length    ${Ephemeral_vols}
    Power Off Servers in Profiles    ${existing_private_share_sp}
    ${tasks}=  Remove Server Profile	 ${verify_existing_private_share_sp}  force=${True}
    Wait For Task2  ${tasks}     timeout=900    interval=10
    Run keyword if   ${perm_count} > 0     Verify Permanent Volumes after profile delete    ${perm_vols}
    Run keyword if   ${Ephemeral_count} > 0     Verify Ephemaral Volumes removed after profile delete    ${Ephemeral_vols}

Create a server profile with no StoreVirtual Volumes for Edit
    Power Off Servers in Profiles    ${edit_profile}
    ${list}=  Add Server Profiles from variable	 ${edit_profile}
    Run Keyword for List with kwargs  ${list}  Wait For Task2   timeout=3600    interval=10

Edit a server profile - Add existing and new StoreVirtual Volume
    ${list}=  Edit Server Profiles from variable    ${edit_profile_new_and_existing_volumes}
    Run Keyword for List with kwargs  ${list}  Wait For Task2   timeout=3600    interval=10
    verify server profile    ${verify_edit_profile_new_and_existing_volumes}

Delete edit_profile_new_and_existing_volumes Profile and validate volumes
    ${Ephemeral_vols}=    Get Ephemeral Volumes    ${verify_edit_profile_new_and_existing_volumes}
    ${perm_vols}=    Get Permanent Volumes    ${verify_edit_profile_new_and_existing_volumes}
    ${perm_count}=    Get Length    ${perm_vols}
    ${Ephemeral_count}=    Get Length    ${Ephemeral_vols}
    Power Off Servers in Profiles    ${edit_profile_new_and_existing_volumes}
    ${tasks}=  Remove Server Profile	 ${verify_edit_profile_new_and_existing_volumes}  force=${True}
    Wait For Task2  ${tasks}     timeout=900    interval=10
    Run keyword if   ${perm_count} > 0     Verify Permanent Volumes after profile delete    ${perm_vols}
    Run keyword if   ${Ephemeral_count} > 0     Verify Ephemaral Volumes removed after profile delete    ${Ephemeral_vols}

TS0 Create the Negative Profiles Validation Errors
    Run Negative Tasks for List  ${ts0_negative_profile_tasks}  timeout=900    interval=10

TS1 Create the Negative Profiles Volume Attachment Failures
    Power Off Servers in Profiles  ${ts1_profiles_delete}
    Run Negative Tasks for List  ${ts1_negative_profile_tasks}  timeout=900    interval=10


*** Keywords ***

Efuse blade by profile
    [Arguments]     ${profile}    ${action}
    ${profile}=  copy dictionary     ${verify_Multiple_LUN_Per_Target}
    ${server} =  set variable  ${profile['serverHardwareUri']}
    ${server} =  replace string using regexp  ${server}  SH:  ${EMPTY}
    ${words} =  set variable  ${server.split(',')}
    ${enclosure} =  set variable  ${words[0]}
    ${bay} =  set variable  ${words[1]}
    ${bay} =  set variable  ${bay.strip()}
    ${bay} =  set variable  ${bay[-1]}
    Get EM IP
    Get EM Token    ${enclosure}
    EFuse Blade   ${action}     ${bay}

Profile In Critical Status
    [Arguments]    ${profile}
    Set Log Level    TRACE
	${profile} =   Fusion Api Get Server Profiles     ${profile['uri']}
    ${status} =  Get From Dictionary  ${profile}  status
    Log to console and logfile    \t Server Profile: [${profile['name']}] is: ${status}
    Should Match    ${status}    Critical

Profile In OK Status
    [Arguments]    ${profile}
    Set Log Level    TRACE
	${profile} =   Fusion Api Get Server Profiles     ${profile['uri']}
    ${status} =  Get From Dictionary  ${profile}  status
    Log to console and logfile    \t Server Profile: [${profile['name']}] is: ${status}
    Should Match    ${status}    OK

Profile In Updating State
    [Arguments]    ${profile}
    Set Log Level    TRACE
	${profile} =   Fusion Api Get Server Profiles     ${profile['uri']}
    ${state} =  Get From Dictionary  ${profile}  state
    Log to console and logfile    \t Server Profile: [${profile['name']}] is: ${state}
    Should Match    ${state}    Updating

Get blade details by profile
    [Arguments]     ${profile}
    ${profile}=  copy dictionary     ${verify_Multiple_LUN_Per_Target}
    ${server} =  set variable  ${profile['serverHardwareUri']}
    ${server_uri}=    Common URI lookup by name    ${server}
    ${resp}=    Get Resource     ${server_uri}
    ${blade_details} =    Create Dictionary     name=${resp['name']}
    ...                                         uri=${resp['uri']}
    ...                                         state=${resp['state']}
    ...                                         status=${resp['status']}
    [return]  ${blade_details}

check blade removed
    [Arguments]  ${blade_uri}
	Log to console and logfile  	\t Waiting for Blade to be removed
	${status}=    Check Resource Existing     ${blade_uri}	   '404'
	Log to logfile    \t Server state is: ${status}
    Should Match    ${status}    'PASS'

check blade added
    [Arguments]  ${blade_uri}
	Log to console and logfile  	\t Waiting for Blade to be added
	${status}=    Check Resource Existing     ${blade_uri}	   '200'
	Log to logfile    \t Server state is: ${status}
    Should Match    ${status}    'PASS'

Get Permanent Volumes
    [Arguments]     ${Profile}
    ${status}  ${return} =  Run Keyword and Ignore Error  	Get From Dictionary	${Profile}	sanStorage
	${sanStorage} =  set variable if  '${status}'=='PASS'  ${return}  error
    ${sanStorageCopy} =  copy dictionary  ${sanStorage}
	${volumeList}=	Get from Dictionary		${sanStorageCopy}  	volumeAttachments
	${perm_vols} =  Create List
	:FOR	${vol}	IN	@{volumeList}
	\   	${vol} =     Copy dictionary     ${vol}
	\		${resp} =  Get Resource     ${vol['volumeUri']}
	\   	Run Keyword If  '${resp['isPermanent']}'=='True'  append to list  ${perm_vols}    ${vol}
    [Return]	${perm_vols}

Get Ephemeral Volumes
    [Arguments]     ${Profile}
    ${status}  ${return} =  Run Keyword and Ignore Error  	Get From Dictionary	${Profile}	sanStorage
	${sanStorage} =  set variable if  '${status}'=='PASS'  ${return}  error
    ${sanStorageCopy} =  copy dictionary  ${sanStorage}
	${volumeList}=	Get from Dictionary		${sanStorageCopy}  	volumeAttachments
	${Ephemeral_vols} =  Create List
	:FOR	${vol}	IN	@{volumeList}
	\   	${vol} =     Copy dictionary     ${vol}
	\		${resp} =  Get Resource     ${vol['volumeUri']}
	\   	Run Keyword If  '${resp['isPermanent']}'=='False'  append to list  ${Ephemeral_vols}    ${vol}
    [Return]	${Ephemeral_vols}

Verify Permanent Volumes after profile delete
    [Arguments]     ${volumeList}
	:FOR	${vol}	IN	@{volumeList}
	\   	${vol} =     Copy dictionary     ${vol}
	\		${status}=     Check Resource Existing     ${vol['volumeUri']}	   '200'
	\   	Run Keyword If  ${status}=='FAIL'  Fail  Fail:Permanent volumes removed or not found

Verify Ephemaral Volumes removed after profile delete
    [Arguments]     ${volumeList}
	:FOR	${vol}	IN	@{volumeList}
	\   	${vol} =     Copy dictionary     ${vol}
	\		${status}=     Check Resource Existing     ${vol['volumeUri']}	   '404'
	\   	Run Keyword If  ${status}=='FAIL'  Fail  Fail:Ephermal volumes not removed or found

Add existing StoreVirtual Volumes
    Add Existing Storage Volume       ${existing_volumes}

Delete Base Storage Resources
    ${resplist} =  Remove All Storage Volumes Async  param=?suppressDeviceUpdates=false
    Wait for task2  ${resplist}  timeout=120  interval=10
	${resplist} =  Remove ALL Storage Volume Templates Async
    ${resplist} =  Remove ALL Storage Systems Async
    Wait for task2  ${resplist}  timeout=120  interval=10

Add and Edit the Storage Systems
	${resplist} =  Add Storage Systems Async  ${storage_systems}
	Wait for task2  ${resplist}  timeout=300  interval=10
	${resplist} =  Edit Storage Systems Async  ${storage_systems}
	Wait for task2  ${resplist}  timeout=300  interval=10

Edit the Storage Pools to Managed
	${resplist} =  Edit Storage Pools Async  ${storage_pools}
	Wait for task2  ${resplist}  timeout=300  interval=10

Create the Storage Volume Templates
    ${resplist} =  Add Storage Volume Templates Async  ${storage_templates}

Create the Storage Volumes
	${resplist} =  Add Storage Volumes Async  ${storage_volumes}
	Wait for task2  ${resplist}  timeout=300  interval=10

Add Base resources
	${resplist} =  Add San Managers Async  ${san_managers}
	Add FC Networks from variable  ${fc_networks}
    Wait Until Keyword Succeeds  120s  10s  Check Resource Attribute  FCSan:${FA_SAN_A}  state  Managed
	Wait Until Keyword Succeeds  120s  10s  Check Resource Attribute  FCSan:${FA_SAN_B}  state  Managed
	Add Ethernet Networks from variable	${ethernet_networks}
	Add LIG from list	${ligs}
	Add Enclosure Group from list	${enc_groups}
    Add Logical Enclosure from lists    ${les}
