*** Settings ***
Library                         FusionLibrary
Resource                        ../../../../Resources/api/fusion_api_resource.txt
Resource                        ../../support_files/clrm_common.txt
Resource                        ../../esxi_autodeploy/resource.robot
Resource                        ../SPT/resource.txt
Variables                       data_variables_ovf1024_Synergy.py

*** Keywords ***
Login to Appliance and Set Trace
    [Documentation]         Set log level to trace and login to Oneview
    [Arguments]        ${ip}    ${credentials}
    Set Log Level    Trace
    Fusion Api Login Appliance    ${ip}    ${credentials}

Create Prerequisties for Import
    [Documentation]     Creates the cluster and adds the host to vcenter
    [Arguments]    ${profiles}    ${server_hardware_list}    ${vcenter_details}    ${cluster_name}    ${enclosure_type}   ${deploy_configs}    ${mgmt_net}   ${mgmt_nic}
    Set Log Level    Trace
    Fusion Api Login Appliance  ${OV_IP}     ${OV_credentials}
    ${configured_mgmt_ips}=    run keyword if    '${enclosure_type}' == 'C7K'      Create Prerequisites for C7K Import    ${profiles}    ${server_hardware_list}   ${deploy_configs}  ${mgmt_net}   ${mgmt_nic}
        ...    ELSE IF   '${enclosure_type}' == 'Synergy'      Create Prerequisites for I3S Import    ${profiles}    ${server_hardware_list}
        ...    ELSE       Fatal Error     msg=Enclosure Type Not defined
    Set To Dictionary    ${vcenter_details}    cluster    ${cluster_name}
    Create Target Cluster    ${vcenter_details}
    run keyword if    '${enclosure_type}' == 'Synergy'      Add Hosts to Target VCenter    ${configured_mgmt_ips}   ${vcenter_details}  ${deploy_configs}
    ...    ELSE    Add Hosts to Target VCenter    ${configured_mgmt_ips}   ${vcenter_details}  ${deploy_configs['esxi_config']}
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be present in CLRM    ${cluster_name}

Test Setup to Add Hosts in Datacenter
    [Documentation]    Add Hosts in a different datacenter than the cluster
    [Arguments]    ${profiles}    ${server_hardware_list}    ${vcenter_details}    ${cluster_name}    ${enclosure_type}   ${deploy_configs}    ${mgmt_net}   ${mgmt_nic}    ${host_datacenter}
    Fusion Api Login Appliance    ${ov_ip}     ${ov_credentials}
    ${configured_mgmt_ips}=    run keyword if    '${enclosure_type}' == 'C7K'      Create Prerequisites for C7K Import    ${profiles}    ${server_hardware_list}   ${deploy_configs}  ${mgmt_net}   ${mgmt_nic}
        ...    ELSE IF   '${enclosure_type}' == 'Synergy'      Create Prerequisites for I3S Import    ${profiles}    ${server_hardware_list}
        ...    ELSE       Fatal Error     msg=Enclosure Type Not defined
    Set To Dictionary    ${vcenter_details}    cluster    ${cluster_name}
    Create Target Cluster    ${vcenter_details}
    Log    Change the Datacenter location where hosts will be added
    ${host_target_vcenter} =    copy.deepcopy    ${vcenter_details}
    Set To Dictionary    ${host_target_vcenter}    datacenter=${host_datacenter}
    Log    Datacenter where the hosts will be added in this test case is different from where cluster is created: ${host_datacenter}    console=True
    run keyword if    '${enclosure_type}' == 'Synergy'      Add Hosts to Target Datacenter    ${configured_mgmt_ips}   ${host_target_vcenter}  ${esxi_configs}
    ...    ELSE    Add Hosts to Target Datacenter    ${configured_mgmt_ips}   ${host_target_vcenter}  ${deploy_configs['esxi_config']}
    Wait Until Keyword Succeeds    8 minutes    1 minutes      Cluster should be present in DB    ${cluster_name}
    :FOR    ${ip}    IN    @{configured_mgmt_ips}
   \    Wait Until Keyword Succeeds    8 minutes    1 minutes      Host should be present in DB    ${ip}

