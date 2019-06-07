*** Settings ***
Documentation		Configures an appliance with resources found in supplied data file. Pass in specific tags with pybot -i <tag(s)> to limit processing
...  TAGS:          [FTS, CONFIGURE],USERS, ETHERNET, ETHERNET_RANGES, NS, NS_RANGES, FC, FCOE, FCOE_RANGES, LIGS, LICENSES, ENCLOSURES, ENCLOSURE_GROUPS,
...                 LES, RANGES, POWER_OFF_SERVERS, PROFILES, SERVER_PROFILES, SERVER_PROFILES_NO_HW, SPSNOHW, SERVER_PROFILE_TEMPLATES, REMOTE_BACKUP, MINIMAL, FABRIC_MANAGER
...	 FTS:           Performs FTS on the appliance.
...	 CONFIGURE:     Run all tags except FTS
...	 MINIMAL:       Add enclosures then assign server profiles to server hardware.
...      PROFILES:      Disable generated ranges, add custom ranges, add server profiles then assign server profiles to server hardware.
...      SERVER_PROFILES:      Add server profiles then assign server profiles to server hardware.
...      FABRIC_MANAGER:      Add APIC server certificate, fabric manager, and tenants to OneView
...                     Example: pybot -V /root/ci-fit/config_files/C15M_Bmark_basic_data-devt.py -vAPPLIANCE_IP:15.186.xx.xx -d /tmp/logs/setup/ -i CONFIGURE -L TRACE setup.robot
...                     Optional arguments:
...                     Default profile throttle: None, to override it use -vPROFILE_THROTTLE:[<number of profiles at a time>]

Library			RoboGalaxyLibrary
Library			FusionLibrary
Library			OperatingSystem
Library			BuiltIn
Library			Collections
Library		        SSHLibrary
Library			String

Resource		../../../../resource/fusion_api_all_resource_files.txt
Resource		resource/common.robot
Library			Collections

Suite Setup   		Get appliance IP and Login

*** Variables ***
${APPLIANCE_IP}                    ${None}
${VM}                              ${None}
${VMSETUP}                         no
${FTS}                             no
${CONFIGURE}                       no
${tbirdEnv}                        ${False}
${X-API-VERSION}                   ${null}
${PROFILE_THROTTLE}                ${Null}
${PROFILE_ASSIGN_WAIT_TIMEOUT}     860m
${PROFILE_ASSIGN_WAIT_INTERVAL}    3s
${FORCE_PROFILE_APPLY}             all
${PROFILE_CREATION_WAIT_TIMEOUT}   860m
${PROFILE_CREATION_WAIT_INTERVAL}  2s
${SPST_WAIT_TIMEOUT}               300m
${SPST_WAIT_INTERVAL}              2s

*** Test Cases ***
First Time Setup
	[Tags]    FTS
    Get VM IP   ${VM}
	First Time Setup    password=${admin_credentials['password']}

Configure Time And Locale
    [Documentation]   Configure OneView time and locale.
    [Tags]   CONFIGURE   TIMELOCALE
    ${resp} =   Fusion Api Configure Appliance Time and Locale   ${timeandlocale}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=200s   interval=5s
    Asynchronous Task Should Be Successful   ${task}

Add Ethernet Networks
    [Documentation]   Add ethernet networks from variable file.
    [Tags]   CONFIGURE   ETHERNET
    ${ethernet_networks} =   Get Variable Value   ${ethernet_networks}
    Run Keyword If   ${ethernet_networks} is not ${null}   common.Add Ethernet Networks from variable   ${ethernet_networks}

Add Ethernet Ranges
    [Documentation]   Add ethernet ranges from data variable file.
    [Tags]   CONFIGURE   ETHERNET_RANGES
    ${ethernet_ranges} =   Get Variable Value   ${ethernet_ranges}
    Run Keyword If   ${ethernet_ranges} is not ${null}   Run Keyword for List   ${ethernet_ranges}   common.Create Ethernet Range

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

Add FC Networks
    [Documentation]   Add Fibre Channel networks from data variable.
    [Tags]   CONFIGURE   FC
    ${fc_networks} =   Get Variable Value   ${fc_networks}
    Run Keyword If   ${fc_networks} is not ${null}   common.Add FC Networks from variable   ${fc_networks}

