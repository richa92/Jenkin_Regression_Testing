*** Settings ***
Documentation           snmpv3 trap and trap forwarding testing

Library                FusionLibrary
Library                RoboGalaxyLibrary
Library                OperatingSystem
Library                BuiltIn
Library                Collections
Library                XML
Library                String
Library                json
Library                Process
Suite setup            Setup Sender and Receier OV for trap testing


Resource                ../../Resources/api/fusion_api_resource.txt
Variables                data_variables_trap_validation.py


*** Test Cases ***

SNMPV3 trap forwarding setup for OV1
    Fusion Api Login Appliance    ${sender_appliance_ip}    ${admin_credentials_sender_ov}
    ${resp} =  fusion api get appliance snmpv3 Trap Forwarding Users
    Log    snmpv3_trap_users=${resp}    console=True
    ${resp} =  fusion api add appliance snmpv3 trap forwarding user  body=${trap_forwarding_user}
    Run keyword if    '${resp['status_code']}'!='200'    FAIL    Adding trap forwarding user failed
    ${resp} =  fusion api get appliance snmpv3 Trap Forwarding Users    param=?filter=userName==${trap_forwarding_user['userName']}
    Log    snmpv3_trap_users=${resp}    console=True
    ${trap_forwarding_user_uri} =  set variable  ${resp['members'][0]['uri']}
    ${trap_forwarding_user_id} =  set variable  ${resp['members'][0]['id']}
    set suite variable  ${trap_forwarding_user_uri}
    set suite variable  ${trap_forwarding_user_id}
    set to dictionary  ${trap_destination}  userId  ${trap_forwarding_user_id}
    set to dictionary  ${trap_destination}  userUri  ${trap_forwarding_user_uri}
    ${resp}=    fusion_api_get_appliance_snmpv3_trap_destinations
    Log    snmpv3_trap_destinations=${resp}    console=True
    ${resp}=    fusion_api_add_appliance_snmpv3_trap_destination    ${trap_destination}
    ${resp}=    fusion_api_get_appliance_snmpv3_trap_destinations
    Log    snmpv3_trap_destinations=${resp}    console=True
    Fusion Api Logout Appliance

SNMPV3 trap forwarding setup for OV2
    Fusion Api Login Appliance    ${receiver_appliance_ip}    ${admin_credentials_receiver_ov}
    ${resp} =  fusion api get appliance snmpv3 Trap Forwarding Users
    Log    snmpv3_trap_users=${resp}    console=True
    ${resp} =  fusion api add appliance snmpv3 trap forwarding user  body=${trap_destination_user}
    Run keyword if    '${resp['status_code']}'!='200'    FAIL    Adding trap destination user failed
    ${resp} =  fusion api get appliance snmpv3 Trap Forwarding Users    param=?filter=userName==${trap_destination_user['userName']}
    ${trap_receiving_user_uri} =  set variable  ${resp['members'][0]['uri']}
    ${trap_receiving_user_id} =  set variable  ${resp['members'][0]['id']}
    set suite variable  ${trap_receiving_user_uri}
    set suite variable  ${trap_receiving_user_id}
    set to dictionary  ${trap_forwadring_destination}  userId  ${trap_receiving_user_id}
    set to dictionary  ${trap_forwadring_destination}  userUri  ${trap_receiving_user_uri}
    ${resp}=    fusion_api_get_appliance_snmpv3_trap_destinations
    Log    snmpv3_trap_destinations=${resp}    console=True
    ${resp}=    fusion_api_add_appliance_snmpv3_trap_destination    ${trap_forwadring_destination}
    ${resp}=    fusion_api_get_appliance_snmpv3_trap_destinations
    Log    snmpv3_trap_destinations=${resp}    console=True
    Fusion Api Logout Appliance

Verify iLO SNMP Settings
    ${ilo_snmp_settings}=    Run Cpqlocfg and Get SNMP Settings    ${ilo_ip}
    set suite variable    ${ilo_snmp_settings}
    Check iLO SNMP User Presence    ${ilo_snmp_settings}    user=oneview    expected=True
    Check iLO SNMP Address    ${ilo_snmp_settings}    address=${sender_appliance_ip}    rocommunity=${EMPTY}    check_rocommunity=${False}