Create Prerequisites for C7K Import
    [Documentation]    Create SP from SPT with wait task and deploy ESXI using autodeploy.
    ...     Configure management network and return the management IP Addresses
    [Arguments]    ${profiles}   ${servers}   ${deploy_configs}   ${mgmt_net}   ${mgmt_nic}

    Log  \nCreating new profiles     console=True
    ${resp_list} =       Create List
    ${sp_list} =    create list
    :for    ${profile}    in     @{profiles}
    \    ${parented_sp}=  run keyword and return status    dictionary should contain key    ${profile}    serverProfileTemplateUri
    \    ${payload}=  Run keyword if  '${parented_sp}'=='True'    Create Server Profile POST Payload from SPT    ${profile}
    \    ...           ELSE    Create Server Profile POST Payload    ${profile}
    \    ${payload}=    Create Server Profile POST Payload from SPT       ${profile}
    \    ${response}=    Fusion API Create Server Profile    body=${payload}   param=?force=ignoreServerHealth
    \    Append To List    ${resp_list}    ${response}
    \    Append to list  ${sp_list}  ${payload['name']}

    Wait For Task2    ${resp_list}    timeout=1500    interval=60
    Delete Autodeploy Rules     ${sp_list}    ${deploy_configs}
    ${sp_dict} =    Generate Server Profile List   ${sp_list}
    Add Autodeploy Rules    ${sp_dict}   ${deploy_configs}
    Set One Time Boot    ${servers}    NETWORK
    Log  \nDeploying ESXi via Autodeploy; this may take a while..     console=True
    Power On Servers    ${sp_dict}
    Sleep     22m
    ${deployed_hosts} =     Get Deployed Hosts From Vcenter     ${sp_dict}   ${deploy_configs['deployment_vc']}
    ${mgmt_ips} =    Run Keyword If  '${ipv6}' == 'True'
    ...    Configure IPv6 Management Networking on ESXi   ${deployed_hosts}   ${deploy_configs['esxi_config']}   ${mgmt_net}   ${mgmt_nic}
    ...    ELSE    Configure Management Networking on ESXi   ${deployed_hosts}   ${deploy_configs['esxi_config']}   ${mgmt_net}   ${mgmt_nic}
    Delete Autodeploy Rules     ${sp_list}   ${deploy_configs}
    Remove Deployed Hosts From Deployment Vcenter    ${deployed_hosts}   ${deploy_configs['deployment_vc']}
    Remove deployment networking   ${mgmt_ips}   ${deploy_configs['esxi_config']}
    [Return]    ${mgmt_ips}

Create Prerequisites for I3S Import
    [Documentation]    Creates SP from SPT with wait task As part of I3S Prerequisites and Returns the list of IP Address assigned to SP
    [Arguments]    ${profiles}    ${server_hardware_list}
    Power Off servers in list    ${server_hardware_list}    PressAndHold
    ${resp_list} =       Create List
    :for    ${profile}    in     @{profiles}
    \    ${parented_sp}=  run keyword and return status    dictionary should contain key    ${profile}    serverProfileTemplateUri
    \    ${payload}=  Run keyword if  '${parented_sp}'=='True'    Create Server Profile POST Payload from SPT    ${profile}
    \    ...           ELSE    Create Server Profile POST Payload    ${profile}
    \    ${payload}=   Set Server Profile Password    ${payload}    hpVSE123#
    \    ${response}=    Fusion API Create Server Profile    body=${payload}   param=?force=ignoreServerHealth
    \    Append To List    ${resp_list}    ${response}
    Wait For Task2    ${resp_list}    timeout=1500    interval=60
    Power on servers in list    ${server_hardware_list}
    ${ip_list}=    Get Ip from server profile    ${profiles}
    :for    ${host_ip}    in     @{ip_list}
    \    clrm_common.Wait For Appliance To Become Pingable    ${host_ip}    20min    60sec
    [Return]    ${ip_list}

