*** Settings ***
Library             Collections
Library             json
Library             DateTime
Library             OperatingSystem
Library             String
Library             FusionLibrary
Library             RoboGalaxyLibrary
Resource            ../../../Resources/api/fusion_api_resource.txt

*** Keywords ***
Esxi Autodeploy Suite Setup
    [Documentation]         Set log level to trace and login to Oneview
    [Arguments]        ${ip}    ${credentials}
    Set Log Level    Trace
    Fusion Api Login Appliance    ${ip}    ${credentials}

Get Server Hardware by Name
    [Documentation]        Finds and returns the server hardware by name
    [Arguments]        ${sh}
    ${sh_raw}=    Fusion API Get Server Hardware    param=?filter="name='${sh}'"
    [Return]  ${sh_raw['members'][0]}

Set One Time Boot
    [Documentation]        sets the one time boot on the list of server hardwares
    [Arguments]        ${sh_list}   ${boot_option}
    :FOR  ${sh}  IN  @{sh_list}
    \    ${hw} =  Get Server Hardware by Name   ${sh}
    \    ${dict} =  Create Dictionary  op=replace  path=/oneTimeBoot   value=${boot_option}
    \    ${payload} =  Create List  ${dict}
    \    ${resp} =  fusion api patch server hardware  ${payload}  ${hw['uri']}

Generate profile connection settings
    [Documentation]       Generates and returns the connection settings payload for Server Profile Creation
    [Arguments]        ${data}
    ${connections} =    Get From Dictionary    ${data['connectionSettings']}  connections
    ${connection_list} =    create list
    :FOR    ${connection}    IN    @{connections}
    \       ${temp_dict} =      Copy Dictionary     ${connection}
    \       ${type} =   Get From Dictionary     ${connection}   functionType
    \       ${nw} =        Run Keyword If  '${type}' == 'Ethernet'
    \       ...               Fusion Api Get Ethernet Networks    param=?filter="'name'=='${connection["networkUri"]}'"
    \       ...          ELSE IF         '${type}' == 'FibreChannel'
    \       ...               Fusion Api Get FC Networks        param=?filter="'name'=='${connection["networkUri"]}'"
    \       ...          ELSE IF         '${type}' == 'FCOE'
    \       ...               Fusion Api Get FCoE Networks    param=?filter="'name'=='${connection["networkUri"]}'"
    \       ...          ELSE            Log     Invalid network type specified     WARN
    \       ${nw_uri} =     Get From Dictionary        ${nw['members'][0]}    uri
    \       Set to Dictionary   ${temp_dict}    networkUri=${nw_uri}
    \       Append to list  ${connection_list}  ${temp_dict}
    ${connection_settings} =    Create Dictionary   connections=${connection_list}
    [Return]   ${connection_settings}

Get All Types Of Ethernet Networks
    [Documentation]  Gets the etnernet and netset networks
    [Arguments]    ${network_name}
    ${ethernet_network}=    Fusion Api Get Ethernet Networks    param=?filter="'name'=='${network_name}'"
    ${ethernet_network}=    Run Keyword If    '${ethernet_network['count']}' == '0'    Fusion Api Get Network Set    param=?filter="'name'=='${network_name}'"
    [Return]    ${ethernet_network}

Generate server profile payload
    [Documentation]       Generate and return the Server Profile Payload
    [Arguments]        ${sh_data}      ${payload_template}

    ${sp_payload}=    Copy Dictionary        ${payload_template}

    Set to Dictionary    ${sp_payload}    serverHardwareUri=${sh_data['uri']}
        ...    serverHardwareTypeUri=${sh_data['serverHardwareTypeUri']}
        ...    enclosureGroupUri=${sh_data['serverGroupUri']}

    ${sp_name} =   Remove String    ${sh_data['name']}  ,
    ${sp_name} =    catenate    SEPARATOR=-     SP     ${sp_name.replace(" ", "-")}
    Set to Dictionary    ${sp_payload}     name     ${sp_name}

    ${connection_settings} =    Generate profile connection settings     ${sp_payload}
    Set to Dictionary    ${sp_payload}    connectionSettings    ${connection_settings}
    [Return]   ${sp_payload}

Power On Servers
    [Documentation]        Power On Servers given server profiles
    [Arguments]    ${server_profiles}
    :FOR    ${server_profile}    IN    @{server_profiles}
    \    ${sh_uri} =    Get From Dictionary    ${server_profile}    serverHardwareUri
    \    Run Keyword    Power On Server By Uri    ${sh_uri}

Delete Server Profile
    [Documentation]    Delete Server Profile
    [Arguments]        ${uri}
    ${resp}=    Fusion Api Delete Server Profile    uri=${uri}    param=?force=true
    ${task} =   Wait For Task   ${resp}     200s    10s
    Should Be Equal As Integers    ${resp['status_code']}   202   msg=Could not delete Server profile!