#
Remove iLo SNMP Settings
    ${response}=    Run cpqlocfg and Clear SNMP Settings    ${ilo_ip}
    Check iLO SNMP User Presence    ${ilo_snmp_settings}    user=oneview    expected=False

Reset iLO and Refresh Server
    Fusion Api Login Appliance    ${sender_appliance_ip}    ${admin_credentials_sender_ov}
    Run cpqlocfg and reset iLO    ${ilo_ip}
    Fusion Api Logout Appliance

Verify iLO SNMP Settings after server reset and refresh
    ${ilo_snmp_settings}=    Run Cpqlocfg and Get SNMP Settings    ${ilo_ip}
    Check iLO SNMP User Presence    ${ilo_snmp_settings}    user=oneview    expected=True
    Check iLO SNMP Address    ${ilo_snmp_settings}    address=${sender_appliance_ip}    rocommunity=${EMPTY}    check_rocommunity=${False}

Send iLO Test Trap
    trap capture at destination OV
    Run Command Via SSH    ${ilo_ip}    ${ilo_credentials['username']}    ${ilo_credentials['password']}    testtrap    >    30
    Fusion Api Login Appliance    ${sender_appliance_ip}    ${admin_credentials_sender_ov}
    ${ilo_alert}=    wait until keyword succeeds    1m    10s    Get Alert By Param   param=?filter=description+like+'Remote+Insight+Test+Trap*' and alertState EQ 'Active' and resourceUri EQ '${server_hardware_uri}'
    Check alert event item    ${ilo_alert}    eventItemName=PduTrapType    eventItemValue=TRAP
    Validate the trap    ${ilo_alert}    ${alert_validation}
    Fusion Api Logout Appliance

Clear Test Trap Alert
    Fusion Api Login Appliance    ${sender_appliance_ip}    ${admin_credentials_sender_ov}
    ${alert_uri}    Create dictionary
    ${alert}=    wait until keyword succeeds    1m    10s    Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${server_hardware_uri}'
    Run Keyword If    '${alert['alertState']}' != 'Active'    FAIL    msg=Alert is not active
    Set To Dictionary    ${alert_uri}    uri=${alert['uri']}
    Clear Alert    ${alert_uri}
    ${cleared_alert}=    wait until keyword succeeds    1m    10s    Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Cleared' and resourceUri EQ '${server_hardware_uri}'
    Run Keyword If    '${cleared_alert['alertState']}' != 'Cleared'    FAIL    msg=Alert is not cleared
    Fusion Api Logout Appliance

Send trap storm
    trap capture at destination OV    300
    : FOR    ${INDEX}    IN RANGE    1    10
    \    Run Command Via SSH    ${ilo_ip}    ${ilo_credentials['username']}    ${ilo_credentials['password']}    testtrap    >    10s
    Fusion Api Login Appliance    ${sender_appliance_ip}    ${admin_credentials_sender_ov}
    ${ilo_alert}=    Wait Until Keyword Succeeds    5m    10s    Get Alert By Param   param=?filter=description like 'A trap storm from ${ilo_ip}*'
    Validate the trap    ${ilo_alert}    ${trap_storm_validation}
    Fusion Api Logout Appliance
    Validate trap forwarding    ${search_string_pcap_file}

Check for storm clearance of trap storm and validate
    trap capture at destination OV    300
    : FOR    ${INDEX}    IN RANGE    1    10
    \    Run Command Via SSH    ${ilo_ip}    ${ilo_credentials['username']}    ${ilo_credentials['password']}    testtrap    >    10s
    Fusion Api Login Appliance    ${sender_appliance_ip}    ${admin_credentials_sender_ov}
    ${ilo_alert}=    Wait Until Keyword Succeeds    20m    10s    Get Alert By Param   param=?filter=description like 'A trap storm from ${ilo_ip} for the trap ${trap_type} has ended*'
    Validate the trap    ${ilo_alert}    ${trap_clearance_validation}
    ${cleared_storm_alert}=    wait until keyword succeeds    1m    10s    Get Alert By Param   param=?filter=description like 'A trap storm from ${ilo_ip} for the trap ${trap_type} has been detected*' and alertState EQ 'Cleared' and resourceUri EQ '${server_hardware_uri}'
    Run Keyword If    '${cleared_storm_alert['alertState']}' != 'Cleared'    FAIL    msg=Trap Storm Alert is not cleared
    ${cleared_trap_storm_alert}=    wait until keyword succeeds    1m    10s    Get Alert By Param   param=?filter=description like 'A trap storm from 16.83.13.66 for the trap ${trap_type} has ended*' and alertState EQ 'Cleared' and resourceUri EQ '${server_hardware_uri}'
    Run Keyword If    '${cleared_trap_storm_alert['alertState']}' != 'Cleared'    FAIL    msg=Trap storm alert is not cleared
    Fusion Api Logout Appliance

