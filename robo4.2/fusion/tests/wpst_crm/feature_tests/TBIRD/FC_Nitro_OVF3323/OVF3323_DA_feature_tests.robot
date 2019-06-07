*** Settings ***
Documentation    FC DirectAttach on Nitro User Story
...
...    - Goal:
...      |  - Ensure FC DirectAttach end2end work with Nitro ICM (OVF3233)
...      |  - Test with 2 different LI downlinkSpeedMode: 25Gb and 50Gb (OVF4511)
...      |  \ \  to ensure end2end works in both speedMode for Quack and Quagmire2 servers
...      |  - Ensure LI downlinkSpeedMode change to and from 50Gb works
...      |  \ \  any connection outage incurred should be recovered (OVF5199)
...
...    - Usage:
...      |  - full test:
...      |  \ \ Run with LI downlinkSpeedMode 25Gb, default. same as -dls:25
...      |  \ \ - robot -V data_OVF3323_DA_BB56_ha.py -T -d /Result/DA  OVF3323_DA_feature_tests.robot
...      |  \ \ Run with LI downlinkSpeedMode 50Gb, excluding DLS and BFS tests
...      |  \ \ - robot -V data_OVF3323_DA_BB56_ha.py -v dls:50 -e DLS -e BFS
...      |  \ \ \ \  -T -d /Result/DA  OVF3323_DA_feature_tests.robot
...      |  - skip precondition setup: robot -v skipSetup:True -V data_OVF3323_DA_BB56_ha.py
...      |  \ \ \ \ -T -d /Result/DA  OVF3323_DA_feature_tests.robot
...      |  - run tagged cases: robot -V data_OVF3323_DA_BB56_ha.py -i setup -i Happy -i efuse
...      |  \ \ \ \ -T -d /Result/DA  OVF3323_DA_feature_tests.robot
...
...    - The test can test different test enclosures with configuration specified in data file.
...    - The following is BB56 config:
...
...    - LE - 2 frame, HA, IBS3, 2 CXP between Methane and Nitro, total 4 CXP
...
...    - 1 Enet uplinkset on Aside: IC3:Q1 (40Gb Enet)
...    - 1 DA uplinkset on Aside
...      |  - US-DA1: DA1, 2 uplinks, IC3:Q2, Q5, desiredSpeed: 16Gb (1x32Gb SFP)
...    - 1 DA uplinkset on Bside
...      |  - US-DA2: DA2, 2 uplinkd, IC6:Q2:1, Q4:1, desiredSpeed: 16Gb(1x16Gb SFP)
...    - 1 FA uplinkset on Aside
...      |  - US-FA1: FA1. with Auto LoginRedistribution
...      |  - 2 uplinks
...      |  \ \ - IC3:Q3:1 desiredSpeed 16Gb (1x16Gb SFP)
...      |  \ \ - IC3:Q4:1 desiredSpeed 32Gb (1x32Gb SFP)
...    - 1 FA uplinkset on Bside
...      |  - US-FA2: FA2, with Manual LoginRedistribution, treated as Auto on Nitro and Potash
...      |  - 2 uplinks
...      |  \ \ - IC6:Q3 desiredSpeed 16Gb (1x16Gb SFP)
...      |  \ \ - IC6:Q5 desiredSpeed 32Gb (1x32Gb SFP)
...
...    - Note:
...      |  - 3par partner ports need to be in the same Fabric, hence have to be in the same DA uplinkset
...      |  - 3par currently only support 16Gb
...
...    - 4 servers: 2 FC DA connections (DA1 and DA2 connections)
...      |  - All servers are WS2016
...      |  - total 4 servers: each frame: 2 servers, 1 with Quack, 1 with Quagmire2
...      |  - among the 4 servers, 2 BFS servers, one on each side, with Quack and Quagmire2
...
...    - Minimum 4 servers going through each uplinkset locally or through Methane for storage access
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
...      |  \ \ - uplink speed change (16 to 8) on LI uplinkset, and UFG change back to 16 from 8
...      |  \ \ - disable/enable Aside uplinks
...      |  \ \ \ \ - disable 1 uplink at a time
...      |  \ \ \ \ - enable back both uplinks at a time
...      |  \ \ - disable/enable Bside uplinks
...      |  \ \ \ \ - disable both uplinks at a time
...      |  \ \ \ \ - enable back 1 uplink at a time
...      |  \ \ - disable/enable downlinks, Aside and Bside,
...      |  \ \ \ \ - one enc1 and enc2 servers for Aside, different enc1 and enc2 servers for Bside
...      |  \ \ - Power off/on Nitro (Aside and Bside)
...      |  \ \ - Remove/insert Nitro (Aside and Bside)
...      |  \ \ - reset Nitro (Aside and Bside)
...
...    - Server DA storage path verification are through
...      |  \ \ - server downlink connectionMap of OneView ICM nameServers
...      |  \ \ - 3par DA port attached devices through 3par cli 'showportdev ns <port>'
...
...    - Ensure all servers lost connection can recover for the aforementioned scenarios
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
OVF3323 Negative LIG FC DA Uplinkset
    [Tags]  LigUSNegative    Negative
    [Documentation]    The following are tested: limitations for FC DA uplinkset defined on LIG
    ...                CRM_INVALID_UPLINK_SET_PORT
    ...                    case - IRF split port
    ...                    case - IRF unsplit port
    ...                CRM_LOGICAL_UPLINK_TEMPLATE_FIBRE_CHANNEL_PORTS_DO_NOT_ALL_BELONG_TO_SAME_SWITCH
    ...                CRM_LOGICAL_UPLINK_CAN_ONLY_CONTAIN_MAX_ONE_FC_NETWORK
    ...                CRM_BOTH_SPLIT_AND_UNSPLIT_PORTS_USED_IN_UPLINK_SETS
    ...                CRM_INVALID_DESIRED_PORT_SPEED
    ...                    cases - Auto/2Gb/4Gb
    ...                    case - not specify speed

    PASS EXECUTION IF    '${REDUNDANCY}' == 'AB'    Skip Negative Test If Redundancy is A plus B

    Log    ${\n}FC FA uplinkset on LIG negative test    console=True
    :FOR    ${ligtest}    IN    @{err_ligs}
    \    ${body} =    Build LIG body    ${ligtest['ligBody']}
    \    ${task} =    Fusion Api Create LIG    ${body}
    \    ${resp} =    Wait for Task2    ${task}    2m    5
    \    ...                                       PASS=Error
    \    ...                                       errorMessage=${ligtest['errorCode']}


