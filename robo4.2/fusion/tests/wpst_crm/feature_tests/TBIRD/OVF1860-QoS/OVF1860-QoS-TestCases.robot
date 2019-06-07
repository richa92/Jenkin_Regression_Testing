*** Settings ***
Documentation		OVF1860 QoS
...                 SuiteName: OVF1860-QoS-TestCases

...					Usage (Rack AS51 Single Frame Redundant configuration):
...					Note: Make sure Server Hardware Type matching to data file
...					E.g. SHT:SY 480 Gen9 1 or SHT:SY 480 Gen9 2 etc.
...					pybot -d logs -T -V data_QoS.py -v APPLIANCE_IP:15.245.131.222 OVF1860-QoS-TestCases.robot

Variables		data_QoS.py

Resource            ../../../../../Resources/api/fusion_api_resource.txt
#Resource            ../FVT/fvt-keywords.txt
#Resource			../FVT/Resources/fvt_resource.txt

Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary
Library			Collections
Library			SSHLibrary
Library			String
Library			Process
Library			../FVT/fvt_api.py

Suite Setup			Login User
Suite Teardown	Suite Teardown

# Setup\Teardown for ALL test cases
Test Setup       Common Test Setup
Test Teardown    Common Test Teardown

*** Variables ***
${APPLIANCE_IP}		15.245.131.222
${numFrames}    1
${PAUSE}    1
#${PAUSE}    0
${TRUE}    1
${bay3}               3
${efuse_sleeptime}    120
${sleeptime_potashAdd}    2400
${enc1_bay3_icm}	${ENC_1}, interconnect 3
${enc1_bay6_icm}	${ENC_1}, interconnect 6
${FUSION_IP}					${APPLIANCE_IP}
${SKIPTEARDOWN}                 ${True}

*** Test Cases ***

QoS Create LE with QoS with FCoE lossless
    [Tags]  LEwithFCoE
    [Documentation]    Networks, LIG, EG and LE setup for QoS test cases

    # Test Specific Setup creates networks and users from F108 COMMON keywords
    Test Specific Setup

    # create LIG
    Log to console	\n Creating LIG
	Set Suite Variable	${LIG}	Enc${numFrames}-LIG

    ${body} =    Build LIG body    ${ligs_noUplinkSets['Enc${numFrames}-LIG']}
	${qosConfiguration} =   Get From Dictionary   ${QoS_Fcoe}  qosConfiguration
	Set to dictionary	${body}     qosConfiguration    ${qosConfiguration}
	log to console		replaced body is:${body}
    ${resp} =    Fusion Api Create LIG    ${body}
    ${task} =    Wait For Task    ${resp}    300s    2s
    ${resp}	Fvt Api Get Logical Interconnect Group By Name	${ligs_noUplinkSets['Enc${numFrames}-LIG']['name']}
    Should Be Equal As Strings	${resp['name']}	${ligs_noUplinkSets['Enc${numFrames}-LIG']['name']}
    verify LIG QoS values   ${ligs_noUplinkSets['Enc${numFrames}-LIG']}    ${QoS_Fcoe['qosConfiguration']}

    Log to console	\n Creating EG
	Set Suite Variable	${EG}	Enc${numFrames}-EG
	${Resp} =	Add Enclosure Group from variable		${enc_group['Enc${numFrames}-EG']}
	Run Keyword If  '${Resp['status_code']}' != '201'  Fail    ELSE  log to console   \n-created EG successfully

    Log to console	\n Creating LE
	Set Suite Variable	${EG}	Enc${numFrames}-EG
	Set Suite Variable	${LE}	${les['QoS-LE${numFrames}']}
	${Resp} =	Add Logical Enclosure from variable     ${les['QoS-LE${numFrames}']}
#	Run Keyword If  '${Resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-created LE successfully

	#verify LI and LE consistency status values
	Sleep	3 sec
	Set Suite Variable	${LE}	${les['QoS-LE${numFrames}']['name']}
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['state']}	Consistent

	Set Suite Variable	${LI}	${LE}-Enc${numFrames}-LIG
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT

    verify LI QoS values    ${QoS_Fcoe['qosConfiguration']}

    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    QoS Created LE with QoS with FCoE lossless
	Log To Console	\n Finished Creating LE with QoS with FCoE lossless

