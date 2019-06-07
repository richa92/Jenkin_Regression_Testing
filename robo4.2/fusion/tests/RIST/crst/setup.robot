*** Settings ***
Documentation		Configures an appliance with resources found in supplied data file.
...                 Pass in specific tags with pybot -i <tag(s)> to limit operations.
...                 pybot -d /tmp/logs/setup -L TRACE -V /root/ci-fit/config_files/cr_dev_ov420.py setup.robot

Library    Collections
Resource   ../../resource/fusion_api_all_resource_files.txt
Resource   ../../wpst_crm/ci_fit/tests/configure_appliance/resource/common.robot

#Suite Setup   		Get appliance IP and Login
#Suite Setup         Suite Setup

# Setup\Teardown for ALL test cases
Test Setup      Test Setup
Test Teardown   Test Teardown


*** Variables ***
${APPLIANCE_IP}                   ${None}
${PLEXXI_CONNECT_HOST}            ${None}
${X-API-VERSION}                  ${Null}
${tbirdEnv}                       ${False}
${PROFILE_ASSIGN_WAIT_TIMEOUT}    860m
${PROFILE_ASSIGN_WAIT_INTERVAL}   2s
${PROFILE_THROTTLE}               ${Null}
${CHECK_DEFAULT_RESERVED_VLAN}    ${True}
${FORKED_SERVER_ADD}              ${True}
${FORKED_PROFILE_CREATE}          ${True}

*** Keywords ***
Suite Setup
    [Documentation]   Suite setup steps
    Run Keyword If   '${X-Api-Version}' == '${null}'   Set Api Version To Current

Test Setup
    [Documentation]                 Pre-conditions for ALL test cases
    Run Keyword If   '${APPLIANCE_IP}' == '${null}'   Set Suite Variable   ${APPLIANCE_IP}   ${appliance['applianceNetworks'][0]['app1Ipv4Addr']}
    Run Keyword If   '${APPLIANCE_IP}' == '${null}'   Fail   msg=APPLIANCE_IP is ${APPLIANCE_IP}. Exiting...
    Fusion Api Login Appliance      ${APPLIANCE_IP}     ${admin_credentials}
    Run Keyword If   '${X-Api-Version}' == '${null}'   Set Api Version To Current

Test Teardown
    [Documentation]     Post-conditions for ALL test cases
    fusion api logout appliance

*** Test Cases ***
OneView First Time Setup
    [Tags]   FTS   OV_FTS   CONFIGURE
    [Setup]
    Get VM IP   ${OV_VM}
    First Time Setup   password=${admin_credentials['password']}
    [Teardown]

Configure Time And Locale
    [Documentation]   Configure OneView time and locale.
    [Tags]   CONFIGURE   TIMELOCALE
    ${resp} =   Fusion Api Configure Appliance Time and Locale   ${timeandlocale}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=200s   interval=5s
    Asynchronous Task Should Be Successful   ${task}

Add Scopes
    [Documentation]   Create scopes from variable.
    [Tags]   CONFIGURE   SCOPES
    ${scopes} =   Get Variable Value   ${scopes}
    Run Keyword If   ${scopes} is not ${null}   Create Scopes   ${scopes}

Add Licenses
	[Tags]    CONFIGURE   LICENSES
	${licenses} =	Get Variable Value	${licenses}
	Run Keyword If	${licenses} is not ${null}		Add Licenses from variable		${licenses}

Add Ranges
    [Documentation]   Disable all generated address and id ranges and add custom ranges from data variable file. Warn users on errors.
    [Tags]   CONFIGURE   RANGES   PROFILES
    ${ranges} =   Get Variable Value   ${ranges}
    ${pools} =   Run Keyword If   ${ranges} is not ${null}   Create List   /rest/id-pools/vmac   /rest/id-pools/vwwn   /rest/id-pools/vsn
    Run Keyword If   ${ranges} is not ${null}   Run Keyword for List   ${pools}   common.Disable ALL Generated ID Ranges
    Run Keyword If   ${ranges} is not ${null}   Add Ranges From variable   ${ranges}

