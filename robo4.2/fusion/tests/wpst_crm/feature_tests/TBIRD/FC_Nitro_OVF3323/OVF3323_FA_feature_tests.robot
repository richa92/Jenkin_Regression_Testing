*** Settings ***
Documentation    OVF3323 - FC FabricAttach on Nitro User Story
...
...    - Goal:
...      |  - Ensure FC FabricAttach end2end work with Nitro ICM (OVF3233)
...      |  - Test with 2 different LI downlinkSpeedMode: 25gb and 50Gb (OVF4511)
...      |  \ \  to ensure end2end works in both speedMode for Quack and Quagmire2 servers
...      |  - Ensure LI downlinkSpeedMode change to and from 50Gb works
...      |  \ \  any connection outage incurred should be recovered (OVF5199)
...
...    - Usage:
...      |  - full test:
...      |  \ \ Run with LI downlinkSpeedMode 25Gb, default. same as -v dls:25
...      |  \ \ - robot -V data_OVF3323_FA_BB56_ha.py -T -d /Result/FA OVF3323_FA_feature_tests.robot
...      |  \ \ Run with LI downlinkSpeedMode 50Gb, excluding DLS tests
...      |  \ \ - robot -V data_OVF3323_FA_BB56_ha.py -v dls:50 -e DLS -T -d /Result/FA OVF3323_FA_feature_tests.robot
...      |  - skip precondition setup: robot -v skipSetup:True -V data_OVF3323_FA_BB56_ha.py
...      |  \ \ \ \ -T -d /Result/FA  OVF3323_FA_feature_tests.robot
...      |  - run tagged cases: robot -V data_OVF3323_FA_BB56_ha.py -i setup -i Happy -i DLS
...      |  \ \ \ \ -T -d /Result/FA  OVF3323_FA_feature_tests.robot
...
...    - The test can test different test enclosures with configuration specified in data file.
...    - The following is BB56 config:
...
...    - LE - 2 frame, HA, IBS3, 2 CXP between Methane and Nitro, total 4 CXP
...
...    - 1 Enet uplinkset on Aside: IC3:Q1 (40Gb Enet DA)
...    - 1 FA uplinkset on Aside
...      |  - US-FA1: FA1, with Auto LoginRedistribution
...      |  - 2 uplinks
...      |  \ \ - IC3:Q3:1 desiredSpeed 16Gb (1x16Gb SFP)
...      |  \ \ - IC3:Q4:1 desiredSpeed 32Gb (1x32Gb SFP)
...    - 1 FA uplinkset on Bside
...      |  - US-FA2: FA2, with Manual LoginRedistribution, treated as Auto on Nitro and Potash
...      |  - 2 uplinks
...      |  \ \ - IC6:Q3 desiredSpeed 16Gb (1x16Gb SFP)
...      |  \ \ - IC6:Q5 desiredSpeed 32Gb (1x32Gb SFP)
...
...    - Note: All FA uplinkports are connected to 32Gb SAN swtich which is then connected
...      |  \ \ \ to 3par 8200 16Gb external HBA (to be replaced with 32Gb when 3par support it)
...
...    - 4 servers: 2 FC FA connections (FA1 and FA2 connections)
...      |  - All servers are WS2016
...      |  - total 4 servers: each frame: 2 servers, 1 with Quack, 1 with Quagmire2
...      |  - among the 4 servers, 2 BFS servers, one on each side, with Quack and Quagmire2
...
...    - Minimum 2 servers going through each uplinkset locally or through Methane for storage access
...
...    - Test Coverage:
...      |  - Negative (LIG and LI)
...      |  \ \ - All legacy limitation
...      |  \ \ - Nitro specific:
...      |  \ \ \  - cannot mixed unsplit and split port in an FC uplinkset
...      |  \ \ \  - uplink speed: Auto/2Gb/4Gb not allowed, require speed specification
...
...      |  - PortStatusReason (delete Uplinksets, compliance, portStatusReason, UFG)
...      |  \ \ - FabricMismatch
...      |  \ \ - FcSpeedMismatch
...      |  \ \ - Unpopulated
...      |  \ \ - ModuleIncompatible
...
...      |  - end2End: LI downlinkSpeedMode 25Gb and 50Gb; BFS servers go through the scenarios
...      |  \ \ - Happy path
...      |  \ \ - uplink speed change on LI uplinkset, and UFG
...      |  \ \ \ \ - Aside uplinks from 32 and 16 to 8Gb, UFG change back to 16 and 32 from 8
...      |  \ \ \ \ - Bside uplinks, one from 32 to 16, the other from 16 to 8, UFG change back
...      |  \ \ - disable/enable uplinks, Aside and Bside
...      |  \ \ \ \ - Aside disable/enable one uplink at a time
...      |  \ \ \ \ - Bside disable/enable both uplinks at a time
...      |  \ \ - disable/enable downlinks, Aside and Bside
...      |  \ \ \ \ - one enc1 and enc2 servers for Aside, different enc1 and enc2 servers for Bside
...      |  \ \ - Power off/on enc1 Nitro 3 (Aside)
...      |  \ \ - make sure FC uplinkset modification works after power back on Nitro
...      |  \ \ \ \ - Edit uplinkset defined on Aside removing uplinkport
...      |  \ \ \ \ - LI UFG adding back uplinkport
...      |  \ \ - Power off/on enc2 Nitro 6 (Bside)
...      |  \ \ - make sure FC uplinkset modification works after power back on Nitro (when 4x cable available)
...      |  \ \ \ \ - Edit uplinkset defined on Bside adding uplinkport and existing uplink speed change
...      |  \ \ \ \ - LI UFG remove added uplinkport and speed change back
...      |  \ \ - Remove/insert Nitro (Aside and Bside)
...      |  \ \ - reset Nitro (Aside and Bside)
...
...    - Servers login redistribution were verified when adding uplink, enable back uplinks
...    - With 4 servers and uplinkset with 2 uplinkports, expect servers logins evenly distributed
...      |  \ \ between the uplinkports after Happy Path, efuse insert, power on, reset Nitro,
...      |  \ \ enable/add uplink port
...
...    - Ensure all servers lost connection can recover for the aforementioned scenarios
...    - Server storage path verification are through FC uplinkport loginsCount
...
...    - LI downlinkSpeed Change to and from 25Gb, and to and from 50Gb
...      |  \ \ - end2end connections are verified
...      |  \ \ - overall connection bw exceeding DLS mode is disallowed
...      |  \ \ - Expect BFS server may go down and expect it will come back up
...
...    - Expected Nitro maxBandwidth, server downlink operationalSpeed are verified
...      |  in LE creation, LI downlinkSpeed Change, UFG, ICM efuse, power, reset scenarios.
...      |  based on LI downlinkSpeedMode and servers MZ card
...      |  \ \ For DLS mode 50Gb:
...      |  \ \ \ \ - Quack connection downlink operationalSpeed: 25Gb
...      |  \ \ \ \ - Quagmire2 connection downlink operationalSpeed: 50Gb
...      |  \ \ For DLS mode 25Gb:
...      |  \ \ \ \ - Both Quack and Quagmire2 connection downlink operationalSpeed: 25Gb
...


Resource         ../../../../../Resources/api/fusion_api_resource.txt
Resource         ../FVT/fvt-keywords.txt
Resource         ../FVT/Resources/fvt_resource.txt
Resource         ./DF_keywords.txt

Library          FusionLibrary
Library          ../FVT/fvt_api.py

Suite Setup      Suite Precondition Setup
Suite Teardown   Suite Min Teardown

# Setup for each test case
Test Setup       Common Test Setup
Test Teardown    Common Test Teardown

*** Variables ***
${skipSetup}    ${False}
${dls}          25
${downlink_mode}    SPEED_25GB
${expected_ic_maxbw}    SPEED_25G


*** Test Cases ***
OVF3323 Negative LIG FC FA Uplinkset
    [Tags]  LigUSNegative    Negative
    [Documentation]    The following are tested: limitations for FC FA uplinkset defined on LIG
    ...                CRM_INVALID_UPLINK_SET_PORT
    ...                    case - IRF split port
    ...                    case - IRF unsplit port
    ...                CRM_LOGICAL_UPLINK_TEMPLATE_FIBRE_CHANNEL_PORTS_DO_NOT_ALL_BELONG_TO_SAME_SWITCH
    ...                CRM_LOGICAL_UPLINK_CAN_ONLY_CONTAIN_MAX_ONE_FC_NETWORK
    ...                CRM_BOTH_SPLIT_AND_UNSPLIT_PORTS_USED_IN_UPLINK_SETS
    ...                CRM_INVALID_DESIRED_PORT_SPEED
    ...                    cases - Auto/2Gb/4Gb
    ...                    case - not specify speed


    PASS EXECUTION IF   '${REDUNDANCY}' == 'AB'   Skip Negative Test If Redundancy is A+B

    Log    ${\n}FC FA uplinkset on LIG negative test    console=True
    :FOR    ${ligtest}    IN    @{err_ligs}
    \    ${body} =    Build LIG body    ${ligtest['ligBody']}
    \    ${task} =    Fusion Api Create LIG    ${body}
    \    ${resp} =    Wait for Task2    ${task}    2m    5
    \    ...                                       PASS=Error
    \    ...                                       errorMessage=${ligtest['errorCode']}


