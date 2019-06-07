*** Settings ***
Documentation       OVF2394 Synergy Support for SNMPv1 in addition to SNMPv3 for trap forwarding
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
Suite Setup         OVF2394 Synergy Setup

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

*** Test Cases ***
OVF2394 Synergy TS0 Login the Appliance
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

OVF2394 Synergy PTS1 Cleanup SNMPv1 Trap Destination
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance 		${APPLIANCE_IP}  ${admin_credentials}
    ${ovf2394_trap_destination_id} =  set variable  ${ovf2394_trap_destination['uri'][-1]}
    set suite variable  ${ovf2394_trap_destination_id}
    ${resp} = 	fusion api get appliance trap destinations  id=${ovf2394_trap_destination_id}
    run keyword if  ${resp['status_code']}==200  fusion api delete appliance trap destination  id=${ovf2394_trap_destination_id}

OVF2394 Synergy PTS1 Add SNMPv1 Trap Destination
    ${resp} = 	fusion api validate appliance trap destination  body=${ovf2394_trap_destination}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Validate appliance trap destination by id status code should match 200
    ${resp} =  fusion api add or update appliance trap destination  body=${ovf2394_trap_destination}  id=${ovf2394_trap_destination_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Add appliance trap destination status code should match 200
    ${resp} = 	fusion api get appliance trap destinations  id=${ovf2394_trap_destination_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Get appliance trap destination by id status code should match 200

OVF2394 Synergy PTS1 Update SNMPv1 Trap Destination
    ${resp} =  fusion_api_update_appliance_trap_destination  body=${ovf2394_edit_trap_destination}  id=${ovf2394_trap_destination_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Update appliance trap destination status code should match 200
    ${resp} = 	fusion api get appliance trap destinations  id=${ovf2394_trap_destination_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Get appliance trap destination by id status code should match 200
    ${ovf2394_trap_destination_port} =  set variable  ${resp['port']}
    ${ovf2394_community_string} =  set variable  ${resp['communityString']}
    set suite variable  ${ovf2394_trap_destination_port}
    set suite variable  ${ovf2394_community_string}

OVF2394 Synergy PTS1 Purge Trap Listener
    Purge trap listeners  testhead=${OVF2394_testhead}  username=${OVF2394_testhead_username}  password=${OVF2394_testhead_password}  status_file=${ovf2394_status_file}

OVF2394 Synergy PTS1 Start Trap Listener
    Start trap listener  testhead=${OVF2394_testhead}  username=${OVF2394_testhead_username}  password=${OVF2394_testhead_password}  validate_string=${ovf2394_community_string}  data_size=${ovf2394_data_size}  listen_port=${ovf2394_trap_destination_port}  status_file=${ovf2394_status_file}  log_file=${ovf2394_log_file}
    ${status} =  Get trap listener status  testhead=${OVF2394_testhead}  username=${OVF2394_testhead_username}  password=${OVF2394_testhead_password}  status_file=${ovf2394_status_file}
    Should Match  ${status}  START  msg=Trap Listener status should match START

OVF2394 Synergy PTS1 Send iLO Test Trap
    Run Command Via SSH  ${ovf487_ilo1}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s

OVF2394 Synergy PTS1 Check Trap Forwarding
    ${status} =  Get trap listener status  testhead=${OVF2394_testhead}  username=${OVF2394_testhead_username}  password=${OVF2394_testhead_password}  status_file=${ovf2394_status_file}
    Should Match  ${status}  PASS  msg=Trap Listener status should match PASS

OVF2394 Synergy PTS1 Stop Trap Listener
    ${status} =  Get Trap Listener Status  testhead=${OVF2394_testhead}  username=${OVF2394_testhead_username}  password=${OVF2394_testhead_password}  status_file=${ovf2394_status_file}
    run keyword if  '${status}'=='START'  Stop Trap Listener  testhead=${OVF2394_testhead}  username=${OVF2394_testhead_username}  password=${OVF2394_testhead_password}

OVF2394 Synergy PTS1 Remove Test Trap Alerts
    Remove all alerts  param=?filter=description like '*Remote Insight Test Trap*'

OVF2394 Synergy Delete SNMPv1 Trap Destination
    ${resp} =  fusion api delete appliance trap destination  id=${ovf2394_trap_destination_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Delete appliance trap destination status code should match 200

*** Keywords ***
OVF2394 Synergy Setup
    [Documentation]  OVF2394 Synergy Setup
    Set Log Level	TRACE
    ${feature} =  set variable  OVF2394 Synergy
    log  ${feature} Suite Setup: Start suite setup  console=True
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

    # Get the variables
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
    log  ${feature} Suite Setup: Finish suite setup  console=True

    # Remove the test trap alerts
    Remove all alerts  param=?filter=description like '*Remote Insight Test Trap*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_ilo1_LL}*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_ilo2_LL}*'
    log  ${feature} Suite Setup: Finish remove alerts  console=True

    log  ${feature} Suite Setup: Finish suite setup  console=True
	fusion api logout appliance