Add Ethernet Networks
    [Documentation]   Add ethernet networks from variable file.
    [Tags]   CONFIGURE   ETHERNET   INDIVIDUAL_ETHERNET
    ${ethernet_networks} =   Get Variable Value   ${ethernet_networks}
    Run Keyword If   ${ethernet_networks} is not ${null}   common.Add Ethernet Networks from variable   ${ethernet_networks}

Add Ethernet Ranges
    [Documentation]   Add ethernet ranges from data variable file.
    [Tags]   CONFIGURE   ETHERNET   ETHERNET_RANGES
    ${ethernet_ranges} =   Get Variable Value   ${ethernet_ranges}
    Run Keyword If   ${ethernet_ranges} is not ${null}   Run Keyword for List   ${ethernet_ranges}   common.Create Ethernet Range

Add Ethernet Networks In Bulk
    [Documentation]   Bulk create ethernet networks from data variable file.
    [Tags]   CONFIGURE   ETHERNET   ETHERNET_BULK
    ${bulk_ethernet_network} =   Get Variable Value   ${bulk_ethernet_network}
    ${resp} =   Run Keyword If   ${bulk_ethernet_network} is not ${null}   Fusion Api Create Ethernet Bulk Networks   ${bulk_ethernet_network}
    Pass Execution If   ${resp} is ${null}   Skipping create ethernet bulk networks due to bulk_ethernet_network being NoneType.
    Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=60m   interval=5s
    Asynchronous Task Should Be Successful   ${task}   checkAssociatedResourceUri=${False}
 
Add Network Sets
    [Documentation]   Add network sets from data variable file.
    [Tags]   CONFIGURE   NS
    ${network_sets} =   Get Variable Value   ${network_sets}
    Run Keyword If   ${network_sets} is ${null}   Fail   msg=network_sets variable is ${null}. Please check your data variable file.
    common.Add Network Sets from variable   ${network_sets}

Add Network Set Ranges
    [Documentation]   Add network set ranges from data variable file.
    [Tags]   CONFIGURE   NS_RANGES
    ${network_set_ranges} =   Get Variable Value   ${network_set_ranges}
    Run Keyword If   ${network_set_ranges} is not ${null}   Run Keyword for List   ${network_set_ranges}   common.Create Network Set Range

# Plexxi stuff starts...
Get Plexxi Connect Authentication Token
    [Documentation]   Login to Plexxi Connect to get authentication token
    [Tags]   CONFIGURE   MINIMAL   PLEXXI_CONFIGURE   PLEXXI_LOGIN   ENABLE_CCIS   DISCOVER_FABRICS   PLEXXI_ONEVIEW_CONFIG
    ...   CFM_ntp   CFM_dns   CFM_transform_gateway_ports   CFM_vlans_gateway_ports   CFM_native_vlan_gateway_ports
    ...   CFM_fec_gateway_ports   CFM_enable_gateway_ports   CFM_LAG   CFM_FIT
    Plexxi Api Login   ${plexxi_connect_host}   ${plexxi_connect_user}   ${plexxi_connect_password}

Enable Composable Cloud Integration Set
    [Documentation]   Enable composable cloud integration set in Composable Fabric Manager
    [Tags]   CONFIGURE   MINIMAL   PLEXXI_CONFIGURE   ENABLE_CCIS
    ${resp} =   Plexxi Api Enable Composable Cloud Integration Set
    Run Keyword If  ${resp['status_code']} is not 200    Fail      status_code:${resp['status_code']}

Discover Plexxi Fabrics
    [Documentation]   Discover Plexxi fabrics in Composable Fabric Manager
    [Tags]   CONFIGURE   MINIMAL   PLEXXI_CONFIGURE   DISCOVER_FABRICS
    ${plexxi_fabrics} =   Get Variable Value   ${plexxi_fabrics}
    Run Keyword If   ${plexxi_fabrics} is not ${Null}   Discover Plexxi Fabrics From Variable   ${plexxi_fabrics}

