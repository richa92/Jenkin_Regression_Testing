*** Settings ***
Documentation    OVF3581 - TBird 8 S-Channel pert port support using Quack
...
...      - Goal:
...        |  - Ensure Profile Manager and CRM S-Channel related features work with physical functions 5-8
...        |  - Ensure Quack fw/driver works for aforementioned features and end2end ethernet traffic works
...        |  - Not intended for full-fledged feature testing of S-chcannel-LAG or SmarLink features
...
...      - Test Coverage focus:
...        |  - S-channel LAG connetions on PF5-8 and traffic, no traffic interruptions for some major actions
...        |  - Smartlink
...        |  - validation of profile/profile template with and without S-Channel LAG using all physical functions
...
...      - Usage:
...        |  - full test: robot -V data_Quack_8PF.py -T -d /Result/Quack OVF3581_Quack_8PF.robot
...        |  - skip precondition setup: robot -v skipSetup:True -V data_Quack_8PF.py -i sp OVF3581_Quack_8PF.robot
...        |  - run tagged cases: robot -V data_Quack_8PF.py -i SChannelLAG OVF3581_Quack_8PF.robot
...
...      - LE: 2 frame, HA, IBS3, CL20
...
...      - 3 Enet MLAG uplinksets, Tagged, Untagged and Tunnel Ethernet Type, 2 uplinks with 1 uplink on each Potash
...        |  - tagged uplinkset:
...        | \ \ - uplinks: IC3 and IC6 Q6
...        | \ \ - networks: net_401 - net_409, odd vlan networks with SmartLink, even ones without;
...        | \ \ \ \ \ native: net_403
...        |  - tunnel uplinkset:
...        | \ \ - uplinks: IC3 and IC6 Q1:1
...        | \ \ - network: tunnel_2, not smartlink
...        |  - untag uplinkset:
...        | \ \ - uplinks: IC3 and IC6 Q1:2
...        | \ \ - network: untag_2, not smartlink
...
...      - network set used in connection: netset_1: net_403 (checked as Untagged), net_404
...
...      - 1 server with MZ3 Quack card. For end2end testing, total 8 Enet Connections defined on PF 5-8 of each port
...        |  - WS 2016
...        |  - Server Profile with 4 S-Channel LAG connections
...        |  - serves with switch dependent LACP NIC teaming, with static ip for each teamed interface
...        | \ \ \ - conn-netset1-1e: networkset netset_1 (1 net_403 native, ToR pvid 403; tag net_404), LAG1
...        | \ \ \ - conn-tag-1f: single tagged net_407, LAG2
...        | \ \ \ - conn-tunnel-1g: tunnel_2, LAG3  (untagged net, ToR pvid 412; tagged vlanid 410)
...        | \ \ \ - conn-untag-1h:: untag_2, LAG4   (ToR pvid 415)
...        | \ \ \ - conn-netset1-2e: networkset netset_1,  LAG1
...        | \ \ \ - conn-tag-2f: single tagged net_407, LAG2
...        | \ \ \ - conn-tunnel-2g: tunnel_2, LAG3
...        | \ \ \ - conn-untag-2h:: untag_2, LAG4
...
...      - Negative Test cases
...        |  - Server Profile template and Server Profile connections
...        | \ \ \ - total connections bandwidth per port exceed physical link bandwitdh limit
...        | \ \ \ - duplicate network on connections of the physical port (single network connections)
...        | \ \ \ - duplicate network result from different networkset connections of the physical port
...
...        |  - S-Channel LAG requirement validataon
...        | \ \ \ - lagged connections should have same network/networkset, same requested bandwidth

...      - Max connections (S-Channel LAGed, non S-Channel LAGed) defined on max physical functions per port
...        |  - Server Profile template creation OK
...        |  - Server Profile created OK from SPT
...
...      - End2End Enet traffic testing with S-Channel LAGed connections on PF 5-8 on Quack, or PF 1-4 on Bronco
...        |  - server traffic for the connections
...        | \ \ \ - network set networks connection: 1 native (untagged): NS_NATIVE, and 1 tagged: NS_TAG
...        | \ \ \ - single tag network connection: TAG
...        | \ \ \ - tunnel connection: 1 tagged network TUNNEL_TAG, 1 untagged network (TUNNEL_UNTAG)
...        | \ \ \ - untag connection: 1 untag network UNTAG
...
...        |  - Server ethernet connections traffic verification are through ping from testhead
...        |  - ping processes start from testhead for all types of traffic before the scenarios and stopped afterwards
...        | \ \ \ - disable downlink
...        | \ \ \ - enable back downlink
...        | \ \ \ - Remove Aside Potash
...        | \ \ \ - Insert Aside Potash
...        | \ \ \ - Power off Bside Potash
...        | \ \ \ - Power on Bside Potash
...
...        |  - ping process output for all types of network are in ping_<type>_<scenario>.txt files
...        |  \ \ \  e.g., ping_NS_NATIVE_RemoveA.txt
...
...        |  - lost packets were calculated based on the transmitted/received packets from ping statistics
...
...        |  - For S-Channel LAG connections, traffic verification PASS if lost packets <= 2
...
...      - SmartLink
...        |  - All uplinks of the uplinkset are down (thorugh disabling ports)
...        | \ \ \ - subport for the affected network connection
...        | \ \ \ \ \   - Unlinked/SmartLink if all networks in the network set are smartlink
...        | \ \ \ \ \   - Uninked/SmartLink if single SmartLink network
...        | \ \ \ \ \   - Linked/Active if mixed SmartLink and Non SmartLink networks in network set
...        | \ \ \ \ \   - Linked/Active if single Non SmartLink network
...
...        |  - Change connection relevant network(s) from non SmartLink to SmartLink (Edit network)
...        | \ \ \ - all connections subports will be Unlinked/SmartLink
...
...        |  - Bring up some uplinks (not all) of uplinkset uplinks (enable port)
...        | \ \ \ - subport for the affected connection will change from Unlinked/SmartLink to Linked/Active
...
...        |  - Bring up all uplinks of the uplinkset (enable port)
...        | \ \ \ - subport for the affected connection will change from Unlinked/SmartLink to Linked/Active
...