QoS Create Server Profiles without Connections
	Log To Console	\n Creating Server Profiles for Bay5 and Bay8 Linux servers

    # create profile 3 and 4 from the Dictionary
	:FOR	${x}	IN RANGE	3	5
	\	${resp} =   server_profile.Add Server Profile    ${profiles_noConns['Profile${x}']['payload']}
	\	${task} =   Wait For Task	${resp}		timeout=20m		interval=5s
	\	${task_state} = 	Get From dictionary 	${task}     taskState
	\	Should Match Regexp	${task_state}	 ((?i)Warning|Completed)
	\	${resp}	Fvt Api Get Server Profile By Name	${profiles_noConns['Profile${x}']['payload']['name']}
	\	Should Be Equal As Strings	${resp['status']}	OK

    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    QoS Created Profile3 and Profile4
	Log To Console	\n Finished Creating Server Profiles 3 and 4

QoS Add uplink set
#Configure QoS. Add an uplink set and verify QoS configuration.
	Log To Console	\n Add an uplink set and verify QoS configuration
	#edit LIG to add uplink set
    ${body} =    Build LIG body    ${edit_ligs['Enc${numFrames}-LIG-AddUplinkset']['ligBody']}
	${uri} =	Get LIG Uri   ${edit_ligs['Enc${numFrames}-LIG-AddUplinkset']['ligBody']['name']}
    ${resp} =    Fusion Api Edit LIG    ${body}    ${uri}
    ${task} =    Wait For Task    ${resp}    300s    2s
    ${resp}	Fvt Api Get Logical Interconnect Group By Name	${edit_ligs['Enc${numFrames}-LIG-AddUplinkset']['ligBody']['name']}
    Should Be Equal As Strings	${resp['name']}	${edit_ligs['Enc${numFrames}-LIG-AddUplinkset']['ligBody']['name']}

	# LE update from roup
	${Resp} =	Update Logical Enclosure from Group     ${les['QoS-LE${numFrames}']}

	#verify LI and LE consistency status values
	Sleep	3 sec
	Set Suite Variable	${LE}	${les['QoS-LE${numFrames}']['name']}
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['state']}	Consistent

	Set Suite Variable	${LI}	${LE}-Enc${numFrames}-LIG
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT

    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    QoS Add uplink set
	Log To Console	\n Finished Adding  uplink sets

QoS Create Server Profiles when QoS is configured
	Log To Console	\n Creating Server Profiles for Bay3 and Bay4 Linux servers

    # create Profile 3 and 4 profiles from the Dictionary
	:FOR	${x}	IN RANGE	1	3
	\	${resp} =   server_profile.Add Server Profile    ${profiles['Profile${x}']['payload']}
	\	${task} =   Wait For Task	${resp}		timeout=20m		interval=5s
	\	${task_state} = 	Get From dictionary 	${task}     taskState
	\	Should Match Regexp	${task_state}	 ((?i)Warning|Completed)
	\	${resp}	Fvt Api Get Server Profile By Name	${profiles['Profile${x}']['payload']['name']}
	\	Should Be Equal As Strings	${resp['status']}	OK

    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    QoS Created Profile1 and Profile2 for Bays 3 and 4
	Log To Console	\n Finished Creating Profile1 and Profile2 for Bay 3 and 4 servers

QoS Edit Profile to add Profile connections
#Create server profile with QoS configured. Add another profile connection and verify QoS configuration
	Log To Console	\n Edit Profile to add a server profile connection and verify QoS configuration

    #edit Bay 4 (Profile2) profile to add a B side close connection
    Edit Profile    ${edit_profiles['Profile3']['payload']}

    #edit Bay 4 (Profile2) profile to add a B side close connection
    Edit Profile    ${edit_profiles['Profile4']['payload']}

    # Power ON ALL servers (Bay3, Bay4, Bay5 and Bay8)
    Run Keyword for List	${servers}	Power on Server
   	Log     Waiting 5 more minutes for servers to boot... (Keyword waits 4 minutes)- should not have to do this!    WARN
    Sleep	5 min

    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    Qos with Add profile connections
	Log To Console	\n Finished Edit Profile to add a server profile connection and verifying QoS configuration

