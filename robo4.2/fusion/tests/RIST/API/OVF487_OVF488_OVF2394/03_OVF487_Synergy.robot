*** Settings ***
Documentation       OVF487 Synergy Support SNMPv3 monitoring of physical servers and enclosures
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
Variables 		    ${DATA_FILE}
Suite Setup         OVF487 Synergy Setup

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

*** Test Cases ***
OVF487 Synergy TS0 Login Fusion
    Set Log Level	TRACE
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

OVF487 Synergy PTS1 Check iLO SNMP Settings
    Check iLO SNMP User Presence  ${ovf487_ilo1_snmp_settings}  user=oneview  expected=True
    Check iLO SNMP Address  ${ovf487_ilo1_snmp_settings}  address=${APPLIANCE_IPv6}  rocommunity=${EMPTY}
    Check iLO SNMP User Presence  ${ovf487_ilo2_snmp_settings}  user=oneview  expected=True
    Check iLO SNMP Address  ${ovf487_ilo2_snmp_settings}  address=${APPLIANCE_IPv6}  rocommunity=${EMPTY}

OVF487 Synergy PTS2 Send iLO Test Trap After Add Enclosure
    Run Command Via SSH  ${ovf487_ilo1}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  30
    Run Command Via SSH  ${ovf487_ilo2}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  30

OVF487 Synergy PTS2 Verify iLO Test Trap Alert After Add Enclosure
    ${ovf487_ilo1_alert} =  wait until keyword succeeds  1m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server1_uri}'
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=ipv6Address  eventItemValue=${ovf487_ilo1_LL}
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo1_engine_id}
    ${ovf487_ilo2_alert} =  wait until keyword succeeds  1m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server2_uri}'
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=ipv6Address  eventItemValue=${ovf487_ilo2_LL}
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo2_engine_id}

OVF487 Synergy PTS2 Remove Test Trap Alert After Add Enclosure
    Remove all alerts  param=?filter=description like '*Remote Insight Test Trap*'

OVF487 Synergy PTS3 Refresh Enclosure
    ${resp} =  Refresh Enclosure  ${enclosures_expected[0]}
    Wait for Task2  ${resp}  timeout=1200  interval=10

OVF487 C7000 PTS3 Get the iLO SNMP Settings after Refresh Enclosure
    ${ovf487_ilo1_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo1}
    ${ovf487_ilo2_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo2}

OVF487 Synergy PTS3 Send iLO Test Trap after Refresh Enclosure
    Run Command Via SSH  ${ovf487_ilo1}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s
    Run Command Via SSH  ${ovf487_ilo2}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s

OVF487 Synergy PTS3 Verify iLO Test Trap Alert after Refresh Enclosure
    ${ovf487_ilo1_alert} =  wait until keyword succeeds  1m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server1_uri}'
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=ipv6Address  eventItemValue=${ovf487_ilo1_LL}
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo1_engine_id}
    ${ovf487_ilo2_alert} =  wait until keyword succeeds  1m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server2_uri}'
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=ipv6Address  eventItemValue=${ovf487_ilo2_LL}
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo2_engine_id}

OVF487 Synergy PTS3 Remove Test Trap Alerts after Refresh Enclosure
    Remove all alerts  param=?filter=description like 'Remote Insight Test Trap*'

OVF487 Synergy PTS5 Create iLO Trap Storms
    : FOR    ${INDEX}    IN RANGE    1    10
    \    Run Command Via SSH  ${ovf487_ilo1}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s
    \    Run Command Via SSH  ${ovf487_ilo2}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s

OVF487 Synergy PTS5 Wait for iLO Trap Storm Alert and Verify
    ${ovf487_ilo1_alert} =  Wait Until Keyword Succeeds  1m  10s  Get Alert By Param   param=?filter=description like 'A trap storm from ${ovf487_ilo1_LL}*'
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=ipv6Address  eventItemValue=${ovf487_ilo1_LL}
    ${ovf487_ilo2_alert} =  Wait Until Keyword Succeeds  1m  10s  Get Alert By Param   param=?filter=description like 'A trap storm from ${ovf487_ilo2_LL}*'
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=ipv6Address  eventItemValue=${ovf487_ilo2_LL}

OVF487 Synergy PTS5 Remove Trap Storm Alerts
    Remove all alerts  param=?filter=description like 'Remote Insight Test Trap*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_ilo1_LL}*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_ilo2_LL}*'

OVF487 Synergy PTS4 Reset iLO and Refresh Server
    Run cpqlocfg and reset iLO  ${ovf487_ilo1}
    Run cpqlocfg and reset iLO  ${ovf487_ilo2}
    sleep  5m
    ${resp1} =  Refresh Server Hardware  ${ovf487_server1}
    ${resp2} =  Refresh Server Hardware  ${ovf487_server2}
    Wait for Task2  ${resp1}  timeout=1200  interval=10
    Wait for Task2  ${resp2}  timeout=1200  interval=10

