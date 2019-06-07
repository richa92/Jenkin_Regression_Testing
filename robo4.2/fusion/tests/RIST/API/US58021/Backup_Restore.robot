*** Settings ***
Documentation                   Perform Backup Restore Operations

Library                         FusionLibrary
Library                         RoboGalaxyLibrary
Library                         OperatingSystem
Library                         BuiltIn
Library                         Collections
Library                         XML
Library                         String
Library                         json

Resource                        ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot

Variables 		                ${DATA_FILE}

Suite Setup                     Setup Suite
#Suite Teardown                  Teardown Suite

*** Variables ***
${APPLIANCE_IP}                 APPLIANCE_IP

${wordy}                        ${True}

${DATA_FILE}                    ./Regression_Data.py

*** Test Cases ***
Create OneView Backup
    Set Log Level      DEBUG
    Log    Creating Initial Backup    console=true
    Create Backup

Get OneView Backup
    # not really doing anything with this yet.
    ${backup} =    Get Backup

Get OneView Backup URI
    ${uri} =    Get Backup URI
    Set Suite Variable    ${BACKUPURI}    ${uri}

Download OneView Backup
    Log    Download Backup    console=true
    ${OUTPUT_DIR} =    Set Variable If   '${OUTPUT_DIR}'==''    .\\    ${OUTPUT_DIR}

    ${local_file} =    Get Time
    ${local_file} =    Catenate    SEPARATOR=.    ${local_file}    bkp
    ${local_file} =    Replace String Using Regexp    ${local_file}    ( |:)    _
    ${local_file} =    Catenate    SEPARATOR=\\    ${OUTPUT_DIR}    ${local_file}
    Log    Download to: ${local_file}    console=true
    Set Suite Variable    ${BKP_FILE}     ${local_file}

    Download Backup    ${BACKUPURI}    ${local_file}

Do Some Stuff
    Add Ethernet Networks from variable	${Post_backup_ethernet_networks}
    Add LIG from list  ${Post_backup_lig}
	Add Enclosure Group from list  ${Post_backup_eg}

    Add Logical JBODs Async     ${Post_backup_ljbs}
    Wait Until Keyword Succeeds    2 min    5s    Check Resource Attribute     SASLJBOD:${ljb1_name}  state  Configured
    Wait Until Keyword Succeeds    2 min    5s    Check Resource Attribute     SASLJBOD:${ljb2_name}  state  Configured
    Reapply SAS Logical Interconnect Configuration By Name and Verify     ${SASLI}

	# Remove two networks we created in Suite Setup
    Delete Resource    ETH:BR_Network1
    Delete Resource    ETH:BR_Network2

    Power off Server    ${Post_backup_SH}    PressAndHold
    ${resp} =    Add Server Profile    ${Post_backup_profile}
    log to console    ${resp}
    Wait For Task2    ${resp}    timeout=2400    interval=20

Create Another OneView Backup
    # This will overwrite the original backup.  This way, we know for sure our uploaded backup is used.
    Log    Creating 2nd Backup    console=true
    Create Backup

Upload Original OneView Backup
    Upload Backup    ${BKP_FILE}
    ${uri} =    Get Backup URI
    Set Suite Variable    ${BACKUPURI}    ${uri}

Restore Original OneView Backup
    ${resp}=    Initiate Restore    ${BACKUPURI}

Wait for Restore to Complete
    Wait Until Keyword Succeeds    90m    30s    OneView Restore Complete

Wait for Startup Complete
    Wait Until Keyword Succeeds    5m    30s    OneView Startup Complete    ${APPLIANCE_IP}

Verify Original Stuff
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

    # verify Post Backup Ethernet Networks are not there
    :For    ${net}   IN    @{Post_backup_ethernet_networks}
    \    ${uri} =    Get Ethernet URI    ${net['name']}
    \    Should Match    ${uri}    /rest/network_uri_${net['name']}_not_found

    Verify Initial Counts
	${dto} =  Get Resource  LIG:${LIG_NAME}
    ${validate_status} =  Fusion api validate response follow  ${BR_lig_validate}  ${dto}  wordy=${wordy}
    Should Be Equal As Strings    ${validate_status}    True

    ${dto} =  Get Resource  EG:${EG_NAME}
    ${validate_status} =  Fusion api validate response follow  ${BR_eg[0]}  ${dto}  wordy=${wordy}
    Should Be Equal As Strings    ${validate_status}    True

    ${dto} =  Get Resource  SP:${SP_NAME}
    ${mezz} =    Get Substring    ${BR_profile["serverHardwareTypeUri"]}    4
    ${uri} =    Get Server Hardware Type URI By Name And Mezz    ${mezz}
    ${sht} =    Get Resource by URI    ${uri}
    Set To Dictionary    ${BR_profile}    serverHardwareTypeUri    SH:${SH}
    ${validate_status} =  Fusion api validate response follow  ${BR_profile}  ${dto}  wordy=${wordy}
    Should Be Equal As Strings    ${validate_status}    True

