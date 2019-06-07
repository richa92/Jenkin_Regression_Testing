*** Settings ***
Documentation		OVF565 Remove 162 Network limit
...                 Tests are run in Grow Logical Enclosure configuration
...                 to test limits in various ME configurations
...                 SuiteName: OVF565grow

...					Usage (Rack AV51 ME):
...					Note: update Enclosure serial #s in data_common.py file and run following command
...					Note: Make sure Server Hardware Type matching to data file
...					E.g. SHT:SY 480 Gen9 1 or SHT:SY 480 Gen9 2 etc.
...					pybot -d /tmp/logs/OVF565 -T -V data_redundant_cl10.py -v APPLIANCE_IP:15.245.131.182 -v max:2 OVF565grow.robot

# Additional info about command usage.
#pybot –V data_file  [-v start:x] [-v max:x] [-v inc:x] grow.txt
#
#Where
#1.	data_file:
#data file for a specific configuration, for example, data_ha_cl10 for HA configuration with CL10,
#data_redundant_cl20 for Redundant configuration with CL20,…etc.
#2.	start:
#optional.  number of enclosures you want to start with. It can be any number.
#If not given then the default value is 1 for redundant and 2 for HA.
#3.	max:
#optional. max number of enclosures to grow to. It can be any number.
#If not given then the default value is 5 for CL10 and 3 for CL20.
#4.	Inc:
#optional. number of enclosures you want to grow each time. It can be any number.
#If not given then the default value is 1.
#

Resource            ../../../../../Resources/api/fusion_api_resource.txt
Resource            ../FVT/fvt-keywords.txt
Resource			../FVT/Resources/fvt_resource.txt
Resource            ./additionalOVF565-keywords.txt

Library				FusionLibrary
Library				../FVT/fvt_api.py
Library				Process

Suite Setup			Login User

*** Variables ***
${LE}	${les['name']}

*** Keywords ***
Login User
    [Documentation]    Common login and setting variables keyword for test cases
	Set Log Level	TRACE
	Fusion Api Login Appliance	${appliance_ip}	${admin_credentials}
	${start_in} =	Get Variable Value	${start}	None
	${start_in} =	Set Variable If	
	...	${start_in} != None	${start_in}	
	...	'${CONFIG}' == 'HA'	2	1
	Set Suite Variable	${start}	${start_in}
	${inc_in} =	Get Variable Value	${inc}	None
	${inc_in} =	Set Variable If	${inc_in} != None	${inc_in}	1
	Set Suite Variable	${inc}	${inc_in}	
	${max_in} =	Get Variable Value	${max}	None
	${max_in} =	Set Variable If	
	...	${max_in} != None	${max_in}	
	...	'${CXP}' == 'CL10'	5	3
	Set Suite Variable	${max_frame}	${max_in}
    Setup Grow Variables
	[Return]

Test Specific Setup
    [Documentation]    Common setup tasks for test cases to run
    [Tags]  TSS     Setup
	Set Log Level	TRACE
	Run Keyword and Ignore Error    Write To ciDebug Log
	Log to console	[TEST-SPECIFIC SETUP]
	${users} =	Get Variable Value	${users}
	Run Keyword If	${users} is not ${null}	Add Users from variable				${users}
	${fcoe_networks} =	Get Variable Value	${fcoe_networks}
	Run Keyword If	${fcoe_networks} is not ${null}	        Add FCoE Networks from variable		${fcoe_networks}
	${ethernet_networks} =	Get Variable Value	${ethernet_networks}
	Run Keyword If	${ethernet_networks} is not ${null}	Add Ethernet Networks from variable	${ethernet_networks}
    ${ethernet_ranges} =	Get Variable Value	${ethernet_ranges}
	Run Keyword If	${ethernet_ranges} is not ${null}		Run Keyword for List	${ethernet_ranges}	Create Ethernet Range
	[Return]

Teardown
    [Documentation]    Common applaince cleanup tasks to run after test case run is complete
	Set Log Level	TRACE
	Log to console	[TEARDOWN]
#	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
#	Power off ALL Servers
#	Remove All Server Profiles
#    Remove All LEs
#	Remove All Logical Enclosures
#	Remove ALL Enclosure Groups
#	Remove ALL LIGs
    Remove All Network Sets
