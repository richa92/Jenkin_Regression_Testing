*** Settings ***
Documentation       OVF1071 Server profile templates supports StoreVirtual volumes.
Suite Setup         OVF1071 C7000 Setup
Library				Collections
Library             json
Library  			Dialogs
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

*** Test Cases ***
OVF1071 C7000 TS0 Initialize the Variables and Login
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

OVF1071 C7000 NTS1 Create the Negative SPT and Fail Validation
    Run Negative Tasks for List  ${nts1_negative_spt_tasks}  timeout=120    interval=10

OVF1071 C7000 NTS1 Cleanup
    ${resplist}=  Remove All Server Profile Templates
    Wait for Task2  ${resplist}    timeout=60    interval=10

OVF1071 C7000 NTS2 Create the SPT
    ${resplist}=  Add Server Profile Templates from variable	 ${nts2_spts_create}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF1071 C7000 NTS2 Edit the SPT to Fail Validation
    Run Negative Tasks for List  ${nts2_negative_spt_tasks}  timeout=120    interval=10

OVF1071 C7000 NTS2 Delete the SPT
    ${resplist}=  Remove Server Profile Templates from variable  ${nts2_spts_create}
    Wait for Task2  ${resplist}    timeout=60    interval=10

OVF1071 C7000 PTS1 Create the SPT
    ${resplist}=  Add Server Profile Templates from variable	 ${pts1_spts_create}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF1071 C7000 PTS1 Verify the SPT after Create
    Verify Server Profile Templates  ${pts1_spts_create_expected}