QoS Edit an existing uplink set
#Configure QoS. Edit an existing uplink set (add/remove additional ports) and verify QoS configuration
	Log To Console	\n Edit an uplink set and verify QoS configuration

	#edit LIG to add uplink set
    ${body} =    Build LIG body    ${edit_ligs['Enc${numFrames}-LIG-EditUplinkset']['ligBody']}
	${uri} =	Get LIG Uri   ${edit_ligs['Enc${numFrames}-LIG-EditUplinkset']['ligBody']['name']}
    ${resp} =    Fusion Api Edit LIG    ${body}    ${uri}
    ${task} =    Wait For Task    ${resp}    300s    2s
    ${resp}	Fvt Api Get Logical Interconnect Group By Name	${edit_ligs['Enc${numFrames}-LIG-EditUplinkset']['ligBody']['name']}
    Should Be Equal As Strings	${resp['name']}	${edit_ligs['Enc${numFrames}-LIG-EditUplinkset']['ligBody']['name']}

	# Edit LI uplinkset
#	${Resp} =	Update Logical Enclosure from Group     ${les['QoS-LE${numFrames}']}
	Set Suite Variable	${LE}	${les['QoS-LE${numFrames}']['name']}
	Set Suite Variable	${LI}	${LE}-Enc${numFrames}-LIG

	${us} = 		Copy Dictionary	${li_edit_uplinkset['us-fcoe-enet-Aside']}
	${resp} =	Edit uplinkset    us-fcoe-enet-Aside    ${us}    ${LI}
    ${task} =    Wait For Task    ${resp}    300s    2s

	#verify LI and LE consistency status values
	Sleep	3 sec
	Set Suite Variable	${LE}	${les['QoS-LE${numFrames}']['name']}
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['state']}	Consistent

	Set Suite Variable	${LI}	${LE}-Enc${numFrames}-LIG
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT

	#verify QoS values
    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    QoS after editing an existing uplink set
	Log To Console	\n Finished Editing an uplink set test case

QoS Delete an uplink set
#Configure QoS. Delete an uplink set and all uplink sets and verify QoS configuration
	Log To Console	\n Add an uplink set and verify QoS configuration
	#edit LIG to delete an uplink set
    ${body} =    Build LIG body    ${edit_ligs['Enc${numFrames}-LIG-AddUplinkset']['ligBody']}
	${uri} =	Get LIG Uri   ${edit_ligs['Enc${numFrames}-LIG-AddUplinkset']['ligBody']['name']}
    ${resp} =    Fusion Api Edit LIG    ${body}    ${uri}
    ${task} =    Wait For Task    ${resp}    300s    2s
    ${resp}	Fvt Api Get Logical Interconnect Group By Name	${edit_ligs['Enc${numFrames}-LIG-AddUplinkset']['ligBody']['name']}
    Should Be Equal As Strings	${resp['name']}	${edit_ligs['Enc${numFrames}-LIG-AddUplinkset']['ligBody']['name']}

	# LE update from roup
	${Resp} =	Update Logical Enclosure from Group     ${les['QoS-LE${numFrames}']}

	#verify LI and LE consistency status values
	Sleep	3 sec
	Set Suite Variable	${LE}	${les['QoS-LE${numFrames}']['name']}
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['state']}	Consistent

	Set Suite Variable	${LI}	${LE}-Enc${numFrames}-LIG
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT

    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    QoS after deleting previously added uplink set
	Log To Console	\n Finished Adding an uplink set

QoS Delete a server profile connection
#Create server profile with QoS configured. Delete a server profile connection and verify QoS configuration
	Log To Console	\n Delete a server profile connection and verify QoS configuration

    #edit Bay 4 (Profile2) profile to delete previously added B side connection
    Edit Profile    ${edit_profiles['Profile2_deleteConn']['payload']}

    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    Qos with Delete profile connection
	Log To Console	\n Finished deleting server profile connection and verifying QoS configuration

QoS Edit profile connection FCoE bandwidth and Ethernet networks
#Create server profile with QoS configured. Edit profile connection and verify QoS configuration
	Log To Console	\n Edit a server profile connection and verify QoS configuration

    # FCOE Bandwidth change to 4Gbps from 2.5Gbps; Networks change from netset to net_401, net_403 and net_404
    #edit Bay 4 (Profile2) profile to add a B side connection
    Edit Profile    ${edit_profiles['Profile1_editConn']['payload']}

    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    Qos with Edit profile connection
	Log To Console	\n Finished Editing a server profile connection and verifying QoS configuration

