*** Settings ***
Documentation		OVF4511 Nitro ME 50Gb VPLAG Test cases
...                 SuiteName: OVF4511-50Gb-vplags

...					Usage (Nitro Integration Rig Multi Frame configuration):
...					pybot -d /tmp/logs/OVF4511-50G-vplags -T -V data-OVF4511-50Gb-vplags-NitroIntRig.py -v APPLIANCE_IP:15.245.131.251 -v max:3 OVF4511-50G-vplags-TestCases.robot

Library			FusionLibrary
Library			RoboGalaxyLibrary
Variables		data-OVF4511-50Gb-vplags-NitroIntRig.py

Resource            ../FVT/speedmode-keywords.txt
Resource            ../../../../../Resources/api/fusion_api_resource.txt

Library			json
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
${APPLIANCE_IP}		15.186.9.146
${numFrames}    3
${TESTSETUP}    ${False}
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

# Enclosure 1 Bay 1 server = index 0 (d1); Enclosure 2 Bay 1 server = index 12 (d13) etc..
# 0 - Enclosure 1 Bay 1 Bronco; 1 - Enclosure 1 Bay 2 Quack; 2 - Enclosure 1 Bay 3 Quagmire;
# 14 - Enclosure 2 Bay 3 Quagmire; 21 - Enclosure 2 Bay 10 Quagmire2;

${enc1_QuagmireSeverBay}               0
${enc1_QuackSeverBay}               1
${enc1_Quagmire2SeverBay}               2
${enc2_QuagmireSeverBay}               12
${enc2_Quagmire2SeverBay}               14
${enc3_QuagmireSeverBay}               24
${enc3_Quagmire2SeverBay}               26

${FUSION_IP}					${APPLIANCE_IP}
${SKIPTEARDOWN}                 ${True}

*** Test Cases ***
OVF4511 Create LIGs with 50G speed mode and verify downlinkSpeedMode 50G
    [Tags]  PRECONFIG
    [Documentation]    Create LIGs for OVF4511 test cases

    # create 50G LIGs
	Log To Console	\n Create LIG with 50G speedmode

    ${ligs} =     Evaluate  {k: v for k, v in ${ligs_50G}.iteritems() if 'Enc${numFrames}' in k}
    Run Keyword If	${ligs} is not ${null}	Run Keyword for Dict	    ${ligs}       Add LIG from variable
    Run Keyword If	${ligs} is not ${null}	Run Keyword for Dict	    ${ligs}       Verify LIG speedmode    SPEED_50GB

	Log To Console	\n Finished Create LIG with 50G speedmode

OVF4511 Create EGs using 50G LIGs
    [Tags]  PRECONFIG
    [Documentation]    Create EGs for OVF4511 test cases

	Log To Console	\n Create EGs

    ${egs} =     Evaluate  {k: v for k, v in ${enc_group}.iteritems() if 'Enc${numFrames}' in k}
    Run Keyword for Dict    ${egs}    Add Enclosure Group and Verify

	Log To Console	\n Finished Creating EGs

OVF4511 Create 50G LE
    [Tags]  PRECONFIG
    [Documentation]    LE setup for OVF4511 test cases

    Log to console	\n Creating LE
	Create Enclosure List for LE Dictionary    ${numFrames}	${numFrames}
	Set To Dictionary	${les}	enclosureGroupUri	EG:Enc${numFrames}-50G-EG
	${task} =	Add Logical Enclosure from variable     ${les}
	Sleep	3 sec

	# Verify ICM status(Configured)
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured

    # Verify LI and LE consistency status values
	${resp}	Fvt Api Get Logical Enclosure By Name	${LE}
    Should Match Regexp	${resp['status']}	 ((?i)Warning|OK)
	Should Be Equal As Strings	${resp['state']}	Consistent

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_50G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_50GB

	Log To Console	\n Finished Creating 50Gb LE

OVF4511 50G Happy path mode ICM downlink status check
    [Documentation]    Verify downlinks after LE create

	Log To Console	\n 50Gb Happy path mode ICM downlink status check

	# Verify ICM status(Configured)
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured

#   OVD25148 - The test scripts should be changed to have about 4.5 minutes of delay
#   between the ICM going to configured state and checking the interconnect info data.
#    Sleep    5 min  #	${server_efuse_sleeptime}
	Sleep	${server_efuse_sleeptime}

