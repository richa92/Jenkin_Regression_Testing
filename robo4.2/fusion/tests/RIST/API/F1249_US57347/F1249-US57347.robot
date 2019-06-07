*** Settings ***
Documentation       F1249 US57347 software and Hardware iSCSI boot on Tbird with DHCP
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
#Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${CURDIR}\\${DATA_FILE}

Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}		'16.114.209.223'
${DATA_FILE}         Regression_Data.py

*** Test Cases ***
F1249 US57347 Appliance Login
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

F1249 US57347 Add existing Volume
    [Tags]    F1249_SY_Add_Vol
    ${resplist} =  Add Existing Storage Volumes Async  ${existing_volumes}
    Wait for Task2  ${resplist}  timeout=30  interval=10

F1249 US57347 Create Server Profile Templates
   [Tags]    F1249_SY_SPT
   Create Server Profile Templates

F1249 US57347 Create Server Profiles
   [Tags]    F1249_SY_SP
   Create Server Profiles

F1249 US57347 Verify RIS Node for SW iSCSI Profiles
    Verify RIS Nodes after Create

# F1249 US57347 Verify hpmctp data for HW iSCSI Profiles
#    Verify hpmctp Nodes after Create

F1249 US57347 Edit Server Profile Template Change from userSpecified to DHCP
   [Tags]    F1249_SY_Edit_SPT
   Edit Server Profile Template Change from userSpecified to DHCP

F1249 US57347 Edit Profile From DHCP to User Specified
    [Tags]    F1249_SY_Edit_SP
    Edit Profile From DHCP to User Specified

F1249 US57347 Edit Profile From User Specified to DHCP
    [Tags]    F1249_SY_Edit_SP2
    Edit Profile From User Specified to DHCP

F1249 US57347 delete Profile1 for bay 6 to move profile to Bay 1
   [Tags]    F1249_SY_MV_SP
   delete Profile1 for bay 6 to move profile to Bay 1

F1249 US57347 Move DHCP Profile from SY660 to SY480 blade
    [Tags]    F1249_SY_MV_SP2
    Move DHCP Profile from SY660 to SY480 blade

#Create DHCP Server Profile 300
#    Create DHCP Server Profile 300

#GET DHCP Server Profile Template With Version300
#    GET DHCP Server Profile Template 300

#GET DHCP Server Profile With Version300
#    GET DHCP Server Profile 300

#EDIT DHCP Server Profile Template With Version300 Add DHCP connection
#    Edit DHCP Server Profile Template 300

#Create DHCP Server Profile With Version300 Add DHCP connection
#    Create DHCP Server Profile 300

#Edit DHCP Server Profile With Version300 Add DHCP connection
#    Edit DHCP Server Profile 300

#Edit Storage System With Tunnel Network
#    Edit Storage System With Tunnel Network

#Create Server Profiles with Tunnel Network with DHCP
#   Create Server Profiles with Tunnel Network with DHCP

*** Keywords ***
Setup
    [Documentation]    F1249_US57347 setup
    Set Log Level  DEBUG
    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
    ${admin_session} =    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Power off Servers in Profiles    ${server_profiles}
    Remove All Server Profile Templates
    ${resp} =    Remove Server Profiles from variable    ${server_profiles}
    Wait For Task2    ${resp}	   timeout=2400	interval=15

Clean Up
    [Documentation]    F1249_US57347 Teardown
    Power off Servers in Profiles    ${server_profiles}
    ${resp} =    Remove Server Profiles from variable    ${server_profiles}
    Wait For Task2    ${resp}       timeout=2400    interval=15
    Remove All Server Profile Templates
    ${resplist} =  Remove Storage Volumes Async  ${existing_volumes}  param=?suppressDeviceUpdates=true
    Wait For Task2  ${resplist}  timeout=30  interval=10
    Fusion Api Logout Appliance

Create Server Profile Templates
    [Documentation]  Create Server Profile Templates
    :FOR	${profile_template}	IN	@{profile_templates}
	\		${resp} = 	Add Server Profile Template   ${profile_template}
	\		log to console		${resp}
	\      Wait For Task2	${resp}	   timeout=60	interval=5

Create Server Profiles
    [Documentation]  Create Server Profiles
    Power off Servers in Profiles    ${server_profiles}
    ${resp} =    Remove Server Profiles from variable    ${server_profiles}
    Wait For Task2    ${resp}	   timeout=2400	interval=15
    @{resplist} =    Create List
    :FOR	${server_profile}	IN	@{server_profiles}
	\    ${resp} =    Add Server Profile    ${server_profile}
	\    Append To List    ${resplist}    ${resp}
    Wait For Task2	${resplist}    timeout=2400    interval=20