#	Remove ALL Ethernet Networks
#	Remove ALL FCoE Networks
#	Remove ALL Users

OVF565 - Create Bulk Network
    [Documentation]    Creates Ethernet networks in bulk
    ...              Data Required:
    ...                Bulk Network VLANID range

	${resp} = 	Fusion Api Create Ethernet Bulk Networks		${bulk_networks_dict}
	${task} =    Wait For Task     ${resp}     10m
    ${valDict} =     Create Dictionary    status_code=${200}
    ...                                 taskState=Completed
    Validate Response    ${task}    ${valDict}

Verify ErrorCode in taskError
    [Documentation]    Verify taskErrors contain specified errorCode
    [Arguments]    ${taskErrors}    ${expected_errorcode}

    :FOR    ${taskerror}    IN    @{taskErrors}
    \    ${errorCode} =    Get From Dictionary    ${taskError}    errorCode
    \    Exit For Loop If    '${errorCode}' == '${expected_errorcode}'

    Should Be Equal As Strings    ${errorCode}    ${expected_errorcode}

OVF565 Verify Profile Status
    [Documentation]    Verify Profile status is OK or not
	[Arguments]	${numFrames}
	:FOR    ${index}	IN RANGE	1	${numFrames}+1
    \    ${resp}	Fvt Api Get Server Profile By Name	Profile${index}
    \    Should Be Equal As Strings	${resp['status']}	OK

Create Logical Enclosure Dictionary
    [Documentation]    Create LE Dictionary for LE requests
	[Arguments]		${start}	${end}
	${encs} =	Create List
	:FOR    ${index}	IN RANGE	1	${end}+1
	\  	Append to List	${encs}	${Enc_${index}}
	Set To Dictionary	${les}	enclosureUris	${encs}
	[Return]
	
Create Logical Enclosure Grow Dictionary
    [Documentation]    Create LE Dictionary for LE Grow requests
	[Arguments]		${start}	${end}
	${dict} =	Create Dictionary
	${encs} =	Create List
	:FOR    ${index}	IN RANGE	${start}+1	${end}+1
	\  	Append to List	${encs}	${Enc_${index}}
	Set To Dictionary	${dict}	enclosureUris	${encs}
	[Return]	${dict}

OVF565 Grow with Invalid Network Limits
    [Documentation]    Attempt to LE Grow when network limits are invalid for Grow configuration
	[Arguments]		${les}

    ${task}=	fvt-keywords.Edit Logical Enclosure	${les}	15min	1sec
    Sleep	3s
    Verify ErrorCode in taskError  ${task['taskErrors']}    VALIDATE_LE_REPARENT_FAIL

    ${failedsubtasks} =    fusion api get task    param=?filter="parentTaskUri='${task['uri']}'"&filter="taskState ne 'Completed'"
    Sleep	3s
    Verify ErrorCode in taskError  ${failedsubtasks['members'][0]['taskErrors']}    GROW_NETWORK_SET_NETWORK_LIMIT_VIOLATION

	[Return]

##################################
#  Profiles and ping keywords
##################################
Delete Profile With Ping
    [Documentation]    Delete Server Profile that is created with Ping test
	[Arguments]		${profile}
	Log To Console	\n Deleting Profile ${profile} And Ping Process

    # New end to end validation
	Delete Profile With Multiple Ping Sessions    ${profile}

	[Return]

OVF565 Create Server Profiles
    [Documentation]    Create Server Profile
	[Arguments]		${EG}	${start}	${end}
	Log To Console	\n Creating Server Profiles
	:FOR	${x}	IN RANGE	${start}	${end}
	\	Set to Dictionary	${profiles['Profile${x}']['payload']}	enclosureGroupUri	${EG}
	\	FVT Add Server Profile	${profiles['Profile${x}']['payload']}	timeout=20m	interval=1s
	Log To Console	\n Finished Creating Server Profiles
	[Return]

Server Profile Connectivity With Ping
    [Documentation]    Ping Connectivity for a Server Profile
	[Arguments]		${EG}	${start}	${end}    ${timeout}=15m	${interval}=5s