QoS Reboot ICM
#Configure QoS. ICM life cycle actions (Power reboot, efuse…) and verify QoS configuration
	Log To Console	\n Reboot Potash ICM and verify QoS configuration

    # CN754406W6, interconnect 3
    ${uri} =    Get IC URI      ${ENC_1}, interconnect 3

#    Power Off and On Interconnect

    Power request    ${uri}   Off
	Log    \t Waiting for ${uri} to reach state:Maintenance    console=True
    Wait Until Keyword Succeeds     30 min   30s      IC reached state    ${uri}    Maintenance

    Power request    ${uri}   On
	Log    \t Waiting for ${uri} to reach state:Configured    console=True
    Wait Until Keyword Succeeds     30 min   30s      IC reached state    ${uri}    Configured

    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    Qos with ICM Power OFF and ON
	Log To Console	\n Finished rebooting Potash ICM and verifying QoS configuration

QoS RipAndRepalce ICM
    [Documentation]    Remove Potash ICM from a HA LI
    #Configure QoS. ICM life cycle actions (Power reboot, efuse…) and verify QoS configuration
	Log To Console	\n Remove and add Potash ICM and verify QoS configuration

    # CN754406W6, interconnect 3
    ${uri} =    Get IC URI      ${ENC_1}, interconnect 3

    # Remove Potash from Enclosure 1 bay 3 which is part of Redundant LI
    Get EM IP      ${ENC_1}
    Get EM Token    ${ENC_1}
    Efuse ICM   EFuseOn     ${bay3}

	Log    \t Waiting for ${uri} to reach state:Absent    console=True
    Wait Until Keyword Succeeds     3 min   30s      IC reached state    ${uri}    Absent

    Efuse ICM   EFuseOff     ${bay3}
	Log    \t Waiting for ${uri} to reach state:Configured    console=True
    Wait Until Keyword Succeeds     40 min   30s      IC reached state    ${uri}    Configured

    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    Qos with Rip and Replace of ICM
	Log To Console	\n Finished removing and adding Potash ICM and verifying QoS configuration

QoS Reapply ICM configuration
#Reapply configuration and verify QoS configuration
	Log To Console	\n Reaaply Potash ICM configuration and verify QoS configuration

    # CN754406W6, interconnect 3
    ${icmuri} =    Get IC URI      ${ENC_1}, interconnect 3

	${resp} =   Fusion Api Reapply Interconnect Configuration    ${icmuri}
    ${task} =   Wait For Task	${resp}		timeout=20m		interval=5s
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ((?i)Warning|Completed)

    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    QoS after ICM Reapply configuration
	Log To Console	\n Finished reapplying Potash ICM configuration and verifying QoS configuration

QoS Update from group to QoS without FCoE
# QoS Enable QoS without FCoE
# Configure QoS. Update from group with QoS changes; Verify ICM state
	Log To Console	\n Make QoS changes without FCoE and verify QoS configuration

    # Edit 4 profiles to remove FCoE connections
	:FOR	${x}	IN RANGE	1	5
	\   Edit Profile    ${edit_profiles_noFCoE['Profile${x}']['payload']}
	\	${resp}	Fvt Api Get Server Profile By Name	${edit_profiles_noFCoE['Profile${x}']['payload']['name']}
	\	Should Be Equal As Strings	${resp['status']}	OK

	#edit LIG to enable QoS without FCoE lossless (Enc1-LIG-QoSwithoutFCoE)
    ${body} =    Build LIG body    ${edit_ligs['Enc${numFrames}-LIG-QoSwithoutFCoE']['ligBody']}
	${qosConfiguration} =   Get From Dictionary   ${QoS_NoFcoe}  qosConfiguration
	Set to dictionary	${body}     qosConfiguration    ${qosConfiguration}
	log to console		replaced body is:${body}

	${uri} =	Get LIG Uri   ${edit_ligs['Enc${numFrames}-LIG-QoSwithoutFCoE']['ligBody']['name']}
    ${resp} =    Fusion Api Edit LIG    ${body}    ${uri}
    ${task} =    Wait For Task    ${resp}    300s    2s
    ${resp}	Fvt Api Get Logical Interconnect Group By Name	${edit_ligs['Enc${numFrames}-LIG-QoSwithoutFCoE']['ligBody']['name']}
    Should Be Equal As Strings	${resp['name']}	${edit_ligs['Enc${numFrames}-LIG-QoSwithoutFCoE']['ligBody']['name']}

	# LE update from roup
	${Resp} =	Update Logical Enclosure from Group     ${les['QoS-LE${numFrames}']}

	#verify LI and LE consistency status values
	Sleep	3 sec
	Set Suite Variable	${LE}	${les['QoS-LE${numFrames}']['name']}
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['state']}	Consistent

	Set Suite Variable	${LI}	${LE}-Enc${numFrames}-LIG
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT

    verify LIG QoS values   ${ligs['Enc${numFrames}-LIG']}    ${QoS_NoFcoe['qosConfiguration']}
    verify LI QoS values    ${QoS_NoFcoe['qosConfiguration']}
    Verify Server Profile status

    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    Qos Update from group to without FCoE lossless
	Log To Console	\n Finished QoS changes and verifying QoS configuration

