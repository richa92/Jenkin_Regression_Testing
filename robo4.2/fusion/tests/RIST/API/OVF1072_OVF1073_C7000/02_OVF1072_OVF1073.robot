*** Settings ***
Documentation       OVF1072 OVF1073 StoreVirtual iSCSI volume attach with auto-generated MCHAP.
Suite Setup         OVF1072 OVF1073 C7000 Setup
Library				Collections
Library             json
Library  			Dialogs
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

*** Test Cases ***
OVF1072 OVF1073 C7000 TS0 Initialize the Variables
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

OVF1072 OVF1073 C7000 NTS1 Create the Profiles to Fail Validation
    Power Off Server  ${NTS1_PROFILE_SERVER}  powerControl=PressAndHold
    Run Negative Tasks for List  ${nts1_negative_profile_tasks}  timeout=900    interval=10

OVF1072 OVF1073 C7000 NTS1 Cleanup
    ${resplist} =  Remove All Server Profiles Async  force=${True}
    wait for task2  ${resplist}  timeout=600  interval=10

OVF1072 OVF1073 C7000 NTS2 Create the profiles to Fail SAN Validation
    Power Off Servers in Profiles  ${nts2_profiles_delete}
    Run Negative Tasks for List  ${nts2_negative_profile_tasks}  timeout=600  interval=10

OVF1072 OVF1073 C7000 NTS2 Delete the profiles
    Power off Servers in Profiles  ${nts2_profiles_delete}
    ${resplist}=  Remove Server Profiles from variable	 ${nts2_profiles_delete}  force=${True}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF1072 OVF1073 C7000 NTS3 Create the Profile
    ${resplist}=  Add Server Profiles from variable	 ${nts3_profiles_create}
    Wait for Task2  ${resplist}     timeout=300    interval=10

OVF1072 OVF1073 C7000 NTS3 Edit the Profile to Fail Validation
    Run Negative Tasks for List  ${nts3_negative_profile_tasks}  timeout=120    interval=10

OVF1072 OVF1073 C7000 NTS3 Delete the Profiles
    Power Off Servers in Profiles  ${nts3_profiles_create}
    ${resplist}=  Remove Server Profiles from variable  ${nts3_profiles_create}
    Wait for Task2  ${resplist}    timeout=300    interval=10

OVF1072 OVF1073 C7000 NTS4 Create the Profile
    ${resplist}=  Add Server Profiles from variable	 ${nts4_profiles_create}
    Wait for Task2  ${resplist}     timeout=300    interval=10

OVF1072 OVF1073 C7000 NTS4 Verify the Profile after Create
    Run Keyword for List  ${nts4_profiles_create_expected}  Verify Server Profile
    Run Keyword for List  ${nts4_profiles_create_expected}  Verify Server Profile Volume Attachments

OVF1072 OVF1073 C7000 NTS4 Power on the Servers
    Power On Servers in Profiles  ${nts4_profiles_create}

OVF1072 OVF1073 C7000 NTS4 Edit the Profile to Fail Power Operation Validation
    Run Negative Tasks for List  ${nts4_negative_profile_tasks}  timeout=300    interval=10

OVF1072 OVF1073 C7000 NTS4 Delete the Profiles
    Power Off Servers in Profiles  ${nts4_profiles_create}
    ${resplist}=  Remove Server Profiles from variable  ${nts4_profiles_create}
    Wait for Task2  ${resplist}    timeout=300    interval=10