# profile status verification is moved down after Server Power is turned ON
# (Intermettent issue that profile status is Critical and connections are in error if serer is not Powered ON

    # New end to end verification keyword
    # Reads IP addresses through Server iLO address

	:FOR	${x}	IN RANGE	${start}	${end}
	\	Server Profile Connectivity With Ping IP Extension    ${profiles['Profile${x}']}

	Log To Console	\n Finished verifying Server Profile Connectivity With Ping
	[Return]

OVF565 Delete Profile
    [Documentation]    Delete Server Profile
	[Arguments]		${profile}
	Log To Console	\n Deleting Profile ${profile}
 	${task}	Fusion Api Delete Server Profile	name=${profile['name']}	param=?force=true
	Should Be Equal As Integers	${task['status_code']}	202
	${task} =	Wait For Task	${task}	timeout=10m	interval=2s
	[Return]

OVF565 Edit Profile
    [Documentation]    Edit a Server Profile
	[Arguments]	${profile}    ${timeout}=30m    ${interval}=10s   ${endstate}=((?i)Warning|Completed)
    # Edit Profiles
	${resp}	Fvt Api Get Server Hardware By Name	${profile['serverHardwareUri']}
	${uri} =	Set Variable	${resp['uri']}
	${payload} =	Create Dictionary	powerState=Off	powerControl=PressAndHold
	${resp}	Fusion Api Edit Server Hardware Power State	uri=${uri}	body=${payload}
	Should Be Equal As Integers	${resp['status_code']}	202
	${task} =	Wait For Task	${resp} 	${timeout}	${interval}
	${resp}	Fvt Api Get Server Hardware By Name	${profile['serverHardwareUri']}
	Should Be Equal As Strings	${resp['powerState']}	Off

    ${resp} =   server_profile.Edit Server Profile    ${profile}
	${task} =   Wait For Task	${resp}		timeout=${timeout}		interval=${interval}
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ${endstate}

	${resp}	Fvt Api Get Server Profile By Name	${profile['name']}
	Should Be Equal As Strings	${resp['status']}	OK
	[Return]

OVF565 Create Profile Negative
    [Documentation]    Create Profile with invalid network limits
	[Arguments]	${profile}    ${timeout}=15m    ${interval}=10s   ${endstate}=((?i)Error)
    # Create Profiles
    ${resp} =   server_profile.Add Server Profile    ${profile}
	${task} =   Wait For Task	${resp}		timeout=${timeout}		interval=${interval}
    Verify ErrorCode in taskError  ${task['taskErrors']}    MaximumNetworksError
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ${endstate}
	[Return]

OVF565 Edit Profile Negative
    [Documentation]    Edit Profile with invalid network limits
	[Arguments]	${profile}    ${timeout}=15m    ${interval}=10s   ${endstate}=((?i)Error)
	${resp}	Fvt Api Get Server Hardware By Name	${profile['serverHardwareUri']}
	${uri} =	Set Variable	${resp['uri']}
	${payload} =	Create Dictionary	powerState=Off	powerControl=PressAndHold
	${resp}	Fusion Api Edit Server Hardware Power State	uri=${uri}	body=${payload}
	Should Be Equal As Integers	${resp['status_code']}	202
	${task} =	Wait For Task	${resp} 	${timeout}	${interval}
	${resp}	Fvt Api Get Server Hardware By Name	${profile['serverHardwareUri']}
	Should Be Equal As Strings	${resp['powerState']}	Off

    ${resp} =   server_profile.Edit Server Profile    ${profile}
	${task} =   Wait For Task	${resp}		timeout=${timeout}		interval=${interval}
    Verify ErrorCode in taskError  ${task['taskErrors']}    MaximumNetworksError
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ${endstate}
	[Return]

##################################
#  Unassigned Profiles keywords
##################################

OVF565 Edit Profile Unassigned Negative
    [Documentation]    Edit Unassigned Server Profile with invalid network limits
	[Arguments]	${profileUnassigned}    ${timeout}=15m    ${interval}=10s   ${endstate}=((?i)Error)
    # Edit Profiles server_profiles_unassigned
    ${resp} =   server_profile.Edit Server Profile    ${profileUnassigned}
	${task} =   Wait For Task	${resp}		timeout=${timeout}		interval=${interval}
    Verify ErrorCode in taskError  ${task['taskErrors']}    MaximumNetworksError
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ${endstate}
	[Return]