QoS Create LE with QoS Passthrough
    [Tags]  LEwithFCoE
    [Documentation]    Networks, LIG, EG and LE setup for QoS test cases

    # remove previous confifuration to recreate LE with Passthrough configuration
    Power off all servers
    Remove All Server Profiles
    Remove All LEs

    # create LIG
    Log to console	\n Creating LIG
	Set Suite Variable	${LIG}	Enc${numFrames}-LIG

    ${body} =    Build LIG body    ${ligs['Enc${numFrames}-LIG']}
    ${resp} =    Fusion Api Create LIG    ${body}
    ${task} =    Wait For Task    ${resp}    300s    2s
    ${resp}	Fvt Api Get Logical Interconnect Group By Name	${ligs_noUplinkSets['Enc${numFrames}-LIG']['name']}
    Should Be Equal As Strings	${resp['name']}	${ligs['Enc${numFrames}-LIG']['name']}
    verify LIG QoS values   ${ligs['Enc${numFrames}-LIG']}    ${QoS_Fcoe['qosConfiguration']}

    Log to console	\n Creating EG
	Set Suite Variable	${EG}	Enc${numFrames}-EG
	${Resp} =	Add Enclosure Group from variable		${enc_group['Enc${numFrames}-EG']}
	Run Keyword If  '${Resp['status_code']}' != '201'  Fail    ELSE  log to console   \n-created EG successfully

    Log to console	\n Creating LE
	Set Suite Variable	${EG}	Enc${numFrames}-EG
	Set Suite Variable	${LE}	${les['QoS-LE${numFrames}']}
	${Resp} =	Add Logical Enclosure from variable     ${les['QoS-LE${numFrames}']}
#	Run Keyword If  '${Resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-created LE successfully

	#verify LI and LE consistency status values
	Sleep	3 sec
	Set Suite Variable	${LE}	${les['QoS-LE${numFrames}']['name']}
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['state']}	Consistent

	Set Suite Variable	${LI}	${LE}-Enc${numFrames}-LIG
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT

    verify LI QoS values    ${QoS_Fcoe['qosConfiguration']}

QoS Create Server Profiles with QoS Passthrough
	Log To Console	\n Creating Server Profiles for 4 Linux servers

    # create 4 profiles from the Dictionary
	:FOR	${x}	IN RANGE	1	5
	\	${resp} =   server_profile.Add Server Profile    ${profiles['Profile${x}']['payload']}
	\	${task} =   Wait For Task	${resp}		timeout=20m		interval=5s
	\	${task_state} = 	Get From dictionary 	${task}     taskState
	\	Should Match Regexp	${task_state}	 ((?i)Warning|Completed)
	\	${resp}	Fvt Api Get Server Profile By Name	${profiles['Profile${x}']['payload']['name']}
	\	Should Be Equal As Strings	${resp['status']}	OK

    # Power ON servers
    Run Keyword for List	${servers}	Power on Server
   	Log     Waiting 5 more minutes for servers to boot... (Keyword waits 4 minutes)- should not have to do this!    WARN
    Sleep	5 min

	Log To Console	\n Finished Creating Server Profiles