Suite Teardown
    Teardown Suite

*** Keywords ***
Setup Suite
    [Documentation]    Setup Suite
    Set Log Level    DEBUG
    Should Not Be Equal As Strings    ${APPLIANCE_IP}    APPLIANCE_IP

    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

    # Just add some extra stuff
    Add Ethernet Networks from variable	${BR_ethernet_networks}
    Add LIG from list  ${BR_lig}
	Add Enclosure Group from list  ${BR_eg}

    Add Logical JBODs Async     ${ljbs}
    Wait Until Keyword Succeeds    2 min    5s    Check Resource Attribute     SASLJBOD:${ljb1_name}  state  Configured
    Reapply SAS Logical Interconnect Configuration By Name and Verify     ${SASLI}

    @{profiles} =    Create list
    Append To List    ${profiles}    ${br_profile}
    :FOR	${profile}	IN	@{profiles}
    \    ${sp_uri} =    Common Uri Lookup By Name    SP:${profile['name']}
    \    ${status}    ${dontcare} =    Run Keyword and Ignore Error    Should End With    ${sp_uri}    _not_found
    \    Run Keyword If   '${status}'=='FAIL'    Continue For Loop
    \    Power off Server    ${SH}    PressAndHold
    \    ${task} =    Add Server Profile    ${profile}
    \    Wait For Task2    ${task}    timeout=4200    interval=15

    Remove From List    ${profiles}    0
    Append To List    ${profiles}    ${Post_backup_profile}
    :FOR	${profile}	IN	@{profiles}
    \    ${sp_uri} =    Common Uri Lookup By Name    SP:${profile['name']}
    \    ${status}    ${dontcare} =    Run Keyword and Ignore Error    Should End With    ${sp_uri}    _not_found
    \    Run Keyword If   '${status}'=='PASS'    Continue For Loop
    \    Power off Server    ${Post_backup_SH}    PressAndHold
    \    ${task} =    Remove Server Profile    ${profile}
    \    Wait For Task2    ${task}    timeout=4200    interval=15

	Get Initial Counts

Teardown Suite
    [Documentation]    Teardown Suite
    Reapply SAS Logical Interconnect Configuration By Name and Verify     ${SASLI}
    Delete Logical JBODs Async     ${ljbs}
    ${uri} =    Get Server Profile URI    ${SP_NAME}
    ${resp} =    Fusion Api Delete Server Profile    uri=${uri}    param=?force=${True}
    Wait For Task2    ${resp}    timeout=600    interval=10

    ${uri} =    Get Enclosure Group URI    ${EG_NAME}
    ${resp} = 	Fusion Api Delete Enclosure Group		uri=${uri}
    Wait For Task2    ${resp}    timeout=15    interval=2

    ${uri} =    Get LIG URI    ${LIG_NAME}
    ${resp} =    Fusion Api Delete LIG    uri=${uri}
    Wait For Task2    ${resp}    timeout=15    interval=2
    Fusion Api Logout Appliance

Get Initial Counts
    [Documentation]    Get Initial Counts
#   Server Resources
    ${enc} =    Fusion Api Get Enclosures
    Set Suite Variable    ${ENC_COUNT}    ${enc['count']}

    ${le} =    Fusion Api Get Logical Enclosure
    Set Suite Variable    ${LE_COUNT}    ${le['count']}

    ${hw} =    Fusion Api Get Server Hardware
    Set Suite Variable    ${HW_COUNT}    ${hw['count']}

    ${eg} =    Fusion Api Get Enclosure Groups
    Set Suite Variable    ${EG_COUNT}    ${eg['count']}

    ${sp} =    Fusion Api Get Server Profiles
    Set Suite Variable    ${SP_COUNT}    ${sp['count']}

    ${spt} =    Fusion Api Get Server Profile Templates
    Set Suite Variable    ${SPT_COUNT}    ${spt['count']}