OVF3323 Create Logical Enclosure and Verify LI LE and uplinks status, speed and connectedTo
    [Tags]  LE    setup
    [Documentation]   Create 2 FRAME ME HA or SE Redundant IBS3 LE with FA Uplinksets defined on each side
    ...               change LI downlinkSpeedMode based on variable dls value, user can pass in variable value

    Run Keyword for List    ${ligs}    Add LIG from variable

    Add Enclosure Group from variable    ${enc_group['${EG}']}

    Add Logical Enclosure from variable    ${les['${LE}']}

    Run Keyword And Continue On Failure    Verify Happy LE

    Run Keyword if    '${downlink_mode}' != 'SPEED_25GB'
    ...    Update LI DownlinkSpeedMode    ${LIs[0]}    ${downlink_mode}
    ...                                   ${data_common.LI_DLS_CHANGE_WAIT}    20s

    Log    ${\n}wait till Nitro maxBandwidth reached ${expected_ic_maxbw}    console=True
    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Named Interconnect     ${NITROA}    maxBandwidth=${expected_ic_maxbw}

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Named Interconnect     ${NITROB}    maxBandwidth=${expected_ic_maxbw}

    Run Keyword And Continue On Failure    Verify LI with SpeedMode

    Wait Until Keyword Succeeds    ${data_common.SERVERS_INIT_DLS_WAIT}    10s
    ...    Verify Servers Downlink Speed


OVF3323 LI FA Uplinksets Negative Tests
    [Tags]  LiUSNegative    Negative
    [Documentation]    The following are tested: limitations for FC FA uplinkset on LI
    ...                CRM_BOTH_SPLIT_AND_UNSPLIT_PORTS_USED_IN_UPLINK_SETS
    ...                CRM_PORT_CONFIG_INFO_LOCATION_IS_NOT_FC_UPLINK_CAPABLE
    ...                    case - IRF split port
    ...                    case - IRF unsplit port
    ...                CRM_PORTS_IN_DIFFERENT_SWITCH
    ...                CRM_LOGICAL_UPLINK_CAN_ONLY_CONTAIN_MAX_ONE_FC_NETWORK
    ...                CRM_PORT_ALREADY_ASSIGNED
    ...                CRM_PORT_NUMBER_UNKNOWN_FGORMAT
    ...                    case - Invalid port
    ...                CRM_INVALID_DESIRED_PORT_SPEED
    ...                    cases - Auto/2Gb/4Gb
    ...                    case - not specify speed

    PASS EXECUTION IF    '${REDUNDANCY}' == 'AB'    Skip Negative Test If Redundancy is A plus B

    ${resp} =    Fvt Api Get Logical Interconnect By Name    ${LIs[0]}
    ${li_uri} =    Get From Dictionary    ${resp}    uri

    :FOR    ${li_us}    IN    @{err_li_us_list}
    \    ${us} =     Copy Dictionary    ${li_us['usBody']}
    \    ${body} =    Build US body    ${us}    ${li_uri}
    \    ${task} =    Fusion Api Create Uplink Set    body=${body}
    \    ${resp} =    Wait for Task2    ${task}    2m    5
    \    ...                                       PASS=Error
    \    ...                                       errorMessage=${li_us['errorCode']}


OVF3323 Delet All LI uplinksets
    [Tags]  DeleteUS    LiUSPortStatusReason
    [Documentation]    Delete All LI Uplinksets
    ...                Testing Delete of uplinkset, verify LI become Inconsistent
    ...                Also free up uplinks for portStatusReason testing

    Log    ${\n}Remove all uplinksets and wait until uplinks are Unlinked    console=True
    Remove All Uplinksets
    :FOR    ${uplink}    IN    @{US_FA1_UPLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Port    ${NITROA}    ${uplink}    portStatus=Unlinked
    :FOR    ${uplink}    IN    @{US_FA2_UPLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Port    ${NITROB}    ${uplink}    portStatus=Unlinked

    Log    ${\n}Verify LI Inconsistent    console=True
    :FOR    ${li}    IN    @{LIs}
    \    Verify Logical Interconnect    ${li}    status=Warning    consistencyStatus=NOT_CONSISTENT


OVF3323 LI FA Uplinksets uplink Unlink various portStatusReason cases
    [Tags]  LiUSPortStatusReason  statusReason
    [Documentation]    The following are tested Uplinkset is created but uplink Unlinked with
    ...                portStatusReason
    ...                Split port format on 1x SFP - None with Alert
    ...                FA uplink on port connected to 3par - FabricTypeMismatch
    ...                FA uplink on port without SFP - Unpopulated
    ...                FA uplink with speed not supported on SFP - FcSpeedMismatch
    ...                FA uplink on port connected to Enet switch - ModuleIncompatible
    ...                Unsplit port format on 4x QSFP - Unknown? (when 4x QSFP available)
    ...
    ...                The uplinkset and uplinkport should be in Critical status

    PASS EXECUTION IF    '${REDUNDANCY}' == 'AB'    Skip Negative Test If Redundancy is A plus B

    ${li0_uri} =    Get LI URI    ${LIs[0]}
    ${li1_uri} =    Get LI URI    ${LIs[1]}

    :FOR    ${li_us}    IN    @{li_us_port_unlink_list}
    \    ${li_uri} =    Set Variable If    '${li_us['icm']}' == '${NITROA}'     ${li0_uri}    ${li1_uri}
    \    ${li_name} =    Set Variable If    '${li_us['icm']}' == '${NITROA}'     ${LIs[0]}    ${LIs[1]}
    \    ${us} =     Copy Dictionary    ${li_us['usBody']}
    \    ${body} =    Build US body    ${us}    ${li_uri}
    \    ${resp} =    Fusion Api Create Uplink Set    body=${body}
    \    ${task} =    Wait For Task    ${resp}    5min    15s
    \    Should Be Equal As Strings    ${task['taskState']}    Completed
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_ERROR_WAIT}    30s
    \    ...    Verify Port    ${li_us['icm']}    ${li_us['uplink']}    status=Critical
    \    ...        portStatus=Unlinked    portStatusReason=${li_us['expected_reason']}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_SPEED_WAIT}    20s
    \    ...    Verify Uplinkset Status    ${li_name}    ${us['name']}    Critical


OVF3323 LI Update From Group Remove added uplinksets and Add back deleted old ones
    [Tags]  LiUSPortStatusReason    LiUFGAddUS
    [Documentation]    LI update from group - remove and add uplinksets
    ...                Verify FA uplinkset status, uplinkport operationalSpeed and connectedTo
    ...                Verify LI and LE Consistent and
    ...                Nitro maxBandwidth and servers downlink operationalSpeed

    # take care of HA or Redundant where LE has only 1 LI, do UFG once. Only A+B need to do both LI UFG
    Log    ${\n}Perform LI UFG - remove added uplinksets and add back old deleted ones    console=True
    @{local_lis} =    Run Keyword If    '${LIs[0]}' == '${LIs[1]}'    Create List    ${LIs[0]}
                      ...    ELSE    Copy List    ${LIs}

    :FOR    ${li}    IN    @{local_lis}
    \    Perform LI Update From Group    ${li}    ${data_common.UFG_WAIT}    30s

    Run Keyword And Continue On Failure    Verify Happy LE and LI


OVF3323 Create 4 Server Profiles Each With 2 FabricAttach Connections, Verify Profile status
    [Tags]  SP    Happy

    :FOR     ${sp}    IN     @{server_profiles}
    \    Create Server Profile    ${sp}    ${data_common.SP_CREATE_WAIT}    20s
    \    Run Keyword And Continue On Failure    Verify Server Profile Status    ${sp['name']}    OK


OVF3323 Power On Servers, Verify Servers Connections through uplink port loginsCount
    [Tags]  ServerEnd2End    Happy

    # power on servers
    Run Keyword for List    ${server_hws}    Power on Server

    # use BFS_SERVER_BOOT_WAIT when bfs servers are added
    Log    ${\n}Waiting ${data_common.BFS_SERVER_BOOT_WAIT} minutes for servers to boot and come up
    ...    console=True
    Sleep    ${data_common.BFS_SERVER_BOOT_WAIT}

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    Run Keyword And Continue On Failure    Verify Server Profiles Status    ${server_profile_names}    OK

    Verify Happy Servers FA Connections


