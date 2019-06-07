*** Settings ***
Documentation		Configures an appliance with resources found in supplied data file. Pass in specific tags with pybot -i <tag(s)> to limit processing
...  TAGS:          [FTS, CONFIGURE], RENAME_ENCLOSURES, HWSETUP, USERS, ETHERNET, ETHERNET_RANGES, NS, NS_RANGES, FC, FCOE, FCOE_RANGES, LIGS, LICENSES, ENCLOSURES,
...                 ENCLOSURE_GROUPS, LES, POWER_OFF_SERVERS, PROFILES, SERVER_PROFILES, SERVER_PROFILE_TEMPLATES, SERVER_PROFILES_TEMPLATE, SPST, SET_ENV, SPTS, TIMELOCALE, REMOTE_BACKUP, RESERVED_VLANID, SERVER_PROFILES_NO_HW, SPSNOHW, LES, FABRIC_MANAGERS, TENANTS, REPO, CONNECTION_TEMPLATE, LSGS, LSS, LSGS_LSS
...	 CONFIGURE:     Run all tags except HWSETUP
...      MINIMAL:       Add logical enclosures then assign server profiles to server hardware.
...      PROFILES:      Disable generated ranges, add custom ranges, add server profiles then assign server profiles to server hardware
...      SERVER_PROFILES: Add server profiles then assign profiles to server hardware.
...      FABRIC_MANAGERS: Add APIC Server certificate and fabric manager from data variable to OneView.
...      TENANTS: Add tenants from data variable to OneView.
...      REPO: Add repository from data variable to OneView.
...      CONNECTION_TEMPLATE: Changes the bandwidth through connection template.
...                     Example workflow: Don't do FTS instead go straight to configuring your tbird based on the data variable you have
...                                       pybot -d /tmp/logs/eagle62-dev/tbird-setup-sp-nohw -V /root/ci-fit/config_files/eagle62_basic_data-devt.py -i "CONFIGURE" -L TRACE tbird-setup-sp-nohw.robot
...                                       Optional arguments:
...                                       To add an external repository to appliance, use -v REPOSITORY_NAME:"External" -v REPOSITORY_USERNAME:"test" -v REPOSITORY_PASSWORD:"hpvse123" -v REPOSITORY_WEBADDRESS:"http://15.186.7.144/webdav"
...                                       Default profile throttle: None, to override it use -vPROFILE_THROTTLE:[<number of profiles at a time>]
...                                       Default LIG_ADD_WAIT_TIMEOUT: 260s, to override it use -vLIG_ADD_WAIT_TIMEOUT:<ex:  180s>
...                                       Default REPOSITORY_NAME: None, to override it use -v REPOSITORY_NAME:<name of external repository>
...                                       Default REPOSITORY_WEBADDRESS: None, to override it use -v REPOSITORY_WEBADDRESS:<link of webaddress>
...                                       Default REPOSITORY_USERNAME: None, to override it use -v REPOSITORY_USERNAME:<repository username>
...                                       Default REPOSITORY_PASSWORD: None, to override it use -v REPOSITORY_PASSWORD:<repository password>
...                                       To set your setup add logical switches timeout (default 15m), use -vADD_LOGICAL_SWITCHES_TIMEOUT:<Robot Framework's time format (e.g. '1 minute', '2 min 3 s', '4.5')>


Resource                ../../../../resource/fusion_api_all_resource_files.txt
Resource		resource/common.robot
Library			Collections

Suite Setup		Get appliance IP and Login