Remove Test Trap Alert
    Fusion Api Login Appliance    ${sender_appliance_ip}    ${admin_credentials_sender_ov}
    Remove all alerts    param=?filter=description like '*Remote Insight Test Trap*'
    Fusion Api Logout Appliance

Remove Trap Storm Alert
    Fusion Api Login Appliance    ${sender_appliance_ip}    ${admin_credentials_sender_ov}
    Remove all alerts    param=?filter=description like 'A trap storm from ${ilo_ip}*'
    Fusion Api Logout Appliance

Delete SNMPv3 Trap Destination and SNMPv3 User on Sender OV
    Fusion Api Login Appliance    ${sender_appliance_ip}    ${admin_credentials_sender_ov}
    ${resp}=    fusion api delete appliance snmpv3 trap destination    id=${trap_forwarding_user_id}
    Should Be Equal    '${resp['status_code']}'    '200'    msg=Delete appliance SNMPv3 trap destination by id status code should match 200
    ${resp}=    Fusion Api Delete Appliance Snmpv3 Trap Forwarding User    id=${trap_forwarding_user_id}
    Should Be Equal    '${resp['status_code']}'    '200'    msg=Delete appliance SNMPv3 trap forwarding user by id status code should match 200
    Fusion Api Logout Appliance

Delete SNMPv3 Trap Destination and SNMPv3 User on Receiver OV
    Fusion Api Login Appliance    ${receiver_appliance_ip}    ${admin_credentials_receiver_ov}
    ${resp}=    fusion api delete appliance snmpv3 trap destination    id=${trap_receiving_user_id}
    Should Be Equal    '${resp['status_code']}'    '200'    msg=Delete appliance SNMPv3 trap destination by id status code should match 200
    ${resp}=    Fusion Api Delete Appliance Snmpv3 Trap Forwarding User    id=${trap_receiving_user_id}
    Should Be Equal    '${resp['status_code']}'    '200'    msg=Delete appliance SNMPv3 trap forwarding user by id status code should match 200
    Fusion Api Logout Appliance


*** Keywords ***

Setup Sender and Receier OV for trap testing
    [Documentation]     Enables Debug Logging
    Set log level    TRACE
    Open Connection    ${sender_appliance_ip}
    Login    ${sender_ov_root_username}    ${sender_ov_root_password}
    ${stdout}    ${stderr}    ${rc}=    Execute command    ${cmd_sender_ov[0]}    return_stdout=True    return_stderr=True    return_rc=True
    Should Be Equal    '${rc}'    '0'    command has errored with ${stderr}
    Close connection
    Open Connection    ${receiver_appliance_ip}
    Login    ${receiver_ov_root_username}    ${receiver_ov_root_password}
    ${stdout}    ${stderr}    ${rc}=    Execute command    ${cmd_receiver_ov[0]}    return_stdout=True    return_stderr=True    return_rc=True
    Should Be Equal    '${rc}'    '0'    command has errored with ${stderr}
    ${cmd}=    Set variable    yumdownloader --resolve tcpdump
    ${stdout}    ${stderr}    ${rc}=  Wait until keyword succeeds    120    5    Execute Command    ${cmd}    return_stdout=True    return_stderr=True    return_rc=True
    Should Be Equal    '${rc}'    '0'    ${cmd} has errored with ${stderr}
    ${cmd}=    Set variable    rpm -q tcpdump
    ${stdout}    ${stderr}    ${rc}=  Wait until keyword succeeds    120    5    Execute Command    ${cmd}    return_stdout=True    return_stderr=True    return_rc=True
    ${status}=    Set variable if    ${rc}==0    True
    ${cmd}=    Set variable    rpm -ivh tcpdump*
    ${stdout}    ${stderr}    ${rc}=  Run keyword if    ${status}!=${True}    Wait until keyword succeeds    120    5    Execute Command    ${cmd}    return_stdout=True    return_stderr=True    return_rc=True
    Run keyword if    ${status}!=${True}    Should Be Equal    '${rc}'    '0'    ${cmd} has errored with ${stderr}
    Close connection
    setup environment for trap testing