Get Server Profile Management IP
    [Documentation]  Get Server Profile Management IP
    [Arguments]  ${server_profile}
    ${osCustomAttributes}=  Get From Dictionary  ${server_profile['osDeploymentSettings']}  osCustomAttributes
    :For  ${attribute}  IN  @{osCustomAttributes}
    \    Continue For Loop If  '${attribute['name']}'!='ManagementNIC.ipaddress'
    \    ${mngt_ip}=  Run KeyWord If  '${attribute['name']}'=='ManagementNIC.ipaddress'  Get From Dictionary  ${attribute}  value
    \    Exit For Loop If  '${attribute['name']}'=='ManagementNIC.ipaddress'
    Log  \nServer profile '${server_profile['name']}' management IP '${mngt_ip}'  console=True
    [Return]  ${mngt_ip}

Set Server Profile Password
    [Documentation]  Set Server Profile Password
    [Arguments]  ${server_profile}    ${password}
    ${osCustomAttributes}=  Get From Dictionary  ${server_profile['osDeploymentSettings']}  osCustomAttributes
    :For  ${attribute}  IN  @{osCustomAttributes}
    \    Continue For Loop If  '${attribute['type']}'!='password'
    \    Run KeyWord If  '${attribute['type']}'=='password'  Set To Dictionary  ${attribute}  value    ${password}
    \    Exit For Loop If  '${attribute['type']}'=='password'
    Log  \nServer profile '${server_profile['name']}' Password has been set to '${password}'  console=True
    [Return]  ${server_profile}


Get Ip from server profile
    [Documentation]     Get the Ip Address from Server profile deplyed using I3s
    [Arguments]     ${profiles}
    Log    Get the ip address from server profile    console=true
    ${ip_list} =       Create List
    :for    ${profile}    in     @{profiles}
    \    ${response}=    Fusion Api Get Server Profiles    param=?filter="'name'=='${profile["name"]}'"
    \    ${mngt_ip}=    Get Server Profile Management IP    ${response['members'][0]}
    \    Append to list       ${ip_list}    ${mngt_ip}
    [Return]    ${ip_list}

Power on servers in list
    [Documentation]    Powers on the servers in the list of server hardwares given with server hardware name
    [Arguments]    ${server_hardware_list}
    ${body} =     Create Dictionary    powerState=On
    ...                                powerControl=MomentaryPress
    Log      Powering On servers in list    console=True
    ${resp_list} =       Create List
    :for    ${server_hardware}    in    @{server_hardware_list}
    \       ${server} =  Get Resource  SH:${server_hardware}
    \       Continue For Loop If    '${server['powerState']}'!='On'
    \       Log      Powering On ${server['name']}, uri ${server['uri']}    console=True
    \       ${resp} =     Fusion Api Edit Server Hardware Power State        body=${body}    uri=${server['uri']}
    \       Append To List    ${resp_list}    ${resp}
    ${count} =   Get Length    ${resp_list}
    Run Keyword If    '${count}'=='0'    Log    All servers were On, no need to Wait For Task
    Return From Keyword If    '${count}'=='0'
    Wait For Task2    ${resp_list}    timeout=1500    interval=60

