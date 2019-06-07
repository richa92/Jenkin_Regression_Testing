*** Settings ***
Documentation
...     This Test Suite uses AD server Group User credentials to add hosts to cluster and perform ping test for vms on the cluster.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                   CLUSTER
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${ad_server_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  T-BIRD  C7000  4.0  3.10
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${esxi_os_servers_post_upgrade}

Add ESXi Hosts To Cluster
    [Tags]    HOSTS    C7000    4.0    3.10   T-BIRD
    [Documentation]     Add hosts to cluster
    Add Hosts To Cluster  ${esxi_os_servers_post_upgrade}  ${vi_server_details}

Exit Maintenance Mode For ESXi Hosts
    [Tags]    EXIT    C7000    4.0    3.10
    [Documentation]     Exit Maintenance Mode For ESXi Hosts
    Exit Maintenance Mode For Hosts   ${esxi_os_servers_post_upgrade}

Connect To Vsphere Server, Power On The VM And Windows OS Should Be Pinging
    [Tags]    POWERON-Test    C7000   T-BIRD
    [Documentation]   Connect To Vsphere Server, Power On The VM And Windows OS Should Be Pinging
    connect_to_vi_server  ${vi_server_details['vcenter']}    ${vi_server_details['username']}    ${vi_server_details['password']}
    vi_server_should_be_connected
    ${status}      get_status_of_vm    ${vi_server_details['vcenter']}    ${vi_server_details['username']}    ${vi_server_details['password']}   ${cluster_vm['name']}
    Run Keyword If  '${status}' == 'POWERED OFF'   Power On The VM     ${cluster_vm}
    Wait Until Keyword Succeeds    ${timeout}    ${interval}  Windows OS Should Be Pinging   ${cluster_vm}