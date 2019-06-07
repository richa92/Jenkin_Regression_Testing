*** Settings ***
Documentation		OVF5199 Nitro SpeedMode Test cases
...                 SuiteName: OVF5199-Nitro-Speedmodes

...					Usage (Rack Nitro Integration rig Multi Frame Redundant configuration):
...					pybot -d /tmp/logs/OVF5199-speedmode -T -V data-OVF5199-25n50Gb-speedmodes-NitroIntRig.py -v APPLIANCE_IP:15.245.131.182 -v max:2 OVF5199-Nitro-Speedmode-TestCases.robot

Variables		data-OVF5199-25n50Gb-speedmodes-NitroIntRig.py

Resource            ../FVT/speedmode-keywords.txt
Resource            ../../../../../Resources/api/fusion_api_resource.txt

Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary
Library			Collections
Library			SSHLibrary
Library			String
Library			Process
Library			../FVT/fvt_api.py

Suite Setup     Speedmode Suite Setup with Networks
Suite Teardown	Suite Teardown

# Setup\Teardown for ALL test cases
Test Setup       Common Test Setup
Test Teardown    Common Test Teardown

*** Variables ***
${APPLIANCE_IP}		15.245.131.251
${numFrames}    3
# Demo mode - 1; Nonstop - 0
${PAUSE}    1
${TRUE}    1

${bay3}               3
${server_efuse_sleeptime}    300
${ufg_statusdelay}    180
${efuse_sleeptime}    180

${sleeptime_potashAdd}    2400
${enc1_bay3_icm}	${ENC_1}, interconnect 3
${enc1_bay6_icm}	${ENC_1}, interconnect 6
${enc2_bay3_icm}	${ENC_2}, interconnect 3
${enc2_bay6_icm}	${ENC_2}, interconnect 6
${enc3_bay3_icm}	${ENC_3}, interconnect 3
${enc3_bay6_icm}	${ENC_3}, interconnect 6

# Nitro Integration rig
# Enclosure 1 Bay 1 server = index 0 (d1); Enclosure 2 Bay 1 server = index 12 (d13) etc..
# 0 - Enclosure 1 Bay 1 Quagmire; 1 - Enclosure 1 Bay 2 Quack; 2 - Enclosure 1 Bay 3 Quagmire2;
# 12 - Enclosure 2 Bay 1 Quagmire; 13 - Enclosure 2 Bay 2 Quack; 14 - Enclosure 2 Bay 3 Quagmire2;
# 24 - Enclosure 3 Bay 1 Quagmire; 25 - Enclosure 3 Bay 2 Quack; 26 - Enclosure 3 Bay 3 Quagmire2;

${enc1_QuagmireSeverBay}               0
${enc1_QuackSeverBay}               1
${enc2_QuagmireSeverBay}               12
${enc2_QuackSeverBay}               13
${enc2_Quagmire2SeverBay}               14
${enc3_QuagmireSeverBay}               24
${enc3_QuackSeverBay}               25
${enc3_Quagmire2SeverBay}               26

${FUSION_IP}					${APPLIANCE_IP}
${SKIPTEARDOWN}                 ${True}

${LI_SPEEDMODE_extra2ndILT_ERROR}    The interconnect link topology is not compatible with a logical interconnect downlink speed of 25.
${LI_SPEEDMODE_extra2ndILT_RSLN}    Ensure all enclosures have one interconnect link cable if the downlink port speed is set to 10 or 25 Gb/s. Alternatively, if the downlink speed setting is set to 50 Gb/s, two interconnect link cables are required.
${LI_SPEEDMODE10_DOWNGRADE_ERROR}    The requested logical interconnect downlink speed of 10 Gb/s is less than the sum of all requested bandwidth settings for connections on the downlink ports associated with this logical interconnect.
${LI_SPEEDMODE25_DOWNGRADE_ERROR}    The requested logical interconnect downlink speed of 25 Gb/s is less than the sum of all requested bandwidth settings for connections on the downlink ports associated with this logical interconnect.
${LI_SPEEDMODE50_DOWNGRADE_ERROR}    The requested logical interconnect downlink speed of 50 Gb/s is less than the sum of all requested bandwidth settings for connections on the downlink ports associated with this logical interconnect.

*** Keywords ***
Create LIG Negative Use Cases
    [Documentation]    Create LIG Negative test cases
    ...                    Test cases and Error message details are in data file

    Log to console    ${\n}Create LIG negative tests
    # Create LIG Negative test cases return 400 or task errors.

    # This error returns httpstatus 400 instead of from task taskErrors
    :FOR    ${ligtest}    IN    @{EncX_ligs_400errs}
    \	${body} =    Build LIG body    ${ligtest['ligBody']}
    \	${resp} =    Fusion Api Create LIG    ${body}
    \	Should Be Equal As Integers    ${resp['status_code']}    ${ligtest['status_code']}
    \	Should Be Equal As Strings    ${resp['errorCode']}    ${ligtest['errorCode']}

#    # For some LIGs error is returned as task Error. None for this feature
#    :FOR    ${ligtest}    IN    @{EncX_ligs_taskerrs}
#    \	${resp} =    Add LIG from variable async    ${ligtest['ligBody']}
#    \	Wait For Task2    ${resp}    timeout=240    interval=2    PASS=Error    errorMessage=${ligtest['errorMessage']}

Edit LIG Negative Use Cases
    [Documentation]    Edit LIG Negative test cases
    ...                    Test cases and Error message details are in data file

    Log to console    ${\n}Edit LIG negative tests
    # Edit LIG Negative test cases return 400 or task errors.

    # This error returns httpstatus 400 instead of from task taskErrors
    :FOR    ${ligtest}    IN    @{EncX_edit_ligs_400errs}
    \	${body} =    Build LIG body    ${ligtest['ligBody']}
    \   Set To Dictionary	${body}	qosConfiguration	${LIGqosConfiguration}
	\   ${uri} =	Get LIG Uri   ${ligtest['ligBody']['name']}
    \	${resp} =    Fusion Api Edit LIG    ${body}    ${uri}
    \	Should Be Equal As Integers    ${resp['status_code']}    ${400}
    \	Should Be Equal As Strings    ${resp['errorCode']}    ${ligtest['errorCode']}

#     No LIG task error use cases for this feature

#    # For some LIGs error is returned as task Error
#    :FOR    ${ligtest}    IN    @{EncX_edit_ligs_taskerrs}
#    \	${body} =    Build LIG body    ${ligtest['ligBody']}
#    \   Set To Dictionary	${body}	qosConfiguration	${LIGqosConfiguration}
#	\   ${uri} =	Get LIG Uri   ${ligtest['ligBody']['name']}
#    \	${resp} =    Fusion Api Edit LIG    ${body}    ${uri}
#    \	Wait For Task2    ${resp}    timeout=240    interval=2    PASS=Error    errorMessage=${ligtest['errorCode']}

Verify LIG speedmode
    [Documentation]    Verify speed mode of LIG
    [Arguments]     ${tempLig}     ${speedMode}

    ${resp}	Fvt Api Get Logical Interconnect Group By Name	${tempLig['name']}
    Should Be Equal As Strings	${resp['name']}	${tempLig['name']}
    Should Be Equal As Strings	${resp['downlinkSpeedMode']}	${speedMode}

Edit Downlink Speed Mode Of LI
	[Documentation]	Edit Downlink Speed Mode Of LI
	[Arguments]		${LI}    ${SpeedMode}

	Log	\n Edit Downlink Speed Mode Of LI ${LI}	console=True
	${resp}	Fvt Api Get Logical Interconnect By Name	${LI}
	${LI_URI} =	Set Variable if	${resp} != None	${resp['uri']}	'/${LI} does not exist'
	${LI_ConsistencyStatus} =	Set Variable if	${resp} != None	${resp['consistencyStatus']}	'/${LI} does not exist'
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	${LE_ConsistencyStatus} =	Set Variable if	${resp} != None	${resp['state']}	'/${LE} does not exist'

	Set To Dictionary	${li_downlinkSpeedMode[0]}    value   ${SpeedMode}
	${resp}	Fusion Api Patch Li		${li_downlinkSpeedMode}	${LI_URI} ?force=true
	Should Be Equal As Integers	${resp['status_code']}	202
	Wait For Task	${resp}	timeout=30 m	interval=2 s

    # verify LI is changed to new Speedmode or not
	Sleep	${ufg_statusdelay}
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	${SpeedMode}

    # No change in LI or LE consistency status
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['state']}	${LE_ConsistencyStatus}

	[Return]