OVF1071 C7000 PTS1 Create the profiles from SPT
    Power Off Servers in Profiles  ${pts1_profiles_create}
    ${resplist}=  Add Server Profiles from variable	 ${pts1_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF1071 C7000 PTS1 Verify the Profiles after Create
    Run Keyword for List  ${pts1_profiles_create_expected}  Verify Server Profile
    Run Keyword for List  ${pts1_profiles_create_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS1 Verify the Profiles Compliance after Create
    Run Keyword for List  ${profiles_compliant_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS1 Edit1 Update LUN Number LUN Type and Storage Paths in Profiles
    Power Off Servers in Profiles  ${pts1_profiles_edit1}
    ${resplist}=  Edit Server Profiles from variable	 ${pts1_profiles_edit1}  param=?force=ignoreServerHealth,ignoreSANWarnings
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF1071 C7000 PTS1 Verify the Profiles after Edit1
    Run Keyword for List  ${pts1_profiles_edit1_expected}  Verify Server Profile
    Run Keyword for List  ${pts1_profiles_edit1_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS1 Verify the Profiles Compliance after Edit1
    Run Keyword for List  ${pts1_profiles_edit1_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS1 Patch1 Update the Profiles From Template
    ${resplist}=  Update Server Profiles from Template  ${pts1_profiles_patch}
    Wait For Task2  ${resplist}   timeout=600    interval=10

OVF1071 C7000 PTS1 Verify the Profiles Compliance after Patch1
    Run Keyword for List  ${profiles_compliant_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS1 Edit2 Remove ATAI Mapping in Profiles
    Power Off Servers in Profiles  ${pts1_profiles_edit2}
    ${resplist}=  Edit Server Profiles from variable	 ${pts1_profiles_edit2}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF1071 C7000 PTS1 Verify the Profiles after Edit2
    Run Keyword for List  ${pts1_profiles_edit2_expected}  Verify Server Profile
    Run Keyword for List  ${pts1_profiles_edit2_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS1 Verify the Profiles Compliance after Edit2
    Run Keyword for List  ${pts1_profiles_edit2_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS1 Edit3 Add ATAI Mapping in Profiles
    Power Off Servers in Profiles  ${pts1_profiles_edit3}
    ${resplist}=  Edit Server Profiles from variable	 ${pts1_profiles_edit3}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF1071 C7000 PTS1 Verify the Profiles after Edit3
    Run Keyword for List  ${pts1_profiles_edit3_expected}  Verify Server Profile
    Run Keyword for List  ${pts1_profiles_edit3_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS1 Verify the Profiles Compliance after Edit3
    Run Keyword for List  ${profiles_compliant_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS1 Edit4 Remove One Volume in Profiles
    Power Off Servers in Profiles  ${pts1_profiles_edit4}
    ${resplist}=  Edit Server Profiles from variable	 ${pts1_profiles_edit4}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF1071 C7000 PTS1 Verify the Profiles after Edit4
    Run Keyword for List  ${pts1_profiles_edit4_expected}  Verify Server Profile
    Run Keyword for List  ${pts1_profiles_edit4_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS1 Verify the Profiles Compliance after Edit4
    Run Keyword for List  ${pts1_profiles_edit4_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS1 Patch2 Update the Profiles From Template
    ${resplist}=  Update Server Profiles from Template  ${pts1_profiles_patch}
    Wait For Task2  ${resplist}   timeout=600    interval=10

OVF1071 C7000 PTS1 Verify the Profiles after Patch2
    Run Keyword for List  ${pts1_profiles_patch2_expected}  Verify Server Profile

OVF1071 C7000 PTS1 Verify the Profiles Compliance after Patch2
    Run Keyword for List  ${profiles_compliant_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS1 Delete the profiles
    Power off Servers in Profiles  ${pts1_profiles_create}
    ${resplist}=  Remove Server Profiles from variable	 ${pts1_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF1071 C7000 PTS1 Remove the Profile Permanent Volumes
    ${resp} =  Fusion Api Get Storage Volumes  param=?filter=Name matches '%spt2-vsa_-perm-priv%'
    ${resplist} =  Run keyword if  ${resp['status_code']}==200 and ${resp['count']}!=0  Remove Storage Volumes Async  ${resp['members']}  param=?suppressDeviceUpdates=false
    Run keyword if  ${resp['status_code']}==200 and ${resp['count']}!=0  Wait for Task2  ${resplist}     timeout=600    interval=5

OVF1071 C7000 PTS1 Remove the SPTs
    ${resplist} =  Remove Server Profile Templates from variable  ${pts1_spts_create}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF1071 C7000 PTS2 Create the SPT
    ${resplist}=  Add Server Profile Templates from variable	 ${pts2_spts_create}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF1071 C7000 PTS2 Verify the SPT after Create
    Verify Server Profile Templates  ${pts2_spts_create_expected}

OVF1071 C7000 PTS2 Create the profiles from SPT
    Power Off Servers in Profiles  ${pts2_profiles_create}
    ${resplist}=  Add Server Profiles from variable	 ${pts2_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF1071 C7000 PTS2 Verify the Profiles after Create
    Run Keyword for List  ${pts2_profiles_create_expected}  Verify Server Profile
    Run Keyword for List  ${pts2_profiles_create_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS2 Verify the Profiles Compliance after Create
    Run Keyword for List  ${profiles_compliant_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS2 Edit1 Update LUN Number LUN Type and Storage Paths in SPT
    ${resplist}=  Edit Server Profile Templates from variable	 ${pts2_spts_edit1}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF1071 C7000 PTS2 Verify the Profiles Compliance after Edit1
    Run Keyword for List  ${pts2_profiles_edit1_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS2 Patch1 Update the Profiles From Template
    ${resplist}=  Update Server Profiles from Template  ${pts2_profiles_patch}
    Wait For Task2  ${resplist}   timeout=600    interval=10

OVF1071 C7000 PTS2 Verify the Profiles after Patch1
    Run Keyword for List  ${pts2_profiles_patch1_expected}  Verify Server Profile
    Run Keyword for List  ${pts2_profiles_patch1_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS2 Verify the Profiles Compliance after Patch1
    Run Keyword for List  ${profiles_compliant_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS2 Edit2 Remove One Volume in SPT
    ${resplist}=  Edit Server Profile Templates from variable	 ${pts2_spts_edit2}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF1071 C7000 PTS2 Verify the Profiles after Edit2
    Run Keyword for List  ${pts2_profiles_edit2_expected}  Verify Server Profile
    Run Keyword for List  ${pts2_profiles_edit2_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS2 Verify the Profiles Compliance after Edit2
    Run Keyword for List  ${profiles_compliant_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS2 Edit3 Add Volume Back in SPT
    ${resplist}=  Edit Server Profile Templates from variable	 ${pts2_spts_edit3}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF1071 C7000 PTS2 Verify the Profiles after Edit3
    Run Keyword for List  ${pts2_profiles_edit3_expected}  Verify Server Profile
    Run Keyword for List  ${pts2_profiles_edit3_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS2 Verify the Profiles Compliance after Edit3
    Run Keyword for List  ${pts2_profiles_edit3_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS2 Edit4 Assoctate ATAI Mapping in Profiles
    Power Off Servers in Profiles  ${pts2_profiles_edit4}
    ${resplist}=  Edit Server Profiles from variable	 ${pts2_profiles_edit4}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF1071 C7000 PTS2 Verify the Profiles after Edit4
    Run Keyword for List  ${pts2_profiles_edit4_expected}  Verify Server Profile
    Run Keyword for List  ${pts2_profiles_edit4_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS2 Verify the Profiles Compliance after Edit4
    Run Keyword for List  ${profiles_compliant_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS2 Delete the profiles
    Power off Servers in Profiles  ${pts2_profiles_create}
    ${resplist}=  Remove Server Profiles from variable	 ${pts2_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF1071 C7000 PTS2 Remove the Profile Permanent Volumes
    ${resplist}=  Remove Storage Volumes Async   ${pts2_new_permanent_volumes}  param=?suppressDeviceUpdates=false
    Wait for Task2  ${resplist}     timeout=600    interval=5

OVF1071 C7000 PTS2 Remove the SPTs
    ${resplist} =  Remove Server Profile Templates from variable  ${pts2_spts_create}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF1071 C7000 PTS3 Create the SPT
    ${resplist}=  Add Server Profile Templates from variable	 ${pts3_spts_create}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF1071 C7000 PTS3 Verify the SPT after Create
    Verify Server Profile Templates  ${pts3_spts_create_expected}

OVF1071 C7000 PTS3 Create the profiles
    Power Off Servers in Profiles  ${pts3_profiles_create}
    ${resplist}=  Add Server Profiles from variable	 ${pts3_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF1071 C7000 PTS3 Verify the Profiles after Create
    Run Keyword for List  ${pts3_profiles_create_expected}  Verify Server Profile
    Run Keyword for List  ${pts3_profiles_create_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS3 Power on the Servers
    Power On Servers in Profiles  ${pts3_profiles_create}

OVF1071 C7000 PTS3 Edit1 the Profiles to associate with SPT
    ${resplist}=  Edit Server Profiles from variable	 ${pts3_profiles_edit1}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF1071 C7000 PTS3 Verify the Profiles after Edit1
    Run Keyword for List  ${pts3_profiles_edit1_expected}  Verify Server Profile
    Run Keyword for List  ${pts3_profiles_edit1_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS3 Verify the Profiles Compliance after Edit1
    Run Keyword for List  ${pts3_profiles_edit1_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS3 Edit2 the Profiles to Map ATAI
    ${resplist}=  Edit Server Profiles from variable	 ${pts3_profiles_edit2}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF1071 C7000 PTS3 Verify the Profiles after Edit2
    Run Keyword for List  ${pts3_profiles_edit2_expected}  Verify Server Profile
    Run Keyword for List  ${pts3_profiles_edit2_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS3 Verify the Profiles Compliance after Edit2
    Run Keyword for List  ${profiles_compliant_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS3 Delete the profiles
    Power off Servers in Profiles  ${pts3_profiles_create}
    ${resplist}=  Remove Server Profiles from variable	 ${pts3_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF1071 C7000 PTS3 Remove the Profile Permanent Volumes
    ${resplist}=  Remove Storage Volumes Async   ${pts3_new_permanent_volumes}  param=?suppressDeviceUpdates=false
    Wait for Task2  ${resplist}     timeout=600    interval=5

OVF1071 C7000 PTS3 Remove the SPTs
    ${resplist} =  Remove Server Profile Templates from variable  ${pts3_spts_create}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF1071 C7000 PTS4 Create the SPT
    ${resplist}=  Add Server Profile Templates from variable	 ${pts4_spts_create}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF1071 C7000 PTS4 Verify the SPT after Create
    Verify Server Profile Templates  ${pts4_spts_create_expected}

OVF1071 C7000 PTS4 Create the profiles
    Power Off Servers in Profiles  ${pts4_profiles_create}
    ${resplist}=  Add Server Profiles from variable	 ${pts4_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF1071 C7000 PTS4 Verify the Profiles after Create
    Run Keyword for List  ${pts4_profiles_create_expected}  Verify Server Profile
    Run Keyword for List  ${pts4_profiles_create_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS4 Power on the Servers
    Power On Servers in Profiles  ${pts4_profiles_create}

OVF1071 C7000 PTS4 Edit1 the Profiles to associate with SPT
    ${resplist}=  Edit Server Profiles from variable	 ${pts4_profiles_edit1}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF1071 C7000 PTS4 Verify the Profiles after Edit1
    Run Keyword for List  ${pts4_profiles_edit1_expected}  Verify Server Profile
    Run Keyword for List  ${pts4_profiles_edit1_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS4 Verify the Profiles Compliance after Edit1
    Run Keyword for List  ${pts4_profiles_edit1_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS4 Edit the Storage Volumes
    ${resplist}=  Edit Storage Volumes Async	 ${pts4_volumes_edit}
    Wait For Task2  ${resplist}   timeout=300    interval=10

OVF1071 C7000 PTS4 Edit the Volume Permanence in SPT
    ${resplist}=  Edit Server Profile Templates from variable	 ${pts4_spts_edit}
    Wait For Task2  ${resplist}   timeout=300    interval=10

OVF1071 C7000 PTS4 Verify the Profiles Compliance
    Run Keyword for List  ${three_profiles_compliant_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS4 Delete the profiles
    Power off Servers in Profiles  ${pts4_profiles_create}
    ${resplist}=  Remove Server Profiles from variable	 ${pts4_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF1071 C7000 PTS4 Remove the Profile Permanent Volumes
    ${resplist}=  Remove Storage Volumes Async   ${pts4_new_permanent_volumes}  param=?suppressDeviceUpdates=false
    Wait for Task2  ${resplist}     timeout=600    interval=5

OVF1071 C7000 PTS4 Remove the SPTs
    ${resplist} =  Remove Server Profile Templates from variable  ${pts4_spts_create}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF1071 C7000 PTS5 Create the SPT
    ${resplist}=  Add Server Profile Templates from variable	 ${pts5_spts_create}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF1071 C7000 PTS5 Verify the SPT after Create
    Verify Server Profile Templates  ${pts5_spts_create_expected}

OVF1071 C7000 PTS5 Create the profiles
    Power Off Servers in Profiles  ${pts5_profiles_create}
    ${resplist}=  Add Server Profiles from variable	 ${pts5_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF1071 C7000 PTS5 Verify the Profiles after Create
    Run Keyword for List  ${pts5_profiles_create_expected}  Verify Server Profile
    Run Keyword for List  ${pts5_profiles_create_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS5 Power on the Servers
    Power On Servers in Profiles  ${pts5_profiles_create}

OVF1071 C7000 PTS5 Edit1 the Profiles to associate with SPT
    ${resplist}=  Edit Server Profiles from variable	 ${pts5_profiles_edit1}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF1071 C7000 PTS5 Verify the Profiles after Edit1
    Run Keyword for List  ${pts5_profiles_edit1_expected}  Verify Server Profile
    Run Keyword for List  ${pts5_profiles_edit1_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS5 Verify the Profiles Compliance after Edit1
    Run Keyword for List  ${pts5_profiles_edit1_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS5 Edit2 the Profiles to Map ATAI
    ${resplist}=  Edit Server Profiles from variable	 ${pts5_profiles_edit2}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF1071 C7000 PTS5 Verify the Profiles after Edit2
    Run Keyword for List  ${pts5_profiles_edit2_expected}  Verify Server Profile
    Run Keyword for List  ${pts5_profiles_edit2_expected}  Verify Server Profile Volume Attachments

OVF1071 C7000 PTS5 Verify the Profiles Compliance after Edit2
    Run Keyword for List  ${three_profiles_compliant_compliance}  Verify Server Profile Compliance

OVF1071 C7000 PTS5 Delete the profiles
    Power off Servers in Profiles  ${pts5_profiles_create}
    ${resplist}=  Remove Server Profiles from variable	 ${pts5_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF1071 C7000 PTS5 Remove the SPTs
    ${resplist} =  Remove Server Profile Templates from variable  ${pts5_spts_create}
    wait for task2  ${resplist}  timeout=900  interval=10

*** Keywords ***
OVF1071 C7000 Setup
    [Documentation]    OVF1071 C7000 Setup
    Set Log Level	TRACE
    ${feature} =  set variable  OVF1071
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
    :FOR    ${profile}  IN  @{pts1_profiles_create}
    \   ${status}  ${return} =  Run Keyword and Ignore Error  Get From Dictionary  ${profile}  serverHardwareUri
	\   ${server} =  set variable if  '${status}'=='PASS'  ${return}  ${None}
	\   CONTINUE FOR LOOP IF    '${server}'=='None'
	\   ${start_state} =  Get Resource Attribute  ${server}  state
	\   Log    ${feature} Suite Setup: The server ${server} start state is ${start_state}    console=true
	\   Run keyword if  '${start_state}'!= 'NoProfileApplied'  Reset Server Hardware iLO via cpqlocfg and Wait for Refresh to Finish  ${server}
	\   Run keyword if  '${start_state}'!= 'NoProfileApplied'  Check Resource Attribute	 SH:${server}  state  NoProfileApplied
    Log    ${feature} Suite Setup: Finish check servers state.    console=true

	# Check servers state, reset iLO and refresh if initial state is not NoProfileApplied
	Log    ${feature} Suite Setup: Start check servers state.    console=true
    :FOR    ${profile}  IN  @{pts1_profiles_create}
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

    # Force remove any profiles from previous tests
    Log    ${feature} Suite Setup: Start force remove all profiles    console=true
    Power Off all Servers  control=PressAndHold
    ${resplist} =  Remove All Server Profiles Async  force=${True}
    Wait for Task2  ${resplist}  timeout=3600  interval=10
    Log    ${feature} Suite Setup: Finish force remove all profiles    console=true

    Log    ${feature} Suite Setup: Finish check preconditions    console=true
	Fusion Api Logout Appliance