OVF565 Create Profile Unassigned Negative
    [Documentation]    Create Unassigned Server Profile with invalid network limits
	[Arguments]	${profileUnassigned}    ${timeout}=15m    ${interval}=10s   ${endstate}=((?i)Error)
    # Create Profiles server_profiles_unassigned
    ${resp} =   server_profile.Add Server Profile    ${profileUnassigned}
	${task} =   Wait For Task	${resp}		timeout=${timeout}		interval=${interval}
    Verify ErrorCode in taskError  ${task['taskErrors']}    MaximumNetworksError
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ${endstate}
	[Return]

OVF565 Create Profile Unassigned
    [Documentation]    Create Unassigned Server Profile
	[Arguments]	${profileUnassigned}    ${timeout}=15m    ${interval}=10s   ${endstate}=((?i)Warning|Completed)
    # Create Profiles server_profiles_unassigned
    ${resp} =   server_profile.Add Server Profile    ${profileUnassigned}
	${task} =   Wait For Task	${resp}		timeout=${timeout}		interval=${interval}
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ${endstate}
	[Return]

OVF565 Assign Server Hardware To Profile
    [Documentation]    Assign Server Hardware to Unassigned Server Profile
	[Arguments]	${profile}    ${timeout}=20m    ${interval}=10s   ${endstate}=((?i)Warning|Completed)
	${resp}	Fvt Api Get Server Hardware By Name	${profile['serverHardwareUri']}
	${uri} =	Set Variable	${resp['uri']}
	${payload} =	Create Dictionary	powerState=Off	powerControl=PressAndHold
	${resp}	Fusion Api Edit Server Hardware Power State	uri=${uri}	body=${payload}
	Should Be Equal As Integers	${resp['status_code']}	202
	${task} =	Wait For Task	${resp} 	${timeout}	${interval}
	${resp}	Fvt Api Get Server Hardware By Name	${profile['serverHardwareUri']}
	Should Be Equal As Strings	${resp['powerState']}	Off

    ${resp} =   server_profile.Edit Server Profile    ${profile}
	${task} =   Wait For Task	${resp}		timeout=${timeout}		interval=${interval}
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ${endstate}

	${resp}	Fvt Api Get Server Profile By Name	${profile['name']}
	Should Be Equal As Strings	${resp['status']}	OK

	[Return]

###########################################
#  Server Profile Template keywords
###########################################

OVF565 Create Profile Templates
    [Documentation]    Create Server Profile Template
	[Arguments]	${profileTemplate}    ${timeout}=15m    ${interval}=10s   ${endstate}=((?i)Warning|Completed)
    # Create Profile Templates
    ${resp} =   Add Server Profile Template    ${profileTemplate}
	${task} =   Wait For Task	${resp}		timeout=${timeout}		interval=${interval}
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ${endstate}

OVF565 Create Profile from SPT
    [Documentation]    Create Server Profile from Profile Template
	[Arguments]	${profile}    ${timeout}=15m    ${interval}=10s   ${endstate}=((?i)Warning|Completed)
    # Create Profiles server_profiles_unassigned
	${resp}	Fvt Api Get Server Hardware By Name	${profile['serverHardwareUri']}
	${uri} =	Set Variable	${resp['uri']}
	${payload} =	Create Dictionary	powerState=Off	powerControl=PressAndHold
	${resp}	Fusion Api Edit Server Hardware Power State	uri=${uri}	body=${payload}
	Should Be Equal As Integers	${resp['status_code']}	202
	${task} =	Wait For Task	${resp} 	${timeout}	${interval}
	${resp}	Fvt Api Get Server Hardware By Name	${profile['serverHardwareUri']}
	Should Be Equal As Strings	${resp['powerState']}	Off

    ${resp} =   server_profile.Add Server Profile    ${profile}
	${task} =   Wait For Task	${resp}		timeout=${timeout}		interval=${interval}
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ${endstate}
	${resp}	Fvt Api Get Server Profile By Name	${profile['name']}
	Should Be Equal As Strings	${resp['status']}	OK
	[Return]

OVF565 Create Profile Templates Negative
    [Documentation]    Create Server Profile Template with invalid network limits