Power off servers in list
    [Documentation]    Powers off the servers in the list of server hardwares given with server hardware name
    [Arguments]    ${server_hardware_list}    ${powerControl}
    ${body} =     Create Dictionary    powerState=Off
    ...                                powerControl=${powerControl}
    Log      Powering Off servers in list    console=True
    ${resp_list} =       Create List
    :for    ${server_hardware}    in    @{server_hardware_list}
    \       ${server} =  Get Resource  SH:${server_hardware}
    \       Continue For Loop If    '${server['powerState']}'=='Off'
    \       Log      Powering Off ${server['name']}, uri ${server['uri']}    console=True
    \       ${resp} =     Fusion Api Edit Server Hardware Power State        body=${body}    uri=${server['uri']}
    \       Append To List    ${resp_list}    ${resp}
    ${count} =   Get Length    ${resp_list}
    Run Keyword If    '${count}'=='0'    Log    All servers were On, no need to Wait For Task
    Return From Keyword If    '${count}'=='0'
    Wait For Task2    ${resp_list}    timeout=1500    interval=60

Power off servers with uri list
    [Documentation]    Powers off the servers in the list of server hardwares given with server hardware uri
    [Arguments]    ${server_hardware_list}    ${powerControl}
    ${body} =     Create Dictionary    powerState=Off
    ...                                powerControl=${powerControl}
    Log      Powering Off servers in list    console=True
    ${resp_list} =       Create List
    :for    ${server_hardware}    in    @{server_hardware_list}
    \       Log      Powering Off ${server_hardware}    console=True
    \       ${resp} =     Fusion Api Edit Server Hardware Power State        body=${body}    uri=${server_hardware}
    \       Append To List    ${resp_list}    ${resp}
    ${count} =   Get Length    ${resp_list}
    Run Keyword If    '${count}'=='0'    Log    All servers were On, no need to Wait For Task
    Return From Keyword If    '${count}'=='0'
    Wait For Task2    ${resp_list}    timeout=1500    interval=60

Create C7K SP from C7K SPT
    [Documentation]    Create SP from SPT with wait task
    [Arguments]    ${sp_payload}
    ${pay_load}=    Create Server Profile POST Payload from SPT    ${sp_payload}
    ${resp}=    Fusion API Create Server Profile    ${pay_load}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    [Return]    ${blnStatus}

Import Virtual switch layout
    [Documentation]     gets virtual switch layout for the cluster provided
    [Arguments]     ${spt_uri}    ${hypervisorManagerUri}    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}
    ${payload}=     Create Dictionary
    set to dictionary       ${payload}      serverProfileTemplateUri=${spt_uri}
    ...     hypervisorManagerUri=${hypervisorManagerUri}
    ...     hypervisorClusterSettings=${hypervisorClusterSettings}
    ...     virtualSwitchConfigPolicy=${virtualSwitchConfigPolicy}
    Log     ${payload}   console=True
    ${VSL}=  Fusion Api Create Virtual Switch Layout    ${payload}
    Remove from dictionary      ${VSL}      headers     status_code
    [return]    ${VSL}

Create Shared Storage body
    [Documentation]  Creates the shared storage body
    [Arguments]    ${volumeAttachments}    ${managed_volumes}=${None}
    ${sharedStorageVolumes}=    Create List
    :for    ${volume}    in    @{volumeAttachments}
    \    ${volume_attachment}=    Create Dictionary
    \    Run KeyWord If  '${managed_volumes}' != '${None}' and $volume['volumeUri'] in $managed_volumes
    \    ...     Set To Dictionary    ${volume_attachment}    storageVolumeUri=${volume['volumeUri']}    volumeFileSystemType=VMFS
    \    ...    ELSE    Set To Dictionary    ${volume_attachment}    storageVolumeUri=${volume['volumeUri']}    volumeFileSystemType=Unmanaged
    \    Append To List  ${sharedStorageVolumes}    ${volume_attachment}
    [Return]    ${sharedStorageVolumes}

