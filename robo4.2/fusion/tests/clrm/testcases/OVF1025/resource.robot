*** Settings ***
Library                         FusionLibrary
Resource                        ../../../../Resources/api/fusion_api_resource.txt
Resource                        ../../support_files/clrm_common.txt

*** Keywords ***

Get Volume association details
    [Documentation]    Get storage Volume associations.
    [Arguments]        ${Vol_name}
    ${vol_uri} =  Get Storage Volume URI  ${Vol_name}
    ${resp}=    Fusion Api Get Resource    /rest/index/trees/${vol_uri}
    [Return]  ${resp['parents']}

Verify Volume association to cluster
    [Documentation]    Verify storage Volume associations to cluster.
    [Arguments]        ${Vol_name}    ${Cluster_name}
    ${resp}=    Get Volume association details    ${Vol_name}
    ${key_status}=    run keyword and return status    Dictionary should contain key    ${resp}    HYPERVISOR_CLUSTER_PROFILE_TO_STORAGE_VOLUME
    Return From Keyword If    '${key_status}' == '${False}'   ${key_status}
    ${vol_cluster_attachments}=    get from dictionary    ${resp}    HYPERVISOR_CLUSTER_PROFILE_TO_STORAGE_VOLUME
    :For    ${cluster_attached}    in    @{vol_cluster_attachments}
    \    Return From Keyword If    '${cluster_attached['resource']['name']}' == '${Cluster_name}'   ${True}
    [Return]  ${False}

Get Ips from cluster
    [Documentation]     Get the Ip Address from Host profiles
    [Arguments]     ${cluster}
    Log    Get the ip address from Host profiles    console=true
    ${ip_list} =       Create List
    ${host_profiles}=    Get Host Profile Uris From Cluster    ${cluster}
    :for    ${profile}    in     @{host_profiles}
    \    ${response}=    Fusion Api Get Hypervisor Host Profile    uri=${profile}
    \    ${mngt_ip}=    Get from dictionary    ${response['ipSettings']}    ip
    \    Append to list       ${ip_list}    ${mngt_ip}
    [Return]    ${ip_list}