Resource         ../../../../../Resources/api/fusion_api_resource.txt
Resource         ../FVT/fvt-keywords.txt
Resource         ../FVT/Resources/fvt_resource.txt
Resource         ./DF_keywords.txt

Library          FusionLibrary
Library          ../FVT/fvt_api.py
Library          Process

Suite Setup      Suite Precondition Setup
Suite Teardown   Suite Min Teardown

# Setup for each test case
Test Setup       Common Test Setup
Test Teardown    Common Test Teardown

*** Variables ***
${skipSetup}    ${False}
${LE_URI}    None
${POTASH3_URI}    None
${POTASH6_URI}    None

*** Test Cases ***

OVF3581 SPT Connection Negative Tests - max bandwidth per port and duplicate network among connections per port
    [Tags]    Negative    SPTBwDupNet
    [Documentation]    Negative tests for SPT connectiond per port max bandwidth and network limition
    ...
    ...                - BW_TOTAL_LINKRATE_OVERFLOW_ERROR:
    ...                |  - total connections bw per port exceeds max; 1 test per port
    ...                - DuplicateNetworksPerPortError:
    ...                |  - case 1 duplicate network in connections from networkset and single network
    ...                |  - case 2 duplicate network in connections from different network sets
    ...                - UnavailableEthernetFCError
    ...                |  - connection on PF 6 with network which is not provisioned

    :FOR    ${spt}    IN    @{err_spt_list}
    \    ${resp} =    Create Server Profile Template     ${spt['sptBody']}    ${server_profiles[0]}
    \    ${task} =    Wait For Task    ${resp}    ${data_common.SP_CREATE_WAIT}    20s
    \    Verify Task Error    ${task}    ${spt['errorCode']}

OVF3581 SPT S-Channel LAGed Connection Negative Tests - mismatched network, networkset, and bandwidth
    [Tags]    Negative    SPTMismatchedConn
    [Documentation]    Negative tests for SPT S-Channel lagged connections - require same network, networkset and bw
    ...
    ...                - MISMATCH_NETWORK_LAG_VIOLATION_ERROR:
    ...                |  - connections in the same lag using different network
    ...                |  - connections in the same lag using different network set
    ...                - MISMATCH_BANDWIDTH_LAG_VIOLATION_ERROR
    ...                |  - connections in the same lag with different bandwidth

    :FOR    ${spt}    IN    @{err_spt_scmlag_list}
    \    ${resp} =    Create Server Profile Template     ${spt['sptBody']}    ${server_profiles[0]}
    \    ${task} =    Wait For Task    ${resp}    ${data_common.SP_CREATE_WAIT}    20s
    \    Verify Task Error    ${task}    ${spt['errorCode']}

OVF3581 Profile Connection Negative Tests - max bandwidth per port and duplicate network among connections per port
    [Tags]    Negative    SPBwDupNet
    [Documentation]    Negative tests for profile connectiond per port max bandwidth and network limition
    ...
    ...                - BW_TOTAL_LINKRATE_OVERFLOW_ERROR:
    ...                |  - total connections bw per port exceeds max
    ...                - DuplicateNetworksPerPortError
    ...                |  - case 1 duplicate network in connections from networkset and single network
    ...                |  - case 2 duplicate network in connections from different network sets

    :FOR    ${sp}    IN    @{err_sp_list}
    \    ${resp} =    Create Server Profile    ${sp['spBody']}
    \    ${task} =    Wait For Task    ${resp}    ${data_common.SP_CREATE_WAIT}    20s
    \    Verify Task Error    ${task}    ${sp['errorCode']}

OVF3581 Profile S-Channel LAGed Connection Negative Tests - mismatched network, networkset, and bandwidth
    [Tags]    Negative    SPMismatchedConn
    [Documentation]    Negative tests for profile S-Channel lagged connections - require same network, networkset and bw
    ...
    ...                - MISMATCH_NETWORK_LAG_VIOLATION_ERROR:
    ...                |  - connections in the same lag using different network
    ...                |  - connections in the same lag using different network set
    ...                - MISMATCH_BANDWIDTH_LAG_VIOLATION_ERROR
    ...                |  - connections in the same lag with different bandwidth

    :FOR    ${sp}    IN    @{err_sp_scmlag_list}
    \    ${resp} =    Create Server Profile    ${sp['spBody']}
    \    ${task} =    Wait For Task    ${resp}    ${data_common.SP_CREATE_WAIT}    20s
    \    Verify Task Error    ${task}    ${sp['errorCode']}

OVF3581 Create Profile Template with Max Connections and Max bandwitdh, Create Profile from this SPT
    [Tags]    Max    SPTMaxConn    SPMaxConn
    [Documentation]    Create profile template with max number of connections and max bandwidth.
    ...                Create Profile from this SPT
    ...                - Expect both succeed

    # clean up if exist
    Delete SPT    ${spt_no_lag['name']}

    Create Server Profile Template     ${spt_no_lag}    ${server_profiles[0]}    ${data_common.SPT_CREATE_WAIT}    10s
    Verify Server Profile Template Status    ${spt_no_lag['name']}    OK

    Delete Profile   ${sp_with_spt_no_lag['name']}
    Create Server Profile    ${sp_with_spt_no_lag}    ${data_common.SP_CREATE_WAIT}    20s
    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    ...    Verify Server Profile Status    ${sp_with_spt_no_lag['name']}    OK
    # Verify Server Profile Status    ${sp_with_spt_no_lag['name']}    OK

    # only one server, delete and use for other test
    Delete Profile   ${sp_with_spt_no_lag['name']}