Edit Downlink Speed Mode Of LI Negative
	[Documentation]	Edit Downlink Speed Mode Of LI for Negative test cases
	[Arguments]		${LI}    ${SpeedMode}    ${expected_errorcode}

	Log	\n Edit Downlink Speed Mode Of LI ${LI}	console=True
	${resp}	Fvt Api Get Logical Interconnect By Name	${LI}
	${LI_URI} =	Set Variable if	${resp} != None	${resp['uri']}	'/${LI} does not exist'
	${LI_ConsistencyStatus} =	Set Variable if	${resp} != None	${resp['consistencyStatus']}	'/${LI} does not exist'
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	${LE_ConsistencyStatus} =	Set Variable if	${resp} != None	${resp['state']}	'/${LE} does not exist'

	Set To Dictionary	${li_downlinkSpeedMode[0]}    value   ${SpeedMode}
	${resp}	Fusion Api Patch Li		${li_downlinkSpeedMode}	${LI_URI}
    Should Be Equal As Integers    ${resp['status_code']}    ${400}
    Should Be Equal As Strings    ${resp['errorCode']}    ${expected_errorcode}

	[Return]

Edit LI Downlink Speed Mode Downgrade Error
	[Documentation]	Edit Downlink Speed Mode Of LI not allowed
	[Arguments]		${LI}    ${SpeedMode}    ${timeout}=5m    ${interval}=10s   ${endstate}=((?i)Error)

	Log	\n Edit Downlink Speed Mode Of LI ${LI}	console=True
	${resp}	Fvt Api Get Logical Interconnect By Name	${LI}
	${LI_URI} =	Set Variable if	${resp} != None	${resp['uri']}	'/${LI} does not exist'
#	${LI_ConsistencyStatus} =	Set Variable if	${resp} != None	${resp['consistencyStatus']}	'/${LI} does not exist'
#	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
#	${LE_ConsistencyStatus} =	Set Variable if	${resp} != None	${resp['state']}	'/${LE} does not exist'

    ${LI_SPEEDMODE_DOWNGRADE_ERROR} =    Set Variable    The requested logical interconnect downlink speed of 25 Gb/s is less than the sum of all requested bandwidth settings for connections on the downlink ports associated with this logical interconnect.

	Set To Dictionary	${li_downlinkSpeedMode[0]}    value   ${SpeedMode}
	${resp}	Fusion Api Patch Li		${li_downlinkSpeedMode}	${LI_URI}
#    Wait For Task2    ${resp}    timeout=240    interval=2    PASS=Error    errorMessage=${LI_SPEEDMODE10_DOWNGRADE_ERROR}
	${task} =   Wait For Task	${resp}		timeout=${timeout}		interval=${interval}
    Verify ErrorMessage in taskError  ${task['taskErrors']}    ${LI_SPEEDMODE_DOWNGRADE_ERROR}
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ${endstate}
	[Return]

Delete Profiles and LE in speedmode
    [Documentation]    Delete Profiles and LE from appliance
	[Arguments]		${LE}	${timeout}=600m	${interval}=1m

    # Not Planning to implement as other test suites covers default speed mode testing
    Power off all servers    PressAndHold
	Sleep	300 sec
    Remove All Server Profiles

    Remove All LEs

	[Return]

Verify Server Profile status
    [Documentation]    Verify Server Profile status
	[Arguments]		${profile}

    ${resp} =     Fusion Api Get Server Profiles        param=?filter="'name'=='${profile['payload']['name']}'"
    Return From Keyword If  ${resp['count']}==0  /rest/server_profile_uri_${sp}_not_found
#    Log To Console	\n ProfileResponse : ${resp['members'][0]}
#    Should Be Equal As Strings	${resp['members'][0]['status']}	OK
    Run Keyword And Continue On Failure    Should Be Equal As Strings	${resp['members'][0]['status']}	OK
    [Return]

Speedmode Profile Status verification
    [Documentation]    Verify Profile status is OK or not
	[Arguments]	${numFrames}    ${profilesDataSection}

    # Verify Profile status
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesDataSection}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Verify Server Profile status
    [Return]

LI Alert Cleared verification
    [Documentation]    LI page Activity Log entry verification
    [Arguments]     ${LI_NAME}    ${description}    ${correctiveAction}

    ${resp} =  Get Alert by Param    param=?filter="alertState EQ 'Cleared'"&filter="healthCategory EQ 'logical-interconnect'"&filter="associatedResource.resourceName EQ '${LI_NAME}'"&filter="description EQ '${description}'"
    Log to console      \n LI Alert response : ${resp}
    [Return]

LI Alert verification
    [Documentation]    LI page Activity Log entry verification
    [Arguments]     ${LI_NAME}    ${description}    ${correctiveAction}

    ${resp} =  Get Alert by Param    param=?filter="alertState EQ 'Active'"&filter="healthCategory EQ 'logical-interconnect'"&filter="associatedResource.resourceName EQ '${LI_NAME}'"&filter="description EQ '${description}'"
    Log to console      \n LI Alert response : ${resp}

    [Return]

# QoS keywords
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

Get Server Ip Windows
    [Documentation]    Gets the valid IP addresses of the server.
    [Arguments]         ${ilo_details}
	[Arguments]		${ilo_details}	${netPrefix}
    ${serverip_List}    Create List
    ${serverip_List1}    Create List
    SSHLibrary.Open Connection     ${ilo_details['ilo_ip']}     prompt=>     timeout=20s
    ${login}    SSHLibrary.Login    ${ilo_details['username']}     ${ilo_details['password']}
    SSHLibrary.Read Until Prompt
    SSHLibrary.Write     stop /system1/oemhp_VSP1
    SSHLibrary.Read Until Prompt
    SSHLibrary.Write     vsp
    Sleep    5sec
    SSHLibrary.Read Until    SAC>
    Sleep    5sec
    SSHLibrary.Write    i
    Sleep    5sec
    ${stdout}    SSHLibrary.Read
    Log to Console    \nstdout is ${stdout}

    # Nitro Integration rig IP addresses 172.16.<1-15>.x
    # Ip=191\\.\\d+\\.\\d+\\.\\d+
    # Ip=19\\d\\.\\d+\\.\\d+\\.\\d+
    # Ip=19\\d\\.\\d+\\.\\^[3]\\d+\\.\\d+

#    ${cmd_output}=    Get Regexp Matches    ${stdout}    Ip=17\\d\\.\\d+\\.\\d+\\.\\d+
    ${cmd_output}=    Get Regexp Matches    ${stdout}    Ip=${netPrefix}\\d\\.\\d+\\.\\d+\\.\\d+

    Log to Console    \nstdout is ${cmd_output}
    ${ip_list_new}    Create List
    ${len}    Get Length    ${cmd_output}
    :FOR    ${x}    IN RANGE    ${len}
    \    ${ip_lists}    Remove String    ${cmd_output[${x}]}    Ip=
    \    Log to console    ip is ${ip_lists}
    \    Append To List   ${ip_list_new}    ${ip_lists}
    SSHLibrary.Close All Connections
    [Return]    ${ip_list_new}

*** Test Cases ***
OVF5199 Create LIG with invalid speed mode NEGATIVE TEST
    [Documentation]    LIG Negative test cases with invalid speed modes
    ...                    Test cases and Error message details are in data files

	Log To Console	\n LIG Negative test cases with invalid speed modes

	Run Keyword And Continue On Failure	Create LIG Negative Use Cases

	Log To Console	\n Finished LIG Negative test cases with invalid speed modes

OVF5199 Create LIG with default speedmode and verify downlinkSpeedMode 25G
    [Documentation]    OVF5199 Create LIG with default speedmode and verify downlinkSpeedMode 25G

# Create a SE/ME LIG and verify default speed mode is set to 25G
# "downlinkSpeedMode": 25G

    # Create LIG without speed mode specified.
    # LIG is created with default speedmode 25G
	Log To Console	\n Create LIG with default speedmode 25G

    ${ligs} =     Evaluate  {k: v for k, v in ${ligs_25G}.iteritems() if 'Enc${numFrames}' in k}
    Run Keyword If	${ligs} is not ${null}	Run Keyword for Dict	    ${ligs}       Add LIG from variable
    Run Keyword If	${ligs} is not ${null}	Run Keyword for Dict	    ${ligs}       Verify LIG speedmode    SPEED_25GB

	Log To Console	\n Finished Create LIG with default speedmode

OVF5199 Create LIG with 50G speed mode and verify downlinkSpeedMode 50G
    [Documentation]    OVF5199 Create LIG with 50G speed mode and verify downlinkSpeedMode 50G