*** Variables ***
${X-API-VERSION}		    ${null}
${FUSION_PROMPT}		    \#
${FUSION_TIMEOUT}		    60
${PROFILE_THROTTLE}                 ${Null}
${PROFILE_ASSIGN_WAIT_TIMEOUT}      860m
${PROFILE_ASSIGN_WAIT_INTERVAL}     3s
${PROFILE_CREATION_WAIT_TIMEOUT}    860m
${PROFILE_CREATION_WAIT_INTERVAL}   2s
${LE_ADD_WAIT_TIMEOUT}              120m
${LE_ADD_WAIT_INTERVAL}             1m
${LIG_ADD_WAIT_TIMEOUT}             260s
${LIG_ADD_WAIT_INTERVAL}            5s
${SPST_WAIT_TIMEOUT}                300m
${SPST_WAIT_INTERVAL}               2s
${FORCE_PROFILE_APPLY}              all
${tbirdEnv}                         ${True}
${REPOSITORY_NAME}                  None
${REPOSITORY_USERNAME}              None
${REPOSITORY_PASSWORD}              None
${REPOSITORY_WEBADDRESS}            None
${ADD_REPOSITORY_TIMEOUT}           2m
${ADD_REPOSITORY_INTERVAL}          2s
${NITRO_MODEL_NAME}                 Virtual Connect SE 100Gb F32 Module for Synergy
${NETWORK_RANGE_TO_EDIT_BANDWIDTH}  None
${ADD_LOGICAL_SWITCHES_TIMEOUT}     15m
&{RANGES_CAT_URIS}                  id-range-VMAC=/rest/id-pools/vmac   id-range-VWWN=/rest/id-pools/vwwn   id-range-VSN=/rest/id-pools/vsn


*** Test Cases ***
Rename Enclosures
    [Documentation]   Rename enclosure based on enc_names variable defined in data variable file. This will fail on error.
    [Tags]   CONFIGURE   RENAME_ENCLOSURES
    ${enc_names} =   Get Variable Value   ${enc_names}
    Run Keyword If   ${enc_names} is not ${null}   Rename Enclosures From Variable   ${enc_names}
    ...       ELSE   Log   enc_names not defined. Skipping enclosure rename...   WARN   console=${True}

Configure Thunderbird Hardware
    [Documentation]   Run thunderbird hardware setup and fail on error.
    [Tags]	  HWSETUP
    Log   \n\nX-API-Version: ${X-API-VERSION}   console=${True}
    Invoke Hardware Setup 		timeout=720

Configure Time And Locale
    [Documentation]   Configure OneView time and locale.
    [Tags]    CONFIGURE   TIMELOCALE
    ${timeandlocale} =   Get Variable Value   ${timeandlocale}   &{EMPTY}
    Pass Execution If   ${timeandlocale} == &{EMPTY}   Skipping time and locale, variable is not defined in data file.
    ${resp} =   Fusion Api Configure Appliance Time and Locale   ${timeandlocale}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=200s   interval=5s
    Asynchronous Task Should Be Successful   ${task}

Update Reserved Vlan Id Range
    [Documentation]  Update reserved vlan id range for the fabric.
    [Tags]   CONFIGURE   RESERVED_VLANID
    ${reserved_vlan} =   Get Variable Value   ${reserved_vlan}
    Run Keyword If   ${reserved_vlan} is not ${null}   Update Reserved Vlan Id Range   ${reserved_vlan}
    ...       ELSE   Log   reserved_vlan not defined. Skipping update reserved vlan id range for fabric...   WARN   console=${True}

Add IPv4 Subnets And Ranges
    [Tags]   CONFIGURE   IPV4_SUBNETS_RANGES
    ${ipv4_subnets} =   Get Variable Value   ${ipv4_subnets} 
    Pass Execution If   ${ipv4_subnets} is ${null}   Skipping add IPv4 subnets due to undefined ipv4_subnets variable.
    Create ID Pools IPv4 Subnet   ${ipv4_subnets}
    ${ipv4_ranges} =   Get Variable Value   ${ipv4_ranges} 
    Pass Execution If   ${ipv4_ranges} is ${null}   Skipping add IPv4 ranges due to undefined ipv4_ranges variable.
    Create ID Pools IPv4 Ranges   ${ipv4_ranges}

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

Add Ethernet Networks In Bulk
    [Documentation]   Bulk create ethernet networks from data variable file.
    [Tags]   CONFIGURE   ETHERNET_BULK
    ${bulk_ethernet_network} =   Get Variable Value   ${bulk_ethernet_network}
    Pass Execution If   ${bulk_ethernet_network} is ${null}   Skipping create ethernet bulk networks due to bulk_ethernet_network being NoneType.
    :FOR   ${b}   IN    @{bulk_ethernet_network}
    \    ${resp}     Fusion Api Create Ethernet Bulk Networks   ${b}
    \    Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=60m   interval=5s
    \    Asynchronous Task Should Be Successful   ${task}   checkAssociatedResourceUri=${False}