OVF3581 Create Profile Template with Max S-Channel LAGed Connections and Max bandwitdh, Create Profile from this SPT
    [Tags]    Max    LagSPTMaxConn    LagSPMaxConn
    [Documentation]    Create profile template with max number of S-Channel LAGed connections and max bandwidth.
    ...                Create Profile from this SPT
    ...                - Expect both succeed

    # clean up if exist
    Delete SPT    ${spt_lag['name']}

    Create Server Profile Template     ${spt_lag}    ${server_profiles[0]}    ${data_common.SPT_CREATE_WAIT}    10s
    Verify Server Profile Template Status    ${spt_lag['name']}    OK

    Delete Profile   ${sp_with_spt_lag['name']}
    Create Server Profile    ${sp_with_spt_lag}    ${data_common.SP_CREATE_WAIT}    20s

    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    ...    Verify Server Profile status    ${sp_with_spt_lag['name']}    OK
    #Verify Server Profile status    ${sp_with_spt_lag['name']}    OK

    Delete Profile   ${sp_with_spt_lag['name']}

OVF3581 Create Profile with PF5-8 S-Channel LAGed connections
    [Tags]    SP    SChannelLAG
    [Documentation]    Create profile with connections on last 4 PFs of the card, for Quack, PF 5-8, for Bronco PF 1-4
    ...                - Verify Profile created OK

    # Power off all servers

    # Note that keyword 'Add Server Profiles from variable' use 'Add Server Profile' which are defined in
    # fvt-keywords and server_profile. So use loop and specify server_profile.Add Server Profile directly

    :FOR     ${sp}    IN     @{server_profiles}
    \    Create Server Profile    ${sp}    ${data_common.SP_CREATE_WAIT}    20s
    \    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    \    ...    Verify Server Profile status    ${sp['name']}    OK
    #\    Verify Server Profile Status    ${sp['name']}    OK

OVF3581 Power On Servers, Verify Servers Connections traffic through ping
    [Tags]    ServerEnd2End    Happy    SChannelLAG

    # for Tag include without going through LE creation that was created already
    # Setup Suite Variables

    # power on servers
    Run Keyword for List    ${servers}    Power on Server

    Log to Console    ${\n}Waiting ${data_common.SERVER_BOOT_SHORT_WAIT} minutes for servers to come up
    Sleep    ${data_common.SERVER_BOOT_SHORT_WAIT}

    # Verify server ethernet connections are pingable
    Run Keyword for List    ${PING_LIST}    Wait For Appliance To Become Pingable

    # Sometime SP has some transient alerts, wait till cleared
    :FOR     ${sp}    IN     @{server_profiles}
    \    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    \    ...    Verify Server Profile status    ${sp['name']}    OK


OVF3581 S-Channel Lag - Disable Downlink Mapped to Master Potash, No Traffic interruption
    [Tags]    DisableDownlinkA    SChannelLAG
    [Documentation]    The following are verified
    ...                - Server Profile Critical
    ...                - IC3 downlink port d3 Disabled/Critical,
    ...                - all subports Unlinked/AdminDisable
    ...                - No Traffic interruption


    Start Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    DDownLinkA

    Log to Console      ${\n}Disable downlink of server and verify expected portStatus, portStatusReason, disabled
    ${dl_list} =    Create List     ${ENC1_SERVERS[0]['enc1_downlink']}
    Disable Ports    ${POTASH3}    ${dl_list}    ${data_common.SUBPORT_STATUS_WAIT}

    Log to Console     ${\n}Verify disabled downlinks Unlinked/AdminDisabled and same for all subports
    :FOR    ${dl}    IN    @{dl_list}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    \    ...    Verify Port    ${POTASH3}    ${dl}    status=Critical    portStatus=Unlinked
    \    ...    portStatusReason=AdminDisabled
    # DF REVISIT
    #\    ...    subports=${dl_subports_all_down_disabled_template}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    \    ...    Verify Downlink Subports Status    ${POTASH3}    ${dl}     ${dl_subports_all_down_disabled_template}

    # @{sp_set1} =    Create List    ${ENC1_SERVERS[0]['sp_name']}
    Log to Console      ${\n}Verify Server Profiles with disabled downlink status Critical
    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    \    ...    Verify Server Profile status    ${sp}    Critical

    Stop Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    DDownLinkA

OVF3581 S-Channel Lag - Enable back Downlink Mapped to Master Potash, No Traffic interruption
    [Tags]    EnableDownlinkA    SChannelLAG
    [Documentation]    Enable back the disabled downlink. The following are verified
    ...                - Server Profile OK
    ...                - IC3 downlink port Enabled/Ok, all subports Linked/Active
    ...                - No Traffic interruption

    Start Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    EDownLinkA

    Log to Console      ${\n}Enable back server downlink and check expected port portStatus, enabled, portStatusReason
    ${dl_list} =    Create List     ${ENC1_SERVERS[0]['enc1_downlink']}
    Enable Ports    ${POTASH3}    ${dl_list}    ${data_common.SUBPORT_STATUS_WAIT}

    Log to Console      ${\n}Verify downlink status, portStatus, and all subports status
    :FOR    ${dl}    IN    @{dl_list}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    \    ...    Verify Port    ${POTASH3}    ${dl}    status=OK    portStatus=Linked
    # DF REVISIT
    #\    ...    subports=${dl_subports_all_up_active_template}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    \    ...    Verify Downlink Subports Status    ${POTASH3}    ${dl}    ${dl_subports_all_up_active_template}

    Log to Console      ${\n}Verify Server Profiles status back to OK
    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    \    ...    Verify Server Profile status    ${sp}    OK

    Stop Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    EDownLinkA