setup environment for trap testing
    [Documentation]    setup environment for trap testing
    Fusion Api Login Appliance    ${sender_appliance_ip}    ${admin_credentials_sender_ov}
    Log    Adding server to OneView    console=True
    ${resp}=    Add Server hardware from variable    ${server_hardware}
    Log    ${resp}    console=True
    Run keyword if    '${resp[0]['status_code']}'=='202'    Wait For Task   ${resp[0]}   300s   5s
    ...        ELSE    FAIL    Failed to add server hardware to Oneview
    ${resp} =     Fusion Api Get Server Hardware
    Run keyword if    '${resp['count']}'=='0'    FAIL    Failed to add server hardware to Oneview
    Remove All Alerts
    ${ilo_snmp_settings}=    Run Cpqlocfg and Get SNMP Settings    ${ilo_ip}
    Check iLO SNMP User Presence  ${ilo_snmp_settings}  user=oneview  expected=True
    Fusion Api Logout Appliance

trap capture at destination OV
    [Documentation]     trap capture at destination OV
    [Arguments]    ${time_out}=30
    Open Connection    ${receiver_appliance_ip}
    Login    ${receiver_ov_root_username}    ${receiver_ov_root_password}
    Log    Starting command    console=True
    ${cmd}=    Set Variable    timeout ${time_out} tcpdump -nvvv -i any host ${sender_appliance_ip} -w ${pcap_filename}
    Start Command    ${cmd}
    Log    Started command    console=True

Validate the trap
    [Documentation]     Validate the traps
    [Arguments]    ${ilo_alert}    ${alert_validation}
    ${unmatching_list}    Create List
    ${items}=    Get Dictionary Items    ${alert_validation}
    :FOR    ${validation_key}    ${validation_value}    IN    @{items}
    \    ${unmatching_item}=    Compare values in trap to validate    ${validation_key}    ${validation_value}    ${ilo_alert}
    \    Run keyword if    '${unmatching_item}'!='None'    Append to list    ${unmatching_list}    ${unmatching_item}
    \    Run keyword if    '${unmatching_item}'!='None'    Log    Validation failed for ${validation_key}:${validation_value}    console=True
    Log    unmatching_list:${unmatching_list}    console=True
    ${len} =    Get Length    ${unmatching_list}
    Run keyword if    ${len}==0    Log    Validation is successful    console=True
    Run keyword if    ${len}>0    Log    Validation failed for ${len} items    console=True
    Run keyword if    ${len}>0    FAIL    Trap Validation Failed

Compare values in trap to validate
    [Documentation]     Compare values in trap against input values to validate
    [Arguments]    ${v_key}    ${v_value}    ${ilo_alert}
    ${alert_items}=    Get Dictionary Items    ${ilo_alert}
    :FOR    ${a_key}    ${a_value}    IN    @{alert_items}
    \    Run keyword if    '${a_key}'=='${v_key}'    Run keyword if    '${a_value}'!='${v_value}'    Return from keyword    ${v_key}

Validate trap forwarding
    [Documentation]     Validate trap forwarding
    [Arguments]    ${search_pattern}
    Open Connection    ${receiver_appliance_ip}
    Login    ${receiver_ov_root_username}    ${receiver_ov_root_password}
    ${stdout}    ${stderr}    ${rc}=    Execute command    ${pcap_file_process}    return_stdout=True    return_stderr=True    return_rc=True
    Should Be Equal    '${rc}'    '0'    command has errored with ${stderr}
    ${cmd}=    Set Variable    grep -i '${search_pattern}' ${pcap_text_file}
    ${stdout}    ${stderr}    ${rc}=    Execute command    ${cmd}    return_stdout=True    return_stderr=True    return_rc=True
    Should Be Equal    '${rc}'    '0'    command has errored with ${stderr}
    Should contain    ${stdout}    ${search_pattern}
    Close connection
