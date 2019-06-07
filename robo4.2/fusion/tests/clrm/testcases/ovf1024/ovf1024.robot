*** Settings ***
Documentation       This is to test CLRM OVF1024 Import Cluster Features
...                 This expects atleast All the Hardwares in working condidtions

Resource                        resource.robot
Resource                        ../ovf379_380/resource.txt
Variables                       data_variables_ovf1024_Synergy.py
Resource                        ../SPT/resource.txt
Suite Teardown                  Fusion Api Logout Appliance

*** Variables ***
${dvsVersion}           6.6.0
${enclosure_type}       Synergy
${mgmt_net}             ${EMPTY}
${mgmt_nic}             ${EMPTY}


*** Test Cases ***

OVTC29141
    [Documentation]    ClusterImport_03 - Import vCenter cluster with Host in Standard switch layout
    ...    (All, General networks along with Tunnel Network) and with storage volumes on CLRM
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC29141}    ${server_hardware_list}    ${target_vcenter}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${payload}=    Create Import Cluster Payload     ${TEST_NAME}    OVTC29141_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list}

OVTC29143
    [Documentation]    ClusterImport_10 - Import vCenter cluster with Host with cluster having HA and DRS enabled
    ...    and "multiNicVMotion" : true on CLRM.
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC29143}    ${server_hardware_list}    ${target_vcenter}    ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    Log    Change the HA,DRS and MultiNivCmotion to True in hypervisorClusterSettings
    ${hypervisorClusterSettings_OVTC29143} =    copy.deepcopy    ${hypervisorClusterSettings}
    Set To Dictionary    ${hypervisorClusterSettings_OVTC29143}    drsEnabled=True    haEnabled=True    multiNicVMotion=True
    Log    hypervisorClusterSettings for this test case:${hypervisorClusterSettings_OVTC29143}    console=True
    ${payload}=    Create Import Cluster Payload     ${TEST_NAME}    OVTC29143_SPT    ${hypervisorClusterSettings_OVTC29143}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list}

OVTC29144
    [Documentation]    ClusterImport_15 - Import vCenter cluster with two Hosts and one of them with different hardware type than specified on SPT
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC29144}    ${server_hardware_list_different_Hw}    ${target_vcenter}    ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    Log    Import Cluster    console=True
    ${payload}=    Create Import Cluster Payload     ${TEST_NAME}    OVTC29144_SPT_1    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list_different_Hw}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_different_Hw}

OVTC29145
    [Documentation]    ClusterImport_19 - Grow already imported cluster by adding one host of same hardware type
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC29141}    ${server_hardware_list}    ${target_vcenter}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${payload}=    Create Import Cluster Payload     ${TEST_NAME}    OVTC29141_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m    errorMessage=Import Cluster failed
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    Log    Grow Cluster with additional Hardware
    clrm_common.update cluster    ${OVTC29145_hardware}    ${True}
    [Teardown]    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list}

OVTC29146
    [Documentation]    ClusterImport_04 - Import vCenter cluster with Host in Distributed switch layout (All, General networks)
    [setup]  Create Prerequisties for Import    ${profiles_OVTC29141}    ${server_hardware_list}    ${target_vcenter}    ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    Log    Change the Switch type to DVS All Networks in hypervisorClusterSettings
    ${hypervisorClusterSettings_OVTC29146} =    copy.deepcopy    ${hypervisorClusterSettings}
    Set To Dictionary    ${hypervisorClusterSettings_OVTC29146}    virtualSwitchType=Distributed    distributedSwitchVersion=${dvsVersion}    distributedSwitchUsage=AllNetworks
    Log    hypervisorClusterSettings for this test case:${hypervisorClusterSettings_OVTC29146}    console=True
    Log    Import Cluster    console=True
    ${payload}=    Create Import Cluster Payload    ${TEST_NAME}    OVTC29141_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name    ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]    Delete Cluster By Name    ${TEST_NAME}    ${server_hardware_list}

