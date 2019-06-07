*** Settings ***
Documentation   Feature Test: F108 Switch Life Cycle Management SLM tests
...					Usage:
...					Note: update Enclosure serial #s in data_common.py file and run following command
...					AR51 ME: pybot -d logs -T -V cl10_data.py -v frame:3 -v APPLIANCE_IP:15.245.131.12 F108-SLM.robot

Variables       ../data_F108_common.py
Variables       ./cl10_data.py

Resource        ../../../../../../Resources/api/fusion_api_resource.txt
Resource        ../../FVT/fvt-keywords.txt
Resource		../../FVT/Resources/fvt_resource.txt

Library			FusionLibrary
Library			../../FVT/fvt_api.py

Suite Setup			Login User
Suite Teardown		Teardown

*** Variables ***
${efuse_sleeptime}    120
${sleeptime_potashAdd}    2400
${frame}	3

${LIG}	Enc3-LIG
${EG}	Enc3-EG
${LE}	Enc3-LE
${LI}	Enc3-LE-Enc3-LIG
${LI_uri}	None

${FUSION_IP}					${APPLIANCE_IP}

${bay2}               2
${bay3}               3
${bay6}               6

${enc1_bay2_icm}	${ENC_1}, interconnect 2
${enc1_bay5_icm}	${ENC_1}, interconnect 5
${enc2_bay2_icm}	${ENC_2}, interconnect 2
${enc2_bay5_icm}	${ENC_2}, interconnect 5
${enc3_bay2_icm}	${ENC_3}, interconnect 2
${enc3_bay5_icm}	${ENC_3}, interconnect 5

${enc1_bay3_icm}	${ENC_1}, interconnect 3
${enc1_bay6_icm}	${ENC_1}, interconnect 6
${enc2_bay3_icm}	${ENC_2}, interconnect 3
${enc2_bay6_icm}	${ENC_2}, interconnect 6
${enc3_bay3_icm}	${ENC_3}, interconnect 3
${enc3_bay6_icm}	${ENC_3}, interconnect 6

${ICM_MODEL}                    Virtual Connect SE 40Gb F8 Module for Synergy
${ICM_MODEL_CL}                 Synergy 10Gb Interconnect Link Module


*** Keywords ***
Login User
    [Documentation]    Common login and setting variables for test cases
	Set Log Level	TRACE
	Fusion Api Login Appliance	${appliance_ip}	${admin_credentials}
	Set Suite Variable	${LIG}	Enc${frame}-LIG
	Set Suite Variable	${EG}	Enc${frame}-EG
	Set Suite Variable	${LE}	Enc${frame}-LE
	Set Suite Variable	${LI}	${LE}-${LIG}

Teardown
    [Documentation]    Common applaince cleanup tasks after test case run is complete
	Set Log Level	TRACE
	Log to console and logfile	[TEARDOWN]
    Remove All LEs
	Remove ALL Enclosure Groups
	Remove ALL LIGs
    Remove All Network Sets
	Remove ALL Ethernet Networks
	Remove ALL FCoE Networks
	Remove ALL Users

Create LIG
	[Documentation]	Create LIG
	[Arguments]		${lig}	${timeout}=3 m	${interval}=1 m

	${resp} =	Add LIG from variable	${lig}

	${resp}	Fvt Api Get Logical Interconnect Group By Name	${lig['name']}
	Should Be Equal As Strings	${resp['name']}	${lig['name']}

Create EG
	[Documentation]	Create EG
	[Arguments]		${eg}	${timeout}=3 m	${interval}=1 m
	${resp} =	Add Enclosure Group from variable	${eg}

	${resp}	Fvt Api Get Enclosure Group By Name	${eg['name']}

	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['name']}	${eg['name']}

Create LE
	[Documentation]	Create LE
	[Arguments]		${le}	${timeout}=60 m	${interval}=1 m
	${resp} =	Add Logical Enclosure from variable	${le}

	${resp}	Fvt Api Get Logical Enclosure By Name	${le['name']}

	Should Be Equal As Strings	${resp['name']}	${le['name']}
	Should Match Regexp	${resp['status']}	((?i)Warning|OK)

FVT Initialize Globals
    [Documentation]    Initialize global variables depending on Frame count
	[Arguments]	${frame}
	Set Global Variable	${LIG}	Enc${frame}-LIG
	Set Global Variable	${EG}	Enc${frame}-EG
	Set Global Variable	${LE}	Enc${frame}-LE
	Set Global Variable	${LI}	Enc${frame}-LI