Create Server Profiles
    [Documentation]    Creates Server Profiles based on the Profile template created for autodeploy and
    ...    list of names of server hardwares
    [Arguments]        ${sp_template}    ${blades}
    ${sp_list} =    create list
    ${resp_list} =    create list
    :FOR    ${blade}    IN    @{blades}
    \     ${hw_data}=   Get Server Hardware by Name    ${blade}
    \     ${server_power_state} =     Get from Dictionary     ${hw_data}      powerState
    \     Run Keyword If    '${server_power_state}' != 'Off'    Power Off Server    ${blade}   PressAndHold
    \     Run Keyword If    '${hw_data['serverProfileUri']}' != 'None'    Run Keywords
    \           ...    Log  \nDeleting existing Server Profile for ${blade}    console=True  AND
    \           ...    Delete Server Profile    ${hw_data['serverProfileUri']}
    \     Log  \nGenerating SP Payload for ${blade}..   console=True
    \     ${payload}=    Generate server profile payload  ${hw_data}    ${sp_template}
    \     Log  \n\nCreating New Server Profile for ${blade}...   console=True
    \     ${response}=    Fusion API Create Server Profile    body=${payload}   param=?force=ignoreServerHealth
    \     Should Be Equal as Strings    ${response['status_code']}    202      msg=Failed to create SP
    \     continue for loop if  ${response['status_code']}!=202
    \     Append to list    ${resp_list}   ${response}
    \     Append to list  ${sp_list}  ${payload['name']}
    [Return]   ${resp_list}    ${sp_list}

Get SP Item List
    [Documentation]    Get Server Profiles Item List
    [Arguments]        ${sp_name}    ${item}
    ${item_list} =     create List
    :FOR    ${sp}    IN    @{sp_list}
    \     ${sp_data}=   Fusion Api Get Server Profiles    param=?filter="'name'=='${sp_name}'"
    \     ${value} =     Get From Dictionary        ${sp_data['members'][0]}    ${item}
    \     append to list    ${item_list}   ${value}
    [Return]    ${item_list}

Add Autodeploy Rules
    [Documentation]    Set autodeploy rules based on serial numbers
    [Arguments]        ${sp_list}   ${ad_configs}
    ${vcenter_config} =   copy dictionary   ${ad_configs['deployment_vc']}
    ${esxi_configs} =   copy dictionary   ${ad_configs['esxi_config']}
    ${cmd} =  Catenate  powershell.exe -ExecutionPolicy Bypass -file ${ad_configs['add_rule']} ${vcenter_config['vc']}
    ...     ${vcenter_config['user']}  ${vcenter_config['password']} ${esxi_configs['image']} ${esxi_configs['profile']}
    ...     ${esxi_configs['depot_path']} ${vcenter_config['datacenter']}
    :FOR    ${sp}    IN    @{sp_list}
    \     Log  \nAdding AutoDeploy Rules for ${sp['name']}\n   console=True
    \     ${rc}   ${Output}=   Run and return RC and output   ${cmd} ${sp['name']} ${sp['serialNumber']}
    \     Run Keyword If  ${rc} != 0   Log \nFailed to add rule\n ${output}

Delete Autodeploy Rules
    [Documentation]    Delete autodeploy rules
    [Arguments]        ${sp_list}   ${ad_configs}
    ${vcenter_config} =   copy dictionary   ${ad_configs['deployment_vc']}
    ${cmd} =  Catenate  powershell.exe -ExecutionPolicy Bypass -file ${ad_configs['remove_rule']} ${vcenter_config['vc']}
    ...     ${vcenter_config['user']}  ${vcenter_config['password']}
    :FOR    ${sp}    IN    @{sp_list}
    \     Log  \nDeleting AutoDeploy Rule for ${sp}   console=True
    \    ${rc}   ${Output}=   Run and return RC and output    ${cmd} ${sp}
    \     Run Keyword If  ${rc} != 0   Log \nFailed to delete rule\n ${output}

Generate Server Profile List
    [Documentation]    Get UUID And Serial From Server Profiles
    [Arguments]        ${sp_list}
    ${server_profiles} =     create List
    :FOR    ${sp}    IN    @{sp_list}
    \    ${sp_data}=   Fusion Api Get Server Profiles    param=?filter="'name'=='${sp}'"
    \    ${sp_members} =     Get From Dictionary    ${sp_data}   members
    \    ${sh} =    Get From List    ${sp_members}    0
    \    &{dict} =   Create Dictionary  name=${sh['name']}   uri=${sh['uri']}   uuid=${sh['uuid']}
    \       ...     serialNumber=${sh['serialNumber']}    serverHardwareUri=${sh['serverHardwareUri']}
    \    append to list    ${server_profiles}   ${dict}
    [Return]   ${server_profiles}