Add Network Sets
    [Documentation]   Add network sets from data variable file.
    [Tags]    CONFIGURE   NS
    ${network_sets} =	Get Variable Value	${network_sets}
    Run Keyword If   ${network_sets} is ${null}    Fail   msg=network_sets variable is ${null}. Please check your data variable file.
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
	Run Keyword If	${ligs} is ${null}   Fail   msg=ligs variable is ${null}. Please check your data variable file.
        ${l} =   Get Length   ${ligs}
	:FOR   ${x}   IN RANGE   0   ${l}
        \   ${body} =   Build LIG body   ${ligs[${x}]}
        \   ${resp} =   Fusion Api Create LIG   ${body}
        \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}    timeout=${LIG_ADD_WAIT_TIMEOUT}    interval=${LIG_ADD_WAIT_INTERVAL}
        \   Asynchronous Task Should Be Successful   ${task}

Add Enclosure Groups
 	[Tags]    CONFIGURE   ENCLOSURE_GROUPS  EGS
 	${enc_groups} =	Get Variable Value	${enc_groups}
	Run Keyword If	${enc_groups} is ${null}   Fail   msg=enc_groups variable is ${null}. Please check your data variable file.
        ${l} =   Get Length   ${enc_groups}
	:FOR   ${x}   IN RANGE   0   ${l}
	\   ${resp} =   Add Enclosure Group from variable   ${enc_groups[${x}]}
	\   Request Should Be Successful   ${resp}

Add Licenses
    [Documentation]   Add licenses to OneView from data variabl file. Warn user for error.
    [Tags]   CONFIGURE   LICENSES
    ${licenses} =   Get Variable Value   ${licenses}
    Run Keyword If   ${licenses} is not ${null}   	Add Licenses from variable   ${licenses}

Add Logical Enclosures
    [Tags]    CONFIGURE   MINIMAL   LOGICAL_ENCLOSURES    LES   Performance   logical_enclosures-condition-CIFIT_5MECL10
    ${les} =	Get Variable Value	${les}
    Run Keyword If   ${les} is ${null}    Fail   msg=les variable is ${null}. Please check your data variable file.
    ${l} =   Get Length   ${les}
    :FOR   ${x}   IN RANGE   0   ${l}
    \   ${task} =   Add Logical Enclosure from variable   ${les[${x}]}   timeout=${LE_ADD_WAIT_TIMEOUT}   interval=${LE_ADD_WAIT_INTERVAL}
    \   Asynchronous Task Should Be Successful   ${task}

Add Ranges
    [Documentation]   Disable all generated address and id ranges and add custom ranges from data variable file. Warn users on errors.
    [Tags]   CONFIGURE   RANGES   PROFILES
    stackingDomainMAC Should Exist In Nitro LI
    ${ranges} =	  Get Variable Value   ${ranges}
    ${pools} =   Run Keyword If   ${ranges} is not ${null}   Create List   /rest/id-pools/vmac   /rest/id-pools/vwwn   /rest/id-pools/vsn
    Run Keyword If   ${ranges} is not ${null}   Run Keyword for List   ${pools}   common.Disable ALL Generated ID Ranges
    Run Keyword If   ${ranges} is not ${null}   Add Ranges From variable   ${ranges}
    Ranges Should Exist In OneView   ${ranges}   ${RANGES_CAT_URIS}

Power Off Servers
    [Documentation]   Poweroff servers.
    [Tags]   CONFIGURE   POWER_OFF_SERVERS
    Power Off All Servers In Parallel

Add Server Profile Templates
    [Documentation]   Add server profile templates from variable.
    [Tags]   CONFIGURE   SERVER_PROFILE_TEMPLATES   SPTS
    stackingDomainMAC Should Exist In Nitro LI
    ${ranges} =	  Get Variable Value   ${ranges}
    ${server_profile_templates} =   Get Variable Value   ${server_profile_templates}
    Run Keyword If   ${server_profile_templates} is not ${null}   Run Keywords   Ranges Should Exist In OneView   ${ranges}   ${RANGES_CAT_URIS}   AND   common.Add Server Profile Templates From Variable   ${server_profile_templates}   connectionSettingsApi=${500}