FVT ICM Efuse
    [Documentation]    Interconnect Efuse keyword
	[Arguments]	${enc}	${bay}	${onOff}
	Get EM IP	${enc}
	Get EM Token	${enc}
	Efuse ICM	EFuse${onOff}	${bay}
	
FVT All ICM Efuse
    [Documentation]    Efuse keyword for all Interconnects in the configuration
	[Arguments]	${frame}	${bay}	${icmstate}
	:FOR    ${x}   IN RANGE	${frame}+1
	\    FVT ICM Efuse    $(enc${x})    ${bay}    ${icmstate}

FVT Check Interconnect State
    [Documentation]    Verify Interconnect state
	[Arguments]	${enc_bay_icm}	${icm_state}

#    ${resp} =	Fvt Api Get Interconnect By Name	${enc_bay_icm}
#    Should Be Equal As Strings    ${resp['state']}    ${icm_state}
    ${resp}=    Fusion Api Get Interconnect   param=?filter="'name'=='${enc_bay_icm}'"
    Should Be Equal As Strings    ${resp['members'][0]['state']}    ${icm_state}

FVT Edit LIG
    [Documentation]    Edit LIG
	[Arguments]	${lig_body}   ${LIG_URI}
	${body} =	Build LIG body	${lig_body}

	${resp} =	Fusion Api Edit Lig	body=${body}	uri=${LIG_URI}
	${task} =	Wait For Task	${resp}	5 min	15s

FVT LI Update From Group
    [Documentation]    LI update from group
	[Arguments]	${LI}
	${li_uri} =   Get LI URI  	${LI}

	${resp} =   Fusion Api Update From Group	${LI_URI}
	Should Be Equal As Integers	${resp['status_code']}	202
	${task} =	Wait For Task	${resp}	50 min	15s
	Sleep	5m

F108 SLM ICM Absent
    [Documentation]    efuse IBS3 ICMs to absent
	[Tags]  ABSENT
	Set Log Level	TRACE
	Fusion Api Login Appliance	${APPLIANCE_IP}	${admin_credentials}
	FVT Check Interconnect State	${frame}	3	Configured
#	FVT All ICM Efuse	${frame}    3     On
#   FVT ICM Efuse    $(enc${x})    ${bay}    ${icmstate}
    FVT ICM Efuse    $(enc2)    6    On
    FVT ICM Efuse    $(enc3)    3    On
	FVT Check Interconnect State	${frame}	6	Absent
	FVT Check Interconnect State	${frame}	3	Absent
#	FVT All ICM Efuse	${frame}    3    Off
    FVT ICM Efuse    $(enc2)    6    Off
    FVT ICM Efuse    $(enc3)    3    Off
	FVT Check Interconnect State	${frame}	3	Configured

F108 SLM Clean Up
    [Documentation]    cleanup keyword for SLM tests
    # delete LE
	FVT Delete Logical Enclosure    ${LE}
	${resp}               Fvt Api Get Logical Enclosure BY Name       ${LE}
	Should Be Equal As Strings          ${resp}  None

	FVT Delete Enclosure Group       ${EG}
	${resp}               Fvt Api Get Enclosure Group BY Name       ${EG}
	Should Be Equal As Strings          ${resp}  None

	FVT Delete Logical Interconnect Group  ${LIG}
	${resp}               Fvt Api Get Logical Interconnect Group BY Name  ${LIG}
	Should Be Equal As Strings          ${resp}  None

	Pass Execution   "Finished F108 Switch Life Cycle Testing"


*** Test Cases ***
F108 SLM Create Ethernet Networks
    [Documentation]    Create Ethernet networks for SLM tests
    [Tags]  SETUP
	Create Ethernet Networks	 ${ethernet_networks}

F108 SLM ICMs in Monitored state
    [Documentation]    Verify ICMs in Monitored state
    [Tags]  ICMmonitor
	# Verify Monitored state of the ICMs that will be used in SLM tests
	FVT Check Interconnect State    ${enc1_bay3_icm}    Monitored
    FVT Check Interconnect State    ${enc1_bay2_icm}    Monitored
	FVT Check Interconnect State    ${enc3_bay6_icm}    Monitored
	FVT Check Interconnect State    ${enc3_bay2_icm}    Monitored