OVF3323 Create Logical Enclosure and Verify LI LE and uplinks status and speed
    [Documentation]   Create 2 FRAME ME HA IBS3 LE with DA Uplinksets defined on each side
    [Tags]  LE    setup

    Run Keyword for List    ${ligs}    Add LIG from variable

    # create EG
    Add Enclosure Group from variable    ${enc_group['${EG}']}

    Add Logical Enclosure from variable    ${les['${LE}']}

    # Need to continue so that downlinkSpeedMode will be set as specified
    Run Keyword And Continue On Failure    Verify Happy LE

    Log    ${\n}Change LI downlinkSpeedMode to ${downlink_mode}    console=True
    Run Keyword if    '${downlink_mode}' != 'SPEED_25GB'
    ...    Update LI DownlinkSpeedMode    ${LIs[0]}    ${downlink_mode}
    ...                                   ${data_common.LI_DLS_CHANGE_WAIT}    20s

    Log    ${\n}wait till Nitro maxBandwidth reached ${expected_ic_maxbw}    console=True
    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Named Interconnect     ${NITROA}    maxBandwidth=${expected_ic_maxbw}

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Named Interconnect     ${NITROB}    maxBandwidth=${expected_ic_maxbw}

    Run Keyword And Continue On Failure    Verify LI with SpeedMode

    Wait Until Keyword Succeeds    ${data_common.SERVERS_INIT_DLS_WAIT}    20s
    ...    Verify Servers Downlink Speed


OVF3323 Verify all DA uplinkports connected 3par portWWN
    [Tags]   IC    setup    DAUplinks

    Verify Happy Uplinks DA ports


OVF3323 LI DA Uplinksets Negative Tests
    [Tags]  LiUSNegative    Negative
    [Documentation]    The following are tested: limitations for FC DA uplinkset on LI
    ...                CRM_BOTH_SPLIT_AND_UNSPLIT_PORTS_USED_IN_UPLINK_SETS
    ...                CRM_PORT_CONFIG_INFO_LOCATION_IS_NOT_FC_UPLINK_CAPABLE
    ...                    case - IRF split port
    ...                    case - IRF unsplit port
    ...                CRM_PORTS_IN_DIFFERENT_SWITCH
    ...                CRM_LOGICAL_UPLINK_CAN_ONLY_CONTAIN_MAX_ONE_FC_NETWORK
    ...                CRM_PORT_ALREADY_ASSIGNED
    ...                CRM_PORT_NUMBER_UNKNOWN_FORMAT
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
    \    ${resp} =    Wait for Task2    ${task}    3m    5
    \    ...                                       PASS=Error
    \    ...                                       errorMessage=${li_us['errorCode']}


OVF3323 DA - Delet All LI uplinksets
    [Tags]  DeleteUS    LiUSPortStatusReason
    [Documentation]    Delete All LI Uplinksets
    ...                Testing Delete of uplinkset, verify LI become Inconsistent
    ...                Also free up uplinks for portStatusReason testing

    Remove All Uplinksets

    Log    ${\n}Remove all uplinksets and wait until uplinks are Unlinked    console=True
    :FOR    ${uplink}    IN    @{US_DA1_UPLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Port    ${NITROA}    ${uplink}    portStatus=Unlinked

    :FOR    ${uplink}    IN    @{US_DA2_UPLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Port    ${NITROB}    ${uplink}    portStatus=Unlinked

    :FOR    ${li}    IN    @{LIs}
    \    Verify Logical Interconnect    ${li}    status=Warning    consistencyStatus=NOT_CONSISTENT


OVF3323 LI DA Uplinksets uplink Unlink various portStatusReason cases
    [Tags]  LiUSPortStatusReason    statusReason
    [Documentation]    The following are tested Uplinkset is created but uplink Unlinked with
    ...                portStatusReason
    ...                Split port format on 1x SFP - None with Alert
    ...                DA uplink on port connected to SAN switch - FabricTypeMismatch
    ...                FA uplink on port without SFP - Unpopulated
    ...                DA uplink with speed not supported on SFP - FcSpeedMismatch
    ...                DA uplink on port connected to Enet switch - ModuleIncompatible
    ...                Unsplit port format on 4x QSFP - Unknown? (when 4x QSFP available)

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


OVF3323 LI Update From Group Remove added DA uplinksets and Add back deleted old ones
    [Tags]  LiUSPortStatusReason    LIUFGAddUS
    [Documentation]    LI update from group - remove and add back DA uplinksets
    ...                Verify DA uplinkset status, uplinkport operationalSpeed and connectedTo
    ...                Verify LI and LE Consistent and
    ...                Nitro maxBandwidth and servers downlink operationalSpeed

    Log    ${\n}Perform LI UFG - remove added uplinksets and add back old deleted ones    console=True
    @{local_lis} =    Run Keyword If    '${LIs[0]}' == '${LIs[1]}'    Create List    ${LIs[0]}
                      ...    ELSE    Copy List    ${LIs}

    Log    ${\n}Perform LI UFG - remove added uplinksets, add back old deleted ones    console=True
    :FOR    ${li}    IN    @{local_lis}
    \    Perform LI Update From Group    ${li}    ${data_common.UFG_WAIT}    30s

    Verify Happy LE and LI


OVF3323 Create 4 Server Profiles Each With 2 DirectAttach Connections, Verify Profile status
    [Tags]  SP    Happy

    :FOR     ${sp}    IN     @{server_profiles}
    \    Create Server Profile    ${sp}    ${data_common.SP_CREATE_WAIT}    20s
    \    Run Keyword And Continue On Failure    Verify Server Profile Status    ${sp['name']}    OK


OVF3323 Power On Servers, Verify Servers DA Connections
    [Tags]  ServerEnd2End    Happy

    # power on servers
    Run Keyword for List    ${server_hws}    Power on Server

    # use BFS_SERVER_BOOT_WAIT when bfs servers are added
    Log to Console    ${\n}Waiting ${data_common.SERVER_BOOT_WAIT} minutes for servers to boot and come up
    # Sleep    ${data_common.SERVER_BOOT_WAIT}
    Sleep    ${data_common.BFS_SERVER_BOOT_WAIT}

    # DF UNCOMMENT when enet connections are OK
    # Run Keyword for List    ${PING_LIST_A}    Wait For Appliance To Become Pingable

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    Run Keyword And Continue On Failure    Verify Server Profiles Status    ${server_profile_names}    OK

    # Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Servers DA Connections

    # Double check DA connected 3par port attached devices
    Verify Happy DA 3par ports Attached Devices


OVF3323 Change DA uplink speed Case 1, Update LI uplinkset uplink speed from 16Gb to 8Gb, Verifications
    [Tags]  UplinkSpeedChange1    speedChange
    [Documentation]    Change Aside DA uplinks speed
    ...                Verify
    ...                - speed change accordingly
    ...                - not affecting severs connections
    ...                - LI become Inconsistent

    Log    ${\n}Edit LI uplinkset US-DA1 uplinks from 16Gb to 8Gb    console=True
    Perform Edit LI UplinkSet    ${li_uplinksets['US_DA1_8Gb']['name']}
    ...                          ${li_uplinksets['US_DA1_8Gb']}    ${LIs[0]}

    Verify Logical Interconnect    ${LIs[0]}    status=Warning    consistencyStatus=NOT_CONSISTENT

    Log     ${\n}Verify uplink updated speed, not affecting servers connections    console=True
    :FOR    ${uplink}    IN    @{US_DA1_UPLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_SPEED_WAIT}    20s
    \    ...    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked
    \    ...            operationalSpeed=${data_common.OPSPEED8}

    # In the past, in HA environment, changing Aside uplink spped affect Bside same uplink port speed
    Log     ${\n}Verify Bside uplink speed not affected.    console=True
    :FOR    ${uplink}    IN    @{US_DA2_UPLINKS}
    \    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked
    \    ...            operationalSpeed=${ORIG_UPLINK_SPEED}

    Log    ${\n}Verify server profiles status going through US-DA1 are not affected    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles Status    ${server_profile_names}    OK

    Verify Happy Servers DA Connections

    Verify Happy DA 3par ports Attached Devices


OVF3323 Change uplink speed Case 3, LI UFG change uplink speed back to Original, Servers DA connection verification
    [Tags]  LIUFGSpeedChange    speedChange

    Log    ${\n}Perform LI update from group to change uplink speed back    console=True
    Perform LI Update From Group    ${LIs[0]}    ${data_common.UFG_WAIT}    30s

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    Log    ${\n}Verify server profiles status going through US_DA1 are not affected    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles Status    ${server_profile_names}    OK

    # Verify servers Aside connections through connection map
    Verify Happy Servers DA Connections

    Verify Happy DA 3par ports Attached Devices


OVF3323 Disable Uplinks Case 1, Affect Servers Aside Connection, Servers DA connection verification
    [Tags]  DisableUplinkA   DisEnaUplinkA   DisEnaUL
    [Documentation]    Disable Aside DA uplinkset first uplink of the 2 uplinkports
    ...                Expect uplinkset to be Warning status, no profile connection error
    ...                Disable Aside DA uplinkset second uplink of the 2 uplinkports - all are disabled
    ...                Expect uplinkset to be Critical status, profile connection error, servers lose storage path
    ...                Servers connection is verified through DA nameServers connection map

    Log    ${\n}Disable Aside uplinkset first uplink ${US_DA1_UPLINKS[0]}    console=True
    ${disabled_ports} =    Create List    ${US_DA1_UPLINKS[0]}
    Disable Ports    ${NITROA}    ${disabled_ports}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify affected uplinkset status    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[0]}    US-DA1    Warning

    Log    ${\n}Verify uplink status, portStatus and disabled    console=True
    :FOR    ${ul}    IN    @{disabled_ports}
    \    Verify Port    ${NITROA}    ${ul}    status=Warning
    \    ...             portStatus=Unlinked    enabled=${False}

    Log    ${\n}Verify server profiles status going through US-DA1 still OK    console=True
    Verify Server Profiles status    ${server_profile_names}    OK

    # If the affected port trigger 3par failover to its partner port (active), any server with connection to
    # that active port will result with no loss of path due to failed over connection.
    # This is the expected behavior for 3Par partner ports, confirmed by developer who also verified
    # on C7K with the same expected behavior.
    # US-DA1 2 uplinks are connected to 3par-A partner ports. disable one uplink, cause 3Par port failover to
    # its partner port.
    # For servers with connection through US-DA1 - its connectionMap for serers on IC3 remain the same

    Log    ${\n}Verify servers DA connection on Asdie are not affected ue to 3par partner port failover
    ...    console=True
    Verify Happy Servers Aside DA Connections

    Log    ${\n}Disable US-DA1 second uplink ${US_DA1_UPLINKS[1]}    console=True
    ${disabled_ports} =    Create List    ${US_DA1_UPLINKS[1]}
    Disable Ports    ${NITROA}    ${disabled_ports}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify affected uplinkset status    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[0]}    US-DA1    Critical

    Log    ${\n}Verify uplink status, portStatus and disabled    console=True
    :FOR    ${ul}    IN    @{disabled_ports}
    \    Verify Port    ${NITROA}    ${ul}    status=Warning
    \    ...             portStatus=Unlinked    enabled=${False}

    Log    ${\n}Verify server profiles status going through US-DA1 become Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    Critical

    Log    ${\n}Verify affected servers Aside connectionMap should be empty    console=True
    ${nameservers_ic3} =    Get IC NameServers    ${NITROA}
    Should Not Be Empty    ${nameservers_ic3}

    :FOR    ${ul}    IN    @{US_DA1_UPLINKS}
    \    Log     ${\n}Verify disabled uplinks ${ul} not in nameServers    console=True
    \    Verify Port Not In nameServers    ${nameservers_ic3}    ${ul}

    Log     ${\n}Verify servers DA connection on Aside, expect no connections    console=True
    # Expect all servers Aside downlink connectionMap is ['']
    ${expected_conn_map} =    Create List    ${EMPTY}
    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
    \    Verify Server DA Connection    ${nameservers_ic3}    ${dl}    ${expected_conn_map}

    Log    ${\n}Verify servers DA connection on Bsdie are not affected    console=True
    Run Keyword And Continue On Failure    Verify Happy Servers Bside DA Connections

    Run Keyword And Continue On Failure    Verify Happy Bside DA 3par ports Attached Devices