# Create a SE/ME LIG with 50G speed mode
# "downlinkSpeedMode": 50G

    # create 50G LIG
	Log To Console	\n Create LIG with 50G speedmode

    ${ligs} =     Evaluate  {k: v for k, v in ${ligs_50G}.iteritems() if 'Enc${numFrames}' in k}
    Run Keyword If	${ligs} is not ${null}	Run Keyword for Dict	    ${ligs}       Add LIG from variable
    Run Keyword If	${ligs} is not ${null}	Run Keyword for Dict	    ${ligs}       Verify LIG speedmode    SPEED_50GB

	Log To Console	\n Finished Create LIG with 50G speedmode

OVF5199 Edit LIG with speed mode changed 25Gb to 50G and vice versa
    [Documentation]    OVF5199 Edit LIG with speed mode changed 25Gb to 50G and vice versa

    # Edit LIG with speed mode changed from default 25Gb to 50G and back to 25G.

    # create LIGs which will be used for LIG Edit test cases
   	${ligs} =	      Get Variable Value	${ligs}
	Run Keyword If	${ligs} is not ${null}	Run Keyword for Dict	    ${ligs}       Add LIG from variable

	Log To Console	\n Edit LIG with with speed mode changed from 25Gb to 50Gb.

	#edit LIG to change speed mode from 25G to 50G
    ${body} =    Build LIG body    ${edit_ligs['Enc${numFrames}-25G-EDIT-LIG']['ligBody']}
#	Set To Dictionary	${body}	qosConfiguration	${LIGqosConfiguration}
	${uri} =	Get LIG Uri   ${edit_ligs['Enc${numFrames}-25G-EDIT-LIG']['ligBody']['name']}

    ${resp} =    Fusion Api Edit LIG    ${body}    ${uri}
    ${task} =    Wait For Task    ${resp}    300s    2s
    ${resp}	Fvt Api Get Logical Interconnect Group By Name	${edit_ligs['Enc${numFrames}-25G-EDIT-LIG']['ligBody']['name']}
    Should Be Equal As Strings	${resp['name']}	${edit_ligs['Enc${numFrames}-25G-EDIT-LIG']['ligBody']['name']}
    Verify LIG speedmode     ${edit_ligs['Enc${numFrames}-25G-EDIT-LIG']['ligBody']}    SPEED_50GB

	Log To Console	\n Edit LIG with with speed mode changed from 50Gb to 25Gb.

	#edit LIG to change speed mode from 50G to 25G
    ${body} =    Build LIG body    ${edit_ligs['Enc${numFrames}-50G-EDIT-LIG']['ligBody']}
#	Set To Dictionary	${body}	qosConfiguration	${LIGqosConfiguration}
	${uri} =	Get LIG Uri   ${edit_ligs['Enc${numFrames}-50G-EDIT-LIG']['ligBody']['name']}
    ${resp} =    Fusion Api Edit LIG    ${body}    ${uri}
    ${task} =    Wait For Task    ${resp}    300s    2s
    ${resp}	Fvt Api Get Logical Interconnect Group By Name	${edit_ligs['Enc${numFrames}-50G-EDIT-LIG']['ligBody']['name']}
    Should Be Equal As Strings	${resp['name']}	${edit_ligs['Enc${numFrames}-50G-EDIT-LIG']['ligBody']['name']}
    Verify LIG speedmode     ${edit_ligs['Enc${numFrames}-50G-EDIT-LIG']['ligBody']}    SPEED_25GB

 	Log To Console	\n Finished Edit LIG with with speed mode changed 25Gb to 50G and vice versa.

OVF5199 Edit LIG with invalid speed mode NEGATIVE TEST
# Edit LIG with invalid speed mode NEGATIVE TEST
    [Documentation]    LIG Negative test cases with invalid speed modes
    ...                    Test cases and Error message details are in data files

	Log To Console	\n LIG Negative test cases with invalid speed modes

	Run Keyword And Continue On Failure	Edit LIG Negative Use Cases

	Log To Console	\n Finished LIG Negative test cases with invalid speed modes

OVF5199 Create EGs
    [Documentation]    OVF5199 Create EGs

	Log To Console	\n Create EGs

    ${egs} =     Evaluate  {k: v for k, v in ${enc_group}.iteritems() if 'Enc${numFrames}' in k}
    Run Keyword for Dict    ${egs}    Add Enclosure Group and Verify

	Log To Console	\n Finished Creating EGs

OVF5199 25G Happy path Create LE
    [Documentation]    OVF5199 25G Happy path Create LE

#•	CXP/ILT 2x25Gb topology
#•	Create LE/LI from an LIG with 25G speed mode.
#•	Verify LI speed mode is set to 25G
#•	Verify ICM downlinks for 25G speedmode
#•	Create server profiles for servers with Bronco and Quack
#o	Quack 10/20/25Gb – 25G
#o	Quagmire 25/50Gb – 25G
#   Verify end to end traffic

	Log To Console	\n OVF5199 25G Happy path Create LE
#    Delete Profiles and LE in speedmode    ${LE}

    Log to console	\n Creating LE
	Create Enclosure List for LE Dictionary    ${numFrames}	${numFrames}
	Set To Dictionary	${les}	enclosureGroupUri	EG:Enc${numFrames}-25G-EG
	${task} =	Add Logical Enclosure from variable     ${les}
	Sleep	3 sec

	# Verify ICM status(Configured)
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc1_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay6_icm}    Configured

    # Verify LI and LE consistency status values
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['state']}	Consistent

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_REDUNDANT_25G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_25GB

	Log To Console	\n Finished OVF5199 25G Happy path Create LE

OVF5199 25G Happy path ICM downlink status check
    [Documentation]    OVF5199 25G Happy path ICM downlink status check

	Log To Console	\n 25Gb Happy path ICM downlink status check

	# Verify ICM status(Configured)
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc1_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay6_icm}    Configured

#   OVD25148 - The test scripts should be changed to have about 4.5 minutes of delay
#   between the ICM going to configured state and checking the interconnect info data.
#    Sleep    5 min  #	${server_efuse_sleeptime}
	Sleep	${server_efuse_sleeptime}

# Enclosure 1 Bay 1 server = index 0 (d1); Enclosure 2 Bay 1 server = index 12 (d13) etc..
# 0 - Enclosure 1 Bay 1 Bronco; 1 - Enclosure 1 Bay 2 Quack; 2 - Enclosure 1 Bay 3 Quagmire;
# 12 - Enclosure 2 Bay 1 Bronco; 21 - Enclosure 2 Bay 10 Quagmire2;

    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc1_QuackSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc1_QuagmireSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc2_QuagmireSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc2_Quagmire2SeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc2_QuagmireSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc2_Quagmire2SeverBay}    Linked    Speed25G

    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc1_QuackSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc1_QuagmireSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc2_QuagmireSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc2_Quagmire2SeverBay}    Linked    Speed25G

	Log To Console	\n Finished OVF1811 NitroME Nitro ICM downlink status check

OVF5199 25G LI with 50G ILT verify extra cable alert
    [Documentation]    OVF5199 25Gb SPEEDMODE LE with A and B side LIGs

# If LE is created with 25G mode and Synergy frames are with 50G ILT,
# an extra cable alert is logged (LI is being used in 25G ILT topology)

    # Verify LI extra cable alert
    # The interconnect link topology is not compatible with a logical interconnect downlink speed of 25.
    # Resolution: Remove the excess interconnect link cable. Alternatively, update the logical interconnect downlink speed mode setting to 25 Gb/s mode.
	Set Suite Variable	${LIName}	${LI_REDUNDANT_25G}
    LI Alert verification    ${LIName}    ${LI_SPEEDMODE_extra2ndILT_ERROR}    ${LI_SPEEDMODE_extra2ndILT_RSLN}

	Log To Console	\n Finished Edit LI Speed mode to 25Gb

OVF5199 25G SPEED Mode Create Server Profiles
    [Documentation]    OVF5199 25Gb SPEEDMODE LE with A and B side LIGs

	Log To Console	\n Creating Server Profiles for 25Gb speedmode

    Power off all servers

# EG Enc${numFrames}-25G-EG
    Set Suite Variable	${EG}	Enc${numFrames}-25G-EG
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profiles25}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       FVT Create Server Profile FlexFrames    ${EG}

	Log To Console	\n Finished Creating Profiles for LI 25Gb mode

