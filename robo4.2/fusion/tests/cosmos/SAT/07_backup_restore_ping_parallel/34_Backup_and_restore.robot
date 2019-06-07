*** Settings ***
Documentation
...     Backup and Restore of OV appliance
...     Ping IP Post Backup and Restore
Library                         dynamicdata.DynamicData   WITH NAME   DD
Resource                        ../resource.txt
Suite Teardown          Regression Test Teardown

*** Test cases ***
Backup Oneview
    [Tags]      BACKUP   T-BIRD   C7000
    [Documentation]     Backup OV appliance
    Regression Test Setup     ${ad_backup_credentials}
    Create Backup from OV

Download Oneview Backup
    [Tags]    DOWNLOAD-BCKUP   T-BIRD  C7000
    [Documentation]     Download Oneview Backup
    Regression Test Setup     ${ad_backup_credentials}
    ${uri}=     Get Backup URI

    ${OUTPUT_DIR} =    Set Variable If   '${OUTPUT_DIR}'==''    .\\    ${OUTPUT_DIR}

    ${local_file} =    Get Time
    ${local_file} =    Catenate    SEPARATOR=.    ${local_file}    bkp
    ${local_file} =    Replace String Using Regexp    ${local_file}    ( |:)    _
    ${local_file} =    Catenate    SEPARATOR=\\    ${OUTPUT_DIR}    ${local_file}
    Log to console and logfile    Download to: ${local_file}
    Set Suite Variable    ${BKP_FILE}     ${local_file}

    ${resp}      Download Backup    ${uri}    ${local_file}

Add And Remove Resources After Backup - C7000
    [Tags]     POST-ADD-ISCSI-NW  C7000
    [Documentation]     Add Ethernet Networks to OneView
    Regression Test Setup     ${admin_credentials}
    Run Keyword If  ${postbackup_ethernet_networks} is not ${null}     Add Ethernet Networks from variable async  ${postbackup_ethernet_networks}  ${VERIFY}  ${postbackup_expected_ethernet_networks}

    # Remove two networks we created in Suite Setup
    ${resp} =    Delete Resource    ETH:eth_1187
    Wait For Task2    ${resp}    timeout=500    interval=2
    ${resp} =    Delete Resource    ETH:eth_1188
    Wait For Task2    ${resp}    timeout=500    interval=2

Add And Remove Resources After Backup - Tbird
    [Tags]     POST-ADD-ISCSI-NW  T-BIRD
    [Documentation]     Add Ethernet Networks to OneView
    Regression Test Setup     ${admin_credentials}
    Run Keyword If  ${postbackup_ethernet_networks} is not ${null}     Add Ethernet Networks from variable async  ${postbackup_ethernet_networks}  ${VERIFY}  ${postbackup_expected_ethernet_networks}

    # Remove two networks we created in Suite Setup
    ${resp} =    Delete Resource    ETH:eth1_1187
    Wait For Task2    ${resp}    timeout=500    interval=2
    ${resp} =    Delete Resource    ETH:eth1_1188
    Wait For Task2    ${resp}    timeout=500    interval=2

Restore OneView Backup
    [Tags]    RESTORE  T-BIRD  C7000
    [Documentation]     Restore Oneview Backup
    Regression Test Setup     ${admin_credentials}
    ${resp}=    Restore Appliance    ${BKP_FILE}

Wait for Startup Complete
    [Tags]    START-UP  T-BIRD  C7000
    [Documentation]     Restore Oneview Backup
    Regression Test Setup     ${admin_credentials}
    Wait Until Keyword Succeeds    5m    30s    OneView Startup Complete    ${APPLIANCE_IP}

SPP Upload - C7000
    [Documentation]    Upload SPP bundle to OV
    [Tags]    ADDSPP-C7000  C7000
    Regression Test Setup     ${admin_credentials}
    :FOR    ${spp_local_path}   IN    @{buildup_spp_local_paths}
    \   Upload Firmware Bundle Async    ${spp_local_path}   ${TRUE}

SPP Upload - Synergy
    [Documentation]    Upload SPP bundle to OV
    [Tags]    ADDSPP-T-BIRD    T-BIRD
    ${build_path}    Create List
    ${get_spp_path}   DD.get_spp_path   ${sppname}   ${spp_local_dir}
    Append To List   ${build_path}   ${get_spp_path}
    Log   ${build_path}   console=True
    :FOR    ${spp_local_path}   IN    @{build_path}
    \   Upload Firmware Bundle Async    ${spp_local_path}   ${TRUE}

SPP Upload Gen9 And Gen10
   [Documentation]    Upload SPP bundle to OV
    [Tags]    ADDSPP    C7000
    Regression Test Setup     ${admin_credentials}
    :FOR    ${spp_local_path}   IN    @{backup_spp_local_paths}
    \   Upload Firmware Bundle Async    ${spp_local_path}   ${TRUE}