Create Shared Storage body for extra volumes attachment
    [Documentation]  Creates the shared storage body to add to clusters
    [Arguments]    ${volumeAttachments}
    ${sharedStorageVolumes}=    Create List
    :for    ${volume}    in    @{volumeAttachments}
    \    ${volume_attachment}=    Create Dictionary
    \    ${volumeUri}=    Get Storage Volume URI    ${volume['volumeUri']}
    \    Set To Dictionary    ${volume_attachment}    storageVolumeUri=${volumeUri}
    \    ...    volumeFileSystemType=Unmanaged
    \    Append To List  ${sharedStorageVolumes}    ${volume_attachment}
    [Return]    ${sharedStorageVolumes}

Create Hypervisor Hosts body
    [Documentation]    Creates the Hypervisor Host body
    [Arguments]    ${server_hardware_list}
    ${hypervisor_host_body}=    Create List
    :for    ${Server_hardware}    in    @{server_hardware_list}
    \    ${host}=    Create Dictionary
    \    ${host_uri}=    Get Server Hardware URI    ${Server_hardware}
    \    Set To Dictionary    ${host}    serverHardwareUri=${host_uri}    importHost=${True}
    \    Append To List  ${hypervisor_host_body}    ${host}
    [Return]    ${hypervisor_host_body}

Create DP Password Body
    [Documentation]    Creates the body for setting password
    [Arguments]    ${password}    ${osCustomAttributes}
    ${deploymentPlan}=    Create Dictionary
    :For  ${attribute}  IN  @{osCustomAttributes}
    \    Continue For Loop If  '${attribute['type']}'!='password'
    \    Run KeyWord If  '${attribute['type']}'=='password'  Set To Dictionary  ${deploymentPlan}  serverPassword    ${password}
    \    Exit For Loop If  '${attribute['type']}'=='password'
    [Return]    ${deploymentPlan}

Cluster should be present in CLRM
    [Documentation]     checks the cluster in OV after it gets created in Vcenter
    [Arguments]    ${cluster_name}
    ${cluster_resp}=    Fusion Api Get Hypervisor Clusters    param=?filter="'name'=='${cluster_name}'"
    Should Be Equal As Integers    ${cluster_resp["count"]}    1

Host should be present in DB
    [Documentation]     checks the cluster in OV after it gets created in Vcenter
    [Arguments]     ${configured_mgmt_ip}
    ${host_resp}=    Fusion Api Get Hypervisor Host    param=?filter="'name'=='${configured_mgmt_ip}'"
    Should Be Equal As Integers    ${host_resp["count"]}    1

Host should be in unmanaged state
    [Documentation]     checks state of hypervisor host unmanaged state
    [Arguments]    ${configured_mgmt_ip}
    ${host_resp}=    Fusion Api Get Hypervisor Host    param=?filter="'name'=='${configured_mgmt_ip}'"
    Should Be Equal As Strings    ${host_resp["members"][0]["state"]}    Unmanaged

