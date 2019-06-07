*** Settings ***
Documentation                   AddBaseResources C7000
...                                 - First time setup
...                                 - Add networks, LIG, EG, and enclosures
...                                 - Add storage systems and edit the storage pools to managed
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Library              json
Library  			 Dialogs
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ../global_variables.robot
Variables 		     ${CURDIR}\\${DATA_FILE}
Suite Setup          ABR C7000 Setup
Suite Teardown       Logout


*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'
${DATA_FILE}         Regression_Data.py
${APPLIANCE_ADMIN_PASSWORD}		wpsthpvse1

*** Test Cases ***
ABR C7000 Initialize the Variables
    Set Log Level	TRACE
    log variables

ABR C7000 FTS, Add Licenses and Upload SPP
    First Time Setup	            password=${APPLIANCE_ADMIN_PASSWORD}
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
	Add Licenses from variable		${licenses}
	Upload SPP Bundle    ${spp_path}

ABR C7000 Add the Base Resources
	Add Users from variable			${users}
	${resplist} =  Add San Managers Async  ${san_managers}
    Wait for task2  ${resplist}  timeout=120  interval=10
	Add Ethernet Networks from variable	${ethernet_networks}
	Add FC Networks from variable    ${fc_networks}
	Add FCoE Networks from variable  ${fcoe_networks}
	Remove All Network Sets
	Add Network Sets from variable  ${network_sets}
	Add LIG from list	            ${ligs}
	Add Enclosure Group from list	${enc_groups}
	Add Enclosures from variable	${enclosures}

ABR C7000 Add and Edit the Storage Systems
	${resplist} =  Add Storage Systems Async  ${storage_systems}
	wait for task2  ${resplist}  timeout=300  interval=10
	${resplist} =  Edit Storage Systems Async  ${storage_systems}
	wait for task2  ${resplist}  timeout=300  interval=10

ABR C7000 Edit the Storage Pools to Managed
	${resplist} =  Edit Storage Pools Async  ${storage_pools}
	wait for task2  ${resplist}  timeout=300  interval=10


*** Keywords ***
Logout
	[Documentation]  Log out OneView
    Fusion Api Logout Appliance

