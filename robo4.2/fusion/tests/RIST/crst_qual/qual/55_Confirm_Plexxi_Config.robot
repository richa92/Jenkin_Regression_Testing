*** Settings ***
Documentation         Confirm Plexxi configured by OneView

Resource              ../resource.txt

Variables             ../Common.py
Variables             ../${DATA_FILE}

Suite Setup           QUAL Suite Setup    ${admin_credentials}
Suite Teardown        QUAL Suite Teardown

*** Test Cases ***
Plexxi Login
    [Documentation]    Ensure Logged Into Plexxi for the following [TAG] Test Cases
    [Tags]  TEST    55    CONFIRM_PLEXXI_Ports_ONE    CONFIRM_PLEXXI_LAG_ONE    CONFIRM_PLEXXI_LAG_EDIT
    Plexxi Login

Confirm Plexxi Ports With SP Applied
    [Documentation]  Confirm Plexxi Ports configured by OneView
    [Tags]  TEST    55    CONFIRM_PLEXXI_Ports_ONE
    [Teardown]    Run Keyword If    ${PAUSE_IF_PLEXXI_CONFIRM_FAILS}==${True}
    ...    Run Keyword If    '${TEST STATUS}'=='FAIL'    Pause Execution    Confirm Plexxi Done?

    ${confirm} =    Copy Dictionary    ${CONFIRM_PLEXXI_PORTS_ONE}  # uses deep copy so we won't trash original

    # Need to rotate ${confirm} as the connections were rotated
    # When profiles were created, the validated indexes were [0] - [7].  4 servers, 2 connections each.
    # The connections were then shifted left by 2 with the first 2 wrapping around to[0] -> [6] and [1] -> [7]
    # I hope that makes sense.
    ${zero} =    Remove From List    ${confirm["result"]}    0
    ${one} =     Remove From List    ${confirm["result"]}    0   # [0] was previously [1]
    Insert Into List    ${confirm["result"]}    6    ${one}    # will be the new [7]
    Insert Into List    ${confirm["result"]}    6    ${zero}   # will be the new [6]

    # now update "port_label" values
    Set To Dictionary    ${confirm["result"][0]}    port_label    1
    Set To Dictionary    ${confirm["result"][1]}    port_label    1
    Set To Dictionary    ${confirm["result"][2]}    port_label    2
    Set To Dictionary    ${confirm["result"][3]}    port_label    2
    Set To Dictionary    ${confirm["result"][4]}    port_label    3
    Set To Dictionary    ${confirm["result"][5]}    port_label    3
    Set To Dictionary    ${confirm["result"][6]}    port_label    4
    Set To Dictionary    ${confirm["result"][7]}    port_label    4

    ${sort_keys} =    Create List    port_label    switch_name
    ${expected} =    Sort Helper    ${confirm}    result    ${sort_keys}
    LOG    ${expected}
    Wait Until Keyword Succeeds   3x    30sec    Confirm Plexxi Access Ports    ${confirm}

Confirm Plexxi LAG with SP Applied
    [Documentation]    Confirms Plexxi LAG configured by OneView
    [Tags]    TEST    CONFIRM_PLEXXI_LAG_EDIT
    ${vlan_ports} =    Get Plexxi VLAN Ports For LAG Test
    ${lag_ports} =    Get Plexxi LAG Ports For LAG Test

    # Get the profile with expected lags
    @{expected} =    Create List
    ${profiles} =    Get Dictionary Keys    ${EXPECTED_LAGS_EDIT}
    :FOR    ${name}    IN    @{profiles}
    \    ${sp} =    Get Resource    SP:${name}
    \    ${uuid} =    Fetch From Right    ${sp['uri']}    /
    \    Set To Dictionary    ${EXPECTED_LAGS_EDIT['${name}']}    name    OV-${uuid}-LAG1
    \    Log    Update expected ${name} to: OV-${uuid}-LAG1    console=${CONSOLE}
    \    Append To List    ${expected}    ${EXPECTED_LAGS_EDIT['${name}']}

    Log    ${vlan_ports}
    Log    ${lag_ports}
    Log    ${expected}

    # Confirm LAG Vlans, native_vlan and a few other things
    # Convert to Dict as needed by Fusion Api Validate Response Follow
    ${dict_lag_ports} =    Create Dictionary    lags    ${lag_ports}
    ${dict_expected} =    Create Dictionary    lags    ${expected}
    ${status} =    Fusion Api Validate Response Follow    ${dict_expected}    ${dict_lag_ports}    wordy=True
    Should Be True    ${status}

    # Now confirm the correct ports
    &{port_to_vlans} =    Create Dictionary
    :FOR    ${lp}    IN    @{lag_ports}
    \    Log    Get Port for vlans: ${lp['vlans']}    console=${CONSOLE}
    \    ${expected_port} =    Set Variable If    '${WIN_NS_RANGE}' == '${lp['vlans']}'    ${WIN_NS_PORT_EDIT}    ${LINUX_NS_PORT_EDIT}
    \    Log    ${lp['vlans']} Expected to be connected to ${expected_port} as ${lp['vlans']}   console=${CONSOLE}
    \    Set To Dictionary    ${port_to_vlans}    ${expected_port}    ${lp['vlans']}
    \    @{port_ids} =    Create List
    \    Append To List    ${port_ids}    ${lp['port_properties'][0]['port_uuids'][0]}    ${lp['port_properties'][1]['port_uuids'][0]}
    \    Set To Dictionary    ${port_to_vlans}    ${lp['vlans']}    ${port_ids}

    Log    port_to_vlans: ${port_to_vlans}
    Confirm Vlans To Ports    ${vlan_ports}    ${port_to_vlans}