OVF3323 Change FA uplink speed Case 1, Update LI Aside uplinkset uplink speed from 16Gb and 32Gb to 8Gb
    [Tags]  UplinkSpeedChangeA    speedChange

    Log    ${\n}Edit LI US-FA1 uplinks from 16Gb and 32Gb to 8Gb    console=True

    Perform Edit LI UplinkSet    ${li_uplinksets['US_FA1_8Gb']['name']}
    ...                          ${li_uplinksets['US_FA1_8Gb']}    ${LIs[0]}

    Verify Logical Interconnect    ${LIs[0]}    status=Warning    consistencyStatus=NOT_CONSISTENT

    Log     ${\n}Wait and Verify uplink updated operational speed, not affecting servers logins    console=True
    :FOR    ${uplink}    IN    @{US_FA1_UPLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_SPEED_WAIT}    20s
    \    ...    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked
    \    ...            operationalSpeed=${data_common.OPSPEED8}    loginsCount=2

    # In the past, in HA environment, changing Aside uplink spped affect Bside same uplink port speed
    Log     ${\n}Verify Bside uplink speed not affected.    console=True
    Verify Port    ${NITROB}    ${US_FA2_UPLINKS[0]}    status=OK    portStatus=Linked
    ...            operationalSpeed=${data_common.OPSPEED16}    loginsCount=2

    Log    ${\n}Verify server profiles status going through US-FA1 are not affected    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles Status    ${server_profile_names}    OK

    Verify Happy Servers FA Connections


OVF3323 Change uplink speed Case 2, LI UFG change Aside uplinkset uplink speed back to 16Gb and 32G
    [Tags]  LIUFGSpeedChangeA    speedChange

    Log    ${\n}Perform LI update from group to change uplink speed back    console=True
    Perform LI Update From Group    ${LIs[0]}    ${data_common.UFG_WAIT}    30s

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    Log     ${\n}Verify server profiles status going through US-FA1 are not affected    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Servers FA Connections


OVF3323 Change FA uplink speed Case 3, Update LI Bside uplinkset uplink speed from 16Gb and 32Gb to 8Gb and 16Gb
    [Tags]  UplinkSpeedChangeB    speedChange

    Log    ${\n}Edit LI US-FA2 uplinks from 16Gb and 32Gb to 8 and 16Gb    console=True

    Perform Edit LI UplinkSet    ${li_uplinksets['US_FA2_8Gb_16Gb']['name']}
    ...                          ${li_uplinksets['US_FA2_8Gb_16Gb']}    ${LIs[1]}

    Verify Logical Interconnect    ${LIs[1]}    status=Warning    consistencyStatus=NOT_CONSISTENT

    # In the past, in HA environment, changing Aside uplink spped affect Aside same uplink port speed
    Log     ${\n}Verify Bside uplink speed changed.    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_SPEED_WAIT}    20s
    ...    Verify Port    ${NITROB}    ${US_FA2_UPLINKS[0]}    status=OK    portStatus=Linked
    ...            operationalSpeed=${data_common.OPSPEED8}    loginsCount=2

    Wait Until Keyword Succeeds    ${data_common.UPLINK_SPEED_WAIT}    20s
    ...    Verify Port    ${NITROB}    ${US_FA2_UPLINKS[1]}    status=OK    portStatus=Linked
    ...            operationalSpeed=${data_common.OPSPEED16}    loginsCount=2

    Log     ${\n}Verify Aside same uplink speed not affected.    console=True
    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[0]}    status=OK    portStatus=Linked
    ...            operationalSpeed=${data_common.OPSPEED16}    loginsCount=2

    Log    ${\n}Verify server profiles status going through US-FA2 are not affected    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles Status    ${server_profile_names}    OK

    Verify Happy Servers FA Connections


OVF3323 Change uplink speed Case 4, LI UFG change Bside uplinkset uplink speed back to 16Gb and 32G
    [Tags]  LIUFGSpeedChangeB    speedChange

    Log    ${\n}Perform LI update from group to change uplink speed back    console=True
    Perform LI Update From Group    ${LIs[1]}    ${data_common.UFG_WAIT}    30s

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    Log     ${\n}Verify server profiles status going through US-FA1 are not affected    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Servers FA Connections


OVF3323 Disable Uplinks Case 1, Affect Servers Aside Connection
    [Tags]  DisableUplinkA    DisEnaUplinkA    DisEnaUL
    [Documentation]    Disable Aside US-FA1 uplinkport Q4:2 and Q3:1
    ...                US-FA1 has 2 uplinkports Q4:2 and Q3:1, disabling 1 port at a time.
    ...                Disable 1 out of 2, expect uplinkset in Warning status, no profile connection error
    ...                Disable both uplinks, expect uplinkset in Critical status, and cause profile connection error.


    Log    ${\n}Disable US-FA1 first uplink ${US_FA1_UPLINKS[0]}    console=True
    ${disabled_ports} =    Create List    ${US_FA1_UPLINKS[0]}
    Disable Ports    ${NITROA}    ${disabled_ports}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify affected uplinkset status    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[0]}    US-FA1    Warning

    Log    ${\n}Verify server profiles status going through US-FA1 still OK    console=True
    Verify Server Profiles status    ${server_profile_names}    OK

    Log    ${\n}Verify servers logins through remaining uplinkport ${US_FA1_UPLINKS[1]}    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[1]}    loginsCount=4

    Log    ${\n}Disable US-FA1 second uplink ${US_FA1_UPLINKS[1]}    console=True
    ${disabled_ports} =    Create List    ${US_FA1_UPLINKS[1]}

    Disable Ports    ${NITROA}    ${disabled_ports}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify affected uplinkset status    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[0]}    US-FA1    Critical

    Log    ${\n}Verify server profiles status going through US-FA1 become Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    Critical

    Log    ${\n}Verify no server logins to these 2 uplinkports    console=True
    :FOR    ${ul}    IN    @{US_FA1_UPLINKS}
    \    Verify Port    ${NITROA}    ${ul}    loginsCount=0

    Log    ${\n}Verify servers logins on Bside not impacted    console=True
    Run Keyword And Continue On Failure    Verify Happy Servers Bside FA Connections


OVF3323 Enable back Uplinks Case 1, Aside Connection Restoration, Verify Server Connections and login redistribution
    [Tags]  EnableUplinkA    DisEnaUplinkA    DisEnaUL
    [Documentation]    Enable Aside US-FA1 uplinkports one at a time
    ...                When one uplinkport is enabled back, all servers can login through this uplinkport
    ...                Profiles connection should be OK.
    ...                After second uplinkport is enabled back, server logins should be evenly redistributed


    Log    ${\n}Enable back Aside US-FA1 uplinkports one at a time, enable ${US_FA1_UPLINKS[0]}
    ...    console=True
    ${ports} =    Create List    ${US_FA1_UPLINKS[0]}
    Enable Ports     ${NITROA}    ${ports}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify affected uplinkset in Warning status    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[0]}    US-FA1    Warning

    Log      ${\n}Verify Server Profiles status back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Log    ${\n}Verify servers logins through enabled uplinkport ${US_FA1_UPLINKS[0]}
    ...    console=True
    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[0]}    loginsCount=4

    Log     ${\n}Enable back Aside US-FA1 second uplinkport ${US_FA1_UPLINKS[1]}
    ...    console=True
    ${ports} =    Create List    ${US_FA1_UPLINKS[1]}
    Enable Ports     ${NITROA}    ${ports}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify affected uplinksets back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[0]}    US-FA1    OK

    Log    ${\n}Verify servers logins evenly redistribute between the uplinkports    console=True
    Verify Happy Servers Aside FA Connections


OVF3323 Disable Uplinks Case 2, Affect Server Bside Connection, Verify servers connection thru loginsCount
    [Tags]  DisableUplinkB    DisEnaUplinkB    DisEnaUL
    [Documentation]    Disable Bside US-FA2 both uplinkports in one update port REST call
    ...                Expect Uplinkset Critical, profile connection error
    ...                uplinkports loginsCount 0


    Disable Ports    ${NITROB}    ${US_FA2_UPLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify affected uplinkset Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[1]}    US-FA2    Critical

    Log      ${\n}Verify Server Profiles status Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    Critical

    Log    ${\n}Verify no server logins through these 2 disabled uplinkports    console=True
    :FOR    ${ul}    IN    @{US_FA2_UPLINKS}
    \    Verify Port    ${NITROB}    ${ul}    loginsCount=0

    Log      ${\n}Verify servers logins on Aside not impacted    console=True
    Verify Happy Servers Aside FA Connections


OVF3323 Enable back Uplinks Case 2, Bside Connection Restoration, Verify servers connection through loginsCount
    [Tags]  EnableUplinkB    DisEnaUplinkB    DisEnaUL
    [Documentation]    Enable Bside US-FA2 both uplinkports through the same update port REST call
    ...                Expect uplinkset back to OK and profiles connection should be OK.
    ...                server logins should be evenly distributed bteween the 2 uplinks


    Enable Ports    ${NITROB}    ${US_FA2_UPLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify affected uplinkset back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[1]}    US-FA2    OK

    Log      ${\n}Verify Server Profiles status back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Log      ${\n}Verify servers logins evenly distributed between the Bside uplinks    console=True
    Verify Happy Servers FA Connections


