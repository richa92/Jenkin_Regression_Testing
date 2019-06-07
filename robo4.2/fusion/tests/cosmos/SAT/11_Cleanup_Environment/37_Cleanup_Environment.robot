*** Settings ***
Documentation
...     This Test Suite uses administrator credentials to clean Server Profiles, Server Profile Templates, Storage Volumes, Enclosures
...     Test Data is defined in Python Data Variable file.
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Regression Test Teardown

*** Test Cases ***
Power Off VM
    [Tags]    ESXI  POWEROFF    C7000-cleanup
    [Documentation]   Power Off The VM
    connect_to_vi_server  ${vi_server_details['vcenter']}    ${vi_server_details['username']}    ${vi_server_details['password']}
    vi_server_should_be_connected
    power_off_vm   ${cluster_vm['name']}

Enter Maintenance Mode For ESXir Hosts
    [Tags]    ESXI  EXIT    C7000-cleanup
    [Documentation]   Enter Maintenance Mode For ESXir Hosts
    Enter Maintenance Mode For Hosts   ${esxi_os_servers}
    Enter Maintenance Mode For Hosts   ${esxi_os_servers_post_upgrade}

Remove Hosts In Cluster
    [Tags]    ESXI  REMOVE    C7000-cleanup
    connect_to_vi_server  ${vi_server_details['vcenter']}    ${vi_server_details['username']}    ${vi_server_details['password']}
    vi_server_should_be_connected
    ${hosts}     get_hosts_in_cluster   ${vi_server_details['cluster']}
    :FOR  ${ip}  IN  @{hosts}
    \    ${status}    remove_host_in_cluster   ${vi_server_details['cluster']}   ${ip}
    \    Run Keyword if    ${status} == 'None'   Fail  No hosts found: ${ip} to delete in the cluster

Cleanup Server Profiles
    [Tags]    CLEANUP-ENV  CLEANUP-SP  C7000-cleanup  TBIRD-cleanup
    [Documentation]     Remove Server Profiles
    ${profiles} =    Fusion Api Get Server Profiles
    :FOR    ${profile}  IN  @{profiles['members']}
    \   Run Keyword If  '${profile['serverHardwareUri']}' == 'None'     Continue For Loop
    \   ${server} =   Fusion Api Get Server Hardware  uri=${profile['serverHardwareUri']}
    \   Power off Server    ${server['name']}
    ${responses} =  Remove All Server Profiles Async    ${True}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}   timeout=3000    interval=15
    Run Keyword If  ${responses} is not ${Null}  Verify Server profile exists

Cleanup Server Profile Templates
    [Tags]    CLEANUP-ENV  CLEANUP-SPT  C7000-cleanup  TBIRD-cleanup
    [Documentation]     Remove Server Profile Templates, Storage Volumes, Enclosures
    Remove All Server Profile Templates Async

Remove Logical Enclosure
    [Documentation]     Remove Logical Enclosure from OV
    [Tags]   CLEANUP-ENV  CLEANUP-LE  TBIRD-cleanup
    Remove All LEs Async

Clean Virtual Volumes From Host And 3PAR
     [Tags]    CLEANUP-ENV  CLEANUP-VLUNS  TBIRD-cleanup  C7000-cleanup
     [Documentation]     Clean Virtual Volumes From Host And 3PAR
     Storage3par Open Connection    ${storage_system[0]["hostname"]}    ${storage_system[0]["username"]}   ${storage_system[0]["password"]}
     Cleanup All Vluns   ${remove_iscsi_exported_volumes}
     Storage3par Close Connection