OVF3323 Enable back Uplinks Case 1, Aside Connection Restoration, Verify servers DA connections
    [Tags]  EnableUplinkA    DisEnaUplinkA    DisEnaUL
    [Documentation]    Enable back Aside DA uplinkset both uplinks at the same time
    ...                Expect uplinks, uplinkset, server profiles back to OK
    ...                and servers storage access restored and logins redistribute

    Log    ${\n}Enable back Aside US_DA1 both uplinkports    console=True
    Enable Ports     ${NITROA}    ${US_DA1_UPLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log   ${\n}Verify affected uplinksets back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[0]}    US-DA1    OK

    Log    ${\n}Verify uplink status, portStatus and enabled    console=True
    :FOR    ${ul}    IN    @{US_DA1_UPLINKS}
    \    Verify Port    ${NITROA}    ${ul}    status=OK    portStatus=Linked
    \    ...    enabled=${True}    operationalSpeed=${ORIG_UPLINK_SPEED}

    Log    ${\n}VVerify Server Profiles status back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Run Keyword And Continue On Failure    Verify Happy Aside Uplinks DA ports

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Servers DA Connections

    Verify Happy DA 3par ports Attached Devices


OVF3323 Disable Uplinks Case 2, Affect Server Bside Connection, Verify servers DA connections
    [Tags]  DisableUplinkB    DisEnaUplinkB    DisEnaUL
    [Documentation]    Disable Bside uplinkset both uplinkports in one update port REST call
    ...                Expect Uplinkset Critical, profile connection error
    ...                servers Bside storage access lost. Aside not impacted

    Log   ${\n}Disable both uplinks    console=True
    Disable Ports    ${NITROB}    ${US_DA2_UPLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log   ${\n}Verify affected uplinksets Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[1]}    US-DA2    Critical

    Log    ${\n}Verify uplink status portStatus and disabled    console=True
    :FOR    ${disabled_port}    IN    @{US_DA2_UPLINKS}
    \    Verify Port    ${NITROB}    ${disabled_port}    status=Warning
    \    ...    portStatus=Unlinked    enabled=${False}

    #Verify all 4 server profiles status become Critical
    Log      ${\n}Verify Server Profiles status Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    Critical

    ${nameservers_ic6} =    Get IC NameServers    ${NITROB}
    Should Not Be Empty    ${nameservers_ic6}

    :FOR    ${disabled_port}    IN    @{US_DA2_UPLINKS}
    \    Log      ${\n}Verify disabled uplink ${disabled_port} not in nameServers    console=True
    \    Verify Port Not In nameServers    ${nameservers_ic6}    ${disabled_port}

    Log     ${\n}Verify servers DA connection on Bside, expect no connections    console=True
    # Expect all servers Bside downlink connectionMap is ['']
    ${conn_map} =    Create List    ${EMPTY}
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Verify Server DA Connection    ${nameservers_ic6}    ${dl}    ${conn_map}

    #Verify Servers DA connections on Aside not affected
    Run Keyword And Continue On Failure    Verify Happy Servers Aside DA Connections

    Run Keyword And Continue On Failure    Verify Happy Aside DA 3par ports Attached Devices