Perform fitting
    [Documentation]   Perform a fitting for the fabric
    [Tags]   CONFIGURE   MINIMAL   PLEXXI_CONFIGURE   CFM_FIT
    ${resp} =    plexxi api get fabrics
    ${fuuid} =   get from dictionary   ${resp['result'][0]}   uuid
    &{body} =    create dictionary    fabric_uuid=${fuuid}   description=automated fit   name=Automated Fit
    ${resp} =    plexxi api perform fit   body=${body}
    Run Keyword If  ${resp['status_code']} is not 200    Fail      status_code:${resp['status_code']}
    ${uuid} =    get from dictionary   ${resp}   result
    ${resp} =    plexxi api get fits   uuid=${uuid}
    should be equal     ${resp['result']['fit_status']}    COMPLETED


Add OneView Configuration To Plexxi Connect
    [Documentation]   Add OneView configuration to Plexxi Connect Packs
    [Tags]   CONFIGURE   MINIMAL   PLEXXI_CONFIGURE   PLEXXI_ONEVIEW_CONFIG
    ${mac_addresses} =  DeepCopy   ${switch_names}
    Run Keyword If   ${mac_addresses} is not ${Null}   Wait Until List Of Switches Are Healthy And Synced   ${mac_addresses}
    ${oneview_config} =   Get Variable Value   ${oneview_config}   @{EMPTY}
    Run Keyword If   ${oneview_config} != @{EMPTY}   Add OneView Configuration To Plexxi Connect From Variable   ${oneview_config}
    Wait Until Fabric Reached State   ${fabric_name}   Unmanaged
# Plexxi stuff ends...

Initiate Fabric Claim Process
    [Documentation]   Initiate the claim process in fabrics which will transition to fabrics to Adding and Configured
    [Tags]   ONEVIEW_CLAIM_FABRICS
    ${fabric_name} =   Get Variable Value   ${fabric_name}
    ${uri} =   Get Fabric Uri By Name   ${fabric_name}
    ${resp} =   Fusion Api Generic Patch   body=${fabric_adding}   uri=${uri}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=200s   interval=1s
    Asynchronous Task Should Be Successful   ${task}
    # Check that fabric and switches are in configured state
    Wait Until Fabric Reached State   ${fabric_name}   Configured
    ${mac_addresses} =  DeepCopy   ${switch_names}
    Wait Until Switches Reached State  ${mac_addresses}   Configured

Negative Update Reserved Vlan Id Range
    [Documentation]  Attempt to update reserved vlan id range for the fabric as a negative test.
    [Tags]   CONFIGURE   RESERVED_VLANID
    ${reserved_vlan} =   Get Variable Value   ${reserved_vlan}
    Run Keyword If   ${reserved_vlan} is not ${null}   Negative Update Reserved Vlan Id Range   ${reserved_vlan}
    ...       ELSE   Log   reserved_vlan not defined. Skipping update reserved vlan id range for fabric...   WARN   console=${True}

Reserved Vlan Should Be At Default
    [Documentation]   Checks that reserved vlan pool remained at default. Vlan Id 4001-4094 is reserved for Plexxi.
    [Tags]   CONFIGURE   RESERVED_VLANID   DEFAULT_RESERVED_VLANID
    ${resp} =   Run Keyword If   ${CHECK_DEFAULT_RESERVED_VLAN} is ${True}   Fusion Api Get Fabric
    ${total} =   Convert To Integer   ${resp['total']}
    Should Be True   ${total} > ${0}   msg=Response body total is not as expected.
    ${failed_vlan_range} =   Create List
    :FOR   ${m}   IN   @{resp['members']}
    \   Run Keyword If   ${m['reservedVlanRange']['start']} != ${4001} or ${m['reservedVlanRange']['length']} != ${94}   Append To List   ${failed_vlan_range}   ${m['name']}
    :FOR   ${f}   IN   @${failed_vlan_range}
    \   Log To Console   Fabric ${m['name']} has start vlan ${m['reservedVlanRange']['start']} with length ${m['reservedVlanRange']['length']}
    Run Keyword If   ${failed_vlan_range} != @{EMPTY}   Fail   msg=One or more fabrics has unexpected reserved vlan range.