OVF3323 Disable Downlinks Case 1, Affect Servers Aside Connection, Verify servers connection thru loginsCount
    [Tags]  DisableEnable    DisableDownlinkA    DisEnaDL

    Log      ${\n}Disable Aside downlink of one of enc1 and enc2 server    console=True
    ${dl_list} =    Create List     ${enc1_server_2['enc1_downlink']}    ${enc2_server_1['enc1_downlink']}
    Disable Ports    ${NITROA}    ${dl_list}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify downlink status, portStatus and disabled    console=True
    :FOR    ${dl}    IN    @{dl_list}
    \    Verify Port    ${NITROA}    ${dl}    status=Critical    portStatus=Unlinked    enabled=${False}

    @{sp_set1} =    Create List    ${enc1_server_2['sp_name']}    ${enc2_server_1['sp_name']}
    Log      ${\n}Verify Server Profiles with disabled downlink status Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${sp_set1}    Critical

    Log    ${\n}Verify Server Profiles without disabled downlink status OK    console=True
    @{sp_set2} =    Create List    ${enc1_server_1['sp_name']}    ${enc2_server_2['sp_name']}
    Verify Server Profiles status    ${sp_set2}    OK

    Log   ${\n}Verify affected Aside downlink servers Bside connection not impacted    console=True
    Run Keyword And Continue On Failure    Verify Happy Servers Bside FA Connections


OVF3323 Enable Back Downlinks Case 1, Aside Connection Restoration, Verify servers connection thru loginsCount
    [Tags]  DisableEnable    EnableDownlinkA    DisEnaDL

    ${dl_list} =    Create List     ${enc1_server_2['enc1_downlink']}    ${enc2_server_1['enc1_downlink']}
    Enable Ports    ${NITROA}    ${dl_list}    ${data_common.SUBPORT_STATUS_WAIT}

    #Verify server profiles status back to OK
    Log      ${\n}Verify Server Profiles status back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Log to Console    ${\n}Verify downlink status, portStatus and enabled
    :FOR    ${dl}    IN    @{dl_list}
    \    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked    enabled=${True}

    Run Keyword And Continue On Failure    Verify Servers Downlink Speed

    Log    ${\n}Verify affected servers now login thru Aside uplinks    console=True
    Run Keyword And Continue On Failure    Verify Happy Servers Aside FA Connections


OVF3323 Disable Downlinks Case 2, Affect Servers Bside Connection, Verify servers connection thru loginsCount
    [Tags]  DisableEnable    DisableDownlinkB    DisEnaDL

    Log    ${\n}Disable Bside downlink of one of enc1 and enc2 server    console=True
    ${dl_list} =    Create List     ${enc1_server_1['enc2_downlink']}    ${enc2_server_2['enc2_downlink']}
    Disable Ports    ${NITROB}    ${dl_list}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify downlink status, portStatus and disabled    console=True
    :FOR    ${dl}    IN    @{dl_list}
    \    Verify Port    ${NITROB}    ${dl}    status=Critical    portStatus=Unlinked    enabled=${False}

    @{sp_set1} =    Create List    ${enc1_server_1['sp_name']}    ${enc2_server_2['sp_name']}
    Log      ${\n}Verify Server Profiles with disabled downlink status Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${sp_set1}    Critical

    Log      ${\n}Verify Server Profiles without disabled downlink status OK    console=True
    @{sp_set2} =    Create List    ${enc1_server_2['sp_name']}    ${enc2_server_1['sp_name']}
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${sp_set2}    OK

    Log    ${\n}Verify affected Bside downlink servers Aside connection not impacted    console=True
    Run Keyword And Continue On Failure    Verify Happy Servers Aside FA Connections


OVF3323 Enable Back Downlinks Case 2, Bside Connection Restoration, Verify servers connection thru loginsCount
    [Tags]  DisableEnable    EnableDownlinkB    DisEnaDL

    ${dl_list} =    Create List     ${enc1_server_1['enc2_downlink']}    ${enc2_server_2['enc2_downlink']}
    Enable Ports    ${NITROB}    ${dl_list}    ${data_common.SUBPORT_STATUS_WAIT}

    #Verify server profiles status back to OK
    Log      ${\n}Verify Server Profiles status back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Log to Console    ${\n}Verify downlink status, portStatus and enabled
    :FOR    ${dl}    IN    @{dl_list}
    \    Verify Port    ${NITROB}    ${dl}    status=OK    portStatus=Linked    enabled=${True}

    Run Keyword And Continue On Failure    Verify Servers Downlink Speed

    Log    ${\n}Verify affected servers now login thru Bside uplinks    console=True
    Run Keyword And Continue On Failure    Verify Happy Servers Bside FA Connections


OVF3323 Efuse Remove Aside Nitro Affecting Aside connections, Verify servers Bside connection thru loginsCount
    [Tags]  RemoveA    efuse    efuseA
    [Documentation]    Remove Aside Nitro affecting servers connection through US-FA1
    ...                Expect uplinkset defined on Aside Critical status, and profiles connection error
    ...                server logins on Bside should not be affected

    Log    ${\n}Remove Aside Nitro and wait for Absent state    console=True
    Efuse IC and Wait    ${NITROA}    EFuseOn

    Log     ${\n}Verify Bside Interconnect become Master, remains Configured    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${NITROB}    state=Configured
    ...    stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify Aside uplinksets Critical    console=True
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Uplinkset Status    ${LIs[0]}    ${us}    Critical

    Log      ${\n}Verify Profile status Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    Critical

    Log     ${\n}Verify FA Bside Uplinks status and portStatus not impacted    console=True
    :FOR    ${uplink}    IN    @{IC6_FA_UPLINKS}
    \    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Bside uplinksets OK, not impacted    console=True
    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LIs[1]}    ${us}    OK

    Log     ${\n}Verify servers FA connection on Bside not impacted    console=True
    Verify Happy Servers Bside FA Connections


OVF3323 Efuse Insert Aside Nitro Restoring Aside connections, Verify servers connection thru loginsCount
    [Tags]  InsertA    efuse    efuseA
    [Documentation]    Insert back Aside Nitro affecting servers connection through US-FA1
    ...                Expect uplinkset defined on Aside back to OK, and profiles connection OK
    ...                servers connection path through Aside is restored


    Log    ${\n}Insert back Aside Nitro and wait for Configured state    console=True
    Efuse IC and Wait    ${NITROA}    EFuseOff

    Log     ${\n}Verify Aside Interconnect up as Subordinate    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect    ${NITROA}    stackingDomainRole=${data_common.SUBORDINATE}

    Log     ${\n}Verify Bside Interconnect remains Configured    console=True
    Verify Named Interconnect    ${NITROB}    state=Configured
    ...          stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify FA Uplinks status, portStatus and speed    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[1]}    status=OK    portStatus=Linked
    ...                          operationalSpeed=${data_common.OPSPEED32}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[0]}    status=OK    portStatus=Linked
    ...                          operationalSpeed=${data_common.OPSPEED16}

    Log     ${\n}Verify Bside FA Uplinks status and portStatus    console=True
    :FOR    ${uplink}    IN    @{IC6_FA_UPLINKS}
    \    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside downlinks Linked OK    console=True
    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked

    # Note: it took longer time for Uplinkset status change on Nitro
    Log     ${\n}Verify Aside and Bside uplinksets OK    console=True
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LIs[1]}    ${us}    OK

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    Log     ${\n}Verify Servers Profile status OK    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    OK

    Log     ${\n}Verify servers storage path on both Aside Bside are OK    console=True
    Verify Happy Servers FA Connections


OVF3323 Efuse Remove Bside Nitro Affecting Bside connections, Verify servers Aside connection thru loginsCount
    [Tags]  RemoveB    efuse    efuseB
    [Documentation]    Remove Bside Nitro affecting servers connection through US-FA2
    ...                Expect uplinkset defined on Bside Critical status, and profiles connection error
    ...                server logins on Aside should not be affected


    Log    ${\n}Remove Bside Nitro and wait for Absent state    console=True
    Efuse IC and Wait    ${NITROB}    EFuseOn

    Log     ${\n}Verify Aside Interconnect become Master, remains Configured    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${NITROA}    state=Configured
    ...                                      stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify Bside uplinksets Critical    console=True
    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Uplinkset Status    ${LIs[1]}    ${us}    Critical

    Log      ${\n}Verify Profile status Critical    console=True
    Verify Server Profiles status    ${server_profile_names}    Critical

    Log     ${\n}Verify Aside FA Uplinks status and portStatus not impacted    console=True
    :FOR    ${uplink}    IN    @{IC3_FA_UPLINKS}
    \    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside downlinks Linked OK not impacted    console=True
    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside uplinksets OK, not impacted    console=True
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    Log     ${\n}Verify servers FA connection on Aside not impacted    console=True
    Verify Happy Servers Aside FA Connections


