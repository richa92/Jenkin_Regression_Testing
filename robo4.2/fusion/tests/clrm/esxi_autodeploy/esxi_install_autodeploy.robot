*** Settings ***
Documentation   Create Server Profile and deploy ESXi using vmware Autodeploy
Resource            ./resource.robot
Suite Setup         Esxi Autodeploy Suite Setup   ${appliance_ip}    ${credentials}
Suite Teardown      Fusion Api Logout Appliance


*** Test Cases ***

Create Server Profiles
    [Documentation]    Creates Server Profiles from the given list of hardwares
    ...     if a profile exists, it will be removed
    [Tags]    create_sp
    ${response_list}    ${server_profile_list} =   Create Server Profiles   ${sp_bl460c_gen9}    ${servers}
    Wait For Task2    ${response_list}    timeout=1800    interval=60
    set suite variable  ${server_profile_list}

Configure AutoDeploy Rules
    [Documentation]      Delete any existing autodeploy rules for the server hardware and add new rules
    [Tags]    add_autodeploy_rules
    Log  \nRemoving any esxisting rules:    console=True
    Delete Autodeploy Rules     ${server_profile_list}    ${autodeploy_configs}
    ${sp_dict} =    Generate Server Profile List   ${server_profile_list}
    set suite variable  ${sp_dict}
    Add Autodeploy Rules    ${sp_dict}   ${autodeploy_configs}

Deploy ESXi via AutoDeploy
    [Documentation]        Set the server to boot from network and power on
    [Tags]    deploy_esxi
    Set One Time Boot    ${servers}    NETWORK
    Log  \nDeploying ESXi via Autodeploy; this may take a while..     console=True
    Power On Servers    ${sp_dict}
    # enhancement to include a way of monitoring the esxi deployment. hence for now have just given sleep
    Sleep     18m
    ${deployed_hosts} =     Get Deployed Hosts From Vcenter     ${sp_dict}   ${autodeploy_configs['deployment_vc']}
    set suite variable  ${deployed_hosts}
    Delete Autodeploy Rules     ${server_profile_list}  ${autodeploy_configs}

Reconfigure ESXi Networking
    [Documentation]        Reconfigure ESXi Networking
    [Tags]    reconfig_esxi_net
    ${configured_mgmt_ips} =    Run Keyword If  '${ipv6}' == 'True'
    ...    Configure IPv6 Management Networking on ESXi   ${deployed_hosts}   ${autodeploy_configs['esxi_config']}  ${mgmt_net}   ${mgmt_nic}
    ...    ELSE    Configure Management Networking on ESXi   ${deployed_hosts}   ${autodeploy_configs['esxi_config']}  ${mgmt_net}   ${mgmt_nic}
    set suite variable  ${configured_mgmt_ips}
    Remove Deployed Hosts From Deployment Vcenter    ${deployed_hosts}   ${autodeploy_configs['deployment_vc']}
    Remove deployment networking   ${configured_mgmt_ips}  ${autodeploy_configs['esxi_config']}

Create Target Cluster and Add Deployed ESXi
    [Documentation]        Create Target Cluster and Migrate Deployed ESXi
    [Tags]    migrate_esxi
    Create Target Cluster    ${target_vcenter}
    Add Hosts to Target VCenter   ${configured_mgmt_ips}   ${target_vcenter}  ${autodeploy_configs['esxi_config']}
