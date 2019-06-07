*** Settings ***
Library           json
Library           copy
Resource          ${fusion_api_resource}
Resource          ../Resources/api/resource.robot
Variables         ./ovf1135_me_data.py
Variables         ./environment_data.py

#below path gives the location for the input of Fusion_ip
Variables              ../../../testdata/i3s_QA_testdata.py

*** Variables ***

${X-API-VERSION}    800
${fusion_api_resource}    ../fusion/Resources/api/fusion_api_resource.txt
${blnVerifyPreReqs}       False
@{allResourcesCommonList}    ethernets    egs    servers    osdps
${profile}    ovf1135_server_profile

*** Keywords ***
Get Subnet Uri of network
    [Arguments]    ${net}
    ${net}=    replace string using regexp    ${net}    ETH:    ${EMPTY}
    ${resp} =    Fusion Api Get Ethernet Networks    param=?filter="'name'=='${net}'"
    ${Subneturi} =    Get From Dictionary    ${resp['members'][0]}    subnetUri
    [Return]    ${Subneturi}

Get Subnet
    [Arguments]    ${NETWORK_ID}
    ${resp} =    fusion api get ipv4 subnet
    ${subnetcounts} =     Get From Dictionary     ${resp}    members
    ${l} =    Get Length    ${subnetcounts}
    :FOR    ${x}    IN RANGE    0    ${l}
    \    ${subnet} =     Get From List    ${subnetcounts}    ${x}
    \    Exit For Loop If    '${subnet['networkId']}' == '${NETWORK_ID}'
    [Return]    ${subnet}

Get from Subnet
    [Arguments]     ${subnet_list}    ${element}
    ${return} =     Get From Dictionary     ${subnet_list}        ${element}
    [Return]    ${return}

Get Available IP Count In Subnet Of Network
    [Arguments]    ${network}
    ${subneturi} =    Get Subnet Uri of network    ${network}
    ${subnet_response} =    Fusion Api Get Ipv4 Subnet    uri=${subneturi}
    ${rangeuri} =    Get From Dictionary    ${subnet_response}    rangeUris
    ${available_ips} =    Convert To Integer     0
    :For    ${range}    IN    @{rangeuri}
    \    ${pool_response} =    fusion_api_get_pool    uri=${range}
    \    ${free_ipcount} =    Get From Dictionary    ${pool_response}    freeIdCount
    \    ${available_ips} =    Evaluate    ${available_ips} + ${free_ipcount}
    Log    \nAvailable ip's : ${available_ips}    console=True
    [Return]    ${available_ips}

Change OSDP To None In SP Json Body
    [Arguments]    ${sp_body}
    ${sp_response_body} =    copy.deepcopy    ${sp_body}
    Set To Dictionary    ${sp_response_body}    osDeploymentSettings    ${null}
    Set To Dictionary    ${sp_response_body}    iscsiInitiatorName    ${null}
    ${boot_mode} =    Create Dictionary    manageMode=${false}
    Set To Dictionary    ${sp_response_body}    bootMode    ${boot_mode}
    Set To Dictionary    ${sp_response_body}    boot    ${null}
    ${connections} =    Get From Dictionary    ${sp_response_body['connectionSettings']}    connections
    ${Number_of_connections}=  Get Length    ${connections}
    :FOR    ${conn_index}    IN Range    0    ${Number_of_connections}
    \    Remove From Dictionary    ${connections[${conn_index}]}    boot
    \	 Set To Dictionary    ${connections[${conn_index}]}    ipv4    ${null}
    [Return]    ${sp_response_body}

Get Free IP From Subnet IP Pool
    [Arguments]    ${ip_pool}
    :FOR    ${ip}    IN    @{ip_pool}
    \    ${blnPingStatus} =    Ping IP    ${ip}
    \    Return From Keyword If    '${blnPingStatus}'!='True'    ${ip}
    [Return]

Ping IP
    [Arguments]    ${host}
    ${resp}  ${ping_output} =  Run And Return Rc And Output  ping -n 4 ${host}
    Return From Keyword If    ${resp} == 0  ${true}
    [Return]

Update Profile request body with free Ipaddress
    [Arguments]    ${sp_body}    ${free_pool_ip}
    ${osCustomAttributes} =    Get From Dictionary    ${sp_body['osDeploymentSettings']}    osCustomAttributes
    :FOR    ${ca}    IN    @{osCustomAttributes}
    \    Run Keyword If    '${ca['name']}'=='ManagementNIC.ipaddress'    Set To Dictionary    ${ca}    value=${free_pool_ip}
    [Return]    ${sp_body}

Remove Network attributes except Ipaddress for osCutomAttributes
    [Arguments]    ${sp_body}
    ${osCustomAttributes} =    Get From Dictionary    ${sp_body['osDeploymentSettings']}    osCustomAttributes
    :FOR    ${ca}    IN    @{osCustomAttributes}
    \    Run Keyword If    '${ca['name']}'=='ManagementNIC.dns1'    Remove Values From List    ${osCustomAttributes}    ${ca}
    \    Run Keyword If    '${ca['name']}'=='ManagementNIC.dns2'    Remove Values From List    ${osCustomAttributes}    ${ca}
    \    Run Keyword If    '${ca['name']}'=='ManagementNIC.gateway'    Remove Values From List    ${osCustomAttributes}    ${ca}
    \    Run Keyword If    '${ca['name']}'=='ManagementNIC.netmask'    Remove Values From List    ${osCustomAttributes}    ${ca}
    [Return]    ${sp_body}

Change Nic Connection from profile
    [Documentation]    Change Nic connection from existing server profile
    [Arguments]    ${sp}    ${nic_connection}
    ${profile} =    copy.deepcopy  ${sp}
    ${osca} =     Get From Dictionary    ${profile['osDeploymentSettings']}    osCustomAttributes
    :FOR    ${ca}    IN    @{osca}
    \    Run Keyword If    '${ca['name']}'=='ManagementNIC.networkuri'    Set To Dictionary    ${ca}    value=ETH:${nic_connection}
    \    Exit For Loop If    '${ca['name']}'=='ManagementNIC.networkuri'
    ${connections} =    Get From Dictionary    ${profile['connectionSettings']}    connections
    :FOR    ${connection}    IN    @{connections}
    \    Run Keyword If    '${connection['name']}'=='Blade_boot_mgmt'    Set To Dictionary    ${connection}    networkUri=ETH:${nic_connection}
    \    Exit For Loop If        '${connection['name']}'=='Blade_boot_mgmt'
    [Return]    ${profile}

Change Nic2 Connection from profile
    [Documentation]    Change Nic2 connection from existing server profile
    [Arguments]    ${sp}    ${nic_connection}
    ${profile} =    copy.deepcopy  ${sp}
    ${osca} =     Get From Dictionary    ${profile['osDeploymentSettings']}    osCustomAttributes
    :FOR    ${ca}    IN    @{osca}
    \    Run Keyword If    '${ca['name']}'=='ManagementNIC2.networkuri'    Set To Dictionary    ${ca}    value=ETH:${nic_connection}
    \    Exit For Loop If    '${ca['name']}'=='ManagementNIC2.networkuri'
    ${connections} =    Get From Dictionary    ${profile['connectionSettings']}    connections
    :FOR    ${connection}    IN    @{connections}
    \    Run Keyword If    '${connection['name']}'=='Blade_boot_mgmt B'    Set To Dictionary    ${connection}    networkUri=ETH:${nic_connection}
    \    Exit For Loop If        '${connection['name']}'=='Blade_boot_mgmt B'
    [Return]    ${profile}
