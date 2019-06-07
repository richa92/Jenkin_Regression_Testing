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
    [Tags]  TEST    45    CONFIRM_PLEXXI_Ports_ONE    CONFIRM_PLEXXI_LAG_ONE
    Plexxi Login

Confirm Plexxi Ports With SP Applied
    [Documentation]  Confirm Plexxi Ports configured by OneView
    [Tags]  TEST    45    CONFIRM_PLEXXI_Ports_ONE
    [Teardown]    Run Keyword If    ${PAUSE_IF_PLEXXI_CONFIRM_FAILS}==${True}
    ...    Run Keyword If    '${TEST STATUS}'=='FAIL'    Pause Execution    Confirm Plexxi Done?

    Wait Until Keyword Succeeds   3x    30sec    Confirm Plexxi Access Ports    ${CONFIRM_PLEXXI_PORTS_ONE}

Confirm Plexxi LAG with SP Applied
    [Documentation]    Confirms Plexxi LAG configured by OneView
    [Tags]    TEST    CONFIRM_PLEXXI_LAG_ONE
    ${vlan_ports} =    Get Plexxi VLAN Ports For LAG Test
    ${lag_ports} =    Get Plexxi LAG Ports For LAG Test

    # Get the profile with expected lags
    @{expected} =    Create List
    ${profiles} =    Get Dictionary Keys    ${EXPECTED_LAGS}
    :FOR    ${name}    IN    @{profiles}
    \    ${sp} =    Get Resource    SP:${name}
    \    ${uuid} =    Fetch From Right    ${sp['uri']}    /
    \    Set To Dictionary    ${EXPECTED_LAGS['${name}']}    name    OV-${uuid}-LAG1
    \    Log    Update expected ${name} to: OV-${uuid}-LAG1    console=${CONSOLE}
    \    Append To List    ${expected}    ${EXPECTED_LAGS['${name}']}

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
    \    ${expected_port} =    Set Variable If    '${WIN_NS_RANGE}' == '${lp['vlans']}'    ${WIN_NS_PORT}    ${LINUX_NS_PORT}
    \    Log    ${lp['vlans']} Expected to be connected to ${expected_port} as ${lp['vlans']}   console=${CONSOLE}
    \    Set To Dictionary    ${port_to_vlans}    ${expected_port}    ${lp['vlans']}
    \    @{port_ids} =    Create List
    \    Append To List    ${port_ids}    ${lp['port_properties'][0]['port_uuids'][0]}    ${lp['port_properties'][1]['port_uuids'][0]}
    \    Set To Dictionary    ${port_to_vlans}    ${lp['vlans']}    ${port_ids}

    Log    port_to_vlans: ${port_to_vlans}
    Confirm Vlans To Ports    ${vlan_ports}    ${port_to_vlans}