OVTC29147
    [Documentation]    ClusterImport_07 - Import vCenter cluster with Host with storage volumes
    [setup]  Create Prerequisties for Import    ${profiles_OVTC29141}    ${server_hardware_list}    ${target_vcenter}    ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    Log    Change the Switch type to DVS All Networks in hypervisorClusterSettings
    ${hypervisorClusterSettings_OVTC29147} =    copy.deepcopy    ${hypervisorClusterSettings}
    Set To Dictionary    ${hypervisorClusterSettings_OVTC29147}    virtualSwitchType=Distributed    distributedSwitchVersion=${dvsVersion}    distributedSwitchUsage=AllNetworks
    Log    hypervisorClusterSettings for this test case:${hypervisorClusterSettings_OVTC29147}    console=True
    Log    Import Cluster    console=True
    ${payload}=    Create Import Cluster Payload    ${TEST_NAME}    OVTC29141_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name    ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]    Delete Cluster By Name    ${TEST_NAME}    ${server_hardware_list}

OVTC29152
    [Documentation]    ClusterImport_24 - check Delete on cluster profile created after importing a cluster OOB
    [setup]  Create Prerequisties for Import    ${profiles_OVTC29141}    ${server_hardware_list}    ${target_vcenter}    ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    Log    Change the Switch type to DVS General Networks in hypervisorClusterSettings
    ${hypervisorClusterSettings_OVTC29152} =    copy.deepcopy    ${hypervisorClusterSettings}
    Set To Dictionary    ${hypervisorClusterSettings_OVTC29152}    virtualSwitchType=Distributed    distributedSwitchVersion=${dvsVersion}    distributedSwitchUsage=GeneralNetworks
    Log    hypervisorClusterSettings for this test case:${hypervisorClusterSettings_OVTC29152}    console=True
    Log    Import Cluster    console=True
    ${payload}=    Create Import Cluster Payload    ${TEST_NAME}    OVTC29141_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name    ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    Delete Cluster By Name    ${TEST_NAME}    ${server_hardware_list}

OVTC33056
    [Documentation]    Import_OVF1024_23 - Import additional hosts to an existing cluster profile Distributed Switch
    ...    (All, General networks along with Netset)
    [Tags]    F323    P0
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC29141}    ${server_hardware_list}    ${target_vcenter}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    Log    Change the Switch type to DVS All Networks in hypervisorClusterSettings
    ${hypervisorClusterSettings_OVTC33056} =    copy.deepcopy    ${hypervisorClusterSettings}
    Set To Dictionary    ${hypervisorClusterSettings_OVTC33056}    virtualSwitchType=Distributed    distributedSwitchVersion=${dvsVersion}    distributedSwitchUsage=AllNetworks
    Log    hypervisorClusterSettings for this test case:${hypervisorClusterSettings_OVTC33056}    console=True
    Log    Import Cluster    console=True
    ${payload}=    Create Import Cluster Payload    ${TEST_NAME}    OVTC29141_SPT    ${hypervisorClusterSettings_OVTC33056}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name    ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    Create SP and Add Hosts to existing Cluster OOB    ${profiles_OVTC33056}    ${server_hardware_list_OVTC33056}    ${TEST_NAME}    ${target_vcenter}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    Remove from dictionary      ${hcp_response}      headers    status_code
    ${hypervisor_host_body}=     Create Hypervisor Hosts body    ${server_hardware_list_1[1:2]}
    set to dictionary    ${hcp_response}    addHostRequests=${hypervisor_host_body}
    ${import_response}=    Fusion Api Update Hypervisor Cluster Profile    body=${hcp_response}    uri=${hcp_response['uri']}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m

    [Teardown]    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1}

OVTC45327
    [Documentation]    Import - [netset only] - vCenter cluster with a Hosts on CLRM using Auto Address assignment with
    ...    SPT and Cluster shared volumes , netset in SPT
    [Tags]    F323    P0
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC45327}    ${server_hardware_list_1}    ${target_vcenter_OVTC45327}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${payload}=    Create Import Cluster Payload     ${TEST_NAME}    OVTC64029_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list_OVTC45327}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m     interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1}

