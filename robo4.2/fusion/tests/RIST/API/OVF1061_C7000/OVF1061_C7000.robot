*** Settings ***
Documentation       OVF1076 C7000 show server name and OS info on the SH
Suite Setup         OVF1061 C7000 Setup
Library				Collections
Library             json
Library  			Dialogs
Resource            ../global_variables.robot
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'
${APPLIANCE_ADMIN_PASSWORD}		wpsthpvse1

*** Test Cases ***
OVF1061 C7000 TS0 Initialize the Variables
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

OVF1061 C7000 Refresh the Servers After Import
    :FOR    ${setting}  IN  @{server_settings_1}
    \  ${resp}=  Refresh Server Hardware  SH:${setting['name']}
    \  Wait for Task2  ${resp}  timeout=600  interval=10

OVF1061 C7000 PTS1 Verify Server Names Match Initial Settings
    :FOR    ${setting}  IN  @{server_settings_1}
    \   Check Resource Attribute  SH:${setting['name']}  serverName  ${setting['server_name']}

OVF1061 C7000 PTS1 Update Server Name via RIBCL
    :FOR    ${setting}  IN  @{server_settings_2}
    \   Set Server Hardware Server Name  ${setting['name']}  ${setting['server_name']}
    \	Check Server Hardware Server Name  ${setting['name']}  ${setting['server_name']}

OVF1061 C7000 Refresh the Servers After Update
    :FOR    ${setting}  IN  @{server_settings_2}
    \  ${resp}=  Refresh Server Hardware  SH:${setting['name']}
    \  Wait for Task2  ${resp}  timeout=600  interval=10

OVF1061 C7000 PTS1 Verify Server Names Match Changes
    :FOR    ${setting}  IN  @{server_settings_2}
    \   Wait Until Keyword Succeeds  2m  10s  Check Resource Attribute  SH:${setting['name']}  serverName  ${setting['server_name']}

OVF1061 C7000 PTS1 Power On the Servers
    :FOR    ${setting}  IN  @{server_settings_3}
    \   Power on server  SH:${setting['name']}
    :FOR    ${setting}  IN  @{server_settings_3}
    \   Wait for Server to reach POST state  SH:${setting['name']}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=5m  interval=20s

OVF1061 C7000 Refresh the Servers After Power On
    sleep  10 minutes
    :FOR    ${setting}  IN  @{server_settings_3}
    \  ${resp}=  Refresh Server Hardware  SH:${setting['name']}
    \  Wait for Task2  ${resp}  timeout=600  interval=10

OVF1061 C7000 PTS1 Verify Server Names Match OS Hostnames after Boot OS
    :FOR    ${setting}  IN  @{server_settings_3}
    \   Wait Until Keyword Succeeds  10m  10s  Check Resource Attribute  SH:${setting['name']}  serverName  ${setting['server_name']}

OVF1061 C7000 PTS1 Power Off the Servers
    :FOR    ${setting}  IN  @{server_settings_3}
    \   Power off server  SH:${setting['name']}

OVF1061 C7000 PTS1 Verify Server Names Match OS Hostnames after Power off
    :FOR    ${setting}  IN  @{server_settings_3}
    \   Wait Until Keyword Succeeds  10m  10s  Check Resource Attribute  SH:${setting['name']}  serverName  ${setting['server_name']}

*** Keywords ***
OVF1061 C7000 Setup
    [Documentation]  OVF1061 C7000 Setup
    Set Log Level	TRACE
    ${feature} =  set variable  OVF1061 C7000
    Log    ${feature} Suite Setup: Start Check preconditions    console=true
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

    # Check enclsoures state
    Log    ${feature} Suite Setup: Start check enclosures state.    console=true
    :FOR    ${enclosure}  IN  @{enclosures_expected}
	\   ${start_state} =  Get Resource Attribute	 ENC:${enclosure['name']}  state
	\   Log    ${feature} Suite Setup: The enclosure ${enclosure['name']} start state is ${start_state}    console=true
	\   CONTINUE FOR LOOP IF    '${start_state}'=='Configured'
	\   ${resp} =  Refresh enclosure  ${enclosure}
	\   Wait for Task2  ${resp}  600  10
	\   Check Resource Attribute	 ENC:${enlcosure}  state  Configured
	Log    ${feature} Suite Setup: Finish check enclosures state.    console=true

    # Check enclsoures status
    Log    ${feature} Suite Setup: Start check enclosures state.    console=true
    :FOR    ${enclosure}  IN  @{enclosures_expected}
	\   ${start_status} =  Get Resource Attribute	 ENC:${enclosure['name']}  status
	\   Log    ${feature} Suite Setup: The enclosure ${enclosure['name']} start status is ${start_status}    console=true
	\   CONTINUE FOR LOOP IF    '${start_status}'!='Critical'
	\   ${resp} =  Refresh enclosure  ${enclosure}
	\   Wait for Task2  ${resp}  600  10
	\   Check Resource Attribute	 ENC:${enlcosure}  status  OK|Warning
	Log    ${feature} Suite Setup: Finish check enclosures status.    console=true

    # check server name on the iLOs
    Log    ${feature} Suite Setup: Start check server name on iLOs    console=true
    :FOR    ${setting}  IN  @{server_settings_1}
    \	Run cpqlocfg and Check Server Name  ${setting['ilo']}  ${setting['server_name']}  VERBOSE=True
    Log    ${feature} Suite Setup: Finish check server name on iLOs    console=true

    Log    ${feature} Suite Setup: Finish check preconditions    console=true
	Fusion Api Logout Appliance