Get Host name by uuid
    [Documentation]     Get Host name by uuid
    [Arguments]   ${host_list}      ${uuid}
    ${host_ip} =   Set Variable      ${EMPTY}
    :FOR   ${host}  IN   @{host_list}
    \      Run Keyword If   '${host['uuid']}' == '${uuid}'   Run Keywords
    \       ...   Set Test Variable    ${host_ip}   ${host['host']}   AND
    \       ...   Exit For Loop
    Log  \nHost IP: ${host_ip}     console=True
    [Return]    ${host_ip}

Get Deployed Hosts From Vcenter
    [Documentation]        Gets the list of deployed hosts from the vcenter and filter based on the UUID
    [Arguments]   ${sp_list}  ${vcenter_config}
    Log  \n\nRetreiving deployed hosts from vcenter:   console=True
    ${filtered_hosts} =  create list
    Connect To VI Server   ${vcenter_config['vc']}  ${vcenter_config['user']}   ${vcenter_config['password']}
    ${hosts_in_vc} =   get all hosts and uuid
    Log  \nHosts in vCenter: ${hosts_in_vc}    console=True
    :For  ${sp}   IN   @{sp_list}
    \      ${host} =    Get Host name by uuid   ${hosts_in_vc}    ${sp['uuid']}
    \      Run Keyword If    '${host}' == ''   Log  \nHost not found in vCenter: ${sp['name']}, ${sp['uuid']}   console=True
    \      ...    ELSE    append to list   ${filtered_hosts}     ${host}
    Disconnect from VI Server
    Log  \n Hosts Found based on uuid : ${filtered_hosts}    console=True
    [Return]    ${filtered_hosts}

Get Deployed Hosts From Vcenter using find by uuid
    [Documentation]        Get Deployed Hosts From Vcenter based on the uuid
    [Arguments]   ${sp_list}   ${vcenter_config}
    Log  \n\nRetreiving deployed hosts from vcenter:   console=True
    ${hosts} =  create list
    Connect To VI Server   ${vcenter_config['vc']}  ${vcenter_config['user']}   ${vcenter_config['password']}
    :For  ${sp}   IN   @{sp_list}
    \      ${sp_uuid} =     Convert To String     ${sp['uuid']}
    \      ${host} =     find host by uuid   ${sp_uuid}
    \      append to list   ${hosts}     ${host}
    Disconnect from VI Server
    Log  \nHosts found: ${hosts}    console=True
    [Return]    ${hosts}

Remove Deployed Hosts From Deployment Vcenter
    [Documentation]        Remove hosts from the deployment vCenter
    [Arguments]   ${hosts}  ${vcenter_config}
    Connect To VI Server   ${vcenter_config['vc']}  ${vcenter_config['user']}   ${vcenter_config['password']}
    :FOR  ${host}   IN   @{hosts}
    \     Log  \nRemoving host ${host} from vcenter   console=True
    \     ${output} =     remove host from Datacenter   ${vcenter_config['datacenter']}   ${host}
    \     Log  ${output}    console=True
    Disconnect from VI Server

Login to Host via SSH
    [Documentation]    Login to host via SSH
    [Arguments]    ${ip}    ${user}     ${password}
    #Sleep     3m
    ${Id} =    Open Connection    ${ip}
    ${Output} =    Login    ${user}    ${password}
    [Return]    ${Id}

Logout of Host Via SSH
    [Documentation]    Logout of Host Via SSH
    Close Connection

Get Available IP
    [Documentation]        From list of IP Adresses, returns the first IP that is available (non pingable)
    [Arguments]        ${ips}
    :For    ${ip}   IN    @{ips}
    \       ${rc}   ${Output}=   Run and return RC and output   ping ${ip} -w 100
    \       Run keyword if     '${rc}' == '0'   continue for loop
    \       ...    ELSE      Run Keywords       Set Test Variable  ${available_ip}    ${ip}   AND   Exit For Loop
    Log    \nAvailable IP:${available_ip}       console=True
    [Return]  ${available_ip}