#   'errorCode': 'MaximumNetworksError',
#   'message': 'Physical port Mezzanine (Mezz) 3:1 cannot support 501 networks requested.The number requested on the connections is [501 from connection 1].',
#   'recommendedActions': ['Place the connections on different physical ports so that the number of networks on each port does not exceed 500.']}],
	[Arguments]	${profileTemplate}    ${timeout}=15m    ${interval}=10s        ${endstate}=((?i)Error)
    # Create Profile Templates
    ${resp} =   Add Server Profile Template    ${profileTemplate}
	${task} =   Wait For Task	${resp}		timeout=${timeout}		interval=${interval}
    Verify ErrorCode in taskError  ${task['taskErrors']}    MaximumNetworksError
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ${endstate}

OVF565 Edit Profile Templates Negative
    [Documentation]    Edit Server Profile Template with invalid network limits
#   'errorCode': 'MaximumNetworksError',
#   'message': 'Physical port Mezzanine (Mezz) 3:1 cannot support 501 networks requested.The number requested on the connections is [501 from connection 1].',
#   'recommendedActions': ['Place the connections on different physical ports so that the number of networks on each port does not exceed 500.']}],
	[Arguments]	${profileTemplate}    ${timeout}=15m    ${interval}=10s        ${endstate}=((?i)Error)
    # Edit Profile Templates
    ${resp} =   Edit Server Profile Template    ${profileTemplate}
	${task} =   Wait For Task	${resp}		timeout=${timeout}		interval=${interval}
    Verify ErrorCode in taskError  ${task['taskErrors']}    MaximumNetworksError
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ${endstate}

OVF565 Remove A Server Profile Template
    [Documentation]	Remove given Server Profile Template
	...                OVF565 Remove A Server Profile Template  ${profile_templates}
	[Arguments]  ${profile_template}
	Log To Console  	\nRemoving Server Profile Template
    ${uri} =  Common URI lookup by name  SPT:${profile_template['name']}
	${task} =  Fusion Api Delete Server Profile Template  uri=${uri}
	Should Be Equal As Integers	${task['status_code']}	202
	${task} =	Wait For Task	${task}	timeout=3m	interval=2s

##################################
# Network set keywords
##################################
OVF565 Edit Network Sets
    [Documentation]    Edit Network sets as per number of Frames allowed limit
	[Arguments]	${numFrames}
    # Edit network set to reduce number of networks depending on frame size ${new_start}
    ${task} =	Edit Network Set	 ${grow_network_sets['Enc${numFrames}_netset']}	timeout=5m	interval=1s
    Should Be Equal As Integers	${task['status_code']}	200

OVF565 Edit Network Set Negative
	[Documentation]	Edit network sets with more than 1000 networks
	[Arguments]		${networkset_in}	    ${expected_errorcode}
	Log to console	\n Editing Network Set ${networkset_in['name']}
	${networkset}	FVT Copy Dictionary	${networkset_in}
	${resp} =	Fvt Api Get Network Set By Name	${networkset['name']}
	Set To Dictionary	${networkset}	connectionTemplateUri	${resp['connectionTemplateUri']}
	${networkUris} =	Get Ethernet Network Uris	${networkset['networkUris']}
	Set To Dictionary	${networkset}	networkUris	${networkUris}
	${native} =	Get Variable Value	${networkset['nativeNetworkUri']}
	${resp} =	Run Keyword If	'${native}' != 'None'	FVT Api Get Ethernet Network By Name	${native}
	Run Keyword If	'${native}' != 'None'	Set To Dictionary	${networkset}	nativeNetworkUri	${resp['uri']}
	${resp} =	Fvt Api Get Network Set By Name	${networkset['name']}
	${resp} =	Fusion Api Edit Network Set	body=${networkset}	uri=${resp['uri']}
    Should Be Equal As Integers    ${resp['status_code']}    ${400}
    Should Be Equal As Strings    ${resp['errorCode']}    ${expected_errorcode}
	[Return]

OVF565 Create Network Sets
    [Documentation]    Create network sets with 1000 networks
# 3.2.1	Network set can be created with 1000 networks.
# Expected result: Network sets can be successfully created upto 1000 VLANs.
	${network_sets} =	Get Variable Value	${network_sets}
	Run Keyword If	${network_sets} is not ${null}	Add Network Sets from variable		${network_sets}

