*** Settings ***
Documentation       OVF488 Synergy SNMPv3 support for forwarding device traps and OneView Alerts to 3rd party destination systems
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             String
Library             json
Library  			Dialogs
Library             OperatingSystem
Library             String
Library             XML
Resource            ../global_variables.robot
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables 		    ${DATA_FILE}
Suite Setup         OVF488 Synergy Setup

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

*** Test Cases ***
Confirm Firewall Open
    [Documentation]    Confirm the firewall on the trap destination testhead is open for UDP from this ring
    [Tags]    CONFIRM_FW_OPEN
    Set Log Level	TRACE

    ${exp_reject} =    Set Variable    REJECT\\s+all

    ${iptables} =    Run Command Via SSH    ip=${ovf488_testhead}  username=${ovf488_testhead_username}
    ...    pswd=${ovf488_testhead_password}    command=iptables -L    prompt=#    timeout=20s
    Log    iptables: ${iptables}    console=true

    @{iptables} =     Split To Lines    ${iptables}
    :FOR    ${entry}    IN    @{iptables}
    \    ${status}    ${value} =    Run Keyword And Ignore Error    Should Match Regexp    ${entry}    ${ovf488_fw_required}
    \   Pass Execution If    '${status}'=='PASS'    Found needed ACCEPT entry prior to REJECT: ${entry}
    \    ${status}    ${value} =    Run Keyword And Ignore Error    Should Match Regexp    ${entry}    ${exp_reject}
    \    Run Keyword If    '${status}'=='PASS'    Fatal Error    Found REJECT all entry prior to required ACCEPT entry: ${entry}

OVF488 Synergy TS0 Login the Appliance
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

OVF488 Synergy PTS1 Get SNMPv3 Trap Destinations and Remove
    ${resp} =  fusion api get appliance snmpv3 trap destinations  param=?filter=destinationAddress EQ '${ovf488_testhead}'
    ${count} =  get length  ${resp['members']}
    run keyword if  ${count}==1  fusion api delete appliance snmpv3 trap destination  id=${resp['members'][0]['id']}

OVF488 Synergy PTS1 Get SNMPv3 Users and Remove
    ${resp} =  fusion api get appliance snmpv3 Trap Forwarding Users  param=?filter=userName EQ '${snmpv3_user3}'
    ${count} =  get length  ${resp['members']}
    run keyword if  ${count}==1  Fusion Api Delete Appliance Snmpv3 Trap Forwarding User  id=${resp['members'][0]['id']}

