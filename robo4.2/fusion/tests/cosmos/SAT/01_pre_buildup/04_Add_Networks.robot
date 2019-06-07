*** Settings ***
Documentation
...     This Test Suite uses AD Network Group User credentials for Networkst Tests.
...     Uses Administartor credentials to add SAS LIG
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${ad_network_credentials}
#Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
#...                             AND  Regression Test Teardown
Suite Teardown                  Regression Test Teardown

*** Test Cases ***
Add iSCSI Networks
    [Tags]  SETUP  ADD-ISCSI-NW  T-BIRD  C7000
    [Documentation]     Add ISCSI Ethernet Networks to OneView
    Run Keyword If  ${ethernet_networks} is not ${null}     Add Ethernet Networks from variable async  ${ethernet_networks}  ${VERIFY}  ${expected_ethernet_networks}

Add Ethernet Networks Bulk
    [Tags]  SETUP  ADD-ENW-BULK  T-BIRD  C7000
    [Documentation]     Add Ethernet Networks to OneView in Bulk
    Run Keyword If  ${ethernet_networks_bulk} is not ${null}    Create Bulk Ethernet Networks   ${ethernet_networks_bulk}     timeout=1000  interval=10
    Verify Bulk Ethernet Networks    ${expected_ethernet_networks_bulk}  eth

Add Untagged And Tunnel Ethernet Networks
    [Tags]  SETUP  ADD-ENW-TAGGED-TUNNEL  T-BIRD  C7000
    [Documentation]     Add Untagged and Tagged Ethernet Networks to OneView
    Run Keyword If  ${untagged_tunnel_eth_networks} is not ${null}     Add Ethernet Networks from variable async  ${untagged_tunnel_eth_networks}  ${VERIFY}  ${expected_untagged_tunnel_eth_networks}

Add FC networks
    [Tags]    SETUP      FC-NW  T-BIRD  C7000
    [Documentation]     Add FC Networks to OneView
    Run Keyword If  ${fc_networks} is not ${null}    Add FC Networks from variable async    ${fc_networks}  ${VERIFY}    expected_networks=${expected_fc_networks}

Add FCoE networks
    [Tags]    SETUP      FCoE-NW  T-BIRD  C7000
    [Documentation]        Add FCoE Networks to OneView
    Run Keyword If    ${fcoe_networks} is not ${null}      Add FCoE Networks from variable async  ${fcoe_networks}  ${VERIFY}  ${expected_fcoe_networks}
    Verify Regression Resources  ${expected_fcoe_networks}

Add Network Sets
    [Tags]    SETUP        NW-SETS  T-BIRD  C7000
    [Documentation]        Add Network Sets to OneView
    Run Keyword If    ${network_sets} is not ${null}      Add Networks Sets from variable async  ${network_sets}  ${VERIFY}  expected_network_sets=${expected_network_sets}

Add LIG
    [Tags]      SETUP       LIG  T-BIRD  C7000
    [Documentation]     Add LIG to OneView
    Run Keyword If    ${ligs} is not ${null}   Add LIG async   ${ligs}
    Verify Bulk LIG    ${expected_lig}

Add SAS LIG
    [Tags]   SETUP        SAS  T-BIRD
    [Documentation]       Add SAS LIG to OneView
    Regression Test Teardown
    Regression Test Setup    ${admin_credentials}
    Run Keyword If  ${sas_lig} is not ${null}    Add SAS LIG from variable async    ${sas_lig}    ${VERIFY}    expected_sas_lig=${expected_sas_lig}