OVF565 Create Network Sets Negative
    [Documentation]    Network set cannot be created with more than 1000 networks
    # 3.2.2	Network set can not be created with more than 1000 networks.
    # Expected result: Error message with resolution to create network set with Max 1000 networks.
    # 'CRM_DOMAIN_NETWORK_SET_LIMIT_EXCEEDED'

    Log to console    ${\n}Network sets negative tests
	:FOR	${net}	IN	@{neg_network_sets}
	\		${networkUris} = 	Get Ethernet URIs	${net['networkUris']}
	\		Set to dictionary	${net}	networkUris	${networkUris}
	\		${nativeNetworkUri} = 	Run Keyword If 	'${net['nativeNetworkUri']}' != 'None'		Get Ethernet URI	${net['nativeNetworkUri']}
	\		Set To Dictionary 	${net}	nativeNetworkUri	${nativeNetworkUri}
	\		${resp} = 	Fusion Api Create Network Set		body=${net}
    \	    Should Be Equal As Integers    ${resp['status_code']}    ${400}
    \	    Should Be Equal As Strings    ${resp['errorCode']}    CRM_DOMAIN_NETWORK_SET_LIMIT_EXCEEDED

Setup Grow Variables
    [Documentation]    Setup variables for Grow test cases
    [Tags]  SETUP
	#Pass Execution	Skip Create Logical Enclosure
	Set Suite Variable	${LIG}	Enc${start}-LIG
	Set Suite Variable	${EG}	Enc${start}-EG
	Set Suite Variable	${LI}	${LE}-Enc${start}-LIG

*** Test Cases ***
OVF565 Network Sets Test Cases
    [Documentation]    Test cases for Network sets limits
    [Tags]  TCNS
    Test Specific Setup
    OVF565 - Create Bulk Network
    OVF565 Create Network Sets
    OVF565 Create Network Sets Negative
    OVF565 Edit Network Set Negative    ${neg_grow_network_sets['Enc${start}_netset']}    CRM_DOMAIN_NETWORK_SET_LIMIT_EXCEEDED
	Pass Execution	Finished Network sets Test Cases

Create Logical Enclosure
    [Documentation]    Create LIG, EG and LE
    [Tags]  TCC
	#Pass Execution	Skip Create Logical Enclosure
	Set Suite Variable	${LIG}	Enc${start}-LIG
	Add Logical Interconnect Group	${ligs['${LIG}']}	timeout=4m	interval=1s
	Set Suite Variable	${EG}	Enc${start}-EG
	FVT Add Enclosure Group		${enc_group['${EG}']}
	Create Logical Enclosure Dictionary	${start}	${start}
	Set To Dictionary	${les}	enclosureGroupUri	${EG}
	Add Logical Enclosure	${les}	timeout=90m	interval=1m
	Sleep	3 mins
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['state']}	Consistent
	Set Suite Variable	${LI}	${LE}-Enc${start}-LIG	
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	FVT Verify Interconnects	Enc${start}Map
	Pass Execution	Finished Create Logical Enclosure

OVF565 Server Profile Template Test Cases
    [Documentation]    Server Profile Template test cases with network limits
    [Tags]  SPT
    OVF565 Create Profile Templates Negative   ${neg_server_profile_templates['Enc${start}_sptemplate']}
    OVF565 Create Profile Templates    ${server_profile_templates['Enc${start}_sptemplate']}
    OVF565 Edit Profile Templates Negative   ${neg_server_profile_templates['Enc${start}_sptemplate']}
    OVF565 Create Profile from SPT    ${server_profiles_SPT['Enc${start}_sp_spt']}
    OVF565 Edit Network Set Negative    ${neg_grow_network_sets['Enc${start}_netset']}    CRM_DOMAIN_NETWORK_SET_LIMIT_EXCEEDED
    OVF565 Delete Profile    ${server_profiles_SPT['Enc${start}_sp_spt']}
    Sleep	5 mins
    OVF565 Remove A Server Profile Template    ${server_profile_templates['Enc${start}_sptemplate']}
	Pass Execution	Finished Server Profile Template test cases

