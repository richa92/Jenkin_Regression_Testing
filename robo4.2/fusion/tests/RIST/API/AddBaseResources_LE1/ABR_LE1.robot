*** Settings ***
Documentation                   AddBaseResources_LE1
...                               -  Creates/Adds resouces through LE1 for RIST FVT Functional tests

Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${DATA_FILE}

Suite Setup         Setup
Suite Teardown      Logout

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

${DATA_FILE}         Regression_Data.py

*** Test Cases ***
Update Time and Locale
    ${resp} =    Configure Appliance Time and Locale    ${Time_and_Locale}
    Wait Until Keyword Succeeds    15 min    15 sec      OneView Startup Complete  ${APPLIANCE_IP}
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    Wait For Task      ${resp}
    ${ntp_resp}     Get Appliance Time and Locale
    Verify NTP Servers      ${ntp_resp['ntpServers']}     ${Time_and_Locale['ntpServers']}

Add Licenses and Upload SPP
    Add Licenses from variable  ${licenses}
    Upload SPP Bundle    ${spp_path}

Add Base Resources
	Add San Managers Async  ${san_managers}
	Add Ethernet Networks from variable	${ethernet_networks}
	Add FC Networks from variable  ${fc_networks}
	Add FCoE Networks from variable  ${fcoe_networks}
	Add Network Sets from variable  ${network_sets}
	Add LIG from list  ${ligs}
    Add Enclosure Group from list  ${egs}

Add LE1
    [Tags]    Performance    logical_enclosures-condition-3encl
    Add Logical Enclosure from list  ${les}

Verify Configured Base Resoureces LE1
    Verify Interconnects from list  ${ics}  state=Configured
    Verify Enclosures from list  ${enclosures}  state=Configured
	Wait Until Keyword Succeeds  120s  10s  Run Keyword for List  ${interconnects_linked_ports_expected}  check interconnect linked port status

Add StoreServ and StoreVirtual Storage Systems
    ${resplist} =  Add Storage Systems Async  ${storage_systems}
	Wait for task2  ${resplist}  timeout=300  interval=10

Edit StoreServ and StoreVirtual Storage Systems
	${resplist} =  Edit Storage Systems Async  ${storage_systems}
	Wait for task2  ${resplist}  timeout=300  interval=10

Edit the Storage Pools to Managed
	${resplist} =  Edit Storage Pools Async  ${storage_pools}
	Wait for task2  ${resplist}  timeout=300  interval=10

*** Keywords ***
Setup
    [Documentation]    Setup for ABR_LE1
    Set Log Level	DEBUG
	Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
	Verify Enclosures from list  ${enclosures}  state=Monitored
	Verify Interconnects from list  ${ics}  state=Monitored

Upload SPP bundle
    [Documentation]    Read SPP bundle from a given path on mapped folder and upload it into OV
    [Arguments]     ${spp_path}
    @{spps_name} =  OperatingSystem.List Directory  ${spp_path}  *.iso  absolute
    :FOR    ${spp_name}  IN  @{spps_name}
    \  Upload Firmware Bundle By Curl  fw_absolute_path=${spp_name}  VERBOSE=True
    Log  Finished uploading ${spp_name} bundle  console=True

Logout
    [Documentation]   Just Logout
    Fusion Api Logout Appliance