OVF5199 25G SPEED Mode Profile Status verification
    [Documentation]    OVF5199 25Gb SPEEDMODE LE with A and B side LIGs

	Log To Console	\n 25G SPEED Mode REDUNDANT end to end verification

    # Verify Profile status
    Set Test Variable	${profilesGroup}	${profiles25}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Verify Server Profile status

	Log To Console	\n Finished 25G SPEED Mode REDUNDANT end to end verification

OVF5199 25G SPEED Mode end to end verification
    [Documentation]   Start End to End tests
	Log To Console	\n 25Gb SPEED Mode REDUNDANT end to end verification

    Set Test Variable	${profilesGroup}	${profiles25}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Server Profile Connectivity With Ping

	Log To Console	\n Finished 25G SPEED Mode REDUNDANT end to end verification

OVF5199 Edit LI Speed mode NEGATIVE
    [Documentation]    OVF5199 25Gb SPEEDMODE LE with A and B side LIGs

#261	Change LI mode from 25G to 50G (speed upgrade)

	Log To Console	\n Edit LI Speed mode to UNSUPPORTED/UNKNOWN/NOT_APPLICABLE/Invalid values

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_REDUNDANT_25G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_25GB

    # Edit LI speed to UNSUPPORTED
    Edit Downlink Speed Mode Of LI Negative    ${LI_REDUNDANT_25G}    UNSUPPORTED    CRM_INVALID_DOWNLINKSPEEDMODE

    # Edit LI speed to UNSUPPORTED
    Edit Downlink Speed Mode Of LI Negative    ${LI_REDUNDANT_25G}    UNKNOWN    CRM_INVALID_DOWNLINKSPEEDMODE

    # Edit LI speed to UNSUPPORTED
    Edit Downlink Speed Mode Of LI Negative    ${LI_REDUNDANT_25G}    NOT_APPLICABLE    CRM_INVALID_DOWNLINKSPEEDMODE

    # Edit LI speed to UNSUPPORTED
    Edit Downlink Speed Mode Of LI Negative    ${LI_REDUNDANT_25G}    ["SPEED_25_50GB"]    CRM_INVALID_PATCH_REQUEST

    Edit Downlink Speed Mode Of LI Negative    ${LI_REDUNDANT_25G}    ""    CRM_INVALID_PATCH_REQUEST

	Log To Console	\n Finished Edit LI Speed mode to UNSUPPORTED/UNKNOWN/NOT_APPLICABLE/Invalid values

# ICM action test cases have multiple defects. May have to Ignore tests with TAG ICMACTIONS.

OVF5199 Remove and insert back Nitro ICM when LI is in 25G mode
    [Documentation]    OVF5199 Remove and insert back Nitro ICM when LI is in 25G mode
    [Tags]  ICMACTIONS
#•	Remove and insert back Nitro ICM
#•	Verify LI continues to be in 25G mode after Nitro ICM efuse

	Log To Console	\n Remove and add Nitro ICM and verify Speedmode configuration

    # CN754406W4, interconnect 3
    ${uri} =    Get IC URI      ${ENC_1}, interconnect 3

    # Remove Potash from Enclosure 1 bay 3 which is part of Redundant LI
    Get EM IP      ${ENC_1}
    Get EM Token    ${ENC_1}
    Efuse ICM   EFuseOn     ${bay3}

	Log    \t Waiting for ${uri} to reach state:Absent    console=True
    Wait Until Keyword Succeeds     5 min   30s      IC reached state    ${uri}    Absent

    # ICM is Absent now. Wait for couple of more minutes
	Sleep	${efuse_sleeptime}

    Efuse ICM   EFuseOff     ${bay3}
	Log    \t Waiting for ${uri} to reach state:Configured    console=True
    Wait Until Keyword Succeeds     40 min   30s      IC reached state    ${uri}    Configured

	# Verify ICM status(Configured)
	Sleep	${efuse_sleeptime}
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured

    # Verify LI and LE consistency status values
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['state']}	Consistent

	Set Suite Variable	${LI}	${LE}-Enc${numFrames}-25G-LIG
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LIName}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_25GB

	Log To Console	\n Finished removing and adding Nitro ICM and verifying Speedmode configuration

OVF5199 Reset ICM when LI is in 25G mode
    [Documentation]    OVF5199 Reset ICM when LI is in 25G mode
    [Tags]  ICMACTIONS
#•	LI in 25G mode
#•	Reset ICM
#•	Verify LI continues to be in 25G mode after Nitro ICM reset

	Log To Console	\n Reset ICM when LI is in 25G mode

	${LI_SPEEDMODE} =	Set Variable	SPEED_25GB
	${LIName} =	Set Variable	${LI_REDUNDANT_25G}
#	Set Suite Variable	${LIName}	${LI_REDUNDANT_25G}

    # CN754406W4, interconnect 3
    ${uri} =    Get IC URI      ${ENC_1}, interconnect 3

    # Reset ICM with patch request
    ${data} =   Create Dictionary   op=replace
    ...                             path=/deviceResetState
    ...                             value=Reset
    ${body} =   Create List     ${data}
    Run Keyword and Ignore Error    Write To ciDebug Log    \nResetting ICM: ${uri}
    ${resp} =   fusion api patch interconnect   body=${body}    uri=${uri}
    ${task} =   Wait for Task   ${resp}  10m   10s
    ${valDict} =    Create Dictionary       status_code=${200}
    ...                                 taskState=Completed
    Validate Response       ${task}   ${valDict}

    # Action on ICM. Wait for couple of minutes for ICM to bootup/configure
	Sleep	${efuse_sleeptime}

	Log    \t Waiting for ${uri} to reach Configured back after ICM reset    console=True
    Wait Until Keyword Succeeds     20 min   20s      IC reached state    ${uri}    Configured

	# Verify ICM status(Configured)
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured

    # Verify LI and LE consistency status values
    Logical Enclosure State Should Be    ${LE}    Consistent
    Logical Interconnect Consistency Status Should Be  ${LIName}    CONSISTENT

	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['state']}	Consistent

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LIName}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	${LI_SPEEDMODE}

	Log To Console	\n Finished resetting Nitro ICM and verifying Speedmode configuration

OVF5199 Reaply ICM when LI is in 25G mode
    [Documentation]    OVF5199 Reaply ICM when LI is in 25G mode
    [Tags]  ICMACTIONS
#•	LI in 25G mode
#•	Reaply ICM
#•	Verify LI continues to be in 25G mode after Nitro ICM reset

    #Reapply configuration and verify speedmode configuration
	Log To Console	\n Reaply Potash ICM configuration and verify speedmode

    # CN754406W4, interconnect 3
    ${icmuri} =    Get IC URI      ${ENC_1}, interconnect 3

	${resp} =   Fusion Api Reapply Interconnect Configuration    ${icmuri}
    ${task} =   Wait For Task	${resp}		timeout=20m		interval=5s
	${task_state} = 	Get From dictionary 	${task}     taskState
	Should Match Regexp	${task_state}	 ((?i)Warning|Completed)

    # Action on ICM. Wait for couple of minutes for ICM to bootup/configure
	Sleep	${efuse_sleeptime}

	Log    \t Waiting for ${icmuri} to reach Configured back after ICM Reapply    console=True
    Wait Until Keyword Succeeds     20 min   20s      IC reached state    ${icmuri}    Configured

	# Verify ICM status(Configured)
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured

    # Verify LI and LE consistency status values
#	Set Suite Variable	${LE}	${les['SPEED-LE${numFrames}']['name']}
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['state']}	Consistent

	Set Suite Variable	${LI}	${LE}-Enc${numFrames}-25G-LIG
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LIName}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_25GB

	Log To Console	\n Finished reapplying Potash ICM configuration and verifying speedmode configuration

OVF5199 Power OFF and ON ICM when LI is in 25G mode
    [Documentation]    OVF5199 Power OFF and ON ICM when LI is in 25G mode
    [Tags]  ICMACTIONS
#•	LI in 25G mode
#•	Power OFF and ON ICM
#•	Verify LI continues to be in 25G mode after Nitro ICM Power cycle

	Log To Console	\n Power OFF and ON Nitro ICM and verify Speedmode configuration

    # CN754406W4, interconnect 3
    ${uri} =    Get IC URI      ${ENC_1}, interconnect 3

    # Power Off Interconnect
    Power request    ${uri}   Off
    # Action on ICM. Wait for couple of minutes for ICM to bootup/configure
	Sleep	${efuse_sleeptime}

	Log    \t Waiting for ${uri} to reach state:Maintenance    console=True
    Wait Until Keyword Succeeds     45 min   30s      IC reached state    ${uri}    Maintenance

	# Verify ICM status
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Maintenance
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured

    # Power On Interconnect
    Power request    ${uri}   On
    # Action on ICM. Wait for couple of minutes for ICM to bootup/configure
	Sleep	${efuse_sleeptime}
	Log    \t Waiting for ${uri} to reach state:Configured    console=True
    Wait Until Keyword Succeeds     50 min   30s      IC reached state    ${uri}    Configured

	# Verify ICM status(Configured)
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured

    # Verify LI and LE consistency status values