OVF3323 Enable back Uplinks Case 2, Bside Connection Restoration, Verify servers DA connections
    [Tags]  EnableUplinkB    DisEnaUplinkB    DisEnaUL
    [Documentation]    Enable back Bside DA uplinkset one at a time
    ...                Enable back first uplink
    ...                  - Expect uplinkset to be Warning status,
    ...                  - Profiles back to OK
    ...                  - Servers recover connections (storage path)
    ...                    verified through DA nameServers connection map
    ...                Enable back second uplink (all)
    ...                  - Expect uplinkset to be OK status, others the same

    Log   ${\n}Enable back first uplink    console=True
    ${enabled_ports} =    Create List    ${US_DA2_UPLINKS[0]}
    Enable Ports     ${NITROB}    ${enabled_ports}   ${data_common.SUBPORT_STATUS_WAIT}

    Log   ${\n}Verify uplinkset Warning    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[1]}    US-DA2    Warning

    Verify Port    ${NITROB}    ${US_DA2_UPLINKS[0]}    status=OK
    ...    portStatus=Linked    enabled=${True}    operationalSpeed=${ORIG_UPLINK_SPEED}

    Log   ${\n}Verify Server Profiles back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Log    ${\n}Verify servers DA connection on Bsdie are not affected due to 3par partner port failover
    ...    console=True
    Run Keyword And Continue On Failure    Verify Happy Servers Bside DA Connections

    Log   ${\n}Enable back second uplink    console=True
    ${enabled_ports} =    Create List    ${US_DA2_UPLINKS[1]}
    Enable Ports     ${NITROB}    ${enabled_ports}   ${data_common.SUBPORT_STATUS_WAIT}

    Log   ${\n}Verify uplinkset back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[1]}    US-DA2    OK

    Verify Port    ${NITROB}    ${US_DA2_UPLINKS[1]}    status=OK
    ...    portStatus=Linked    enabled=${True}    operationalSpeed=${ORIG_UPLINK_SPEED}

    Run Keyword And Continue On Failure    Verify Happy Bside Uplinks DA ports
    Verify Happy Servers DA Connections

    Verify Happy DA 3par ports Attached Devices


OVF3323 Disable Downlinks Case 1, Affect Server Aside Connection, Verify servers DA connections
    [Tags]  DisableDownlinkA    DisEnaDL

    Log    ${\n}Disable downlink of one of enc1 and enc2 server    console=True
    ${dl_list} =    Create List     ${enc1_server_1['enc1_downlink']}    ${enc2_server_2['enc1_downlink']}
    Disable Ports    ${NITROA}    ${dl_list}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify Server Profiles with disabled downlink status Critical    console=True

    @{sp_set1} =    Create List    ${enc1_server_1['sp_name']}    ${enc2_server_2['sp_name']}
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${sp_set1}    Critical

    Log    ${\n}Verify Server Profiles without disabled downlink status OK    console=True
    @{sp_set2} =    Create List    ${enc1_server_2['sp_name']}    ${enc2_server_1['sp_name']}
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${sp_set2}    OK

    Log    ${\n}Verify downlink status, portStatus and disabled    console=True
    :FOR    ${dl}    IN    @{dl_list}
    \    Verify Port    ${NITROA}    ${dl}    status=Critical    portStatus=Unlinked
    \    ...    enabled=${False}

    Log    ${\n}Verify disabled downlink should not be in nameServers    console=True
    ${nameservers_ic3} =    Get IC NameServers    ${NITROA}
    Should Not Be Empty    ${nameservers_ic3}
    :FOR    ${dl}    IN    @{dl_list}
    \    Verify Port Not In nameServers    ${nameservers_ic3}    ${dl}

    Log    ${\n}Servers w/o disabled downlink connection OK thru nameServers check    console=True
    ${ok_servers_aside_downlink} =    Create List     ${enc1_server_2['enc1_downlink']}
                                      ...             ${enc2_server_1['enc1_downlink']}

    :FOR    ${dl}    IN    @{ok_servers_aside_downlink}
    \    Verify Server DA Connection    ${nameservers_ic3}    ${dl}    ${ASIDE_HAPPY_CONNECTION_MAP}

    Run Keyword And Continue On Failure    Verify Happy Servers Bside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Bside DA 3par ports Attached Devices


OVF3323 Enable Back Downlinks Case 1, Aside Connection Restoration, Verify servers DA connections
    [Tags]  EnableDownlinkA    DisEnaDL

    Log to Console      ${\n}Enable back the 2 servers downlink on Aside
    ${dl_list} =    Create List     ${enc1_server_1['enc1_downlink']}    ${enc2_server_2['enc1_downlink']}
    Enable Ports    ${NITROA}    ${dl_list}    ${data_common.SUBPORT_STATUS_WAIT}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Log to Console    ${\n}Verify downlink status, portStatus and enabled
    :FOR    ${dl}    IN    @{dl_list}
    \    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked    enabled=${True}

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Servers DA Connections

    Verify Happy DA 3par ports Attached Devices


OVF3323 Disable Downlinks Case 2, Affect Server Bside Connection, Verify servers DA connections
    [Tags]  DisableDLB    DisEnaDL

    Log    ${\n}Disable downlink of one of enc1 and enc2 server    console=True
    ${dl_list} =    Create List     ${enc1_server_2['enc2_downlink']}    ${enc2_server_1['enc2_downlink']}
    Disable Ports    ${NITROB}    ${dl_list}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify Server Profiles with disabled downlink status Critical    console=True

    @{sp_set1} =    Create List    ${enc1_server_2['sp_name']}    ${enc2_server_1['sp_name']}
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${sp_set1}    Critical

    Log    ${\n}Verify Server Profiles without disabled downlink status OK    console=True
    @{sp_set2} =    Create List    ${enc1_server_1['sp_name']}    ${enc2_server_2['sp_name']}
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${sp_set2}    OK

    Log    ${\n}Verify downlink status, portStatus and disabled    console=True
    :FOR    ${dl}    IN    @{dl_list}
    \    Verify Port    ${NITROB}    ${dl}    status=Critical    portStatus=Unlinked
    \    ...    enabled=${False}

    Log    ${\n}Verify disabled downlink should not be in nameServers    console=True
    ${nameservers_ic6} =    Get IC NameServers    ${NITROB}
    Should Not Be Empty    ${nameservers_ic6}
    :FOR    ${dl}    IN    @{dl_list}
    \    Verify Port Not In nameServers    ${nameservers_ic6}    ${dl}

    Log    ${\n}Servers w/o disabled downlink connection OK thru nameServers check    console=True
    ${ok_servers_bside_downlink} =    Create List     ${enc1_server_1['enc2_downlink']}
                                      ...             ${enc2_server_2['enc2_downlink']}

    :FOR    ${dl}    IN    @{ok_servers_bside_downlink}
    \    Verify Server DA Connection    ${nameservers_ic6}    ${dl}    ${BSIDE_HAPPY_CONNECTION_MAP}

    Run Keyword And Continue On Failure    Verify Happy Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Aside DA 3par ports Attached Devices