Add Server Profiles Using Templates
    [Documentation]   Add server profiles using templates from variable.
    [Tags]   CONFIGURE   SERVER_PROFILES_TEMPLATE   SPST
    stackingDomainMAC Should Exist In Nitro LI
    ${ranges} =	  Get Variable Value   ${ranges}
    ${server_profiles_using_template} =   Get Variable Value   ${server_profiles_using_template}
    Run Keyword If   ${server_profiles_using_template} is not ${null}   Run Keywords   Ranges Should Exist In OneView   ${ranges}   ${RANGES_CAT_URIS}   AND   Add Server Profiles Using Template From Variable   ${server_profiles_using_template}   ${server_profile_to_bay_map}   waitTime=${SPST_WAIT_TIMEOUT}   interval=${SPST_WAIT_INTERVAL}   connectionSettingsApi=${600}

Add Server Profiles No Hardware Assigned
    [Documentation]   Create server profiles from variable without assigning to server hardware.
    [Tags]   CONFIGURE   PROFILES   SERVER_PROFILES   SERVER_PROFILES_NO_HW   SPSNOHW   Performance   server_profiles-condition-CIFIT_5MECL10
    stackingDomainMAC Should Exist In Nitro LI
    ${ranges} =	  Get Variable Value   ${ranges}
    ${server_profiles} =   Get Variable Value   ${server_profiles_nohw}
    Run Keyword If   ${server_profiles} is not ${null}   Run Keywords   Ranges Should Exist In OneView   ${ranges}   ${RANGES_CAT_URIS}   AND   Add Unassigned Server Profiles   ${server_profiles}   ${server_profile_to_bay_map}   waitTime=${PROFILE_CREATION_WAIT_TIMEOUT}   interval=${PROFILE_CREATION_WAIT_INTERVAL}

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

#[JMP] - Marking this out now that we have create profile+assign hw
Add Server Profiles
#	[Tags]    PROFILES   SERVER_PROFILES    SPS
#       stackingDomainMAC Should Exist In Nitro LI
#       ${ranges} =	  Get Variable Value   ${ranges}
# 	${server_profiles} =	Get Variable Value	${server_profiles}
# 	Run Keyword If	${server_profiles} is not ${null}		Run Keywords   Ranges Should Exist In OneView   ${ranges}   ${RANGES_CAT_URIS}   AND   Add Server Profiles from variable	${server_profiles}   forceProfileApply=${FORCE_PROFILE_APPLY}   timeout=30m

Assign Server Hardware To Profile
	[Tags]	CONFIGURE   MINIMAL   PROFILES   SERVER_PROFILES   ASSIGN_HARDWARE   Performance   server_profiles-condition-CIFIT_5MECL10
	${server_profiles} =   Get Variable Value   ${server_profiles_nohw}
	Log   \n\nAssigning Server Hardware to Profiles   console=${True}
 	Run Keyword If	${server_profiles} is not ${null}		common.Assign Server Hardware To Existing Profiles From Variable	${server_profiles}   ${server_profile_to_bay_map}   timeout=${PROFILE_ASSIGN_WAIT_TIMEOUT}   interval=${PROFILE_ASSIGN_WAIT_INTERVAL}   waitForTask=${True}   forceProfileApply=${FORCE_PROFILE_APPLY}   throttle=${PROFILE_THROTTLE}

Add Fabric Manager From Variable
    [Tags]   CONFIGURE   FABRIC_MANAGERS
    ${fabric_manager} =   Get Variable Value   ${fabric_manager}
    ${apic_certificate} =   Get Variable Value   ${apic_certificate}
    Pass Execution If   ${fabric_manager} is ${null}   Skipping add fabric manager due to missing fabric_manager variable.
    Pass Execution If   ${apic_certificate} is ${null}   Skipping add fabric manager due to missing apic_certificate variable.
    Add Fabric Manager   ${fabric_manager}   ${apic_certificate}

Add Tenant To Fabric Manager From Variable
    [Tags]   CONFIGURE   TENANTS
    ${tenants} =   Get Variable Value   ${tenants}
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

Add Repository
    [Documentation]    Add repository from the data variable file.
    [Tags]    CONFIGURE   REPO
	Pass Execution If   "${REPOSITORY_WEBADDRESS}"=="None"   Did not find any webaddress.
    ${Repository_body}    Create Dictionary    repositoryName=${REPOSITORY_NAME}
	...										   userName=${REPOSITORY_USERNAME}
	...									       password=${REPOSITORY_PASSWORD}
	...									       repositoryURI=${REPOSITORY_WEBADDRESS}
	${resp} =    Fusion Api Add repository    ${Repository_body}
	${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   ${ADD_REPOSITORY_TIMEOUT}   ${ADD_REPOSITORY_INTERVAL}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task}