Create Import Cluster Payload
    [Documentation]    Creates the payload for Importing the cluster
    [Arguments]    ${cluster_name}    ${SPT}    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}    ${managed_volumes}
    ${cluster_post_payload}=    Create Dictionary
    ${cluster_resp}=    Fusion Api Get Hypervisor Clusters    param=?filter="'name'=='${cluster_name}'"
    Run Keyword And Return If    '${cluster_resp["count"]}'=='0'    Log    Unable to find the cluster name : ${cluster_name} Sepcified
    ${cluster_body}=    Get From List    ${cluster_resp['members']}    0
    Set To Dictionary    ${cluster_post_payload}    hypervisorClusterUri=${cluster_body['uri']}
    ...    hypervisorManagerUri=${cluster_body['hypervisorManagerUri']}
    ...    path=${cluster_body['path']}
    ...    name=${cluster_body['name']}
    ...    hypervisorType=${cluster_body['hypervisorClusterConfig']['type']}
    ...    type=HypervisorClusterProfileV3
    ...    hypervisorClusterSettings=${hypervisorClusterSettings}

    ${hypervisorHostProfileTemplate}=    Create Dictionary
    ${spt_body}=   Fusion Api Get Server Profile Templates    param=?filter="'name'=='${SPT}'"
    Run Keyword And Return If    '${spt_body["count"]}'=='0'    Log    Unable to find the Server Profile template : ${SPT} Sepcified
    Set To Dictionary    ${hypervisorHostProfileTemplate}    serverProfileTemplateUri=${spt_body['members'][0]['uri']}
    ...    hostprefix=${cluster_body['name']}
    ...    virtualSwitchConfigPolicy=${virtualSwitchConfigPolicy}
    ${VSL}=    Import Virtual switch layout    ${spt_body['members'][0]['uri']}    ${cluster_body['hypervisorManagerUri']}    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}
    ${vsl_json}     json.loads      ${vsl['response_body']}
    set to dictionary       ${hypervisorHostProfileTemplate}      virtualSwitches    ${vsl_json}

    ${osCustomAttributes_status}=    run keyword and return status    Dictionary should contain key    ${spt_body['members'][0]['osDeploymentSettings']}    osCustomAttributes
    ${deploymentPlan}=    run keyword if    ${osCustomAttributes_status}==True    Create DP Password Body    hpVSE123#    ${spt_body['members'][0]['osDeploymentSettings']['osCustomAttributes']}
    ${deployment_manager_type}=    Set Variable If    ${deploymentPlan}==None     UserManaged
    ...    ${deploymentPlan} != None    I3S

    ${hostConfigPolicy}=    Create Dictionary
    Set To Dictionary    ${hostConfigPolicy}    leaveHostInMaintenance=False    useHostnameToRegister=False
    Set To Dictionary    ${hypervisorHostProfileTemplate}      hostConfigPolicy=${hostConfigPolicy}
    ...    deploymentPlan=${deploymentPlan}
    ...    deploymentManagerType=${deployment_manager_type}
    Set To Dictionary    ${cluster_post_payload}    hypervisorHostProfileTemplate    ${hypervisorHostProfileTemplate}


    ${shared_storage}=    Run Keyword If    '${spt_body['members'][0]['sanStorage']['manageSanStorage']}' == 'True'
    ...    Create Shared Storage body   ${spt_body['members'][0]['sanStorage']['volumeAttachments']}    ${managed_volumes}
    set to dictionary    ${cluster_post_payload}    sharedStorageVolumes=${shared_storage}

    ${hypervisor_host_body}=     Create Hypervisor Hosts body    ${server_hardware_list}
    set to dictionary    ${cluster_post_payload}    addHostRequests=${hypervisor_host_body}

    [Return]    ${cluster_post_payload}


Import Cluster
    [Documentation]  Imports the cluster with specified configuration
    [Arguments]    ${cluster_name}    ${spt_name}    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}    ${managed_volumes}=${None}
    ${payload}=    Create Import Cluster Payload     ${cluster_name}    ${spt_name}    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}    ${managed_volumes}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${cluster_name}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}

Delete Cluster By Name
    [Documentation]    Deletes the cluster by name
    [Arguments]    ${cluster_name}    ${server_hardware_list}
    ${cluster_uri}=     Get Cluster Profile Uri by Name     ${cluster_name}
    :For    ${server}     In      @{server_hardware_list}
    \    Power off Server    ${server}    powerControl=PressAndHold
    ${resp}=    Run keyword IF      '${cluster_uri}' != 'None'    Delete cluster profile by url       ${cluster_uri}      True
    wait for task2      ${resp[0]['task_resp']}

Create Target Cluster
    [Documentation]        Creates the cluster in the given datacenter if not already created
    [Arguments]     ${vcenter_config}
    Connect To VI Server   ${vcenter_config['vc']}  ${vcenter_config['user']}   ${vcenter_config['password']}
    Log  \nCreating cluster: ${vcenter_config['cluster']} in DC: ${vcenter_config['datacenter']}     console=True
    ${resp} =   Run Keyword And Ignore Error    RoboGalaxyLibrary.create cluster   ${vcenter_config['cluster']}   ${vcenter_config['datacenter']}
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