#   Networking Resources
    ${lig} =    Fusion Api Get LIG
    Set Suite Variable    ${LIG_COUNT}    ${lig['count']}

    ${ic} =    Fusion Api Get Interconnect
    Set Suite Variable    ${IC_COUNT}    ${ic['count']}

    ${ict} =    Fusion Api Get Interconnect Types
    Set Suite Variable    ${ICT_COUNT}    ${ict['count']}

    ${sasic} =    Fusion Api Get SAS Interconnects
    Set Suite Variable    ${SASIC_COUNT}    ${sasic['count']}

    ${ethernet} =    Fusion Api Get Ethernet Networks
    Set Suite Variable    ${ETH_COUNT}    ${ethernet['count']}

    ${fc} =    Fusion Api Get FC Networks
    Set Suite Variable    ${FC_COUNT}    ${fc['count']}

    ${fcoe} =    Fusion Api Get FCoE Networks
    Set Suite Variable    ${FCOE_COUNT}    ${fcoe['count']}

    ${ns} =    Fusion Api Get Network Set
    Set Suite Variable    ${NS_COUNT}    ${ns['count']}

#   Storage
    ${ss} =    Fusion Api Get Storage System
    Set Suite Variable    ${SSystems_COUNT}    ${ss['count']}

    ${sp} =    Fusion Api Get Storage Pools
    Set Suite Variable    ${SPools_COUNT}    ${sp['count']}

    ${sv} =    Fusion Api Get Storage Volumes
    Set Suite Variable    ${SVolumes_COUNT}    ${sv['count']}

    ${svt} =    Fusion Api Get Storage Volumes Template
    Set Suite Variable    ${SVolumeTemplate_COUNT}    ${svt['count']}

    ${de} =    Fusion Api Get Drive Enclosure
    Set Suite Variable    ${DE_COUNT}    ${de['count']}

    ${san} =    Fusion Api Get Managed San
    Set Suite Variable    ${SAN_COUNT}    ${san['count']}

    ${ljb} =    Fusion Api Get Sas Logical Jbods
    Set Suite Variable    ${ljb_COUNT}    ${ljb['count']}

#   Users
    ${u} =    Fusion Api Get User
    Set Suite Variable    ${USER_COUNT}    ${u['count']}

Verify Initial Counts
    [Documentation]    Verify Initial Counts
#   Server Resources
    ${enc} =    Fusion Api Get Enclosures
    Log    Enclosure ${ENC_COUNT} vs ${enc['count']}    console=true
    Should Be Equal As Integers    ${ENC_COUNT}    ${enc['count']}    Enclosure count not the same a was at backup time

    ${le} =    Fusion Api Get Logical Enclosure
    Log    Logical Enclosure ${LE_COUNT} vs ${le['count']}    console=true
    Should Be Equal As Integers    ${LE_COUNT}    ${le['count']}    Logical Enclosure count not the same a was at backup time

    ${hw} =    Fusion Api Get Server Hardware
    Log    Server Hardware ${HW_COUNT} vs ${hw['count']}    console=true
    Should Be Equal As Integers    ${HW_COUNT}    ${hw['count']}    Server Hardware count not the same a was at backup time

    ${eg} =    Fusion Api Get Enclosure Groups
    Log    Enclosure Group ${EG_COUNT} vs ${eg['count']}    console=true
    Should Be Equal As Integers    ${EG_COUNT}    ${eg['count']}    Enclosure Group count not the same a was at backup time

    ${sp} =    Fusion Api Get Server Profiles
    Log    Server Profile ${SP_COUNT} vs ${sp['count']}    console=true
    Should Be Equal As Integers    ${SP_COUNT}    ${sp['count']}    Server Profile count not the same a was at backup time

    ${spt} =    Fusion Api Get Server Profile Templates
    Log    Server Profile Template ${SPT_COUNT} vs ${spt['count']}    console=true
    Should Be Equal As Integers    ${SPT_COUNT}    ${spt['count']}    Server Profile Template count not the same a was at backup time

