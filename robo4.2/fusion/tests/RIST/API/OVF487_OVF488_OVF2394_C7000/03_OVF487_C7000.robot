*** Settings ***
Documentation       OVF487 C7000 Support SNMPv3 monitoring of physical servers and enclosures
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Library             OperatingSystem
Library             String
Library             XML
Resource            ../global_variables.robot
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables 		    ${CURDIR}\\${DATA_FILE}
Suite Setup         OVF487 C7000 Setup

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

*** Test Cases ***
OVF487 C7000 PTS1 Get the SNMP Settings
    Set Log Level	TRACE
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    ${ovf487_oa_engine_id} =  Get OA SNMP Engine Id  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}
    ${ovf487_oa_snmp_users} =  Get OA SNMP Users  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}
    ${ovf487_oa_snmp_trapreceivers} =  Get Oa Snmp Trapreceivers  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}
    # ovf487_server1
    ${ovf487_server1_uri} =  Get Server Hardware Uri  ${ovf487_server1}
    ${ovf487_ilo1} =  Get Server Hardware iLO IP  ${ovf487_server1}
    ${ovf487_ilo1_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo1}
    ${ovf487_ilo1_engine_id} =  Get iLO SNMP Engine ID  ${ovf487_ilo1_snmp_settings}
    # ovf487_server2
    ${ovf487_server2_uri} =  Get Server Hardware Uri  ${ovf487_server2}
    ${ovf487_ilo2} =  Get Server Hardware iLO IP  ${ovf487_server2}
    ${ovf487_ilo2_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo2}
    ${ovf487_ilo2_engine_id} =  Get iLO SNMP Engine ID  ${ovf487_ilo2_snmp_settings}
    # ovf487_server3
    ${ovf487_server3_uri} =  Get Server Hardware Uri  ${ovf487_server3}
    ${ovf487_ilo3} =  Get Server Hardware iLO IP  ${ovf487_server3}
    ${ovf487_ilo3_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo3}
    ${ovf487_ilo3_engine_id} =  Get iLO SNMP Engine ID  ${ovf487_ilo3_snmp_settings}
    set suite variable  ${ovf487_oa_engine_id}
    set suite variable  ${ovf487_oa_snmp_users}
    set suite variable  ${ovf487_oa_snmp_trapreceivers}
    set suite variable  ${ovf487_server1_uri}
    set suite variable  ${ovf487_ilo1}
    set suite variable  ${ovf487_ilo1_snmp_settings}
    set suite variable  ${ovf487_ilo1_engine_id}
    set suite variable  ${ovf487_server2_uri}
    set suite variable  ${ovf487_ilo2}
    set suite variable  ${ovf487_ilo2_snmp_settings}
    set suite variable  ${ovf487_ilo2_engine_id}
    set suite variable  ${ovf487_server3_uri}
    set suite variable  ${ovf487_ilo3}
    set suite variable  ${ovf487_ilo3_snmp_settings}
    set suite variable  ${ovf487_ilo3_engine_id}
    log variables

OVF487 C7000 PTS1 Check OA SNMP Settings after Import Enclosure
    Check OA SNMP User Presence  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}  user=oneview  expected=True
    Check OA SNMP User Presence  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}  user=${ovf487_oa_user1[0]}  expected=True
    Check OA SNMP Trapreceiver  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}  destination=${ovf487_oa_trapreceiver1[0]}  community=${ovf487_oa_trapreceiver1[1]}
    Check OA SNMP Trapreceiver  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}  destination=${ovf487_oa_trapreceiver2[0]}  user=${ovf487_oa_trapreceiver2[1]}
    Check OA SNMP Trapreceiver  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}  destination=${APPLIANCE_IP}  user=oneview

OVF487 C7000 PTS1 Check iLO SNMP Settings after Import Enclosure
    # ovf487_server1
    Check iLO SNMP User Presence  ${ovf487_ilo1_snmp_settings}  user=oneview  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo1_snmp_settings}  user=${snmpv3_user1}  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo1_snmp_settings}  user=${snmpv3_user2}  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo1_snmp_settings}  user=${snmpv3_user3}  expected=False
    Check iLO SNMP Address  ${ovf487_ilo1_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity1}
    Check iLO SNMP Address  ${ovf487_ilo1_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity2}
    Check iLO SNMP Address  ${ovf487_ilo1_snmp_settings}  address=${APPLIANCE_IP}  rocommunity=${EMPTY}
    # ovf487_server2
    Check iLO SNMP User Presence  ${ovf487_ilo2_snmp_settings}  user=oneview  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo2_snmp_settings}  user=${snmpv3_user1}  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo2_snmp_settings}  user=${snmpv3_user2}  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo2_snmp_settings}  user=${snmpv3_user3}  expected=False
    Check iLO SNMP Address  ${ovf487_ilo2_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity1}
    Check iLO SNMP Address  ${ovf487_ilo2_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity2}
    Check iLO SNMP Address  ${ovf487_ilo2_snmp_settings}  address=${APPLIANCE_IP}  rocommunity=${EMPTY}
    # ovf487_server3
    Check iLO SNMP User Presence  ${ovf487_ilo3_snmp_settings}  user=oneview  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo3_snmp_settings}  user=${snmpv3_user1}  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo3_snmp_settings}  user=${snmpv3_user2}  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo3_snmp_settings}  user=${snmpv3_user3}  expected=False
    Check iLO SNMP Address  ${ovf487_ilo3_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity1}
    Check iLO SNMP Address  ${ovf487_ilo3_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity2}
    Check iLO SNMP Address  ${ovf487_ilo3_snmp_settings}  address=${APPLIANCE_IP}  rocommunity=${EMPTY}