OVF3323 Enable Back Downlinks Case 2, Bside Connection Restoration, Verify servers DA connections
    [Tags]  EnableDLB    DisEnaDL

    Log to Console      ${\n}Enable back the 2 servers downlink on Aside
    ${dl_list} =    Create List     ${enc1_server_2['enc2_downlink']}    ${enc2_server_1['enc2_downlink']}
    Enable Ports    ${NITROB}    ${dl_list}    ${data_common.SUBPORT_STATUS_WAIT}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Log to Console    ${\n}Verify downlink status, portStatus and enabled
    :FOR    ${dl}    IN    @{dl_list}
    \    Verify Port    ${NITROB}    ${dl}    status=OK    portStatus=Linked    enabled=${True}

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Servers DA Connections

    Verify Happy DA 3par ports Attached Devices


OVF3323 Power Off Aside Nitro Affecting Aside connections, Verify servers Bside DA connections
    [Tags]  PowerOffA    PowerA    Power
    [Documentation]    power off Aside IC3, all servers will lose Aside DA connection
    ...                Servers Bside storage access os not impacted

    Log    ${\n}Power off Aside Nitro and wait for Maintenance state    console=True
    Power IC and Wait    ${NITROA}    Off

    Log     ${\n}Verify Bside Interconnect remains Configured and become Master    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect    ${NITROB}    state=Configured
    ...           stackingDomainRole=${data_common.MASTER}

    # Note: profiles, LI and uplinksets are no longer guranteed to be Critical
    # Engineer - after ICM is maintenance, the SDS is not polle hence port status is not updated
    # remove verification
    # Log to Console     ${\n}Verify Aside uplinksets Critical
    # :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    # \    Verify Uplinkset Status    ${LIs[0]}    ${us}    Critical
    # Log to Console      ${\n}Verify Profile status Critical
    # Run Keyword And Continue On Failure    Verify Server Profiles status
    # ...     ${server_profile_names}    Critical

    #    Log    ${\n}Verify Aside DA Uplinks Unlinked Critical    console=True
#    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
#    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
#    \    ...    Verify Port    ${NITROA}    ${uplink}    status=Critical    portStatus=Unlinked

#    Log     ${\n}Verify Aside downlinks Unlinked Critical    console=True
#    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
#    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
#    \    ...    Verify Port    ${NITROA}    ${dl}    status=Critical    portStatus=Unlinked


    Log     ${\n}Verify Bside DA Uplinks portStatus not impacted    console=True
    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Bside uplinksets OK, not impacted    console=True
    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LIs[1]}    ${us}    OK

    Log    ${\n}Ensure Nitro 6 nameServers not be empty when power off Nitro 3    console=True
    ${nameservers_ic6} =    Get IC NameServers    ${NITROB}
    Should Not Be Empty    ${nameservers_ic6}

    Log to Console     ${\n}Verify servers DA connection on Bside remain intact
    Run Keyword And Continue On Failure    Verify Happy Servers Bside DA Connections

    Run Keyword And Continue On Failure    Verify Happy Bside DA 3par ports Attached Devices


OVF3323 Power On Aside Nitro Restoring Aside connections, Verify servers DA connections
    [Tags]  PowerOnA    PowerA    Power
    [Documentation]    Power back on Aside Nitro affecting servers connection through US-DA1
    ...                Expect uplinkset defined on Aside back to OK, and profiles connection OK
    ...                servers connection path through Aside is restored
    ...                and servers downlink operationalSpeed

    Log     ${\n}Power back on Aside Nitro and wait for Configured state    console=True
    Power IC and Wait    ${NITROA}    On

    Log     ${\n}Verify Aside Interconnect come up as Subordinate    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${NITROA}    stackingDomainRole=${data_common.SUBORDINATE}

    Log    ${\n}Verify Bside Interconnect remain Master, Configured    console=True
    Verify Named Interconnect     ${NITROB}    state=Configured
    ...          stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify DA Uplinks status and portStatus    console=True
    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked
    \    ...                   operationalSpeed=${ORIG_UPLINK_SPEED}

    Log     ${\n}Verify Aside downlinks back to Linked OK    console=True
    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked

    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside and Bside uplinksets OK    console=True
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LIs[1]}    ${us}    OK

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    Verify ICM MaxBW

    Log     ${\n}Verify servers Profile status OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Uplinks DA ports

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Servers DA Connections

    Verify Happy DA 3par ports Attached Devices


OVF3323 Power Off Bside Nitro Affecting Bside connections, Verify servers Aside DA connections
    [Tags]  PowerOffB    PowerB    Power
    [Documentation]    Power off Bside Nitro affecting servers connection through Bside uplinks
    ...                Expect uplinkset defined on Bside Critical, and profiles connection error
    ...                server storage access on Aside should not be affected

    Log    ${\n}Power off Bside Nitro and wait for Maintenance state    console=True
    Power IC and Wait    ${NITROB}    Off

    Log     ${\n}Verify Aside Interconnect become Master, remains Configured    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${NITROA}    state=Configured
    ...                 stackingDomainRole=${data_common.MASTER}

    Log    ${\n}Verify Aside DA Uplinks status and portStatus not impacted    console=True
    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked

    Log    ${\n}Verify Aside uplinksets OK, not impacted    console=True
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    Log    ${\n}Verify Nitro 3 nameServers not affected when power off Nitro 6    console=True
    ${nameservers_ic3} =    Get IC NameServers    ${NITROA}
    Should Not Be Empty    ${nameservers_ic3}

    Run Keyword And Continue On Failure    Verify Happy Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Aside DA 3par ports Attached Devices


OVF3323 Power On Bside Nitro Restoring Bside connections, Verify servers DA connections
    [Tags]  PowerOnBside    PowerB    Power
    [Documentation]    Power back on Bside Nitro affecting servers connection through Bside uplinks
    ...                Expect uplinkset defined on Bside back to OK, and profiles connection OK
    ...                servers connection path through Bside is restored
    ...                Verify servers downlink operationalSpeed


    # DF: Wait sometime for power off underneath changes quiesce down
    sleep    ${data_common.IC_SHORT_WAIT}

    Log     ${\n}Power back on Bside Nitro and wait for Configured state    console=True
    Power IC and Wait    ${NITROB}    On

    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${NITROB}    stackingDomainRole=${data_common.SUBORDINATE}

    Log     ${\n}Verify Aside Interconnect remain Master, Configured    console=True
    Verify Named Interconnect     ${NITROA}    state=Configured
    ...          stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify Aside and Bside FA Uplinks status and portStatus    console=True
    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked
    \    ...                   operationalSpeed=${ORIG_UPLINK_SPEED}

    Log      ${\n}Verify Bside downlinks Linked OK    console=True
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROB}    ${dl}    status=OK    portStatus=Linked

    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside and Bside uplinksets OK    console=True
    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Uplinkset Status    ${LIs[1]}    ${us}    OK
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    Verify ICM MaxBW

    Log      ${\n}Verify servers Profile status back to OK    console=True
    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Uplinks DA ports

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Servers DA Connections

    Verify Happy DA 3par ports Attached Devices


