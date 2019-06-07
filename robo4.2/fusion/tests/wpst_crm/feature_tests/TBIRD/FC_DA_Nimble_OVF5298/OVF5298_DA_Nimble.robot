*** Settings ***
Documentation    OVF5298 FC DirectAttach on Potash and Nitro with Nimble Storage
...
...    - Goal:
...      |  - Ensure FC DirectAttach end2end work on Nitro/Potaash with Nimble storage
...      |  - For Nitro test with LI downlinkSpeedMode 25Gb and change to 50Gb
...      |  \ \  to ensure end2end works with Quagmire2 servers
...      |  - Ensure connection outage incurred by LI downlinkSpeedMode change will recover (OVF5199)
...
...    - Usage:
...      |  - full test:
...      |  \ \ Run with LI downlinkSpeedMode 25Gb, default. same as -dls:25
...      |  \ \ - robot -V data_OVF5298_DA_Nimble_ha.py -T -d /Result/NB  OVF5298_DA_Nimble.robot
...      |  - skip precondition setup: robot -v skipSetup:True -V data_OVF5298_DA_Nimble_ha.py
...      |  \ \ \ \ -T -d /Result/NB  OVF5298_DA_Nimble.robot
...      |  - run tagged cases: robot -V data_OVF5298_DA_BB56_ha.py -i setup -i Happy -i efuse
...      |  \ \ \ \ -T -d /Result/DA  OVF5298_DA_Nimble.robot
...      |  - run tagged cases Nimble failover once: robot -V data_OVF5298_DA_BB56_ha.py
...      |  \ \ \ \ -v nfo:1 -i setup -i Happy -i Failover -T -d /Result  OVF5298_DA_Nimble.robot
...
...    - The test can test different test enclosures with configuration specified in data file.
...    - The following is eagle159 config:
...
...    - LE - 2 frame, HA. 2 LI, Potash and Nitro
...      |  - IBS1: Potash/Chroride-20
...      |  - IBS3: Nitro; 2 CXP between Methane and Nitro, total 4 CXP
...
...    - 1 DA uplinkset on Potash and Nitro Aside an Bside each
...      |  - 2 uplinks, connecting to Nimble active/standby ports
...      |  - Nitro Aside: Q1, Q2 , desiredSpeed: 16Gb (1x32Gb SFP)
...      |  - Nitro Bside: Q1:1, Q2:1 , desiredSpeed: 16Gb (1x16Gb SFP)
...      |  - Potash both sides: Q1:1, Q2:1 , desiredSpeed: 8Gb (1x8Gb SFP)
...
...    - Note:
...      |  - Nimble active/standby ports have to be in the same DA uplinkset
...      |  - Nimble currently only support 16Gb
...
...    - Servers: in enc1 and enc2; each with 2 DA connections
...      |  - All servers are WS2016, with MZ1 (Bronco) and MZ3 (Quagmire2) cards
...      |  - some servers local OS with mapped lun, some servers with BFS
...      |  - MPIO enabled
...      |  - BFS servers for Nitro and Potash connection
...      |  - Each BFS connection needs 2 target wwpn since Nimble failver is on controller basis
...
...    - Test Coverage: (Potash and Nitro)
...      |  - PortStatusReason (delete Uplinksets, compliance, portStatusReason, UFG)
...      |  \ \ - FabricMismatch
...
...      |  - end2End: BFS servers and servers with local OS and mapped lun go through the scenarios
...      |  \ \ - Happy path
...      |  \ \ - uplink speed change (Nitro:16 to 8, Potash:8 to 4) on LI uplinkset, UFG change back
...      |  \ \ - disable/enable all Aside uplinks
...      |  \ \ - disable/enable all Bside uplinks
...      |  \ \ - disable/enable downlinks, Aside and Bside
...      |  \ \ - Power off/on ICM (Aside, Bside)
...      |  \ \ - Remove/insert ICM (Aside, Bside)
...      |  \ \ - reset ICM (Aside, Bside)
...      |  \ \ - Nimble array failover  (failover --force)
...
...    - Ensure no traffic distruption, and servers lost connection recovers for the aforementioned scenarios
...
...    - Server DA storage path verification are through
...      |  \ \ - server downlink connectionMap of OneView ICM nameServers
...      |  \ \ - Nimble DA port attached devices through Nimble cli 'fc --info <port> --ctrl <ctrl>'
...
...    - Nimble attached device verification is skipped for the following due to incorrect fc info
...      |  \ \ - OneView DA uplinks speed change
...      |  \ \ - OneView LI downlinkSpeedMode change
...      |  \ \ - Nimble array failover
...
...    - LI downlinkSpeed Change to 50Gb (Nitro) and back to 25Gb
...      |  \ \ - Expect end2end connections distrupted but should recover
...      |  \ \ - BFS servers may go down but should be up afterwards
...
...    - Expected Nitro maxBandwidth, server downlink operationalSpeed are verified
...      |  in LE creation, LI downlinkSpeed Change, UFG, ICM efuse, power, reset scenarios.
...      |  based on LI downlinkSpeedMode and servers MZ card
...      |  \ \ For DLS mode 50Gb:
...      |  \ \ \ \ - Quagmire2 connection downlink operationalSpeed: 50Gb
...      |  \ \ For DLS mode 25Gb:
...      |  \ \ \ \ - Quagmire2 connection downlink operationalSpeed: 25Gb
...


Resource         ../../../../../Resources/api/fusion_api_resource.txt
Resource         ../FVT/fvt-keywords.txt
Resource         ../FVT/Resources/fvt_resource.txt
Resource         ../FC_Nitro_OVF3323/DF_keywords.txt

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
${nfo}          2
${downlink_mode}    SPEED_25GB
${expected_ic_maxbw}    SPEED_25G

*** Test Cases ***

OVF5298 Create Logical Enclosure and Verify LI LE and uplinks status and speed
    [Documentation]   Create 2 FRAME ME HA LE with DA Uplinksets defined on each side
    [Tags]  LE    setup    Potash     Nitro

    Run Keyword for List    ${ligs}    Add LIG from variable

    # create EG
    Add Enclosure Group from variable    ${enc_group['${EG}']}

    Add Logical Enclosure from variable    ${les['${LE}']}

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    # Log    ${\n}Change LI downlinkSpeedMode to ${downlink_mode}    console=True
    Run Keyword if    '${downlink_mode}' != 'SPEED_25GB'
    ...    Change LI downlinkSpeedMode    ${LIs[1]}    ${downlink_mode}


OVF5298 Verify all DA uplinkports connected Nimble portWWN
    [Tags]   IC    setup    DAUplinks    Potash     Nitro

    Verify Happy Uplinks DA ports


OVF5298 Remove Nitro Aside and Potash Bside Uplinksets
    [Tags]  DeleteUS    LiUSPortStatusReason    Potash     Nitro
    [Documentation]    Delete Nitro Aside uplinkset and Potash Bside uplinkset
    ...                Verify LI Inconsistent

    Log    ${\n}Remove Nitro Aside uplinkset and Potash Bside uplinkset    console=True

    ${usp_b} =    fvt-keywords.Get Uplink Set By Name    ${LIs[0]}    ${POTASH_BSIDE_UPLINK_SET}
    ${usn_a} =    fvt-keywords.Get Uplink Set By Name    ${LIs[1]}    ${NITRO_ASIDE_UPLINK_SET}

    @{us_uris} =    Create List    ${usn_a['uri']}    ${usp_b['uri']}

    :FOR    ${us}    IN    @{us_uris}
    \    ${resp} =    Remove Uplinkset By Uri    ${us}
    \    ${task} =    Wait For Task    ${resp}    ${data_common.US_DELETE_WAIT}    30s
    \    Should Be Equal As Strings    ${task['taskState']}    Completed

    Log    ${\n}Wait until uplinks are Unlinked    console=True
    :FOR    ${uplink}    IN    @{US_NITRO_ASIDE_UPLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Port    ${NITROA}    ${uplink}    portStatus=Unlinked

    :FOR    ${uplink}    IN    @{US_POTASH_BSIDE_UPLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Port    ${POTASHB}    ${uplink}    portStatus=Unlinked

    :FOR    ${li}    IN    @{LIs}
    \    Verify Logical Interconnect    ${li}    status=Warning    consistencyStatus=NOT_CONSISTENT


OVF5298 LI DA uplink Unlinked and FabricTypeMismatch portStatusReason
    [Tags]  LiUSPortStatusReason    statusReason    Potash     Nitro
    [Documentation]    Tested Potash/Nitro FA Uplinkset is created with DA uplinks
    ...                Expect FabricTypeMismatch portStatusReason and Unlinked portstatus

    :FOR    ${li_us}    IN    @{li_us_port_unlink_list}
    \    ${li_uri} =    Get LI URI    ${li_us['logicalInterconnectUri']}
    \    ${us} =     Copy Dictionary    ${li_us['usBody']}
    \    ${body} =    Build US body    ${us}    ${li_uri}
    \    ${resp} =    Fusion Api Create Uplink Set    body=${body}
    \    ${task} =    Wait For Task    ${resp}    5min    15s
    \    Should Be Equal As Strings    ${task['taskState']}    Completed
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_ERROR_WAIT}    30s
    \    ...    Verify Port    ${li_us['icm']}    ${li_us['uplink']}    status=Critical
    \    ...        portStatus=Unlinked    portStatusReason=${li_us['expected_reason']}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_SPEED_WAIT}    20s
    \    ...    Verify Uplinkset Status    ${li_us['logicalInterconnectUri']}
    \    ...           ${us['name']}    Critical


OVF5298 LI Update From Group Remove added FA uplinksets and Add back deleted ones
    [Tags]  LiUSPortStatusReason    LIUFGAddUS    Potash     Nitro
    [Documentation]    LI update from group - remove and add back DA uplinksets
    ...                Verify DA uplinkset status, uplinkport operationalSpeed and connectedTo
    ...                Verify LI and LE Consistent and
    ...                Nitro maxBandwidth and servers downlink operationalSpeed

    Log    ${\n}Perform LI UFG - remove added uplinksets, add back old deleted ones    console=True
    :FOR    ${li}    IN    @{LIs}
    \    Perform LI Update From Group    ${li}    ${data_common.UFG_WAIT}    30s

    Verify Happy LE and LI


OVF5298 Create Server Profiles Each With 2 DirectAttach Connections, Verify Profile status
    [Tags]  SP    Happy    Potash     Nitro
    [Documentation]    Create Server Profiles with connections defined on Potash and Nitro

    :FOR     ${sp}    IN     @{server_profiles}
    \    Create Server Profile    ${sp}    ${data_common.SP_CREATE_WAIT}    20s
    \    Run Keyword And Continue On Failure    Verify Server Profile Status    ${sp['name']}    OK


OVF5298 Power On Servers, Verify Servers DA Connections
    [Tags]  ServerEnd2End    Happy    Potash     Nitro

    # power on servers
    Run Keyword for List    ${server_hws}    Power on Server
    Log    ${\n}Waiting ${data_common.BFS_SERVER_BOOT_WAIT} minutes for servers to boot and come up
    ...    console=True

    Sleep    ${data_common.BFS_SERVER_BOOT_WAIT}

    # Nitro servers are Gen10 which boot faster, wait for them before Potash Gen9 servers
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    OK

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    OK

    # Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Servers DA Connections

    # Double check DA connected Nimble port attached devices
    Verify Happy DA Nimble ports Attached Devices


