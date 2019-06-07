*** Settings ***
Documentation       OVF2972 iLO configure local accounts
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Library             OperatingSystem
Library             String
Library             XML
Suite Setup         OVF2972 Synergy Setup
Resource            ../global_variables.robot
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

${DATA_FILE}         Regression_Data.py

*** Test Cases ***
OVF2972 Synergy TS0 Initialize the Variables and Login
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

OVF2972 Synergy NTS1 Create the Negative SPT and Fail Validation
    Run Negative Tasks for List  ${nts1_negative_spt_tasks}  timeout=120    interval=10

OVF2972 Synergy NTS1 Cleanup
    ${resplist}=  Remove All Server Profile Templates
    Wait for Task2  ${resplist}    timeout=60    interval=10

OVF2972 Synergy NTS2 Create the SPT
    ${resplist}=  Add Server Profile Templates from variable	 ${nts2_spts_create}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF2972 Synergy NTS2 Edit the SPT to Fail Validation
    Run Negative Tasks for List  ${nts2_negative_spt_tasks}  timeout=120    interval=10

OVF2972 Synergy NTS2 Delete the SPT
    ${resplist}=  Remove Server Profile Templates from variable  ${nts2_spts_create}
    Wait for Task2  ${resplist}    timeout=60    interval=10

OVF2972 Synergy NTS3 Create the Profiles to Fail Validation
    Power Off Server  ${SERVER1}  powerControl=PressAndHold
    Power Off Server  ${SERVER2}  powerControl=PressAndHold
    Power Off Server  ${SERVER_UNSUPPORTED}  powerControl=PressAndHold
    Run Negative Tasks for List  ${nts3_negative_profile_tasks}  timeout=120    interval=10

OVF2972 Synergy NTS3 Cleanup
    ${resplist} =  Remove All Server Profiles Async  force=${True}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF2972 Synergy NTS4 Create the Profile
    Power Off Server  ${SERVER1}  powerControl=PressAndHold
    Power Off Server  ${SERVER2}  powerControl=PressAndHold
    Power Off Server  ${SERVER_UNSUPPORTED}  powerControl=PressAndHold
    ${resp}=  Add Server Profile  ${nts4_profile_create}
    Wait for Task2  ${resp}     timeout=600    interval=10

OVF2972 Synergy NTS4 Edit the Profile to Fail Validation
    Run Negative Tasks for List  ${nts4_negative_profile_tasks}  timeout=120    interval=10

OVF2972 Synergy NTS4 Delete the Profiles
    ${resp}=  Remove Server Profile  ${nts4_profile_create}
    Wait for Task2  ${resp}    timeout=60    interval=10

OVF2972 Synergy PTS1 Create the profiles
    Power off Servers in Profiles  ${pts1_profiles_create}  powerControl=PressAndHold
    verify servers powerstate in profiles  ${pts1_profiles_create}  Off
    ${resplist}=  Add Server Profiles from variable	 ${pts1_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF2972 Synergy PTS1 Verify local Accounts via RIS after create
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts1_profile1_create}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts1_profile2_create}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS1 Run RIBCL script after create
    Run cpqlocfg and Verify Server POST State  ${server1_ilo}  PWR_STATE_OFF  ilo_username=${pts1_create_user}  ilo_password=${pts1_create_user_password}
    Run cpqlocfg and Verify Server POST State  ${server2_ilo}  PWR_STATE_OFF  ilo_username=${pts1_create_user}  ilo_password=${pts1_create_user_password}

OVF2972 Synergy PTS1 Power on servers
    Power On Servers in Profiles  ${pts1_profiles_create}
    Wait Until Keyword Succeeds  15m  5s  Run cpqlocfg and Verify Server POST State  ${server1_ilo}  IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  ilo_username=${pts1_edit_user}  ilo_password=${pts1_edit_user_password}
    Wait Until Keyword Succeeds  15m  5s  Run cpqlocfg and Verify Server POST State  ${server2_ilo}  IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  ilo_username=${pts1_edit_user}  ilo_password=${pts1_edit_user_password}

OVF2972 Synergy PTS1 Edit the profiles
    verify servers powerstate in profiles  ${pts1_profiles_create}  On
    ${resplist}=  Edit Server Profiles from variable	 ${pts1_profiles_edit}
    Wait For Task2  ${resplist}  timeout=900    interval=10