OVF3581 S-Channel Lag - Disable Bside Downlink, No Traffic interruption
    [Tags]    DisableDownlinkB    SChannelLAG
    [Documentation]    The following are verified
    ...                - Server Profile Critical
    ...                - IC6 downlink port d3 Disabled/Critical,
    ...                - all subports Unlinked/AdminDisable
    ...                - No Traffic interruption

    Start Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    DDownLinkB

    Log to Console      ${\n}Disable downlink of server and verify expected portStatus, portStatusReason, disabled
    ${dl_list} =    Create List     ${ENC1_SERVERS[0]['enc2_downlink']}
    Disable Ports    ${POTASH6}    ${dl_list}    ${data_common.SUBPORT_STATUS_WAIT}

    Log to Console     ${\n}Verify disabled downlinks Unlinked/AdminDisabled and same for all subports
    :FOR    ${dl}    IN    @{dl_list}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    \    ...    Verify Port    ${POTASH6}    ${dl}    status=Critical    portStatus=Unlinked
    \    ...    portStatusReason=AdminDisabled
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    \    ...    Verify Downlink Subports Status    ${POTASH6}    ${dl}    ${dl_subports_all_down_disabled_template}

    # @{sp_set1} =    Create List    ${ENC1_SERVERS[0]['sp_name']}
    Log to Console      ${\n}Verify Server Profiles with disabled downlink status Critical
    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    \    ...    Verify Server Profile status    ${sp}    Critical

    Stop Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    DDownLinkB


OVF3581 S-Channel Lag - Enable back Bside Downlink, No Traffic interruption
    [Tags]    EnableDownlinkB    SChannelLAG
    [Documentation]    Enable back the disabled bside downlink. The following are verified
    ...                - Server Profile OK
    ...                - IC6 downlink port Enabled/Ok, all subports Linked/Active
    ...                - No Traffic interruption

    Start Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    EDownLinkB

    Log to Console      ${\n}Enable back server downlink and check expected port portStatus, enabled, portStatusReason
    ${dl_list} =    Create List     ${ENC1_SERVERS[0]['enc2_downlink']}
    Enable Ports    ${POTASH6}    ${dl_list}    ${data_common.SUBPORT_STATUS_WAIT}

    Log to Console      ${\n}Verify downlink status, portStatus, and all subports status
    :FOR    ${dl}    IN    @{dl_list}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    \    ...    Verify Port    ${POTASH6}    ${dl}    status=OK    portStatus=Linked
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    \    ...    Verify Downlink Subports Status    ${POTASH6}    ${dl}    ${dl_subports_all_up_active_template}

    Log to Console      ${\n}Verify Server Profiles status back to OK
    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    \    ...    Verify Server Profile status    ${sp}    OK

    Stop Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    EDownLinkB