QoS Enable QoS with FCoE
#Configure QoS. Update from group with QoS changes; Verify ICM state
	Log To Console	\n Make QoS changes and verify QoS configuration

	#edit LIG to enable QoS with FCoE
    ${body} =    Build LIG body    ${edit_ligs['Enc${numFrames}-LIG-QoSwithFCoE']['ligBody']}
	${qosConfiguration} =   Get From Dictionary   ${QoS_Fcoe}  qosConfiguration
	Set to dictionary	${body}     qosConfiguration    ${qosConfiguration}
	log to console		replaced body is:${body}

	${uri} =	Get LIG Uri   ${edit_ligs['Enc${numFrames}-LIG-QoSwithFCoE']['ligBody']['name']}
    ${resp} =    Fusion Api Edit LIG    ${body}    ${uri}
    ${task} =    Wait For Task    ${resp}    300s    2s
    ${resp}	Fvt Api Get Logical Interconnect Group By Name	${edit_ligs['Enc${numFrames}-LIG-QoSwithFCoE']['ligBody']['name']}
    Should Be Equal As Strings	${resp['name']}	${edit_ligs['Enc${numFrames}-LIG-QoSwithFCoE']['ligBody']['name']}

	# LE update from roup
	${Resp} =	Update Logical Enclosure from Group     ${les['QoS-LE${numFrames}']}

	#verify LI and LE consistency status values
	Sleep	3 sec
	Set Suite Variable	${LE}	${les['QoS-LE${numFrames}']['name']}
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['state']}	Consistent

	Set Suite Variable	${LI}	${LE}-Enc${numFrames}-LIG
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT

    verify LIG QoS values   ${ligs['Enc${numFrames}-LIG']}    ${QoS_Fcoe['qosConfiguration']}
    verify LI QoS values    ${QoS_Fcoe['qosConfiguration']}
    Verify Server Profile status

    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    Qos Enabled QoS with FCoE.
	Log To Console	\n Finished QoS changes and verifying QoS configuration

# Manual test case
#QoS Upgrade OneView
##Configure End to End on prior version os OV. Upgrade to new OV version. Verify QoS configuration is retained as is.
#	Log To Console	\n Upgrade OneView and verify QoS configuration
#    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    Qos with OneView Appliance upgrade
#	Log To Console	\n Finished upgrading OneView and verifying QoS configuration

***Keywords***
Login User
    [Documentation]    Common login and setting variables keyword for test cases
	Set Log Level	TRACE
	Fusion Api Login Appliance	${appliance_ip}	${admin_credentials}
#	Set Suite Variable	${LIG}	Enc${frame}-LIG
#	Set Suite Variable	${EG}	Enc${frame}-EG
#	Set Suite Variable	${LE}	Enc${frame}-LE
#	Set Suite Variable	${LI}	${LE}-${LIG}
	[Return]

Common Test Setup
    [Documentation]    Pre-conditions for ALL test cases
    Set Log Level    TRACE
#    Run Keyword and Ignore Error    Write To ciDebug Log
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

Common Test Teardown
    [Documentation]    Post-conditions for ALL test cases
    fusion api logout appliance
#    Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

Test Specific Setup
    [Documentation]    QoS Test specififc setup users, networks and network sets etc.
	Set Log Level	TRACE
	Run Keyword and Ignore Error    Write To ciDebug Log
	Log to console and logfile	[TEST-SPECIFIC SETUP]
	${users} =	Get Variable Value	${users}
	Run Keyword If	${users} is not ${null}	Add Users from variable				${users}
	${ethernet_networks} =	Get Variable Value	${ethernet_networks}
	Run Keyword If	${ethernet_networks} is not ${null}	Add Ethernet Networks from variable	${ethernet_networks}
	${fcoe_networks} =	Get Variable Value	${fcoe_networks}
	Run Keyword If	${fcoe_networks} is not ${null}	        Add FCoE Networks from variable		${fcoe_networks}
	${network_sets} =	Get Variable Value	${network_sets}
	Run Keyword If	${network_sets} is not ${null}	Add Network Sets from variable		${network_sets}
	[Return]

