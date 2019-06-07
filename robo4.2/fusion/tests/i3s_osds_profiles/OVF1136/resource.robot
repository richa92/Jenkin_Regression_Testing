*** Settings ***
Library           json
Library           copy
Resource          ${fusion_api_resource}
Resource          ../Resources/api/resource.robot
Variables         ./ovf_1136_me_data.py
Variables         ./environment_data.py

*** Variables ***
${fusion_api_resource}    C:/Users/komerao/OVF1134/fusion/Resources/api/fusion_api_resource.txt
# ${X-API-VERSION}    600
${fusion_ip}        15.212.167.184
${blnVerifyPreReqs}    False
@{allResourcesCommonList}    ethernets    egs    servers    osdps
${profileTemplate}    OVF1136_SPT

*** Keywords ***
Get Subnet Uri of network
    [Documentation]    Get Subnet Uri of network
    [Arguments]    ${net}
    ${net}=    replace string using regexp    ${net}    ETH:    ${EMPTY}
    ${resp} =    Fusion Api Get Ethernet Networks    param=?filter="'name'=='${net}'"
    ${Subneturi} =    Get From Dictionary    ${resp['members'][0]}    subnetUri
    [Return]    ${Subneturi}

Get Available IP Count In Subnet Of Network
    [Documentation]    Get Available IP Count In Subnet Of Network
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
    [Documentation]    Change OSDP To None In SP Json Body
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
    ${ipv4} =    Get From Dictionary    ${connections[0]}    ipv4
    ${ipv4_attrib} =    Get Dictionary Keys    ${ipv4}
    :FOR    ${attrib}    IN    @{ipv4_attrib}
    \    Set To Dictionary    ${ipv4}    ${attrib}    ${null}
    [Return]    ${sp_response_body}

Get Free IP From Subnet IP Pool
    [Documentation]    Get Free IP From Subnet IP Pool
    [Arguments]    ${ip_pool}
    :FOR    ${ip}    IN    @{ip_pool}
    \    ${blnPingStatus} =    Ping IP    ${ip}
    \    Return From Keyword If    '${blnPingStatus}'!='True'    ${ip}
    [Return]

Ping IP
    [Documentation]    Ping IP
    [Arguments]    ${host}
    ${resp}  ${ping_output} =  Run And Return Rc And Output  ping -n 4 ${host}
    Return From Keyword If    ${resp} == 0  ${true}
    [Return]

Update Profile request body with free Ipaddress
    [Documentation]    Update Profile request body with free Ipaddress
    [Arguments]    ${sp_body}    ${free_pool_ip}
    ${osCustomAttributes} =    Get From Dictionary    ${sp_body['osDeploymentSettings']}    osCustomAttributes
    :FOR    ${ca}    IN    @{osCustomAttributes}
    \    Run Keyword If    '${ca['name']}'=='ManagementNIC.ipaddress'    Set To Dictionary    ${ca}    value=${free_pool_ip}
    [Return]    ${sp_body}

Remove Network attributes except Ipaddress for osCutomAttributes
    [Documentation]    Remove Network attributes except Ipaddress for osCutomAttributes
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