OVF3581 S-Channel LAG - Efuse Remove Aside Potash, No Traffic Interruption
    [Tags]    removeA    efuse    SChannelLAG
    [Documentation]    Remove Aside Potash. The following are verified
    ...                - IC6 downlinks remain OK/Linked, becomes Master
    ...                - uplinksets Warning status
    ...                - Server Profile Critical
    ...                - No Traffic interruption

    Start Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    EfuseRemoveA

    Log to Console    ${\n}Remove Aside potash and wait for Absent state
    Efuse IC and Wait    ${POTASH3}    EFuseOn

    # Log to Console    ${\n}Wait for HA sync and nameServers info stabilization for Efuse case
    # sleep    ${data_common.CONN_DEPLOY_WAIT}

    Log to Console     ${\n}Verify Bside Interconnect become Master, remains Configured
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${POTASH6}    state=Configured    stackingDomainRole=${data_common.MASTER}

    Log to Console     ${\n}Verify uplinks on Bside remained OK/Linked
    :FOR    ${uplink}    IN    @{BSIDE_UPLINKS}
    \    Verify Port    ${POTASH6}    ${uplink}    status=OK    portStatus=Linked

    Log to Console     ${\n}Verify all uplinksets in Warning state
    :FOR    ${us}    IN    @{ALL_UPLINK_SETS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Uplinkset Status    ${LIs[1]}    ${us}    Warning

    Log to Console     ${\n}Verify Bside downlinks Linked OK
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${POTASH6}    ${dl}    status=OK    portStatus=Linked

    Log to Console      ${\n}Verify Profile status Critical with 4 connection errors
    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    \    ...    Verify Server Profile status    ${sp}    Critical

    Stop Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    EfuseRemoveA


OVF3581 S-Channel LAG - Efuse Insert Aside Potash, No Traffic Interruption
    [Tags]    InsertA    efuse    SChannelLAG
    [Documentation]    The following are verified
    ...                - IC3 Configured/OK, Subordinate; IC6 remained Master
    ...                - IC3 uplinks Linked/Active, downlink Linked, subports Linked/Active
    ...                - uplink sets back to OK
    ...                - all uplinks lagStates
    ...                - Server Profile OK
    ...                - No Traffic interruption


    Start Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    InsertA

    Log to Console    ${\n}Insert back Aside potash and wait for Configured state
    Efuse IC and Wait    ${POTASH3}    EFuseOff

    # Log to Console     ${\n}Wait for connection deployment before checking profile status
    # sleep    ${data_common.CONN_DEPLOY_WAIT}

    Log to Console     ${\n}Verify Aside Interconnect up as Subordinate
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect    ${POTASH3}    stackingDomainRole=${data_common.SUBORDINATE}

    Log to Console     ${\n}Verify Bside Interconnect remains Configured
    Verify Named Interconnect    ${POTASH6}    state=Configured    stackingDomainRole=${data_common.MASTER}

    Log to Console     ${\n}Verify all uplinksets in OK state
    :FOR    ${us}    IN    @{ALL_UPLINK_SETS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    Wait and Verify Uplinks Active lagStates

    Log to Console     ${\n}Verify Aside downlinks Linked OK and subports all back to Linked
    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    \    ...    Verify Port    ${POTASH3}    ${dl}    status=OK    portStatus=Linked
    # DF REVISIT
    #\    ...                   subports=${dl_subports_all_up_active_template}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    \    ...    Verify Downlink Subports Status    ${POTASH3}    ${dl}    ${dl_subports_all_up_active_template}

    Log to Console     ${\n}Verify Servers Profile status OK
    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    \    ...    Verify Server Profile status    ${sp}    OK

    Stop Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    InsertA


OVF3581 S-Channel LAG - Power off Bside Potash, No Traffic Interruption
    [Tags]    PowerOffB    PowerB    Power    SChannelLAG
    [Documentation]    Power off Bside Potash.
    ...              | Note SDS polling for ICM 'Maintenance' mode is stopped, no gurantee of ports status,
    ...              | profile status, etc. Use hard-coded wait before stop and verify traffic
    ...              | The following are verified
    ...                - IC3 become 'Master', its uplinks and downlinks should not be impacted
    ...                - No Traffic interruption

    Log to Console    ${\n}Power off Bside Potash and wait for Maintenance state

    Start Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    PowerOffB

    Power IC and Wait    ${POTASH6}    Off

    Log to Console     ${\n}Verify Aside Interconnect remains Configured and become Master
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect    ${POTASH3}    stackingDomainRole=${data_common.MASTER}

    Log to Console     ${\n}Verify Aside Uplinks status and portStatus not impacted
    :FOR    ${uplink}    IN    @{ASIDE_UPLINKS}
    \    Verify Port    ${POTASH3}    ${uplink}    status=OK    portStatus=Linked

    # Since we could not verify Server Profile status for power off case, need to make sure the
    # scenarion goes to the right state by waiting some time

    Log to Console    ${\n}Wait some time to ensure traffic monitor catch the right duration for power off impact
    sleep    ${data_common.POWEROFF_IC_WAIT}

    Stop Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    PowerOffB


OVF3581 S-Channel LAG - Power back on Bside Potash, No Traffic Interruption
    [Tags]  PowerOnB   PowerB    Power    SChannelLAG
    [Documentation]    Power back the Bside Potash. The following are verified
    ...                - IC6 back to Configured/OK, become Subordinate
    ...                - IC3 Configured/OK, remain Master
    ...                - uplink sets back to OK
    ...                - all uplinks Linked/Active, with expected lagStates
    ...                - server Bside downlink OK/Linked, subports Linked/Active
    ...                - Server Profile OK
    ...                - No Traffic interruption

    Log to Console     ${\n}Power back on Bside Potash and wait for Configured state

    Start Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    PowerOnB

    Power IC and Wait    ${POTASH6}    On

    # Log to Console     ${\n}Wait for connection deployment before checking profile status
    # sleep    ${data_common.CONN_DEPLOY_WAIT}

    Log to Console     ${\n}Verify Bside Interconnect up Configured, Subordinate
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...   Verify Named Interconnect    ${POTASH6}    status=OK    state=Configured
    ...          stackingDomainRole=${data_common.SUBORDINATE}

    Log to Console     ${\n}Verify all uplinksets back in OK state
    :FOR    ${us}    IN    @{ALL_UPLINK_SETS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    Wait and Verify Uplinks Active lagStates

    Log to Console     ${\n}Verify Aside Interconnect remains Configured, Master
    Verify Named Interconnect    ${POTASH3}    state=Configured    stackingDomainRole=${data_common.MASTER}

    Log to Console     ${\n}Verify Bside downlinks Linked/OK and subports all back to Linked
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    \    ...    Verify Port    ${POTASH6}    ${dl}    status=OK    portStatus=Linked
    # DF REVISIT
    #\    ...                   subports=${dl_subports_all_up_active_template}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    \    ...    Verify Downlink Subports Status    ${POTASH6}    ${dl}    ${dl_subports_all_up_active_template}

    Log to Console     ${\n}Verify Servers Profile status OK
    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    \    ...    Verify Server Profile status    ${sp}    OK

    Stop Enet Traffic Monitor For Server Connections    ${CONN_TRAFFIC_INFOS}    PowerOnB


OVF3581 SmartLink - Disable all uplinks of the 3 uplinksets, verify expected downlinks subports status
    [Tags]  SmartLink    disableAllUplinks
    [Documentation]    Disable all uplinks of the 3 types of uplinksets
    ...     | The conn 1 with network set contains 1 smartlink and 1 non-smartlink network
    ...     | The conn 2 with single tagged smartlink network
    ...     | The conn 3 with tunnel network without smart link
    ...     | The conn 4 with untagged network without smart link
    ...     | When uplinkset all uplinks are down, with HA and uplinks on each side
    ...     | downlink on each enclosure will fail the same way
    ...     | Expect:
    ...     | For connection on Bronco with 4 PF
    ...     |    - downlink subport 1 Linked/Active
    ...     |    - downlink subport 2 Unlinked/SmartLink
    ...     |    - downlink subport 3 Linked/Active
    ...     |    - downlink subport 4 Linked/Active
    ...     | Or for connection on Quack PF5-8
    ...     |    - downlink subport 1 UnLinked/Ok
    ...     |    - downlink subport 5 Linked/Active
    ...     |    - downlink subport 6 Unlinked/SmartLink
    ...     |    - downlink subport 7 Linked/Active
    ...     |    - downlink subport 8 Linked/Active
    ...
    ...     |    - Server Profile critical

    Log to Console      ${\n}Disable all uplinks of the 3 uplinksets
    Disable Ports    ${POTASH3}    ${ASIDE_UPLINKS}    ${data_common.SUBPORT_STATUS_WAIT}
    Disable Ports    ${POTASH6}    ${BSIDE_UPLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log to Console     ${\n}Verify All uplinksets Critical
    :FOR    ${us}    IN    @{ALL_UPLINK_SETS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Uplinkset Status    ${LIs[0]}    ${us}    Critical

    # set up expected subports, deep copy template then modify, thus not to affect template
    @{expect_subports_status} =    Fvt Copy Dictionary    ${dl_subports_all_up_active_template}
    Set To Dictionary    ${expect_subports_status[${SUBPORT_OFFSET} + 1]}    portStatus    Unlinked
    Set To Dictionary    ${expect_subports_status[${SUBPORT_OFFSET} + 1]}    portStatusReason    SmartLink

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}   20s
    ...    Verify Downlink Subports Status    ${POTASH3}    ${ENC1_SERVERS[0]['enc1_downlink']}
    ...                                       ${expect_subports_status}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}   20s
    ...    Verify Downlink Subports Status    ${POTASH6}    ${ENC1_SERVERS[0]['enc2_downlink']}
    ...                                       ${expect_subports_status}

    Log to Console      ${\n}Verify Profile status Critical
    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    \    ...    Verify Server Profile status    ${sp}    Critical


OVF3581 SmartLink - Edit networks used in connections from non-smartLink to smartLink, verify downlinks subports status
    [Tags]    SmartLink    EditNetSmart
    [Documentation]    Edit network net_404 used in networkset ns1, tunntel_2 and untag_2 used
    ...                in connections from non_smartLink to smartLink, result in all networks in use are SmartLink
    ...     | - The conn 1 with network set contains 2 smartlink networks
    ...     | - The conn 2 with single tagged smartlink network
    ...     | - The conn 3 with tunnel network with smart link
    ...     | - The conn 4 with untagged network with smart link
    ...     | Expect: downlink subports for all S-Channel LAGed connections Unlinked/SmartLink


    # Edit netowrk that is part of connection involves configuration on ICM and will take time
    # 1min is not enough
    ${net_list} =    Create List    net_404    tunnel_2    untag_2
    :FOR    ${net}    IN    @{net_list}
    \    Log to Console      ${\n}Edit network ${net} to be with smartLink
    \    ${resp} =    Fvt Api Get Ethernet Network By Name    ${net}
    \    Set To Dictionary    ${resp}    smartLink    ${True}
    \    ${uri} =    Set Variable    ${resp['uri']}
    \    ${task} =    Fusion Api Edit Ethernet Network    ${resp}    ${uri}
    \    Should Be Equal As Integers    ${task['status_code']}    202
    \    ${task} =    Wait For Task    ${task}    ${data_common.SUBPORT_STATUS_WAIT}    20s
    \    Should Be Equal As Strings    ${task['taskState']}    Completed

    # Expect all subport down due to all connections network changed to SmartLink
    Log to Console      ${\n}Verify server downlink subports Unlinked due to SmartLink
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}   15s
    ...    Verify Downlink Subports Status    ${POTASH3}    ${ENC1_SERVERS[0]['enc1_downlink']}
    ...                                       ${dl_subports_all_down_smart_template}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}   20s
    ...    Verify Downlink Subports Status    ${POTASH6}    ${ENC1_SERVERS[0]['enc2_downlink']}
    ...                                       ${dl_subports_all_down_smart_template}

    Log to Console      ${\n}Verify Profile status Critical
    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    \    ...    Verify Server Profile status    ${sp}    Critical


OVF3581 SmartLink - Enable back one of 2 uplinks of each 3 uplinksets, verify expected downlinks subport status
    [Tags]    SmartLink    EnablePartialUplink
    [Documentation]    Enable back one of 2 uplinks of each of the 3 types of uplinksets
    ...     | When not all uplinks of the uplinkset are down, the relevant network connection subport will be up
    ...     | Expect:
    ...     |    - All S-channel of the downlink back to Linked/Active
    ...     |    -  All uplinksets in Warning status
    ...     |    - Server Profile back to OK

    Log to Console      ${\n}Enable back one uplink out of 2 of each of the 3 uplinksets
    Enable Ports    ${POTASH3}    ${ASIDE_UPLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log to Console     ${\n}Verify All uplinksets Warning
    :FOR    ${us}    IN    @{ALL_UPLINK_SETS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Uplinkset Status    ${LIs[0]}    ${us}    Warning


    Log to Console      ${\n}Expect all subport up since not all uplinks are down
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}   20s
    ...    Verify Downlink Subports Status    ${POTASH3}    ${ENC1_SERVERS[0]['enc1_downlink']}
    ...                                       ${dl_subports_all_up_active_template}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}   20s
    ...    Verify Downlink Subports Status    ${POTASH6}    ${ENC1_SERVERS[0]['enc2_downlink']}
    ...                                       ${dl_subports_all_up_active_template}

    Log to Console      ${\n}Verify Profile status back to OK
    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    \    ...    Verify Server Profile status    ${sp}    OK


OVF3581 SmartLink - Enable back last of 2 uplinks of each 3 uplinksets, verify expected downlinks subports status
    [Tags]    SmartLink    EnableLastUplink
    [Documentation]    Enable back last of 2 uplinks of each of the 3 types of uplinksets
    ...     | Expect:
    ...     |    - All uplink sets back to OK
    ...     |    - uplinks Linked/Active, with expected lagStates
    ...     |    - All S-channel of the downlink Linked/Active
    ...     |    - Server Profile back to OK

    Log to Console      ${\n}Enable back last uplink out of 2 of each of the 3 uplinksets
    Enable Ports    ${POTASH6}    ${BSIDE_UPLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log to Console     ${\n}Verify All uplinksets back to OK
    :FOR    ${us}    IN    @{ALL_UPLINK_SETS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    # Verify All uplinks lagStates
    Wait and Verify Uplinks Active lagStates

    Log to Console      ${\n}Subports should remain Linked/Active
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}   15s
    ...    Verify Downlink Subports Status    ${POTASH3}    ${ENC1_SERVERS[0]['enc1_downlink']}
    ...           ${dl_subports_all_up_active_template}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}   15s
    ...    Verify Downlink Subports Status    ${POTASH6}    ${ENC1_SERVERS[0]['enc2_downlink']}
    ...           ${dl_subports_all_up_active_template}

    Log to Console      ${\n}Verify Profile remain OK
    :FOR    ${sp}    IN    @{server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.CONN_DEPLOY_WAIT}    20s
    \    ...    Verify Server Profile status    ${sp}    OK

#OVF3581 temp test
#    [Tags]    startPing    verifyTraffic
#    #${handle} =    Start Ping Process    ${ENC1_SERVER_IP_NS_TAG}    ping_test.txt
#    ${list} =    Create List     pingTest.txt    pingTest2.txt
#    :FOR    ${file}    IN     @{list}
#    \    Run Keyword And Continue On Failure    Verify Traffic     ${file}
#    \    ...                                           ${data_common.ALLOWED_PACKET_LOSS_SCHANNEL_LAG}

#OVF3581 temp test
#    [Tags]    maxPF8
#    Log to Console     ${\n} SP with PF 5-8 connection with lag: ${server_profiles[0]}
#    Log to Console     ${\n} SP with max 8 connection with lag: ${spt_lag}
#    Log to Console     ${\n} expected subports for SP with PF5-8 conn: ${dl_subports_all_up_active_template}
#    Log to Console     ${\n} err_spt_exceed_max_bw: ${err_spt_exceed_max_bw}
#    Log to Console     ${\n} err_spt_dup_net_connections: ${err_spt_dup_net_connections}
#    Log to Console     ${\n} err_spt_different_bw_same_lag_conn: ${err_spt_different_bw_same_lag_conn}

*** Keywords ***
Login OV
    [Documentation]    Login to OneView
    Set Log Level    TRACE
    Fusion Api Login Appliance    ${appliance_ip}    ${data_common.admin_credentials}

Common Test Setup
    [Documentation]    Pre-condition keyword run before each test case
    Login OV

Common Test Teardown
    [Documentation]    Post-conditions for ALL test cases
    fusion api logout appliance

Suite Min Teardown
    [Documentation]     Minimal Suite cleanup, will clean up ping processes used for traffic verification

    Run Keyword If Any Tests Failed    Cleanup All Ping Processes


Suite Precondition Setup
    [Documentation]    Suite Pre-condition setup run before suite start
    ...                - Remove all left over ping traffic files
    ...                - create 3 types of ethernet networks; networksets
    ...                - LIG - HA, 2 frames, IBS
    ...                |  - 3 tagged, untagged and tunnel ethernet uplinksets
    ...                |  - each uplinkset with 2 uplinks, one on each side
    ...                - create EG and LE


    Remove File    ping_*

    Return from keyword if    ${skipSetup}    is    ${True}

    Login OV

    Add Ethernet Networks from variable   ${ethernet_networks}

    Add Network Sets from variable     ${network_sets}

    # Create the LIG
    Run Keyword for List    ${ligs}    Add LIG from variable

    # create EG
    Add Enclosure Group from variable    ${enc_group['${EG}']}

    Create Logical Enclosure and Verify LE uplinks lagStates


Create Logical Enclosure and Verify LE uplinks lagStates
    [Documentation]   Create 2 FRAME ME HA IBS3 LE and verify uplinkset and uplinks status
    [Tags]  LE    setup

    Log to Console     ${\n}Create HA 2frame LE and ethernet uplinksets

    Add Logical Enclosure from variable    ${les['${LE}']}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Logical Interconnect    ${LIs[0]}    status=OK    consistencyStatus=CONSISTENT

    Log to Console     ${\n}Wait for all uplinkset to reach OK status

    # With PB120, some behavior change, LI seems to be in OK status even though
    # configuration is not done, i.e., the uplinkset is still in Unknown status
    # add wait until uplinksets become OK.
    :FOR    ${us}    IN    @{ALL_UPLINK_SETS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Uplinkset Status    ${LIs[0]}    ${us}    OK

    Wait and Verify Uplinks Active lagStates

    Log to Console     ${\n}Verify Both Potashes in Configured state
    Verify Named Interconnect     ${POTASH3}    state=Configured
    Verify Named Interconnect     ${POTASH6}    state=Configured

    Log to Console     ${\n}Verify LE status OK and Consistent
    Verify Named Logical Enclosure    ${LE}    status=OK    state=Consistent


Wait and Verify Uplinks Active lagStates
    [Documentation]    Verify all uplinks in working LagStates

    Log to Console     ${\n}Verify All Uplinks lagStates
    :FOR    ${uplink}    IN    @{ASIDE_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_LAG_WAIT}    20s
    \    ...    Verify Uplink lagStates   ${POTASH3}    ${uplink}    ${data_common.LACP}

    :FOR    ${uplink}    IN    @{BSIDE_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_LAG_WAIT}    20s
    \    ...    Verify Uplink lagStates   ${POTASH6}    ${uplink}    ${data_common.LACP}


Cleanup All Ping Processes
    [Documentation]     Clean up ping processes used for traffic verification; Use by Suite teardown

    Run Keyword and Return If     os.name == "nt"    Terminate All Processes

    ${traffic_network_keys} =    Get Dictionary Keys    ${CONN_TRAFFIC_INFOS}
    :FOR    ${key}    IN    @{traffic_network_keys}
    \    ${handle} =    Set Variable      ${CONN_TRAFFIC_INFOS['${key}']['handle']}
    \    Continue For Loop If    ${handle} == ${None}
    \    ${running} =    Is Process Running     ${handle}
    \    Continue For Loop If    ${running} == ${False}
    \    Run Keyword And Continue On Failure    Stop Ping Process    ${handle}

Stop Enet Traffic Monitor For Server Connections
    [Documentation]    Stop Enet Traffic monior ping oricesses for the server connections networks
    [Arguments]    ${traffic_network_infos}    ${suffix}

    Log To Console    ${\n}Stop Ping process and verified traffic for all connections

    # Give more time for the ping process for the effect of the scenario of interest
    sleep    1m

    ${traffic_network_keys} =    Get Dictionary Keys    ${traffic_network_infos}

    # Stop all ping processes first then check traffic packet loss
    # This way we can Fail test if found traffic packet loss
    :FOR    ${key}    IN    @{traffic_network_keys}
    \    Run Keyword And Continue On Failure    Stop Ping Process    ${traffic_network_infos['${key}']['handle']}

    :FOR    ${key}    IN    @{traffic_network_keys}
    \    ${prefix} =    Set Variable    ${traffic_network_infos['${key}']['filePrefix']}
    \    Run Keyword And Continue On Failure    Verify Traffic    ${prefix}_${suffix}.txt    ${data_common.ALLOWED_PACKET_LOSS_SCHANNEL_LAG}


Start Enet Traffic Monitor For Server Connections
    [Documentation]    Start Enet Traffic monior through ping for the server connections
    ...                Start each ping process and direct output to specific output file
    ...                This routine assumes all servers connections network already pingable
    [Arguments]    ${traffic_network_infos}    ${suffix}

    Log To Console    ${\n}Start Ping process for all connections

    ${traffic_network_keys} =    Get Dictionary Keys    ${traffic_network_infos}

    :FOR    ${key}    IN    @{traffic_network_keys}
    \    ${traffic_network_info} =    Get From Dictionary    ${traffic_network_infos}    ${key}
    \    ${ip} =    Set Variable    ${traffic_network_info['IP']}
    \    ${prefix} =    Set Variable    ${traffic_network_info['filePrefix']}
    \    ${output} =    Set Variable    ${prefix}_${suffix}.txt
    \    ${handle} =    Run Keyword And Continue On Failure    Start Ping Process    ${ip}    ${output}
    \    Set To Dictionary    ${traffic_network_infos['${key}']}    handle    ${handle}
    \    OperatingSystem.File Should Exist    ${output}

Create Server Profile
    [Documentation]    Create server profile using keyword Add Server Profile from server_profile
    ...                If 'serverProfileTemplateUri' is specified, the profile is create base on SPT.
    ...                Server is powered off if it is on before creating the profile.
    ...                If timeout not provided or 0, will return resp for caller to wait and check
    ...                otherwise will wait for task and expect taskState to be Completed
    [Arguments]    ${sp}    ${timeout}=0    ${interval}=0

    # Power of server if it is on
    ${sh} =    Fvt Api Get Server Hardware By Name    ${sp['serverHardwareUri']}
    Run Keyword If    '${sh['powerState']}' == 'On'    Power off Server    ${sp['serverHardwareUri']}    PressAndHold

    # clean up if exist
    Delete Profile    ${sp['name']}

    ${resp} =    server_profile.Add Server Profile    ${sp}
    Should Be Equal As Integers    ${resp['status_code']}    202
    Return From Keyword If    '${timeout}' == '0'    ${resp}

    ${task} =    Wait For Task    ${resp}    ${timeout}    ${interval}
    Should Be Equal As Strings    ${task['taskState']}    Completed
    [Return]    ${task}


Create Server Profile Template
    [Documentation]    Create Server Profile Template
    ...                If timeout not provided or 0, will return resp for caller to wait and check
    ...                otherwise will wait for task and expect taskState to be Completed
    ...                NOTE: The reason to put server profile as input parameter is that
    ...                SHT is created at import time and there is no guarantee the name remains the
    ...                same, especially in our test environment where add/remove adapter
    ...                and ddimage and reimport occur.
    ...                Using the SPT from server hardware is guarantee to get the correct name
    [Arguments]    ${spt}    ${sp}    ${timeout}=0    ${interval}=0

    # clean up if exist
    Delete SPT    ${spt['name']}

    # Get the Server Hardware Type from server hardware of
    ${sh} =    Fvt Api Get Server Hardware By Name    ${sp['serverHardwareUri']}
    ${sht_Uri} =    Set Variable    ${sh['serverHardwareTypeUri']}

    # The RG keyword expect SHT name with SHT: prefix
    ${sht_resp} =    Fusion Api Get Server Hardware Types    uri=${sht_Uri}
    ${spt['serverHardwareTypeUri']} =    Set Variable    'SHT:' + ${sht_resp['name']}

    ${resp} =    Add Server Profile Template    ${spt}
    Should Be Equal As Integers    ${resp['status_code']}    202
    Return From Keyword If    '${timeout}' == '0'    ${resp}

    ${task} =    Wait For Task    ${resp}    ${timeout}    ${interval}
    Should Be Equal As Strings    ${task['taskState']}    Completed
    [Return]    ${task}
