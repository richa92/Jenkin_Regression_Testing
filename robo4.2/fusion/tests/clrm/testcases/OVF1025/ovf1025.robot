*** Settings ***
Documentation       Automate presentation of iSCSI-attached StoreVirtual volumes to ESXi
...                 This expects atleast All the Hardwares in working conditions

Resource        ../../../../Resources/api/fusion_api_resource.txt
Resource        ../../support_files/clrm_common.txt
Resource        ../SPT/resource.txt
Resource        resource.robot
Resource        ../ovf379_380/resource.txt
Library         ../../support_files/clrm_support_functions.py
Variables       ovf1025.py

Suite Setup                     Setup Suite environment    ${APPLIANCE_IP}
Suite Teardown                  Fusion Api Logout Appliance


*** Variables ***

${X-Api-Version}    1000

*** Test Cases ***

OVTC29102
    [Documentation]            PUT on existing cluster profile with iSCSI volume
    ...           to add host and two ISCSI volumes
    [Tags]        OVF1025              Positive
    Create SPT    ${SPT_iSCSI_Vol_2}    ${True}
    Create cluster     ${HCP_iSCSI_Vol_2}    ${True}
    ${spt_response}=    update SPT with volume    ${SPT_iSCSI_Vol_2_update}
    should be equal as integers     ${spt_response['status_code']}      202
    Wait For Task2    ${spt_response}    timeout=5m    interval=1m
    Update cluster    ${HCP_iSCSI_Vol_2_update}    ${True}
    Get cluster    ${HCP_iSCSI_Vol_2_update}
    Delete cluster    ${HCP_iSCSI_Vol_2_update}    ${false}
    [Teardown]    run keyword and return status    Delete cluster    ${HCP_iSCSI_Vol_2_update}    ${false}

OVTC29120
    [Documentation]            Create cluster using SPT having network variations
    [Tags]        OVF1025              Positive
    Create SPT    ${SPT_iSCSI_Vol_21}    True
    Create cluster    ${HCP_iSCSI_Vol_21}    ${True}
    Get cluster    ${HCP_iSCSI_Vol_21}
    Delete cluster    ${HCP_iSCSI_Vol_21}    ${False}
    [Teardown]    run keyword and return status    Delete cluster    ${HCP_iSCSI_Vol_21}    ${False}

OVTC29106
    [Documentation]            Edit cluster to delete shared iSCSI volumes
    [Tags]        OVF1025                Positive
    Create SPT    ${SPT_iSCSI_Vol_6}    ${True}
    Create cluster    ${HCP_iSCSI_Vol_6}    ${True}
    Get cluster    ${HCP_iSCSI_Vol_6}
    Update cluster    ${HCP_iSCSI_Vol_6_update}    ${True}
    [Teardown]    run keyword and return status    Delete cluster    ${HCP_iSCSI_Vol_6}    ${False}

OVTC29107
    [Documentation]  iSCSI_Vol_7-Shrink cluster to remove some hosts - should not remove iSCSI volume
    [Tags]        OVF1025              Positive
    Create SPT    ${SPT_iSCSI_Vol_7}    True
    Create cluster     ${HCP_iSCSI_Vol_7}    ${True}
    Update cluster    ${HCP_iSCSI_Vol_7_update}    ${True}
    Connect to VI Server    ${vCenterIp}    ${vCenterUsername}    ${VcenterPassword}
    :For    ${volume}    in    @{HCP_iSCSI_Vol_7[0]['shared_volume']}
    \    Datastore Should Exist cluster     ${HCP_iSCSI_Vol_7[0]['name']}    ${volume['name']}    ${data_center}
    Disconnect From VI Server
    [Teardown]    Run Keywords     Delete cluster    ${HCP_iSCSI_Vol_7}    ${True}    AND    Fusion Api Delete Server Profile Template    name=${SPT_iSCSI_Vol_7[0]['name']}

OVTC29124
    [Documentation]            Create cluster with Distributed-All switch configuration
    [Tags]        OVF1025                Positive
    Create SPT    ${SPT_iSCSI_Vol_25}    ${True}
    Create cluster    ${HCP_iSCSI_Vol_25}    ${True}
    Get cluster    ${HCP_iSCSI_Vol_25}
    [Teardown]    run keyword and return status    Delete cluster    ${HCP_iSCSI_Vol_25}    ${False}

OVTC29111
    [Documentation]    Name:iSCSI_Vol_12 Create cluster from CLRM (Test 1) and delete the iSCSI volume from SPT.
     ...    Check cluster profile is consistent
    Create SPT    ${SPT_iSCSI_Vol_12}   isPositive=True
    Create cluster    ${HCP_iSCSI_Vol_12}    ${True}
    update SPT with volume    ${SPT_iSCSI_Vol_12_update}
    ${cluster_uri}=    Get Cluster Profile Uri by Name     ${HCP_iSCSI_Vol_12[0]['name']}
    run keyword if     ${cluster_uri}==${None}   FAIL    Get cluster is not valid
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster should be Consistent    ${cluster_uri}
    delete cluster    ${HCP_iSCSI_Vol_12}    ${True}
    [Teardown]    run keywords    run keyword and ignore error    delete cluster    ${HCP_iSCSI_Vol_12}    ${True}    AND
     ...    run keyword and ignore error    remove sp spt    ${SPT_iSCSI_Vol_12}