#   Networking Resources
    ${lig} =    Fusion Api Get LIG
    Log    LIG ${LIG_COUNT} vs ${lig['count']}    console=true
    Should Be Equal As Integers    ${LIG_COUNT}    ${lig['count']}    LIG count not the same a was at backup time

    ${ic} =    Fusion Api Get Interconnect
    Log    Interconnect ${IC_COUNT} vs ${ic['count']}    console=true
    Should Be Equal As Integers    ${IC_COUNT}    ${ic['count']}    Interconnect count not the same a was at backup time

    ${ict} =    Fusion Api Get Interconnect Types
    Log    Interconnect Types ${ICT_COUNT} vs ${ict['count']}    console=true
    Should Be Equal As Integers    ${ICT_COUNT}    ${ict['count']}    Interconnect Types count not the same a was at backup time

    ${sasic} =    Fusion Api Get SAS Interconnects
    Log    SAS Interconnect ${SASIC_COUNT} vs ${sasic['count']}    console=true
    Should Be Equal As Integers    ${SASIC_COUNT}    ${sasic['count']}    SAS Interconnect count not the same a was at backup time

    ${ethernet} =    Fusion Api Get Ethernet Networks
    Log    Ethernet Network ${ETH_COUNT} vs ${ethernet['count']}    console=true
    Should Be Equal As Integers    ${ETH_COUNT}    ${ethernet['count']}    Ethernet Network count not the same a was at backup time

    ${fc} =    Fusion Api Get FC Networks
    Log    FC Network${FC_COUNT} vs ${fc['count']}    console=true
    Should Be Equal As Integers    ${FC_COUNT}    ${fc['count']}    FC Network count not the same a was at backup time

    ${fcoe} =    Fusion Api Get FCoE Networks
    Log    FCoE Network ${FCoE_COUNT} vs ${fcoe['count']}    console=true
    Should Be Equal As Integers    ${FCoE_COUNT}    ${fcoe['count']}    FCoE Network count not the same a was at backup time

    ${ns} =    Fusion Api Get Network Set
    Log    Network Set ${NS_COUNT} vs ${ns['count']}    console=true
    Should Be Equal As Integers    ${NS_COUNT}    ${ns['count']}    Network Set count not the same a was at backup time

#   Storage
    ${ss} =    Fusion Api Get Storage System
    Log    Storage System ${SSystems_COUNT} vs ${ss['count']}    console=true
    Should Be Equal As Integers    ${SSystems_COUNT}    ${ss['count']}    Storage System count not the same a was at backup time

    ${sp} =    Fusion Api Get Storage Pools
    Log    Storage System Pool ${SPools_COUNT} vs ${sp['count']}    console=true
    Should Be Equal As Integers    ${SPools_COUNT}    ${sp['count']}    Storage System Pool count not the same a was at backup time

    ${sv} =    Fusion Api Get Storage Volumes
    Log    Storage System Volume ${SVolumes_COUNT} vs ${sv['count']}    console=true
    Should Be Equal As Integers    ${SVolumes_COUNT}    ${sv['count']}    Storage System Volume count not the same a was at backup time

    ${svt} =    Fusion Api Get Storage Volumes Template
    Log    Storage System Template ${SVolumeTemplate_COUNT} vs ${svt['count']}    console=true
    Should Be Equal As Integers    ${SVolumeTemplate_COUNT}    ${svt['count']}    Storage System Template count not the same a was at backup time

    ${de} =    Fusion Api Get Drive Enclosure
    Log    Drive Enclosure ${DE_COUNT} vs ${de['count']}    console=true
    Should Be Equal As Integers    ${DE_COUNT}    ${de['count']}    Drive Enclosure count not the same a was at backup time

    ${san} =    Fusion Api Get Managed San
    Log    Managed SAN ${SAN_COUNT} vs ${san['count']}    console=true
    Should Be Equal As Integers    ${SAN_COUNT}    ${san['count']}    Managed SAN count not the same a was at backup time

    ${ljb} =    Fusion Api Get Sas Logical Jbods
    Log    LJBODs ${ljb_COUNT} vs ${ljb['count']}    console=true
    Should Be Equal As Integers    ${ljb_COUNT}    ${ljb['count']}    LJBODs count does not match that was taken at backup time
    ${ljb_name} =     Get From Dictionary        ${ljb['members'][0]}    name
    Should Match    ${ljb_name}    ${ljb1_name}    LJBOD name does not match that was taken at backup time
    Wait Until Keyword Succeeds    180s    10s    Get Alert By Param   param=?filter=description like 'A mismatch between the logical interconnect configuration and the interconnect configuration has been detected*'

#   Users
    ${u} =    Fusion Api Get User
    Log    User {USER_COUNT} vs ${u['count']}    console=true
    Should Be Equal As Integers    ${USER_COUNT}    ${u['count']}    User count not the same a was at backup time
