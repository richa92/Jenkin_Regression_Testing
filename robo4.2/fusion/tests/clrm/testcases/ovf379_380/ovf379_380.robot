*** Settings ***
Documentation       This is to test CLRM OVF_379_380 COmpliance and Remediation Features
...                 This expects atleast 1 cluster to be in consistent state with alteast 1 host in it
...                 If there are no cluster test cases will fail
...                 Environment_remediation.txt should be run before running OVF379_380
...                 Environment_remediation.txt creates SPTs and Cluster profilesrequired for OVF379_380

Resource                        resource.txt
Test Teardown                   Collect SupportDump on Failure    ${cluster_standard}
Suite Teardown                  Fusion Api Logout Appliance

*** Variables ***

${File_Location}        E:/Shares/testrepo/Logs

*** Test Cases ***
OVTC29249
    [Documentation]     Vcenter events for Create Cluster OOB Create a cluster-profile from clrm.
    ...     Make OOB change on this cluster by selecting the vsphere HA as enabled
    [Tags]    Cluster_Standard_Switch
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    Log    ${cluster_standard[0]['name']}    console=True
    ${cluster_ha}=      Get from Dictionary     ${Cluster_with_prereq['hypervisorClusterSettings']}      haEnabled
    ${flip_ha}=     Evaluate    not $cluster_ha
    Log     ${flip_ha}      console=True
    Reconfigure HA      ${Cluster_with_prereq['name']}     ${flip_ha}
    Log    Waiting for the cluster to became Inconsistent,Wait time is for 5 min maximum
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      ClusterConfigInconsistent
    ${remediate_response}=      Remediate cluster profile Inconsistent    ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=10m    interval=1m    errorMessage=Remediate Failed


OVTC29250
    [Documentation]     Vcenter events for Create Cluster OOB Create a cluster-profile from clrm.
    ...     Make OOB change on this cluster by selecting the vsphere DRS as enabled
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    ${cluster_DRS}=      Get from Dictionary     ${Cluster_with_prereq['hypervisorClusterSettings']}      drsEnabled
    ${flip_drs}=     Evaluate    not $cluster_DRS
    Log     ${flip_drs}      console=True
    Reconfigure DRS      ${Cluster_with_prereq['name']}     ${flip_drs}
    Log    Waiting for the cluster to became Inconsistent,Wait time is for 5 min maximum
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      ClusterConfigInconsistent
    ${remediate_response}=      Remediate cluster profile Inconsistent    ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=10m    interval=1m    errorMessage=Remediate Failed

OVTC29255
    [Documentation]     Deleting the existing connection in server profile should cause
    ...     inconsistancy with state "HostProfileInconsistent"
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    ${Cluster_host_uri}=      Get From List       ${Cluster_with_prereq['hypervisorHostProfileUris']}    0
    ${host_response}=   Fusion Api Get Hypervisor Host profile      uri=${Cluster_host_uri}
    Remove Connection from SP     ${host_response['serverProfileUri']}
    ${host_ip}=     Get Ip From Host Profile    ${Cluster_host_uri}
    clrm_common.Wait For Appliance To Become Pingable    ${host_ip}    20min    60sec
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      HostProfileInconsistent
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    Sleep     300 sec
    ${remediate_response}=      Remediate cluster profile Inconsistent    ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Remediate Failed\

OVTC29253
    [Documentation]     Compliance for updating an existing connection in SPT with a new network uri
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    Update Connection in SPT    ${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}     OVTC29253
    Log    Waiting for the cluster to became Inconsistent,Wait time is for 5 min maximum
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      ClusterTemplateVSwitchError
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent with Vswitch   ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Remediate Failed

OVTC29244
    [Documentation]     Compliance for adding networks in server profile - FT,  and Tunnel
    ...     Add connections in server profile FT,  and Tunnel  connections.Make GET
    ...      call for cluster profile
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    ${Cluster_host_uri}=      Get From List       ${Cluster_with_prereq['hypervisorHostProfileUris']}    0
    ${host_response}=   Fusion Api Get Hypervisor Host profile      uri=${Cluster_host_uri}
    ${server_profile_uri}=      Get from Dictionary     ${host_response}      serverProfileUri
    Add Connection to SP    ${server_profile_uri}    ft_nw
    ${host_ip}=     Get Ip From Host Profile    ${Cluster_host_uri}
    clrm_common.Wait For Appliance To Become Pingable    ${host_ip}    20min    60sec
    Sleep     300 sec
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      HostProfileInconsistent
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent    ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Remediate Failed