F108 SLM create LIG EG LE
    [Documentation]    Create LIG, EG and LE for SLM tests
    [Tags]  LEsetup
	Create LIG	${ligs['Enc${frame}-LIG']}
	Create LIG	${ligs['Enc${frame}-IBS2-Aside-LIG']}
	Create LIG	${ligs['Enc${frame}-IBS2-Bside-LIG']}
	Create EG	${enc_groups['${EG}']}
	Create LE	${les['${LE}']}

F108 Efuse Remove Chloride from HA LI
    [Documentation]    Remove chloride ICM from a HA LI
    Get EM IP     ${ENC_3}
    Get EM Token  ${ENC_3}
    Efuse ICM   EFuseOn     ${bay6}
    sleep       ${efuse_sleeptime}
	FVT Check Interconnect State    ${enc3_bay6_icm}    Absent

F108 Efuse Remove Chloride from A side LI
    [Documentation]    Remove chloride ICM from an A-side LI
    Get EM IP     ${ENC_3}
    Get EM Token  ${ENC_3}
    Efuse ICM   EFuseOn     ${bay2}
    sleep       ${efuse_sleeptime}
	FVT Check Interconnect State    ${enc3_bay2_icm}    Absent

F108 Efuse Add Chloride from HA LI
    [Documentation]    Add chloride ICM to a HA LI
    Get EM IP      ${ENC_3}
    Get EM Token    ${ENC_3}
    Efuse ICM   EFuseOff     ${bay6}
    sleep       ${efuse_sleeptime}
    FVT Check Interconnect State    ${enc3_bay6_icm}    Configured

F108 Efuse Add Chloride from A side LI
    [Documentation]    Add chloride ICM to an A-side LI
    Get EM IP     ${ENC_3}
    Get EM Token  ${ENC_3}
    Efuse ICM   EFuseOff    ${bay2}
    sleep       ${efuse_sleeptime}
    FVT Check Interconnect State	${enc3_bay2_icm}    Configured

F108 Efuse Remove Potash ICM from HA LI
    [Documentation]    Remove Potash ICM from a HA LI
    # Remove Potash from Enclosure 1 bay 3 which is part of HA LI
    Get EM IP      ${ENC_1}
    Get EM Token    ${ENC_1}
    Efuse ICM   EFuseOn     ${bay3}
    sleep       ${efuse_sleeptime}
    FVT Check Interconnect State	${enc1_bay3_icm}    Absent

F108 Efuse Add Potash ICM from HA LI
    [Documentation]    Add Potash ICM back to a HA LI
    # Add Potash to Enclosure 1 bay 3 which is part of HA LI
    Get EM IP      ${ENC_1}
    Get EM Token    ${ENC_1}
    Efuse ICM   EFuseOff     ${bay3}
    sleep       ${efuse_sleeptime}
    sleep       ${sleeptime_potashAdd}
    FVT Check Interconnect State	${enc1_bay3_icm}    Configured

F108 Efuse Remove Potash ICM from A side LI
    [Documentation]    Remove Potash ICM from an A-side LI
    # Remove Potash from Enclosure 1 bay 2 which is part of A side LI
    Get EM IP      ${ENC_1}
    Get EM Token    ${ENC_1}
    Efuse ICM   EFuseOn     ${bay2}
    sleep       ${efuse_sleeptime}
    FVT Check Interconnect State	${enc1_bay2_icm}    Absent

F108 Efuse Add Potash ICM from A side LI
    [Documentation]    Add Potash ICM back to an A-side LI
    # Add Potash to Enclosure 1 bay 2 which is part of A side LI
    Get EM IP      ${ENC_1}
    Get EM Token    ${ENC_1}
    Efuse ICM   EFuseOff    ${bay2}
    sleep       ${efuse_sleeptime}
    sleep       ${sleeptime_potashAdd}
    FVT Check Interconnect State	${enc1_bay2_icm}    Configured

F108 SLM ICM unmanaged
    [Documentation]    Test case for SLM ICM Unmanaged state
	[Tags]  UNMANAGED
	Set Log Level	TRACE

	### Edit LIG so it has CL10 in place of CL20. Needed to simulate Unmanaged state.
	# Edit LIG in use from unmanaged_ligs dictionary
    ${lig_uri} =    Get LIG Uri   ${LIG}
    FVT Edit LIG   ${unmanaged_ligs['${LIG}']}   ${LIG_URI}

	FVT LI Update From Group   ${LI}

	### Edit LIG so it has all the right interconnects ###
    ${lig_uri} =    Get LIG Uri   ${LIG}
    FVT Edit LIG    ${ligs['${LIG}']}    ${LIG_URI}

	FVT LI Update From Group    ${LI}