OVTC64029
    [Documentation]   Import - [netset only] - add host to imported cluster (standard switch)
    [Tags]    F323    P0
    Fusion Api Login Appliance    ${ov_ip}     ${ov_credentials}
    Set To Dictionary    ${target_vcenter_38}    cluster    ${TEST_NAME}
    resource.Create Target Cluster    ${target_vcenter_38}
    Wait Until Keyword Succeeds    8 minutes    1 minutes      resource.Cluster should be present in CLRM    ${TEST_NAME}
    ${no_hardware}    Create List
    ${payload}=    resource.Create Import Cluster Payload     ${TEST_NAME}    OVTC64029_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${no_hardware}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    Log    Grow Cluster out of band
    resource.Create SP and Add Hosts to existing Cluster OOB    ${profiles_OVTC64029}    ${server_hardware_list_1[:2]}    ${TEST_NAME}    ${target_vcenter_38}
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    Remove from dictionary      ${hcp_response}      headers    status_code
    ${hypervisor_host_body}=     Create Hypervisor Hosts body    ${server_hardware_list_1[:2]}
    set to dictionary    ${hcp_response}    addHostRequests=${hypervisor_host_body}
    ${import_response}=    Fusion Api Update Hypervisor Cluster Profile    body=${hcp_response}    uri=${hcp_response['uri']}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    should be equal as integers     ${remediate_response['status_code']}      202
    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]    resource.Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1[:2]}

OVTC64031
    [Documentation]    Import - [netset only] - Remove host from imported cluster (standard switch)
    [Tags]    F323    P0
    [Setup]  resource.Create Prerequisties for Import    ${profiles_OVTC64029}    ${server_hardware_list_1[:2]}    ${target_vcenter_38}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${payload}=    resource.Create Import Cluster Payload     ${TEST_NAME}    OVTC64029_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list_1[:2]}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    Log    Shrink Cluster
    ${update_resp}      Update cluster profile    ${OVTC64031_update}    ${True}
    Wait For Task2    ${update_resp[0]['rest_resp']}    timeout=20m    interval=1m
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]     run keywords    resource.Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1[:2]}    AND
    ...    run keyword and ignore error     remove sp spt    ${profiles_OVTC64029}

OVTC64030
    [Documentation]    Import - [netset only] - add host to imported cluster (distributed switch)
    [Tags]    F323    P0
    Fusion Api Login Appliance    ${ov_ip}     ${ov_credentials}
    Set To Dictionary    ${target_vcenter_38}    cluster    ${TEST_NAME}
    resource.Create Target Cluster    ${target_vcenter_38}
    Wait Until Keyword Succeeds    8 minutes    1 minutes      resource.Cluster should be present in CLRM    ${TEST_NAME}
    Log    Change the Switch type to DVS All Networks in hypervisorClusterSettings
    ${hypervisorClusterSettings_OVTC64030} =    copy.deepcopy    ${hypervisorClusterSettings}
    Set To Dictionary    ${hypervisorClusterSettings_OVTC64030}    virtualSwitchType=Distributed    distributedSwitchVersion=${dvsVersion}    distributedSwitchUsage=AllNetworks
    Log    hypervisorClusterSettings for this test case:${hypervisorClusterSettings_OVTC64030}    console=True
    Log    Import Cluster    console=True
    ${no_hardware}    Create List
    ${payload}=    resource.Create Import Cluster Payload    ${TEST_NAME}    OVTC64029_SPT    ${hypervisorClusterSettings_OVTC64030}    ${virtualSwitchConfigPolicy}    ${no_hardware}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name    ${TEST_NAME}
    Log    Grow Cluster
    ${update_resp}      Update cluster profile    ${OVTC64030_update}    ${True}
    Wait For Task2    ${update_resp[0]['rest_resp']}    timeout=20m    interval=1m
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    should be equal as integers     ${remediate_response['status_code']}      202
    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]    resource.Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1[:2]}