OVTC29245
    [Documentation]     Compliance for adding and deleting networks in server profile Template- FT, and Tunnel
    ...         Add connections in server profile FT,  and Tunnel and then delete these connections.
    ...         Make GET call for cluster profile
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    Add Ethernet Connection to SPT    ${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}    ft_nw
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      ClusterTemplateVSwitchError
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent with Vswitch   ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Adding the connection from SPT Failed

    Remove Ethernet Connection from SPT    ${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}    ft_nw
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      ClusterTemplateVSwitchError
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent with Vswitch   ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Deleting the connection from SPT Failed

OVTC29246
    [Documentation]     Compliance for adding and deleting networks in server profile Template- FT, and Tunnel
    ...         Add connections in server profile FT,  and Tunnel and then delete these connections.
    ...         Make GET call for cluster profile
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    Add Ethernet Connection to SPT    ${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}    net_147
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      ClusterTemplateVSwitchError
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent with Vswitch   ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Adding the connection from SPT Failed

    Remove Ethernet Connection from SPT    ${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}    net_147
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      ClusterTemplateVSwitchError
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent with Vswitch   ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Deleting the connection from SPT Failed

OVTC29252
    [Documentation]     Compliance for redundant/teamed networks in SPT Craete an SPT with non-redundant connections.
    ...     Create a Cluster profile using this SPT.Update SPT to team the connections. Remediate CP
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    Add Ethernet Connection to SPT    ${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}    ${OVTC29252_connection}
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      ClusterTemplateVSwitchError
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent with Vswitch   ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Remediate Failed

OVTC29247
    [Documentation]     Compliance for adding,updating and deleting  networks in Net set of server profile template
    ...                 Update the networks in the Net-set for addition, updating(renaming) and deleting the networks.
    ...                 Then revert the changes. Make GET call for cluster profile
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    Update Network Set    ${update_network_set_add}
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      ClusterTemplateVSwitchError
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent with Vswitch   ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Remediate Failed

    Update Network Set    ${update_network_set_del}
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      ClusterTemplateVSwitchError
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent with Vswitch   ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Remediate Failed while deleting the network set