#	Set Suite Variable	${LE}	${les['SPEED-LE${numFrames}']['name']}
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['state']}	Consistent

	Set Suite Variable	${LI}	${LE}-Enc${numFrames}-25G-LIG
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LIName}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_25GB

	Log To Console	\n Finished rebooting Nitro ICM and verifying Speedmode configuration

OVF5199 SPEED Upgrade from 25G to 50G Edit LI speedmode
    [Documentation]    OVF5199 25Gb SPEEDMODE LE with A and B side LIGs

	Log To Console	\n OVF5199 SPEED Upgrade Edit LI speedmode from 25G to 50G

    # verify LI is in 25Gb mode
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_REDUNDANT_25G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_25GB

    # Edit LI speed to 25Gb. LI edit speedmode keyword verifies speedmode value also
    Edit Downlink Speed Mode Of LI    ${LI_REDUNDANT_25G}    SPEED_50GB
	Sleep	${ufg_statusdelay}

    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc1_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay6_icm}    Configured

	#verify LI and LE consistency status values
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_REDUNDANT_25G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_50GB
	# LI status is in Warning with Cisco ToR switch
#	Should Be Equal As Strings	${resp['status']}	OK

    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc1_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay6_icm}    Configured

	Log To Console	\n Finished OVF5199 SPEED Upgrade Edit LI speedmode from 25Gb to 50Gb

OVF5199 SPEED Upgrade from 25G to 50G ICM downlink status check
    [Documentation]    OVF5199 SPEED Upgrade from 25G to 50G ICM downlink status check

	Log To Console	\n 25Gb Happy path ICM downlink status check

	# Verify ICM status(Configured)
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc1_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay6_icm}    Configured

#   OVD25148 - The test scripts should be changed to have about 4.5 minutes of delay
#   between the ICM going to configured state and checking the interconnect info data.
#    Sleep    5 min  #	${server_efuse_sleeptime}
	Sleep	${server_efuse_sleeptime}

# Enclosure 1 Bay 1 server = index 0 (d1); Enclosure 2 Bay 1 server = index 12 (d13) etc..
# 0 - Enclosure 1 Bay 1 Bronco; 1 - Enclosure 1 Bay 2 Quack; 2 - Enclosure 1 Bay 3 Quagmire;
# 12 - Enclosure 2 Bay 1 Bronco; 20 - Enclosure 2 Bay 9 Quagmire2;

    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc1_QuackSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc1_QuagmireSeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc2_QuagmireSeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc2_Quagmire2SeverBay}    Linked    Speed50G

    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc1_QuackSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc1_QuagmireSeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc2_QuagmireSeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc2_Quagmire2SeverBay}    Linked    Speed50G

	Log To Console	\n Finished OVF1811 NitroME Nitro ICM downlink status check

OVF5199 SPEED Upgrade from 25G to 50G ILT verify NO extra cable alert
    [Documentation]    OVF5199 SPEED Upgrade from 25G to 50G ILT verify NO extra cable alert

    # Verify LI extra cable alert cleared
    # The interconnect link topology is compatible with a logical interconnect downlink speed of 50Gbps.
	Set Suite Variable	${LIName}	${LI_REDUNDANT_25G}
    LI Alert Cleared verification    ${LIName}    ${LI_SPEEDMODE_extra2ndILT_ERROR}    ${LI_SPEEDMODE_extra2ndILT_RSLN}

	Log To Console	\n Finished Edit LI Speed mode to 25Gb

OVF5199 SPEED Upgrade speedmode from 25G to 50G Profile Status verification
    [Documentation]    OVF5199 SPEED Upgrade Edit LI speedmode from 25G to 50G Profile Status verification

	Log To Console	\n 25G SPEED Mode REDUNDANT end to end verification

    # Verify Profile status
    Set Test Variable	${profilesGroup}	${profiles25}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Verify Server Profile status

	Log To Console	\n Finished 25G SPEED Mode REDUNDANT end to end verification

OVF5199 SPEED Upgrade end to end tests
    [Documentation]   OVF5199 SPEED Upgrade end to end tests

    Log to Console    Nitro 50G VPLAG End to End tests Verification

    Set Test Variable	${profilesGroup}	${profiles25}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Delete Profile With Multiple Ping Sessions

	Log To Console	\n Finished Nitro 50G VPLAG End to End tests

OVF5199 SPEED Upgrade speedmode from 25G to 50G end to end verification
    [Documentation]   OVF5199 SPEED Upgrade speedmode from 25G to 50G end to end verification
	Log To Console	\n 25G to 50G end to end verification

    Set Test Variable	${profilesGroup}	${profiles50}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
#	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Find Server IP addresses
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Server Profile Connectivity With Ping

	Log To Console	\n Finished 25G to 50G end to end verification

OVF5199 50G SPEEDMODE Create LE
    [Tags]  LE50
    [Documentation]    OVF5199 50G SPEEDMODE Create LE

#   Required LIG and EGs are created in LIG test cases

    Delete Profiles and LE in speedmode    ${LE}

    Log to console	\n Creating 50G SPEEDMODE Create LE
	Create Enclosure List for LE Dictionary    ${numFrames}	${numFrames}
	Set To Dictionary	${les}	enclosureGroupUri	EG:Enc${numFrames}-50G-EG
#	Add Logical Enclosure	${les}	timeout=90m	interval=1m
	${task} =	Add Logical Enclosure from variable     ${les}
	Sleep	3 sec

	# Verify ICM status(Configured)
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc1_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay6_icm}    Configured

    # Verify LI and LE consistency status values
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
#	Should Be Equal As Strings	${resp['status']}	OK
    Should Match Regexp	${resp['status']}	 ((?i)Warning|OK)
	Should Be Equal As Strings	${resp['state']}	Consistent

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_REDUNDANT_50G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_50GB

	Log To Console	\n Finished Creating LE with 50Gb SPEED Mode

OVF5199 50G Happy path ICM downlink status check
    [Documentation]    OVF5199 50G Happy path ICM downlink status check

	Log To Console	\n 50Gb Happy path ICM downlink status check

	# Verify ICM status(Configured)
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc1_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay6_icm}    Configured


#   OVD25148 - The test scripts should be changed to have about 4.5 minutes of delay
#   between the ICM going to configured state and checking the interconnect info data.
#    Sleep    5 min  #	${server_efuse_sleeptime}
	Sleep	${server_efuse_sleeptime}

# Enclosure 1 Bay 1 server = index 0 (d1); Enclosure 2 Bay 1 server = index 12 (d13) etc..
# 0 - Enclosure 1 Bay 1 Bronco; 1 - Enclosure 1 Bay 2 Quack; 2 - Enclosure 1 Bay 3 Quagmire;
# 12 - Enclosure 2 Bay 1 Bronco; 21 - Enclosure 2 Bay 10 Quagmire2;

    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc1_QuackSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc1_QuagmireSeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc2_QuagmireSeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc2_Quagmire2SeverBay}    Linked    Speed50G

    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc1_QuackSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc1_QuagmireSeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc2_QuagmireSeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc2_Quagmire2SeverBay}    Linked    Speed50G

	Log To Console	\n Finished OVF5199 50GB LE Nitro ICM downlink status check

OVF5199 50G SPEED Mode Create Server Profiles
    [Documentation]    OVF5199 50G SPEED Mode Create Server Profiles

	Log To Console	\n Creating Server Profiles for 50Gb speedmode

    # change to selective power off
    Power off all servers    PressAndHold

    Set Suite Variable	${EG}	Enc${numFrames}-50G-EG
    Set Test Variable	${profilesGroup}	${profiles50}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       FVT Create Server Profile FlexFrames    ${EG}

    Set Test Variable	${profilesGroup}	${profiles50to25}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       FVT Create Server Profile FlexFrames    ${EG}

	Log To Console	\n Finished Creating Profiles for LI 50G mode

OVF5199 50Gb SPEED Mode Profile Status verification
    [Documentation]    OVF5199 50Gb SPEED Mode Profile Status verification

	Log To Console	\n 50Gb SPEED Mode REDUNDANT profile verification

    # Verify Profile status
    Set Test Variable	${profilesGroup}	${profiles50}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Verify Server Profile status

    Set Test Variable	${profilesGroup}	${profiles50to25}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Verify Server Profile status

	Log To Console	\n Finished 50Gb SPEED Mode profile verification