Verify Server Profile status
    [Documentation]    Verify Server Profile status
    [Arguments]
    # create 4 profiles from the Dictionary
	:FOR	${x}	IN RANGE	1	5
	\	${resp}	Fvt Api Get Server Profile By Name	${profiles['Profile${x}']['payload']['name']}
	\	Should Be Equal As Strings	${resp['status']}	OK
    [Return]

Edit uplinkset
    [Documentation]   Edit's an uplinkset associated with a LI
    [Arguments]    ${name}    ${us}   ${LI}
    ${li_uri} =    Get LI URI   ${LI}
    ${us_uri} =    Get Uplinkset URI       ${name}
    ${body} =      Build US body    ${us}    ${li_uri}
    ${resp} =      Fusion Api Edit Uplink Set    body=${body}    uri=${us_uri}
    [Return]       ${resp}

Server Process
    [Documentation]   Server OS process. Tested for Linux. Windows stub only
    [Arguments]    ${name}    ${us}   ${LI}

	${ip} =	Set Variable	${profiles['Profile${x}']['IP']}
	Wait For Server To Be Pingable	${ip}
	${handle} =	Run keyword if    os.name == "nt"	Start Process	ping    ${ip}    stdout=Profile${x}_${ip}.out
	...	ELSE	Start Process	ping    ${ip}    stdout=Profile${x}_${ip}.out   shell=yes
	Sleep	1m
	Set To Dictionary	${profiles['Profile${x}']}	handle	${handle}
	OperatingSystem.File Should Exist    Profile${x}_${ip}.out

Edit Profile
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

IC reached state
    [Documentation]     ...
	[Arguments]	    ${uri}  ${state}
	Set Log Level	TRACE
    ${resp} =   fusion api get resource     ${uri}
	Log    \t ${uri}: ${resp['state']}    console=True
	Should Match Regexp 	${resp['state']}    ${state}
	[Return]	${resp}

Power request
    [Documentation]     ...
    [Arguments]     ${uri}    ${power}
    ${data} =   Create Dictionary   op=replace
    ...                             path=/powerState
    ...                             value=${power}
    ${body} =   Create List     ${data}
    Run Keyword and Ignore Error    Write To ciDebug Log    \nPowering ${power}: ${uri}
    ${resp} =   fusion api patch interconnect   body=${body}    uri=${uri}
    ${task} =   Wait for Task   ${resp}  5m   10s
    ${valDict} =    Create Dictionary       status_code=${200}
    ...                                 taskState=Completed
    Validate Response       ${task}   ${valDict}
	Log    \t Waiting for ${uri} to reach powerState:${power}    console=True
    Wait Until Keyword Succeeds     10 min   20s      IC reached powerState    ${uri}    ${power}

IC reached powerState
    [Documentation]     ...
	[Arguments]	    ${uri}  ${state}
	Set Log Level	TRACE
    ${resp} =   fusion api get resource     ${uri}
	Log    \t ${uri}: ${resp['powerState']}    console=True
	Should Match Regexp 	${resp['powerState']}    ${state}
	[Return]	${resp}

verify LIG QoS values
    [Documentation]     verify LIG QoS configuration
	[Arguments]	    ${qoslig}   ${qosConfig}
    ${Resp} =	Fusion Api Get Lig     param=?filter="'name'=='${qoslig['name']}'"
	${Resp1} = 	Copy List	${Resp['members'][0]['qosConfiguration']['activeQosConfig']['qosTrafficClassifiers']}
	${Resp2} = 	Copy List	${qosConfig['activeQosConfig']['qosTrafficClassifiers']}
    Run Keyword If		'${Resp['members'][0]['qosConfiguration']['activeQosConfig']['configType']}' != '${qosConfig['activeQosConfig']['configType']}' or '${Resp['members'][0]['qosConfiguration']['activeQosConfig']['uplinkClassificationType']}' != '${qosConfig['activeQosConfig']['uplinkClassificationType']}' or '${Resp['members'][0]['qosConfiguration']['activeQosConfig']['downlinkClassificationType']}' != '${qosConfig['activeQosConfig']['downlinkClassificationType']}'  Fail    ELSE  log to console   \n-Successfully got the QoS details
	Check Qos values	${Resp1}	${Resp2}