Add NTP to CFM
    [Documentation]   Adds the NTP server info for Fabric\Swithces
    [Tags]    CFM_ntp   CONFIGURE
    ${resp} =    plexxi api get fabrics
    ${uuid} =    get from dictionary   ${resp['result'][0]}   uuid
    append to list    ${cfm_ntp['fabric_uuids']}   ${uuid}
    ${resp} =    plexxi api add ntp client configuration   ${cfm_ntp}
    Run Keyword If  ${resp['status_code']} is not 200    Fail      status_code:${resp['status_code']}


Add DNS to CFM
    [Documentation]   Add the DNS info for fabrics\switches
    [Tags]    CFM_dns   CONFIGURE
    ${resp} =    plexxi api get fabrics
    ${uuid} =    get from dictionary   ${resp['result'][0]}   uuid
    append to list    ${cfm_dns['fabric_uuids']}   ${uuid}
    ${resp} =    plexxi api add dns client configuration   ${cfm_dns}
    Run Keyword If  ${resp['status_code']} is not 200    Fail      status_code:${resp['status_code']}


Set qsfp mode on Gateway ports
    [Documentation]   Changes gateway ports qsfp_mode. 
    [Tags]   CFM_transform_gateway_ports   CONFIGURE
    Log   WARN: This is a workaround step until 100gb cables are supported!    console=True
    ${resp} =    plexxi api bulk patch ports by label    ${gateway_ports_split}   /qsfp_mode    ${gateway_qsfp_mode}
    Run Keyword If  ${resp['status_code']} is not 200    Fail      status_code:${resp['status_code']}

Set FEC mode on Gateway ports
    [Documentation]   Changes gateway ports FEX mode
    [Tags]   CFM_fec_gateway_ports   CONFIGURE
    ${resp} =    plexxi api bulk patch ports by label    ${gateway_ports}   /fec    ${gateway_fec_mode}
    Run Keyword If  ${resp['status_code']} is not 200    Fail      status_code:${resp['status_code']}

Set VLANS on Gateway ports
    [Documentation]   Changes gateway ports VLANS
    [Tags]   CFM_vlans_gateway_ports   CONFIGURE
    ${resp} =    plexxi api bulk patch ports by label    ${gateway_ports}   /ungrouped_vlans    ${gateway_vlan_range}
    Run Keyword If  ${resp['status_code']} is not 200    Fail      status_code:${resp['status_code']}

Set native VLAN on Gateway ports
    [Documentation]   Changes gateway ports native VLAN
    [Tags]   CFM_native_vlan_gateway_ports   CONFIGURE
    # This TC is disabled now that we have MLAGs working. Basically, native vlan should NOT be set on the gateway
    # ports OR on the CFM gw LAG.
    Log   This testcase has been disabled. Native VLAN should NOT be set on GW ports   console=True
    #${resp} =    plexxi api bulk patch ports by label    ${gateway_ports}   /native_vlan    ${gateway_native_vlan}
    #Run Keyword If  ${resp['status_code']} is not 200    Fail      status_code:${resp['status_code']}

Create Uplink LAGS
    [Documentation]   Creates LAG for the gateway ports
    [Tags]   CFM_LAG   CONFIGURE
    Run keyword if    ${gateway_lag_ports} is ${None}    Pass
    @{ports} =   plexxi api get port uuid by switch name and port label   ${gateway_lag_ports}
    ${resp} =    plexxi api get fabrics
    ${fuuid} =   get from dictionary   ${resp['result'][0]}   uuid
    ${body} =    plexxi api make lag body    name=MLAG   fabric_uuid=${fuuid}   port_uuids=${ports}   lacp_fallback_port=${ports[0]}
    ${resp} =    plexxi api add lag    body=${body}
    Run Keyword If  ${resp['status_code']} is not 200    Fail      status_code:${resp['status_code']}

