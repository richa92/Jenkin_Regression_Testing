** Settings ***
Documentation
...     This Test Suite uses Administrator credentials to appliance failover and validate the primary/secondary roles
...     Post Appliance Failover validate the existing resources and ping os and check multipath
...     TAGS:                   APPLIANCE-FO
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Regression Test Teardown

*** Test cases ***
CIM Failover
    [Tags]    CIM-FO  T-BIRD
    [Documentation]  Appliance failover and validate the CIM roles
    Sleep    1m
    CIM Failover

After Failover Verify All The Resources - Tbird
    [Tags]    VERIFY-ALL-RES-TB  T-BIRD
    [Documentation]  Verify all the resources after post failover for Tbird
    Regression Test Setup     ${admin_credentials}
    Active Directory Should Exists    ${expected_ad}
    Active Directory Group and Role Should Exists   ${expected_adgrp}
    Verify Resources for List  ${expected_san_managers}
    Verify Bulk Ethernet Networks    ${expected_ethernet_networks_bulk}  eth
    Verify Resources for List  ${expected_fc_networks}
    Verify FCoE Networks   ${expected_fcoe_networks}
    Verify Network Sets    ${expected_network_sets}
    Verify Resources for List  ${expected_lig}
    Verify Resources for List  ${expected_storagesystem}
    Verify Storage Pool is Managed      ${storage_pools}
    Verify Resources for List  ${expected_volume_templates}
    Verify Resources for List  ${expected_volumes}
    sleep   400s
    All Enclosures Status Should Be OK or Warning
    All Interconnects Status Should Be OK or Warning
    All SAS Interconnects Status Should Be OK or Warning
    All Servers Status Should Be OK or Warning
    All Uplink Set Status Should Be OK or Warning
    All Fan Status Should Be OK or Warning
    All Power Supply Status Should Be OK or Warning
    Verify Resources for List  ${expected_spts_edit}
    Verify Resources for List  ${expected_pre_post_server_profiles}

Ping IP Post Appliance Failover, Windows Server Should Be Pinging, FC Disk Should Exist and Active - Tbird
    [Tags]      POST-APP-FO   T-BIRD
    [Documentation]     Ping IP Post Appliance Failover, Windows Server Should Be Pinging and FC Disk Should Exist and Active
    Regression Test Setup    ${ad_server_credentials}
    Power On Server Profile And Wait For POST State    ${win_os_servers}
    :FOR  ${win_os_server}  IN   @{win_os_servers}
    \  Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active   ${win_os_server}   04

Download Support Dump - Post CIM Failover
    [Tags]   DOWNLOAD-OVSD  T-BIRD
    [Documentation]    Get And Download Oneview Support Dump - Post CIM Failover
    Get Support Dump  ${support_dump}   ${TEST NAME}