Add FCoE Networks
    [Documentation]   Add FCoE networks from data variable file.
    [Tags]   CONFIGURE   FCOE
    ${fcoe_networks} =   Get Variable Value   ${fcoe_networks}
    Run Keyword If   ${fcoe_networks} is not ${null}   common.Add FCoE Networks from variable   ${fcoe_networks}

Add FCoe Ranges
	[Tags]    CONFIGURE   FCOE_RANGES
	${fcoe_ranges} =	Get Variable Value	${fcoe_ranges}
	Run Keyword If	${fcoe_ranges} is not ${null}	Run Keyword for List	${fcoe_ranges}	common.Create FCoE Range

Add LIGS
	[Tags]    CONFIGURE   LIGS
	${ligs} =	Get Variable Value	${ligs}
	Run Keyword If	${ligs} is ${null}   Fail   msg=ligs variable is empty. Please check your data variable file.
        ${l} =   Get Length   ${ligs}
	:FOR   ${x}   IN RANGE   0   ${l}
	\   ${task} =  Add LIG from variable   ${ligs[${x}]} 
        \   Asynchronous Task Should Be Successful   ${task}

Add Enclosure Groups
	[Tags]    CONFIGURE   ENCLOSURE_GROUPS  EGS
	${enc_groups} =	Get Variable Value	${enc_groups}
	Run Keyword If	${enc_groups} is ${null}   Fail   msg=enc_groups variable is empty. Please check your data variable file.
        ${l} =   Get Length   ${enc_groups}
	:FOR   ${x}   IN RANGE   0   ${l}
	\   ${resp} =   Add Enclosure Group from variable   ${enc_groups[${x}]}
	\   Request Should Be Successful   ${resp}

Add Licenses
	[Tags]    CONFIGURE   LICENSES
	${licenses} =	Get Variable Value	${licenses}
	Run Keyword If	${licenses} is not ${null}		Add Licenses from variable		${licenses}

Add Enclosures
    [Tags]   CONFIGURE   ENCLOSURES   ENCS   MINIMAL
    ${encs} =   Get Variable Value   ${encs}
    Run Keyword If   ${encs} is not ${null}   Add Enclosures from variable   ${encs}   timeout=60m   interval=5s

Add Ranges
    [Documentation]   Disable all generated address and id ranges and add custom ranges from data variable file. Warn users on errors.
    [Tags]   CONFIGURE   RANGES   PROFILES
    ${ranges} =   Get Variable Value   ${ranges}
    ${pools} =   Run Keyword If   ${ranges} is not ${null}   Create List   /rest/id-pools/vmac   /rest/id-pools/vwwn   /rest/id-pools/vsn
    Run Keyword If   ${ranges} is not ${null}   Run Keyword for List   ${pools}   common.Disable ALL Generated ID Ranges
    Run Keyword If   ${ranges} is not ${null}   Add Ranges From variable   ${ranges}

Power Off Servers
    [Documentation]   Poweroff servers.
    [Tags]    CONFIGURE   POWER_OFF_SERVERS
    Power Off All Servers In Parallel

Add Server Profile Templates
    [Documentation]   Add server profile templates from variable.
    [Tags]   CONFIGURE   SERVER_PROFILE_TEMPLATES   SPTS
    ${server_profile_templates} =   Get Variable Value   ${server_profile_templates}
    Run Keyword If   ${server_profile_templates} is not ${null}   common.Add Server Profile Templates From Variable   ${server_profile_templates}   connectionSettingsApi=${500}

Add Server Profiles Using Templates
    [Documentation]   Add server profiles using templates from variable.
    [Tags]   CONFIGURE   SERVER_PROFILES_TEMPLATE   SPST
    ${server_profiles_using_template} =   Get Variable Value   ${server_profiles_using_template}
    Run Keyword If   ${server_profiles_using_template} is not ${null}   Add Server Profiles Using Template From Variable   ${server_profiles_using_template}   ${server_profile_to_bay_map}   waitTime=${SPST_WAIT_TIMEOUT}   interval=${SPST_WAIT_INTERVAL}   connectionSettingsApi=${600}