OVTC29248
    [Documentation]     Compliance for adding  a new storage volume in the server profile template Add a new volume to the existing serevr profile template.
    ...    Make a GET call for the cluster profile
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    ${vol_uri} =       Get Storage Volume URI     svol3
    Add Volume to SPT    ${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}    svol3
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      ClusterTemplateStorageVolError
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile StorageInconsistent    ${Cluster_with_prereq['uri']}    ${vol_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=10m    interval=1m    errorMessage=Remediate Failed

OVTC29263
    [Documentation]     Changing connections bandwidth from SPT for Management network should cause inconsistency in cluster profile.
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    ${spt_response}=      Fusion Api Get Server Profile Templates       ${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Remove from dictionary      ${spt_response}      headers    status_code
    ${Connections}=     Get From Dictionary     ${spt_response['connectionSettings']}     connections
    :For    ${connection}   in      @{Connections}
    \   ${resp}=    Fusion Api Get Ethernet Networks      ${connection['networkUri']}
    \   Run keyword if      '${resp['category']}' != 'ethernet-networks'    Continue for loop
    \   Run keyword if      '${resp['purpose']}' == 'Management'    run keywords
    \   ...     set to Dictionary      ${connection}      requestedMbps=2000     AND
    \   ...     Exit for loop
    Remove from dictionary      ${spt_response}      headers    status_code
    ${spt_edit_response}=    Fusion Api Edit Server Profile Template     ${spt_response}     uri=${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Wait For Task2  ${spt_edit_response}  300  5
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      HostProfileInconsistent
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent    ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Remediate Failed

OVTC29251
    [Documentation]     Changing connections bandwidth from SPT for Vmotion network should cause inconsistency in cluster profile.
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    ${spt_response}=      Fusion Api Get Server Profile Templates       ${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Remove from dictionary      ${spt_response}      headers    status_code
    ${Connections}=     Get From Dictionary     ${spt_response['connectionSettings']}     connections
    :For    ${connection}   in      @{Connections}
    \   ${resp}=    Fusion Api Get Ethernet Networks      ${connection['networkUri']}
    \   Run keyword if      '${resp['category']}' != 'ethernet-networks'    Continue for loop
    \   Run keyword if      '${resp['purpose']}' == 'VMMigration'    run keywords
    \   ...     set to Dictionary      ${connection}      requestedMbps=2000     AND
    \   ...     Exit for loop
    Remove from dictionary      ${spt_response}      headers    status_code
    ${spt_edit_response}=    Fusion Api Edit Server Profile Template     ${spt_response}     uri=${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Wait For Task2  ${spt_edit_response}  300  5
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      HostProfileInconsistent
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent    ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Remediate Failed

OVTC29262
    [Documentation]     Changing connections bandwidth from SPT for Fault Tolerance network should cause inconsistency in cluster profile.
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    ${spt_response}=      Fusion Api Get Server Profile Templates       ${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Remove from dictionary      ${spt_response}      headers    status_code
    ${Connections}=     Get From Dictionary     ${spt_response['connectionSettings']}     connections
    :For    ${connection}   in      @{Connections}
    \   ${resp}=    Fusion Api Get Ethernet Networks      ${connection['networkUri']}
    \   Run keyword if      '${resp['category']}' != 'ethernet-networks'    Continue for loop
    \   Run keyword if      '${resp['purpose']}' == 'FaultTolerance'    run keywords
    \   ...     set to Dictionary      ${connection}      requestedMbps=2000     AND
    \   ...     Exit for loop
    Remove from dictionary      ${spt_response}      headers    status_code
    ${spt_edit_response}=    Fusion Api Edit Server Profile Template     ${spt_response}     uri=${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Wait For Task2  ${spt_edit_response}  300  5
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      HostProfileInconsistent
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent    ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Remediate Failed


OVTC29242
    [Documentation]     Vcenter events for Create Cluster OOB Create a cluster-profile from clrm.
    ...     Add Vmkernal port on the host on the selected cluster profile
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    ${host_profiles}=       Get from Dictionary    ${Cluster_with_prereq}    hypervisorHostProfileUris
    :For    ${host_profile}     In      @{host_profiles}
    \    ${host_profile_detail}=     Get Host Profile by Uri     ${host_profile}
    \    Create Port Group       ${host_profile_detail['ipSettings']['ip']}      OVTC29242      vSwitch1        100
    \    ${vmk} =       Create Vmkernal Nic On Std Switch      ${host_profile_detail['ipSettings']['ip']}      OVTC29242
    \    Enable Vmotion Service       ${host_profile_detail['ipSettings']['ip']}       ${vmk}
    \    Sleep     60 sec
    Log    Waiting for the cluster to became Inconsistent,Wait time is for 5 min maximum
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      HostProfileInconsistent
    ${remediate_response}=      Remediate cluster profile Inconsistent    ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=10m    interval=1m    errorMessage=Remediate Failed

OVTC29257
    [Documentation]     Vcenter events for Create Cluster OOB Create a cluster-profile from clrm.
    ...     Remove Datastore from cluster profile
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    ${host_profiles}=       Get from Dictionary    ${Cluster_with_prereq}    hypervisorHostProfileUris
    Log     ${Cluster_with_prereq['sharedStorageVolumes'][0]['name']}
    ${host_profile_detail}=     Get Host Profile by Uri     ${host_profiles[0]}
    Remove Cluster Datastore       ${host_profile_detail['ipSettings']['ip']}      svol4
    Sleep     30 sec
    Log    Waiting for the cluster to became Inconsistent,Wait time is for 5 min maximum
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      HostProfileInconsistent
    ${remediate_response}=      Remediate cluster profile Inconsistent    ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=10m    interval=1m    errorMessage=Remediate Failed

OVTC29264
    [Documentation]     Changing connection's (general, FT, Vmotion, management, tunnel and untagged) bandwidth from Server Profile should cause inconsistency in host profile
    [setup]     Get Cluster with Consistent state    ${cluster_standard[0]['name']}
    ${host_response}=   Fusion Api Get Hypervisor Host profile      uri=${Cluster_with_prereq['hypervisorHostProfileUris'][0]}
    Update Connection Bandwidth in SP      ${host_response['serverProfileUri']}
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      HostProfileInconsistent
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent    ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=25m    interval=1m    errorMessage=Remediate Failed


OVTC29258
    [Documentation]     Vcenter events for Create Cluster OOB Create a cluster-profile from clrm.
    ...     Make OOB change on this cluster by deleting the Standard Switch
    [Tags]    OOB    p1
    [setup]     Get Cluster with Consistent state    ${cluster_standard[0]['name']}
    ${vcenter} =    copy.deepcopy    ${cluster_standard}
    ${host_ip} =     Get Ip From Host Profile    ${Cluster_with_prereq['hypervisorHostProfileUris'][0]}
    Vswitch Should Exist     ${host_ip}    ${OVT29252_switch_name}
    Remove Vswitch      ${host_ip}    ${OVT29252_switch_name}
    Log    Waiting for the cluster to became Inconsistent, Wait time is maximum
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response} =    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      HostProfileInconsistent    Cluster Profile is consistent
    ${remediate_response} =    Remediate cluster profile Inconsistent    ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=10m    interval=1m    errorMessage=Remediate Failed

OVTC35041
    [Documentation]  OOB_vCenter_54-Vcenter compliance for  adding an extra port group to a standard switch
    [Tags]  OOB   p0
    [setup]     Get Cluster with Consistent state    ${cluster_standard[0]['name']}
    ${host_ip} =     Get Ip From Host Profile    ${Cluster_with_prereq['hypervisorHostProfileUris'][0]}
    Vswitch Should Exist     ${host_ip}    ${OVT29252_switch_name}
    add_portgroup_to_vswitch    ${OVT29252_switch_name}    ${TEST_NAME}    host=${host_ip}
    Log    Waiting for the cluster to became Inconsistent, Wait time is maximum
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response} =    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      HostProfileInconsistent    Cluster Profile is consistent
    ${remediate_response} =    Remediate cluster profile Inconsistent    ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=10m    interval=1m    errorMessage=Remediate Failed

OVTC29241
    [Documentation]     Vcenter compliance for  adding and deleting a standard switch-Management 
    ...    Add a new standard switch OOB to a host and then delete the new switch OOB. Make GET
    ...   call for cluster profile
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    ${host_ip} =     Get Ip From Host Profile    ${Cluster_with_prereq['hypervisorHostProfileUris'][0]}
    Vswitch Should Exist     ${host_ip}    ${OVT29252_switch_name}
    remove_vswitch        ${host_ip}    ${OVT29252_switch_name}
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${Cluster_with_prereq['uri']}
    Should be equal     ${hcp_response['complianceState']}      HostProfileInconsistent
    ${remediate_response}=      Remediate cluster profile Inconsistent    ${Cluster_with_prereq['uri']}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=10m    interval=1m    errorMessage=Remediate Failed

OVTC29254
    [Documentation]     Deletion of volume from SPT should not cause inconsistency
    [setup]     Get Cluster with Consistent state       ${cluster_standard[0]['name']}
    Remove Volume to SPT    ${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}    svol5
    sleep    5min
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Be Consistent    ${Cluster_with_prereq['uri']}
    Add Volume to SPT    ${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}    svol5

OVTC45270
    [Documentation]     Use cases for HA alerts in OV when check/uncheck selected OOB-- in OV and VC
    ...     Make OOB change on this cluster by selecting the vsphere HA as enabled. Update cluster
    ...     profile to ensure that compliance alert is cleared
    ...    [Tags]    F379&F380    p0
    [Setup]     Get Cluster with Consistent state    ${cluster_standard[0]['name']}
    ${cluster_ha}=      Get from Dictionary    ${Cluster_with_prereq['hypervisorClusterSettings']}    haEnabled
    ${flip_ha}=     Evaluate    not $cluster_ha
    Reconfigure HA      ${Cluster_with_prereq['name']}    ${flip_ha}
    Log    Waiting for the cluster to became Inconsistent,Wait time is for 5 min maximum    console=True
    Wait Until Keyword Succeeds    5 minutes    1 minutes    Cluster Should Not Be Consistent    ${Cluster_with_prereq['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile    ${Cluster_with_prereq['uri']}
    Should be equal    ${hcp_response['complianceState']}    ClusterConfigInconsistent
    Remove from dictionary    ${hcp_response}    headers    status_code
    set to dictionary    ${hcp_response['hypervisorClusterSettings']}    haEnabled=${flip_ha}
    ${update_response}=    Fusion Api Update Hypervisor Cluster Profile    body=${hcp_response}    uri=${hcp_response['uri']}
    Log    Waiting for the cluster to became consistent,Wait time is for 5 min maximum    console=True
    Wait Until Keyword Succeeds    5 minutes    1 minutes    Cluster Should Be Consistent    ${hcp_response['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile    ${hcp_response['uri']}
    Should be equal    ${hcp_response['complianceState']}    Consistent