Change Network Bandwidth Through ConnectionTemplate
    [Documentation]  Changing networks bandwidth through connection template.
	[Tags]    CONFIGURE   CONNECTION_TEMPLATE
    Pass Execution If    ${NETWORK_RANGE_TO_EDIT_BANDWIDTH}==${None}   Please define NETWORK_RANGE_TO_EDIT_BANDWIDTH variable in your data file if needed. For example, please refer to tests/wpst_crm/ci_fit/tests/configure_appliance/example_data_variables.py.
    Run Keyword for List  	${NETWORK_RANGE_TO_EDIT_BANDWIDTH}    Change Bandwidth For Range Of Networks

Add Logical Switch Group
    [Documentation]   Add LSG to OneView
    [Tags]   CONFIGURE   LSGS   LSGS_LSS
    ${lsgs} =   Get Variable Value   ${lsgs}   @{EMPTY}
    Pass Execution If   ${lsgs} == @{EMPTY}   Skipping add logical switch group, variable is not defined in data file.
    :FOR   ${lsg}   IN   @{lsgs}
    \   ${task} =   Add Logical Switch Group From Variable   ${lsg}
    \   Asynchronous Task Should Be Successful   ${task}

Add Logical Switches
    [Documentation]   Add Logical Switches to OneView
    [Tags]   CONFIGURE   LSS   LSGS_LSS
    ${lss} =   Get Variable Value   ${lss}   @{EMPTY}
    Pass Execution If   ${lss} == @{EMPTY}   Skipping add logical switches, variable is not defined in data file.
    :FOR   ${ls}   IN   @{lss}
    \   ${task} =   Add Logical Switch From Variable   ${ls}   timeout=${ADD_LOGICAL_SWITCHES_TIMEOUT}
    \   Asynchronous Task Should Be Successful   ${task}



# SAN Managers
# Storage Systems
# Storage Pools
# Volumes
# Volume Templates


*** Keywords ***
# -----------------------------------------------------------------------------
#   Tbird Hardware Setup
# -----------------------------------------------------------------------------
Invoke Hardware Setup
    [Documentation]  SSH to the Tbird appliance and invoke hardware setup via REST, only on Tbird platform
    ...              Example:
    ...                Invoke Hardware Setup
    ...                Invoke Hardware Setup  timeout=60  interval=2
    ...                Invoke Hardware Setup  api=300 timeout=60  interval=5
    ...              Data Varables Required:
    ...                ${X-API-VERSION}              300              # X-API-VERSION
    ...                ${FUSION_IP}                  ${APPLIANCE_IP}  # Fusion Appliance IP
    ...                ${FUSION_SSH_USERNAME}        root             # Fusion SSH Username
    ...                ${FUSION_SSH_PASSWORD}        hponeview        # Fusion SSH Password
    ...                ${FUSION_PROMPT}              \#               # Fusion Appliance Prompt
    ...
    [Arguments]  ${api}=${X-API-VERSION}  ${timeout}=60  ${interval}=5
    Log   \n\n[Invoking Hardware Setup]   console=${True}
    Login to Fusion via SSH
    Log   \nX-API-Version: ${api}   console=${True}
    ${output} =   Execute SSH Command     curl -k -X POST -H "X-API-Version:${api}" https://localhost/rest/appliance/tech-setup
    ${resp} =   Get Task By Param   param=?filter='name'='Discover hardware'&sort=created:descending&count=1
    Log   \nDiscovering Hardware...  console=${True}
    ${valDict} =   Create Dictionary   taskState=Completed
    Set Suite Variable   ${forkedErrorFound}   ${False}
    common.Wait For Forked Tasks   ${resp['members']}   ${valDict}   ${timeout}   interval=${interval}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=Not all forked tasks state finished with Completed.

Get Task By Param
        [Documentation]    Get task by param
        ...    Examples:
        ...    Get Task By Param param=?filter='name'=='Discover hardware'&sort=created:descending&count=1
        ...    Get Task By Param param=?filter="'name'='Add' AND associatedResource.resourceName='${name}'"&sort=created:descending&count=1
        [Arguments]    ${param}
        ${resp}=    Fusion Api Get Task    param=${param}
        Log   ${resp}   TRACE   console=${True}
        ${status} =    Run keyword and return status    Dictionary should contain key    ${resp}    'errorCode'
        Return from keyword if    ${status}==${True}    ${resp}
        ${count} =    Get From Dictionary    ${resp}    count
        Return from keyword if    ${count}==0    ${resp}
        [Return]    ${resp}