Configure Management Networking on ESXi
    [Documentation]        Reconfigures the esxi networking to use the management network
    ...   returns list of the configured management IP Addresses
    [Arguments]        ${hosts}   ${host_config}   ${net}   ${nic}

    ${configured_ips} =    create list
    :FOR    ${host}  IN    @{hosts}
    \   ${ip} =     Get Available IP    ${net['ips']}
    \   ${sf} =     Fetch From Right    ${ip}   .
    \   Log  \nReconfiguring Networking for host: ${host}      console=True
    \   Login to Host via SSH   ${host}   ${host_config['user']}   ${host_config['password']}
    \   Execute Command   esxcli system hostname set --host=host${sf}
    \   Execute Command   esxcli system hostname set --domain lab.local
    \   Execute Command   esxcli network vswitch standard add -v mgmt_vswitch
    \   Execute Command   esxcli network vswitch standard uplink add -u ${nic} -v mgmt_vswitch
    \   Execute Command   esxcli network vswitch standard policy failover set -a ${nic} -v mgmt_vswitch
    \   Execute Command   esxcli network vswitch standard portgroup add -p mgmt_pg -v mgmt_vswitch
    \   Execute Command   esxcli network ip interface add --interface-name=vmk1 --portgroup-name=mgmt_pg
    \   Execute Command   esxcli network ip interface tag add --interface-name=vmk1 --tagname=Management
    \   ${ip_set_cmd} =  Catenate  esxcli network ip interface ipv4 set -i vmk1 -I ${ip} -N ${net['netmask']}
    \   ...    -g ${net['gw']} -t static
    \   Execute Command   ${ip_set_cmd}
    \   Logout of Host Via SSH
    \   append to list   ${configured_ips}    ${ip}
    [Return]    ${configured_ips}

Configure IPv6 Management Networking on ESXi
    [Documentation]        Reconfigures the esxi networking to use the ipv6 management network
    ...   returns list of the configured management IP Addresses
    [Arguments]        ${hosts}   ${host_config}   ${net}   ${nic}

    ${configured_ips} =    create list
    :FOR    ${host}  IN    @{hosts}
    \   ${ip} =     Get Available IP    ${net['ips']}
    \   ${sf} =     Fetch From Right    ${ip}   :
    \   Log  \nReconfiguring Networking for host: ${host}      console=True
    \   Login to Host via SSH   ${host}   ${host_config['user']}   ${host_config['password']}
    \   Execute Command   esxcli system hostname set --host=host${sf}
    \   Execute Command   esxcli system hostname set --domain lab.local
    \   Execute Command   esxcli network vswitch standard add -v mgmt_vswitch
    \   Execute Command   esxcli network vswitch standard uplink add -u ${nic} -v mgmt_vswitch
    \   Execute Command   esxcli network vswitch standard policy failover set -a ${nic} -v mgmt_vswitch
    \   Execute Command   esxcli network vswitch standard portgroup add -p mgmt_pg -v mgmt_vswitch
    \   Execute Command   esxcli network ip interface add --interface-name=vmk1 --portgroup-name=mgmt_pg
    \   Execute Command   esxcli network ip interface tag add --interface-name=vmk1 --tagname=Management
    \   Execute Command   esxcli network ip interface ipv6 address add -i vmk1 -I ${ip}/${net['netmask']}
    \   Logout of Host Via SSH
    \   append to list   ${configured_ips}    ${ip}
    [Return]    ${configured_ips}

Remove deployment networking
    [Documentation]        Removes the deployment networking from the host
    [Arguments]        ${hosts}  ${host_config}
    :FOR    ${host}  IN    @{hosts}
    \   Log  \nRemoving deployment network on host: ${host}      console=True
    \   Login to Host via SSH   ${host}   ${host_config['user']}   ${host_config['password']}
    \   Execute Command   esxcli network ip interface remove --interface-name=vmk0
    \   Execute Command   esxcli network vswitch standard remove --vswitch-name=vSwitch0
    \   Execute Command   echo completed execution!
    \   Logout of Host Via SSH

Create Target Cluster
    [Documentation]        Creates the cluster in the given datacenter if not already created
    [Arguments]     ${vcenter_config}
    Connect To VI Server   ${vcenter_config['vc']}  ${vcenter_config['user']}   ${vcenter_config['password']}
    Log  \nCreating cluster: ${vcenter_config['cluster']} in DC: ${vcenter_config['datacenter']}     console=True
    ${resp} =   Run Keyword And Ignore Error  RoboGalaxyLibrary.create cluster  ${vcenter_config['cluster']}   ${vcenter_config['datacenter']}
    Log  \n Response: ${resp}

Add Hosts to Target VCenter
    [Documentation]        adds the given hosts to cluster
    [Arguments]     ${hosts}   ${vcenter_config}  ${host_config}
    Connect To VI Server   ${vcenter_config['vc']}  ${vcenter_config['user']}   ${vcenter_config['password']}
    :FOR  ${host}   IN   @{hosts}
    \    Log  \nAdding host: ${host} to cluster: ${vcenter_config['cluster']}     console=True
    \    ${thumbprint}=        get host ssl thumbprint  ${host}
    \    ${response}=    Add Host To Datacenter Cluster     ${host}   ${thumbprint}   ${vcenter_config['datacenter']}
    \   ...    ${vcenter_config['cluster']}   ${host_config['user']}    ${host_config['password']}
    Disconnect from VI Server