OVF565 Unassigned Server Profile Test Cases
    [Documentation]    Unassigned Server Profile test cases with network limits
    [Tags]  SPUN
	OVF565 Create Profile Unassigned Negative    ${neg_server_profiles_unassigned['Enc${start}_sp_unassigned']}
	OVF565 Create Profile Unassigned    ${server_profiles_unassigned['Enc${start}_sp_unassigned']}
	OVF565 Edit Profile Unassigned Negative     ${neg_server_profiles_unassigned['Enc${start}_sp_unassigned']}
    OVF565 Assign Server Hardware To Profile    ${server_profiles_HW['Enc${start}_sp_unassigned']}
    OVF565 Edit Network Set Negative    ${neg_grow_network_sets['Enc${start}_netset']}    CRM_DOMAIN_NETWORK_SET_LIMIT_EXCEEDED
    OVF565 Delete Profile    ${server_profiles_HW['Enc${start}_sp_unassigned']}
	Sleep	5 mins
	Pass Execution	Finished Unassigned Server Profile test cases

OVF565 Server Profile Test Cases
    [Documentation]    Server Profile test cases with network limits
    [Tags]  SP
    OVF565 Create Profile Negative    ${neg_server_profiles['Profile${start}']}
    OVF565 Create Server Profiles	${EG}	1	${start}+1
    Sleep	3 mins
    OVF565 Edit Profile Negative     ${neg_server_profiles['Profile${start}']}
    OVF565 Edit Network Set Negative    ${neg_grow_network_sets['Enc${start}_netset']}    CRM_DOMAIN_NETWORK_SET_LIMIT_EXCEEDED
    Server Profile Connectivity With Ping	${EG}	1	${start}+1
    OVF565 Verify Profile Status     ${start}
	Pass Execution	Finished Server Profile test cases