####### Modify Server Profile Test
Modify Server Profile
    [Documentation]   Edit server profile based on a given request body.
    [Arguments]    ${SP}   ${forceProfileApply}=false
    ${param} =   Run Keyword If   '${forceProfileApply}' != 'false'   Set Variable   ?force="${forceProfileApply}"
    ...                    ELSE   Set Variable   ${EMPTY}
    Log Dictionary    ${SP}
    ${Response} =    Fusion API Edit Server Profile    ${SP}    ${SP['uri']}   param=${param}
    Should Be Equal as Strings   ${Response['status_code']}   202   msg=Failed to initiate Edit SP.
    ${Retry Interval}    Convert To Number     60
    ${Retries}           Convert To Integer    15
    ${Response} =   Fusion API Wait For Task To Complete   ${Response['uri']}   sleep_time=${Retry Interval}   retries=${Retries}
    ${Errors} =   Get From Dictionary   ${Response}   taskErrors
    ${Errors} =   Get Length   ${Errors}
    Run Keyword If   ${Errors} != 0
    ...    Log    Errors encountered while creating Server Profile.   level=WARN
    [Return]    ${Response}

Rename Enclosures From Variable
    [Documentation]   Rename enclosures defined in a dictionary of old:new names.
    [Arguments]   ${enc_names}
    ${body} =   Create List
    ${headers} =   Create Dictionary   If-Match=*   Content-Type=application/json   X-Api-Version=${X-API-VERSION}
    :FOR   ${key}   IN   @{enc_names.keys()}
    \   ${resp} =   Fusion Api Get Enclosures   param=?filter="name='${key}'"
    \   Continue For Loop If   ${resp['members']} == @{EMPTY}
    \   ${request} =   Create Dictionary   op=replace   path=/name   value=${enc_names['${key}']}
    \   Append To List   ${body}   ${request}
    \   ${resp} =   Fusion Api Patch Enclosure   ${body}   ${resp['members'][0]['uri']}   headers=${headers}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=200s   interval=5s
    \   Asynchronous Task Should Be Successful   ${task}
    \   ${body} =   Create List

Change Bandwidth For Range Of Networks
    [Documentation]    Changing bandwidth for range of networks through connection template.
    [Arguments]   ${range}
    :FOR   ${x}   IN RANGE   ${range['start']}   ${range['end']}+1
    \    ${resp}    Fusion Api Get Resource     /rest/${range['type']}-networks?filter=name='${range['prefix']}${x}${range['suffix']}'
    \    ${Conn_Temp_Uri}    Get From Dictionary    ${resp['members'][0]}    connectionTemplateUri
    \    ${ConnectionTemplate}    Fusion Api Get Connection Templates     uri=${Conn_Temp_Uri}
    \    ${typical_band_width}     Get From Dictionary    ${ConnectionTemplate['bandwidth']}   typicalBandwidth
    \    ${max_band_width}    Get From Dictionary    ${ConnectionTemplate['bandwidth']}    maximumBandwidth
    \    Run Keyword If    ${range['User_typical_bandwidth']} != None and ${range['User_typical_bandwidth']} < ${max_band_width}    Set To Dictionary    ${ConnectionTemplate['bandwidth']}    typicalBandwidth    ${range['User_typical_bandwidth']}
    \    Run Keyword If    ${range['User_max_bandwidth']} != None   Set To Dictionary   ${ConnectionTemplate['bandwidth']}    maximumBandwidth     ${range['User_max_bandwidth']}
    \    Run keyword if    ${ConnectionTemplate['bandwidth']} != ${None}
    \    ...                 Remove From Dictionary      ${ConnectionTemplate}   headers     category   created   status_code   state   modified   description
    \    ${resp}     Fusion Api Update Connection Template   body=${ConnectionTemplate}   uri=${Conn_Temp_Uri}
    \    ${statusCode} =   Check Response For Error   ${resp}
    \    Run Keyword If   ${statusCode} != ${200}   Fail   msg= task returned status code ${resp['status_code']}.