Enable Gateway ports
    [Documentation]   Changes admin state to enabled on gateway ports
    [Tags]   CFM_enable_gateway_ports   CONFIGURE
    ${resp} =    plexxi api bulk patch ports by label    ${gateway_ports}   /admin_state    enabled
    Run Keyword If  ${resp['status_code']} is not 200    Fail      status_code:${resp['status_code']}

Add Logical Switch Groups
    [Documentation]   Add Logical Switch Groups to OneView
    [Tags]   CONFIGURE   LSGS
    ${lsgs} =   Get Variable Value   ${lsgs}
    :FOR   ${lsg}   IN   @{lsgs}
    \   ${task} =   Add Logical Switch Group From Variable   ${lsg}
    \   Asynchronous Task Should Be Successful   ${task}

Add Logical Switches
    [Documentation]   Add Logical Switches to OneView
    [Tags]   CONFIGURE   LSS
    ${lss} =   Get Variable Value   ${lss}
    :FOR   ${ls}   IN   @{lss}
    \   ${task} =   Add Logical Switch From Variable For Composable Rack   ${ls}
    \   Asynchronous Task Should Be Successful   ${task}

Add Rack-mount server hardware
    [Documentation]   Add rack-mount server hardware for management in OneView
    [Tags]   CONFIGURE   DL_SERVER_HARDWARE   DL_SH   SERVER_HARDWARE   SH
    ${server_hardware} =  Get Variable Value   ${server_hardware}
    Add Server Hardware from variable   ${server_hardware}   parallel=${FORKED_SERVER_ADD}

Power Off Servers
    [Documentation]   Poweroff servers.
    [Tags]   CONFIGURE   POWER_OFF_SERVERS
    Power Off All Servers In Parallel

Add Server Profile Templates
    [Documentation]   Add rack-mount server profile templates from variable.
    [Tags]   CONFIGURE   SERVER_PROFILE_TEMPLATES   SPTS
    ${server_profile_templates} =   Get Variable Value   ${server_profile_templates}
    Run Keyword If   ${server_profile_templates} is not ${null}   common.Add Rack-mount Server Profile Templates From Variable   ${server_profile_templates}   connectionSettingsApi=${500}

Add Server Profiles Using Templates
    [Documentation]   Add rack-mount server profiles using templates from variable.
    [Tags]   CONFIGURE   SERVER_PROFILES_TEMPLATE   SPST
    ${server_profiles_using_template} =   Get Variable Value   ${server_profiles_using_template}
    Run Keyword If   ${server_profiles_using_template} is not ${null}   Add Rack-mount Server Profiles Using Template From Variable   ${server_profiles_using_template}  parallel=${FORKED_PROFILE_CREATE}   throttle=${PROFILE_THROTTLE}

Power On All Servers
    [Documentation]   Power up server by hitting momentary press 
    [Tags]   POWER_ON_SERVERS   
    ${POWER_ON_SERIALLY} =   Get Variable Value   ${POWER_ON_SERIALLY}
    Run Keyword If   '${POWER_ON_SERIALLY}' == '${null}'   Power On All Servers In Parallel
    ...       ELSE   Power ON ALL Servers

Add Users
    [Documentation]   Add users from variable file. This will fail on error.
    [Tags]   CONFIGURE   USERS
    ${users} =   Get Variable Value   ${users}
    Run Keyword If   ${users} is not ${null}   common.Add Users from variable   ${users}

Setup Remote Backup
    [Tags]   CONFIGURE   REMOTE_BACKUP
    ${remote_backup} =   Get Variable Value   ${remote_backup}
    Run Keyword If   ${remote_backup} is not ${null}   Update Backup Config   ${remote_backup}