OVF2972 Synergy PTS1 Verify local Accounts via RIS after edit
    server profile mpsettings local accounts should match ris  ${pts1_profile1_edit}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    server profile mpsettings local accounts should match ris  ${pts1_profile2_edit}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS1 Run RIBCL script after edit
    Run cpqlocfg and Verify Server POST State  ${server1_ilo}  IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  ilo_username=${pts1_edit_user}  ilo_password=${pts1_edit_user_password}
    Run cpqlocfg and Verify Server POST State  ${server2_ilo}  IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  ilo_username=${pts1_edit_user}  ilo_password=${pts1_edit_user_password}

OVF2972 Synergy PTS1 Delete the profiles
    Power off Servers in Profiles  ${pts1_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts1_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF2972 Synergy PTS1 Verify local Accounts via RIS after delete
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts1_profile1_edit}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts1_profile2_edit}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS2 Create the SPT
    ${resplist}=  Add Server Profile Templates from variable	 ${pts2_spts_create}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF2972 Synergy PTS2 Verify the SPT after Create
    Verify Server Profile Templates  ${pts2_spts_create}

OVF2972 Synergy PTS2 Create the profiles from SPT
    Power Off Servers in Profiles  ${pts2_profiles_create}
    ${resplist}=  Add Server Profiles from variable	 ${pts2_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF2972 Synergy PTS2 Verify the Profiles after Create
    Run Keyword for List  ${pts2_profiles_create_expected}  Verify Server Profile

OVF2972 Synergy PTS2 Verify the Profiles Compliance after Create
    Run Keyword for List  ${pts2_profiles_compliance}  Verify Server Profile Compliance

OVF2972 Synergy PTS2 Verify local Accounts via RIS after create
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts2_profile1_create_expected}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts2_profile2_create_expected}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS2 Edit the Profiles
    ${resplist}=  Edit Server Profiles from variable	 ${pts2_profiles_edit}  param=?force=ignoreServerHealth,ignoreSANWarnings
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF2972 Synergy PTS2 Verify the Profiles after Edit
    Run Keyword for List  ${pts2_profiles_edit}  Verify Server Profile

OVF2972 Synergy PTS2 Verify the Profiles Non-compliance after Edit
    Run Keyword for List  ${pts2_profiles_non_compliance}  Verify Server Profile Compliance

OVF2972 Synergy PTS2 Verify local Accounts via RIS after edit
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts2_profile1_edit}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts2_profile2_edit}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS2 Update the Profiles From Template
    ${resplist}=  Update Server Profiles from Template  ${pts2_profiles_create}
    Wait For Task2  ${resplist}   timeout=600    interval=10

OVF2971 C7000 PTS2 Verify the Profiles after Patch
    Run Keyword for List  ${pts2_profiles_create_expected}  Verify Server Profile

OVF2972 Synergy PTS2 Verify the Profiles Compliance after Patch
    Run Keyword for List  ${pts2_profiles_compliance}  Verify Server Profile Compliance

OVF2972 Synergy PTS2 Verify local Accounts via RIS after patch
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts2_profile1_create_expected}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts2_profile2_create_expected}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS2 Delete the profiles
    Power off Servers in Profiles  ${pts3_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts2_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF2972 Synergy PTS2 Verify local Accounts via RIS after delete
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts2_profile1_create_expected}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts2_profile2_create_expected}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS2 Remove the SPTs
    ${resplist} =  Remove Server Profile Templates from variable  ${pts2_spts_create}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF2972 Synergy PTS3 Create the SPT
    ${resplist}=  Add Server Profile Templates from variable	 ${pts3_spts_create}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF2972 Synergy PTS3 Verify the SPT after Create
    Verify Server Profile Templates  ${pts3_spts_create}

OVF2972 Synergy PTS3 Create the profiles
    Power Off Servers in Profiles  ${pts3_profiles_create}
    ${resplist}=  Add Server Profiles from variable	 ${pts3_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF2972 Synergy PTS3 Verify the Profiles after Create
    Run Keyword for List  ${pts3_profiles_create_expected}  Verify Server Profile

OVF2972 Synergy PTS3 Verify the Profiles Compliance after Create
    Run Keyword for List  ${pts3_profiles_compliance}  Verify Server Profile Compliance
    
OVF2972 Synergy PTS3 Verify local Accounts via RIS after create
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts3_profile1_create_expected}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts3_profile2_create_expected}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS3 Edit the SPT
    ${resplist}=  Edit Server Profile Templates from variable	 ${pts3_spts_edit}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF2972 Synergy PTS3 Verify the SPT after Edit
    Verify Server Profile Templates  ${pts3_spts_edit}