OVTC64032
    [Documentation]    Import[UI] - [netset only] - Remove host from imported cluster (distributed switch)
    [Tags]    F323    P0
    [setup]  resource.Create Prerequisties for Import    ${profiles_OVTC64029}    ${server_hardware_list_1[:2]}    ${target_vcenter_38}    ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    Log    Change the Switch type to DVS All Networks in hypervisorClusterSettings
    ${hypervisorClusterSettings_OVTC64030} =    copy.deepcopy    ${hypervisorClusterSettings}
    Set To Dictionary    ${hypervisorClusterSettings_OVTC64030}    virtualSwitchType=Distributed    distributedSwitchVersion=${dvsVersion}    distributedSwitchUsage=AllNetworks
    Log    hypervisorClusterSettings for this test case:${hypervisorClusterSettings_OVTC64030}    console=True
    Log    Import Cluster    console=True
    ${payload}=    resource.Create Import Cluster Payload    ${TEST_NAME}    OVTC64029_SPT    ${hypervisorClusterSettings_OVTC64030}    ${virtualSwitchConfigPolicy}    ${server_hardware_list_1[:2]}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name    ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}

    Log    Shrink Cluster
    ${update_resp}      Update cluster profile    ${OVTC64032_update}    ${True}
    Wait For Task2    ${update_resp[0]['rest_resp']}    timeout=20m    interval=1m
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]     run keywords    resource.Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1[:2]}    AND
    ...    run keyword and ignore error     remove sp spt    ${profiles_OVTC64029}

OVTC63959
    [Documentation]   Import - [netset only] - Import pre-existing ESX Clusters (Standard switch)
    [Setup]  resource.Create Prerequisties for Import    ${profiles_OVTC64029}    ${server_hardware_list_1[:2]}    ${target_vcenter_38}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${payload}=    resource.Create Import Cluster Payload     ${TEST_NAME}    OVTC64029_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list_1[:2]}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]     run keywords    resource.Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1[:2]}    AND
    ...    run keyword and ignore error     remove sp spt    ${profiles_OVTC64029}

OVTC63960
    [Documentation]   Import - [netset only] - Import pre-existing ESX Clusters (Distributed switch)
    [Tags]    F323    P0
    [setup]  resource.Create Prerequisties for Import    ${profiles_OVTC64029}    ${server_hardware_list_1[:2]}    ${target_vcenter_38}    ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    Log    Change the Switch type to DVS All Networks in hypervisorClusterSettings
    ${hypervisorClusterSettings_OVTC64030} =    copy.deepcopy    ${hypervisorClusterSettings}
    Set To Dictionary    ${hypervisorClusterSettings_OVTC64030}    virtualSwitchType=Distributed    distributedSwitchVersion=${dvsVersion}    distributedSwitchUsage=AllNetworks
    Log    hypervisorClusterSettings for this test case:${hypervisorClusterSettings_OVTC64030}    console=True
    Log    Import Cluster    console=True
    ${payload}=    resource.Create Import Cluster Payload    ${TEST_NAME}    OVTC64029_SPT    ${hypervisorClusterSettings_OVTC64030}    ${virtualSwitchConfigPolicy}    ${server_hardware_list_1[:2]}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name    ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    resource.Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1[:2]}
    [Teardown]     run keyword and ignore error     remove sp spt    ${profiles_OVTC64029}

OVTC33064
    [Documentation]    ClusterImport_OVF1024_31 - Import Hypervisor cluster with multiple networks and volume specified only in SPT.
    [Tags]    F323    P0
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC33064}    ${server_hardware_list_1}    ${target_vcenter}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${payload}=    Create Import Cluster Payload     ${TEST_NAME}    OVTC29141_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list_1}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m    errorMessage=Import Cluster failed
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    run keywords
    ...    should be equal as integers     ${remediate_response['status_code']}      202    AND
    ...    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed   AND
    ...    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1}

OVTC33082
    [Documentation]    Import_OVF1024_45 - Import of a cluster with host where host is part of a different datacenter than the cluster.
    [Tags]    F323    P0
    [Setup]  Test Setup to Add Hosts in Datacenter    ${profiles_OVTC33082}    ${server_hardware_list_1}    ${target_vcenter}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}    ${host_datacenter}
    ${payload}=    Create Import Cluster Payload     ${TEST_NAME}    OVTC29141_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list_1}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m    errorMessage=Import Cluster failed
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    run keywords
    ...    should be equal as integers     ${remediate_response['status_code']}      202    AND
    ...    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed   AND
    ...    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1}