# Enclosure 1 Bay 1 server = index 0 (d1); Enclosure 2 Bay 1 server = index 12 (d13) etc..
# 0 - Enclosure 1 Bay 1 Bronco; 1 - Enclosure 1 Bay 2 Quack; 2 - Enclosure 1 Bay 3 Quagmire;
# 12 - Enclosure 2 Bay 1 Bronco; 20 - Enclosure 2 Bay 9 Quagmire2;

    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc1_QuackSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc1_QuagmireSeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc1_Quagmire2SeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc2_QuagmireSeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc2_Quagmire2SeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc3_QuagmireSeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc1_bay3_icm}    ${enc3_Quagmire2SeverBay}    Linked    Speed50G

    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc1_QuackSeverBay}    Linked    Speed25G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc1_QuagmireSeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc1_Quagmire2SeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc2_QuagmireSeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc2_Quagmire2SeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc3_QuagmireSeverBay}    Linked    Speed50G
    FVT Check Interconnect Downlink Speed    ${enc2_bay6_icm}    ${enc3_Quagmire2SeverBay}    Linked    Speed50G

	Log To Console	\n Finished OVF1811 NitroME Nitro ICM downlink status check

OVF4511 50G SPEED Mode Create Server Profiles
    [Documentation]    Create Server Profiles after LE create in 50Gb mode

	Log To Console	\n Creating Server Profiles for 10Gb speedmode

    # change to selective power off
    Power off all servers    PressAndHold

    Set Test Variable	${profilesGroup}	${profilesVPLAG}
    Set Suite Variable	${EG}	Enc${numFrames}-50G-EG
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       FVT Create Server Profile FlexFrames    ${EG}

	Log To Console	\n Finished Creating Profiles for LI 10G mode

OVF4511 50G SPEED Mode Profile Status verification
    [Documentation]    Profile status verification after LE and profile creation

	Log To Console	\n 50G SPEED Mode Profile Status verification

    Set Test Variable	${profilesGroup}	${profilesVPLAG}
    # Verify Profile status
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Verify Server Profile status

	Log To Console	\n Finished 50G SPEED Mode Profile Status verification

OVF4511 50G SPEED Mode end to end verification
    [Documentation]   Start End to End tests
    Log to Console    "Nitro End to End tests"

    Set Test Variable	${profilesGroup}	${profilesVPLAG}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Server Profile Connectivity With Ping

OVF4511 50G SPEED Mode Remove and insert back Nitro ICM
    [Documentation]   OVF4511 50G SPEED Mode Remove and insert back Nitro ICM

    # Remove and insert back Nitro ICM

	Log To Console	\n Remove and add Nitro ICM

	# Verify ICM status(Configured)
    LCLKW Check Interconnect State    ${enc1_bay3_icm}    Configured
    LCLKW Check Interconnect State    ${enc2_bay6_icm}    Configured

    # Enclosure 1 bAY 3 (MXQ81804ZF, interconnect 3)
    ${uri} =    Get IC URI      ${ENC_1}, interconnect 3

    # Remove Potash from Enclosure 1 bay 3 which is part of LI
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

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI_50G}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
	Should Be Equal As Strings	${resp['downlinkSpeedMode']}	SPEED_50GB

	Log To Console	\n Finished removing and adding Nitro ICM

OVF4511 50G SPEED Mode Nitro ICM rip and replace Profile Status verification
    [Documentation]    Profile status verification after Nitro remove and add

	Log To Console	\n 50G SPEED Mode Nitro ICM rip and replace Profile Status verification

    Set Test Variable	${profilesGroup}	${profilesVPLAG}
    # Verify Profile status
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Verify Server Profile status

	Log To Console	\n Finished 50G SPEED Mode Nitro ICM rip and replace Profile Status verification

OVF4511 50G Nitro ICM rip and replace end to end tests
    [Documentation]   Nitro 50G VPLAG End to End tests Verification
    Log to Console    Nitro 50G VPLAG End to End tests Verification

    # temporary. remove
	Sleep	${efuse_sleeptime}

    Set Test Variable	${profilesGroup}	${profilesVPLAG}
	:FOR	${x}	IN RANGE	1	${numFrames}+1
	\   ${profiles} =     Evaluate  {k: v for k, v in ${profilesGroup}.iteritems() if 'Enc${x}' in k}
	\   Run Keyword If	${profiles} is not ${null}	Run Keyword for Dict	    ${profiles}       Delete Profile With Multiple Ping Sessions

	Log To Console	\n Finished Nitro 50G VPLAG End to End tests