OVF2972 Synergy PTS3 Verify the Profiles Noncompliance after Edit
    Run Keyword for List  ${pts3_profiles_non_compliance}  Verify Server Profile Compliance

OVF2972 Synergy PTS3 Update the Profiles From Template
    ${resplist}=  Update Server Profiles from Template  ${pts3_profiles_create}
    Wait For Task2  ${resplist}   timeout=600    interval=10

OVF2971 C7000 PTS3 Verify the Profiles after Patch
    Run Keyword for List  ${pts3_profiles_patch_expected}  Verify Server Profile

OVF2972 Synergy PTS3 Verify the Profiles Compliance after Patch
    Run Keyword for List  ${pts3_profiles_compliance}  Verify Server Profile Compliance

OVF2972 Synergy PTS3 Verify local Accounts via RIS after patch
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts3_profile1_patch_expected}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts3_profile2_patch_expected}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS3 Delete the profiles
    Power off Servers in Profiles  ${pts3_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts3_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF2972 Synergy PTS3 Verify local Accounts via RIS after delete
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts3_profile1_patch_expected}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts3_profile2_patch_expected}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS3 Remove the SPTs
    ${resplist} =  Remove Server Profile Templates from variable  ${pts3_spts_create}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF2972 Synergy PTS4 Create the profiles
    Power Off Servers in Profiles  ${pts4_profiles_create}
    ${resplist}=  Add Server Profiles from variable	 ${pts4_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF2972 Synergy PTS4 Verify the Profiles after Create
    Run Keyword for List  ${pts4_profiles_create}  Verify Server Profile

OVF2972 Synergy PTS4 Verify local Accounts via RIS after create
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts4_profile1_create}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts4_profile2_create}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS4 Create SPT from SP
    ${resp} =  Create Server Profile Template from Profile  ${pts4_profile1_create}  ${pts4_spt1_create_expected['name']}
    wait for task2  ${resp}  timeout=600  interval=10
    ${resp} =  Create Server Profile Template from Profile  ${pts4_profile2_create}  ${pts4_spt2_create_expected['name']}
    wait for task2  ${resp}  timeout=600  interval=10

OVF2972 Synergy PTS4 Verify the SPT after Create
    Verify Server Profile Templates  ${pts4_spts_create_expected}

OVF2972 Synergy PTS4 Delete the profiles
    Power off Servers in Profiles  ${pts4_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts4_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF2972 Synergy PTS4 Verify local Accounts via RIS after delete
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts4_profile1_create}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts4_profile2_create}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS4 Remove the SPTs
    ${resplist} =  Remove Server Profile Templates from variable  ${pts4_spts_create_expected}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF2972 Synergy PTS5 Create the profiles
    Power off Servers in Profiles  ${pts5_profiles_create}  powerControl=PressAndHold
    verify servers powerstate in profiles  ${pts5_profiles_create}  Off
    ${resplist}=  Add Server Profiles from variable	 ${pts5_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF2972 Synergy PTS5 Verify local Accounts via RIS after create
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts5_profile1_create}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts5_profile2_create}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS5 Edit the profiles
    ${resplist}=  Edit Server Profiles from variable	 ${pts5_profiles_edit}
    Wait For Task2  ${resplist}  timeout=900    interval=10

OVF2972 Synergy PTS5 Verify local Accounts via RIS after edit
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts5_profile1_edit}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts5_profile2_edit}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS5 Delete the profiles
    Power off Servers in Profiles  ${pts5_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts5_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF2972 Synergy PTS5 Verify local Accounts via RIS after delete
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts5_profile1_create}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts5_profile2_create}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS6 Create the profile
    Power off Servers in Profiles  ${pts6_profiles_create}  powerControl=PressAndHold
    verify servers powerstate in profiles  ${pts6_profiles_create}  Off
    ${resplist}=  Add Server Profiles from variable	 ${pts6_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF2972 Synergy PTS6 Verify local Accounts via RIS after create
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts6_profile1_create}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts6_profile2_create}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS6 Unassign the profile
    ${resplist}=  Edit Server Profiles from variable	 ${pts6_profiles_unassign}
    Wait For Task2  ${resplist}  timeout=900    interval=10