OVF3323 Efuse Insert Bside Nitro Restoring Bside connections, Verify servers connection thru loginsCount
    [Tags]  InsertB    efuse    efuseB
    [Documentation]    Insert back Bside Nitro affecting servers connection through US_FA2
    ...                Expect uplinkset defined on Bside back to OK, and profiles connection OK
    ...                servers connection path through Bside is restored


    Log    ${\n}Insert back Bside Nitro and wait for Configured state    console=True
    Efuse IC and Wait    ${NITROB}    EFuseOff

    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect    ${NITROB}    stackingDomainRole=${data_common.SUBORDINATE}

    Log     ${\n}Verify Aside Interconnect remains Configured, Master    console=True
    Verify Named Interconnect    ${NITROA}    state=Configured
    ...          stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify Bside FA Uplinks status, portStatus and speed    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROB}    ${US_FA2_UPLINKS[1]}    status=OK    portStatus=Linked
    ...                          operationalSpeed=${data_common.OPSPEED32}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROB}    ${US_FA2_UPLINKS[0]}    status=OK    portStatus=Linked
    ...                          operationalSpeed=${data_common.OPSPEED16}

    :FOR    ${uplink}    IN    @{IC3_FA_UPLINKS}
    \    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Bside downlinks Linked OK    console=True
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROB}    ${dl}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside and Bside uplinksets OK    console=True
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    # Note: it takes longer time for uplinkset on Nitro turn OK
    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Uplinkset Status    ${LIs[1]}    ${us}    OK

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    Log     ${\n}Verify Profile status OK    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    OK

    Log     ${\n}Verify servers storage path on both Aside Bside are OK    console=True
    Verify Happy Servers FA Connections


OVF3323 Power Off Aside Nitro Affecting Aside connections, Verify servers Bside connection thru loginsCount
    [Tags]  PowerOffA    PowerA    Power
    [Documentation]    Power off Aside Nitro affecting servers connection through US-FA1
    ...                Expect uplinkset defined on Aside Critical status, and profiles connection error
    ...                server logins on Bside should not be affected

    Log    ${\n}Power off Aside Nitro and wait for Maintenance state    console=True
    Power IC and Wait    ${NITROA}    Off

    Log     ${\n}Verify Bside Interconnect remains Configured and become Master    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect    ${NITROB}    stackingDomainRole=${data_common.MASTER}

    # In recenet build, profiles, LI and uplinksets are no longer guranteed to be Critical
    # Engineer - after ICM is maintenance, the SDS is not polled hence port status is not updated
    # remove verification
    # Log to Console     ${\n}Verify Aside uplinksets Critical
    # :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    # \    Verify Uplinkset Status    ${LIs[0]}    ${us}    Critical
    # Log to Console      ${\n}Verify Profile status Critical
    # Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    Critical

    Log     ${\n}Verify Bside FA Uplinks portStatus not impacted    console=True
    :FOR    ${uplink}    IN    @{IC6_FA_UPLINKS}
    \    Run Keyword And Continue On Failure    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Bside uplinksets OK, not impacted    console=True
    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Run Keyword And Continue On Failure    Verify Uplinkset Status    ${LIs[1]}    ${us}    OK

    Log     ${\n}Verify servers Bside FA connection not impacted    console=True
    Verify Happy Servers Bside FA Connections


OVF3323 Power On Aside Nitro Restoring Aside connections, Verify servers connection thru loginsCount
    [Tags]  PowerOnA    PowerA    Power
    [Documentation]    Power back on Aside Nitro affecting servers connection through US-FA1
    ...                Expect uplinkset defined on Aside back to OK, and profiles connection OK
    ...                servers connection path through Aside is restored


    Log    ${\n}Power back on Aside Nitro and wait for Configured state    console=True
    Power IC and Wait    ${NITROA}    On

    Log     ${\n}Verify Aside Interconnect come up as Subordinate    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${NITROA}    stackingDomainRole=${data_common.SUBORDINATE}

    Log     ${\n}Verify Bside Interconnect remain Master, Configured    console=True
    Verify Named Interconnect     ${NITROB}    state=Configured
    ...          stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify FA Uplinks status, portStatus and speed    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[1]}    status=OK    portStatus=Linked
    ...                          operationalSpeed=${data_common.OPSPEED32}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[0]}    status=OK    portStatus=Linked
    ...                          operationalSpeed=${data_common.OPSPEED16}

    Log     ${\n}Verify Aside downlinks back to Linked OK    console=True
    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked

    :FOR    ${uplink}    IN    @{IC6_FA_UPLINKS}
    \    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside and Bside uplinksets OK    console=True
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LIs[1]}    ${us}    OK

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    Log     ${\n}Verify servers Profile status OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    # Verify Servers both Aside and Bside connections are OK
    Verify Happy Servers FA Connections


OVF3323 Add Aside FA uplinkset uplinkports and change existing uplink speed after Power On Enc1 Nitro 3
    [Tags]  AddUplinksAfterPowerA    UpdatePowerA    PowerA    Power
    [Documentation]    Edit uplinkset defined on Aside after powering back on Aside Nitro
    ...                Add 2 uplinkports from 4x32 split port with different speed 8Gb and 32Gb,
    ...                changing existing second uplinkport speed from 32Gb to 16Gb
    ...                expect 4 servers logins OK and redistribute evenly, i.e. each uplink of the
    ...                4 uplinks gets 1 server login

    PASS EXECUTION    Test intended when 4x32Gb cable is available otherwise skip

    Log    ${\n}Edit LI uplinkset US-FA1 add 2 ports and change ${US_FA1_UPLINKS[1]} speed
    ...    console=True

    Perform Edit LI UplinkSet    ${li_uplinksets['US_FA1_Add_Ports_Speed_Change']['name']}
    ...                          ${li_uplinksets['US_FA1_Add_Ports_Speed_Change']}    ${LIs[0]}

    Verify Logical Interconnect    ${LIs[0]}    status=Warning    consistencyStatus=NOT_CONSISTENT

    Log     ${\n}Verify all servers logins evenly redistribute to all 4 uplinks    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[1]}    status=OK    portStatus=Linked
    ...                   loginsCount=1    operationalSpeed=${data_common.OPSPEED16}

    Run Keyword And Continue On Failure    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[0]}
    ...    status=OK    portStatus=Linked    loginsCount=1    operationalSpeed=${data_common.OPSPEED16}

    Run Keyword And Continue On Failure    Verify Port    ${NITROA}    ${IC3_ADDED_UPLINK_PORT_1}
    ...    status=OK    portStatus=Linked    loginsCount=1    operationalSpeed=${data_common.OPSPEED8}

    Run Keyword And Continue On Failure    Verify Port    ${NITROA}    ${IC3_ADDED_UPLINK_PORT_2}
    ...    status=OK    portStatus=Linked    loginsCount=1    operationalSpeed=${data_common.OPSPEED32}

    Log     ${\n}Verify server profiles status going through US-FA1 not affected    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles Status    ${server_profile_names}    OK


OVF3323 LI UFG Remove added uplinkport and change back uplink speed, Servers FA connection verification
    [Tags]  LIUFGRemovePortsAfterPowerA    UpdatePowerA    PowerA    Power
    [Documentation]    UFG removed added uplinkports and change back speed
    ...                Expect uplink back to 2 ports and speed are 16Gb and 32Gb
    ...                Expect servers login evenly redistributed etween the 2 ports

    PASS EXECUTION    Test intended when 4x32Gb cable is available otherwise skip

    Log    ${\n}Perform LI update from group to add back uplinkport    console=True
    Perform LI Update From Group    ${LIs[0]}    ${data_common.UFG_WAIT}    30s

    Log    ${\n}Verify uplinkset and profiles back to OK    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[1]}    portStatus=Linked
    ...                          operationalSpeed=${data_common.OPSPEED32}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[0]}    portStatus=Linked
    ...                          operationalSpeed=${data_common.OPSPEED16}

    Run Keyword And Continue On Failure    Verify Uplinkset Status    ${LIs[0]}    US-FA1    OK

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    Wait Until Keyword Succeeds   ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Log     ${\n}Verify servers logins evenly redistributed    console=True
    Verify Happy Servers Aside FA Connections