OVTC33070
    [Documentation]    Import_OVF1024_37 - Delete imported cluster profile - [Standard Switch]
    [Tags]    F323    P0
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC33070}    ${server_hardware_list}    ${target_vcenter}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${payload}=    Create Import Cluster Payload     ${TEST_NAME}    OVTC29141_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list}

OVTC33063
    [Documentation]    UI: Import Hypervisor cluster with multiple networks and volumes
    [Tags]    F323    P0
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC33063}    ${server_hardware_list}    ${target_vcenter}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${payload}=    Create Import Cluster Payload     ${TEST_NAME}    OVTC29141_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}
    ${extra_attachments}=    Create Shared Storage body for extra volumes attachment   ${cluster_extra_volumes}
    ${attach}=     Evaluate    $extra_attachments+$payload['sharedStorageVolumes']
    set to dictionary    ${payload}    sharedStorageVolumes=${attach}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list}

OVTC29151
    [Documentation]    ClusterImport_22 - Shrink imported cluster by removing a host from it and
    ...    delete one permanent existing volume
    [Tags]    F323    P0
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC29151}    ${server_hardware_list_1[1:2]}    ${target_vcenter}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${payload}=    Create Import Cluster Payload     ${TEST_NAME}    OVTC29144_SPT_1    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list_1[1:2]}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    Fusion Api Login Appliance    ${ov_ip}     ${ov_credentials}
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    Update cluster    ${OVTC29151_update1}    ${True}
    should be equal as integers     ${cluster_response['status_code']}      202
    Wait For Task2    ${cluster_response}    timeout=5m    interval=1m
    Update cluster    ${OVTC29151_update2}    ${True}
    should be equal as integers     ${cluster_response['status_code']}      202
    Wait For Task2    ${cluster_response}    timeout=5m    interval=1m
    [Teardown]    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1[1:2]}

OVTC29150
    [Documentation]    ClusterImport_05 - Import vCenter cluster with Host with  Teamed/Redundant Nics
    ...    (All, General networks along with Tunnel Network) and with storage volumes on CLRM
    [Tags]    F323    P0
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC29150}    ${server_hardware_list_1[:2]}    ${target_vcenter}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${payload}=    Create Import Cluster Payload     ${TEST_NAME}    OVTC29150_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list_1[1:2]}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1[1:2]}

OVTC63961
    [Documentation]   Import - [netset only] - Cluster with standard switch, portgroup for mgmt only(tagged),
    ...    unparented SP (singleNIC) and SPT with multiNIC
    [Tags]    OVF1024    P0
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC63961}    ${server_hardware_list_1[1:2]}    ${target_vcenter}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${payload}=    Create Import Cluster Payload     ${TEST_NAME}    OVTC64029_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list_1[1:2]}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}
    [Teardown]    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1[1:2]}