OVF2972 Synergy PTS6 Verify local Accounts via RIS after unassign
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts6_profile1_create}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts6_profile2_create}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS6 Reassign the profiles
    ${resplist}=  Edit Server Profiles from variable	 ${pts6_profiles_reassign}
    Wait For Task2  ${resplist}  timeout=900    interval=10

OVF2972 Synergy PTS6 Verify local Accounts via RIS after reassign
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts6_profile1_reassign}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts6_profile2_reassign}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS6 Delete the profiles
    Power off Servers in Profiles  ${pts6_profiles_reassign}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts6_profiles_reassign}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF2972 Synergy PTS6 Verify local Accounts via RIS after delete
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts6_profile1_reassign}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts6_profile2_reassign}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS7 Create the profile
    Power off Servers in Profiles  ${pts7_profiles_create}  powerControl=PressAndHold
    verify servers powerstate in profiles  ${pts7_profiles_create}  Off
    ${resplist}=  Add Server Profiles from variable	 ${pts7_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF2972 Synergy PTS7 Verify local Accounts via RIS after create
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts7_profile_create_expected}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}

OVF2972 Synergy PTS7 Transform profile from Gen9 to Gen10
    ${transformation_uri} =  Get Server Profile Transformation URI  ${pts7_profile_gen9_to_gen10_expected}
    ${transformation_dto} =  Get Server Profile Transformation  ${transformation_uri}
    ${verify} =  Fusion api validate response follow  ${pts7_profile_gen9_to_gen10_expected['managementProcessor']}  ${transformation_dto['managementProcessor']}  wordy=True
    Should be equal  ${verify}  ${True}  msg=Transform Gen9 to Gen10

OVF2972 Synergy PTS7 Move the profile
    ${resplist}=  Edit Server Profiles from variable	 ${pts7_profiles_move}
    Wait For Task2  ${resplist}  timeout=900    interval=10

OVF2972 Synergy PTS7 Verify local Accounts via RIS after move
    server profile mpsettings local accounts should match ris  ${pts7_profile_create_expected}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    server profile mpsettings local accounts should match ris  ${pts7_profile_move_expected}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS7 Transform profile from Gen10 to Gen9
    ${transformation_uri} =  Get Server Profile Transformation URI  ${pts7_profile_gen10_to_gen9_expected}
    ${transformation_dto} =  Get Server Profile Transformation  ${transformation_uri}
    ${verify} =  Fusion api validate response follow  ${pts7_profile_gen10_to_gen9_expected['managementProcessor']}  ${transformation_dto['managementProcessor']}  wordy=True
    Should be equal  ${verify}  ${True}  msg=Transform Gen10 to Gen9

OVF2972 Synergy PTS7 Move the profile back
    ${resplist}=  Edit Server Profiles from variable	 ${pts7_profiles_move_back}
    Wait For Task2  ${resplist}  timeout=900    interval=10

OVF2972 Synergy PTS7 Verify local Accounts via RIS after move back
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts7_profile_move_back}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts7_profile_move_expected}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS7 Delete the profiles
    Power off Servers in Profiles  ${pts7_profiles_move_back}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts7_profiles_move_back}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF2972 Synergy PTS7 Verify local Accounts via RIS after delete
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts7_profile_move_back}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts7_profile_move_expected}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS8 Create the SPT
    ${resplist}=  Add Server Profile Templates from variable	 ${pts8_spts_create}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF2972 Synergy PTS8 Verify the SPT after Create
    Verify Server Profile Templates  ${pts8_spts_create}

OVF2972 Synergy PTS8 Create the profile
    Power off Servers in Profiles  ${pts8_profiles_create}  powerControl=PressAndHold
    verify servers powerstate in profiles  ${pts8_profiles_create}  Off
    ${resplist}=  Add Server Profiles from variable	 ${pts8_profiles_create}
    Wait For Task2  ${resplist}   timeout=900    interval=10

OVF2972 Synergy PTS8 Verify local Accounts via RIS after create
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts8_profile1_create_expected}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts8_profile2_create_expected}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS8 B/R Create Backup
    Create Backup
    ${uri} =    Get Backup URI
    Set Suite Variable    ${BACKUPURI}    ${uri}