OVF487 C7000 PTS2 Send OA Test Trap after Import Enclosure
    OA CLI Test SNMP  ${ovf487_oa}  ${oa_credentials['username']}  ${oa_credentials['password']}  VERBOSE=False

OVF487 C7000 PTS2 Verify OA Test Trap Alert after Import Enclosure
    ${ovf487_oa_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'HPE Onboard Administrator Test Trap sent from enclosure*' and alertState EQ 'Active'
    Check alert event item  ${ovf487_oa_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_oa_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_oa}
    check alert event item  ${ovf487_oa_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_oa_engine_id}

OVF487 C7000 PTS2 Send iLO Test Trap after Import Enclosure
    Run Command Via SSH  ${ovf487_ilo1}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s
    Run Command Via SSH  ${ovf487_ilo2}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s
    Run Command Via SSH  ${ovf487_ilo3}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s

OVF487 C7000 PTS2 Verify iLO Test Trap Alert after Import Enclosure
    ${ovf487_ilo1_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server1_uri}'
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_ilo1}
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo1_engine_id}
    ${ovf487_ilo2_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server2_uri}'
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_ilo2}
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo2_engine_id}
    ${ovf487_ilo3_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server3_uri}'
    Check alert event item  ${ovf487_ilo3_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo3_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_ilo3}
    Check alert event item  ${ovf487_ilo3_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo3_engine_id}

OVF487 C7000 PTS2 Remove Test Trap Alerts after Import Enclosure
    Remove all alerts  param=?filter=description like 'HPE Onboard Administrator Test Trap sent from enclosure:*'
    Remove all alerts  param=?filter=description like '*Remote Insight Test Trap*'

OVF487 C7000 PTS5 Create OA Trap Storms
        : FOR    ${INDEX}    IN RANGE    1    10
    \    OA CLI Test SNMP  ${ovf487_oa}  ${oa_credentials['username']}  ${oa_credentials['password']}  VERBOSE=False

OVF487 C7000 PTS5 Wait for OA Trap Storm Alert and Verify
    ${ovf487_oa_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'A trap storm from ${ovf487_oa}*'
    Check alert event item  ${ovf487_oa_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_oa}

OVF487 C7000 PTS5 Create iLO Trap Storms
    : FOR    ${INDEX}    IN RANGE    1    10
    \    Run Command Via SSH  ${ovf487_ilo1}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s
    \    Run Command Via SSH  ${ovf487_ilo2}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s
    \    Run Command Via SSH  ${ovf487_ilo3}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s

OVF487 C7000 PTS5 Wait for iLO Trap Storm Alert and Verify
    ${ovf487_ilo1_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'A trap storm from ${ovf487_ilo1}*'
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_ilo1}
    ${ovf487_ilo2_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'A trap storm from ${ovf487_ilo2}*'
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_ilo2}
    ${ovf487_ilo3_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'A trap storm from ${ovf487_ilo3}*'
    Check alert event item  ${ovf487_ilo3_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_ilo3}

OVF487 C7000 PTS5 Remove Trap Storm Alerts
    Remove all alerts  param=?filter=description like '*Remote Insight Test Trap*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_oa}*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_ilo1}*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_ilo2}*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_ilo3}*'

OVF487 C7000 PTS4 Reset iLO and refresh Server
    Run cpqlocfg and reset iLO  ${ovf487_ilo1}
    Run cpqlocfg and reset iLO  ${ovf487_ilo2}
    Run cpqlocfg and reset iLO  ${ovf487_ilo3}
    sleep  5m
    ${resp1} =  Refresh Server Hardware  ${ovf487_server1}
    ${resp2} =  Refresh Server Hardware  ${ovf487_server2}
    ${resp3} =  Refresh Server Hardware  ${ovf487_server3}
    Wait for Task2  ${resp1}  timeout=1200  interval=10
    Wait for Task2  ${resp2}  timeout=1200  interval=10
    Wait for Task2  ${resp3}  timeout=1200  interval=10

OVF487 C7000 PTS4 Get the iLO SNMP Settings after Reset
    ${ovf487_ilo1_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo1}
    ${ovf487_ilo2_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo2}
    ${ovf487_ilo3_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo3}

OVF487 C7000 PTS4 Send iLO Test Trap after Reset iLO
    Run Command Via SSH  ${ovf487_ilo1}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s
    Run Command Via SSH  ${ovf487_ilo2}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s
    Run Command Via SSH  ${ovf487_ilo3}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s

OVF487 C7000 PTS4 Verify iLO Test Trap Alert after Reset iLO
    ${ovf487_ilo1_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server1_uri}'
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_ilo1}
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo1_engine_id}
    ${ovf487_ilo2_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server2_uri}'
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_ilo2}
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo2_engine_id}
    ${ovf487_ilo3_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server3_uri}'
    Check alert event item  ${ovf487_ilo3_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo3_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_ilo3}
    Check alert event item  ${ovf487_ilo3_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo3_engine_id}