Grow Logical Enclosure
    [Documentation]    Grow Logical Enclosure with network limits test cases
    [Tags]  TCG    GROW
    #Pass Execution	Skip Grow Ligical Enclosure
	:For	${index}	IN RANGE	${start}+${inc}	${max_frame}+1	${inc}
	\	${new_start} =	Evaluate	${start} + ${inc}
	\	Log	\n Grow From ${start} Enclosure To ${new_start} Enclosure For ${CXP} in ${CONFIG} Configuration	console=True
	\	Set Suite Variable	${LIG}	Enc${new_start}-LIG
	\	Set Suite Variable	${EG}	Enc${new_start}-EG
	\	Add Logical Interconnect Group	${ligs['${LIG}']}	timeout=10m	interval=1s
	\	FVT Add Enclosure Group		${enc_group['${EG}']}
	\	Create Logical Enclosure Dictionary	1	${start}
	\	Set To Dictionary	${les}	enclosureGroupUri	Enc${new_start}-EG
	\	OVF565 Grow with Invalid Network Limits    ${les}
	\	Sleep	3 mins
	\	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
    \   # Edit network set to reduce number of networks depending on frame size ${new_start}
    \   OVF565 Edit Network Sets    ${new_start}
	\	fvt-keywords.Edit Logical Enclosure	${les}	20min	1sec
	\	Sleep	3 mins
	\	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	\	Should Be Equal As Strings	${resp['state']}	Inconsistent
	\	Pause Execution		### Waiting for cabling
	\	${dict} =	Create Logical Enclosure Grow Dictionary	${start}	${new_start}
	\	${resp}=	Update From Group On Logical Enclosure	${resp['uri']}	${dict}	timeout=60 m	interval=5 s
	\	Sleep	3s
	\	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	\	Should Be Equal As Strings	${resp['state']}	Consistent
	\	Set Suite Variable	${LI}	${LE}-${LIG}	
	\	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	\	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	\	FVT Verify Interconnects	Enc${new_start}Map
	\	OVF565 Create Profile Templates Negative   ${neg_server_profile_templates['Enc${new_start}_sptemplate']}
	\	OVF565 Create Profile Templates    ${server_profile_templates['Enc${new_start}_sptemplate']}
	\	OVF565 Edit Profile Templates Negative   ${neg_server_profile_templates['Enc${new_start}_sptemplate']}
	\	OVF565 Create Profile from SPT    ${server_profiles_SPT['Enc${new_start}_sp_spt']}
	\	OVF565 Delete Profile    ${server_profiles_SPT['Enc${new_start}_sp_spt']}
	\	Sleep	5 mins
	\   OVF565 Remove A Server Profile Template    ${server_profile_templates['Enc${new_start}_sptemplate']}
	\	OVF565 Create Profile Unassigned Negative    ${neg_server_profiles_unassigned['Enc${new_start}_sp_unassigned']}
	\	OVF565 Create Profile Unassigned    ${server_profiles_unassigned['Enc${new_start}_sp_unassigned']}
	\	OVF565 Edit Profile Unassigned Negative     ${neg_server_profiles_unassigned['Enc${new_start}_sp_unassigned']}
	\	OVF565 Assign Server Hardware To Profile    ${server_profiles_HW['Enc${new_start}_sp_unassigned']}
	\	Sleep	3 mins
	\	OVF565 Delete Profile    ${server_profiles_HW['Enc${new_start}_sp_unassigned']}
	\	Sleep	5 mins
	\	OVF565 Create Profile Negative    ${neg_server_profiles['Profile${new_start}']}
	\	OVF565 Create Server Profiles	${EG}	${start}+1	${new_start}+1
	\   Sleep	3 mins
	\	OVF565 Edit Profile Negative     ${neg_server_profiles['Profile${new_start}']}
	\   OVF565 Edit Network Set Negative    ${neg_grow_network_sets['Enc${new_start}_netset']}    CRM_NETWORK_SET_MAX_VLANS_DOWNLINK_PORT_VIOLATION
	\   Server Profile Connectivity With Ping	${EG}	${start}+1	${new_start}+1
	\   OVF565 Verify Profile Status     ${new_start}
	\	Sleep	2 mins
	\	${resp}	Fvt Api Get Logical Interconnect BY Name	${LE}-Enc${start}-LIG
	\	Should Be Equal As Strings	${resp}	None	### Ensure Old LI Deleted
	\	FVT Delete Enclosure Group	Enc${start}-EG
	\	${resp}	Fvt Api Get Enclosure Group BY Name	Enc${start}-EG
	\	Should Be Equal As Strings	${resp}	None	### Ensure Old EG Deleted
	\	FVT Delete Logical Interconnect Group	Enc${start}-LIG
	\	${resp}	Fvt Api Get Logical Interconnect Group BY Name	Enc${start}-LIG
	\	Should Be Equal As Strings	${resp}	None	### Ensure Old LIG Deleted
	\	${start} =	Set Variable	${new_start}
	\   Set Suite Variable	${profileCount}	${new_start}

OVF565 Verify Server Profile Ping sessions
    [Documentation]    OVF565 Profile End to End Validation
    [Tags]  PINGCHECK

	Sleep	3 mins

#   ${profiles['Profile${x}']}
    :FOR    ${x}   IN RANGE	1	${profileCount}+1
	\	${resp}	Fvt Api Get Server Profile By Name	${profiles['Profile${x}']['payload']['name']}
	\	Run Keyword If	${resp} != None	Delete Profile With Ping	${profiles['Profile${x}']}
    Pause Execution		### Make sure ready for Teardown

Teardown Grow Rig
    [Documentation]    Cleanup appliance after network limits test cases
    [Tags]  TDOWN
    # No profiles or profile templates at this point
    Power off ALL servers    control=PressAndHold
    Sleep	8 mins
    Remove All Server Profiles
	Sleep	3 mins
	Fvt Delete Logical Enclosure	${LE}
	${resp}	FVT Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp}	None
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	Should Be Equal As Strings	${resp}	None
	FVT Delete Enclosure Group	${EG}
	${resp}	Fvt Api Get Enclosure Group BY Name	${EG}
	Should Be Equal As Strings	${resp}	None	### Ensure Old EG Deleted
	FVT Delete Logical Interconnect Group	${LIG}
	${resp}	Fvt Api Get Logical Interconnect Group BY Name	${LIG}
	Should Be Equal As Strings	${resp}	None	### Ensure Old LIG Deleted
    # cleanup remaining network sets, networks etc
    Teardown
	Pass Execution	Finished Teardown of the Grow rig configuration