OVF2972 Synergy PTS8 B/R Delete the Profiles
    Power off Servers in Profiles  ${pts8_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts8_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF2972 Synergy PTS8 B/R Remove the SPTs
    ${resplist} =  Remove Server Profile Templates from variable  ${pts8_spts_create}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF2972 Synergy PTS8 B/R Restore
    ${resp}=    Initiate Restore    ${BACKUPURI}

OVF2972 Synergy PTS8 B/R Wait for Restore to Complete
    Wait Until Keyword Succeeds    90m    30s    OneView Restore Complete

OVF2972 Synergy PTS8 B/R Verify the SPTs after Restore
    Fusion Api Login Appliance 		${APPLIANCE_IP}  ${admin_credentials}
    Verify Server Profile Templates  ${pts8_spts_create}

OVF2972 Synergy PTS8 B/R Verify the Profiles Status Critical after Restore
    Run Keyword for List with kwargs  ${pts8_profiles_create}  Verify Server Profile  status=Critical

OVF2972 Synergy PTS8 B/R Check Profiles Alerts
    ${profile1_uri} =  Get Server Profile URI  ${pts8_profile1_create['name']}
    ${profile1_alert} =  wait until keyword succeeds  1m  10s  Get Alert By Param   param=?filter=description like 'Server profile settings conflict with the server hardware configuration.' and alertState EQ 'Locked' and resourceUri EQ '${profile1_uri}'
    ${profile2_uri} =  Get Server Profile URI  ${pts8_profile2_create['name']}
    ${profile2_alert} =  wait until keyword succeeds  1m  10s  Get Alert By Param   param=?filter=description like 'Server profile settings conflict with the server hardware configuration.' and alertState EQ 'Locked' and resourceUri EQ '${profile2_uri}'

OVF2972 Synergy PTS8 B/R Unassign the Profiles
    Power Off Servers in Profiles  ${pts8_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Edit Server Profiles from variable	 ${pts8_profiles_unassign}
    Wait For Task2  ${resplist}   timeout=1800    interval=10

OVF2972 Synergy PTS8 B/R Reassign the Profiles
    Power Off Servers in Profiles  ${pts8_profiles_reassign}  powerControl=PressAndHold
    ${resplist}=  Edit Server Profiles from variable	 ${pts8_profiles_reassign}
    Wait For Task2  ${resplist}   timeout=1800    interval=10

OVF2972 Synergy PTS8 Verify local Accounts via RIS after reassign
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts8_profile1_create_expected}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts8_profile2_create_expected}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS8 Delete the profiles after restore
    Power off Servers in Profiles  ${pts8_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts8_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF2972 Synergy PTS8 Verify local Accounts via RIS after delete
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts8_profile1_create_expected}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${pts8_profile2_create_expected}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}

OVF2972 Synergy PTS8 B/R Delete the SPTs after restore
    ${resplist} =  Remove Server Profile Templates from variable  ${pts8_spts_create}
    wait for task2  ${resplist}  timeout=900  interval=10

*** Keywords ***
OVF2972 Synergy Setup
    [Documentation]  OVF2972 Synergy Setup
    ${feature} =  set variable  OVF2972 Synergy
    log  ${feature} Suite Setup: Start suite setup  console=True
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

    # server1
    ${server1_ilo} =  Get Server Hardware iLO IP  ${server1}
    ${server1_ilo_admin_user} =  set variable  Administrator
    ${server1_ilo_admin_password} =  set variable  hpvse1-ilo
    # server2
    ${server2_ilo} =  Get Server Hardware iLO IP  ${server2}
    ${server2_ilo_admin_user} =  set variable  Administrator
    ${server2_ilo_admin_password} =  set variable  hpvse123
    set suite variable  ${server1_ilo}
    set suite variable  ${server1_ilo_admin_user}
    set suite variable  ${server1_ilo_admin_password}
    set suite variable  ${server2_ilo}
    set suite variable  ${server2_ilo_admin_user}
    set suite variable  ${server2_ilo_admin_password}

    # Clean up the user accounts on the iLO
    ${rtn} =  Delete Ris Local User Accounts  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Should be equal  ${rtn}  ${True}  msg=Delete RIS local user account on iLO ${server1_ilo}
    ${rtn} =  Delete Ris Local User Accounts  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}
    Should be equal  ${rtn}  ${True}  msg=Delete RIS local user account on iLO ${server2_ilo}

    # Verify the user accounts after cleanup
    Server Profile Mpsettings Local Accounts Should Match RIS  ${suite_setup_profile1}  ${server1_ilo}  ${server1_ilo_admin_user}  ${server1_ilo_admin_password}
    Server Profile Mpsettings Local Accounts Should Match RIS  ${suite_setup_profile2}  ${server2_ilo}  ${server2_ilo_admin_user}  ${server2_ilo_admin_password}
