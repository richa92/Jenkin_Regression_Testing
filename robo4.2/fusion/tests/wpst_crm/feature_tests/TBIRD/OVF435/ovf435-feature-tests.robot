*** Settings ***
Documentation		Feature Test: OVF435 Mini-scale ME Feature tests for TClass
...					Usage:
...						MiniScale ME: pybot -V data_variables.py -v APPLIANCE_IP:16.125.70.221 -v dcs:false ovf435-feature-tests.robot

Resource        ../../../../../Resources/api/fusion_api_resource.txt
#Resource        ../../../../resource/fusion_api_all_resource_files.txt
#Resource        ../FVT/fvt-keywords.txt
#Resource		../FVT/Resources/fvt_resource.txt

Library			json
Library			RoboGalaxyLibrary
Library			FusionLibrary
Library	        ../FVT/fvt_api.py

Library         Dialogs
Library			Collections
Library         OperatingSystem
Library         Process
#Library         ServerOperations
#Library			decrypt_dump.py

# setup before test run
Suite Setup   	Fusion Api Login Appliance     ${APPLIANCE_IP}		${admin_credentials}

#Suite Setup    Test Specific setup
#Suite Setup    Run FTS and test-specific setup

# cleanup after test run
#Suite Teardown		Teardown

*** Variables ***
${VM}
${SSH_USER}                     root
${SSH_PASS}                     hpvse1

${FUSION_IP}					${APPLIANCE_IP}

${ICM_MODEL}                    Virtual Connect SE 40Gb F8 Module for Synergy
${ICM_MODEL_CL}                 Synergy 10Gb Interconnect Link Module

*** Test Cases ***
tss
    [Tags]    tss
    Test Specific setup

temp setup
    [Tags]    temp
    Set Log Level	TRACE

	${spts} =	    Get Variable Value	${spts}
	${resplist} =   Run Keyword If	${spts} is not ${null}   Run Keyword for Dict    ${spts}   Add Server Profile Template
	${resp} =       Run Keyword for List   ${resplist}   Wait for Task

temp setup2
    [Tags]    temp2
	Set Log Level	TRACE

	${sp_from_spts} =	Get Variable Value	${sp_from_spts}
	#Run Keyword If	${sp_from_spts} is not ${null}   Run Keyword for Dict    ${sp_from_spts}   Create SP from SPT
	${items} =    Get Dictionary Items    ${sp_from_spts}
	:FOR	${key}   ${value}	IN 	@{items}
	\	Run Keyword		Create SP from SPT    ${key}   ${value}

    #${resp} =    Create SP from SPT    SPT_EG_SY_480_Gen9_1   NewProfileName

OVF435 Verify Discovery and monitored states
    [Documentation]    verify Enclosure discovery and monitored state of devices
    [Tags]     TC1
    [Setup]    Run Keyword and Ignore Error    Write To ciDebug Log
    Log   verifying Monitored state of ICMs and Servers   console=True
	Fusion Api Login Appliance     ${APPLIANCE_IP}		${admin_credentials}
    Verify All Interconnects
    Verify Monitored Server Hardware
	[Teardown]   Get errors