OVF5298 Disable Nitro Aside Uplinks Case, affect Servers Aside Connection, verify servers Bside DA connection OK
    [Tags]  DisNULA   DisEnaNULA    DisEnaUL    Nitro
    [Documentation]    Disable Aside DA uplinkset both uplinks
    ...                Expect uplinkset to be Critical status, profile Critical,
    ...                servers lose storage path

    # For Nimbe array, the failover is per controller, when all active ports in use are down,
    # then the failover occurs. Standby port remains Linked/LoggedIn unless it's disabled.
    Log    ${\n}Disable Nitro Aside uplinkset uplinks    console=True
    Disable Ports    ${NITROA}    ${US_NITRO_ASIDE_UPLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify uplink status, portStatus and disabled    console=True
    :FOR    ${ul}    IN    @{US_NITRO_ASIDE_UPLINKS}
    \    Verify Port    ${NITROA}    ${ul}    status=Warning
    \    ...             portStatus=Unlinked    enabled=${False}

    Log    ${\n}Verify affected uplinkset status    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[1]}    ${NITRO_ASIDE_UPLINK_SET}    Critical

    Log    ${\n}Verify server profiles status become Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    Critical

    Log    ${\n}Verify affected servers Aside connectionMap should be empty    console=True
    ${nameservers_ic} =    Get IC NameServers    ${NITROA}
    Should Not Be Empty    ${nameservers_ic}

    :FOR    ${ul}    IN    @{US_NITRO_ASIDE_UPLINKS}
    \    Log     ${\n}Verify disabled uplinks ${ul} not in nameServers    console=True
    \    Verify Port Not In nameServers    ${nameservers_ic}    ${ul}

    Log     ${\n}Verify servers DA connection on Aside, expect no connections    console=True
    # Expect all servers Aside downlink connectionMap is ['']
    ${expected_conn_map} =    Create List    ${EMPTY}
    :FOR    ${dl}    IN    @{NITRO_ASIDE_SERVER_DOWNLINKS}
    \    Verify Server DA Connection    ${nameservers_ic}    ${dl}    ${expected_conn_map}

    Log    ${\n}Verify servers DA connection on Bsdie are not affected    console=True
    Run Keyword And Continue On Failure    Verify Happy Nitro Servers Bside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Nitro Bside DA Nimble ports Attached Devices


OVF5298 Enable back Nitro Aside Uplinks Case, verify Aside servers Connection Restoration
    [Tags]  EnaNULA    DisEnaNULA    DisEnaUL    Nitro
    [Documentation]    Enable back Aside DA uplinkset both uplinks at the same time
    ...                Expect uplinks, uplinkset, server profiles back to OK
    ...                and servers storage access restored and logins redistribute

    Log    ${\n}Enable back Nitro Aside uplinkset uplinkports    console=True
    Enable Ports     ${NITROA}    ${US_NITRO_ASIDE_UPLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log   ${\n}Verify affected uplinksets back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[1]}    ${NITRO_ASIDE_UPLINK_SET}    OK

    Log    ${\n}Verify uplink status, portStatus and enabled    console=True
    :FOR    ${ul}    IN    @{US_NITRO_ASIDE_UPLINKS}
    \    Verify Port    ${NITROA}    ${ul}    status=OK    portStatus=Linked
    \    ...    enabled=${True}    operationalSpeed=${NITRO_ORIG_UPLINK_SPEED}

    Log    ${\n}VVerify Server Profiles status back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    OK

    Run Keyword And Continue On Failure    Verify Happy Nitro Aside Uplinks DA ports

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Nitro Servers DA Connections
    Verify Happy Nitro DA Nimble ports Attached Devices


OVF5298 Disable Nitro Bside Uplinks Case, affect Servers Bside Connection, verify servers Aside DA connection OK
    [Tags]  DisNULB   DisEnaNULB    DisEnaUL    Nitro
    [Documentation]    Disable Bside DA uplinkset both uplinks
    ...                Expect uplinkset to be Critical status, profile Critical,
    ...                servers lose storage path

    # For Nimbe array, the failover is per controller, when all active ports in use are down,
    # then the failover occurs. Standby port remains Linked/LoggedIn unless it's disabled.
    Log    ${\n}Disable Nitro Bside uplinkset uplinks    console=True
    Disable Ports    ${NITROB}    ${US_NITRO_BSIDE_UPLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify uplink status, portStatus and disabled    console=True
    :FOR    ${ul}    IN    @{US_NITRO_BSIDE_UPLINKS}
    \    Verify Port    ${NITROB}    ${ul}    status=Warning
    \    ...             portStatus=Unlinked    enabled=${False}

    Log    ${\n}Verify affected uplinkset status    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[1]}    ${NITRO_BSIDE_UPLINK_SET}    Critical

    Log    ${\n}Verify server profiles status going through US-DA1 become Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    Critical

    Log    ${\n}Verify affected servers Bside connectionMap should be empty    console=True
    ${nameservers_ic} =    Get IC NameServers    ${NITROB}
    Should Not Be Empty    ${nameservers_ic}

    :FOR    ${ul}    IN    @{US_NITRO_BSIDE_UPLINKS}
    \    Log     ${\n}Verify disabled uplinks ${ul} not in nameServers    console=True
    \    Verify Port Not In nameServers    ${nameservers_ic}    ${ul}

    Log     ${\n}Verify servers DA connection on Bside, expect no connections    console=True
    # Expect all servers Bside downlink connectionMap is ['']
    ${expected_conn_map} =    Create List    ${EMPTY}
    :FOR    ${dl}    IN    @{NITRO_BSIDE_SERVER_DOWNLINKS}
    \    Verify Server DA Connection    ${nameservers_ic}    ${dl}    ${expected_conn_map}

    Log    ${\n}Verify servers DA connection on Asdie are not affected    console=True
    Run Keyword And Continue On Failure    Verify Happy Nitro Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Nitro Aside DA Nimble ports Attached Devices


OVF5298 Enable back Nitro Bside Uplinks Case, verify Bside servers Connection Restoration
    [Tags]  EnaNULB    DisEnaNULB    DisEnaUL    Nitro
    [Documentation]    Enable back Bside DA uplinkset both uplinks at the same time
    ...                Expect uplinks, uplinkset, server profiles back to OK
    ...                and servers storage access restored and logins redistribute

    Log    ${\n}Enable back Nitro Bside uplinkset uplinkports    console=True
    Enable Ports     ${NITROB}    ${US_NITRO_BSIDE_UPLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log   ${\n}Verify affected uplinksets back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[1]}    ${NITRO_BSIDE_UPLINK_SET}    OK

    Log    ${\n}Verify uplink status, portStatus and enabled    console=True
    :FOR    ${ul}    IN    @{US_NITRO_BSIDE_UPLINKS}
    \    Verify Port    ${NITROB}    ${ul}    status=OK    portStatus=Linked
    \    ...    enabled=${True}    operationalSpeed=${NITRO_ORIG_UPLINK_SPEED}

    Log    ${\n}VVerify Server Profiles status back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    OK

    Run Keyword And Continue On Failure    Verify Happy Nitro Bside Uplinks DA ports

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Nitro Servers DA Connections
    Verify Happy Nitro DA Nimble ports Attached Devices


OVF5298 Disable Potash Aside Uplinks, affect Servers Aside Connection, verify servers Bside connection OK
    [Tags]  DisPULA    DisEnaPULA   DisEnaUL    Potash
    [Documentation]    Disable Potash Aside uplinkset both uplinkports in one update port REST call
    ...                Expect Uplinkset Critical, profile connection error
    ...                servers Aside storage access lost. Bside not impacted

    Log   ${\n}Disable both uplinks    console=True
    Disable Ports    ${POTASHA}    ${US_POTASH_ASIDE_UPLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log   ${\n}Verify affected uplinksets Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[0]}    ${POTASH_ASIDE_UPLINK_SET}    Critical

    Log    ${\n}Verify uplink status portStatus and disabled    console=True
    :FOR    ${disabled_port}    IN    @{US_POTASH_ASIDE_UPLINKS}
    \    Verify Port    ${POTASHA}    ${disabled_port}    status=Warning
    \    ...    portStatus=Unlinked    enabled=${False}

    #Verify all server profiles status become Critical
    Log      ${\n}Verify Server Profiles status Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    Critical

    ${nameservers_ic} =    Get IC NameServers    ${POTASHA}
    Should Not Be Empty    ${nameservers_ic}

    :FOR    ${disabled_port}    IN    @{US_POTASH_ASIDE_UPLINKS}
    \    Log      ${\n}Verify disabled uplink ${disabled_port} not in nameServers    console=True
    \    Verify Port Not In nameServers    ${nameservers_ic}    ${disabled_port}

    Log     ${\n}Verify servers DA connection on Aside, expect no connections    console=True
    # Expect all servers Bside downlink connectionMap is ['']
    ${conn_map} =    Create List    ${EMPTY}
    :FOR    ${dl}    IN    @{POTASH_ASIDE_SERVER_DOWNLINKS}
    \    Verify Server DA Connection    ${nameservers_ic}    ${dl}    ${conn_map}

    #Verify Servers DA connections on Bside not affected
    Run Keyword And Continue On Failure    Verify Happy Potash Servers Bside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Potash Bside DA Nimble ports Attached Devices


OVF5298 Enable back Potash Aside Uplinks, Aside Connection Restoration, Verify servers DA connections
    [Tags]  EnablePULA    DisEnaPULA    DisEnaUL    Potash
    [Documentation]    Enable back Potash Aside DA uplinkset
    ...                  - Expect uplinkset to be OK status,
    ...                  - Profiles back to OK
    ...                  - Servers recover connections (storage path)
    ...                    verified through DA nameServers connection map and
    ...                    storage attached devices information

    Log   ${\n}Enable back Potash Aside uplinks    console=True
    Enable Ports     ${POTASHA}    ${US_POTASH_ASIDE_UPLINKS}   ${data_common.SUBPORT_STATUS_WAIT}

    Log   ${\n}Verify uplinkset back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[0]}    ${POTASH_ASIDE_UPLINK_SET}    OK

    Log    ${\n}Verify uplink status, portStatus and enabled    console=True
    :FOR    ${ul}    IN    @{US_POTASH_ASIDE_UPLINKS}
    \    Verify Port    ${POTASHA}    ${ul}    status=OK    portStatus=Linked
    \    ...    enabled=${True}    operationalSpeed=${POTASH_ORIG_UPLINK_SPEED}

    Log   ${\n}Verify Server Profiles back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    OK

    Run Keyword And Continue On Failure    Verify Happy Potash Aside Uplinks DA ports
    Verify Happy Potash Servers DA Connections
    Verify Happy Potash DA Nimble ports Attached Devices


OVF5298 Disable Potash Bside Uplinks, affect Servers Bside Connection, verify servers Aside connection OK
    [Tags]  DisPULB    DisEnaPULB   DisEnaUL    Potash
    [Documentation]    Disable Potash Bside uplinkset both uplinkports in one update port REST call
    ...                Expect Uplinkset Critical, profile connection error
    ...                servers Bside storage access lost. Aside not impacted

    Log   ${\n}Disable both uplinks    console=True
    Disable Ports    ${POTASHB}    ${US_POTASH_BSIDE_UPLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log   ${\n}Verify affected uplinksets Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[0]}    ${POTASH_BSIDE_UPLINK_SET}    Critical

    Log    ${\n}Verify uplink status portStatus and disabled    console=True
    :FOR    ${disabled_port}    IN    @{US_POTASH_BSIDE_UPLINKS}
    \    Verify Port    ${POTASHB}    ${disabled_port}    status=Warning
    \    ...    portStatus=Unlinked    enabled=${False}

    # Verify all server profiles status become Critical
    Log      ${\n}Verify Server Profiles status Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    Critical

    ${nameservers_ic} =    Get IC NameServers    ${POTASHB}
    Should Not Be Empty    ${nameservers_ic}

    :FOR    ${disabled_port}    IN    @{US_POTASH_BSIDE_UPLINKS}
    \    Log      ${\n}Verify disabled uplink ${disabled_port} not in nameServers    console=True
    \    Verify Port Not In nameServers    ${nameservers_ic}    ${disabled_port}

    Log     ${\n}Verify servers DA connection on Bside, expect no connections    console=True
    # Expect all servers Bside downlink connectionMap is ['']
    ${conn_map} =    Create List    ${EMPTY}
    :FOR    ${dl}    IN    @{POTASH_BSIDE_SERVER_DOWNLINKS}
    \    Verify Server DA Connection    ${nameservers_ic}    ${dl}    ${conn_map}

    # Verify Servers DA connections on Aside not affected
    Run Keyword And Continue On Failure    Verify Happy Potash Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Potash Aside DA Nimble ports Attached Devices