Create SP and Add Hosts to existing Cluster OOB
    [Documentation]        Creates Server profile and adds host to V-center OOB
    [Arguments]     ${profiles_SP}    ${SH_list}    ${Cluster_name}    ${vcenter_details}
    Fusion Api Login Appliance    ${ov_ip}     ${ov_credentials}
    ${configured_mgmt_ips}=    run keyword if    '${enclosure_type}' == 'C7K'      Create Prerequisites for C7K Import    ${profiles_SP}    ${SH_list}   ${deploy_configs}  ${mgmt_net}   ${mgmt_nic}
    ...    ELSE IF   '${enclosure_type}' == 'Synergy'      Create Prerequisites for I3S Import    ${profiles_SP}    ${SH_list}
    ...    ELSE       Fatal Error     msg=Enclosure Type Not defined
    run keyword if    '${enclosure_type}' == 'Synergy'      resource.Add Hosts to Target VCenter    ${configured_mgmt_ips}   ${vcenter_details}  ${deploy_configs}
    ...    ELSE    resource.Add Hosts to Target VCenter    ${configured_mgmt_ips}   ${vcenter_details}  ${deploy_configs['esxi_config']}
    :FOR    ${ip}    IN    @{configured_mgmt_ips}
    \    Wait Until Keyword Succeeds    8 minutes    1 minutes      Host should be present in DB    ${ip}

Add Hosts to Target Datacenter
    [Documentation]        Adds the standalone hosts to Datacenter
    [Arguments]     ${hosts}   ${vcenter_config}    ${host_config}
    Connect To VI Server   ${vcenter_config['vc']}  ${vcenter_config['user']}   ${vcenter_config['password']}
    :FOR  ${host}   IN   @{hosts}
    \    Log  \nAdding host: ${host} to datacenter: ${vcenter_config['datacenter']}     console=True
    \    ${response}=    Add Host To Vcenter     ${host}    ${vcenter_config['datacenter']}    ${host_config['user']}    ${host_config['password']}
    Disconnect from VI Server

Power off host profile and migrate server hardware
    [Documentation]        host profile operations, Power off Server profile and migrate server hardware
    [Arguments]     ${host_profile_name}    ${SP_payload}    ${SP_payload_update}    ${vcenter_config}

    ${host_profile_uri}=    Get Host Profile Uri By Name    ${host_profile_name}
    ${host_profile_detail}=    Get Host Profile by Uri    ${host_profile_uri}
    ${InMaintenance_task}=    Host power state Operations    ${host_profile_uri}    InMaintenance
    Wait For Task2    ${InMaintenance_task}    timeout=20m    interval=1m    errorMessage=Enter Maintenance task has been failed
    Connect To VI Server   ${vcenter_config['vc']}  ${vcenter_config["user"]}   ${vcenter_config["password"]}
    Host Should Be In Maintenance Mode    ${host_profile_detail['ipSettings']['ip']}
    Migrate SP to another server hardware    Payload=${SP_payload}    Payload_update=${SP_payload_update}

Grow cluster from OV
    [Documentation]        Grow Cluster from OV
    [Arguments]     ${cluster_uri}    ${Payload_grow}
    ${update_resp}      Update cluster profile    ${Payload_grow}    ${True}
    Wait For Task2    ${update_resp[0]['rest_resp']}    timeout=20m    interval=1m
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    should be equal as integers     ${remediate_response['status_code']}      202
    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}

Shrink cluster from OV
    [Documentation]        Shrink cluster from OV
    [Arguments]     ${cluster_uri}    ${Payload_shrink}
    ${update_resp}      Update cluster profile    ${Payload_shrink}    ${True}
    Wait For Task2    ${update_resp[0]['rest_resp']}    timeout=20m    interval=1m
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}