OVF5199 50G SPEED Mode end to end verification
    [Documentation]   OVF5199 50G SPEED Mode end to end verification
    Log to Console    "Start Nitro End to End tests for 50Gb speedmode"

    Set Test Variable	${profilesGroup}	${profiles50}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
#	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Find Server IP addresses
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Server Profile Connectivity With Ping

    Set Test Variable	${profilesGroup}	${profiles50to25}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
#	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Find Server IP addresses
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Server Profile Connectivity With Ping

	Log To Console	\n Finished 50Gb SPEED Mode end to end start

OVF5199 Update from group with QoS changes - No change in LI speed mode
    [Documentation]   OVF5199 Update from group with QoS changes - No change in LI speed mode
# LI is in 50G speedmode
# Edit LIG QoS settings so that LI is inconsistent
# Do UFG, LI is updated with changes except the speedmode and stays at 50G mode

	Log To Console	\n OVF5199 Update from group - No change in speed mode
	#edit LIG to modify uplink set
    ${body} =    Build LIG body    ${edit_ligs['Enc${numFrames}-50G-LIG']['ligBody']}
	${qosConfiguration} =   Get From Dictionary   ${QoS_Fcoe}  qosConfiguration
	Set to dictionary	${body}     qosConfiguration    ${qosConfiguration}
	${uri} =	Get LIG Uri   ${edit_ligs['Enc${numFrames}-50G-LIG']['ligBody']['name']}
    ${resp} =    Fusion Api Edit LIG    ${body}    ${uri}
    ${task} =    Wait For Task    ${resp}    300s    2s
    ${resp}	Fvt Api Get Logical Interconnect Group By Name	${edit_ligs['Enc${numFrames}-50G-LIG']['ligBody']['name']}
    Should Be Equal As Strings	${resp['name']}	${edit_ligs['Enc${numFrames}-50G-LIG']['ligBody']['name']}
    Run Keyword And Continue On Failure	Verify LIG speedmode    ${edit_ligs['Enc${numFrames}-50G-LIG']['ligBody']}    SPEED_25GB
    verify LIG QoS values   ${edit_ligs['Enc${numFrames}-50G-LIG']['ligBody']}    ${QoS_Fcoe['qosConfiguration']}

	Sleep	${ufg_statusdelay}
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['state']}	Inconsistent

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_REDUNDANT_50G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	NOT_CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_50GB

	# LE update from group
	${Resp} =	Update Logical Enclosure from Group     ${les}

	#verify LI and LE consistency status values
	Sleep	${ufg_statusdelay}
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['state']}	Consistent

	#verify LIG downlinkmode is 50G and LI's is 50GB
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_REDUNDANT_50G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_50GB

	Log To Console	\n Finished OVF5199 Update from group - No change in speed mode

OVF5199 SPEED Downgrade 50G to 25G Not Allowed with 50Gb Profile Connections
    [Documentation]   OVF5199 SPEED Downgrade 50G to 25G Not Allowed with 50Gb Profile Connections

	Log To Console	\n OVF5199 SPEED Downgrade 50G to 25G Not Allowed with 50Gb Profile Connections

	Set Suite Variable	${LIName}	${LI_REDUNDANT_50G}

    # verify LI is in 50GB mode
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LIName}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_50GB

    # Edit LI speed to 25Gb. Error case as the profile BW is > 25G
    Edit LI Downlink Speed Mode Downgrade Error    ${LIName}    SPEED_25GB

	Log To Console	\n Finished OVF5199 SPEED Downgrade 50G to 25G Not Allowed with 50Gb Profile Connections

OVF4511 50G to 25G downgrade stop ping sessions for modified profiles before downgrade
    [Documentation]   50G to 25G downgrade stop ping sessions for modified profiles Enc1-Profile3 and Enc2-Profile2
    Log to Console    50G to 25G downgrade stop ping sessions

    Set Test Variable	${profilesGroup}	${edit_profiles_50Gto25G}

	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Delete Profile With Multiple Ping Sessions

	Log To Console	\n Finished OVF5199 SPEED Downgrade from 50G to 25G downgrade stop ping sessions

OVF5199 SPEED Downgrade Change LI mode from 50G to 25G
    [Documentation]    OVF5199 SPEED Downgrade Change LI mode from 50G to 25G

	Log To Console	\n OVF5199 SPEED Downgrade Change LI mode from 50G to 25G

    # Edit profiles
	Log To Console	\n Editing Server Profiles from 50Gb to 25G bandwidth

    Set Suite Variable	${EG}	Enc${numFrames}-50G-EG
    Set Test Variable	${profilesGroup}	${edit_profiles_50Gto25G}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       FVT Edit Server Profile FlexFrames    ${EG}

	Log To Console	\n Edited Server Profiles from 50Gb to 25Gb bandwidth

    # Profile bandwidths are modified to 25Gb. Now Edit LI speed to 25Gb.
    Edit Downlink Speed Mode Of LI    ${LIName}    SPEED_25GB
	Sleep	${ufg_statusdelay}

	#verify LI and LE consistency status values
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LIName}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_25GB

	Log To Console	\n Finished OVF5199 SPEED Downgrade Change LI mode from 50Gb to 25Gb

OVF5199 SPEED Downgrade from 50G to 25G ICM downlink status check
    [Documentation]    OVF5199 SPEED Downgrade from 50G to 25G ICM downlink status check

	Log To Console	\n OVF5199 SPEED Downgrade from 50G to 25G ICM downlink status check

	# Verify ICM status(Configured)
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc1_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay6_icm}    Configured

#   OVD25148 - The test scripts should be changed to have about 4.5 minutes of delay
#   between the ICM going to configured state and checking the interconnect info data.
#    Sleep    5 min  #	${server_efuse_sleeptime}
	Sleep	${server_efuse_sleeptime}

# Enclosure 1 Bay 1 server = index 0 (d1); Enclosure 2 Bay 1 server = index 12 (d13) etc..
# 0 - Enclosure 1 Bay 1 Bronco; 1 - Enclosure 1 Bay 2 Quack; 2 - Enclosure 1 Bay 3 Quagmire;
# 12 - Enclosure 2 Bay 1 Bronco; 21 - Enclosure 2 Bay 10 Quagmire2;

    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc1_QuackSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc1_QuagmireSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc2_QuagmireSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc2_Quagmire2SeverBay}    Linked    Speed25G

    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc1_QuackSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc1_QuagmireSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc2_QuagmireSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc2_Quagmire2SeverBay}    Linked    Speed25G

	Log To Console	\n Finished OVF5199 SPEED Downgrade from 50G to 25G ICM downlink status check

OVF5199 SPEED Downgrade from 50G to 25G verify ILT extra cable alert
    [Documentation]    OVF5199 SPEED Downgrade from 50G to 25G verify ILT extra cable alert

# If LE is created with 25G mode and Synergy frames are with 50G ILT,
# an extra cable alert is logged (LI is being used in 25G ILT topology)

    # The logical interconnect downlink speed mode is configured for 10 Gb/s speed whereas the interconnect link topology is 50 Gb/s compatible.
    # Resolution: Remove the excess interconnect link cable. Alternatively, update the logical interconnect downlink speed mode setting to 25 Gb/s mode.
	Set Suite Variable	${LIName}	${LI_REDUNDANT_50G}
    LI Alert verification    ${LIName}    ${LI_SPEEDMODE_extra2ndILT_ERROR}    ${LI_SPEEDMODE_extra2ndILT_RSLN}

	Log To Console	\n Finished OVF5199 SPEED Downgrade from 50G to 25G verify ILT extra cable alert

OVF5199 SPEED Downgrade from 50G to 25G Profile Status verification
    [Documentation]    OVF5199 SPEED Downgrade from 50G to 25G Profile Status verification

	Log To Console	\n SPEED Downgrade from 50G to 25G Profile Status verification

    # Verify Profile status
    Set Test Variable	${profilesGroup}	${profiles50}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Verify Server Profile status

    Set Test Variable	${profilesGroup}	${profiles50to25}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Verify Server Profile status

	Log To Console	\n Finished SPEED Downgrade from 50G to 25G Profile Status verification

OVF5199 50G SPEED Mode end to end verification for modified profiles after downgrade
    [Documentation]   OVF5199 50G SPEED Mode end to end verification for modified profiles after downgrade
    Log to Console    "Start Nitro End to End tests for profiles that are modified"

    Set Test Variable	${profilesGroup}	${profiles50}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Server Profile Connectivity With Ping

	Log To Console	\n Finished starting Nitro End to End tests for profiles that are modified

