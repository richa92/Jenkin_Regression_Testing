*** Settings ***
Documentation       OVF1061 Synergy show server name and OS info on the SH
Suite Setup         OVF1061 Synergy Setup
Library				Collections
Library             json
Library  			Dialogs
Resource            ../global_variables.robot
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

${DATA_FILE}         Regression_Data.py

*** Test Cases ***
OVF1061 Synergy TS0 Initialize the Variables and Login
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

OVF1061 Synergy PTS1 Power Off the Servers Initially
    :FOR    ${setting}  IN  @{server_settings_1}
    \   Power off server  SH:${setting['name']}

OVF1061 Synergy PTS1 Update Server Name via RIBCL
    :FOR    ${setting}  IN  @{server_settings_1}
    \   Set Server Hardware Server Name  ${setting['name']}  ${setting['server_name']}
    \	Check Server Hardware Server Name  ${setting['name']}  ${setting['server_name']}

OVF1061 Synergy Refresh the Servers After Update
    ${resplist} =  Refresh Servers in Profiles  ${suite_setup_profiles}
    Wait for Task2  ${resplist}  timeout=600  interval=10

OVF1061 Synergy PTS1 Verify Server Names Match Changes
    :FOR    ${setting}  IN  @{server_settings_1}
    \   Wait Until Keyword Succeeds  2m  10s  Check Resource Attribute  SH:${setting['name']}  serverName  ${setting['server_name']}

OVF1061 Synergy PTS1 Power On the Servers
    :FOR    ${setting}  IN  @{server_settings_2}
    \   Power on server  SH:${setting['name']}
    :FOR    ${setting}  IN  @{server_settings_2}
    \   Wait for Server to reach POST state  SH:${setting['name']}  post_state=FINISHED_POST  timeout=10m  interval=10s

OVF1061 Synergy Refresh the Servers After Power On
    sleep  10 minutes
    ${resplist} =  Refresh Servers in Profiles  ${suite_setup_profiles}
    Wait for Task2  ${resplist}  timeout=600  interval=10

OVF1061 Synergy PTS1 Verify Server Names Match OS Hostnames after Boot OS
    :FOR    ${setting}  IN  @{server_settings_2}
    \   Wait Until Keyword Succeeds  2m  10s  Check Resource Attribute  SH:${setting['name']}  serverName  ${setting['server_name']}

OVF1061 Synergy PTS1 Power Off the Servers
    :FOR    ${setting}  IN  @{server_settings_2}
    \   Power off server  SH:${setting['name']}

OVF1061 Synergy PTS1 Verify Server Names Match OS Hostnames after Power off
    :FOR    ${setting}  IN  @{server_settings_2}
    \   Check Resource Attribute  SH:${setting['name']}  serverName  ${setting['server_name']}

OVF1061 Synergy PTS1 Rip and Replace the Server
    ${ssh_enabled} =  check ssh to console  ${APPLIANCE_IP}  ${ssh_credentials['username']}  ${ssh_credentials['password']}
    run keyword if  '${ssh_enabled}'=='True'  Rip and Replace the Server and Check Server Name

*** Keywords ***
OVF1061 Synergy Setup
    [Documentation]  OVF1061 Synergy Setup
    Set Log Level	TRACE
    ${feature} =  set variable  OVF1061 Synergy
    Log  ${feature} Suite Setup: Start Check preconditions  console=True
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

    # Clean up profiles
    Power Off Servers in Profiles  ${suite_setup_profiles}  powerControl=PressAndHold
    ${resplist} =  Remove Server Profiles from variable  ${suite_setup_profiles}
    Wait for task2  ${resplist}  timeout=3600  interval=10

    # Create the profiles to put the blades in correct boot mode, power on the servers, and delete the profiles
    Log  ${feature} Suite Setup: Start create profiles to put the blades in correct boot mode and delete the profiles  console=True
    Power Off Servers in Profiles  ${suite_setup_profiles}  powerControl=PressAndHold
    ${resplist}=  Add Server Profiles from variable	 ${suite_setup_profiles}
    Wait for Task2  ${resplist}  timeout=3600  interval=10
    Power on Servers in Profiles  ${suite_setup_profiles}
    Wait for Servers in Profiles to reach POST State  ${suite_setup_profiles}  post_state=FINISHED_POST  timeout=15m  interval=10s
    Power off Servers in Profiles  ${suite_setup_profiles}  powerControl=PressAndHold
    ${resplist}=  Remove Server Profiles from variable	 ${suite_setup_profiles}  force=${True}
    Wait for Task2  ${resplist}  timeout=3600  interval=10
    Log  ${feature} Suite Setup: Finish create profiles to put the blades in UEFI mode and delete the profiles  console=True

    Log  ${feature} Suite Setup: Finish check preconditions  console=True
	Fusion Api Logout Appliance

EM EFUSE Blade
    [Documentation]  EM Efuse Blade
    [Arguments]     ${server}  ${action}=  ${server_task}=  ${timeout}=300s  ${interval}=50ms
    ${words} =  set variable  ${server.split(',')}
    ${enclosure} =  set variable  ${words[0]}
    ${bay} =  set variable  ${words[1]}
    ${bay} =  set variable  ${bay.strip()}
    ${bay} =  set variable  ${bay[-1]}
    Get EM IP  enc_serial=${enclosure}
    Get EM Token    ${enclosure}
    EFuse Blade   ${action}  ${bay}
    Log  EFUSE blade ${bay} ${action} on enclosure ${enclosure}  console=True
    Wait Until Keyword Succeeds  ${timeout}  ${interval}  Get task by param  param=?filter='name'='${server_task}' AND associatedResource.resourceName='${server}' AND taskState='Running'
    ${task} =  Get Task By Param  param=?filter='name'='${server_task}' AND associatedResource.resourceName='${server}' AND taskState='Running'
    log  After EFUSE ${action}, the server task URI is ${task['uri']}  console=True
    Wait for task2  ${task}  timeout=600  interval=10
    Log  After EFUSE ${action}, ${server_task} server finish  console=True

Rip and Replace the Server and Check Server Name
    [Documentation]  Rip and Replace the Server and Check Server Name
    EM Efuse Blade  ${OVF1061_SERVER1}  action=EFuseOn  server_task=Remove
    EM Efuse Blade  ${OVF1061_SERVER1}  action=EFuseOff  server_task=Add
    Wait for Server to reach POST state  SH:${OVF1061_SERVER1}  post_state=FINISHED_POST  timeout=10m  interval=10s
    :FOR    ${setting}  IN  @{server_settings_3}
    \   Wait Until Keyword Succeeds  10m  10s  Check Resource Attribute  SH:${setting['name']}  serverName  ${setting['server_name']}