OVF3323 Efuse Remove Aside Nitro Affecting Aside connections, Verify servers Bside DA connections
    [Tags]  RemoveA    efuse    efuseA
    [Documentation]    Remove Aside Nitro affecting servers connection through Aside uplinks
    ...                Expect uplinkset defined on Aside Critical status, and profiles connection error
    ...                server storage access on Bside should not be affected

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
    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Bside uplinksets OK, not impacted    console=True
    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LIs[1]}    ${us}    OK

    Run Keyword And Continue On Failure    Verify Happy Servers Bside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Bside DA 3par ports Attached Devices


OVF3323 Efuse Insert Aside Nitro Restoring Aside connections, Verify servers DA connections
    [Tags]  InsertA    efuse    efuseA
    [Documentation]    Insert back Aside Nitro affecting servers connection through Aside uplinks
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

    Log     ${\n}Verify both sides FA Uplinks status and portStatus    console=True
    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked
    \    ...                   operationalSpeed=${ORIG_UPLINK_SPEED}

    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside downlinks Linked OK    console=True
    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside and Bside uplinksets OK    console=True
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...   Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LIs[1]}    ${us}    OK

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    Verify ICM MaxBW

    Log     ${\n}Verify Servers Profile status OK    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Uplinks DA ports
    Verify Happy Servers DA Connections
    Verify Happy DA 3par ports Attached Devices


OVF3323 Efuse Remove Bside Nitro Affecting Bside connections, Verify servers Aside DA connections
    [Tags]  RemoveB    efuse    efuseB
    [Documentation]    Remove Bside Nitro affecting servers connection through Bside uplinks
    ...                Expect uplinkset defined on Bside Critical status, and profiles connection error
    ...                server storage access on Aside should not be affected

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

    Log     ${\n}Verify Aside Uplinks status and portStatus not impacted    console=True
    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside downlinks Linked OK not impacted    console=True
    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside uplinksets OK, not impacted    console=True
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    Run Keyword And Continue On Failure    Verify Happy Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Aside DA 3par ports Attached Devices


OVF3323 Efuse Insert Bside Nitro Restoring Bside connections, Verify servers DA connections
    [Tags]  InsertB    efuse    efuseB
    [Documentation]    Insert back Bside Nitro affecting servers connection through Bside uplinks
    ...                Expect uplinkset defined on Bside back to OK, and profiles connection OK
    ...                servers connection path through Bside is restored
    ...                Verify servers downlink operationalSpeed

    Log    ${\n}Insert back Bside Nitro and wait for Configured state    console=True
    Efuse IC and Wait    ${NITROB}    EFuseOff

    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect    ${NITROB}    stackingDomainRole=${data_common.SUBORDINATE}

    Log     ${\n}Verify Aside Interconnect remains Configured, Master    console=True
    Verify Named Interconnect    ${NITROA}    state=Configured
    ...          stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify Uplinks portStatus and operationalSpeed    console=True
    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked
    \    ...                   operationalSpeed=${ORIG_UPLINK_SPEED}

    :FOR    ${uplink}    IN    @{IC3_FA_UPLINKS}
    \    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Bside downlinks Linked OK    console=True
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROB}    ${dl}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside and Bside uplinksets OK    console=True
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...   Verify Uplinkset Status    ${LIs[1]}    ${us}    OK

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    Verify ICM MaxBW

    Log     ${\n}Verify Profile status OK    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Uplinks DA ports

    Verify Happy Servers DA Connections

    Verify Happy DA 3par ports Attached Devices


OVF3323 DA Reset Aside Nitro, Verify servers connections restore after ICM up
    [Tags]  ResetAsideNitro    reset    resetA
    [Documentation]    Reset Aside Nitro affecting servers connection through US-DA1
    ...                Expect Aside uplinkset back to OK and servers Aside connections restored
    ...                after ICM is back
    ...                Verify servers downlink operationalSpeed

    Log    ${\n}Reset Aside Nitro and wait for it back to Configured state    console=True
    &{ic_name} =    Create Dictionary    name=${NITROA}
    @{ic_list} =    Create List    ${ic_name}
    Hard Reset Interconnects from list    ${ic_list}

    Log     ${\n}Verify Bside Interconnect become Master, remains Configured    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${NITROB}    state=Configured
    ...           stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify servers Bside DA connection not impacted    console=True
    Verify Happy Bside Uplinks DA ports
    Run Keyword And Continue On Failure    Verify Happy Servers Bside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Bside DA 3par ports Attached Devices

    Log    ${\n}Wait for Aside ICM back to Configured as Subordinate   console=True
    Wait Until Keyword Succeeds    ${data_common.RESET_IC_WAIT}    30s
    ...    Verify Named Interconnect     ${NITROA}    state=Configured
    ...           stackingDomainRole=${data_common.SUBORDINATE}

    # After reset ICM, profile will be Critical then when ICM is up, back to OK
    Log    ${\n}Reset will affect Aside uplinks and profile status    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${server_profile_names}    Critical

    Log    ${\n}Wait and verify Aside uplinks back to OK with expected speed    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROA}    ${US_DA1_UPLINKS[1]}    portStatus=Linked
    ...                          operationalSpeed=${ORIG_UPLINK_SPEED}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROA}    ${US_DA1_UPLINKS[0]}    portStatus=Linked
    ...                          operationalSpeed=${ORIG_UPLINK_SPEED}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Uplinkset Status    ${LIs[0]}    US-DA1    OK

    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    Verify ICM MaxBW

    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Server Profile status    ${sp}    OK

    Log     ${\n}Verify servers Aside DA connection restored    console=True
    Verify Happy Uplinks DA ports
    Verify Happy Servers DA Connections
    Verify Happy DA 3par ports Attached Devices