OVF5298 Enable back Potash Bside Uplinks, Bside Connection Restoration, Verify servers DA connections
    [Tags]  EnablePULB    DisEnaPULB    DisEnaUL    Potash
    [Documentation]    Enable back Potash Bside DA uplinkset
    ...                  - Expect uplinkset to be OK status,
    ...                  - Profiles back to OK
    ...                  - Servers recover connections (storage path)
    ...                    verified through DA nameServers connection map and
    ...                    storage attached devices information

    Log   ${\n}Enable back Potash Bside uplinks    console=True
    Enable Ports     ${POTASHB}    ${US_POTASH_BSIDE_UPLINKS}   ${data_common.SUBPORT_STATUS_WAIT}

    Log   ${\n}Verify uplinkset back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    ...    Verify Uplinkset Status    ${LIs[0]}    ${POTASH_BSIDE_UPLINK_SET}    OK

    Log    ${\n}Verify uplink status, portStatus and enabled    console=True
    :FOR    ${ul}    IN    @{US_POTASH_BSIDE_UPLINKS}
    \    Verify Port    ${POTASHB}    ${ul}    status=OK    portStatus=Linked
    \    ...    enabled=${True}    operationalSpeed=${POTASH_ORIG_UPLINK_SPEED}

    Log   ${\n}Verify Server Profiles back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    OK

    Run Keyword And Continue On Failure    Verify Happy Potash Bside Uplinks DA ports
    Verify Happy Potash Servers DA Connections
    Verify Happy Potash DA Nimble ports Attached Devices


