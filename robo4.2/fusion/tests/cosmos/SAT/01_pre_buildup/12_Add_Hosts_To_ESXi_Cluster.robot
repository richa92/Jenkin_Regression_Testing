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
    [Tags]    SP-ON  C7000   T-BIRD
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${esxi_os_servers}

Add ESXi Hosts To Cluster
    [Tags]    HOSTS    C7000   T-BIRD
    [Documentation]     Add hosts to cluster
    Add Hosts To Cluster  ${esxi_os_servers}  ${vi_server_details}

Exit Maintenance Mode For ESXi Hosts
    [Tags]    EXIT    C7000   T-BIRD
    [Documentation]     Exit Maintenance Mode For ESXi Hosts
    Exit Maintenance Mode For Hosts   ${esxi_os_servers}