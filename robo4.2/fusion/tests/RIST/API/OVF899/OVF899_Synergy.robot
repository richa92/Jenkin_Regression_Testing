*** Settings ***
Documentation       OVF899 configure local storage DWC and LDA
Library				FusionLibrary
Suite Setup         OVF899 Synergy Setup
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Library             OperatingSystem
Library             String
Library             XML
Resource            ../global_variables.robot
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

${DATA_FILE}         Regression_Data.py

*** Test Cases ***
OVF899 Synergy TS0 Initialize the Variables and Login
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

OVF899 Synergy NTS1 Create the Negative SPT and Fail Validation
    Power Off Servers in Profiles  ${nts1_profiles}  powerControl=PressAndHold
    Run Negative Tasks for List  ${nts1_negative_profile_tasks}  timeout=120    interval=10

OVF899 Synergy NTS1 Cleanup
    ${resplist} =  Remove All Server Profiles Async  force=${True}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF899 Synergy PTS1 Create the SPTs
    ${resplist}=  Add Server Profile Templates from variable	 ${pts1_spts_create}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF899 Synergy PTS1 Verify the SPTs after Create
    Verify Server Profile Templates  ${pts1_spts_create}

OVF899 Synergy PTS1 Create the Profiles from SPTs
    Power Off Servers in Profiles  ${pts1_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Add Server Profiles from variable	 ${pts1_profiles_create}
    Wait For Task2  ${resplist}   timeout=1800    interval=10

OVF899 Synergy PTS1 Verify the Profiles after Create
    Run Keyword for List with kwargs  ${pts1_profiles_create_expected}  Verify Server Profile  status=OK

OVF899 Synergy PTS1 Check Profile Local Storage Alerts after Create
    ${profile1_uri} =  Get Server Profile URI  ${pts1_profile1_create['name']}
    ${profile1_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile1_uri}'"&sort=created:descending&count=1
    ${profile2_uri} =  Get Server Profile URI  ${pts1_profile2_create['name']}
    ${profile2_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile2_uri}'"&sort=created:descending&count=1
    ${profile3_uri} =  Get Server Profile URI  ${pts1_profile3_create['name']}
    ${profile3_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile3_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS1 Verify Profile Compliance after Create
    Run Keyword for List  ${pts1_profiles_compliance}  Verify Server Profile Compliance

OVF899 Synergy PTS1 Verify Redfish Smartstorageconfig after Create
    Verify RIS nodes for list  ${pts1_ris_nodes_after_create}

OVF899 Synergy PTS1 Edit the SPTs
    ${resplist}=  Edit Server Profile Templates from variable	 ${pts1_spts_edit}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF899 Synergy PTS1 Verify the SPTs after Edit
    Verify Server Profile Templates  ${pts1_spts_edit}

OVF899 Synergy PTS1 Verify Profile Non-compliance after Edit SPTs
    Run Keyword for List  ${pts1_profiles_non_compliance}  Verify Server Profile Compliance

OVF899 Synergy PTS1 Edit the Profiles
    Power Off Servers in Profiles  ${pts1_profiles_edit}  powerControl=PressAndHold
    ${resplist}=  Edit Server Profiles from variable	 ${pts1_profiles_edit}
    Wait For Task2  ${resplist}   timeout=1800    interval=10

OVF899 Synergy PTS1 Verify the Profiles after Edit
    Run Keyword for List with kwargs  ${pts1_profiles_edit}  Verify Server Profile  status=OK

OVF899 Synergy PTS1 Check Profile Local Storage Alerts after Edit
    ${profile1_uri} =  Get Server Profile URI  ${pts1_profile1_create['name']}
    ${profile1_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile1_uri}'"&sort=created:descending&count=1
    ${profile2_uri} =  Get Server Profile URI  ${pts1_profile2_create['name']}
    ${profile2_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile2_uri}'"&sort=created:descending&count=1
    ${profile3_uri} =  Get Server Profile URI  ${pts1_profile3_create['name']}
    ${profile3_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile3_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS1 Verify Profile Compliance after Edit
    Run Keyword for List  ${pts1_profiles_compliance}  Verify Server Profile Compliance

OVF899 Synergy PTS1 Verify Redfish Smartstorageconfig after Edit
    Verify RIS nodes for list  ${pts1_ris_nodes_after_edit}

OVF899 Synergy PTS1 Delete the Profiles
    Power off Servers in Profiles  ${pts1_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts1_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF899 Synergy PTS1 Remove the SPTs
    ${resplist} =  Remove Server Profile Templates from variable  ${pts1_spts_create}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF899 Synergy PTS2 Create the profile
    Power off Servers in Profiles  ${pts2_profiles_create}  powerControl=PressAndHold
    ${resp}=  Add Server Profiles from variable  ${pts2_profiles_create}
    Wait For Task2  ${resp}   timeout=1800    interval=10

OVF899 Synergy PTS2 Verify the Profiles after Create
    Run Keyword for List with kwargs  ${pts2_profiles_create_expected}  Verify Server Profile  status=OK

OVF899 Synergy PTS2 Check Profile Local Storage Alerts after Create
    ${profile1_uri} =  Get Server Profile URI  ${pts2_profile1_create['name']}
    ${profile1_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile1_uri}'"&sort=created:descending&count=1
    ${profile2_uri} =  Get Server Profile URI  ${pts2_profile2_create['name']}
    ${profile2_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile2_uri}'"&sort=created:descending&count=1
    ${profile3_uri} =  Get Server Profile URI  ${pts2_profile3_create['name']}
    ${profile3_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile3_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS2 Verify Redfish Smartstorageconfig after Create
    Verify RIS nodes for list  ${pts2_ris_nodes_after_create}

OVF899 Synergy PTS2 Create SPT from SP
    ${resp} =  Create Server Profile Template from Profile  ${pts2_profile1_create}  ${PTS2_SPT1_NAME}
    wait for task2  ${resp}  timeout=120  interval=10
    ${resp} =  Create Server Profile Template from Profile  ${pts2_profile2_create}  ${PTS2_SPT2_NAME}
    wait for task2  ${resp}  timeout=120  interval=10
    ${resp} =  Create Server Profile Template from Profile  ${pts2_profile3_create}  ${PTS2_SPT3_NAME}
    wait for task2  ${resp}  timeout=120  interval=10

OVF899 Synergy PTS2 Verify SPT
    Verify Server Profile Templates  ${pts2_spts_create_expected}

OVF899 Synergy PTS2 Create the unassigned profiles from SPTs
    ${resplist}=  Add Server Profiles from variable	 ${pts2_unassign_profiles_create}
    Wait For Task2  ${resplist}   timeout=600    interval=10

OVF899 Synergy PTS2 Verify the Unassigned Profiles after Create
    Run Keyword for List  ${pts2_unassign_profiles_create_expected}  Verify Server Profile

OVF899 Synergy PTS2 Verify Unassigned Profile Compliance after Create
    Run Keyword for List  ${pts2_unassign_profiles_compliance}  Verify Server Profile Compliance

OVF899 Synergy PTS2 Delete the Profiles
    Power off Servers in Profiles  ${pts2_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts2_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10
    ${resplist}=  Remove Server Profiles from variable	 ${pts2_unassign_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF899 Synergy PTS2 Remove the SPTs
    ${resplist} =  Remove Server Profile Templates from variable  ${pts2_spts_create_expected}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF899 Synergy PTS3 Create the profiles
    Power off Servers in Profiles  ${pts3_profiles_create}  powerControl=PressAndHold
    ${resp}=  Add Server Profiles from variable  ${pts3_profiles_create}
    Wait For Task2  ${resp}   timeout=1800    interval=10

OVF899 Synergy PTS3 Verify the Profiles after Create
    Run Keyword for List with kwargs  ${pts3_profiles_create_expected}  Verify Server Profile  status=OK

OVF899 Synergy PTS3 Check Profile Local Storage Alerts after Create
    ${profile1_uri} =  Get Server Profile URI  ${pts3_profile1_create['name']}
    ${profile1_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile1_uri}'"&sort=created:descending&count=1
    ${profile2_uri} =  Get Server Profile URI  ${pts3_profile2_create['name']}
    ${profile2_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile2_uri}'"&sort=created:descending&count=1
    ${profile3_uri} =  Get Server Profile URI  ${pts3_profile3_create['name']}
    ${profile3_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile3_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS3 Verify Redfish Smartstorageconfig after Create
    Verify RIS nodes for list  ${pts3_ris_nodes_after_create}

OVF899 Synergy PTS3 Delete the Profiles after Create
    Power off Servers in Profiles  ${pts3_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts3_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF899 Synergy PTS3 Create the Profiles to Import
    Power off Servers in Profiles  ${pts3_profiles_import}  powerControl=PressAndHold
    ${resp}=  Add Server Profiles from variable  ${pts3_profiles_import}
    Wait For Task2  ${resp}   timeout=1800    interval=10

OVF899 Synergy PTS3 Verify the Profiles after Import
    Run Keyword for List  ${pts3_profiles_import_expected}  Verify Server Profile  status=OK

OVF899 Synergy PTS3 Check Profile Local Storage Alerts after Import
    ${profile1_uri} =  Get Server Profile URI  ${pts3_profile1_create['name']}
    ${profile1_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile1_uri}'"&sort=created:descending&count=1
    ${profile2_uri} =  Get Server Profile URI  ${pts3_profile2_create['name']}
    ${profile2_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile2_uri}'"&sort=created:descending&count=1
    ${profile3_uri} =  Get Server Profile URI  ${pts3_profile3_create['name']}
    ${profile3_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile3_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS3 Verify Redfish Smartstorageconfig after Import
    Verify RIS nodes for list  ${pts3_ris_nodes_after_create}

OVF899 Synergy PTS3 Edit the Profiles
    Power off Servers in Profiles  ${pts3_profiles_edit}  powerControl=PressAndHold
    ${resp}=  Edit Server Profiles from variable  ${pts3_profiles_edit}
    Wait For Task2  ${resp}   timeout=1800    interval=10

OVF899 Synergy PTS3 Verify the Profiles after Edit
    Run Keyword for List with kwargs  ${pts3_profiles_edit}  Verify Server Profile  status=OK

OVF899 Synergy PTS3 Check Profile Local Storage Alerts after Edit
    ${profile1_uri} =  Get Server Profile URI  ${pts3_profile1_create['name']}
    ${profile1_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile1_uri}'"&sort=created:descending&count=1
    ${profile2_uri} =  Get Server Profile URI  ${pts3_profile2_create['name']}
    ${profile2_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile2_uri}'"&sort=created:descending&count=1
    ${profile3_uri} =  Get Server Profile URI  ${pts3_profile3_create['name']}
    ${profile3_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile3_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS3 Verify Redfish Smartstorageconfig after Edit
    Verify RIS nodes for list  ${pts3_ris_nodes_after_edit}

OVF899 Synergy PTS3 Delete the Profiles after Edit
    Power off Servers in Profiles  ${pts3_profiles_edit}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts3_profiles_edit}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF899 Synergy PTS4 Create the profiles
    Power off Servers in Profiles  ${pts4_profiles_create}  powerControl=PressAndHold
    ${resp}=  Add Server Profiles from variable  ${pts4_profiles_create}
    Wait For Task2  ${resp}   timeout=1800    interval=10

OVF899 Synergy PTS4 Verify the Profiles after Create
    Run Keyword for List with kwargs  ${pts4_profiles_create_expected}  Verify Server Profile  status=OK

OVF899 Synergy PTS4 Check Profile Local Storage Alerts after Create
    ${profile1_uri} =  Get Server Profile URI  ${pts4_profile1_create['name']}
    ${profile1_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile1_uri}'"&sort=created:descending&count=1
    ${profile2_uri} =  Get Server Profile URI  ${pts4_profile2_create['name']}
    ${profile2_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile2_uri}'"&sort=created:descending&count=1
    ${profile3_uri} =  Get Server Profile URI  ${pts4_profile3_create['name']}
    ${profile3_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile3_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS4 Verify Redfish Smartstorageconfig after Create
    Verify RIS nodes for list  ${pts4_ris_nodes_after_create}

OVF899 Synergy PTS4 Edit the Profiles to Remove LDs
    Power off Servers in Profiles  ${pts4_profiles_edit1}  powerControl=PressAndHold
    ${resp}=  Edit Server Profiles from variable  ${pts4_profiles_edit1}
    Wait For Task2  ${resp}   timeout=1800    interval=10

OVF899 Synergy PTS4 Verify the Profiles after Remove LDs
    Run Keyword for List  ${pts4_profiles_edit1}  Verify Server Profile

OVF899 Synergy PTS4 Check Profile Local Storage Alerts after Remove LDs
    ${profile1_uri} =  Get Server Profile URI  ${pts4_profile1_create['name']}
    ${profile1_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile1_uri}'"&sort=created:descending&count=1
    ${profile2_uri} =  Get Server Profile URI  ${pts4_profile2_create['name']}
    ${profile2_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile2_uri}'"&sort=created:descending&count=1
    ${profile3_uri} =  Get Server Profile URI  ${pts4_profile3_create['name']}
    ${profile3_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile3_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS4 Verify Redfish Smartstorageconfig after Remove LDs
    Verify RIS nodes for list  ${pts4_ris_nodes_after_edit1}

OVF899 Synergy PTS4 Edit the Profiles to Add LDs
    Power off Servers in Profiles  ${pts4_profiles_edit2}  powerControl=PressAndHold
    ${resp}=  Edit Server Profiles from variable  ${pts4_profiles_edit2}
    Wait For Task2  ${resp}   timeout=1800    interval=10

OVF899 Synergy PTS4 Verify the Profiles after Add LDs
    Run Keyword for List  ${pts4_profiles_edit2}  Verify Server Profile

OVF899 Synergy PTS4 Check Profile Local Storage Alerts after Add LDs
    ${profile1_uri} =  Get Server Profile URI  ${pts4_profile1_create['name']}
    ${profile1_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile1_uri}'"&sort=created:descending&count=1
    ${profile2_uri} =  Get Server Profile URI  ${pts4_profile2_create['name']}
    ${profile2_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile2_uri}'"&sort=created:descending&count=1
    ${profile3_uri} =  Get Server Profile URI  ${pts4_profile3_create['name']}
    ${profile3_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile3_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS4 Verify Redfish Smartstorageconfig after Add LDs
    Verify RIS nodes for list  ${pts4_ris_nodes_after_edit2}

OVF899 Synergy PTS4 Delete the Profiles
    Power off Servers in Profiles  ${pts4_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts4_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF899 Synergy PTS5 Create the Profile
    Power off Servers in Profiles  ${pts5_profiles_create}  powerControl=PressAndHold
    ${resp}=  Add Server Profiles from variable  ${pts5_profiles_create}
    Wait For Task2  ${resp}   timeout=1800    interval=10

OVF899 Synergy PTS5 Verify the Profiles after Create
    Run Keyword for List with kwargs  ${pts5_profiles_create_expected}  Verify Server Profile  status=OK

OVF899 Synergy PTS5 Check Profile Local Storage Alerts after Create
    ${profile1_uri} =  Get Server Profile URI  ${pts5_profile1_create['name']}
    ${profile1_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile1_uri}'"&sort=created:descending&count=1
    ${profile2_uri} =  Get Server Profile URI  ${pts5_profile2_create['name']}
    ${profile2_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile2_uri}'"&sort=created:descending&count=1
    ${profile3_uri} =  Get Server Profile URI  ${pts5_profile3_create['name']}
    ${profile3_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile3_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS5 Verify Redfish Smartstorageconfig after Create
    Verify RIS nodes for list  ${pts5_ris_nodes_after_create}

OVF899 Synergy PTS5 Remove Server1
    Remove the blade  ${SERVER1}

OVF899 Synergy PTS5 Remove Server2
    Remove the blade  ${SERVER2}

OVF899 Synergy PTS5 Remove Server3
    Remove the blade  ${SERVER3}

OVF899 Synergy PTS5 Add Server1 Back
    Add the blade  ${SERVER1}

OVF899 Synergy PTS5 Add Server2 Back
    Add the blade  ${SERVER2}

OVF899 Synergy PTS5 Add Server3 Back
    Add the blade  ${SERVER3}
    #Added EfuseReset to bring back the server with SmartArray
    Reset the Blade    ${SERVER3}

OVF899 Synergy PTS5 Verify the Profiles after Add the Blade Back
    Wait Until Keyword Succeeds  60s  5s  Run Keyword for List with kwargs  ${pts5_profiles_create_expected}  Verify Server Profile  status=OK

OVF899 Synergy PTS5 Check Profile Local Storage Alerts after Add the Blade Back
    ${profile1_uri} =  Get Server Profile URI  ${pts5_profile1_create['name']}
    ${profile1_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile1_uri}'"&sort=created:descending&count=1
    ${profile2_uri} =  Get Server Profile URI  ${pts5_profile2_create['name']}
    ${profile2_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile2_uri}'"&sort=created:descending&count=1
    ${profile3_uri} =  Get Server Profile URI  ${pts5_profile3_create['name']}
    ${profile3_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile3_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS5 Delete the Profiles
    Power off Servers in Profiles  ${pts5_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts5_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF899 Synergy PTS6 Create the Profile
    Power off Servers in Profiles  ${pts6_profiles_create}  powerControl=PressAndHold
    ${resp}=  Add Server Profiles from variable  ${pts6_profiles_create}
    Wait For Task2  ${resp}   timeout=1800    interval=10

OVF899 Synergy PTS6 Verify the Profiles after Create
    Run Keyword for List with kwargs  ${pts6_profiles_create_expected}  Verify Server Profile  status=OK

OVF899 Synergy PTS6 Check Profile Local Storage Alerts after Create
    ${profile_uri} =  Get Server Profile URI  ${pts6_profile_create['name']}
    ${profile_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS6 Verify Redfish Smartstorageconfig after Create
    Verify RIS nodes for list  ${pts6_ris_nodes_after_create}

OVF899 Synergy PTS6 Move the Profile
    Power off Servers in Profiles  ${pts6_profiles_move}  powerControl=PressAndHold
    ${resp}=  Edit Server Profiles from variable  ${pts6_profiles_move}
    Wait For Task2  ${resp}   timeout=1800    interval=10

OVF899 Synergy PTS6 Verify the Profiles after Move
    Run Keyword for List with kwargs  ${pts6_profiles_move_expected}  Verify Server Profile  status=OK

OVF899 Synergy PTS6 Check Profile Local Storage Alerts after Move
    ${profile_uri} =  Get Server Profile URI  ${pts6_profile_move['name']}
    ${profile_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS6 Verify Redfish Smartstorageconfig after Move
    Verify RIS nodes for list  ${pts6_ris_nodes_after_move}

OVF899 Synergy PTS6 Delete the Profiles
    Power off Servers in Profiles  ${pts6_profiles_move}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts6_profiles_move}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF899 Synergy PTS7 Create the Profile
    Power off Servers in Profiles  ${pts7_profiles_create}  powerControl=PressAndHold
    ${resp}=  Add Server Profiles from variable  ${pts7_profiles_create}
    Wait For Task2  ${resp}   timeout=1800    interval=10

OVF899 Synergy PTS7 Verify the Profiles after Create
    Run Keyword for List with kwargs  ${pts7_profiles_create_expected}  Verify Server Profile  status=OK

OVF899 Synergy PTS7 Check Profile Local Storage Alerts after Create
    ${profile_uri} =  Get Server Profile URI  ${pts7_profile_create['name']}
    ${profile_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS7 Power on the Server
    Power on Servers in Profiles  ${pts7_profiles_create}
    Wait for Servers in Profiles to reach POST State  ${pts7_profiles_create}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF899 Synergy PTS7 Verify Redfish Smartstorageconfig after Create
    Verify RIS nodes for list  ${pts7_ris_nodes_after_create}

OVF899 Synergy PTS7 Update Smartstorageconfig on iLO
    Update RIS SmartStorageConfig Settings DWC  ${SERVER2}  Disabled

OVF899 Synergy PTS7 Verify Redfish Smartstorageconfig Settings after Update on iLO
    Verify RIS nodes for list  ${pts7_ris_nodes_after_update_on_ilo}

OVF899 Synergy PTS7 Reset the Server
    Reset Server  ${SERVER2}
    Wait for Server to reach POST State  ${SERVER2}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF899 Synergy PTS7 Verify Profile Status after Server Reset
    Run Keyword for List with kwargs  ${pts7_profiles_create_expected}  Verify Server Profile  status=Warning

OVF899 Synergy PTS7 Check the Alert after Server Reset
    ${profile_uri} =  Get Server Profile URI  ${pts7_profile_create['name']}
    ${profile_alert} =  wait until keyword succeeds  1m  10s  Get Alert By Param   param=?filter=description like 'The drive write cache setting on the following SAS controller(s) is incompatible with local storage configuration from the server profile*' and alertState EQ 'Active' and resourceUri EQ '${profile_uri}'

OVF899 Synergy PTS7 Verify Redfish Smartstorageconfig after Server Reset
    Verify RIS nodes for list  ${pts7_ris_nodes_after_server_reset}

OVF899 Synergy PTS7 Delete the Profile
    Power off Servers in Profiles  ${pts7_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts7_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF899 Synergy PTS8 B/R Create the SPTs
    ${resplist}=  Add Server Profile Templates from variable	 ${pts8_spts_create}
    Wait for Task2  ${resplist}     timeout=120    interval=10

OVF899 Synergy PTS8 B/R Verify the SPTs after Create
    Verify Server Profile Templates  ${pts8_spts_create}

OVF899 Synergy PTS8 B/R Create the Profiles from SPTs
    Power Off Servers in Profiles  ${pts8_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Add Server Profiles from variable	 ${pts8_profiles_create}
    Wait For Task2  ${resplist}   timeout=1800    interval=10

OVF899 Synergy PTS8 B/R Verify the Profiles after Create
    Run Keyword for List with kwargs  ${pts8_profiles_create_expected}  Verify Server Profile  status=OK

OVF899 Synergy PTS8 Check Profile Local Storage Alerts after Add the Blade Back
    ${profile1_uri} =  Get Server Profile URI  ${pts8_profile1_create['name']}
    ${profile1_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile1_uri}'"&sort=created:descending&count=1
    ${profile2_uri} =  Get Server Profile URI  ${pts8_profile2_create['name']}
    ${profile2_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile2_uri}'"&sort=created:descending&count=1
    ${profile3_uri} =  Get Server Profile URI  ${pts8_profile3_create['name']}
    ${profile3_local_stoarge_alert} =  Get All Alerts By Param   param=?filter="description like 'Unable to apply the local storage settings*' and severity EQ 'Critical' and resourceUri EQ '${profile3_uri}'"&sort=created:descending&count=1

OVF899 Synergy PTS8 B/R Verify Profile Compliance after Create
    Run Keyword for List  ${pts8_profiles_compliance}  Verify Server Profile Compliance

OVF899 Synergy PTS8 B/R Verify Redfish Smartstorageconfig after Create
    Verify RIS nodes for list  ${pts8_ris_nodes_after_create}

OVF899 Synergy PTS8 B/R Create Backup
    Create Backup
    ${uri} =    Get Backup URI
    Set Suite Variable    ${BACKUPURI}    ${uri}

OVF899 Synergy PTS8 B/R Delete the Profiles
    Power off Servers in Profiles  ${pts8_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts8_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF899 Synergy PTS8 B/R Remove the SPTs
    ${resplist} =  Remove Server Profile Templates from variable  ${pts8_spts_create}
    wait for task2  ${resplist}  timeout=900  interval=10

OVF899 Synergy PTS8 B/R Restore
    ${resp}=    Initiate Restore    ${BACKUPURI}

OVF899 Synergy PTS8 B/R Wait for Restore to Complete
    Wait Until Keyword Succeeds    90m    30s    OneView Restore Complete

OVF899 Synergy PTS8 B/R Verify the SPTs after Restore
    Fusion Api Login Appliance 		${APPLIANCE_IP}  ${admin_credentials}
    Verify Server Profile Templates  ${pts8_spts_create}

OVF899 Synergy PTS8 B/R Verify the Profiles Status Critical after Restore
    Run Keyword for List with kwargs  ${pts8_profiles_create_expected}  Verify Server Profile  status=Critical

OVF899 Synergy PTS8 B/R Check Profiles Alerts
    ${profile1_uri} =  Get Server Profile URI  ${pts8_profile1_create['name']}
    ${profile1_alert} =  wait until keyword succeeds  1m  10s  Get Alert By Param   param=?filter=description like 'Server profile settings conflict with the server hardware configuration.' and alertState EQ 'Locked' and resourceUri EQ '${profile1_uri}'
    ${profile2_uri} =  Get Server Profile URI  ${pts8_profile2_create['name']}
    ${profile2_alert} =  wait until keyword succeeds  1m  10s  Get Alert By Param   param=?filter=description like 'Server profile settings conflict with the server hardware configuration.' and alertState EQ 'Locked' and resourceUri EQ '${profile2_uri}'
    ${profile3_uri} =  Get Server Profile URI  ${pts8_profile3_create['name']}
    ${profile3_alert} =  wait until keyword succeeds  1m  10s  Get Alert By Param   param=?filter=description like 'Server profile settings conflict with the server hardware configuration.' and alertState EQ 'Locked' and resourceUri EQ '${profile3_uri}'

OVF899 Synergy PTS8 B/R Unassign the Profiles
    Power Off Servers in Profiles  ${pts8_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Edit Server Profiles from variable	 ${pts8_profiles_unassign}
    Wait For Task2  ${resplist}   timeout=1800    interval=10

OVF899 Synergy PTS8 B/R Reassign the Profiles
    Power Off Servers in Profiles  ${pts8_profiles_reassign}  powerControl=PressAndHold
    ${resplist}=  Edit Server Profiles from variable	 ${pts8_profiles_reassign}
    Wait For Task2  ${resplist}   timeout=1800    interval=10

OVF899 Synergy PTS8 B/R Verify the Profiles after Reassign
    Run Keyword for List with kwargs  ${pts8_profiles_create_expected}  Verify Server Profile  status=OK

OVF899 Synergy PTS8 B/R Verify Profile Compliance after Reassign
    Run Keyword for List  ${pts8_profiles_compliance}  Verify Server Profile Compliance

OVF899 Synergy PTS8 B/R Verify Redfish Smartstorageconfig after Reassign
    Verify RIS nodes for list  ${pts8_ris_nodes_after_create}

OVF899 Synergy PTS8 B/R Delete the Profiles after Restore
    Power off Servers in Profiles  ${pts8_profiles_create}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${pts8_profiles_create}  force=${True}
    Wait for Task2  ${resplist}     timeout=900    interval=10

OVF899 Synergy PTS8 B/R Remove the SPTs after Restore
    ${resplist} =  Remove Server Profile Templates from variable  ${pts8_spts_create}
    wait for task2  ${resplist}  timeout=900  interval=10

*** Keywords ***
OVF899 Synergy Setup
    [Documentation]  OVF899 Synergy Setup
    ${feature} =  set variable  OVF899 Synergy
    log  ${feature} Suite Setup: Start suite setup  console=True
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

    # Verify the initial Redfish smartstorageconfig
    Verify RIS nodes for list  ${suite_setup_ris_nodes}

    # Clean up the profiles
    Log  ${feature} Suite Setup: Cleanup the profiles  console=True
    Power Off Servers in Profiles  ${suite_setup_profiles}  powerControl=PressAndHold
    ${resplist} =  Remove Server Profiles from variable  ${suite_setup_profiles}
    Wait for task2  ${resplist}  timeout=3600  interval=10

    # Create the profiles to initialze the controllers
    Log  ${feature} Suite Setup: Create profiles to initialize the controllers  console=True
    Power off Servers in Profiles  ${suite_setup_profiles}  powerControl=PressAndHold
    ${resplist}=  Add Server Profiles from variable	 ${suite_setup_profiles}
    Wait for Task2  ${resplist}  timeout=1800  interval=10

    # Remove the profiles
    Log  ${feature} Suite Setup: Remove the profiles  console=True
    Power Off Servers in Profiles  ${suite_setup_profiles}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${suite_setup_profiles}
    Wait for Task2  ${resplist}  timeout=900  interval=10

Remove the Blade
    [Documentation]  Remove the blade
    [Arguments]  ${server}  ${timeout}=120  ${interval}=1
    EM EFUSE Blade  ${server}  action=EFuseOn
    ${task} =  Wait Until Keyword Succeeds  120s  1ms  Get task by param  param=?filter='name'='Remove' AND associatedResource.resourceName='${server}' AND taskState='Running'
    Wait for task2  ${task}  timeout=${timeout}  interval=${interval}
    Log  Remove the blade ${server} task ${task['uri']} completed  console=True

Add the Blade
    [Documentation]  Add the blade
    [Arguments]  ${server}  ${timeout}=600  ${interval}=5
    EM EFUSE Blade  ${server}  action=EFuseOff
    ${task} =  Wait Until Keyword Succeeds  300s  1s  Get task by param  param=?filter='name'='Add' AND associatedResource.resourceName='${server}' AND taskState='Running'
    Wait for task2  ${task}  timeout=${timeout}  interval=${interval}
    Log  Add the blade ${server} task ${task['uri']} completed  console=True

EM EFUSE Blade
    [Documentation]  EN Efuse Blade
    [Arguments]     ${server}  ${action}=
    ${words} =  set variable  ${server.split(',')}
    ${enclosure} =  set variable  ${words[0]}
    ${bay} =  set variable  ${words[1]}
    ${bay} =  set variable  ${bay.strip()}
    ${bay} =  set variable  ${bay[-1]}
    Get EM IP  enc_serial=${enclosure}
    Get EM Token    ${enclosure}
    EFuse Blade   ${action}  ${bay}
    Log  EFUSE blade ${bay} ${action} on enclosure ${enclosure}  console=True

Reset the Blade
    [Documentation]  Reset the blade
    [Arguments]  ${server}  ${timeout}=600  ${interval}=5
    EM EFUSE Blade  ${server}  action=EFuseReset
    ${task1} =  Wait Until Keyword Succeeds  120s  1ms  Get task by param  param=?filter='name'='Remove' AND associatedResource.resourceName='${server}' AND taskState='Running'
    ${task} =  Wait Until Keyword Succeeds  300s  1s  Get task by param  param=?filter='name'='Add' AND associatedResource.resourceName='${server}' AND taskState='Running'
    Wait for task2  ${task}  timeout=${timeout}  interval=${interval}
    Log  Reset the blade ${server} task ${task['uri']} completed  console=True