Resources Should Not Exists Added After Backup - C7000
    [Tags]    VERIFY-RES  C7000
    [Documentation]     Restore Oneview Backup

    Regression Test Setup     ${admin_credentials}
    # verify Post Backup Ethernet Networks are not there
    :For    ${net}   IN    @{postbackup_ethernet_networks}
    \    ${uri} =    Get Ethernet URI    ${net['name']}
    \    Should Match    ${uri}    /rest/network_uri_${net['name']}_not_found

    # verify resources that are deleted after backup
    ${eth1} =   Get Ethernet URI    eth_1187
    Should Not Match    ${uri}    /rest/network_uri_eth_1187_not_found

    ${eth2} =   Get Ethernet URI    eth_1188
    Should Not Match    ${uri}    /rest/network_uri_eth_1188_not_found

Resources Should Not Exists Added After Backup - Tbird
    [Tags]    VERIFY-RES  T-BIRD
    [Documentation]     Restore Oneview Backup

    Regression Test Setup     ${admin_credentials}
    # verify Post Backup Ethernet Networks are not there
    :For    ${net}   IN    @{postbackup_ethernet_networks}
    \    ${uri} =    Get Ethernet URI    ${net['name']}
    \    Should Match    ${uri}    /rest/network_uri_${net['name']}_not_found

    # verify resources that are deleted after backup
    ${eth1} =   Get Ethernet URI    eth1_1187
    Should Not Match    ${uri}    /rest/network_uri_eth1_1187_not_found

    ${eth2} =   Get Ethernet URI    eth1_1188
    Should Not Match    ${uri}    /rest/network_uri_eth1_1188_not_found

After Restore Verify All The Resources - C7000
    [Tags]    VERIFY-ALL-RES  C7000
    [Documentation]  Verify all the resources after post restore
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
    Verify Storage Pool is Managed      ${storage_pools_manage}
    Verify Storage Pool is Discover      ${storage_pools_discover}
    Verify Resources for List  ${expected_volume_templates}
    Verify Resources for List  ${expected_volumes}
    Verify Resources for List  ${expected_newvolumes}
    sleep   400s
    Verify Enclosures from list  ${expected_enclosures_with_spp}  state=Configured
    Verify Resources for List  ${expected_spts_edit}
    Verify Resources for List  ${expected_server_profiles_from_spt_with_spp}
    Verify Resources for List  ${expected_server_profile_with_spp}
    Verify Enclosures from list  ${expected_enclosures_postupgrade_with_spp}  state=Configured
    Verify Resources for List  ${expected_server_profiles_postupgrade}

After Restore Verify All The Resources - Tbird
    [Tags]    VERIFY-ALL-RES-TB  T-BIRD
    [Documentation]  Verify all the resources after post restore for Tbird
    Regression Test Setup     ${admin_credentials}
    Active Directory Should Exists    ${expected_ad}
    Active Directory Group and Role Should Exists   ${expected_adgrp}
    Verify Resources for List  ${expected_san_managers}
    Verify Bulk Ethernet Networks    ${expected_ethernet_networks_bulk}  eth
    Verify Resources for List  ${expected_fc_networks}
    Verify FCoE Networks    ${expected_fcoe_networks}
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

Ping IP Post Backup and Restore, Windows Server Should Be Pinging, FC Disk Should Exist and Active
    [Tags]      POST-BKUP-RSTR   C7000
    [Documentation]     Ping IP Post Backup and Restore, Windows Server Should Be Pinging, FC Disk Should Exist and Active
    Regression Test Setup    ${ad_server_credentials}
    Power On Server Profile And Wait For POST State    ${win_os_servers}
    :FOR  ${win_os_server}  IN   @{win_os_servers}
    \  Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active   ${win_os_server}   02

Ping IP Post Backup and Restore, Windows Server Should Be Pinging, FC Disk Should Exist and Active - Tbird
    [Tags]      POST-BKUP-RSTR-TB   T-BIRD
    [Documentation]     Ping IP Post Backup and Restore, Windows Server Should Be Pinging and FC Disk Should Exist and Active
    Regression Test Setup    ${ad_server_credentials}
    Power On Server Profile And Wait For POST State    ${win_os_servers}
    :FOR  ${win_os_server}  IN   @{win_os_servers}
    \  Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active   ${win_os_server}   04

Download Support Dump - Post Backup And Restore
    [Tags]   DOWNLOAD-OVSD  T-BIRD   C7000
    [Documentation]    Get And Download Oneview Support Dump - Post Backup And Restore
    Get Support Dump  ${support_dump}   ${TEST NAME}