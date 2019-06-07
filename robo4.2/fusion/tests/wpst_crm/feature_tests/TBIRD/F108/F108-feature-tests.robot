*** Settings ***
Documentation		Feature Test: F108 ME Feature tests for TClass
...					Usage:
...						BB58 ME: pybot -V bb58_me_variables.py -v APPLIANCE_IP:15.199.232.97 feature_test_F105.txt
...						DCS ME: pybot -V dcs_variables.py feature_test_F105.txt

#Resource        ../../../../../Resources/api/fusion_api_resource.txt
#Resource        ../FVT/fvt-keywords.txt
#Resource		../FVT/Resources/fvt_resource.txt
#Resource       resource.txt
Resource        ../../../../resource/fusion_api_all_resource_files.txt

#Library			../FVT/fvt_api.py
Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary

Variables		data_variables.py

Library         Dialogs
Library			Collections

#Suite Setup   		Test Specific setup
#Suite Setup   		Run FTS and test-specific setup
#Suite Teardown		Teardown

*** Variables ***
${SSH_USER}                     root
${SSH_PASS}                     hpvse1
${APPLIANCE_IP}					1
${VM}							15.245.131.12

*** Test Cases ***
F108 Appliance Login
    [Tags]  1    POSITIVE   LOGIN   LIGS EGS  LES   SPS
	Set Log Level	TRACE
	Fusion Api Login Appliance     ${APPLIANCE_IP}		${admin_credentials}

F108 pre_setup
    [Tags]    DEBUG
   	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Test Specific setup

F108 Create LIGs and EGs
    [Tags]   CONFIGURE   LOGICAL ENCLOSURE GROUP   LIGS   ENCLOSURE GROUPS  EGS
   	${ligs} =	Get Variable Value	${ligs}
	Run Keyword If	${ligs} is not ${null}	Run Keyword for List	${ligs}	Add LIG from variable
	${enc_groups} =	Get Variable Value	${enc_groups}
	Run Keyword If	${enc_groups} is not ${null}	Run Keyword for Dict	${enc_groups}	Add Enclosure Group from variable

F108 Add Logical Enclosures
	[Tags]    CONFIGURE   LOGICAL ENCLOSURES    LES
	${les} =	Get Variable Value	${les}
	${task} =   Add Logical Enclosure from variable     ${les['3Frame-ibs23-LE']}
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ((?i)Warning|Completed)
#    Pass Execution    Completed Add Logical Enclosures

F108 Add Server Profiles
	[Tags]    CONFIGURE   SERVER PROFILES    SPS
	Power Off Servers
	${server_profiles} =	Get Variable Value	${server_profiles}
	Run Keyword If	${server_profiles} is not ${null}		Add Server Profiles from variable	${server_profiles}
#    ${task} =   Add Server Profiles from variable	${server_profiles['CN754406W7_Bay1_SP']}
#    ${task} =   Add Server Profiles from variable	${server_profiles[1]}
#	${task_state} = 	Get From dictionary 	${task}     taskState
#	Should Match Regexp	${task_state}	 ((?i)Warning|Completed)

F108 end to end test
    Run Keyword for List	${servers}	Power on Server
	Log to console and logfile  	Waiting 20 minutes for servers to boot...
    Sleep   20min
    Run Keyword for List    ${PING_LIST_1}   Wait For Appliance To Become Pingable

*** Keywords ***
Remove all the keys in response that are not in validation
	[Arguments]	${vkeys}	${rkeys}
	:FOR	${x}	IN	@{vkeys}
	\	Remove Values From List	${rkeys}	${x}
	[Return]	${rkeys}

Match Value In List
    [Documentation]   Check if a value exists in list
    [Arguments]   ${val}   ${valList}
    :FOR   ${v}   IN   @{valList}
    \   Return From Keyword If   '${v}' == '${val}'   ${True}
    [Return]   ${False}