ABR C7000 Setup
	[Documentation]  ABR C7000 suite setup
	# OVF1061 Initialize Server Names on iLO
    Set Log Level	TRACE
    ${feature} =  set variable  OVF1061 C7000
    # Get the iLO IPs
    ${OVF1061_SERVER1_ILO} =  Get OA Blade IP  ${ENC1_OA1}  ${oa_credentials['username']}  ${oa_credentials['password']}  14
    ${OVF1061_SERVER2_ILO} =  Get OA Blade IP  ${ENC2_OA1}  ${oa_credentials['username']}  ${oa_credentials['password']}  2
    set suite variable  ${OVF1061_SERVER1_ILO}
    set suite variable  ${OVF1061_SERVER2_ILO}
    Set to Dictionary  ${server_settings_1[0]}  ilo  ${OVF1061_SERVER1_ILO}
    Set to Dictionary  ${server_settings_1[1]}  ilo  ${OVF1061_SERVER2_ILO}
    # Power off the servers via cpqlocfg
    Log  ${feature} Suite Setup: Start power off servers  console=True
    :FOR    ${setting}  IN  @{server_settings_1}
    \   Run cpqlocfg and Power Off Server by Press and Hold  ${setting['ilo']}  VERBOSE=True
    \   Wait Until Keyword Succeeds  120  10  Run cpqlocfg and Check Server Power State  ${setting['ilo']}  OFF  VERBOSE=True
    Log  ${feature} Suite Setup: Finish power off servers  console=True
    # initialize server name on the iLOs
    Log  ${feature} Suite Setup: Start initialize server name on iLOs  console=True
    :FOR    ${setting}  IN  @{server_settings_1}
    \   Run cpqlocfg and Set Server Name  ${setting['ilo']}  ${setting['server_name']}  VERBOSE=True
    \	Run cpqlocfg and Check Server Name  ${setting['ilo']}  ${setting['server_name']}  VERBOSE=True
    Log  ${feature} Suite Setup: Finish initialize server name on iLOs  console=True

    # OVF487 Initialize SNMPv3 users and trap destinations on OA and iLO
    ${feature} =  set variable  OVF487
    log  ${feature} Suite Setup: Start suite setup  console=True
    # Get the iLO IPs
    ${ovf487_ilo1} =  Get OA Blade IP  ${ENC1_OA1}  ${oa_credentials['username']}  ${oa_credentials['password']}  3
    ${ovf487_ilo2} =  Get OA Blade IP  ${ENC3_OA1}  ${oa_credentials['username']}  ${oa_credentials['password']}  5
    ${ovf487_ilo3} =  Get OA Blade IP  ${ENC1_OA1}  ${oa_credentials['username']}  ${oa_credentials['password']}  14
    # Remove ,add and check SNMP users and trapreceivers on the OA
    log  ${feature} Suite Setup: Start remove, add, and check SNMP users and trapreceivers on the OA  console=True
    Remove OA SNMP users  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}
    Remove OA SNMP Trapreceivers  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}
    Add OA SNMP user  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}  ${ovf487_oa_user1}
    Add OA SNMP Trapreceiver  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}  ${ovf487_oa_trapreceiver1}
    Add OA SNMP Trapreceiver  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}  ${ovf487_oa_trapreceiver2}  v3=False
    Check OA SNMP User Presence  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}  user=oneview  expected=False
    Check OA SNMP User Presence  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}  user=${ovf487_oa_user1[0]}  expected=True
    Check OA SNMP Trapreceiver  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}  destination=${ovf487_oa_trapreceiver1[0]}  community=${ovf487_oa_trapreceiver1[1]}
    Check OA SNMP Trapreceiver  ${ovf487_oa}  ${ovf487_oa_username}  ${ovf487_oa_password}  destination=${ovf487_oa_trapreceiver2[0]}  user=${ovf487_oa_trapreceiver2[1]}
    log  ${feature} Suite Setup : Finish remove, add, and check SNMP users and trapreceivers on the OA  console=True
    # Initialize and check iLO SNMP settings
    log  ${feature} Suite Setup: Start initialize and check iLO SNMP settings  console=True
    # ovf487_server1
    Run cpqlocfg and Clear SNMP Settings  ${ovf487_ilo1}
    Run cpqlocfg and Set SNMP Settings  ${ovf487_ilo1}  Init_SNMP_IM_Settings.xml
    ${ovf487_ilo1_snmp_settings} =  Run cpqlocfg and Get SNMP Settings  ${ovf487_ilo1}
    Check iLO SNMP User Presence  ${ovf487_ilo1_snmp_settings}  user=oneview  expected=False
    Check iLO SNMP User Presence  ${ovf487_ilo1_snmp_settings}  user=${snmpv3_user1}  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo1_snmp_settings}  user=${snmpv3_user2}  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo1_snmp_settings}  user=${snmpv3_user3}  expected=True
    Check iLO SNMP Address  ${ovf487_ilo1_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity1}
    Check iLO SNMP Address  ${ovf487_ilo1_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity2}
    Check iLO SNMP Address  ${ovf487_ilo1_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity3}
    # ovf487_server2
    Run cpqlocfg and Clear SNMP Settings  ${ovf487_ilo2}
    Run cpqlocfg and Set SNMP Settings  ${ovf487_ilo2}  Init_SNMP_IM_Settings.xml
    ${ovf487_ilo2_snmp_settings} =  Run cpqlocfg and Get SNMP Settings  ${ovf487_ilo2}
    Check iLO SNMP User Presence  ${ovf487_ilo2_snmp_settings}  user=oneview  expected=False
    Check iLO SNMP User Presence  ${ovf487_ilo2_snmp_settings}  user=${snmpv3_user1}  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo2_snmp_settings}  user=${snmpv3_user2}  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo2_snmp_settings}  user=${snmpv3_user3}  expected=True
    Check iLO SNMP Address  ${ovf487_ilo2_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity1}
    Check iLO SNMP Address  ${ovf487_ilo2_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity2}
    Check iLO SNMP Address  ${ovf487_ilo2_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity3}
    # ovf487_server3
    Run cpqlocfg and Clear SNMP Settings  ${ovf487_ilo3}
    Run cpqlocfg and Set SNMP Settings  ${ovf487_ilo3}  Init_SNMP_IM_Settings.xml
    ${ovf487_ilo3_snmp_settings} =  Run cpqlocfg and Get SNMP Settings  ${ovf487_ilo3}
    Check iLO SNMP User Presence  ${ovf487_ilo3_snmp_settings}  user=oneview  expected=False
    Check iLO SNMP User Presence  ${ovf487_ilo3_snmp_settings}  user=${snmpv3_user1}  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo3_snmp_settings}  user=${snmpv3_user2}  expected=True
    Check iLO SNMP User Presence  ${ovf487_ilo3_snmp_settings}  user=${snmpv3_user3}  expected=True
    Check iLO SNMP Address  ${ovf487_ilo3_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity1}
    Check iLO SNMP Address  ${ovf487_ilo3_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity2}
    Check iLO SNMP Address  ${ovf487_ilo3_snmp_settings}  address=${ovf487_testhead}  rocommunity=${rocommunity3}
    log  ${feature} Suite Setup: Finish initialize and check iLO SNMP settings  console=True
    log  ${feature} Suite Setup: Finish suite setup  console=True

Upload SPP bundle
    [Documentation]    Read SPP bundle from a given path on mapped folder and upload it into OV
    [Arguments]     ${spp_path}
    @{spps_name} =  OperatingSystem.List Directory  ${spp_path}  *.iso  absolute
    :FOR    ${spp_name}  IN  @{spps_name}
    \  Upload Firmware Bundle By Curl  fw_absolute_path=${spp_name}  VERBOSE=True
    Log  Finished uploading ${spp_name} bundle  console=True