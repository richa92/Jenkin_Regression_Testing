*** Settings ***
Documentation
...     This Test Suite uses AD Network Group User credentials for Networks Tests.
...     Uses Administartor credentials to add SAS LIG
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${ad_network_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Add Ethernet Networks
    [Tags]  SETUP  ADD-ETH-NW  T-BIRD
    [Documentation]     Add Bulk Ethernet Networks to OneView
    Run Keyword If  ${ethernet_networks_system_validation} is not ${null}    Create Bulk Ethernet Networks   ${ethernet_networks_system_validation}     timeout=1000  interval=10
    Verify Bulk Ethernet Networks    ${expected_ethernet_networks_system_validation}  ${ethernet_name_prefix_system_validation}

Add Network Sets
    [Tags]    SETUP        NW-SETS  T-BIRD
    [Documentation]        Add Network Sets to OneView
    Run Keyword If    ${network_sets_system_validation} is not ${null}      Add Networks Sets from variable async  ${network_sets_system_validation}  ${VERIFY}  expected_network_sets=${expected_network_sets_system_validation}

Edit Network Sets
    [Tags]    SETUP        NW-SETS  T-BIRD
    [Documentation]        Add Network Sets to OneView
    Run Keyword If    ${update_network_sets_system_validation} is not ${null}     Update Network Set  ${update_network_sets_system_validation}