OVF488 Synergy PTS1 Add SNMPv3 User and Check
    ${resp} =  fusion api add appliance snmpv3 trap forwarding user  body=${ovf488_trap_forwarding_user}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Add appliance SNMPv3 trap forwarding user status code should match 200
    ${ovf488_trap_forwarding_user_uri} =  set variable  ${resp['uri']}
    ${ovf488_trap_forwarding_user_id} =  set variable  ${resp['id']}
    set suite variable  ${ovf488_trap_forwarding_user_uri}
    set suite variable  ${ovf488_trap_forwarding_user_id}
    ${resp} =  fusion api get appliance snmpv3 trap forwarding users  id=${ovf488_trap_forwarding_user_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Get appliance SNMPv3 trap forwarding user by id status code should match 200

OVF488 Synergy PTS1 Add SNMPv3 Trap Destination and Check
    set to dictionary  ${ovf488_trap_destination}  userId  ${ovf488_trap_forwarding_user_id}
    set to dictionary  ${ovf488_trap_destination}  userUri  ${ovf488_trap_forwarding_user_uri}
    ${resp} =  fusion api add appliance snmpv3 trap destination  body=${ovf488_trap_destination}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Add appliance SNMPv3 trap destination status code should match 200
    ${ovf488_trap_destination_uri} =  set variable  ${resp['uri']}
    ${ovf488_trap_destination_id} =  set variable  ${resp['id']}
    set suite variable  ${ovf488_trap_destination_uri}
    set suite variable  ${ovf488_trap_destination_id}
    ${resp} =  fusion api get appliance snmpv3 trap destinations  id=${ovf488_trap_destination_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Get appliance SNMPv3 trap destination by id status code should match 200

OVF488 Synergy Edit SNMPv3 User
    set to dictionary  ${ovf488_edit_trap_forwarding_user}  id  ${ovf488_trap_forwarding_user_id}
    set to dictionary  ${ovf488_edit_trap_forwarding_user}  uri  ${ovf488_trap_forwarding_user_uri}
   ${resp} =  Fusion Api Edit Appliance Snmpv3 Trap Forwarding User  body=${ovf488_edit_trap_forwarding_user}  id=${ovf488_trap_forwarding_user_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Edit appliance SNMPv3 trap forwarding user by id status code should match 200

OVF488 Synergy Edit SNMPv3 Trap Destination
    set to dictionary  ${ovf488_edit_trap_destination}  userId  ${ovf488_trap_forwarding_user_id}
    set to dictionary  ${ovf488_edit_trap_destination}  userUri  ${ovf488_trap_forwarding_user_uri}
    set to dictionary  ${ovf488_edit_trap_destination}  id  ${ovf488_trap_destination_id}
    set to dictionary  ${ovf488_edit_trap_destination}  uri  ${ovf488_trap_destination_uri}
    ${resp} =  Fusion Api Edit appliance snmpv3 trap destination  body=${ovf488_edit_trap_destination}  id=${ovf488_trap_destination_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Edit appliance SNMPv3 trap destination by id status code should match 200

OVF488 Synergy Get SNMPv3 User
    ${resp} =  fusion api get appliance snmpv3 trap forwarding users  id=${ovf488_trap_forwarding_user_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Get appliance SNMPv3 trap forwarding user by id status code should match 200
    ${ovf488_trap_forwarding_user_name} =  set variable  ${resp['userName']}
    set suite variable  ${ovf488_trap_forwarding_user_name}

OVF488 Synergy Get SNMPv3 Trap Destination
    ${resp} =  fusion api get appliance snmpv3 trap destinations  id=${ovf488_trap_destination_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Get appliance SNMPv3 trap destination by id status code should match 200
    ${ovf488_trap_destination_port} =  set variable  ${resp['port']}
    set suite variable  ${ovf488_trap_destination_port}

OVF488 Synergy PTS1 Purge Trap Listener
    Purge trap listeners  testhead=${ovf488_testhead}  username=${ovf488_testhead_username}  password=${ovf488_testhead_password}  status_file=${ovf488_status_file}

OVF488 Synergy PTS1 Start Trap Listener
    Start trap listener  testhead=${ovf488_testhead}  username=${ovf488_testhead_username}  password=${ovf488_testhead_password}  validate_string=${ovf488_trap_forwarding_user_name}  data_size=${ovf488_data_size}  listen_port=${ovf488_trap_destination_port}  status_file=${ovf488_status_file}  log_file=${ovf488_log_file}
    ${status} =  Get trap listener status  testhead=${ovf488_testhead}  username=${ovf488_testhead_username}  password=${ovf488_testhead_password}  status_file=${ovf488_status_file}
    Should Match  ${status}  START  msg=Trap Listener status should match START

OVF488 Synergy PTS1 Send iLO Test Trap
    Run Command Via SSH  ${ovf487_ilo1}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s

OVF488 Synergy PTS1 Check Trap Forwarding
    ${status} =  Get trap listener status  testhead=${ovf488_testhead}  username=${ovf488_testhead_username}  password=${ovf488_testhead_password}  status_file=${ovf488_status_file}
    Should Match  ${status}  PASS  msg=Trap Listener status should match PASS

OVF488 Synergy PTS1 Stop Trap Listener
    ${status} =  Get Trap Listener Status  testhead=${ovf488_testhead}  username=${ovf488_testhead_username}  password=${ovf488_testhead_password}  status_file=${ovf488_status_file}
    run keyword if  '${status}'=='START'  Stop Trap Listener  testhead=${ovf488_testhead}  username=${ovf488_testhead_username}  password=${ovf488_testhead_password}

OVF488 Synergy PTS1 Remove Test Trap Alerts
    Remove all alerts  param=?filter=description like '*Remote Insight Test Trap*'

OVF488 Synergy Delete SNMPv3 Trap Destination
    ${resp} =  fusion api delete appliance snmpv3 trap destination  id=${ovf488_trap_destination_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Delete appliance SNMPv3 trap destination by id status code should match 200

OVF488 Synergy Delete SNMPv3 User
   ${resp} =  Fusion Api Delete Appliance Snmpv3 Trap Forwarding User  id=${ovf488_trap_forwarding_user_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Delete appliance SNMPv3 trap forwarding user by id status code should match 200

*** Keywords ***
OVF488 Synergy Setup
    [Documentation]  OVF488 Synergy Setup
    Set Log Level	TRACE
    ${feature} =  set variable  OVF488 Synergy
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
    log  ${feature} Suite Setup: Start remove alerts  console=True
    Remove all alerts  param=?filter=description like '*Remote Insight Test Trap*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_ilo1}*'
    Remove all alerts  param=?filter=description like 'A trap storm from ${ovf487_ilo2}*'
    log  ${feature} Suite Setup: Finish remove alerts  console=True

    log  ${feature} Suite Setup: Finish suite setup  console=True
	fusion api logout appliance