OVF3323 Power Off Bside Nitro Affecting Bside connections, Verify servers Aside connection thru loginsCount
    [Tags]  PowerOffB    PowerB    Power
    [Documentation]    Power off Bside Nitro affecting servers connection through US-FA2
    ...                Expect uplinkset defined on Bside Critical, and profiles connection error
    ...                server logins on Aside should not be affected


    Log    ${\n}Power off Bside Nitro and wait for Maintenance state    console=True
    Power IC and Wait    ${NITROB}    Off

    Log     ${\n}Verify Aside Interconnect become Master, remains Configured    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${NITROA}    state=Configured
    ...                 stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify Bside FA Uplinks Unlinked Critical    console=True
    :FOR    ${uplink}    IN    @{IC6_FA_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROB}    ${uplink}    status=Critical    portStatus=Unlinked

    Log     ${\n}Verify Bside downlinks Unlinked Critical    console=True
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROB}    ${dl}    status=Critical    portStatus=Unlinked

    Log     ${\n}Verify Aside FA Uplinks status and portStatus not impacted    console=True
    :FOR    ${uplink}    IN    @{IC3_FA_UPLINKS}
    \    Run Keyword And Continue On Failure    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside uplinksets OK not impacted    console=True
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Run Keyword And Continue On Failure    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    Log     ${\n}Verify servers Aside FA connection not impacted    console=True
    Verify Happy Servers Aside FA Connections


OVF3323 Power On Bside Nitro Restoring Bside connections, Verify servers connection thru loginsCount
    [Tags]  PowerOnB    PowerB    Power
    [Documentation]    Power back on Bside Nitro affecting servers connection through US-FA2
    ...                Expect uplinkset defined on Bside back to OK, and profiles connection OK
    ...                servers connection path through Bside is restored

    Log     ${\n}Power back on Bside Nitro and wait for Configured state    console=True
    Power IC and Wait    ${NITROB}    On

    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${NITROB}    stackingDomainRole=${data_common.SUBORDINATE}

    Log     ${\n}Verify Aside Interconnect remain Master, Configured    console=True
    Verify Named Interconnect     ${NITROA}    state=Configured     stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify Bside FA Uplinks status, portStatus and speed    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROB}    ${US_FA2_UPLINKS[1]}    status=OK    portStatus=Linked
    ...                          operationalSpeed=${data_common.OPSPEED32}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROB}    ${US_FA2_UPLINKS[0]}    status=OK    portStatus=Linked
    ...                          operationalSpeed=${data_common.OPSPEED16}

    Log     ${\n}Verify Aside FA Uplinks status and portStatus    console=True
    :FOR    ${uplink}    IN    @{IC3_FA_UPLINKS}
    \    Run Keyword And Continue On Failure    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked

    Log      ${\n}Verify Bside downlinks Linked OK    console=True
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROB}    ${dl}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside and Bside uplinksets OK    console=True
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Run Keyword And Continue On Failure    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Uplinkset Status    ${LIs[1]}    ${us}    OK

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    Log      ${\n}Verify servers Profile status back to OK    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    OK

    # Verify Servers FA connections on both Aside and Bside
    Verify Happy Servers FA Connections


OVF3323 Remove Bside FA Uplinkset Uplinkport and Change Uplink Speed after Power on Enc2 Nitro 6
    [Tags]    RemoveUplinkAfterPowerB    UpdatePowerB    PowerB    power
    [Documentation]    Edit uplinkset defined on Bside after powering back on Bside Nitro
    ...                Remove 1 uplinkport and changing remaining port speed, expect servers login
    ...                to remaining uplink
    ...                Verify changed port speed


    Log    ${\n}Edit LI US-FA2 remove ${US_FA2_UPLINKS[1]} and change ${US_FA2_UPLINKS[1]} speed
    ...    console=True

    Perform Edit LI UplinkSet    ${li_uplinksets['US_FA2_Remove_Port_Speed_Change']['name']}
    ...                          ${li_uplinksets['US_FA2_Remove_Port_Speed_Change']}    ${LIs[1]}

    Verify Logical Interconnect    ${LIs[1]}    status=Warning    consistencyStatus=NOT_CONSISTENT

    Log     ${\n}Verify Bside downlinks Linked OK    console=True
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROB}    ${dl}    status=OK    portStatus=Linked

    Log    ${\n}Verify server profiles status OK    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles Status    ${server_profile_names}    OK

    Log     ${\n}Verify remaining uplink speed changed and all servers logins to 1 port    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROB}    ${US_FA2_UPLINKS[1]}    status=OK    portStatus=Linked
    ...                   loginsCount=4    operationalSpeed=${data_common.OPSPEED16}

    Verify Uplinkset Status    ${LIs[1]}    ${li_uplinksets['US_FA2_Remove_Port_Speed_Change']['name']}    OK


OVF3323 LI UFG Add removed uplinkport and change updated speed back, Servers FA redistribute verification
    [Tags]  LIUFGAddPortChangeSpeedAfterPowerB    UpdatePowerB    PowerB    Power
    [Documentation]    LI UFG Add removed uplink for uplinkset defined on Bside, and change speed back
    ...                Verify servers logins redisgribute through the uplink ports
    ...                Verify expected uplinkports speed


    Log    ${\n}Perform LI update from group to add removed uplinkport    console=True
    Perform LI Update From Group    ${LIs[1]}    ${data_common.UFG_WAIT}    30s

    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[1]}    US-FA2    OK

    Log    ${\n}Verify ${US_FA2_UPLINKS[1]} speed back to 32Gb    console=True

    Verify Port    ${NITROB}    ${US_FA2_UPLINKS[1]}    status=OK    portStatus=Linked
    ...                   operationalSpeed=${data_common.OPSPEED32}

    Verify Port    ${NITROB}    ${US_FA2_UPLINKS[0]}    status=OK    portStatus=Linked
    ...                   operationalSpeed=${data_common.OPSPEED16}

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Log     ${\n}Verify servers logins evenly redistributed    console=True
    Verify Happy Servers FA Connections


OVF3323 Reset Aside Nitro Affecting Aside connections, Verify servers connections restore afterwards
    [Tags]    reset    resetA
    [Documentation]    Reset Aside Nitro affecting servers connection through US-FA1
    ...                Expect Aside uplinkset back to OK and servers Aside connections restored
    ...                after ICM is back

    Log    ${\n}Reset Aside Nitro and wait for it back to Configured state    console=True
    &{ic_name} =    Create Dictionary    name=${NITROA}
    @{ic_list} =    Create List    ${ic_name}
    Hard Reset Interconnects from list    ${ic_list}

    Log     ${\n}Verify Bside Interconnect become Master, remains Configured    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${NITROB}    state=Configured
    ...           stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify servers Bside FA connection not impacted    console=True
    Run Keyword And Continue On Failure    Verify Happy Servers Bside FA Connections

    Log    ${\n}Wait for Aside ICM back to Configured as Subordinate    console=True
    Wait Until Keyword Succeeds    ${data_common.RESET_IC_WAIT}    30s
    ...    Verify Named Interconnect     ${NITROA}    state=Configured
    ...           stackingDomainRole=${data_common.SUBORDINATE}

    Log    ${\n}Reset will affect Aside uplinks and profile status    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${server_profile_names}    Critical

    Log    ${\n}Wait and verify Aside uplinks back to OK with expected speed    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[1]}    portStatus=Linked
    ...                          operationalSpeed=${data_common.OPSPEED32}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[0]}    portStatus=Linked
    ...                          operationalSpeed=${data_common.OPSPEED16}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Uplinkset Status    ${LIs[0]}    US-FA1    OK

    Log     ${\n}Verify Aside downlinks back to Linked OK    console=True
    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Server Profile status    ${sp}    OK

    Log     ${\n}Verify servers Aside FA connection restored    console=True
    Verify Happy Servers FA Connections


OVF3323 Reset Bside Nitro Affecting Bside connections, Verify servers connections restore afterwards
    [Tags]    reset    resetB
    [Documentation]    Reset Bside Nitro affecting servers connection through US-FA2
    ...                Expect Bside uplinkset back to OK and servers Bside connections restored
    ...                after ICM is back

    Log    ${\n}Reset Bside Nitro and wait for it back to Configured state    console=True
    &{ic_name} =    Create Dictionary    name=${NITROB}
    @{ic_list} =    Create List    ${ic_name}
    Hard Reset Interconnects from list    ${ic_list}

    Log     ${\n}Verify Aside Interconnect become Master, remains Configured    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${NITROA}    state=Configured
    ...           stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify servers Aside FA connection not impacted    console=True
    Run Keyword And Continue On Failure    Verify Happy Servers Aside FA Connections

    # take some time for reset to take effect
    Log    ${\n}Wait for Bside ICM back to Configured as Subordinate    console=True
    Wait Until Keyword Succeeds    ${data_common.RESET_IC_WAIT}    30s
    ...    Verify Named Interconnect     ${NITROB}    state=Configured
    ...           stackingDomainRole=${data_common.SUBORDINATE}

    Log    ${\n}Reset will affect Bside uplinks and profile status    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${server_profile_names}    Critical

    Log    ${\n}Wait and verify Bside uplinks back to OK with expected speed    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROB}    ${US_FA2_UPLINKS[1]}    portStatus=Linked
    ...                          operationalSpeed=${data_common.OPSPEED32}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROB}    ${US_FA2_UPLINKS[0]}    portStatus=Linked
    ...                          operationalSpeed=${data_common.OPSPEED16}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Uplinkset Status    ${LIs[1]}    US-FA2    OK

    Log      ${\n}Verify Bside downlinks Linked OK    console=True
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROB}    ${dl}    status=OK    portStatus=Linked

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Server Profile status    ${sp}    OK

    Log     ${\n}Verify servers FA connection restored    console=True
    Verify Happy Servers FA Connections