OVF5298 Disable Potash Aside Downlinks, Affect Server Aside Connection, Verify servers Bside DA connections OK
    [Tags]  DisPDLA    DisEnaPDL    Potash

    Log    ${\n}Disable Potash Aside server downlinks    console=True
    Disable Ports    ${POTASHA}    ${POTASH_ASIDE_SERVER_DOWNLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify Server Profiles with disabled downlink status Critical    console=True

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    Critical

    Log    ${\n}Verify downlink status, portStatus and disabled    console=True
    :FOR    ${dl}    IN    @{POTASH_ASIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${POTASHA}    ${dl}    status=Critical    portStatus=Unlinked
    \    ...    enabled=${False}

    Log    ${\n}Verify disabled downlink should not be in nameServers    console=True
    ${nameservers_ic} =    Get IC NameServers    ${POTASHA}
    Should Not Be Empty    ${nameservers_ic}
    :FOR    ${dl}    IN    @{POTASH_ASIDE_SERVER_DOWNLINKS}
    \    Verify Port Not In nameServers    ${nameservers_ic}    ${dl}

    Log    ${\n}Verify Potash servers Bside connection not affected    console=True
    Run Keyword And Continue On Failure    Verify Happy Potash Servers Bside DA Connections
    Run Keyword And Continue On Failure    Verify Happy potash Bside DA Nimble ports Attached Devices


OVF5298 Enable Back Potash Aside Downlinks, Aside Connection Restoration, Verify servers DA connections
    [Tags]  EnablePDLA    DisEnaPDL    Potash

    Log      ${\n}Enable back the servers Potash downlink on Aside    console=True

    Enable Ports    ${POTASHA}    ${POTASH_ASIDE_SERVER_DOWNLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    OK

    Log    ${\n}Verify downlink status, portStatus and enabled    console=True

    :FOR    ${dl}    IN    @{POTASH_ASIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${POTASHA}    ${dl}    status=OK    portStatus=Linked    enabled=${True}

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Potash Servers DA Connections
    Verify Happy Potash DA Nimble ports Attached Devices


OVF5298 Disable Potash Bside Downlinks, Affect Server Bside Connection, Verify servers Aside DA connections OK
    [Tags]  DisPDLB    DisEnaPDL    Potash

    Log    ${\n}Disable Potash Bside server downlinks    console=True
    Disable Ports    ${POTASHB}    ${POTASH_BSIDE_SERVER_DOWNLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify Server Profiles with disabled downlink status Critical    console=True

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    Critical

    Log    ${\n}Verify downlink status, portStatus and disabled    console=True
    :FOR    ${dl}    IN    @{POTASH_BSIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${POTASHB}    ${dl}    status=Critical    portStatus=Unlinked
    \    ...    enabled=${False}

    Log    ${\n}Verify disabled downlink should not be in nameServers    console=True
    ${nameservers_ic} =    Get IC NameServers    ${POTASHB}
    Should Not Be Empty    ${nameservers_ic}
    :FOR    ${dl}    IN    @{POTASH_ASIDE_SERVER_DOWNLINKS}
    \    Verify Port Not In nameServers    ${nameservers_ic}    ${dl}

    Log    ${\n}Verify Potash servers Aside connection not affected    console=True

    Run Keyword And Continue On Failure    Verify Happy Potash Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy potash Aside DA Nimble ports Attached Devices


OVF5298 Enable Back Potash Bside Downlinks, Bside Connection Restoration, Verify servers DA connections
    [Tags]  EnaPDLB    DisEnaPDL        Potash

    Log      ${\n}Enable back the servers Potash downlink on Bside    console=True
    Enable Ports    ${POTASHB}    ${POTASH_BSIDE_SERVER_DOWNLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    OK

    Log    ${\n}Verify downlink status, portStatus and enabled    console=True
    :FOR    ${dl}    IN    @{POTASH_BSIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${POTASHB}    ${dl}    status=OK    portStatus=Linked    enabled=${True}

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Potash Servers DA Connections
    Verify Happy Potash DA Nimble ports Attached Devices


OVF5298 Disable Nitro Aside Downlinks, Affect Server Aside Connection, Verify servers Bside DA connections OK
    [Tags]  DisableNDLA    DisEnaNDL    Nitro

    Log    ${\n}Disable Nitro Aside server downlinks    console=True
    Disable Ports    ${NITROA}    ${NITRO_ASIDE_SERVER_DOWNLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify Server Profiles with disabled downlink status Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    Critical

    Log    ${\n}Verify downlink status, portStatus and disabled    console=True
    :FOR    ${dl}    IN    @{NITRO_ASIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${NITROA}    ${dl}    status=Critical    portStatus=Unlinked
    \    ...    enabled=${False}

    Log    ${\n}Verify disabled downlink should not be in nameServers    console=True
    ${nameservers_ic} =    Get IC NameServers    ${NITROA}
    Should Not Be Empty    ${nameservers_ic}
    :FOR    ${dl}    IN    @{NITRO_ASIDE_SERVER_DOWNLINKS}
    \    Verify Port Not In nameServers    ${nameservers_ic}    ${dl}

    Log    ${\n}Verify Potash servers Bside connection not affected    console=True
    Run Keyword And Continue On Failure    Verify Happy Nitro Servers Bside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Nitro Bside DA Nimble ports Attached Devices


OVF5298 Enable Back Nitro Aside Downlinks, Aside Connection Restoration, Verify servers DA connections
    [Tags]  EnableNDLA    DisEnaNDL    Nitro

    Log      ${\n}Enable back the servers Nitro downlink on Aside    console=True
    Enable Ports    ${NITROA}    ${NITRO_ASIDE_SERVER_DOWNLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    OK

    Log    ${\n}Verify downlink status, portStatus and enabled    console=True
    :FOR    ${dl}    IN    @{NITRO_ASIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked    enabled=${True}

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Nitro Servers DA Connections

    Verify Happy Nitro DA Nimble ports Attached Devices


OVF5298 Disable Nitro Bside Downlinks, Affect Server Bside Connection, Verify servers Aside DA connections OK
    [Tags]  DisNDLB    DisEnaNDL    Nitro

    Log    ${\n}Disable Nitro Bside server downlinks    console=True
    Disable Ports    ${NITROB}    ${NITRO_BSIDE_SERVER_DOWNLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Log    ${\n}Verify Server Profiles with disabled downlink status Critical    console=True

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    Critical

    Log    ${\n}Verify downlink status, portStatus and disabled    console=True
    :FOR    ${dl}    IN    @{NITRO_BSIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${NITROB}    ${dl}    status=Critical    portStatus=Unlinked
    \    ...    enabled=${False}

    Log    ${\n}Verify disabled downlink should not be in nameServers    console=True
    ${nameservers_ic} =    Get IC NameServers    ${NITROB}
    Should Not Be Empty    ${nameservers_ic}
    :FOR    ${dl}    IN    @{NITRO_BSIDE_SERVER_DOWNLINKS}
    \    Verify Port Not In nameServers    ${nameservers_ic}    ${dl}

    Log    ${\n}Verify Nitro servers Aside connection not affected    console=True

    Run Keyword And Continue On Failure    Verify Happy Nitro Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Nitro Aside DA Nimble ports Attached Devices


OVF5298 Enable Back Nitro Bside Downlinks, Bside Connection Restoration, Verify servers DA connections
    [Tags]  EnaDLB    DisEnaNDL    Nitro

    Log      ${\n}Enable back the servers Nitro downlink on Bside    console=True
    Enable Ports    ${NITROB}    ${NITRO_BSIDE_SERVER_DOWNLINKS}    ${data_common.SUBPORT_STATUS_WAIT}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    OK

    Log    ${\n}Verify downlink status, portStatus and enabled    console=True
    :FOR    ${dl}    IN    @{NITRO_BSIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${NITROB}    ${dl}    status=OK    portStatus=Linked    enabled=${True}

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Nitro Servers DA Connections
    Verify Happy Nitro DA Nimble ports Attached Devices


OVF5298 Power Off Aside Potash affecting Aside connections, Verify servers Bside DA connections OK
    [Tags]  PowerOffPA    PowerPA    Power    Potash
    [Documentation]    power off Aside Potash, servers will lose Aside DA connection
    ...                Servers Bside storage access os not impacted

    Log    ${\n}Power off Aside Potash and wait for Maintenance state    console=True
    Power IC and Wait    ${POTASHA}    Off

    Log     ${\n}Verify Bside Interconnect remains Configured and become Master    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect    ${POTASHB}    state=Configured
    ...           stackingDomainRole=${data_common.MASTER}

    # Profiles, LI and uplinksets are no longer guranteed to be Critical
    # Engineer - after ICM is maintenance, the SDS is not polle hence port status is not updated
    # remove verification
    # Log to Console     ${\n}Verify Aside uplinksets Critical
    # :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    # \    Verify Uplinkset Status    ${LIs[0]}    ${us}    Critical
    # Log to Console      ${\n}Verify Profile status Critical
    # Run Keyword And Continue On Failure    Verify Server Profiles status
    # ...     ${server_profile_names}    Critical

    Log     ${\n}Verify Bside DA Uplinks portStatus not impacted    console=True
    :FOR    ${uplink}    IN    @{US_POTASH_BSIDE_UPLINKS}
    \    Verify Port    ${POTASHB}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Bside uplinksets OK, not impacted    console=True
    Verify Uplinkset Status    ${LIs[0]}    ${POTASH_BSIDE_UPLINK_SET}    OK

    Log     ${\n}Verify servers DA connection on Bside remain intact    console=True
    Run Keyword And Continue On Failure    Verify Happy Potash Servers Bside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Potash Bside DA Nimble ports Attached Devices


OVF5298 Power On Aside Potash Restoring Aside connections, Verify servers DA connections
    [Tags]  PowerOnPA    PowerPA    Power
    [Documentation]    Power back on Aside Potash affecting servers connection through US-DA1
    ...                Expect uplinkset defined on Aside back to OK, and profiles connection OK
    ...                servers connection path through Aside is restored
    ...                and servers downlink operationalSpeed

    Log     ${\n}Power back on Aside Nitro and wait for Configured state    console=True
    Power IC and Wait    ${POTASHA}    On

    Log     ${\n}Verify Aside Interconnect come up as Subordinate    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${POTASHA}    stackingDomainRole=${data_common.SUBORDINATE}

    Log    ${\n}Verify Bside Interconnect remain Master, Configured    console=True
    Verify Named Interconnect     ${POTASHB}    state=Configured
    ...          stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify DA Uplinks status and portStatus    console=True
    :FOR    ${uplink}    IN    @{US_POTASH_ASIDE_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Port    ${POTASHA}    ${uplink}    status=OK    portStatus=Linked
    \    ...                   operationalSpeed=${POTASH_ORIG_UPLINK_SPEED}

    Log     ${\n}Verify Aside downlinks back to Linked OK    console=True
    :FOR    ${dl}    IN    @{POTASH_ASIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${POTASHA}    ${dl}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside and Bside uplinksets OK    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Uplinkset Status    ${LIs[0]}    ${POTASH_ASIDE_UPLINK_SET}    OK


    Log     ${\n}Verify servers Profile status OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    OK

    Run Keyword And Continue On Failure    Verify Happy Potash Aside Uplinks DA ports
    Verify Happy Potash Servers DA Connections
    Verify Happy Potash DA Nimble ports Attached Devices


OVF5298 Power Off Bside Potash affecting Bside connections, Verify servers Bside DA connections OK
    [Tags]  PowerOffPB    PowerPB    Power    Potash
    [Documentation]    power off Bside Potash, servers will lose Bside DA connection
    ...                Servers Aside storage access os not impacted

    Log    ${\n}Power off Bside Potash and wait for Maintenance state    console=True
    Power IC and Wait    ${POTASHB}    Off

    Log     ${\n}Verify Bside Interconnect remains Configured and become Master    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect    ${POTASHA}    state=Configured
    ...           stackingDomainRole=${data_common.MASTER}

    # In recenet build, profiles, LI and uplinksets are no longer guranteed to be Critical
    # After ICM is maintenance, the SDS is not polle hence port status is not updated
    # LI, uplinksets and server profiles are no longer guranteed to be Critical

    Log     ${\n}Verify Aside DA Uplinks portStatus not impacted    console=True
    :FOR    ${uplink}    IN    @{US_POTASH_ASIDE_UPLINKS}
    \    Verify Port    ${POTASHA}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Bside uplinksets OK, not impacted    console=True
    Verify Uplinkset Status    ${LIs[0]}    ${POTASH_ASIDE_UPLINK_SET}    OK

    Log     ${\n}Verify servers DA connection on Aside remain intact    console=True
    Run Keyword And Continue On Failure    Verify Happy Potash Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Potash Aside DA Nimble ports Attached Devices


OVF5298 Power On Bside Potash Restoring Bside connections, Verify servers DA connections
    [Tags]  PowerOnPB    PowerPB    Power    Potash
    [Documentation]    Power back on Bside Potash
    ...                Expect uplinkset defined on Bside back to OK, and profiles connection OK
    ...                servers connection path through Bside is restored

    Log     ${\n}Power back on Bside Potash and wait for Configured state    console=True
    Power IC and Wait    ${POTASHB}    On

    Log     ${\n}Verify Bside Interconnect come up as Subordinate    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${POTASHB}    stackingDomainRole=${data_common.SUBORDINATE}

    Log    ${\n}Verify Aside Interconnect remain Master, Configured    console=True
    Verify Named Interconnect     ${POTASHA}    state=Configured
    ...          stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify DA Uplinks status and portStatus    console=True
    :FOR    ${uplink}    IN    @{US_POTASH_BSIDE_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Port    ${POTASHB}    ${uplink}    status=OK    portStatus=Linked
    \    ...                   operationalSpeed=${POTASH_ORIG_UPLINK_SPEED}

    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Uplinkset Status    ${LIs[0]}    ${POTASH_BSIDE_UPLINK_SET}    OK

    Log     ${\n}Verify Bside downlinks back to Linked OK    console=True
    :FOR    ${dl}    IN    @{POTASH_BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${POTASHB}    ${dl}    status=OK    portStatus=Linked


    Log     ${\n}Verify servers Profile status OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    OK

    Run Keyword And Continue On Failure    Verify Happy Potash Bside Uplinks DA ports
    Verify Happy Potash Servers DA Connections
    Verify Happy Potash DA Nimble ports Attached Devices


OVF5298 Power Off Aside Nitro affecting Aside connections, Verify servers Bside DA connections OK
    [Tags]  PowerOffNA    PowerNA    Power    Nitro
    [Documentation]    power off Aside Nitro, all servers will lose Aside DA connection
    ...                Servers Bside storage access os not impacted

    Log    ${\n}Power off Aside Nitro and wait for Maintenance state    console=True
    Power IC and Wait    ${NITROA}    Off

    Log     ${\n}Verify Bside Interconnect remains Configured and become Master    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect    ${NITROB}    state=Configured
    ...           stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify Bside DA Uplinks portStatus not impacted    console=True
    :FOR    ${uplink}    IN    @{US_NITRO_BSIDE_UPLINKS}
    \    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Bside uplinksets OK, not impacted    console=True
    Verify Uplinkset Status    ${LIs[1]}    ${NITRO_BSIDE_UPLINK_SET}    OK

    Log     ${\n}Verify servers DA connection on Bside remain intact    console=True
    Run Keyword And Continue On Failure    Verify Happy Nitro Servers Bside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Nitro Bside DA Nimble ports Attached Devices


OVF5298 Power On Aside Nitro Restoring Aside connections, Verify servers DA connections
    [Tags]  PowerOnNA    PowerNA    Power    Nitro
    [Documentation]    Power back on Aside Nitro
    ...                Expect uplinkset defined on Bside back to OK, and profiles connection OK
    ...                servers connection path through Bside is restored
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
    :FOR    ${uplink}    IN    @{US_NITRO_ASIDE_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked
    \    ...                   operationalSpeed=${NITRO_ORIG_UPLINK_SPEED}

    Log     ${\n}Verify Aside and Bside uplinksets OK    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Uplinkset Status    ${LIs[1]}    ${NITRO_ASIDE_UPLINK_SET}    OK

    Log     ${\n}Verify Aside downlinks back to Linked OK    console=True
    :FOR    ${dl}    IN    @{NITRO_ASIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    Log     ${\n}Verify servers Profile status OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    OK

    Verify Happy Nitro Uplinks DA ports

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Nitro Servers DA Connections
    Verify Happy Nitro DA Nimble ports Attached Devices


OVF5298 Power Off Bside Nitro Affecting Bside connections, Verify servers Aside DA connections OK
    [Tags]  PowerOffNB    PowerNB    Power    Nitro
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
    :FOR    ${uplink}    IN    @{US_NITRO_ASIDE_UPLINKS}
    \    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked

    Log    ${\n}Verify Aside uplinksets OK, not impacted    console=True
    Verify Uplinkset Status    ${LIs[1]}    ${NITRO_ASIDE_UPLINK_SET}    OK


    Run Keyword And Continue On Failure    Verify Happy Nitro Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Nitro Aside DA Nimble ports Attached Devices


OVF5298 Power On Bside Nitro Restoring Bside connections, Verify servers DA connections
    [Tags]  PowerOnBside    PowerB    Power    Nitro
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
    :FOR    ${uplink}    IN    @{US_NITRO_BSIDE_UPLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked
    \    ...                   operationalSpeed=${NITRO_ORIG_UPLINK_SPEED}

    Log     ${\n}Verify Aside and Bside uplinksets OK    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Uplinkset Status    ${LIs[1]}    ${NITRO_BSIDE_UPLINK_SET}    OK

    Log      ${\n}Verify Bside downlinks Linked OK    console=True
    :FOR    ${dl}    IN    @{NITRO_BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROB}    ${dl}    status=OK    portStatus=Linked


    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    Log      ${\n}Verify servers Profile status back to OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    OK

    Verify Happy Nitro Uplinks DA ports
    Verify Happy Nitro Servers DA Connections
    Verify Happy Nitro DA Nimble ports Attached Devices


OVF5298 Efuse Remove Aside Potash Affecting Aside connections, Verify servers Bside DA connections
    [Tags]  RemovePA    efuse    efusePA    Potash
    [Documentation]    Remove Aside Potash affecting servers connection through Aside uplinks
    ...                Expect uplinkset defined on Aside Critical status, and profiles connection error
    ...                server storage access on Bside should not be affected

    Log    ${\n}Remove Aside Potash and wait for Absent state    console=True
    Efuse IC and Wait    ${POTASHA}    EFuseOn

    Log     ${\n}Verify Bside Interconnect become Master, remains Configured    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${POTASHB}    state=Configured
    ...    stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify Aside uplinksets Critical    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Uplinkset Status    ${LIs[0]}    ${POTASH_ASIDE_UPLINK_SET}    Critical

    Log      ${\n}Verify Profile status Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    Critical

    Log     ${\n}Verify Bside Uplinks status and portStatus not impacted    console=True
    :FOR    ${uplink}    IN    @{US_POTASH_BSIDE_UPLINKS}
    \    Verify Port    ${POTASHB}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Bside uplinksets OK, not impacted    console=True
    Verify Uplinkset Status    ${LIs[0]}    ${POTASH_BSIDE_UPLINK_SET}    OK

    Run Keyword And Continue On Failure    Verify Happy Potash Servers Bside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Potash Bside DA Nimble ports Attached Devices


OVF5298 Efuse Insert Aside Potash Restoring Aside connections, Verify servers DA connections
    [Tags]  InsertPA    efuse    efusePA    Potash
    [Documentation]    Insert back Aside Potash affecting servers connection through Aside uplinks
    ...                Expect uplinkset defined on Aside back to OK, and profiles connection OK
    ...                servers connection path through Aside is restored

    Log    ${\n}Insert back Aside Potash and wait for Configured state    console=True
    Efuse IC and Wait    ${POTASHA}    EFuseOff

    Log     ${\n}Verify Aside Interconnect up as Subordinate    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect    ${POTASHA}    stackingDomainRole=${data_common.SUBORDINATE}

    Log     ${\n}Verify Bside Interconnect remains Configured    console=True
    Verify Named Interconnect    ${POTASHB}    state=Configured
    ...          stackingDomainRole=${data_common.MASTER}

    Wait For Happy Potash Aside DA Uplinks and UplinkSets

    Log     ${\n}Verify Aside downlinks Linked OK    console=True
    :FOR    ${dl}    IN    @{POTASH_ASIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${POTASHA}    ${dl}    status=OK    portStatus=Linked


    Log     ${\n}Verify Servers Profile status OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    OK

    Verify Happy Potash Uplinks DA ports
    Verify Happy Potash Servers DA Connections
    Verify Happy Potash DA Nimble ports Attached Devices


OVF5298 Efuse Remove Bside Potash Affecting Bside connections, Verify servers Aside DA connections
    [Tags]  RemovePB    efuse    efusePB    Potash
    [Documentation]    Remove Bside Potash affecting servers connection through Bside uplinks
    ...                Expect uplinkset defined on Bside Critical status, and profiles connection error
    ...                server storage access on Aside should not be affected

    Log    ${\n}Remove Bside Potash and wait for Absent state    console=True
    Efuse IC and Wait    ${POTASHB}    EFuseOn

    Log     ${\n}Verify Aside Interconnect become Master, remains Configured    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${POTASHA}    state=Configured
    ...    stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify Bside uplinksets Critical    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    \    ...    Verify Uplinkset Status    ${LIs[0]}    ${POTASH_BSIDE_UPLINK_SET}    Critical

    Log      ${\n}Verify Profile status Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    Critical

    Log     ${\n}Verify Aside Uplinks status and portStatus not impacted    console=True
    :FOR    ${uplink}    IN    @{US_POTASH_ASIDE_UPLINKS}
    \    Verify Port    ${POTASHA}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Bside uplinksets OK, not impacted    console=True
    Verify Uplinkset Status    ${LIs[0]}    ${POTASH_ASIDE_UPLINK_SET}    OK

    Run Keyword And Continue On Failure    Verify Happy Potash Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Potash Aside DA Nimble ports Attached Devices


OVF5298 Efuse Insert Bside Potash Restoring Bside connections, Verify servers DA connections
    [Tags]  InsertPB    efuse    efusePB    Potash
    [Documentation]    Insert back Bside Potash affecting servers connection through Bside uplinks
    ...                Expect uplinkset defined on Bside back to OK, and profiles connection OK
    ...                servers connection path through Bside is restored

    Log    ${\n}Insert back Bside Potash and wait for Configured state    console=True
    Efuse IC and Wait    ${POTASHB}    EFuseOff

    Log     ${\n}Verify Bside Interconnect up as Subordinate    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect    ${POTASHB}    stackingDomainRole=${data_common.SUBORDINATE}

    Log     ${\n}Verify Aside Interconnect remains Configured    console=True
    Verify Named Interconnect    ${POTASHA}    state=Configured
    ...          stackingDomainRole=${data_common.MASTER}

    Wait For Happy Potash Bside DA Uplinks and UplinkSets

    Log     ${\n}Verify Bside downlinks Linked OK    console=True
    :FOR    ${dl}    IN    @{POTASH_BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${POTASHB}    ${dl}    status=OK    portStatus=Linked

    Log     ${\n}Verify Servers Profile status OK    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    OK

    Verify Happy Potash Uplinks DA ports
    Verify Happy Potash Servers DA Connections
    Verify Happy Potash DA Nimble ports Attached Devices


OVF5298 Efuse Remove Aside Nitro Affecting Aside connections, Verify servers Bside DA connections
    [Tags]  RemoveNA    efuse    efuseNA    Nitro
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
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Uplinkset Status    ${LIs[1]}    ${NITRO_ASIDE_UPLINK_SET}    Critical

    Log      ${\n}Verify Profile status Critical    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    Critical

    Log     ${\n}Verify FA Bside Uplinks status and portStatus not impacted    console=True
    :FOR    ${uplink}    IN    @{US_NITRO_BSIDE_UPLINKS}
    \    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Bside uplinksets OK, not impacted    console=True
    Verify Uplinkset Status    ${LIs[1]}    ${NITRO_BSIDE_UPLINK_SET}    OK

    Run Keyword And Continue On Failure    Verify Happy Nitro Servers Bside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Nitro Bside DA Nimble ports Attached Devices


OVF5298 Efuse Insert Aside Nitro Restoring Aside connections, Verify servers DA connections
    [Tags]  InsertNA    efuse    efuseNA    Nitro
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

    Wait For Happy Nitro Aside DA Uplinks and UplinkSets

    Log     ${\n}Verify Aside downlinks Linked OK    console=True
    :FOR    ${dl}    IN    @{NITRO_ASIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked


    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    Log     ${\n}Verify Servers Profile status OK    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles status
    ...                                        ${server_profile_names}    OK

    Run Keyword And Continue On Failure    Verify Happy Nitro Aside Uplinks DA ports
    Verify Happy Nitro Servers DA Connections
    Verify Happy Nitro DA Nimble ports Attached Devices


OVF5298 Efuse Remove Bside Nitro Affecting Bside connections, Verify servers Aside DA connections
    [Tags]  RemoveNB    efuse    efuseNB    Nitro
    [Documentation]    Remove Bside Nitro affecting servers connection through Bside uplinks
    ...                Expect uplinkset defined on Bside Critical status, and profiles connection error
    ...                server storage access on Aside should not be affected

    Log    ${\n}Remove Bside Nitro and wait for Absent state    console=True
    Efuse IC and Wait    ${NITROB}    EFuseOn

    Log     ${\n}Verify Aside Interconnect become Master, remains Configured    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${NITROA}    state=Configured
    ...           stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify Bside uplinksets Critical    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...    Verify Uplinkset Status    ${LIs[1]}    ${NITRO_BSIDE_UPLINK_SET}    Critical

    Log      ${\n}Verify Profile status Critical    console=True
    Verify Server Profiles status    ${nitro_server_profile_names}    Critical

    Log     ${\n}Verify Aside Uplinks status and portStatus not impacted    console=True
    :FOR    ${uplink}    IN    @{US_NITRO_ASIDE_UPLINKS}
    \    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside downlinks Linked OK not impacted    console=True
    :FOR    ${dl}    IN    @{NITRO_ASIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked

    Log     ${\n}Verify Aside uplinksets OK, not impacted    console=True
    Verify Uplinkset Status    ${LIs[1]}    ${NITRO_ASIDE_UPLINK_SET}    OK

    Run Keyword And Continue On Failure    Verify Happy Nitro Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Nitro Aside DA Nimble ports Attached Devices


OVF5298 Efuse Insert Bside Nitro Restoring Bside connections, Verify servers DA connections
    [Tags]  InsertNB    efuse    efuseNB    Nitro
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

    Wait For Happy Nitro Bside DA Uplinks and UplinkSets

    Log     ${\n}Verify Bside downlinks Linked OK    console=True
    :FOR    ${dl}    IN    @{NITRO_BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROB}    ${dl}    status=OK    portStatus=Linked


    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    Log     ${\n}Verify Profile status OK    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles status
    ...                                        ${nitro_server_profile_names}    OK

    Run Keyword And Continue On Failure    Verify Happy Nitro Bside Uplinks DA ports
    Verify Happy Nitro Servers DA Connections
    Verify Happy Nitro DA Nimble ports Attached Devices


OVF5298 DA Reset Aside Potash, Verify servers connections restore after ICM up
    [Tags]    reset    resetPA    Potash
    [Documentation]    Reset Aside Potash affecting servers Aside connection
    ...                Expect Aside uplinkset back to OK and servers Aside connections restored
    ...                after ICM is back

    Log    ${\n}Reset Aside Potash and wait for it back to Configured state    console=True
    &{ic_name} =    Create Dictionary    name=${POTASHA}
    @{ic_list} =    Create List    ${ic_name}
    Hard Reset Interconnects from list    ${ic_list}

    Log     ${\n}Verify Bside Interconnect become Master, remains Configured    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${POTASHB}    state=Configured
    ...           stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify servers Bside DA connection not impacted    console=True
    Run Keyword And Continue On Failure    Verify Happy Potash Bside Uplinks DA ports
    Run Keyword And Continue On Failure    Verify Happy Potash Servers Bside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Potash Bside DA Nimble ports Attached Devices

    Log    ${\n}Wait for Aside ICM back to Configured as Subordinate   console=True
    Wait Until Keyword Succeeds    ${data_common.RESET_IC_WAIT}    30s
    ...    Verify Named Interconnect     ${POTASHA}    state=Configured
    ...           stackingDomainRole=${data_common.SUBORDINATE}

    # After reset ICM, profile will be Critical then when ICM is up, back to OK
    Log    ${\n}Reset will affect Aside uplinks and profile status    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    Critical

    Wait For Happy Potash Aside DA Uplinks and UplinkSets

    :FOR    ${dl}    IN    @{POTASH_ASIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${POTASHA}    ${dl}    status=OK    portStatus=Linked

    :FOR    ${sp}    IN    @{potash_server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Server Profile status    ${sp}    OK

    Log     ${\n}Verify Potash servers Aside DA connection restored    console=True
    Verify Happy Potash Uplinks DA ports
    Verify Happy Potash Servers DA Connections
    Verify Happy Potash DA Nimble ports Attached Devices


OVF5298 DA Reset Bside Potash, Verify servers connections restore after ICM up
    [Tags]    reset    resetPB    Potash
    [Documentation]    Reset Bside Potash affecting servers connection through US-DA2
    ...                Expect Bside uplinkset back to OK and servers Aside connections restored
    ...                after ICM is back
    ...                Verify servers downlink operationalSpeed

    Log    ${\n}Reset Bside Potash    console=True
    &{ic_name} =    Create Dictionary    name=${POTASHB}
    @{ic_list} =    Create List    ${ic_name}
    Hard Reset Interconnects from list    ${ic_list}

    Log     ${\n}Verify Aside Interconnect become Master, remains Configured    console=True
    Wait Until Keyword Succeeds    ${data_common.HA_SYNC_WAIT}    20s
    ...    Verify Named Interconnect     ${POTASHA}    state=Configured
    ...           stackingDomainRole=${data_common.MASTER}

    Log     ${\n}Verify servers Aside DA connection not impacted    console=True
    Verify Happy Potash Aside Uplinks DA ports
    Run Keyword And Continue On Failure    Verify Happy Potash Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Potash Aside DA Nimble ports Attached Devices

    Log    ${\n}Wait for Bside ICM back to Configured as Subordinate    console=True
    Wait Until Keyword Succeeds    ${data_common.RESET_IC_WAIT}    30s
    ...    Verify Named Interconnect     ${POTASHB}    state=Configured
    ...           stackingDomainRole=${data_common.SUBORDINATE}

    Log    ${\n}Reset will affect Bside uplinks and profile status    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${potash_server_profile_names}    Critical

    Wait For Happy Potash Bside DA Uplinks and UplinkSets

    :FOR    ${dl}    IN    @{POTASH_BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${POTASHB}    ${dl}    status=OK    portStatus=Linked

    :FOR    ${sp}    IN    @{potash_server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Server Profile status    ${sp}    OK

    Log     ${\n}Verify servers Bside DA connection restored    console=True
    Verify Happy Potash Uplinks DA ports
    Verify Happy Potash Servers DA Connections
    Verify Happy Potash DA Nimble ports Attached Devices


OVF5298 DA Reset Aside Nitro, Verify servers connections restore after ICM up
    [Tags]    reset    resetNA    Nitro
    [Documentation]    Reset Aside Nitro affecting servers connection through Aside uplinks
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
    Verify Happy Nitro Bside Uplinks DA ports
    Run Keyword And Continue On Failure    Verify Happy Nitro Servers Bside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Nitro Bside DA Nimble ports Attached Devices

    Log    ${\n}Wait for Aside ICM back to Configured as Subordinate    console=True
    Wait Until Keyword Succeeds    ${data_common.RESET_IC_WAIT}    30s
    ...    Verify Named Interconnect     ${NITROA}    state=Configured
    ...           stackingDomainRole=${data_common.SUBORDINATE}

    # After reset ICM, profile will be Critical then when ICM is up, back to OK
    Log    ${\n}Reset will affect Aside uplinks and profile status    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    Critical

    Wait For Happy Nitro Aside DA Uplinks and UplinkSets

    :FOR    ${dl}    IN    @{NITRO_ASIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROA}    ${dl}    status=OK    portStatus=Linked

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    :FOR    ${sp}    IN    @{nitro_server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Server Profile status    ${sp}    OK

    Log     ${\n}Verify servers Aside DA connection restored    console=True
    Verify Happy Nitro Uplinks DA ports
    Verify Happy Nitro Servers DA Connections
    Verify Happy Nitro DA Nimble ports Attached Devices


OVF5298 DA Reset Bside Nitro, Verify servers connections restore after ICM up
    [Tags]    reset    resetNB    Nitro
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
    Verify Happy Nitro Aside Uplinks DA ports
    Run Keyword And Continue On Failure    Verify Happy Nitro Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Nitro Aside DA Nimble ports Attached Devices

    Log    ${\n}Wait for Bside ICM back to Configured as Subordinate    console=True
    Wait Until Keyword Succeeds    ${data_common.RESET_IC_WAIT}    30s
    ...    Verify Named Interconnect     ${NITROB}    state=Configured
    ...           stackingDomainRole=${data_common.SUBORDINATE}

    Log    ${\n}Reset will affect Bside uplinks and profile status    console=True
    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    Critical

    Wait For Happy Nitro Bside DA Uplinks and UplinkSets

    :FOR    ${dl}    IN    @{NITRO_BSIDE_SERVER_DOWNLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Port    ${NITROB}    ${dl}    status=OK    portStatus=Linked

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Servers Downlink Speed

    :FOR    ${sp}    IN    @{nitro_server_profile_names}
    \    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    30s
    \    ...    Verify Server Profile status    ${sp}    OK

    Log     ${\n}Verify servers Bside DA connection restored    console=True
    Verify Happy Nitro Uplinks DA ports
    Verify Happy Nitro Servers DA Connections
    Verify Happy Nitro DA Nimble ports Attached Devices


OVF5298 Change DA uplink speed Case 1, Update LI Nitro Aside uplinkset uplink speed from 16Gb to 8Gb
    [Tags]  ULSpeedChangeN    SpeedChangeN     speedChange    Nitro
    [Documentation]    Change Aside DA uplinks speed
    ...                Verify
    ...                - speed change accordingly
    ...                - not affecting severs connections
    ...                - LI become Inconsistent

    Log    ${\n}Edit LI Nitro uplinkset Aside uplinks from 16Gb to 8Gb    console=True
    ${li_name} =     Set Variable    ${nitro_li_uplinksets_a['US_8Gb']['logicalInterconnectUri']}
    Perform Edit LI UplinkSet    ${nitro_li_uplinksets_a['US_8Gb']['name']}
    ...              ${nitro_li_uplinksets_a['US_8Gb']}    ${li_name}

    Verify Logical Interconnect    ${li_name}    status=Warning    consistencyStatus=NOT_CONSISTENT

    Log     ${\n}Verify uplink updated speed, not affecting servers connections    console=True
    :FOR    ${uplink}    IN    @{US_NITRO_ASIDE_UPLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_SPEED_WAIT}    20s
    \    ...    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked
    \    ...            operationalSpeed=${data_common.OPSPEED8}

    # In the past, in HA environment, changing Aside uplink spped affect Bside same uplink port speed
    Log     ${\n}Verify Bside uplink speed not affected.    console=True
    :FOR    ${uplink}    IN    @{US_NITRO_BSIDE_UPLINKS}
    \    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked
    \    ...            operationalSpeed=${NITRO_ORIG_UPLINK_SPEED}

    Log    ${\n}Verify server profiles status are not affected    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles Status
    ...                                        ${server_profile_names}    OK

    Verify Happy Nitro Servers DA Connections

    # Note: Nimble has outdated attached devices for OV uplink speed change scenario
    # can only verify the DA port that does not have speed Change on Nimble side

    # Verify Happy Nitro DA Nimble ports Attached Devices
    Run Keyword And Continue On Failure
    ...    Verify Happy Nitro Bside DA Nimble ports Attached Devices


OVF5298 Change uplink speed Case 2, LI UFG change Nitro uplink speed back, Servers connection verification
    [Tags]  LIUFGSpeedChangeN    SpeedChangeN    speedChange    Nitro

    Log    ${\n}Perform LI update from group to change uplink speed back    console=True
    ${li_name} =     Set Variable    ${nitro_li_uplinksets_a['US_8Gb']['logicalInterconnectUri']}
    Perform LI Update From Group    ${li_name}    ${data_common.UFG_WAIT}    30s

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    Log    ${\n}Verify server profiles status are not affected    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles Status
    ...                                        ${server_profile_names}    OK

    Verify Happy Nitro Servers DA Connections

    # Note: Nimble has outdated attached devices for OV uplink speed change scenario
    # can only verify the DA port that does not have speed Change on Nimble side

    # Verify Happy Nitro DA Nimble ports Attached Devices
    Run Keyword And Continue On Failure
    ...    Verify Happy Nitro Bside DA Nimble ports Attached Devices


OVF5298 Change DA uplink speed Case 3, Update LI Potash Bside uplinkset uplink speed from 8Gb to 4Gb
    [Tags]  ULSpeedChangeP   SpeedChangeP    speedChange    Potash
    [Documentation]    Change Potash Bside DA uplinks speed
    ...                Verify
    ...                - speed change accordingly
    ...                - not affecting severs connections
    ...                - LI become Inconsistent

    Log    ${\n}Edit LI Potash Bside uplinkset uplinks from 8Gb to 4Gb    console=True
    ${li_name} =     Set Variable    ${potash_li_uplinksets_b['US_4Gb']['logicalInterconnectUri']}
    Perform Edit LI UplinkSet    ${potash_li_uplinksets_b['US_4Gb']['name']}
    ...              ${potash_li_uplinksets_b['US_4Gb']}    ${li_name}

    Verify Logical Interconnect    ${li_name}    status=Warning    consistencyStatus=NOT_CONSISTENT

    Log     ${\n}Verify uplink updated speed, not affecting servers connections    console=True
    :FOR    ${uplink}    IN    @{US_POTASH_BSIDE_UPLINKS}
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_SPEED_WAIT}    20s
    \    ...    Verify Port    ${POTASHB}    ${uplink}    status=OK    portStatus=Linked
    \    ...            operationalSpeed=${data_common.OPSPEED4}

    # In the past, in HA environment, changing Aside uplink spped affect Bside same uplink port speed
    Log     ${\n}Verify Bside uplink speed not affected.    console=True
    :FOR    ${uplink}    IN    @{US_POTASH_ASIDE_UPLINKS}
    \    Verify Port    ${POTASHA}    ${uplink}    status=OK    portStatus=Linked
    \    ...            operationalSpeed=${POTASH_ORIG_UPLINK_SPEED}

    Log    ${\n}Verify server profiles status are not affected    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles Status
    ...    ${potash_server_profile_names}    OK

    Verify Happy Potash Servers DA Connections

    # Note: Nimble has outdated attached devices for OV uplink speed change scenario
    # can only verify the DA port that does not have speed Change on Nimble side

    # Verify Happy Potash DA Nimble ports Attached Devices
#    Run Keyword And Continue On Failure
#    ...    Verify Happy Potash Aside DA Nimble ports Attached Devices


OVF5298 Change uplink speed Case 4, LI UFG change Potash uplink speed back, Servers connection verification
    [Tags]  LIUFGSpeedChangeP    SpeedChangeP    speedChange    Potash

    Log    ${\n}Perform LI update from group to change uplink speed back    console=True
    ${li_name} =     Set Variable    ${potash_li_uplinksets_b['US_4Gb']['logicalInterconnectUri']}
    Perform LI Update From Group    ${li_name}    ${data_common.UFG_WAIT}    30s

    Run Keyword And Continue On Failure    Verify Happy LE and LI

    Log    ${\n}Verify server profiles status not affected    console=True
    Run Keyword And Continue On Failure    Verify Server Profiles Status
    ...    ${potash_server_profile_names}    OK

    Verify Happy Potash Servers DA Connections

    # Note: Nimble has outdated attached devices for OV uplink speed change scenario
    # can only verify the DA port that does not have speed Change on Nimble side


OVF5298 Change LI with Nitro DLS mode from 25Gb to 50Gb
    [Tags]    DLS    DLSto50    LIDLSto50    Nitro
    [Documentation]    Change LI downlinkSpeedMode from 25Gb to 50Gb

    Change LI downlinkSpeedMode to 50Gb


OVF5298 Change DLS mode from 50Gb to 25Gb
    [Tags]    DLS    DLSto25    LIDLSto25Allow    Nitro
    [Documentation]    Change LI downlinkSpeedMode from 50Gb to 25Gb

    PASS EXECUTION IF    '${downlink_mode}' == 'SPEED_25GB'    Skip Test already in 25Gb mode
    Change LI downlinkSpeedMode    ${LIs[1]}    SPEED_25GB


    Log    ${\n}wait for expected downgrade outage before checking end2end    console=True
    sleep    ${data_common.DLS_DOWNGRADE_OUTAGE_WAIT}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    OK

    # Expected BFS server down, add BOOT WAIT time
    Log    ${\n}Waiting ${data_common.BFS_SERVER_BOOT_WAIT} minutes for servers to boot and come up
    ...    console=True
    Sleep    ${data_common.BFS_SERVER_BOOT_WAIT}

    Verify Happy Nitro Servers DA Connections

    # Note: Nimble has outdated attached devices for OV LI downlinkSpeedMode change scenario
    # Verify Happy Nitro DA Nimble ports Attached Devices


#OVF5298 Change DLS mode from 25Gb back to 50Gb
#    [Tags]    DLS    DLSto50-2    Nitro
#
#    Change LI downlinkSpeedMode to 50Gb

OVF5298 Nimble Failover
    [Tags]    Failover    Potash    Nitro
    [Documentation]    Failover Nimble Array and verify servers storage paths each time
    ...                default iteration is 2, can specify different in cmmand line -v nfo:<#>

    # The uplinkport that used to be active will become Unlink during transition
    # causing LI becoming Warning. However, Nitro LI is Warning due to wiring
    # wait for Potash LI to become OK (from Warning), to avoid
    # verification prematurely
    # Server Profile should remain OK
    :FOR    ${index}    IN RANGE    0    ${nfo}
    \    Perform Nimble Failover
    \
    \    Wait Until Keyword Succeeds    ${data_common.UPLINK_STATUS_WAIT}    20s
    \    ...    Verify Logical Interconnect    ${LIs[0]}    status=OK
    \
    \    # extra wait for OV to sync the connection map
    \    Sleep    ${data_common.HA_SYNC_WAIT}
    \
    \    Run Keyword And Continue On Failure
    \    ...    Verify Server Profiles status    ${server_profile_names}    OK
    \
    \    Verify Happy Servers DA Connections
    \    # Note: Nimble has outdated attached devices for Nimble failover scenario
    \    # Verify Happy DA Nimble ports Attached Devices


OVF5298 Final DA Verification
    [Tags]    verifyDA    Potash    Nitro
    Verify Happy Uplinks DA ports
    :FOR    ${sp}    IN    @{server_profile_names}
    \    Run Keyword And Continue On Failure    Verify Server Profile status
    \    ...    ${sp}    OK
    Verify Servers Downlink Speed
    Verify ICM MaxBW
    Verify Happy Servers DA Connections
    # Verify Happy DA Nimble ports Attached Devices


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

    ${max_bw} =    Set Variable IF    '${downlink_mode}' == 'SPEED_25GB'    25000
    # ${max_bw} =    Set Variable IF    '${downlink_mode}' == 'SPEED_25GB'    50000
    ...                               '${downlink_mode}' == 'SPEED_50GB'    50000
    ...                               10000

    Add FC Networks from variable    ${fa_networks}
    Add FC Networks from variable    ${da_networks}

    ${fc_typical_bw} =    Set Variable    8000
    ${nitro_fc_typical_bw} =    Set Variable    16000

    :FOR    ${fa}    IN    @{fa_networks}
    \    Edit Network Bandwidth    ${fa['name']}    fc    ${fc_typical_bw}    ${max_bw}

    :FOR    ${da}    IN    @{da_networks_p}
    \    Edit Network Bandwidth    ${da['name']}    fc    ${fc_typical_bw}    ${max_bw}

    :FOR    ${da}    IN    @{da_networks_n}
    \    Edit Network Bandwidth    ${da['name']}    fc    ${nitro_fc_typical_bw}    ${max_bw}


Suite Min Teardown
    [Documentation]    Suite Post-condtion cleanup
    Pass Execution    Nothing to cleanup right now
    # fusion api logout appliance

##################################################################
# Verify servers DA connections through nameServers connectionMap
##################################################################
Verify Servers DA Connections
    [Documentation]    Verify servers DA connections through OneView ICM nameServers connection map
    [Arguments]    ${ic_name}    ${da_uplinks}    ${server_downlinks}    ${expected_conn_map}

    # Log to Console    ${\n}Verify servers DA connections through OneView IC nameServer connection map
    ${nameservers} =    Get IC NameServers    ${ic_name}

    # There is situation that there are extra staled downlink entries in nameServers, check that
    ${ns_entries} =     Get Length     ${nameservers}
    ${expecte_uplinks} =    Get Length   ${da_uplinks}
    ${expecte_downlinks} =    Get Length   ${server_downlinks}
    ${expected_entries} =    Evaluate    ${expecte_uplinks}+${expecte_downlinks}

    Run Keyword And Continue On Failure    Should Be Equal As Integers    ${ns_entries}    ${expected_entries}

    # In happy path, nameServers should not be Empty
    # Should Not Be Empty    ${nameservers}

    :FOR    ${dl}    IN    @{server_downlinks}
    \    Run Keyword And Continue On Failure    Verify Server DA Connection
    \    ...    ${nameservers}    ${dl}    ${expected_conn_map}


Verify Happy Potash Servers Aside DA Connections
    [Documentation]    Verify Potash servers Aside DA connections through nameServers connection map

    Log    ${\n}Verify Potash servers Aside DA connections through connection map
    ...    console=True

    Verify Servers DA Connections    ${POTASHA}    ${US_POTASH_ASIDE_UPLINKS}
    ...    ${POTASH_ASIDE_SERVER_DOWNLINKS}    ${POTASH_ASIDE_HAPPY_CONNECTION_MAP}


Verify Happy Potash Servers Bside DA Connections
    [Documentation]    Verify Potash servers Bside DA connections through nameServers connection map

    Log    ${\n}Verify Potash servers Bside DA connections through connection map
    ...    console=True

    Verify Servers DA Connections    ${POTASHB}    ${US_POTASH_BSIDE_UPLINKS}
    ...    ${POTASH_BSIDE_SERVER_DOWNLINKS}    ${POTASH_BSIDE_HAPPY_CONNECTION_MAP}


Verify Happy Nitro Servers Aside DA Connections
    [Documentation]    Verify Nitro servers Aside DA connections through nameServers connection map

    Log    ${\n}Verify Nitro servers Aside DA connections through connection map
    ...    console=True

    Verify Servers DA Connections    ${NITROA}    ${US_NITRO_ASIDE_UPLINKS}
    ...    ${NITRO_ASIDE_SERVER_DOWNLINKS}    ${NITRO_ASIDE_HAPPY_CONNECTION_MAP}


Verify Happy Nitro Servers Bside DA Connections
    [Documentation]    Verify Nitro servers Bside DA connections through nameServers connection map

    Log    ${\n}Verify Nitro servers Bside DA connections through connection map
    ...    console=True

    Verify Servers DA Connections    ${NITROB}    ${US_NITRO_BSIDE_UPLINKS}
    ...    ${NITRO_BSIDE_SERVER_DOWNLINKS}    ${NITRO_BSIDE_HAPPY_CONNECTION_MAP}


Verify Happy Potash Servers DA Connections
    [Documentation]    Verify servers both Aside and Bside DA connections through nameServers connection map

    # Log to Console    ${\n}Verify servers both Aside and Bside DA connections through connection map

    Run Keyword And Continue On Failure    Verify Happy Potash Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Potash Servers Bside DA Connections


Verify Happy Nitro Servers DA Connections
    [Documentation]    Verify servers both Aside and Bside DA connections through nameServers connection map

    # Log to Console    ${\n}Verify servers both Aside and Bside DA connections through connection map

    Run Keyword And Continue On Failure    Verify Happy Nitro Servers Aside DA Connections
    Run Keyword And Continue On Failure    Verify Happy Nitro Servers Bside DA Connections

############
# Main one
############
Verify Happy Servers DA Connections
    [Documentation]    Verify servers both Aside and Bside DA connections through nameServers connection map

    # Log to Console    ${\n}Verify servers both Aside and Bside DA connections through connection map
    Run Keyword And Continue On Failure    Verify Happy Potash Servers DA Connections
    Run Keyword And Continue On Failure    Verify Happy Nitro Servers DA Connections

##################################################################
# Verify DA uplinks connected to storage port through nameServers
##################################################################
Verify Uplinks DA ports through nameServers
    [Documentation]    Verify DA uplinks connected to Nimble port through
    ...                nameServers uplinkport info
    [Arguments]    ${ic_name}    ${da_uplinks}

    # Log    ${\n}Verify DA uplinks connected to Nimble port    console=True

    ${nameServers} =    Get IC NameServers    ${ic_name}
    Should Not Be Empty    ${nameServers}

    :FOR    ${uplink_da}    IN    @{da_uplinks}
    \    Verify Uplink DA Port    ${nameServers}    ${uplink_da}

Verify Happy Nitro Aside Uplinks DA ports
    [Documentation]    Verify Nitro Aside DA uplinks connected to Nimble port through nameServers

    Log    ${\n}Verify Nitro Aside DA uplinks connected to Nimble port    console=True
    Verify Uplinks DA ports through nameServers    ${NITROA}    ${NITRO_A_UPLINKS_DA}

Verify Happy Nitro Bside Uplinks DA ports
    [Documentation]    Verify Nitro Bside DA uplinks connected to Nimble port through nameServers

    Log    ${\n}Verify Nitro Bside DA uplinks connected to Nimble port    console=True
    Verify Uplinks DA ports through nameServers    ${NITROB}    ${NITRO_B_UPLINKS_DA}


Verify Happy Potash Aside Uplinks DA ports
    [Documentation]    Verify Potash Aside DA uplinks connected to Nimble port through nameServers

    Log    ${\n}Verify Potash Aside DA uplinks connected to Nimble port    console=True
    Verify Uplinks DA ports through nameServers    ${POTASHA}    ${POTASH_A_UPLINKS_DA}

Verify Happy Potash Bside Uplinks DA ports
    [Documentation]    Verify Potash Bside DA uplinks connected to Nimble port through nameServers

    Log    ${\n}Verify Potash Bside DA uplinkports connected to Nimble port    console=True
    Verify Uplinks DA ports through nameServers    ${POTASHB}    ${POTASH_B_UPLINKS_DA}

Verify Happy Potash Uplinks DA ports
    [Documentation]    Verify Potash DA uplinks connected to Nimble port through nameServers uplinkport info

    # Log    ${\n}Verify Potash DA uplinkports connected to Nimble port    console=True
    Verify Happy Potash Aside Uplinks DA ports
    Verify Happy Potash Bside Uplinks DA ports

Verify Happy Nitro Uplinks DA ports
    [Documentation]    Verify Nitro DA uplinks connected to Nimble port through nameServers uplinkport info

    # Log    ${\n}Verify Nitro DA uplinkports connected to Nimble port    console=True
    Verify Happy Nitro Aside Uplinks DA ports
    Verify Happy Nitro Bside Uplinks DA ports

############
# Main one
############
Verify Happy Uplinks DA ports
    [Documentation]    Verify all DA uplinkports connected to its Nimble port through nameServers uplinkport info

    Log    ${\n}Verify all Aside and Bside DA uplinkports connected to Nimble port    console=True

    Run Keyword And Continue On Failure    Verify Happy Potash Uplinks DA ports
    Run Keyword And Continue On Failure    Verify Happy Nitro Uplinks DA ports


Wait For Happy Potash Aside DA Uplinks and UplinkSets
    [Documentation]    Wait for Potash Aside DA uplinks status OK with expected speed and US OK

    # Log     ${\n}Wait for Potash Aside and Bside DA Uplinks status and speed    console=True
    :FOR    ${uplink}    IN    @{US_POTASH_ASIDE_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    10s
    \    ...    Verify Port    ${POTASHA}    ${uplink}    status=OK    portStatus=Linked
    \    ...                   operationalSpeed=${POTASH_ORIG_UPLINK_SPEED}

    Log     ${\n}Wait for Aside uplinksets OK    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...   Verify Uplinkset Status    ${LIs[0]}    ${POTASH_ASIDE_UPLINK_SET}    OK

Wait For Happy Potash Bside DA Uplinks and UplinkSets
    [Documentation]    Wait for Potash Bside DA uplinks status OK with expected speed and US OK

    # Log     ${\n}Wait for Potash Bside DA Uplinks status and speed    console=True
    :FOR    ${uplink}    IN    @{US_POTASH_BSIDE_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    10s
    \    ...    Verify Port    ${POTASHB}    ${uplink}    status=OK    portStatus=Linked
    \    ...                   operationalSpeed=${POTASH_ORIG_UPLINK_SPEED}

    Log     ${\n}Wait for Bside uplinksets OK    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...   Verify Uplinkset Status    ${LIs[0]}    ${POTASH_BSIDE_UPLINK_SET}    OK

Wait For Happy Nitro Aside DA Uplinks and UplinkSets
    [Documentation]    Wait for all Nitro DA uplinks status OK with expected speed and US OK

    # Log     ${\n}Wait for Nitro Aside DA Uplinks status and speed    console=True
    :FOR    ${uplink}    IN    @{US_NITRO_ASIDE_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    10s
    \    ...    Verify Port    ${NITROA}    ${uplink}    status=OK    portStatus=Linked
    \    ...                   operationalSpeed=${NITRO_ORIG_UPLINK_SPEED}

    Log    ${\n}Verify Aside uplinksets OK    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...   Verify Uplinkset Status    ${LIs[1]}    ${NITRO_ASIDE_UPLINK_SET}    OK

Wait For Happy Nitro Bside DA Uplinks and UplinkSets
    [Documentation]    Wait for all Nitro DA uplinks status OK with expected speed and US OK

    # Log     ${\n}Wait for Nitro Aside and Bside DA Uplinks status and speed    console=True
    :FOR    ${uplink}    IN    @{US_NITRO_BSIDE_UPLINKS}
    \    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    10s
    \    ...    Verify Port    ${NITROB}    ${uplink}    status=OK    portStatus=Linked
    \    ...                   operationalSpeed=${NITRO_ORIG_UPLINK_SPEED}

    Log    ${\n}Verify Bside uplinksets OK    console=True
    Wait Until Keyword Succeeds   ${data_common.UPLINK_STATUS_WAIT}    30s
    ...   Verify Uplinkset Status    ${LIs[1]}    ${NITRO_BSIDE_UPLINK_SET}    OK


Wait For Happy Potash DA Uplinks and UplinkSets
    [Documentation]    Wait for all Potash DA uplinks status OK with expected speed and US OK

    Log    ${\n}Wait for Potash Aside and Bside DA Uplinks status and speed    console=True
    Wait For Happy Potash Aside DA Uplinks and UplinkSets
    Wait For Happy Potash Bside DA Uplinks and UplinkSets


Wait For Happy Nitro DA Uplinks and UplinkSets
    [Documentation]    Wait for all Nitro DA uplinks status OK with expected speed and US OK

    Log    ${\n}Wait for Nitro Aside and Bside DA Uplinks status and speed    console=True
    Wait For Happy Nitro Aside DA Uplinks and UplinkSets
    Wait For Happy Nitro Bside DA Uplinks and UplinkSets


############
# Main one
############
Wait For Happy DA Uplinks and UplinkSets
    [Documentation]    Wait for all DA uplinks status OK with specified speed

    # Log     ${\n}Wait for all Uplinks and uplinksets are OK    console=True

    Wait For Happy Nitro DA Uplinks and UplinkSets
    Wait For Happy Potash DA Uplinks and UplinkSets


Verify Happy LE
    [Documentation]    Verify the common scenario LE happy condition
    ...                ICM in Congured state,
    ...                Wait for DA uplinks and uplinksets reach OK status
    ...                LE Consistent and OK

    Log     ${\n}Verify All ICMs in Configured state        console=True
    :FOR    ${ic}    IN    @{ICMS}
    \    Verify Named Interconnect    ${ic}    state=Configured

    Wait For Happy DA Uplinks and UplinkSets

    Log     ${\n}Verify LE status OK and Consistent    console=True
    Verify Named Logical Enclosure    ${LE}    status=OK    state=Consistent


Verify Happy LE and LI
    [Documentation]    Verify the common scenario LE and LI condition,
    ...                Expected Nitro maxBandwidth,
    ...                and servers downlinks expected operationalSpeed
    ...                The LI status may be Warning or OK depending on DLS mode and CXP cabling

    Run Keyword And Continue On Failure    Verify Happy LE
    Verify LI with SpeedMode    ${LIs[1]}
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
    ...                   Quagmire2 servers downlink operationalSpeed is 25 and 50 respectively

    Log     ${\n}Verify servers expected downlink operationalSpeed    console=True

    ${exp_speed} =    Set Variable IF    '${downlink_mode}' == 'SPEED_25GB'    Speed25G
    ...               Speed50G

    :FOR    ${dl}    IN    @{NITRO_ASIDE_SERVER_DOWNLINKS}
    \    Run Keyword And Continue On Failure    Verify Port    ${NITROA}
    \    ...         ${dl}    portStatus=Linked    operationalSpeed=${exp_speed}

    :FOR    ${dl}    IN    @{NITRO_BSIDE_SERVER_DOWNLINKS}
    \    Run Keyword And Continue On Failure    Verify Port    ${NITROB}
    \    ...         ${dl}    portStatus=Linked    operationalSpeed=${exp_speed}


Verify LI with SpeedMode
    [Documentation]    Verify the LI status, consistencyStatus and downlinkSpeedMode
    ...                Applicable for LI with Nitro ICMs only
    ...                In API environment, there are 2 CXP cables between Nitro/Methane L1, L2
    ...                working for both LI downlinkSpeedMode 25Gb and 50Gb
    ...                However, with this cabling, there will be Warning alert if running in 25Gb
    ...                downlinkMode. Therefore expect Warning state if 2 CXP in L1 and L2
    ...                and OK state if 1 CXP between Nitro/Methane L1
    ...                Need to allow both OK and Warning state for LI depending on the speedMode
    ...                and Cabling.
    [Arguments]    ${li_name}

    Log     ${\n}Verify LI status, ConsistencyStatus and downlinkSpeedMode    console=True

    ${exp_status} =    Set Variable IF    '${downlink_mode}' == 'SPEED_25GB'    ((?i)Warning|OK)
    ...                OK

    Verify Logical Interconnect    ${li_name}    status=${exp_status}
    ...    consistencyStatus=CONSISTENT    downlinkSpeedMode=${downlink_mode}


##########################################################################
# Verify servers DA connections through Nimble port connected initiators
##########################################################################
Get Nimble Port FC Info
    [Documentation]    Compose and issue Nimble fc info command for provided port and ctrlr
    ...                return command output file
    ...                'fc --info <port_name> --ctrlr <ctrlName>'
    [Arguments]    ${port_name}    ${ctrl_name}

    ${outfile} =    Catenate    SEPARATOR=    ${data_common.DA_ATTACHED_DEV_OUTFILE_PREFIX}
    ...    ${port_name}    _    ${ctrl_name}    ${data_common.DA_ATTACHED_DEV_OUTFILE_SUFFIX}
    ${cmd} =    Catenate    ${data_common.NIMBLE_FC_CMD}    ${port_name}
    ...    --ctrlr    ${ctrl_name}
    SSH to Source and save command output    ${nimble_info['ip']}    ${nimble_info['user']}
    \    ...    ${nimble_info['pwd']}    ${nimble_info['prompt']}
    \    ...    ${cmd}    ${outfile}
    [Return]    ${outfile}


Verify DA Nimble ports Attached Devices
    [Documentation]    Verify speicified Nimble ports attached devices count
    ...                from 'fc --info <nimble_port_name> --ctrlr <ctrlName>' output
    [Arguments]    ${nimble_ports}    ${initiator_alias_pattern}    ${expected_count}

    # Log     ${\n}Verify DA uplink connected Nimble port attached devices    console=True

    ${len} =    Get Length    ${nimble_ports}
    # get nimble fc port info connected initiators output and verify
    # /tmp/da_ns_attdev_<portname>_A.txt and /tmp/da_ns_attdev_<portname>_B.txt
    :FOR    ${index}    IN RANGE    0    ${len}
    \    ${outfileA} =   Get Nimble Port FC Info    ${nimble_ports[${index}]}    A
    \    Verify Nimble DA AttachedDev    ${outfileA}    ${initiator_alias_pattern}
    \    ...    ${expected_count}
    \    ${outfileB} =   Get Nimble Port FC Info    ${nimble_ports[${index}]}    B
    \    Verify Nimble DA AttachedDev    ${outfileB}    ${initiator_alias_pattern}
    \    ...    ${expected_count}


Verify Happy Potash Aside DA Nimble ports Attached Devices
    [Documentation]    Verify Potash Aside DA uplink attached devices through Nimble port

    # Log    ${\n}SKIP Verify Happy Potash Aside DA Nimble ports Attached Devices    console=True
    Log     ${\n}Verify Potash Aside DA uplink connected Nimble port attached devices    console=True
    ${expected_ad} =    Get Length   ${POTASH_ASIDE_SERVER_DOWNLINKS}
    Verify DA Nimble ports Attached Devices    ${da_potashA_Nimble_ports}
    ...    ${potashA_initiator_alias_pattern}    ${expected_ad}

Verify Happy Potash Bside DA Nimble ports Attached Devices
    [Documentation]    Verify Potash Bside DA uplink attached devices through Nimble port

    # Log    ${\n}SKIP Verify Happy Potash Bside DA Nimble ports Attached Devices    console=True
    Log     ${\n}Verify Potash Bside DA uplink connected Nimble port attached devices    console=True
    ${expected_ad} =    Get Length   ${POTASH_BSIDE_SERVER_DOWNLINKS}
    Verify DA Nimble ports Attached Devices    ${da_potashB_Nimble_ports}
    ...    ${potashB_initiator_alias_pattern}    ${expected_ad}

Verify Happy Nitro Aside DA Nimble ports Attached Devices
    [Documentation]    Verify Nitro Aside DA uplink attached devices through Nimble port

    # Log    ${\n}SKIP Verify Happy Nitro Aside DA Nimble ports Attached Devices    console=True
    Log     ${\n}Verify Nitro Aside DA uplink connected Nimble port attached devices    console=True
    ${expected_ad} =    Get Length   ${NITRO_ASIDE_SERVER_DOWNLINKS}
    Verify DA Nimble ports Attached Devices    ${da_nitroA_Nimble_ports}
    ...    ${nitroA_initiator_alias_pattern}    ${expected_ad}

Verify Happy Nitro Bside DA Nimble ports Attached Devices
    [Documentation]    Verify Nitro Bside DA uplink attached devices through Nimble DA port

    # Log    ${\n}SKIP Verify Happy Nitro Bside DA Nimble ports Attached Devices    console=True
    Log     ${\n}Verify Nitro Bside DA uplink connected Nimble port attached devices    console=True
    ${expected_ad} =    Get Length   ${NITRO_BSIDE_SERVER_DOWNLINKS}
    Verify DA Nimble ports Attached Devices    ${da_nitroB_Nimble_ports}
    ...    ${nitroB_initiator_alias_pattern}    ${expected_ad}

Verify Happy Potash DA Nimble ports Attached Devices
    [Documentation]    Verify Potash Both Side DA uplink attached devices through Nimble DA port

    # Log    ${\n}SKIP Verify Happy Potash DA Nimble ports Attached Devices    console=True
    Run Keyword And Continue On Failure    Verify Happy Potash Aside DA Nimble ports Attached Devices
    Run Keyword And Continue On Failure    Verify Happy Potash Bside DA Nimble ports Attached Devices

Verify Happy Nitro DA Nimble ports Attached Devices
    [Documentation]    Verify Nitro Both Side DA uplink attached devices through Nimble DA port

    # Log    ${\n}SKIP Verify Happy Nitro DA Nimble ports Attached Devices    console=True
    Run Keyword And Continue On Failure    Verify Happy Nitro Aside DA Nimble ports Attached Devices
    Run Keyword And Continue On Failure    Verify Happy Nitro Bside DA Nimble ports Attached Devices

############
# Main one
############
Verify Happy DA Nimble ports Attached Devices
    [Documentation]    Verify Potash and Nitro both sides DA uplink attached devices through Nimble

    # Log    ${\n}SKIP Verify Happy DA Nimble ports Attached Devices    console=True
    Run Keyword And Continue On Failure    Verify Happy Potash DA Nimble ports Attached Devices
    Run Keyword And Continue On Failure    Verify Happy Nitro DA Nimble ports Attached Devices


Change LI downlinkSpeedMode
    [Documentation]    Chage LI DownlinkSpeed mode to 50Gb and perform end2end verification
    [Arguments]    ${li_name}    ${dls_mode}

    PASS EXECUTION IF    '${downlink_mode}' == '${dls_mode}'    Skip already in the speed mode

    Update LI DownlinkSpeedMode    ${li_name}    ${dls_mode}
    ...                            ${data_common.LI_DLS_CHANGE_WAIT}    20s

    Set Suite Variable    ${downlink_mode}    ${dls_mode}

    ${exp_bw} =    Set Variable IF    '${downlink_mode}' == 'SPEED_25GB'    SPEED_25G
    ...               SPEED_50G

    Log    ${\n}wait till Nitro maxBandwidth reach ${exp_bw}    console=True
    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Named Interconnect     ${NITROA}    maxBandwidth=${exp_bw}

    Wait Until Keyword Succeeds    ${data_common.DLS_LANE_CHANGE_WAIT}    10s
    ...    Verify Named Interconnect     ${NITROB}    maxBandwidth=${exp_bw}

    Run Keyword And Continue On Failure    Verify LI with SpeedMode    ${li_name}

    Wait Until Keyword Succeeds    ${data_common.SERVERS_INIT_DLS_WAIT}    10s
    ...    Verify Servers Downlink Speed


Change LI downlinkSpeedMode to 50Gb
    [Documentation]    Chage LI DownlinkSpeed mode to 50Gb and perform end2end verification

    PASS EXECUTION IF    '${downlink_mode}' == 'SPEED_50GB'    Skip Test already in 50Gb mode

    Change LI downlinkSpeedMode    ${LIs[1]}    SPEED_50GB

    Log    ${\n}wait for expected upgrade outage before checking end2end    console=True
    sleep    ${data_common.DLS_UPGRADE_OUTAGE_WAIT}

    Wait Until Keyword Succeeds    ${data_common.SUBPORT_STATUS_WAIT}    20s
    ...    Verify Server Profiles status    ${nitro_server_profile_names}    OK

    # Expected BFS server down, add BOOT WAIT time
    Log    ${\n}Waiting ${data_common.BFS_SERVER_BOOT_WAIT} minutes for servers to boot and come up
    ...    console=True

    Sleep    ${data_common.BFS_SERVER_BOOT_WAIT}

    Verify Happy Nitro Servers DA Connections

    # Note: Nimble has outdated attached devices for OV LI downlinkSpeedMode change scenario
    # Verify Happy Nitro DA Nimble ports Attached Devices


Perform Nimble Failover
    [Documentation]    Issue Nimble failover command
    ...                failover --force --non_interactive

    Log    ${\n}Issue Nimble failover command    console=True

    ${rc} =    SSH to Source and execute command    ${nimble_info['ip']}
    \    ...    ${nimble_info['user']}    ${nimble_info['pwd']}    ${nimble_info['prompt']}
    \    ...    ${data_common.NIMBLE_FAILOVER_CMD}

    Log    ${\n}wait for Nimble failover to complete    console=True
    sleep    ${data_common.NIMBLE_FAILOVER_WAIT_TIME}