OVF3323 DA Reset Bside Nitro, Verify servers connections restore after ICM up
    [Tags]  ResetBsideNitro    reset    resetB
    [Documentation]    Reset Bside Nitro affecting servers connection through US-DA2
    ...                Expect Bside uplinkset back to OK and servers Aside connections restored
    ...                after ICM is back
    ...                Verify servers downlink operationalSpeed

    Log    ${\n}Reset Bside Nitro    console=True
    &{ic_name} =    Create Dictionary    name=${NITROB}
    @{ic_list} =    Create List    ${ic_name}
    Hard Reset Interconnects from list    ${ic_list}

    Log     ${\n}Verify Aside Interconnect become Master, remains Configured    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${NITROA}    state=Configured
    ...           stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify servers Aside DA connection not impacted    console=True
    Verify Happy Aside Uplinks DA ports
    Run Keyword And Continue On Failure    Verify Happy Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Aside DA 3par ports Attached Devices

    Log    ${\n}Wait for Bside ICM back to Configured as Subordinate    console=True
    Wait Until Keyword Succeeds    ${data_common.RESET_IC_WAIT}    30s
    ...    Verify Named Interconnect     ${NITROB}    state=Configured
    ...           stackingDomainRole=${data_common.SUBORDINATE}

    Log    ${\n}Reset will affect Bside uplinks and profile status    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${server_profile_names}    Critical

    Log    ${\n}Wait and Verify Bside uplinks back to OK with expected speed    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROB}    ${US_DA2_UPLINKS[1]}    portStatus=Linked
    ...                          operationalSpeed=${ORIG_UPLINK_SPEED}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Port    ${NITROB}    ${US_DA2_UPLINKS[0]}    portStatus=Linked
    ...                          operationalSpeed=${ORIG_UPLINK_SPEED}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Uplinkset Status    ${LIs[1]}    US-DA2    OK

    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROB}    ${dl}    status=OK    portStatus=Linked

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    Verify ICM MaxBW

    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Server Profile status    ${sp}    OK

    Log     ${\n}Verify servers Bside DA connection restored    console=True
    Verify Happy Uplinks DA ports
    Verify Happy Servers DA Connections
    Verify Happy DA 3par ports Attached Devices



OVF5199 Change DLS mode from 25Gb to 50Gb
    [Tags]    DLS    DLSto50    LIDLSto50

    Change LI downlinkSpeedMode to 50Gb


OVF5199 Update Quagmire2 servers profile FC connection rbw to 32Gbps
    [Tags]    DLS    DLSto50    SPrbwUpgrade
    [Documentation]    Increase FC and Ethernet maxBandwidth and preferred bandwidth
    ...                Increate server profiles FC connection rbw to 32Gb

    Log    ${\n}Change networks maxbw to 50Gb    console=True
    ${max_bw} =    Set Variable    50000

    :FOR    ${enet}    IN    @{ethernet_networks}
    \    Edit Network Bandwidth    ${enet['name']}   ethernet   8000   ${max_bw}

    ${fc_networks} =    Create List    ${da_networks[0]['name']}    ${da_networks[1]['name']}
    ...                                ${fa_networks[0]['name']}    ${fa_networks[1]['name']}

    # We have Quack and Quagmire2 servers. typicalbw set to 16Gb
    :FOR    ${fcnet}    IN    @{fc_networks}
    \    Edit Network Bandwidth    ${fcnet}   fc   16000   ${max_bw}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    10s
    ...    Verify Servers Downlink Speed

    # finish all profile update first then wait
    :For    ${entry}    IN     @{sp_upgrade_conn_rbw_info}
    \    Edit Profile RBW    ${entry['sp_name']}    ${entry['connections']}

    :For    ${entry}    IN     @{sp_upgrade_conn_rbw_info}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    10s
    \    ...    Verify Server Profile Status    ${entry['sp_name']}    OK

    Verify Happy Servers DA Connections

    Verify Happy DA 3par ports Attached Devices


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

    Verify Happy Servers DA Connections
    Verify Happy DA 3par ports Attached Devices

    Verify Servers Downlink Speed


OVF5199 Change DLS mode from 50Gb to 25Gb Allowed
    [Tags]    DLS    DLSto25    LIDLSto25Allow

    PASS EXECUTION IF    '${downlink_mode}' == 'SPEED_25GB'    Skip Test already in 25Gb mode

    ${resp} =    Update LI DownlinkSpeedMode    ${LIs[0]}    SPEED_25GB
    ...                            ${data_common.LI_DLS_CHANGE_WAIT}    10s
    Set Suite Variable    ${downlink_mode}    SPEED_25GB

    Log    ${\n}wait till Nitro maxBandwidth reached 25Gb    console=True
    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Named Interconnect     ${NITROA}    maxBandwidth=SPEED_25G

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Named Interconnect     ${NITROB}    maxBandwidth=SPEED_25G

    Run Keyword And Continue On Failure    Verify LI with SpeedMode

    Log    ${\n}wait for expected downgrade outage before checking end2end    console=True
    sleep    ${data_common.DLS_DOWNGRADE_OUTAGE_WAIT}

    # The BFS server may go down due to both ICM outage, wait for boot up
    Log    ${\n}Waiting ${data_common.BFS_SERVER_BOOT_WAIT} minutes for servers to boot and come up
    ...    console=True
    Sleep    ${data_common.BFS_SERVER_BOOT_WAIT}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Servers DA Connections
    Verify Happy DA 3par ports Attached Devices

    Verify Servers Downlink Speed

    # Run Keyword for List    ${PING_LIST_A}    Wait For Appliance To Become Pingable


OVF5199 Change DLS mode from 25Gb back to 50Gb
    [Tags]    DLS    DLSto50-2

    Change LI downlinkSpeedMode to 50Gb


OVF5199 Final DA Verification
    [Tags]    verifyDA
    Verify Happy Uplinks DA ports
    Verify Happy Servers DA Connections
    Verify Happy DA 3par ports Attached Devices
    :FOR    ${sp}    IN    @{server_profile_names}
    \    Run Keyword And Continue On Failure    Verify Server Profile status    ${sp}    OK
    Verify Servers Downlink Speed
    Verify ICM MaxBW

    # Run Keyword for List    ${PING_LIST_A}    Wait For Appliance To Become Pingable


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

    ${max_bw} =    Set Variable IF    '${downlink_mode}' == 'SPEED_25GB'    25000
    # ${max_bw} =    Set Variable IF    '${downlink_mode}' == 'SPEED_25GB'    50000
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


Verify Happy Servers Aside DA Connections
    [Documentation]    Verify servers Aside DA connections through nameServers connection map

    Log to Console    ${\n}Verify servers Aside DA connections through connection map

    Verify Servers DA Connections    ${NITROA}    ${US_DA1_UPLINKS}
    ...    ${ASIDE_SERVER_DOWNLINKS}    ${ASIDE_HAPPY_CONNECTION_MAP}


Verify Happy Servers Bside DA Connections
    [Documentation]    Verify servers Bside DA connections through nameServers connection map

    Log to Console    ${\n}Verify servers Bside DA connections through connection map

    Verify Servers DA Connections    ${NITROB}    ${US_DA2_UPLINKS}
    ...    ${BSIDE_SERVER_DOWNLINKS}    ${BSIDE_HAPPY_CONNECTION_MAP}


Verify Happy Servers DA Connections
    [Documentation]    Verify servers both Aside and Bside DA connections through nameServers connection map

    Log to Console    ${\n}Verify servers both Aside and Bside DA connections through connection map

    Run Keyword And Continue On Failure    Verify Happy Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Servers Bside DA Connections