OVTC45342
    [Documentation]   Import - OVF1024_75 - Import with Managed manually switch settings
    [Tags]    OVF1024    P0
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC45342}    ${server_hardware_list_1[1:2]}    ${target_vcenter}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${virtualSwitchConfigPolicy_OVTC45342} =    copy.deepcopy    ${virtualSwitchConfigPolicy}
    Set To Dictionary    ${virtualSwitchConfigPolicy_OVTC45342}    manageVirtualSwitches=False
    ${hypervisorClusterSettings_OVTC45342} =    copy.deepcopy    ${hypervisorClusterSettings}
    Set To Dictionary    ${hypervisorClusterSettings_OVTC45342}    haEnabled=True
    ${payload}=    Create Import Cluster Payload     ${TEST_NAME}    OVTC29144_SPT_1    ${hypervisorClusterSettings_OVTC45342}    ${virtualSwitchConfigPolicy_OVTC45342}    ${server_hardware_list_1[1:2]}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    FAIL    Clusterprofile is Inconsistent
    HCP_create_validation    ${payload}
    # Validate the functionality by changing cluster / switch settings from SPT and VCenter
    # Update cluster settings OOB and expect a compliance alert. Resolve it.
    ${cluster_ha}=      Get from Dictionary     ${hcp_response['hypervisorClusterSettings']}      haEnabled
    ${flip_ha}=     Evaluate    not $cluster_ha
    Reconfigure HA      ${hcp_response['name']}     ${flip_ha}
    Log    Waiting for the cluster to became Inconsistent,Wait time is for 5 min maximum      console=True
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${cluster_uri}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    Should be equal     ${hcp_response['complianceState']}      ClusterConfigInconsistent
    ${remediate_response}=    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    # Update connection bandwidth from SPT. Expect a compliance alert
    ${spt_response}=      Fusion Api Get Server Profile Templates       ${hcp_response['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Remove from dictionary      ${spt_response}      headers    status_code
    ${Connections}=     Get From Dictionary     ${spt_response['connectionSettings']}     connections
    :For    ${connection}   in      @{Connections}
    \   ${resp}=    Fusion Api Get Ethernet Networks      ${connection['networkUri']}
    \   Run keyword if      '${resp['category']}' != 'ethernet-networks'    Continue for loop
    \   Run keyword if      '${resp['purpose']}' == 'Management'    run keywords
    \   ...     set to Dictionary      ${connection}      requestedMbps=2000     AND
    \   ...     Exit for loop
    Remove from dictionary      ${spt_response}      headers    status_code
    ${spt_edit_response}=    Fusion Api Edit Server Profile Template     ${spt_response}     uri=${hcp_response['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Wait For Task2  ${spt_edit_response}  300  5
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${cluster_uri}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    Should be equal     ${hcp_response['complianceState']}      HostProfileInconsistent
    ${remediate_response}=    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    Should be equal     ${hcp_response['complianceState']}      Consistent
    # Remove vswitch from VCenter and expect no Compliance alert to come.
    ${host_ip} =     Get Ip From Host Profile    ${hcp_response['hypervisorHostProfileUris'][0]}
    Vswitch Should Exist     ${host_ip}    ${OVTC45342_switch_name}
    Remove Vswitch      ${host_ip}    ${OVTC45342_switch_name}
    Log    Waiting for the cluster to stay consistent, Wait time is maximum
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Be Consistent    ${hcp_response['uri']}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    Should be equal     ${hcp_response['complianceState']}      Consistent
    [Teardown]    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1[1:2]}

OVTC45337
    [Documentation]    Import - Import cluster and thereafter migrate server profile to another server hardware
    ...     Subsequrnt grow -shrink should be successful
    [Tags]    F323    P0
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC45337}    ${server_hardware_list_1[:1]}    ${target_vcenter_38}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${payload}=    Create Import Cluster Payload     ${TEST_NAME}    OVTC29141_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list_1[:1]}
    ${import_response}=    Fusion Api Create Hypervisor Cluster Profile    body=${payload}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${TEST_NAME}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${remediate_response}=    Run Keyword If    '${hcp_response['complianceState']}' != 'Consistent'    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    HCP_create_validation    ${payload}

    Power off host profile and migrate server hardware    ${TEST_NAME}1    ${profiles_OVTC45337}    ${profiles_OVTC45337_update}    ${target_vcenter_38}
    Log    Grow Cluster
    Grow cluster from OV    ${cluster_uri}    ${OVTC45337_grow}
    Log    Shrink Cluster
    Shrink cluster from OV    ${cluster_uri}    ${OVTC45337_shrink}

    [Teardown]    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list_1}