OVF5199 Change DLS mode from 25Gb to 50Gb
    [Tags]    DLS    DLSto50    LIDLSto50

    Change LI downlinkSpeedMode to 50Gb FA


OVF5199 Update Quagmire2 servers profile FC connection rbw to 32Gbps
    [Tags]    DLS    DLSto50    SPrbwUpgrade
    [Documentation]    Increate server profiles FC connection rbw to 32Gb

    # finish all profile update first then wait
    :For    ${entry}    IN     @{sp_upgrade_conn_rbw_info}
    \    Edit Profile RBW    ${entry['sp_name']}    ${entry['connections']}

    :For    ${entry}    IN     @{sp_upgrade_conn_rbw_info}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    10s
    \    ...    Verify Server Profile Status    ${entry['sp_name']}    OK

    Verify Happy Servers FA Connections


OVF5199 Change DLS mode from 50Gb to 25Gb Disallowed
    [Tags]    DLS    DLSto25    LIDLSto25Disallow

    PASS EXECUTION IF    '${downlink_mode}' == 'SPEED_25GB'    Skip Test already in 25Gb mode

    ${resp} =    Update LI DownlinkSpeedMode    ${LIs[0]}    SPEED_25GB
    ${task} =    Wait For Task    ${resp}    ${data_common.LI_DLS_CHANGE_WAIT}   20s
    Verify ErrorMessage in taskError    ${task['taskErrors']}
    ...         ${data_common.MSG_CRM_SPEED_CHANGE_SP_RBW_EXCEED_PHYSICAL_BW}


OVF5199 Update Quagmire2 servers profile FC connection rbw to 16Gbps
    [Tags]    DLS    DLSto25    SPrbwDownGrade

    # finish all profile update first then wait
    :For    ${entry}    IN     @{sp_downgrade_conn_rbw_info}
    \    Edit Profile RBW    ${entry['sp_name']}    ${entry['connections']}

    :For    ${entry}    IN     @{sp_downgrade_conn_rbw_info}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    10s
    \    ...    Verify Server Profile Status    ${entry['sp_name']}    OK

    Verify Happy Servers FA Connections


OVF5199 Change DLS mode from 50Gb to 25Gb Allowed
    [Tags]    DLS    DLSto25    LIDLSto25Allow

    PASS EXECUTION IF    '${downlink_mode}' == 'SPEED_25GB'    Skip Test already in 25Gb mode

    ${resp} =    Update LI DownlinkSpeedMode    ${LIs[0]}    SPEED_25GB
    ...                            ${data_common.LI_DLS_CHANGE_WAIT}    20s
    Set Suite Variable    ${downlink_mode}    SPEED_25GB

    Log    ${\n}wait till Nitro maxBandwidth reached 25Gb    console=True
    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Named Interconnect     ${NITROA}    maxBandwidth=SPEED_25G

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Named Interconnect     ${NITROB}    maxBandwidth=SPEED_25G

    Log    ${\n}wait for expected downgrade outage before checking end2end    console=True
    sleep    ${data_common.DLS_DOWNGRADE_OUTAGE_WAIT}

    # BFS server may go down due to both ICM may have outage, wait for BFS erver to come up
    Log    ${\n}Waiting ${data_common.BFS_SERVER_BOOT_WAIT} minutes for servers to boot and come up
    ...    console=True
    Sleep    ${data_common.BFS_SERVER_BOOT_WAIT}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Servers FA Connections

    Verify Servers Downlink Speed

    # Run Keyword for List    ${PING_LIST_A}    Wait For Appliance To Become Pingable


OVF5199 Change DLS mode from 25Gb back to 50Gb
    [Tags]    DLS    DLSto50-2

    Change LI downlinkSpeedMode to 50Gb FA


OVF5199 End of SpeedChange FA Verification
    [Tags]    verifyLEFA

    Verify Happy Servers FA Connections

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    :FOR    ${sp}    IN    @{server_profile_names}
    \    Run Keyword And Continue On Failure    Verify Server Profile status    ${sp}    OK

    # Run Keyword for List    ${PING_LIST_A}    Wait For Appliance To Become Pingable


OVF3233 Final FA Verification
    [Tags]    finalVerifyLEFA

    Verify Happy Servers FA Connections

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    :FOR    ${sp}    IN    @{server_profile_names}
    \    Run Keyword And Continue On Failure    Verify Server Profile status    ${sp}    OK

    # Run Keyword for List    ${PING_LIST_A}    Wait For Appliance To Become Pingable


#OVF3323 Temp get SAN switchshow
#    [Tags]    sanSwitchshow
#    Log    ${\n}get SAN switch switchshow output to a file    console=True
#    SSH to SAN and get switchshow info    ${san_info['ip']}
#    ...        ${san_info['user']}    ${san_info['pwd']}    ${san_info['prompt']}
#
#OVF3323 Temp Verify all ports NPIV
#    [Tags]    verifySanNPIV
#    Log    ${\n}verify NPIV of uplinks from SAN    console=True
#    &{exp_ports_npiv} =    Create Dictionary    8=2    12=2    16=2    20=2
#    Verify all ports NPIV    ${data_common.SAN_NPIV_OUT_FILE}    ${exp_ports_npiv}


*** Keywords ***
Login OV
    [Documentation]    Login to OneView
    Set Log Level    TRACE
    Run Keyword and Ignore Error    Write To ciDebug Log
    Fusion Api Login Appliance    ${appliance_ip}    ${data_common.admin_credentials}

Common Test Setup
    [Documentation]    Pre-condition keyword run before each test case
    # Run Keyword and Ignore Error    Write To ciDebug Log
    Login OV

Common Test Teardown
    [Documentation]    Post-conditions for ALL test cases
    # Pass Execution
    fusion api logout appliance

Suite Precondition Setup
    [Documentation]    Suite Pre-condition setup run before suite start
    ...                - create ethernet and FC networks
    ...                - set up the network preferred and max bw based on the DLS mode setting


    Run Keyword If    '${dls}' == '10'    Set Suite Variable    ${downlink_mode}    SPEED_10GB
    ...    ELSE IF    '${dls}' == '50'    Set Suite Variable    ${downlink_mode}    SPEED_50GB
    ...    ELSE    Set Suite Variable    ${downlink_mode}    SPEED_25GB

    Run Keyword If    '${dls}' == '10'    Set Suite Variable    ${expected_ic_maxbw}    SPEED_10G
    ...    ELSE IF    '${dls}' == '50'    Set Suite Variable    ${expected_ic_maxbw}    SPEED_50G
    ...    ELSE    Set Suite Variable    ${expected_ic_maxbw}    SPEED_25G

    Return from keyword if    ${skipSetup}    is    ${True}

    Login OV

    Add Ethernet Networks from variable   ${ethernet_networks}
    ${enet_typical_bw} =    Set Variable IF    '${downlink_mode}' == 'SPEED_25GB'    4000
    ...                                        '${downlink_mode}' == 'SPEED_50GB'    8000
    ...                                        2000

    # set max bw for network to max 50000, this way when change speed mode, do not need
    # to modify network and server profile to get new maxbw, core speed change will
    # handle this already

    # ${max_bw} =    Set Variable IF    '${downlink_mode}' == 'SPEED_25GB'    25000
    ${max_bw} =    Set Variable IF    '${downlink_mode}' == 'SPEED_25GB'    50000
    ...                               '${downlink_mode}' == 'SPEED_50GB'    50000
    ...                               10000

    :FOR    ${enet}    IN    @{ethernet_networks}
    \    Edit Network Bandwidth    ${enet['name']}   ethernet   ${enet_typical_bw}   ${max_bw}


    Add FC Networks from variable    ${fa_networks}
    Add FC Networks from variable    ${da_networks}

    # Since Quack also work in DLS 50Gb mode, the preferred bw should be 16Gb
    ${fc_typical_bw} =    Set Variable IF    '${downlink_mode}' == 'SPEED_25GB'    16000
    ...                                      '${downlink_mode}' == 'SPEED_50GB'    16000
    ...                                      8000

    :FOR    ${fa}    IN    @{fa_networks}
    \    Edit Network Bandwidth    ${fa['name']}   fc   ${fc_typical_bw}   ${max_bw}

    :FOR    ${da}    IN    @{da_networks}
    \    Edit Network Bandwidth    ${da['name']}   fc   ${fc_typical_bw}   ${max_bw}