OVF4511 50G to 25G downgrade stop ping sessions for unchanged profiles
    [Documentation]   OVF4511 50G to 25G downgrade stop ping sessions for unchanged profiles
    Log to Console    50G to 25G downgrade stop ping sessions

    Set Test Variable	${profilesGroup}	${profiles50to25}

	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Delete Profile With Multiple Ping Sessions

OVF4511 50G to 25G downgrade stop ping sessions for modified profiles
    [Documentation]   OVF4511 50G to 25G downgrade stop ping sessions for modified profiles
    Log to Console    50G to 25G downgrade stop ping sessions

    Set Test Variable	${profilesGroup}	${edit_profiles_50Gto25G}

	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Delete Profile With Multiple Ping Sessions

	Log To Console	\n Finished OVF5199 SPEED Downgrade from 50G to 25G downgrade stop ping sessions

OVF5199 Backup and Restore with LI speedmode change
    [Tags]  BNR
    [Documentation]   OVF5199 Backup and Restore with LI speedmode change

#•	Create LI in 25G mode
#•	Backup OneView
#•	Update LI to 50G mode
#•	Restore OneView from Backup
#•	Verify LI in 25G mode.
#•	Adapters that support 25/50 (Quack) should be linked at those speeds and any adapters that don’t support 25/50 (Bronco) should be unlinked

	Log To Console	\n OVF5199 Backup and Restore with LI speedmode change

#  LI speed mode is at 50G from above test cases
#	sleep   300s

	Set Suite Variable	${LIName}	${LI_REDUNDANT_50G}
    # verify LI is in 25GB mode
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LIName}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_25GB

#    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    LI at SPEED_25GB

#•	Backup OneView
    ${resp}=    Fusion Api Create Backup
    Run Keyword If  ${resp['status_code']} !=202    fail    msg=\nBackup failed. \n ErrorCode:${resp['errorCode']}\n ${resp['message']}
    ${task} =   Wait For Task   ${resp}     10 min    20s
    Run Keyword If  '${task['taskState']}' !='Completed'   or   ${task['status_code']} !=200   fail    msg=\nBackup failed. \n ErrorCode:${task['taskErrors']}\n ${task['taskStatus']}
    ...         ELSE    Log to console  \n\nBackup Created Succesfully !! \n ${task['taskStatus']}

#    Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    After Backup

    # Edit LI speed to 50Gb
    Edit Downlink Speed Mode Of LI    ${LIName}    SPEED_50GB
	sleep   300s

    # verify LI is in 50GB mode
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LIName}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_50GB

    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc1_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay6_icm}    Configured

#   Run Keyword If    ${PAUSE}==${TRUE}    Pause Execution    LI at SPEED_50GB before Restore

#•	Restore OneView from Backup
    Log to console    \nGetting the created Backup and starting the restore operation

    # login to appiance and restore
    Speedmode Suite Setup
    Restore From Backup
    Sleep     2min

    # Appliance is restored. Login again
	Fusion Api Login Appliance	${appliance_ip}	${admin_credentials}

    # verify LI is in 25GB mode
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LIName}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_25GB

    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc1_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay6_icm}    Configured

	Log To Console	\n Finished OVF5199 Backup and Restore with LI speedmode change

OVF5199 Backup and Restore verify ILT extra cable alert
    [Tags]  BNR
    [Documentation]    OVF5199 Backup and Restore verify ILT extra cable alert

# If LE is created with 25G mode and Synergy frames are with 50G ILT,
# an extra cable alert is logged (LI is being used in 25G ILT topology)

    # The logical interconnect downlink speed mode is configured for 10 Gb/s speed whereas the interconnect link topology is 50 Gb/s compatible.
    # Resolution: Remove the excess interconnect link cable. Alternatively, update the logical interconnect downlink speed mode setting to 25 Gb/s mode.
	Set Suite Variable	${LIName}	${LI_REDUNDANT_50G}
    LI Alert verification    ${LIName}    ${LI_SPEEDMODE_extra2ndILT_ERROR}    ${LI_SPEEDMODE_extra2ndILT_RSLN}

	Log To Console	\n Finished OVF5199 Backup and Restore verify ILT extra cable alert

# Profiles after backpup and restore need to be unassigned and reassigned.
# Not part of speedmode testing. Commenting out.
# Note from Profile error after restore:
# If this error is the result of performing a restore from backup,
# unassign then reassign all affected profiles. The process of unassigning all profiles is required to avoid duplicate MAC or WWN addresses in your environment.


OVF5199 25G SPEEDMODE LE with A and B side LIGs
    [Tags]  ABSAMESPEED10
    [Documentation]    OVF5199 25Gb SPEEDMODE LE with A and B side LIGs

	Log To Console	\n OVF5199 25Gb SPEEDMODE LE with A and B side LIGs
    # Create LE from LIGs with 25Gb speed mode.
    # Verify LIs speed mode is set to 25Gb

    Delete Profiles and LE in speedmode    ${LE}

    # EG Enc2-AB-diffSpeed-EG created earlier
    # creating LE
    Log to console	\n Creating LE
	Create Enclosure List for LE Dictionary    ${numFrames}	${numFrames}
	Set To Dictionary	${les}	enclosureGroupUri	EG:Enc${numFrames}-AB-25G-EG
	${task} =	Add Logical Enclosure from variable     ${les}
	Sleep	3 sec

OVF5199 25G SPEEDMODE LE with A and B side LIGs Reapply Configuration
    [Tags]  ABSAMESPEED101
    [Documentation]    OVF5199 25Gb SPEEDMODE LE with A and B side LIGs Reapply Configuration

	#verify LI and LE consistency status values
	Sleep	3 sec
	Sleep	${ufg_statusdelay}
    FVT Reapply LI Configuration    ${LI_A_25G}
    FVT Reapply LI Configuration    ${LI_B_25G}

	Sleep	3 sec

	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
#	Should Be Equal As Strings	${resp['status']}	OK
    Should Match Regexp	${resp['status']}	 ((?i)Warning|OK)
	Should Be Equal As Strings	${resp['state']}	Consistent

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_A_25G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_25GB

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_B_25G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_25GB

	Log To Console	\n Finished OVF5199 Mixed SPEEDMODE LE with A and B side LIGs

OVF5199 25G SPEEDMODE LE with A and B side LIGs ICM downlink status check
    [Documentation]   OVF5199 25G SPEEDMODE LE with A and B side LIGs ICM downlink status check

	Log To Console	\n 25G Happy path A + B mode ICM downlink status check

	# Verify ICM status(Configured)
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc1_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay6_icm}    Configured

#   OVD25148 - The test scripts should be changed to have about 4.5 minutes of delay
#   between the ICM going to configured state and checking the interconnect info data.
#    Sleep    5 min  #	${server_efuse_sleeptime}
	Sleep	${server_efuse_sleeptime}

    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc1_QuackSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc1_QuagmireSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc2_QuagmireSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc2_Quagmire2SeverBay}    Linked    Speed25G

    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc1_QuackSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc1_QuagmireSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc2_QuagmireSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc2_Quagmire2SeverBay}    Linked    Speed25G

	Log To Console	\n Finished OVF5199 NitroME Nitro ICM downlink status check

OVF5199 25G SPEEDMODE LE with A and B side LIGs LI alerts check
    [Documentation]   OVF5199 25G SPEEDMODE LE with A and B side LIGs LI alerts check

    # If LE is created with 25Gb mode and Synergy frames are with 50G ILT,
    # an extra cable alert is logged (LI is being used in 25G ILT topology)

	Log To Console	\n OVF5199 25Gb SPEEDMODE LE with A and B side LIGs LI alerts check

    LI Alert verification    ${LI_A_25G}    ${LI_SPEEDMODE_extra2ndILT_ERROR}    ${LI_SPEEDMODE_extra2ndILT_RSLN}
    LI Alert verification    ${LI_B_25G}    ${LI_SPEEDMODE_extra2ndILT_ERROR}    ${LI_SPEEDMODE_extra2ndILT_RSLN}

	Log To Console	\n Finished OVF5199 25Gb SPEEDMODE LE with A and B side LIGs LI alerts check