OVTC33054
    [Documentation]     Import additional host(1 or more) to an existing Hypervisor cluster profile.
    ...   Host is added OOB to a different cluster created from CLRM. Distributed switch(General/AllNetworks)
    [setup]  Create Prerequisties for Import    ${profiles_OVTC29141}    ${server_hardware_list}    ${target_vcenter}    ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    Log    Change the Switch type to DVS All Networks in hypervisorClusterSettings
    ${hypervisorClusterSettings_OVTC29146} =    copy.deepcopy    ${hypervisorClusterSettings}
    Set To Dictionary    ${hypervisorClusterSettings_OVTC29146}    virtualSwitchType=Distributed    distributedSwitchVersion=6.6.0    distributedSwitchUsage=AllNetworks
    Log    hypervisorClusterSettings for this test case:${hypervisorClusterSettings_OVTC29146}    console=True
    Log    Import Cluster    console=True

    Import Cluster     ${TEST_NAME}    OVTC29141_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}

    Log    Creating new cluster with extra node
    ${profiles_OVTC33054} =    copy.deepcopy    ${profiles_OVTC29141}
    Set To Dictionary    ${profiles_OVTC33054[0]}    name=OVTC33054_SP    serverHardwareUri=SH:${server_hardware_list_1[1:][0]}
    Create cluster    ${OVTC33054_cluster}    ${True}
    Create Prerequisties for Import    ${profiles_OVTC33054}    ${server_hardware_list_1[1:]}    ${target_vcenter}    ${TEST_NAME}_1    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${cluster_uri}=    Get Cluster Profile Uri by Name    ${TEST_NAME}

    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    Remove from dictionary      ${hcp_response}      headers    status_code

    ${hypervisor_host_body}=     Create Hypervisor Hosts body    ${server_hardware_list_1[1:]}
    set to dictionary    ${hcp_response}    addHostRequests=${hypervisor_host_body}

    ${import_response}=    Fusion Api Update Hypervisor Cluster Profile    body=${hcp_response}    uri=${hcp_response['uri']}
    should be equal as integers     ${import_response['status_code']}      202
    Wait For Task2    ${import_response}    timeout=5m    interval=1m    errorMessage=HYPERVISOR_ALREADY_IN_DIFFERENT_CLUSTER    PASS=((?i)Error|Warning)

    [Teardown]    run keywords    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list}    AND
    ...    Delete Cluster By Name     ${TEST_NAME}_1    ${server_hardware_list}    AND
    ...    Power off Server    ${server_hardware_list_1[1:][0]}    powerControl=PressAndHold    AND
    ...    run keyword and ignore error     remove sp spt    ${profiles_OVTC33054}

OVTC63963
    [Documentation]   Import - [netset only] - migrate switch to distributed (all networks) during import
    [Tags]    OVF1024    P0
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC63963}    ${server_hardware_list}    ${target_vcenter}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${hypervisorClusterSettings_OVTC63963} =    copy.deepcopy    ${hypervisorClusterSettings}
    Set To Dictionary    ${hypervisorClusterSettings_OVTC63963}    virtualSwitchType=Distributed    distributedSwitchVersion=6.6.0    distributedSwitchUsage=AllNetworks
    Log    hypervisorClusterSettings for this test case:${hypervisorClusterSettings_OVTC63963}    console=True
    Log    Import Cluster    console=True
    Import Cluster    ${TEST_NAME}    OVTC64029_SPT    ${hypervisorClusterSettings_OVTC63963}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}
    [Teardown]    run keywords    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list}    AND
    ...    run keyword and ignore error     remove sp spt    ${profiles_OVTC63963}

OVTC63964
    [Documentation]   Import - [netset only] - migrate switch to distributed (all networks) after import
    [Tags]    OVF1024    P0
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC63963}    ${server_hardware_list}    ${target_vcenter}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    Log    Import Cluster    console=True
    Import Cluster    ${TEST_NAME}    OVTC64029_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}
    ${cluster_uri}=    Get Cluster Profile Uri by Name    ${TEST_NAME}
    ${hypervisorClusterSettings_OVTC63964} =    copy.deepcopy    ${hypervisorClusterSettings}
    Set To Dictionary    ${hypervisorClusterSettings_OVTC63964}    virtualSwitchType=Distributed    distributedSwitchVersion=6.6.0    distributedSwitchUsage=1
    ...    drsEnabled=True    haEnabled=True    multiNicVMotion=True
    Log    hypervisorClusterSettings for this test case:${hypervisorClusterSettings_OVTC63964}    console=True
    ${update_cluster_response}=    Migrate Networks in Cluster    ${cluster_uri}    ${hypervisorClusterSettings_OVTC63964}     ${virtualSwitchConfigPolicy}
    should be equal as integers     ${update_cluster_response['status_code']}      202
    Wait For Task2    ${update_cluster_response}    timeout=10m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${cluster_uri}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    Should be equal     ${hcp_response['complianceState']}      HostProfileInconsistent
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Remediate Failed while deleting the network set
    [Teardown]    run keywords    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list}    AND
    ...    run keyword and ignore error     remove sp spt    ${profiles_OVTC63963}