OVF1072 OVF1073 C7000 PTS1 Create the Profiles
    Power Off Servers in Profiles  ${pts1_profiles_create}
    verify servers powerstate in profiles  ${pts1_profiles_create}  Off
    ${resplist}=  Add Server Profiles from variable	 ${pts1_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF1072 OVF1073 C7000 PTS1 Verify the Profiles after Create
    Run Keyword for List  ${pts1_profiles_create_expected}  Verify Server Profile
    Run Keyword for List  ${pts1_profiles_create_expected}  Verify Server Profile Volume Attachments

OVF1072 OVF1073 C7000 PTS1 Power on the Servers
    Power On Servers in Profiles  ${pts1_profiles_create}
    verify servers powerstate in profiles  ${pts1_profiles_create}  On

OVF1072 OVF1073 C7000 PTS1 Edit the Profiles SAN Attributes and Profile iQN
    verify servers powerstate in profiles  ${pts1_profiles_create}  On
    ${resplist}=  Edit Server Profiles from variable	 ${pts1_profiles_edit}
    Wait For Task2  ${resplist}  timeout=900    interval=10

OVF1072 OVF1073 C7000 PTS1 Verify the Profiles after Edit
    Run Keyword for List  ${pts1_profiles_edit_expected}  Verify Server Profile
    Run Keyword for List  ${pts1_profiles_edit_expected}  Verify Server Profile Volume Attachments

OVF1072 OVF1073 C7000 PTS1 Move the Profiles
    Power Off Servers in Profiles  ${pts1_profiles_edit}
    verify servers powerstate in profiles  ${pts1_profiles_edit}  Off
    Power Off Servers in Profiles  ${pts1_profiles_move}
    verify servers powerstate in profiles  ${pts1_profiles_move}  Off
    ${resplist}=  Edit Server Profiles from variable	 ${pts1_profiles_move}
    Wait For Task2  ${resplist}   timeout=1800    interval=10

OVF1072 OVF1073 C7000 PTS1 Verify the Profiles after Move
    Run Keyword for List  ${pts1_profiles_move_expected}  Verify Server Profile
    Run Keyword for List  ${pts1_profiles_move_expected}  Verify Server Profile Volume Attachments

OVF1072 OVF1073 C7000 PTS1 Delete the Profiles
    Power off Servers in Profiles  ${pts1_profiles_delete}
    ${resplist}=  Remove Server Profiles from variable	 ${pts1_profiles_delete}  force=${True}
    Wait For Task2  ${resplist}  timeout=900    interval=10

OVF1072 OVF1073 C7000 PTS1 Remove the Profile Permanent Volumes
    ${resplist}=  Remove Storage Volumes Async   ${new_permanent_volumes}  param=?suppressDeviceUpdates=false
    wait for task2  ${resplist}  timeout=120  interval=10

OVF1072 OVF1073 C7000 PTS2 Rip and Replace - Create the Profiles
    Power Off Servers in Profiles  ${pts1_profiles_create}
    ${resplist}=  Add Server Profiles from variable	 ${pts1_profiles_create}
    Wait For Task2  ${resplist}    timeout=900    interval=10

OVF1072 OVF1073 C7000 PTS2 Rip and Replace - Verify the Profiles after Create
    Run Keyword for List  ${pts1_profiles_create_expected}  Verify Server Profile
    Run Keyword for List  ${pts1_profiles_create_expected}  Verify Server Profile Volume Attachments

OVF1072 OVF1073 C7000 PTS2 Rip and Replace - Remove the Blade in the Profiles
    Run Keyword for List with kwargs  ${pts1_profiles_create_expected}  OA CLI EFUSE Blade in Profile  action=OFF  server_task=Remove  timeout=300s  interval=50ms

OVF1072 OVF1073 C7000 PTS2 Rip and Replace - Verify Server Profiles After Remove the Blade
    Run Keyword for List with kwargs  ${pts2_profiles_efuse_off_expected}  Verify Server Profile  status=Critical

OVF1072 OVF1073 C7000 PTS2 Rip and Replace - Add the blades in the Profiles
    Run Keyword for List with kwargs  ${pts1_profiles_create_expected}  OA CLI EFUSE Blade in Profile  action=ON  server_task=Add  timeout=300s  interval=1s

OVF1072 OVF1073 C7000 PTS2 Rip and Replace - Verify Server Profiles After Add the Blade
    Run Keyword for List  ${pts2_profiles_efuse_on_expected}  Verify Server Profile
    Run Keyword for List  ${pts2_profiles_efuse_on_expected}  Verify Server Profile Volume Attachments

OVF1072 OVF1073 C7000 PTS2 Rip and Replace - Delete the profiles
    Power off Servers in Profiles  ${pts1_profiles_create}
    ${resplist}=  Remove Server Profiles from variable	 ${pts1_profiles_create}  force=${True}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF1072 OVF1073 C7000 PTS2 Rip and Replace - Remove the Profile Permanent Volumes
    ${resplist}=  Remove Storage Volumes Async   ${new_permanent_volumes}  param=?suppressDeviceUpdates=false
    wait for task2  ${resplist}  timeout=120  interval=10

*** Keywords ***
OVF1072 OVF1073 C7000 Setup
    [Documentation]    OVF1072 OVF1073 C7000 Setup
    Set Log Level	TRACE
    ${feature} =  set variable  OVF1072 OVF1073 C7000
    Log    ${feature} Suite Setup: Start Check preconditions    console=true
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

    # Check enclsoures state
    Log    ${feature} Suite Setup: Start check enclosures state.    console=true
    :FOR    ${enclosure}  IN  @{enclosures_expected}
	\   ${start_state} =  Get Resource Attribute	 ENC:${enclosure['name']}  state
	\   Log    ${feature} Suite Setup: The enclosure ${enclosure['name']} start state is ${start_state}    console=true
	\   CONTINUE FOR LOOP IF    '${start_state}'=='Configured'
	\   ${resp} =  Refresh enclosure  ${enclosure}
	\   Wait for Task2  ${resp}  600  10
	\   Check Resource Attribute	 ENC:${enlcosure}  state  Configured
	Log    ${feature} Suite Setup: Finish check enclosures state.    console=true

    # Verify the interconnects state
    Log    ${feature} Suite Setup: Start verify the interconnects state    console=true
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    Verify Interconnects from list  ${interconnects_expected}  state=Configured
    Log    ${feature} Suite Setup : Finish verify the interconnects state    console=true

	# Check servers state, reset iLO and refresh if initial state is not NoProfileApplied
	Log    ${feature} Suite Setup: Start check servers state.    console=true
    :FOR    ${profile}  IN  @{suite_setup_profiles}
    \   ${status}  ${return} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  serverHardwareUri
	\   ${server} =  set variable if  '${status}'=='PASS'  ${return}  ${None}
	\   CONTINUE FOR LOOP IF    '${server}'=='None'
	\   ${start_state} =  Get Resource Attribute  ${server}  state
	\   Log    ${feature} Suite Setup: The server ${server} start state is ${start_state}    console=true
	\   Run keyword if  '${start_state}'!= 'NoProfileApplied'  Reset Server Hardware iLO via cpqlocfg and Wait for Refresh to Finish  ${server}
	\   Run keyword if  '${start_state}'!= 'NoProfileApplied'  Check Resource Attribute	 SH:${server}  state  NoProfileApplied
    Log    ${feature} Suite Setup: Finish check servers state.    console=true

    # Check SAN Managers state and status
    Log    ${feature} Suite Setup: Start check SAN Managers state and status.    console=true
    ${san_managers} =  Fusion Api Get San Manager
    :FOR    ${sm}  IN  @{san_managers['members']}
    \   Should match regexp  ${sm['state']}  Managed
    \   Should match regexp  ${sm['status']}  OK
    Log    ${feature} Suite Setup: Finish check SAN Managers state and status.    console=true

    # Check Storage systems state and status
    Log    ${feature} Suite Setup: Start check storage systems state and status.    console=true
    :FOR    ${ss}  IN  @{storage_systems}
    \   Log    Checking the storage system ${ss['name']}    console=true
    \   Check Resource Attribute  SSYS:${ss['name']}  state  Managed
    \   Check Resource Attribute  SSYS:${ss['name']}  status  OK
    Log    ${feature} Suite Setup: Finish check storage systems state and status.    console=true

    # Check Storage volumes state and status
    Log    ${feature} Suite Setup: Start check storage volumes state and status.    console=true
    ${volumes} =  Fusion Api Get Storage Volumes
    :FOR    ${vol}  IN  @{volumes['members']}
    \   Log    Checking the storage volume ${vol['name']}    console=true
    \   Should match regexp  ${vol['state']}  Managed
    \   Should match regexp  ${vol['status']}  OK
    Log    ${feature} Suite Setup: Finish check storage volumes state and status.    console=true
    Log    ${feature} Suite Setup: Finish setup    console=true
	Fusion Api Logout Appliance


OA CLI EFUSE Blade in Profile
    [Documentation]    Efuse the blade in the profile
    ...                    OA CLI EFUSE BLADE in profile  ${profile}  action=OFF  server_task=Remove
    ...                    OA CLI EFUSE BLADE in profile  ${profile}  action=ON  server_task=Add
    ...                Data file needs to define the following:
    ...                    oa_credentials = {'username': 'Administrator', 'password': 'hpvse1'}
    [Arguments]  ${profile}  ${action}=  ${server_task}=  ${timeout}=300s  ${interval}=50ms
    ${server} =  set variable  ${profile['serverHardwareUri']}
    ${server} =  replace string using regexp  ${server}  SH:  ${EMPTY}
    ${words} =  set variable  ${server.split(',')}
    ${enclosure} =  set variable  ${words[0]}
    ${bay} =  set variable  ${words[1]}
    ${bay} =  set variable  ${bay.strip()}
    ${bay} =  set variable  ${bay[-1]}
    ${enclosure} =   Get Resource  ENC:${enclosure}
    :FOR  ${managerBay}  in  @{enclosure['managerBays']}
    \  ${oa_host} =   set variable if  '${managerBay['role']}'=='Active'  ${managerBay['ipAddress']}
    \  exit for loop if  '${managerBay['role']}'=='Active'
    OA CLI EFUSE  ${oa_host}  ${oa_credentials['username']}  ${oa_credentials['password']}  BLADE  ${bay}  ${action}
    Log to console and log file  EFUSE blade ${bay} ${action} on OA ${oa_host}
    ${task} =  Wait Until Keyword Succeeds  ${timeout}  ${interval}  Get task by param  param=?filter='name'='${server_task}' AND associatedResource.resourceName='${server}' AND taskState='Running'
    log to console and log file  After EFUSE ${action}, the server task URI is ${task['uri']}
    Wait for task2  ${task}  timeout=600  interval=10
    Log to console and log file  After EFUSE ${action}, ${server_task} server finish
    ${task} =  Wait Until Keyword Succeeds  ${timeout}  ${interval}  Get task by param  param=?filter='name'='Update' AND associatedResource.resourceName='${profile['name']}' AND taskState='Running'
    log to console and log file  After EFUSE ${action}, the profile task URI is ${task['uri']}
    Wait for task2  ${task}  timeout=600  interval=10
    Log to console and log file  After EFUSE ${action}, Update profile task finish
    [Return]  PASS