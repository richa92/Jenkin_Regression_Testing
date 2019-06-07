*** Settings ***
Documentation       OVF488 C7000 SNMPv3 support for forwarding device traps and OneView Alerts to 3rd party destination systems
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
Suite Setup         OVF488 C7000 Setup

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

*** Test Cases ***
OVF488 C7000 TS0 Login the Appliance
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

OVF488 C7000 PTS1 Get SNMPv3 Trap Destinations and Remove
    ${resp} =  fusion api get appliance snmpv3 trap destinations  param=?filter=destinationAddress EQ '${ovf488_testhead}'
    ${count} =  get length  ${resp['members']}
    run keyword if  ${count}==1  fusion api delete appliance snmpv3 trap destination  id=${resp['members'][0]['id']}

OVF488 C7000 PTS1 Get SNMPv3 Users and Remove
    ${resp} =  fusion api get appliance snmpv3 Trap Forwarding Users  param=?filter=userName EQ '${snmpv3_user3}'
    ${count} =  get length  ${resp['members']}
    run keyword if  ${count}==1  Fusion Api Delete Appliance Snmpv3 Trap Forwarding User  id=${resp['members'][0]['id']}

OVF488 C7000 PTS1 Add SNMPv3 User and Check
    ${resp} =  fusion api add appliance snmpv3 trap forwarding user  body=${ovf488_trap_forwarding_user}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Add appliance SNMPv3 trap forwarding user status code should match 200
    ${ovf488_trap_forwarding_user_uri} =  set variable  ${resp['uri']}
    ${ovf488_trap_forwarding_user_id} =  set variable  ${resp['id']}
    set suite variable  ${ovf488_trap_forwarding_user_uri}
    set suite variable  ${ovf488_trap_forwarding_user_id}
    ${resp} =  fusion api get appliance snmpv3 trap forwarding users  id=${ovf488_trap_forwarding_user_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Get appliance SNMPv3 trap forwarding user by id status code should match 200

OVF488 C7000 PTS1 Add SNMPv3 Trap Destination and Check
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

OVF488 C7000 Edit SNMPv3 User
    set to dictionary  ${ovf488_edit_trap_forwarding_user}  id  ${ovf488_trap_forwarding_user_id}
    set to dictionary  ${ovf488_edit_trap_forwarding_user}  uri  ${ovf488_trap_forwarding_user_uri}
   ${resp} =  Fusion Api Edit Appliance Snmpv3 Trap Forwarding User  body=${ovf488_edit_trap_forwarding_user}  id=${ovf488_trap_forwarding_user_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Edit appliance SNMPv3 trap forwarding user by id status code should match 200

OVF488 C7000 Edit SNMPv3 Trap Destination
    set to dictionary  ${ovf488_edit_trap_destination}  userId  ${ovf488_trap_forwarding_user_id}
    set to dictionary  ${ovf488_edit_trap_destination}  userUri  ${ovf488_trap_forwarding_user_uri}
    set to dictionary  ${ovf488_edit_trap_destination}  id  ${ovf488_trap_destination_id}
    set to dictionary  ${ovf488_edit_trap_destination}  uri  ${ovf488_trap_destination_uri}
    ${resp} =  Fusion Api Edit appliance snmpv3 trap destination  body=${ovf488_edit_trap_destination}  id=${ovf488_trap_destination_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Edit appliance SNMPv3 trap destination by id status code should match 200

OVF488 C7000 Get SNMPv3 User
    ${resp} =  fusion api get appliance snmpv3 trap forwarding users  id=${ovf488_trap_forwarding_user_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Get appliance SNMPv3 trap forwarding user by id status code should match 200
    ${ovf488_trap_forwarding_user_name} =  set variable  ${resp['userName']}
    set suite variable  ${ovf488_trap_forwarding_user_name}

OVF488 C7000 Get SNMPv3 Trap Destination
    ${resp} =  fusion api get appliance snmpv3 trap destinations  id=${ovf488_trap_destination_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Get appliance SNMPv3 trap destination by id status code should match 200
    ${ovf488_trap_destination_port} =  set variable  ${resp['port']}
    set suite variable  ${ovf488_trap_destination_port}

OVF488 C7000 PTS1 Purge Trap Listener
    Purge trap listeners  testhead=${ovf488_testhead}  username=${ovf488_testhead_username}  password=${ovf488_testhead_password}  status_file=${ovf488_status_file}

OVF488 C7000 PTS1 Start Trap Listener
    Start trap listener  testhead=${ovf488_testhead}  username=${ovf488_testhead_username}  password=${ovf488_testhead_password}  validate_string=${ovf488_trap_forwarding_user_name}  data_size=${ovf488_data_size}  listen_port=${ovf488_trap_destination_port}  status_file=${ovf488_status_file}  log_file=${ovf488_log_file}
    ${status} =  Get trap listener status  testhead=${ovf488_testhead}  username=${ovf488_testhead_username}  password=${ovf488_testhead_password}  status_file=${ovf488_status_file}
    Should Match  ${status}  START  msg=Trap Listener status should match START

OVF488 C7000 PTS1 Send iLO Test Trap
    Run Command Via SSH  ${ovf487_ilo1}  ${ilo_credentials['username']}  ${ilo_credentials['password']}  testtrap  >  10s

OVF488 C7000 PTS1 Check Trap Forwarding
    ${status} =  Get trap listener status  testhead=${ovf488_testhead}  username=${ovf488_testhead_username}  password=${ovf488_testhead_password}  status_file=${ovf488_status_file}
    Should Match  ${status}  PASS  msg=Trap Listener status should match PASS

OVF488 C7000 PTS1 Stop Trap Listener
    ${status} =  Get Trap Listener Status  testhead=${ovf488_testhead}  username=${ovf488_testhead_username}  password=${ovf488_testhead_password}  status_file=${ovf488_status_file}
    run keyword if  '${status}'=='START'  Stop Trap Listener  testhead=${ovf488_testhead}  username=${ovf488_testhead_username}  password=${ovf488_testhead_password}

OVF488 C7000 PTS1 Remove Test Trap Alerts
    Remove all alerts  param=?filter=description like '*Remote Insight Test Trap*'

OVF488 C7000 Delete SNMPv3 Trap Destination
    ${resp} =  fusion api delete appliance snmpv3 trap destination  id=${ovf488_trap_destination_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Delete appliance SNMPv3 trap destination by id status code should match 200

OVF488 C7000 Delete SNMPv3 User
   ${resp} =  Fusion Api Delete Appliance Snmpv3 Trap Forwarding User  id=${ovf488_trap_forwarding_user_id}
    Should Be Equal  '${resp['status_code']}'  '200'  msg=Delete appliance SNMPv3 trap forwarding user by id status code should match 200

*** Keywords ***
OVF488 C7000 Setup
    [Documentation]  OVF488 C7000 Setup
    Set Log Level	TRACE
    ${feature} =  set variable  OVF488 C7000
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