OVF487 C7000 PTS4 Get the iLO SNMP Settings after Reset
    ${ovf487_ilo1_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo1}
    ${ovf487_ilo2_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo2}

OVF487 Synergy PTS4 Send iLO Test Trap after Reset iLO
    Run Command Via SSH  ${ovf487_ilo1}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s
    Run Command Via SSH  ${ovf487_ilo2}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s

OVF487 Synergy PTS4 Verify iLO Test Trap Alert after Reset iLO
    ${ovf487_ilo1_alert} =  wait until keyword succeeds  1m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server1_uri}'
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=ipv6Address  eventItemValue=${ovf487_ilo1_LL}
    Check alert event item  ${ovf487_ilo1_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo1_engine_id}
    ${ovf487_ilo2_alert} =  wait until keyword succeeds  1m  10s  Get Alert By Param   param=?filter=description like 'Remote Insight Test Trap*' and alertState EQ 'Active' and resourceUri EQ '${ovf487_server2_uri}'
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=PduTrapType  eventItemValue=TRAP
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=ipv6Address  eventItemValue=${ovf487_ilo2_LL}
    Check alert event item  ${ovf487_ilo2_alert}  eventItemName=ContextEngineID  eventItemValue=${ovf487_ilo2_engine_id}

OVF487 Synergy PTS4 Remove Test Trap Alerts after Reset iLO
    Remove all alerts  param=?filter=description like '*Remote Insight Test Trap*'

*** Keywords ***
OVF487 Synergy Setup
    [Documentation]  OVF487 Synergy Setup
    Set Log Level	TRACE
    ${feature} =  set variable  OVF487 Synergy
    log  ${feature} Suite Setup: Start suite setup  console=True
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

    # Get the variables
    ${APPLIANCE_IPv6} =  Get Appliance Bond0 IPv6 Address
    # ovf487_server1
    ${ovf487_server1_uri} =  Get Server Hardware Uri  ${ovf487_server1}
    ${ovf487_ilo1} =  Get Server Hardware iLO IP  ${ovf487_server1}
    ${ovf487_ilo1_LL} =  Get Server Hardware iLO LinkLocal IP  ${ovf487_server1}
    ${ovf487_ilo1_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo1}
    ${ovf487_ilo1_engine_id} =  Get iLO SNMP Engine ID  ${ovf487_ilo1_snmp_settings}
    # ovf487_server2
    ${ovf487_server2_uri} =  Get Server Hardware Uri  ${ovf487_server2}
    ${ovf487_ilo2} =  Get Server Hardware iLO IP  ${ovf487_server2}
    ${ovf487_ilo2_LL} =  Get Server Hardware iLO LinkLocal IP  ${ovf487_server2}
    ${ovf487_ilo2_snmp_settings} =  Run Cpqlocfg and Get SNMP Settings  ${ovf487_ilo2}
    ${ovf487_ilo2_engine_id} =  Get iLO SNMP Engine ID  ${ovf487_ilo2_snmp_settings}
    set suite variable  ${APPLIANCE_IPv6}
    set suite variable  ${ovf487_server1_uri}
    set suite variable  ${ovf487_ilo1}
    set suite variable  ${ovf487_ilo1_LL}
    set suite variable  ${ovf487_ilo1_snmp_settings}
    set suite variable  ${ovf487_ilo1_engine_id}
    set suite variable  ${ovf487_server2_uri}
    set suite variable  ${ovf487_ilo2}
    set suite variable  ${ovf487_ilo2_LL}
    set suite variable  ${ovf487_ilo2_snmp_settings}
    set suite variable  ${ovf487_ilo2_engine_id}
    
    # Check enclosure added
    log  ${feature} Suite Setup: Start check enclosures added  console=True
    :FOR	${enclosure}	IN	@{enclosures_expected}
	\   ${status} =  Check Resource Existing  ENC:${enclosure['name']}
	\   Run Keyword If  ${status}=='FAIL'  Fail  Enclosure ${enclosure['name']} not found in the appliance
	\   log  Enclosure ${enclosure['name']} found in the appliance
    log  ${feature} Suite Setup: Finish check enclosures added  console=True

    # Remove the test trap alerts
    log  ${feature} Suite Setup: Start remove alerts  console=True
    Remove all alerts  param=?filter=description like '*Remote Insight Test Trap*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_ilo1_LL}*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_ilo2_LL}*'
    log  ${feature} Suite Setup: Finish remove alerts  console=True

    log  ${feature} Suite Setup: Finish suite setup  console=True
	fusion api logout appliance