Verify Happy Aside Uplinks DA ports
    [Documentation]    Verify Aside DA uplinkports connected to 3par port through nameServers

    Log    ${\n}Verify Aside DA uplinkports connected to 3par port    console=True
    ${nameServers} =    Get IC NameServers    ${NITROA}
    Should Not Be Empty    ${nameServers}

    :FOR    ${uplink_da}    IN    @{IC3_UPLINKS_DA}
    \    Verify Uplink DA Port    ${nameServers}    ${uplink_da}


Verify Happy Bside Uplinks DA ports
    [Documentation]    Verify Bside DA uplinkports connected to 3par port through nameServers uplinkport info

    Log    ${\n}Verify Bside DA uplinkports connected to 3par port    console=True

    ${nameServers} =    Get IC NameServers    ${NITROB}
    Should Not Be Empty    ${nameServers}

    :FOR    ${uplink_da}    IN    @{IC6_UPLINKS_DA}
    \    Verify Uplink DA Port    ${nameServers}    ${uplink_da}


Verify Happy Uplinks DA ports
    [Documentation]    Verify all DA uplinkports connected to its 3par port through nameServers uplinkport info

    Log    ${\n}Verify all Aside and Bside DA uplinkports connected to 3par port    console=True

    Run Keyword And Continue On Failure    Verify Happy Aside Uplinks DA ports
    Run Keyword And Continue On Failure    Verify Happy Bside Uplinks DA ports


Verify Happy DA Uplinks
    [Documentation]    Verify all DA uplinkports status and operationalSpeed same as expected
    [Arguments]    ${speed}

    Log     ${\n}Verify Aside and Bside DA Uplinks portStatus and operationalSpeed    console=True
    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_SPEED_WAIT}    10s
    \    ...    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked
    \    ...                   operationalSpeed=${speed}
    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_SPEED_WAIT}    10s
    \    ...    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked
    \    ...                   operationalSpeed=${speed}


Verify Happy LE
    [Documentation]    Verify the common scenario LE happy condition
    ...                ICM in Congured state, Uplinksets OK, DA uplinks with expected Speed
    ...                LE Consistent and OK

    Log     ${\n}Verify Both Nitro in Configured state        console=True
    Verify Named Interconnect     ${NITROA}    state=Configured
    Verify Named Interconnect     ${NITROB}    state=Configured

    Log     ${\n}Wait for all uplinkset to reach OK status        console=True
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Uplinkset Status    ${LIs[1]}    ${us}    OK

    Run Keyword And Continue On Failure    Verify Happy DA Uplinks    ${ORIG_UPLINK_SPEED}

    Log     ${\n}Verify LE status OK and Consistent    console=True
    Verify Named Logical Enclosure    ${LE}    status=OK    state=Consistent


Verify Happy LE and LI
    [Documentation]    Verify the common scenario LE and LI condition,
    ...                Expected Nitro maxBandwidth,
    ...                and servers downlinks expected operationalSpeed
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
    [Documentation]    Verify the LI status, consistencyStatus and downlinkSpeedMode
    ...                In API environment, there are 2 CXP cables between Nitro/Methane L1, L2
    ...                working for both LI downlinkSpeedMode 25Gb and 50Gb
    ...                However, with this cabling, there will be Warning alert if running in 25Gb
    ...                downlinkMode. Therefore expect Warning state if 2 CXP in L1 and L2
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


Verify Happy Aside DA 3par ports Attached Devices
    [Documentation]    Verify Aside DA uplink attached devices through 3par DA port
    ...                nameserver 'showportdev ns <port>' output

    Log     ${\n}Verify Aside DA uplink connected 3par port attached devices    console=True

    ${len} =    Get Length    ${da_3par_ports_Aside}

    # issue 'showportdev ns 0:2:1' and output to file with portwwn .txt
    # /tmp/da_ns_attdev_20210002ac01d4db.txt
    :FOR    ${index}    IN RANGE    0    ${len}
    \    ${outfile} =    Catenate    SEPARATOR=    ${data_common.DA_ATTACHED_DEV_OUTFILE_PREFIX}
    \    ...    ${da_3par_wwpn_Aside[${index}]}    ${data_common.DA_ATTACHED_DEV_OUTFILE_SUFFIX}
    \    ${cmd} =    Catenate    ${data_common.THREEPAR_NS_CMD}    ${da_3par_ports_Aside[${index}]}
    \    SSH to Source and save command output   ${three_par_info['ip']}    ${three_par_info['user']}
    \    ...    ${three_par_info['pwd']}    ${three_par_info['prompt']}
    \    ...    ${cmd}    ${outfile}
    \
    \    Verify 3par DA AttachedDev    ${outfile}    ${da_3par_wwpn_Aside[${index}]}
    \    ...    ${STORAGE_ATTACH_DEVICES}


Verify Happy Bside DA 3par ports Attached Devices
    [Documentation]    Verify Aside DA uplink attached devices through 3par DA port
    ...                nameserver 'showportdev ns <port>' output

    Log     ${\n}Verify Bside DA uplink connected 3par port attached devices    console=True

    ${len} =    Get Length    ${da_3par_ports_Bside}

    # issue 'showportdev ns 0:2:2' and output to file with portwwn .txt
    # /tmp/da_ns_attdev_20220002ac01d4db.txt
    :FOR    ${index}    IN RANGE    0    ${len}
    \    ${outfile} =    Catenate    SEPARATOR=    ${data_common.DA_ATTACHED_DEV_OUTFILE_PREFIX}
    \    ...    ${da_3par_wwpn_Bside[${index}]}    ${data_common.DA_ATTACHED_DEV_OUTFILE_SUFFIX}
    \    ${cmd} =    Catenate    ${data_common.THREEPAR_NS_CMD}    ${da_3par_ports_Bside[${index}]}
    \    SSH to Source and save command output   ${three_par_info['ip']}    ${three_par_info['user']}
    \    ...    ${three_par_info['pwd']}    ${three_par_info['prompt']}
    \    ...    ${cmd}    ${outfile}
    \
    \    Verify 3par DA AttachedDev    ${outfile}    ${da_3par_wwpn_Bside[${index}]}
    \    ...    ${STORAGE_ATTACH_DEVICES}


Verify Happy DA 3par ports Attached Devices
    [Documentation]    Verify Both Side DA uplink attached devices through 3par DA port
    ...                nameserver 'showportdev ns <port>' output

    Run Keyword And Continue On Failure    Verify Happy Aside DA 3par ports Attached Devices
    Run Keyword And Continue On Failure    Verify Happy Bside DA 3par ports Attached Devices


Change LI downlinkSpeedMode to 50Gb
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

    Run Keyword And Continue On Failure    Verify LI with SpeedMode

    Log    ${\n}wait for expected upgrade outage before checking end2end    console=True
    sleep    ${data_common.DLS_UPGRADE_OUTAGE_WAIT}

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    # BFS server may go down due to both ICM may have outage, wait for BFS erver to come up
    Log    ${\n}Waiting ${data_common.BFS_SERVER_BOOT_WAIT} minutes for servers to boot and come up
    ...    console=True
    Sleep    ${data_common.BFS_SERVER_BOOT_WAIT}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Servers DA Connections

    Verify Happy DA 3par ports Attached Devices

    # Run Keyword for List    ${PING_LIST_A}    Wait For Appliance To Become Pingable