Verify RIS Nodes after Create
    [Documentation]  Create Server Profiles
    Power on Servers in Profiles  ${server_profiles}
    Wait for Servers in Profiles to reach POST State  ${server_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s
    Verify RIS nodes for list  ${sw_iscsi_ris}

Verify hpmctp Nodes after Create
    [Documentation]  Create Server Profiles
    Verify iSCSI Adapter Settings with hpMCTP for list      ${hw_iscsi_hpmctp}

Edit Server Profile Template Change from userSpecified to DHCP
    [Documentation]  Create Server Profiles
    Power off All Servers  control=PressAndHold
	${resp} = 	Edit Server Profile Template	${edit_profile_template}
	log to console		${resp}
	Wait For Task2	${resp}	   timeout=2400	interval=5

Edit Profile From DHCP to User Specified
    [Documentation]  Create Server Profiles
    ${resp} = 	Edit Server Profile	${edit_profile}
	log to console		${resp}
	Wait For Task2	${resp}	   timeout=2400	interval=5

Edit Profile From User Specified to DHCP
    [Documentation]  Create Server Profiles
    ${resp} = 	Edit Server Profile	${edit_profile_back_to_dhcp}
	log to console		${resp}
	Wait For Task2	${resp}	   timeout=2400	interval=5

delete Profile1 for bay 6 to move profile to Bay 1
    [Documentation]  Create Server Profiles
    ${resp} = 	Remove Server Profile        ${server_profiles[0]}
    log to console		${resp}
	Wait For Task2	${resp}	   timeout=2400	interval=5

Move DHCP Profile from SY660 to SY480 blade
    [Documentation]  Create Server Profiles
    ${resp} = 	Edit Server Profile	${move_bay5_to_bay7_profile_with_dhcp}
	log to console		${resp}
	Wait For Task2	${resp}	   timeout=2400	interval=5

Negative Tests Server Profiles
    [Documentation]  Create Server Profiles
    Power Off All Servers    control=PressAndHold
    ${negative_server_profile_tasks} =	Get Variable Value	${negative_server_profile_tasks}
    Run Negative Tasks for List     ${negative_server_profile_tasks}

GET DHCP Server Profile 300
    [Documentation]  Create Server Profiles
    Verify Resource  ${profile300_verify}  api=300

GET DHCP Server Profile Template 300
    [Documentation]  Create Server Profiles
    Verify Resource  ${profileTemplate300_verify}  api=300

Edit DHCP Server Profile Template 300
    [Documentation]  Create Server Profiles
    ${responses} = 	Edit Server Profile Templates from variable     ${edit_profile_tempalte300}  api=300
	:FOR	${resp}	IN	@{responses}
	\		log to console		${resp}
	\      ${x} =  set variable if  '${resp['errorCode']}'=='UNRECOGNIZED_JSON_FIELD'  PASS  error
	[return]  ${x}

Create DHCP Server Profile 300
    [Documentation]  Create Server Profiles
    ${responses} = 	Add Server Profiles from variable     ${create_dhcp_profile_300}  api=300
	:FOR	${resp}	IN	@{responses}
	\		log to console		${resp}
	\      ${x} =  set variable if  '${resp['errorCode']}'=='UNRECOGNIZED_JSON_FIELD'  PASS  error
	[return]  ${x}

Edit DHCP Server Profile 300
    [Documentation]  Create Server Profiles
    ${responses} = 	Edit Server Profiles from variable     ${edit_profile300}  api=300
	:FOR	${resp}	IN	@{responses}
	\		log to console		${resp}
	\      ${x} =  set variable if  '${resp['errorCode']}'=='UNRECOGNIZED_JSON_FIELD'  PASS  error
	[return]  ${x}

Edit Storage System With Tunnel Network
    [Documentation]  Create Server Profiles
    ${resp} = 	Edit Storage System     ${edit_storage_system}
    log to console		${resp}
	Wait For Task2	${resp}	   timeout=2400	interval=5

Create Server Profiles with Tunnel Network with DHCP
    [Documentation]  Create Server Profiles
    Power off All Servers  control=PressAndHold
    Remove All Server Profiles
    :FOR	${server_profile}	IN	@{server_profiles_tunnel}
	\		${resp} = 	Add Server Profile	${server_profile}
	\		log to console		${resp}
	\      Wait For Task2	${resp}    timeout=2400    interval=20