verify LI QoS values
    [Documentation]     verify LI QoS configuration (one LI only for this test suite)
	[Arguments]	    ${qosConfig}
    ${Resp} =    Fusion Api Get Li
	${Resp1} = 	Copy List	${Resp['members'][0]['qosConfiguration']['activeQosConfig']['qosTrafficClassifiers']}
	${Resp2} = 	Copy List	${qosConfig['activeQosConfig']['qosTrafficClassifiers']}
    Run Keyword If		'${Resp['members'][0]['qosConfiguration']['activeQosConfig']['configType']}' != '${qosConfig['activeQosConfig']['configType']}' or '${Resp['members'][0]['qosConfiguration']['activeQosConfig']['uplinkClassificationType']}' != '${qosConfig['activeQosConfig']['uplinkClassificationType']}' or '${Resp['members'][0]['qosConfiguration']['activeQosConfig']['downlinkClassificationType']}' != '${qosConfig['activeQosConfig']['downlinkClassificationType']}'  Fail    ELSE  log to console   \n-Successfully got the QoS details
	Check Qos values	${Resp1}	${Resp2}
    log to console	Successfully verified the QoS values

Check Qos values
    [Documentation]     check QoS values...
	[Arguments]		${Resp1}	${datavalues}
	${Qosvalues1} = 	Copy List	${Resp1}
	${Qosvalues2} = 	Copy List	${datavalues}
	${p} = 	Get Length	${Qosvalues1}
	:FOR	${x}	IN RANGE	0	${p}
    \   Log to Console  in loop
	\	${classname} =	Get From Dictionary	${Qosvalues1[${x}]['qosTrafficClass']}	className
	\	Check Classname    ${Qosvalues2}   ${x}    ${classname}    ${Qosvalues1}

Check Classname
    [Documentation]     check QoS classname...
    [Arguments]    ${Qosvalues2}    ${x}    ${classname}    ${Qosvalues1}
    ${q} =     Get Length    ${Qosvalues2}
    :FOR    ${y}    IN RANGE    0    ${q}
    \   Run Keyword If    '${classname}' == '${Qosvalues2[${y}]['qosTrafficClass']['className']}'   Dictionaries Should Be Equal  ${Qosvalues2[${y}]}  ${Qosvalues1[${x}]}    Else    Continue For Loop
    Log to Console  Successfully verified all values for classname ${classname}
    #\    Run Keyword If    '${classname}' == '${Qosvalues2[${y}]['qosTrafficClass']['className']}' Dictionaries #Should Be Equal  ${Qosvalues2[${y}]}  ${Qosvalues1[${x}]} and Exit For Loop    Else    Continue For Loop

#backup for adhoc tests
QoS Edit Profiles to add FCoE connections
    # Edit 4 profiles to add FCoE connections (default Profile configuration)
	:FOR	${x}	IN RANGE	1	5
	\   Edit Profile    ${profiles['Profile${x}']['payload']}
	\	${resp}	Fvt Api Get Server Profile By Name	${profiles['Profile${x}']['payload']['name']}
	\	Should Be Equal As Strings	${resp['status']}	OK

#Start iperf Process
#    [Documentation]    Start iperf process to the specified target ip, and direct stdout to specified output file
#    ...                Return process handle
#    [Arguments]    ${ip}    ${output}
#
#    ${handle} =    Run keyword if    os.name == "nt"    Start Process    ping   -t   ${ip}    stdout=iperf_srvr_${ip}.txt
#    ...    ELSE    Start Process    ping    ${ip}    stdout=${output}    shell=True
#
#	\    ${handle} =	Run keyword if    os.name == "nt"	Start Process	ping    ${ip}    stdout=Profile${x}_${ip}.out
#	\    ...	ELSE	Start Process	ping    ${ip}    stdout=Profile${x}_${ip}.out   shell=yes
#
#    OperatingSystem.File Should Exist    ${output}
#    [Return]    ${handle}

Suite Teardown
    [Documentation]     Teardown at end of QoS tests
    Set Log Level    TRACE
    Return from keyword if   ${SKIPTEARDOWN} is ${True}
    Log    \n[TEARDOWN]   console=True
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Power off ALL Servers
    Remove All Server Profiles
    Remove ALL LS
    Remove ALL LSGs
    Remove All LEs
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Remove All SAS LIGs
    Remove ALL Ethernet Networks
    Remove ALL FC Networks
    Remove ALL FCoE Networks
    Remove ALL Network Sets
    Remove ALL Users