Suite Min Teardown
    [Documentation]    Suite Post-condtion cleanup
    Pass Execution    Nothing to cleanup right now
    # fusion api logout appliance


Verify Happy Servers Aside FA Connections
    [Documentation]    Verify Servers Aside FA connections through uplinkport loginsCount
    ...                Ensure servers logins evenly distributed among uplinkset uplink ports

    Log    ${\n}Verify servers Aside FA connections evenly distributed between the uplink ports
    ...    console=True

    :FOR    ${uplink}    IN    @{US_FA1_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.LOGIN_WAIT}    30s
    \    ...    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked    loginsCount=2


Verify Happy Servers Bside FA Connections
    [Documentation]    Verify Servers Bside FA connections through uplinkport loginsCount
    ...                Ensure servers logins evenly distributed among uplinkset uplink ports

    Log    ${\n}Verify servers Bside FA connections evenly distributed between the uplink ports
    ...    console=True

    :FOR    ${uplink}    IN    @{US_FA2_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.LOGIN_WAIT}    30s
    \    ...    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked    loginsCount=2


Verify Happy Servers FA Connections
    [Documentation]    Verify servers both Aside and Bside FA connections through uplinkport loginsCount
    ...                Ensure servers logins evenly distributed among uplinkset uplink ports

    Log    ${\n}Verify servers both Aside and Bside FA connections through uplink loginsCount
    ...    console=True

    Run Keyword And Continue On Failure    Verify Happy Servers Aside FA Connections
    Run Keyword And Continue On Failure    Verify Happy Servers Bside FA Connections

Verify Happy FA Uplinks
    [Documentation]    Verify the common scenario uplinks status, operationalSpeed and connectedTo

    Log     ${\n}Verify Aside and Bside FA Uplinks portStatus, operationalSpeed and connectedTo
    ...    console=True

    # take some time for speed change
    Wait Until Keyword Succeeds   ${data_common.UPLINK_SPEED_WAIT}    30s
    ...    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[0]}    status=OK    portStatus=Linked
    ...            operationalSpeed=${data_common.OPSPEED16}    connectedTo=${CONNECTED_TO_WWN}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_SPEED_WAIT}    30s
    ...    Verify Port    ${NITROA}    ${US_FA1_UPLINKS[1]}    status=OK    portStatus=Linked
    ...            operationalSpeed=${data_common.OPSPEED32}    connectedTo=${CONNECTED_TO_WWN}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_SPEED_WAIT}    30s
    ...    Verify Port    ${NITROB}    ${US_FA2_UPLINKS[0]}    status=OK    portStatus=Linked
    ...            operationalSpeed=${data_common.OPSPEED16}    connectedTo=${CONNECTED_TO_WWN}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_SPEED_WAIT}    30s
    ...    Verify Port    ${NITROB}    ${US_FA2_UPLINKS[1]}    status=OK    portStatus=Linked
    ...            operationalSpeed=${data_common.OPSPEED32}    connectedTo=${CONNECTED_TO_WWN}


Verify Happy LE
    [Documentation]    Verify the common scenario LE happy condition

    Log     ${\n}Verify Both Nitro in Configured state        console=True
    Verify Named Interconnect     ${NITROA}    state=Configured
    Verify Named Interconnect     ${NITROB}    state=Configured

    Log     ${\n}Wait for all uplinkset to reach OK status        console=True
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Uplinkset Status    ${LIs[1]}    ${us}    OK

    Run Keyword And Continue On Failure    Verify Happy FA Uplinks

    Log     ${\n}Verify LE status OK and Consistent    console=True
    Verify Named Logical Enclosure    ${LE}    status=OK    state=Consistent


Verify Happy LE and LI
    [Documentation]    Verify the common scenario LE and LI condition
    ...                Expected Nitro maxBandwidth,
    ...                and server downlinks expected operational Speed
    ...                The LI status may be Warning or OK depending on DLS mode and CXP cabling

    Run Keyword And Continue On Failure    Verify Happy LE
    Verify LI with SpeedMode
    Verify Servers Downlink Speed
    Verify ICM MaxBW


Verify ICM MaxBW
    [Documentation]    Verify the interconnects maxBandwidth

    Log     ${\n}Verify Nitro expected maxBandWidth    console=True

    Run Keyword If    '${downlink_mode}' == 'SPEED_25GB'
    ...            Set Suite Variable    ${expected_ic_maxbw}    SPEED_25G
    ...    ELSE    Set Suite Variable    ${expected_ic_maxbw}    SPEED_50G

    Run Keyword And Continue On Failure
    ...    Verify Named Interconnect     ${NITROA}    maxBandwidth=${expected_ic_maxbw}

    Run Keyword And Continue On Failure
    ...    Verify Named Interconnect     ${NITROB}    maxBandwidth=${expected_ic_maxbw}


Verify Servers Downlink Speed
    [Documentation]    Verify servers downlink is Linked and its operationalSpeed value
    ...                based on LI downlinkSpeedMode and servers MZ card max supported speed.
    ...                With supported LI downlinkSpeed as 25Gb and 50Gb,
    ...                   Quack servers downlink operationalSpeed should be 25Gb
    ...                   Quagmire2 servers downlink operationalSpeed is 25 and 50 respectively

    Log     ${\n}Verify servers expected downlink operationalSpeed    console=True

    :FOR    ${sp}    IN    @{QUACK_SERVERS}
    \    Run Keyword And Continue On Failure    Verify Port    ${NITROA}
    \    ...         ${sp['enc1_downlink']}    portStatus=Linked    operationalSpeed=Speed25G
    \    Run Keyword And Continue On Failure    Verify Port    ${NITROB}
    \    ...         ${sp['enc2_downlink']}    portStatus=Linked    operationalSpeed=Speed25G

    ${exp_speed} =    Set Variable IF    '${downlink_mode}' == 'SPEED_25GB'    Speed25G
    ...               Speed50G

    :FOR    ${sp}    IN    @{QUAG2_SERVERS}
    \    Run Keyword And Continue On Failure    Verify Port    ${NITROA}
    \    ...         ${sp['enc1_downlink']}    portStatus=Linked    operationalSpeed=${exp_speed}
    \    Run Keyword And Continue On Failure    Verify Port    ${NITROB}
    \    ...         ${sp['enc2_downlink']}    portStatus=Linked    operationalSpeed=${exp_speed}


Verify LI with SpeedMode
    [Documentation]    Verify the LE condition taking SpeedMode into consideration
    ...                In API environment, there are 2 CXP cables between Nitro/Methane L1, L2
    ...                working for both LI downlinkSpeedMode 25Gb and 25Gb
    ...                However, with this cabling, there will be Warning alert if running in 25Gb
    ...                downlinkMode. Therefore Warning state if 2 CXP in L1 and L2
    ...                and OK state if 1 CXP between Nitro/Methane L1
    ...                Need to allow both OK and Warning state for LI depending on the speedMode
    ...                and Cabling.

    Log     ${\n}Verify LI status, ConsistencyStatus and downlinkSpeedMode    console=True

    @{local_lis} =    Run Keyword If    '${LIs[0]}' == '${LIs[1]}'    Create List    ${LIs[0]}
                      ...    ELSE    Copy List    ${LIs}

    :FOR    ${li}    IN    @{local_lis}
    \    ${exp_status} =    Set Variable IF    '${downlink_mode}' == 'SPEED_25GB'    ((?i)Warning|OK)
    \    ...                OK
    \    Verify Logical Interconnect    ${li}    status=${exp_status}
    \    ...    consistencyStatus=CONSISTENT    downlinkSpeedMode=${downlink_mode}


Change LI downlinkSpeedMode to 50Gb FA
    [Documentation]    Chage LI DownlinkSpeed mode to 50Gb and perform end2end verification

    PASS EXECUTION IF    '${downlink_mode}' == 'SPEED_50GB'    Skip Test already in 50Gb mode

    Update LI DownlinkSpeedMode    ${LIs[0]}    SPEED_50GB
    ...                            ${data_common.LI_DLS_CHANGE_WAIT}    20s

    Set Suite Variable    ${downlink_mode}    SPEED_50GB

    Log    ${\n}wait till Nitro maxBandwidth reach 50Gb    console=True
    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Named Interconnect     ${NITROA}    maxBandwidth=SPEED_50G

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Named Interconnect     ${NITROB}    maxBandwidth=SPEED_50G

    Log    ${\n}wait for expected upgrade outage before checking end2end    console=True
    sleep    ${data_common.DLS_UPGRADE_OUTAGE_WAIT}

    # BFS server may go down due to both ICM may have outage, wait for BFS erver to come up
    Log    ${\n}Waiting ${data_common.BFS_SERVER_BOOT_WAIT} minutes for servers to boot and come up
    ...    console=True
    Sleep    ${data_common.BFS_SERVER_BOOT_WAIT}

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Servers FA Connections

    # Run Keyword for List    ${PING_LIST_A}    Wait For Appliance To Become Pingable