Cleanup Storage Volumes
    [Tags]    CLEANUP-ENV  CLEANUP-SV  C7000-cleanup  TBIRD-cleanup
    [Documentation]     Remove Storage Volumes
    ${response_e} =  Remove Storage Volumes Async  ${delete_storage_volumes_ov_only}   ?suppressDeviceUpdates=true
    ${response_n} =  Remove Storage Volumes Async  ${delete_storage_volumes}  ?suppressDeviceUpdates=false
    Run Keyword If  ${response_e} is not ${null}    Run Keyword And Continue On Failure  Wait For Task2  ${response_e}
    Run Keyword If  ${response_n} is not ${null}    Run Keyword And Continue On Failure  Wait For Task2  ${response_n}
    Storage Volumes Should Not Be Found     ${delete_storage_volumes_ov_only}
    Storage Volumes Should Not Be Found     ${delete_storage_volumes}
    Remove ALL Storage Volumes Async   ?suppressDeviceUpdates=true
    Remove All Storage Volume Templates Async
    Remove ALL Storage Systems Async

Remove Firmware Bundle
    [Tags]    CLEANUP-ENV  CLEANUP-SPP  TBIRD-cleanup    C7000-cleanup
    [Documentation]        Remove SPP Firmware Bundles from OneView appliance
    ${resp} =   Remove All Firmware Bundles
    Run Keyword If  ${resp} is not ${null}     Wait For Task2   ${resp}

Cleanup Enclosures
    [Tags]    CLEANUP-ENV  CLEANUP-ENC  C7000-cleanup
    [Documentation]     Remove Enclosures
    Remove All Enclosures async     VERIFY=${TRUE}    timeout=900
**************
Remove EG
    [Tags]    CLEANUP-ENV  CLEANUP-EG  TBIRD-cleanup    C7000-cleanup
    [Documentation]        Remove Enclosure Group from OneView appliance
    Remove All Enclosure Groups     ${VERIFY}

Remove LIG
    [Tags]    CLEANUP-ENV  CLEANUP-LIG  TBIRD-cleanup    C7000-cleanup
    [Documentation]        Remove All LIGs and SAS LIGs from OneView appliance
    Remove All LIGS     ${VERIFY}
    Remove All SAS LIGs      ${VERIFY}

Remove Network Set
    [Tags]    CLEANUP-ENV  CLEANUP-NS  TBIRD-cleanup    C7000-cleanup
    [Documentation]        Remove NetworkSets from OneView appliance
    Remove All Networks Sets Async      ${VERIFY}

Remove All Ethernet Network
    [Tags]    CLEANUP-ENV  CLEANUP-ETH  TBIRD-cleanup    C7000-cleanup
    [Documentation]        Remove Ethernet Networks from OneView appliance
    Remove All Ethernet Networks Async  ${VERIFY}

Remove FC Network
    [Tags]    CLEANUP-ENV  CLEANUP-FC  TBIRD-cleanup    C7000-cleanup
    [Documentation]        Remove FC Networks from OneView appliance
    Remove All FC Networks Async    ${VERIFY}

Remove FCOE Network
    [Tags]    CLEANUP-ENV  CLEANUP-FCOE    TBIRD-cleanup    C7000-cleanup
    [Documentation]        Remove FCOE Networks from OneView appliance
    Remove All FCoE Networks
    ${resp} =   Fusion Api Get Fcoe Networks
    Run Keyword Unless  '${resp['count']}' == '0'    Fail     msg=Not All FCoE Networks were deleted

Cleanup San Managers
    [Tags]  CLEANUP-ENV  CLEANUP-SAN-MNG  TBIRD-cleanup    C7000-cleanup
    [Documentation]   Remove all SAN Managers
    Remove ALL San Managers Async

Remove Rack
    [Tags]    CLEANUP-ENV  CLEANUP-RACK  TBIRD-cleanup
    [Documentation]        Remove Racks from OneView appliance
    # Remove all the Racks
    ${resp} =    Fusion Api Remove Rack
    Run Keyword If  ${resp} is not ${null}     Wait For Task2    ${resp}

Remove DataCenter
    [Tags]    CLEANUP-ENV  CLEANUP-DC  TBIRD-cleanup
    [Documentation]        Remove Datacenter from OneView appliance
    # Remove all the DataCenters
    ${resp} =   Fusion Api Remove Datacenter
    Run Keyword If  ${resp} is not ${null}     Wait For Task2    ${resp}