OVTC29125
    [Documentation]  iSCSI_Vol1-POST on cluster profile with iSCSI volume and host
    [Tags]        OVF1025              Positive
    Create SPT    ${SPT_iSCSI_Vol_7}    True
    Create cluster     ${HCP_iSCSI_Vol_1}    ${True}
    Connect to VI Server    ${vCenterIp}    ${vCenterUsername}    ${VcenterPassword}
    :For    ${volume}    in    @{HCP_iSCSI_Vol_1[0]['shared_volume']}
    \    Datastore Should Exist cluster     ${HCP_iSCSI_Vol_1[0]['name']}    ${volume['name']}    ${data_center}
    Disconnect From VI Server
    [Teardown]    Run Keywords     Delete cluster    ${HCP_iSCSI_Vol_1}    ${True}    AND    Fusion Api Delete Server Profile Template    name=${SPT_iSCSI_Vol_7[0]['name']}

OVTC29123
    [Documentation]    Create cluster using various Network configuration for the iSCSI like VMNIC configurations- DVS (General)
    [Tags]        OVF1025              Positive
    ${force}=    Convert to boolean   False
    ${validation}=    Convert to boolean   True
    Create SPT    ${SPT_iSCSI_Vol_24}    True
    Create cluster    ${HCP_iSCSI_Vol_24}    ${validation}
    Get cluster    ${HCP_iSCSI_Vol_24}
    Delete cluster    ${HCP_iSCSI_Vol_24}    ${force}
   [Teardown]    run keyword and return status    Delete cluster    ${HCP_iSCSI_Vol_24}    ${force}

OVTC29105
    [Documentation]     iSCSI_Vol_5-Edit of ISCSI volume on already created cluster should display in storage tab
    [Tags]        OVF1025              Positive
    ${force}=    Convert to boolean   False
    ${validation}=    Convert to boolean   True
    Create SPT    ${SPT_iSCSI_Vol_5}    True
    Create cluster    ${HCP_iSCSI_Vol_5}    ${validation}
    Edit Storage Volume    ${HCP_iSCSI_Vol_5_update}
    Get cluster    ${HCP_iSCSI_Vol_5}
    Delete cluster    ${HCP_iSCSI_Vol_5}    ${force}
   [Teardown]    run keyword and return status    Delete cluster    ${HCP_iSCSI_Vol_5}    ${force}

OVTC29109
    [Documentation]     iSCSI_Vol_9-Delete cluster to remove the iSCSI volume's association from the Cluster Profile
    [Tags]        OVF1025              Positive
    Create SPT    ${SPT_iSCSI_Vol_5}    True
    Create cluster    ${HCP_iSCSI_Vol_5}    ${True}
    Get cluster    ${HCP_iSCSI_Vol_5}
    ${status}=    Verify Volume association to cluster    ${HCP_iSCSI_Vol_5[0]['shared_volume'][0]['name']}    ${HCP_iSCSI_Vol_5[0]['name']}
    Should Be True     ${status}
    Delete cluster    ${HCP_iSCSI_Vol_5}    ${False}
    ${status}=    Verify Volume association to cluster    ${HCP_iSCSI_Vol_5[0]['shared_volume'][0]['name']}    ${HCP_iSCSI_Vol_5[0]['name']}
    Should Not Be True     ${status}
   [Teardown]    run keyword and return status    Delete cluster    ${HCP_iSCSI_Vol_5}    ${False}

OVTC29104
    [Documentation]     Addition of ISCSI volume on allready created cluster should display in storage tab
    [Tags]        OVF1025              Positive
    Create SPT    ${SPT_iSCSI_Vol_8}    True
    Create cluster     ${HCP_iSCSI_Vol_30}    ${True}
    Update cluster    ${HCP_iSCSI_Vol_30_update}    ${True}
    ${host_ips}=    Get Ips from cluster    ${HCP_iSCSI_Vol_30}
    Connect to VI Server    ${vCenterIp}    ${vCenterUsername}    ${VcenterPassword}
    :For    ${host}     In      @{host_ips}
    \    Datastore Should Exist     ${host}    ${added_volume}
    Disconnect From VI Server
    [Teardown]    run keyword and return status    Delete cluster    ${HCP_iSCSI_Vol_30}    ${force}

OVTC29122
    [Documentation]     Need Network configuration for the iSCSI by covering VMNIC configurations- Standard
    [Tags]        OVF1025              Positive
    Create SPT    ${SPT_iSCSI_Vol_10}    True
    Create cluster     ${HCP_iSCSI_Vol_31}    ${True}
    ${host_ips}=    Get Ips from cluster    ${HCP_iSCSI_Vol_31}
    Connect to VI Server    ${vCenterIp}    ${vCenterUsername}    ${VcenterPassword}
    :For    ${host}     In      @{host_ips}
    \    ${vswitch_list}=    Get Host vswitches    ${host}
    \    List Should Contain Value    ${vswitch_list}    ${vswitch_name}
    Disconnect From VI Server
    [Teardown]    run keyword and return status    Delete cluster    ${HCP_iSCSI_Vol_31}    ${False}

*** Keywords ***

Setup Suite environment
    [Documentation]    Setup Suite environment
    [Arguments]        ${APPLIANCE_IP}
    Set Log Level    Trace
    connect_to_vi_server    ${vCenterIp}    ${vCenterUsername}    ${VcenterPassword}
    Run keyword and ignore error    create_datacenter    ${data_center}
    disconnect_from_vi_server
    Fusion Api Login Appliance    ${APPLIANCE_IP}     ${admin_credentials}