OVF5199 25G SPEEDMODE LE with A and B side LIGs Create Server Profiles
    [Documentation]     OVF5199 25Gb SPEEDMODE LE with A and B side LIGs Create Server Profiles
	Set Log Level	TRACE

	Log To Console	\n OVF5199 25Gb SPEEDMODE LE with A and B side LIGs Create Server Profiles

    # change to selective power off
    Power off all servers

	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesAB25}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       FVT Create Server Profile FlexFrames    Enc${numFrames}-AB-25G-EG

    Power on ALL servers

	Log To Console	\n Finished OVF5199 Mixed SPEEDMODE LE A and B side Create Server Profiles

OVF5199 SPEED A and B side LIs Profile Status verification
    [Documentation]   OVF5199 SPEED A and B side LIs Profile Status verification

	Log To Console	\n 50G SPEED Mode REDUNDANT Profile Status verification

    Set Test Variable	${profilesGroup}	${profilesAB25}
    # Verify Profile status
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Verify Server Profile status

	Log To Console	\n Finished 50G SPEED Mode REDUNDANT Profile Status verification

OVF5199 SPEED A and B side LIs start end to end verification
    [Documentation]   Start End to End tests
	Log To Console	\n OVF5199 25G SPEED A and B side LIs start end to end verification

    Set Test Variable	${profilesGroup}	${profilesAB25}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Server Profile Connectivity With Ping

	Log To Console	\n Finished OVF5199 25G SPEED A and B side LIs start end to end verification

OVF5199 SPEED Upgrade Edit A and B side LIs speedmode from 25G to 50G
    [Documentation]     OVF5199 SPEED Upgrade Edit A and B side LIs speedmode from 25G to 50G

	Log To Console	\n OVF5199 SPEED Upgrade Edit A and B side LIs speedmode from 25G to 50G

    # Edit Aside LI speed to 50Gb. LI edit speedmode keyword verifies speedmode value also
    Edit Downlink Speed Mode Of LI    ${LE}-Enc${numFrames}-25G-Aside-LIG    SPEED_50GB
	Sleep	${ufg_statusdelay}

    # Edit Aside LI speed to 50Gb. LI edit speedmode keyword verifies speedmode value also
    Edit Downlink Speed Mode Of LI    ${LE}-Enc${numFrames}-25G-Bside-LIG    SPEED_50GB
	Sleep	${ufg_statusdelay}

    # verify LIs are in 25G mode
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_A_25G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_50GB

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_B_25G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_50GB

    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc1_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay6_icm}    Configured

	Log To Console	\n Finished OVF5199 SPEED Upgrade Edit LI speedmode from 25Gb to 25/50G

OVF5199 SPEED A and B side LIs Profile Status verification after 25Gb to 50Gb speedchange
    [Documentation]   OVF5199 SPEED A and B side LIs Profile Status verification after 25Gb to 50Gb speedchange
	Log To Console	\n 50G SPEED Mode REDUNDANT Profile Status verification

    Set Test Variable	${profilesGroup}	${profilesAB25}
    # Verify Profile status
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Verify Server Profile status

	Log To Console	\n Finished 50G SPEED Mode REDUNDANT Profile Status verification

OVF5199 SPEED A and B side LIs Upgrade from 25G to 50G ILT verify NO extra cable alert
    [Documentation]   OVF5199 SPEED A and B side LIs Upgrade from 25G to 50G ILT verify NO extra cable alert
    # an extra cable alert is cleared for 50Gb speedmode
    # The interconnect link topology is compatible with a logical interconnect downlink speed of 50Gbps.

    LI Alert Cleared verification    ${LI_A_25G}    ${LI_SPEEDMODE_extra2ndILT_ERROR}    ${LI_SPEEDMODE_extra2ndILT_RSLN}
    LI Alert Cleared verification    ${LI_B_25G}    ${LI_SPEEDMODE_extra2ndILT_ERROR}    ${LI_SPEEDMODE_extra2ndILT_RSLN}

OVF5199 SPEED A and B side LIs after 25Gb to 50Gb speedchange Ping Verification
    [Documentation]   Nitro 50G VPLAG End to End tests Verification
    Log to Console    Nitro 50G VPLAG End to End tests Verification

    Set Test Variable	${profilesGroup}	${profiles25}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Delete Profile With Multiple Ping Sessions

	Log To Console	\n Finished Nitro 50G VPLAG End to End tests

OVF5199 SPEED Downgrade from 50G to 25G for AB LIs
    [Documentation]   OVF5199 SPEED Downgrade from 50G to 25G for AB LIs

	Log To Console	\n OVF5199 SPEED Downgrade Change LI mode from 50Gb to 25Gb

    # Edit Aside LI speed to 50Gb. LI edit speedmode keyword verifies speedmode value also
    Edit Downlink Speed Mode Of LI    ${LE}-Enc${numFrames}-25G-Aside-LIG    SPEED_25GB
	Sleep	${ufg_statusdelay}

    # Edit Aside LI speed to 50Gb. LI edit speedmode keyword verifies speedmode value also
    Edit Downlink Speed Mode Of LI    ${LE}-Enc${numFrames}-25G-Bside-LIG    SPEED_25GB
	Sleep	${ufg_statusdelay}

    # verify LIs are in 25G mode
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_A_25G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_25GB

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_B_25G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_25GB

    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc1_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay6_icm}    Configured

    LI Alert verification    ${LI_A_25G}    ${LI_SPEEDMODE_extra2ndILT_ERROR}    ${LI_SPEEDMODE_extra2ndILT_RSLN}
    LI Alert verification    ${LI_B_25G}    ${LI_SPEEDMODE_extra2ndILT_ERROR}    ${LI_SPEEDMODE_extra2ndILT_RSLN}

	Log To Console	\n Finished OVF5199 SPEED Downgrade Change LI mode from 50Gb to 25Gb

OVF5199 SPEED A and B side LIs Profile Status verification after 50Gb to 25Gb speedchange
    [Documentation]   OVF5199 SPEED A and B side LIs Profile Status verification after 50Gb to 25Gb speedchange

	Log To Console	\n Profile Status verification after 50Gb to 25Gb speedchange

    Set Test Variable	${profilesGroup}	${profilesAB25}
    # Verify Profile status
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Verify Server Profile status

	Log To Console	\n Finished Profile Status verification after 50Gb to 25Gb speedchange

OVF5199 SPEED A and B side LIs Ping verification after 50Gb to 25Gb speedchange
    [Documentation]   stop end to End tests Verification
    Log to Console    OVF5199 25G SPEED A and B side LIs stop end to end verification

    Set Test Variable	${profilesGroup}	${profilesAB25}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Delete Profile With Multiple Ping Sessions

	Log To Console	\n Finished OVF5199 25G SPEED A and B side LIs stop end to end verification

OVF5199 50G SPEEDMODE LE with A and B side LIGs
    [Tags]  AB50
    [Documentation]    OVF5199 50Gb SPEEDMODE LE with Aside and Bside LIGs

	Log To Console	\n OVF5199 50Gb SPEEDMODE LE with Aside and Bside LIGs

    Delete Profiles and LE in speedmode    ${LE}

    # creating LE
    Log to console	\n Creating LE
	Create Enclosure List for LE Dictionary    ${numFrames}	${numFrames}
	Set To Dictionary	${les}	enclosureGroupUri	EG:Enc${numFrames}-AB-50G-EG
	${task} =	Add Logical Enclosure from variable     ${les}
	Sleep	3 sec

	#verify LI and LE consistency status values
	Sleep	3 sec
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc1_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc3_bay6_icm}    Configured

	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
#	Should Be Equal As Strings	${resp['status']}	OK
    Should Match Regexp	${resp['status']}	 ((?i)Warning|OK)
	Should Be Equal As Strings	${resp['state']}	Consistent

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_A_50G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_50GB

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_B_50G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_50GB

	Log To Console	\n Finished OVF5199 Same SPEEDMODE LE with Aside and Bside LIGs

OVF5199 50G SPEEDMODE LE with A and B side LIGs Reapply Configuration
    [Tags]  AB50REAP
    [Documentation]    OVF5199 50G SPEEDMODE LE with A and B side LIGs Reapply Configuration

	#verify LI and LE consistency status values
	Sleep	3 sec
	Sleep	${ufg_statusdelay}
    FVT Reapply LI Configuration    ${LI_A_50G}
    FVT Reapply LI Configuration    ${LI_B_50G}

	Sleep	3 sec

	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
#	Should Be Equal As Strings	${resp['status']}	OK
    Should Match Regexp	${resp['status']}	 ((?i)Warning|OK)
	Should Be Equal As Strings	${resp['state']}	Consistent

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_A_50G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_50GB

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_B_50G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_50GB

	Log To Console	\n Finished OVF5199 Mixed SPEEDMODE LE with A and B side LIGs