Teardown
	Set Log Level	TRACE
	Log to console and logfile	[TEARDOWN]
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
	Power off ALL Servers
	Remove All Server Profiles
	Remove ALL LS
	Remove ALL LSGs
	Remove All Logical Enclosures
	Remove ALL Enclosure Groups
	Remove ALL LIGs
	Remove ALL Ethernet Networks
	Remove ALL FC Networks
	Remove ALL FCoE Networks
	Remove ALL Network Sets
	Remove ALL Users

Run FTS and test-specific setup
	Set Log Level	TRACE
    FTS
    Test Specific Setup
#    Feature Specific Setup

FTS
    [Tags]  FTS
	Set Log Level	DEBUG
	log variables
    Get VM IP   ${VM}
	First Time Setup    password=hpvse123    interface=bond0

#Login
#    [Tags]  Setup   TSS     1    2    3    4    5    6    7    8    9    10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25
#    ...                     26    27    28    29    30    31    32    33    34    35    36    37    38    39    40    41    42    43    44    45    46    50	X    BFS
#	Set Log Level	DEBUG
#	log variables
#    Get VM IP   ${VM}
#	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

Test Specific Setup
    [Tags]  TSS     Setup
	Set Log Level	TRACE
	Run Keyword and Ignore Error    Write To ciDebug Log
	Log to console and logfile	[TEST-SPECIFIC SETUP]
	${users} =	Get Variable Value	${users}
	Run Keyword If	${users} is not ${null}	Add Users from variable				${users}
	${ethernet_networks} =	Get Variable Value	${ethernet_networks}
	Run Keyword If	${ethernet_networks} is not ${null}	Add Ethernet Networks from variable	${ethernet_networks}
    ${ethernet_ranges} =	Get Variable Value	${ethernet_ranges}
	Run Keyword If	${ethernet_ranges} is not ${null}		Run Keyword for List	${ethernet_ranges}	Create Ethernet Range
	${fcoe_networks} =	Get Variable Value	${fcoe_networks}
	Run Keyword If	${fcoe_networks} is not ${null}	        Add FCoE Networks from variable		${fcoe_networks}
	${network_sets} =	Get Variable Value	${network_sets}
	Run Keyword If	${network_sets} is not ${null}	Add Network Sets from variable		${network_sets}

	#${ranges} =	Get Variable Value	${ranges}
	#${pools} =  Run Keyword If	${ranges} is not ${null}	Create List		/rest/id-pools/vmac	/rest/id-pools/vwwn	/rest/id-pools/vsn
    #Run Keyword If	${ranges} is not ${null}                Run Keyword for List	${pools}	Disable ALL Generated ID Ranges
	#Run Keyword If	${ranges} is not ${null}				Add Ranges From variable	${ranges}

Power Off Servers
	[Tags]    CONFIGURE   POWER OFF SERVERS    OFF
	Power Off All Servers

Add Ranges
	[Tags]    CONFIGURE   RANGES
	${ranges} =	Get Variable Value	${ranges}
	${pools} =  Run Keyword If	${ranges} is not ${null}	Create List		/rest/id-pools/vmac	/rest/id-pools/vwwn	/rest/id-pools/vsn
    Run Keyword If	${ranges} is not ${null}                Run Keyword for List	${pools}	Disable ALL Generated ID Ranges
	Run Keyword If	${ranges} is not ${null}				Add Ranges From variable	${ranges}

F108 Add Server Profiles No Hardware Assigned
 	[Tags]    CONFIGURE   SERVER PROFILES NO HW    SPSNOHW
   	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
 	${server_profiles} =	Get Variable Value	${server_profiles_nohw}
 	Run Keyword If	${server_profiles} is not ${null}		Add Server Profiles from variable no hardware	${server_profiles}   ${server_profile_to_bay_map}

F108 Assign Server Hardware To Profile
	[Tags]	CONFIGURE	ASSIGN HARDWARE   SPADDHW
   	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
 	${server_profiles} =	Get Variable Value	${server_profiles_nohw}
	Log to console and logfile	Assigning Server Hardware to Profiles
 	Run Keyword If	${server_profiles} is not ${null}		Assign Server Hardware To Existing Profiles From Variable	${server_profiles}   ${server_profile_to_bay_map}   waitForTask=${True}