OVTC63965
    [Documentation]   Import - [netset only] - migrate switch to distributed (General networks) after import
    [Tags]    OVF1024    P0
    [Setup]  Create Prerequisties for Import    ${profiles_OVTC63963}    ${server_hardware_list}    ${target_vcenter}   ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    Log    Import Cluster    console=True
    Import Cluster    ${TEST_NAME}    OVTC64029_SPT    ${hypervisorClusterSettings}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}
    ${cluster_uri}=    Get Cluster Profile Uri by Name    ${TEST_NAME}
    ${hypervisorClusterSettings_OVTC63964} =    copy.deepcopy    ${hypervisorClusterSettings}
    Set To Dictionary    ${hypervisorClusterSettings_OVTC63964}    virtualSwitchType=Distributed    distributedSwitchVersion=6.6.0    distributedSwitchUsage=0
    ...    drsEnabled=True    haEnabled=True    multiNicVMotion=True
    Log    hypervisorClusterSettings for this test case:${hypervisorClusterSettings_OVTC63964}    console=True
    ${update_cluster_response}=    Migrate Networks in Cluster    ${cluster_uri}    ${hypervisorClusterSettings_OVTC63964}     ${virtualSwitchConfigPolicy}
    should be equal as integers     ${update_cluster_response['status_code']}      202
    Wait For Task2    ${update_cluster_response}    timeout=10m    interval=1m    errorMessage=Remediate Failed
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${cluster_uri}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    Should be equal     ${hcp_response['complianceState']}      HostProfileInconsistent
    ${Hypervisor_count}=     Get length      ${hcp_response['hypervisorHostProfileUris']}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    errorMessage=Remediate Failed while deleting the network set
    [Teardown]    run keywords    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list}    AND
    ...    run keyword and ignore error     remove sp spt    ${profiles_OVTC63963}

OVTC33040
    [Documentation]    Import_OVF1024_7 - Import of cluster with ISCSI volume(Import of cluster with ISCSI volume in CLRM (POST) - vmfs and Unmanaged)
    [Tags]    OVF1024    P0
    [Setup]    Create Prerequisties for Import    ${profiles_OVTC33040}    ${server_hardware_list}    ${target_vcenter}    ${TEST_NAME}    ${enclosure_type}    ${deploy_configs}    ${mgmt_net}    ${mgmt_nic}
    ${hypervisorClusterSettings_OVTC33040} =    copy.deepcopy    ${hypervisorClusterSettings}
    Set To Dictionary    ${hypervisorClusterSettings_OVTC33040}    drsEnabled=True
    ${spt_body}=   Fusion Api Get Server Profile Templates    param=?filter="'name'==OVTC33040_SPT"
    ${volumes}=    Get From Dictionary     ${spt_body['members'][0]['sanStorage']}    volumeAttachments
    ${volume_list} =    Create List    ${volumes[0]['volumeUri']}
    Import Cluster    ${TEST_NAME}     OVTC33040_SPT    ${hypervisorClusterSettings_OVTC33040}    ${virtualSwitchConfigPolicy}    ${server_hardware_list}    ${volume_list}
    ${cluster_uri}=    Get Cluster Profile Uri by Name    ${TEST_NAME}
    Connect To VI Server   ${target_vcenter['vc']}  ${target_vcenter['user']}   ${target_vcenter['password']}
    rename_datastore    ${OVTC33040_volume_name}    ${OVTC33040_volume_name}_new    ${target_vcenter['datacenter']}
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Should Not Be Consistent    ${cluster_uri}
    ${remediate_response}=    Remediate cluster profile Inconsistent    ${cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=20m    interval=1m
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    [Teardown]    run keywords    Delete Cluster By Name     ${TEST_NAME}    ${server_hardware_list}    AND
    ...    run keyword and ignore error     remove sp spt    ${profiles_OVTC33040}