OVF487 C7000 PTS4 Remove Test Trap Alerts after Reset iLO
    Remove all alerts  param=?filter=description like '*Remote Insight Test Trap*'

OVF487 C7000 PTS3 Refresh Enclosure
    ${resp} =  Refresh Enclosure  ${enclosures_expected[0]}
    Wait for Task2  ${resp}  timeout=1200  interval=10

OVF487 C7000 PTS3 Get SNMP Settings after Refresh Enclosure
    ${ovf487_oa_engine_id} =  Get OA SNMP Engine Id  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}
    ${ovf487_oa_snmp_users} =  Get OA SNMP Users  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}
    ${ovf487_oa_snmp_trapreceivers} =  Get Oa Snmp Trapreceivers  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}
    ${ovf487_ilo1_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo1}
    ${ovf487_ilo2_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo2}
    ${ovf487_ilo3_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo3}

OVF487 C7000 PTS3 Send OA Test Trap after Refresh Enclosure
    OA CLI Test SNMP  ${ovf487_oa}  ${oa_credentials['username']}  ${oa_credentials['password']}  VERBOSE=False

OVF487 C7000 PTS3 Verify OA Test Trap Aler after Refresh Enclosure
    ${ovf487_oa_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'HPE Onboard Administrator Test Trap sent from enclosure*' and alertState EQ 'Active'
    Check alert event item  ${ovf487_oa_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_oa_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_oa}
    check alert event item  ${ovf487_oa_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_oa_engine_id}

OVF487 C7000 PTS3 Send iLO Test Trap after Refresh Enclosure
    Run Command Via SSH  ${ovf487_ilo1}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s
    Run Command Via SSH  ${ovf487_ilo2}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s
    Run Command Via SSH  ${ovf487_ilo3}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s

OVF487 C7000 PTS3 Verify iLO Test Trap Alert after Refresh Enclosure
    ${ovf487_ilo1_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server1_uri}'
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_ilo1}
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo1_engine_id}
    ${ovf487_ilo2_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server2_uri}'
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_ilo2}
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo2_engine_id}
    ${ovf487_ilo3_alert} =  Wait Until Keyword Succeeds  5m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server3_uri}'
    Check alert event item  ${ovf487_ilo3_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo3_alert}  eventItemName=ipv4Address  eventItemValue=${ovf487_ilo3}
    Check alert event item  ${ovf487_ilo3_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo3_engine_id}

OVF487 C7000 PTS3 Remove Test Trap Alerts after Refresh Enclosure
    Remove all alerts  param=?filter=description like 'HPE Onboard Administrator Test Trap sent from enclosure:*'
    Remove all alerts  param=?filter=description like '*Remote Insight Test Trap*'

*** Keywords ***
OVF487 C7000 Setup
    [Documentation]  OVF487 C7000 Setup
    Set Log Level	TRACE
    ${feature} =  set variable  OVF487 C7000
    log  ${feature} Suite Setup: Start suite setup  console=True
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

    # Check enclosure added
    log  ${feature} Suite Setup: Start check enclosures added  console=True
    :FOR	${enclosure}	IN	@{enclosures_expected}
	\   ${status} =  Check Resource Existing  ENC:${enclosure['name']}
	\   Run Keyword If  ${status}=='FAIL'  Fail  Enclosure ${enclosure['name']} not found in the appliance
	\   log  Enclosure ${enclosure['name']} found in the appliance
    log  ${feature} Suite Setup: Finish check enclosures added  console=True

    # Remove the test trap alerts
    log  ${feature} Suite Setup: Start remove alerts  console=True
    ${ovf487_ilo1} =  Get Server Hardware iLO IP  ${ovf487_server1}
    ${ovf487_ilo2} =  Get Server Hardware iLO IP  ${ovf487_server2}
    ${ovf487_ilo3} =  Get Server Hardware iLO IP  ${ovf487_server3}
    Remove all alerts  param=?filter=description like 'HPE Onboard Administrator Test Trap sent from enclosure:*'
    Remove all alerts  param=?filter=description like '*Remote Insight Test Trap*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_oa}*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_ilo1}*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_ilo2}*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_ilo3}*'
    log  ${feature} Suite Setup: Finish remove alerts  console=True

    log  ${feature} Suite Setup: Finish check preconditions  console=True
	fusion api logout appliance