Add Server Profiles No Hardware Assigned
    [Documentation]   Create server profiles from variable without assigning to server hardware.
    [Tags]   CONFIGURE   PROFILES   SERVER_PROFILES   SERVER_PROFILES_NO_HW   SPSNOHW
    ${server_profiles} =   Get Variable Value   ${server_profiles_nohw}
    Run Keyword If   ${server_profiles} is not ${null}   Add Unassigned Server Profiles   ${server_profiles}   ${server_profile_to_bay_map}   waitTime=${PROFILE_CREATION_WAIT_TIMEOUT}   interval=${PROFILE_CREATION_WAIT_INTERVAL}

Add Scopes
    [Documentation]   Create scopes from variable.
    [Tags]   CONFIGURE   SCOPES
    ${scopes} =   Get Variable Value   ${scopes}
    Run Keyword If   ${scopes} is not ${null}   Create Scopes   ${scopes}
 
Add Users
    [Documentation]   Add users from variable file. This will fail on error.
    [Tags]   CONFIGURE   USERS
    ${users} =   Get Variable Value   ${users}
    Run Keyword If   ${users} is not ${null}   common.Add Users from variable   ${users}

#[JMP] - Marking this out now that have create profile+assign hw
Add Server Profiles
#	[Tags]    CONFIGURE   PROFILES   SERVER_PROFILES    SPS
#	${server_profiles} =	Get Variable Value	${server_profiles}
#	Run Keyword If	${server_profiles} is not ${null}		Add Server Profiles from variable	${server_profiles}   forceProfileApply=${FORCE_PROFILE_APPLY}   timeout=30m

Assign Server Hardware To Profile
	[Tags]   CONFIGURE   PROFILES   SERVER_PROFILES   ASSIGN_HARDWARE   MINIMAL
	${server_profiles} =	Get Variable Value	${server_profiles_nohw}
	Log   \n\nAssigning Server Hardware to Profiles...   console=${True}
 	Run Keyword If	${server_profiles} is not ${null}		common.Assign Server Hardware To Existing Profiles From Variable	${server_profiles}   ${server_profile_to_bay_map}   timeout=${PROFILE_ASSIGN_WAIT_TIMEOUT}   interval=${PROFILE_ASSIGN_WAIT_INTERVAL}   waitForTask=${True}   forceProfileApply=${FORCE_PROFILE_APPLY}   throttle=${PROFILE_THROTTLE}

Add Fabric Manager And Tenants From Variable
    [Documentation]   Add Fabric Manager and tenants defined in a data variable file to OneView.
    [Tags]   CONFIGURE   FABRIC_MANAGER
    ${fabric_manager} =   Get Variable Value   ${fabric_manager}
    ${apic_certificate} =   Get Variable Value   ${apic_certificate}
    ${tenants} =   Get Variable Value   ${tenants}
    Pass Execution If   ${fabric_manager} is ${null}   Skipping add fabric manager due to missing fabric_manager variable.
    Pass Execution If   ${apic_certificate} is ${null}   Skipping add fabric manager due to missing apic_certificate variable.
    Add Fabric Manager   ${fabric_manager}   ${apic_certificate}
    Pass Execution If   ${tenants} is ${null}   Skipping add tenant to fabric manager due to missing tenants variable.
    :FOR   ${tenant}   IN   @{tenants}
    \   Add Tenant To Fabric Manager   ${fabric_manager}   ${tenant}

Power On All Servers
    [Documentation]   Power up server by hitting momentary press 
    [Tags]   POWER_ON_SERVERS   
    ${POWER_ON_SERIALLY} =   Get Variable Value   ${POWER_ON_SERIALLY}
    Run Keyword If   '${POWER_ON_SERIALLY}' == '${null}'   Power On All Servers In Parallel
    ...       ELSE   Power ON ALL Servers

Setup Remote Backup
    [Tags]   CONFIGURE   REMOTE_BACKUP
    ${remote_backup} =   Get Variable Value   ${remote_backup}
    Run Keyword If   ${remote_backup} is not ${null}   Update Backup Config   ${remote_backup}

# SAN Managers
# Storage Systems
# Storage Pools
# Volumes
# Volume Templates