OVF435 Create LIGs EGs LEs and check LE LI status
    [Documentation]    Create LIGs, EGs and LEs and then check that the status is correct
	[Tags]     TC2
    [Setup]    Run Keyword and Ignore Error    Write To ciDebug Log
   	${sas_ligs} =	  Get Variable Value	${sas_ligs}
	Run Keyword If	${sas_ligs} is not ${null}	Run Keyword for Dict	${sas_ligs}   Add SAS LIG
   	${ligs} =	      Get Variable Value	${ligs}
	Run Keyword If	${ligs} is not ${null}	Run Keyword for Dict	    ${ligs}       Add LIG from variable
	${enc_groups} =   Get Variable Value	${enc_groups}
	Run Keyword If	${enc_groups} is not ${null}	Run Keyword for Dict	${enc_groups}	Add Enclosure Group from variable
	${les} =	      Get Variable Value	${les}
    ${task} =   Add Logical Enclosure from variable     ${les['${LE1}']}
    ${task_state} =   Get From dictionary 	${task}     taskState
    Should Match Regexp	${task_state}	 ((?i)Warning|Completed)
    ${resp} =  	Fusion Api Get Logical Enclosure 	param=?filter="'name'=='${LE1}'"
	${resp} =         Get From List   ${resp['members']}	0
    Should Be Equal As Strings	${resp['status']}	OK
    Should Be Equal As Strings	${resp['state']}	Consistent
    ${lis} =    fusion api get li
    :FOR   ${li}   IN   @{lis['members']}
    \   Should Be Equal As Strings   ${li['consistencyStatus}   CONSISTENT
    #TODO: uncomment below!
	#[Teardown]   Get errors

OVF435 TC3 UFG without Profiles
    [Documentation]    TC3 UFG from ICM Base to uplink sets
	[Tags]    TC3   UFG0    UFG
#3	Update from Group
#	Update LIGs with Network and ICM port changes
#	Bring managed resources to compliance with LE/LI Update from group actions
#	Verify health status of updated resources

    # LIG reference for UFG ufg_ligs[0]
	### Edit LIG to add uplink sets
    log to console and logfile   Editing LIG ${LIG3}
    ${lig_uri} =    Get LIG Uri   ${LIG3}
    FVT Edit LIG   ${ufg_ligs[0]}   ${lig_uri}

    log to console and logfile   LI status for ${LI}
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	Should Be Equal As Strings	${resp['consistencyStatus']}	NOT_CONSISTENT

    # LI update from group
    log to console and logfile   LI Update from Group ${LI}
    FVT LI Update From Group   ${LI}

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
    log to console and logfile   [OVF435: Test Case 3: UFG without Profiles. END]

OVF435 TC4 Add Server Profiles
    [Documentation]   TC4   Add server profiles
	[Tags]    CONFIGURE   PROFILES   TC4
#4	Connectivity and Storage
#	Ethernet connectivity (including Untagged and Tunnel networks)
#	FC and/or FCoE connectivity
#	Server Profiles are created and volumes attached
#o	First server profile
#o	Add last server profile when 140 connections are already deployed

    log to console and logfile   \n[OVF435: Test Case 4: Create Profiles. START]
#    Power Off All Servers

#Add Server Profiles No Hardware Assigned
#    log to console and logfile   Create Server Profile Templates
#    ${server_profiles} =	Get Variable Value	${add_server_profiles}
# 	Run Keyword If	${server_profiles} is not ${null}		Add Server Profiles from variable no hardware	${server_profiles}   ${server_profile_to_bay_map}

#Assign Server Hardware To Profile
    log to console and logfile   Assign hardware to Server Profile Templates
    ${server_profiles} =	Get Variable Value	${add_server_profiles}
 	Run Keyword If	${server_profiles} is not ${null}		Assign Server Hardware To Existing Profiles From Variable	${server_profiles}   ${server_profile_to_bay_map}   waitForTask=${True}

# Verify Profile status
#	${resp}	Fvt Api Get Logical Interconnect BY Name	${server_profiles}
#	Should Be Equal As Strings	${resp['Status']}	OK


#OVF435 TC4 end to end test
#    Run Keyword for List	${servers}	Power on Server
#	log to console and logfile  	Waiting 20 minutes for servers to boot...
#    Sleep   20min
#    Run Keyword for List    ${PING_LIST_1}   Wait For Appliance To Become Pingable

    log to console and logfile   \n[OVF435: Test Case 4: Create Profiles. END]

OVF435 TC5 CRM Resource changes
    [Documentation]    TC5 CRM resource tests
	[Tags]    CONFIGURE    CRM    TC5
#5	CRM updates
#	Modify an existing Ethernet/FCoE/FC network that is in use
#	Modify ICM uplink set ports
#	Verify change completed in a reasonable amount of time
#	Verify health status of updated resources
#	Verify profile connectivity

    LI update    2    ${LIG3}

OVF435 TC6 UFG with Profiles
    [Documentation]    TC6 UFG from a set of uplink sets to a different set of uplink sets
	[Tags]    CONFIGURE    UFG1    UFGSP    TC6
#6	Update from Group with Server Profile connections
#	Update LIGs with Network and ICM port changes
#	Bring managed resources to compliance with LE/LI Update from group actions
#	Verify change completed in a reasonable amount of time
#	Verify health status of updated resources
#	Verify profile connectivity

    log to console and logfile   [OVF435: Test Case 6: UFG with Profiles. START]

    # LIG reference for UFG ufg_ligs[0]
	### Edit LIG to add uplink sets
    log to console and logfile   Editing LIG ${LIG3}
    ${lig_uri} =    Get LIG Uri   ${LIG3}
    # UFG arguments - data file reference index and LIG Name
    FVT Edit LIG   ${ufg_ligs[2]}   ${lig_uri}

    log to console and logfile   LI status for ${LI}
	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	Should Be Equal As Strings	${resp['consistencyStatus']}	NOT_CONSISTENT

    # LI update from group
    log to console and logfile   LI Update from Group ${LI}
    FVT LI Update From Group   ${LI}

	${resp}	Fvt Api Get Logical Interconnect BY Name	${LI}
	Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
    log to console and logfile   [OVF435: Test Case 6: UFG with Profiles. END]

OVF435 TC7 Server Profile changes
	[Tags]    SPCHK     TC7
#7	Update Server profiles
#	Make changes to server profile (adding connections) and verify connectivity
#	Also verify change completed in a reasonable amount of time
	Set Log Level	TRACE
	Fusion Api Login Appliance	${APPLIANCE_IP}	${admin_credentials}
    Scale Initialize Globals    ${dcs}    ${frame}

    Run Keyword If    '${dcs}' == 'true'    DCS verify all profiles
    ...    ELSE    HW verify all profiles
# Edit Server Profiles
    log to console and logfile   Assign hardware to Server Profile Templates
    ${server_profiles} =	Get Variable Value	${edit_server_profiles}
    # Edit server profiles
 	Run Keyword If	${server_profiles} is not ${null}		Assign Server Hardware To Existing Profiles From Variable	${server_profiles}   ${server_profile_to_bay_map}   waitForTask=${True}

# Verify Profile status
#	${resp}	Fvt Api Get Logical Interconnect BY Name	${server_profiles}
#	Should Be Equal As Strings	${resp['Status']}	OK

OVF435 TC8 miniscale ICM life cycle
    [Documentation]    TC8 Potash Switch life cycle
	[Tags]    SLM
#8	Remove and add ICMs in mini-scale environment
#	Server profile connectivity is restored without errors

# remove and add ICM for each ring
# Ring#, Enclosure#, ICM bay#
    #:FOR    ${x}    IN RANGE    1   ${numLEs}+1
    #\    Efuse Remove HA LI Potash ICM    ${x}    1    3
    #\    Sleep   2sec
    #\    Efuse Add HA LI Potash ICM    ${x}    1    3

OVF435 TC9 collect supportdump
    [Documentation]    TC9 collect support dump in mini-scale environment
	[Tags]    supportdump     TC9
#9	support dump in mini-scale environment

    #Create Directory      ${dump_file_path}
    #FVT LE supportdump

OVF435 TC10 miniscale CIC reboot
    [Documentation]    TC10 reboot
	[Tags]    reboot    TC10
#10	Reboot Appliance in mini-scale environment
#	Appliance back with configured resources

    ${resp} =   Fusion Api Appliance Shutdown  mode=REBOOT
    ${taskResp} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=30m
    Sleep  ${REBOOT_WAIT_TIME}
# TBD - verify configured state of ICMs

OVF435 TC11 Remove mini-scale config
    [Documentation]    TC11 remove mini-scale configuration
	[Tags]    CLEANUP     TC11
#11	Remove managed and configured OneView resources
#	All ICMs and Servers are back in Monitored state

    Teardown
# Verify all ICMs are discovered without any ILT errors in mini-scale configuration
    Verify All Interconnects
    Verify Monitored Server Hardware


Create LE Support Dump
    [Documentation]    Creates LE support dump in a bactch one after the other on one view appliance. Input is a list of dictionary for various users to create.
    [Arguments]      ${LE_support_dump}     ${le_id}   ${VERIFY}=${FALSE}   ${STATUS_CODE}=200
	${resp} =     fusion api get logical enclosure support dump    ${LE_support_dump}     ${le_id}
	${status}  ${task_uri} =  Run Keyword and Ignore Error  Get From Dictionary  ${resp['headers']}  location
    Run keyword if    '${VERIFY}'=='True'     Should Be Equal    '${resp['status_code']}'   '${STATUS_CODE}'    msg=Verification of status_code in create support dumps response body has FAILED    values=False
	Run keyword if    '${VERIFY}'=='True' and '${resp['status_code']}' == '${STATUS_CODE}'    Should Not Be Empty    ${task_uri}    msg=Verification of uri in create support dumps response body has FAILED
    Return From Keyword    ${task_uri}

Create Support name and location
    [Arguments]     ${OUTPUT_DIR}    ${sd_type}   ${VERIFY}=${FALSE}   ${STATUS_CODE}=200
    ${sd_name} =    Get Time
    ${sd_name} =    Catenate    SEPARATOR=-    ${sd_name}     ${sd_type}
    ${sd_name} =    Catenate    SEPARATOR=.    ${sd_name}    sdmp
    ${sd_name} =    Replace String Using Regexp    ${sd_name}    ( |:)    _
    ${sd_name} =    Catenate    SEPARATOR=\\    ${OUTPUT_DIR}    ${sd_name}
    log to console and logfile    sd_name:${sd_name}
    [Return]    ${sd_name}

# Synergy ICM and sevrer verification keywords ----------------------------------------------------------
Verify Monitored Server Hardware
    [Documentation]     To verify all server hardware is monitored
    ${resp} =   Fusion Api Get Server Hardware
    ${l} =  Get Length  ${resp['members']}
    ${status} =   Create List
    :FOR    ${x}    IN RANGE    0   ${l}
    \   Run Keyword If  '${resp['members'][${x}]['status']}'!='OK'  Run Keyword    Log   Verify Server Hardware ${resp['members'][${x}]['name']} Failed     WARN
    \   Run Keyword If  '${resp['members'][${x}]['status']}'=='Critical'  Append to List    ${status}     Critical
    \   Run Keyword If  '${resp['members'][${x}]['state']}'!='Monitored'  Log   Server Hardware ${resp['members'][${x}]['name']} is not Monitored     WARN
    ${len} =   Get Length  ${status}
    Run Keyword Unless  '${len}'=='0'   Fail     msg=One or more Server Hardware are in Critical Status

Verify All Interconnects
    [Documentation]     To check if all Interconnects are in Good Status
    ${resp} =   Fusion Api Get Interconnect
    ${l} =  Get Length  ${resp['members']}
    ${status} =   Create List
    :FOR    ${x}    IN RANGE    0   ${l}
    \   Run Keyword If  '${resp['members'][${x}]['status']}'!='OK'  Run Keyword    Log   Verify Logical Interconnect ${resp['members'][${x}]['name']} Failed     WARN
    \   Run Keyword If  '${resp['members'][${x}]['status']}'=='Critical'  Append to List    ${status}     Critical
    ${resp_sas} =     Fusion Api Get SAS Interconnects
    ${l} =  Get Length  ${resp_sas['members']}
    :FOR    ${x}    IN RANGE    0   ${l}
    \   Run Keyword If  '${resp_sas['members'][${x}]['status']}'!='OK'  Log   Verify Logical Interconnect ${resp_sas['members'][${x}]['name']} Failed     WARN
    \   Run Keyword If  '${resp_sas['members'][${x}]['status']}'=='Critical'  Append to List    ${status}     Critical
    ${len} =   Get Length  ${status}
    Run Keyword Unless  '${len}'=='0'   Fail     msg=One or more Interconnects are in Critical Status

Verify all profiles
    [Documentation]     To check if all server profiles are in Good Status
    ${resp} =   Fusion Api Get Server Profiles
    ${l} =  Get Length  ${resp['members']}
    ${status} =   Create List
    :FOR    ${x}    IN RANGE    0   ${l}
    \   Run Keyword If  '${resp['members'][${x}]['status']}'!='OK'  Run Keyword    Log   Verify Server Profile  ${resp['members'][${x}]['name']} Failed     WARN
    \   Run Keyword If  '${resp['members'][${x}]['status']}'=='Critical'  Append to List    ${status}     Critical
    ${len} =   Get Length  ${status}
    Run Keyword Unless  '${len}'=='0'   Fail     msg=One or more Server Profiles are in Critical Status

FVT Check Profile State
	[Arguments]	${enc_bay_sp}	${sp_state}

    ${resp}=    Fusion Api Get Server Profiles   param=?filter="'name'=='${enc_bay_sp}'"
    Log to console    ${resp['members'][0]['name']}
    Log to console    ${resp['members'][0]['state']}
    Should Be Equal As Strings    ${resp['members'][0]['state']}    ${sp_state}

#	[Arguments]    ${ringNum}    ${encNum}    ${serverBayNum}
# Removes an Interconnect from a specific enclosure and bay location
# Enclosure = DCS_RING1_ENC1 or HW_RING1_ENC1
    Run Keyword If    '${dcs}' == 'true'    Set Suite Variable    ${currEnc}    DCS_RING${ringNum}_ENC1
    ...    ELSE    Set Suite Variable    ${currEnc}    HW_RING${ringNum}_ENC1

#    CN754406W7, interconnect 3
    Set Suite Variable    ${currICM}    ${${currEnc}}, interconnect ${ICMbayNum}
    Log to console   ${${currEnc}}
    Log to console   ${currICM}


# UFG keywords ----------------------------------------------------------
FVT Edit LIG
	[Arguments]	${lig_body}   ${LIG_URI}
	${body} =	Build LIG body	${lig_body}

	${resp} =	Fusion Api Edit Lig	body=${body}	uri=${LIG_URI}
	${task} =	Wait For Task	${resp}	5 min	15s

FVT LI Update From Group
	[Arguments]	${LI}
	${li_uri} =   Get LI URI    ${LI}
#	Log to console  ${li_uri} ${\n}
#    Log to Console      "step - "
	${resp} =   Fusion Api Update From Group	${li_uri}
	Should Be Equal As Integers	${resp['status_code']}	202
	${task} =	Wait For Task	${resp}	50 min	15s
	Sleep	5m

# CRM resource change keywords ----------------------------------------------------------

LI update
#	[Arguments]    ${TCnum}    ${LIGName}  ${uplinksetName}
	[Arguments]    ${TCnum}    ${LIGName}
	### Edit LIG to add network
    ${lig_uri} =    Get LIG Uri   ${LIGName}
    FVT Edit LIG   ${dcs_ufg_ligs[${TCnum}]}   ${LIG_URI}

    ### Delete an LI uplink set "mlag3-enet4x-us"
	${resp} =       Fusion Api Delete Uplink Set    name=mlag3-enet4x-us

	### add network to LI uplink set  "mlag1-enet4x-us"
    ${net} =   Fusion Api Get Ethernet Networks	param=?filter="'name'=='net_403'"
	${net_uri}= 			Get From Dictionary	${net['members'][0]}	uri
	${uplinksets} =			Fusion Api Get Uplink Set	param=?filter="'name'=='mlag1-enet4x-us'"
	${us} = 				Get From List	${uplinksets['members']}	0
	${us_uri} = 			Get From Dictionary	${us}	uri
	Append To List		    ${us['networkUris']}	${net_uri}
	${resp} = 				Fusion Api Edit Uplink Set	body=${us}	uri=${us_uri}
	${task} =               Wait For Task 	${resp} 	5 min	5s
	${valDict} = 			Create Dictionary	status_code=${200}
	Validate Response	${task}	${valDict}

    ${resp}=   Fusion Api Get LI   param=?filter="'name'=='${LI}'"
	Should Be Equal As Strings	${resp['members'][0]['consistencyStatus']}	CONSISTENT


# Server profiles keywords ----------------------------------------------------------
#	Power Off All Servers
Power Off Servers
	[Tags]    CONFIGURE   POWER OFF SERVERS    OFF
	Power Off All Servers


DCS Edit profiles with hardware
#Edit profile connections
 	${server_profiles} =	Get Variable Value	${dcs_edit_server_profiles}
	log to console and logfile	Assigning Server Hardware to Profiles
 	Run Keyword If	${server_profiles} is not ${null}		Edit Server Profiles from variable	${server_profiles}   ${dcs_server_profile_to_bay_map}   waitForTask=${True}

HW Edit  profiles with hardware
#Edit profile connections
 	${server_profiles} =	Get Variable Value	${hw_edit_server_profiles}
	log to console and logfile	Assigning Server Hardware to Profiles
 	Run Keyword If	${server_profiles} is not ${null}		Edit Server Profiles from variable	${server_profiles}   ${hw_server_profile_to_bay_map}   waitForTask=${True}


# SLM keywords ----------------------------------------------------------
FVT Check Interconnect State
	[Arguments]	${enc_bay_icm}	${icm_state}

#    ${resp} =	Fvt Api Get Interconnect By Name	${enc_bay_icm}

    ${resp}=    Fusion Api Get Interconnect   param=?filter="'name'=='${enc_bay_icm}'"
    Should Be Equal As Strings    ${resp['members'][0]['state']}    ${icm_state}

FVT ICM Efuse
	[Arguments]	${enc}	${bay}	${onOff}
	Get EM IP	${enc}
	Get EM Token	${enc}
	Efuse ICM	EFuse${onOff}	${bay}

Efuse Remove CL
# Removes an Interconnect from a specific enclosure and bay location
    Get EM IP     ${enc3}
    Get EM Token  ${enc3}

    Efuse ICM   EFuseOn     ${bay6}
    sleep       ${efuse_sleeptime}
	FVT Check Interconnect State    ${enc3_bay6_icm}    Absent

    Efuse ICM   EFuseOn     ${bay2}
    sleep       ${efuse_sleeptime}
	FVT Check Interconnect State    ${enc3_bay2_icm}    Absent

Efuse Add CL
# Removes an Interconnect from a specific enclosure and bay location
    Get EM IP      ${enc3}
    Get EM Token    ${enc3}

    Efuse ICM   EFuseOff     ${bay6}
    sleep       ${efuse_sleeptime}
    FVT Check Interconnect State    ${enc3_bay6_icm}    Configured

    Efuse ICM   EFuseOff    ${bay2}
    sleep       ${efuse_sleeptime}
    FVT Check Interconnect State	${enc3_bay2_icm}    Configured

Efuse Remove HA LI Potash ICM
	[Arguments]    ${ringNum}    ${encNum}    ${ICMbayNum}
# Removes an Interconnect from a specific enclosure and bay location
# Enclosure = DCS_RING1_ENC1 or HW_RING1_ENC1
    Run Keyword If    '${dcs}' == 'true'    Set Suite Variable    ${currEnc}    DCS_RING${ringNum}_ENC1
    ...    ELSE    Set Suite Variable    ${currEnc}    HW_RING${ringNum}_ENC1

#    CN754406W7, interconnect 3
    Set Suite Variable    ${currICM}    ${${currEnc}}, interconnect ${ICMbayNum}
    Log to console   ${${currEnc}}
    Log to console   ${currICM}

    Get EM IP      ${${currEnc}}
    Get EM Token    ${${currEnc}}
    Efuse ICM   EFuseOn     ${ICMbayNum}
    sleep       ${efuse_sleeptime}
    FVT Check Interconnect State	${currICM}    Absent

Efuse Add HA LI Potash ICM
	[Arguments]	${ringNum}    ${encNum}    ${ICMbayNum}
# Add Potash to Enclosure 1 bay 3 which is part of HA LI
# Enclosure = DCS_RING1_ENC1 or HW_RING1_ENC1
    Run Keyword If    '${dcs}' == 'true'    Set Suite Variable    ${currEnc}    DCS_RING${ringNum}_ENC1
    ...    ELSE    Set Suite Variable    ${currEnc}    HW_RING${ringNum}_ENC1

#    CN754406W7, interconnect 3
    Set Suite Variable    ${currICM}    ${${currEnc}}, interconnect ${ICMbayNum}
    Log to console   ${${currEnc}}
    Log to console   ${currICM}

    Get EM IP      ${${currEnc}}
    Get EM Token    ${${currEnc}}
    Efuse ICM   EFuseOff     ${ICMbayNum}
    sleep       ${efuse_sleeptime}
    sleep       ${sleeptime_potashAdd}
    FVT Check Interconnect State	${currICM}    Configured

# support dump keywords ----------------------------------------------------------
FVT LE supportdump
	${les} =	Get Variable Value	${les}

#  for each ring (ringX-Enc3-LE)
    #:FOR    ${x}    IN RANGE    1   ${numLEs}+1
    #\    Set Suite Variable    ${currentLE}    ring${x}-Enc3-LE
    #\    Log to console    ${currentLE}
    #\    FVT support dump per LE    ${currentLE}

FVT support dump per LE
	[Arguments]   ${currentLE}
# from Carbon testcases
     ${le_uri} =    Get LE URI      ${currentLE}
     ${logicalEnclosureId}=    Fetch From Right        ${le_uri}      /
     Log to console    LE uri- ${logicalEnclosureId}

     ${Response}=    Fusion Api Get Logical Enclosure Support Dump   body=${LE_SupportDump_Payload}   id=${logicalEnclosureId}
     Should Be Equal as Strings      ${Response['status_code']}       202       msg=Failed to initiate Create Enclosure Support Dump.
     Log to console    \n-Waiting for dump creation task to complete
     ${task} =                       Wait For Task           ${Response}     15min    1min
     Should Be Equal as Strings      ${task['status_code']}      200       msg=Failed to Create Enclosure Support Dump.
     log to console and logfile     \n-Support dump created successfully

     Empty Directory     ${dump_file_path}
     ${supportDumpUri}=          Get From Dictionary     ${task['associatedResource']}   resourceUri
     ${Response1}=        Fusion Api Download Support Dump            uri=${supportDumpUri}   localfile=${LE_DUMP_FILE}
     Should Be Equal as Strings      ${Response1['status_code']}      200           msg=Failed to Download Enclosure Support Dump.
     log to console and logfile      \n-Support Dump downloaded successfully

#     log to console and logfile      \n-Decrypting ,extracting the downloaded dump file and verifying if the Carbon module is present
#     Decrypt and extract the dump file    ${dump_file_path}    ${decryptor_path}
#     :FOR  ${x}  IN  @{icbays}
#     \     OperatingSystem.File Should Exist      ${CURDIR}/support_dump/logical-enclosure/var/tmp/le-support-dumps/li-0/${LI_Name}/encl000000${ENC1}/bay${x}/VCFC4${IC${x}}*
#     ...     msg=The Carbon module VCFC4${IC${x}} is not found in LE Dump
#     \    log to console and logfile      \n- Verified Carbon Module VCFC4${IC${x}} is showing up in LE support dump


# variables keywords ----------------------------------------------------------
