*** Settings ***
Documentation
...     This Test Suite uses admin credentials for modifying base Ethernet, Storage, Server profile resources.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                   ADD-ETH-NW, UPDATE-SP, NW-SETS, EDIT-SPT, SP-SPT, SP, SP-UNASSIGN
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${admin_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
ESXi Server Should Be Pinging And Volume Should Be Active
    [Tags]    ESXI-PING   T-BIRD
    [Documentation]     ESXi Server Should Be Pinging And Volume Should Be Active
    Power On Server Profile And Wait For POST State   ${esxi_os_servers}
    :FOR  ${esxi_os_server}  IN   @{esxi_os_servers}
    \    Run Keyword And Continue On Failure   ESXi Server Should Be Pinging And Volume Should Be Active   ${esxi_os_server}

Add Ethernet Networks
    [Tags]    ADD-ETH-NW  T-BIRD
    [Documentation]     Add Bulk Ethernet Networks to OneView
    Run Keyword If  ${ethernet_networks_system_validation} is not ${null}    Create Bulk Ethernet Networks   ${ethernet_networks_system_validation}     timeout=1000  interval=10
    Verify Bulk Ethernet Networks    ${expected_ethernet_networks_system_validation}  ${ethernet_name_prefix_system_validation}

Add Network Sets
    [Tags]    NW-SETS   T-BIRD
    [Documentation]     Add Network Sets to OneView
    Run Keyword If    ${network_sets_system_validation} is not ${null}      Add Networks Sets from variable async  ${network_sets_system_validation}  ${VERIFY}  expected_network_sets=${expected_network_sets_system_validation}

Edit Network Sets To Add Networks
    [Tags]    NW-SETS   T-BIRD
    [Documentation]     Edit Network Sets in OneView
    Run Keyword If    ${update_network_sets_system_validation} is not ${null}     Update Network Set  ${update_network_sets_system_validation}
    ${count}=  Existing Network Set Should Be Updated With Networks    ${edit_network_set_system_validation}    FALSE
    Run Keyword If    '${count}'!='0'   FAIL   Failed to update the network set

Add Shared Storage Volumes
    [Tags]    SV   T-BIRD
    [Documentation]     Add Shared Storage Volumes in OneView
    ${responses}=  Add Storage Volumes Async  ${new_volumes_add_system_validation}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    ...  timeout=1200  interval=5
    Verify Resources for List  ${expected_new_volumes_add_system_validation}

Update Storage Volumes
    [Tags]    UPDATE-SV   T-BIRD
    [Documentation]     Edit Storage Volumes in OneView
    ${responses}=  Edit Storage Volumes Async  ${edit_storage_volume_system_validations}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_edit_storage_volumes_system_validation}

Update Server Profile BIOS Settings
    [Tags]    UPDATE-SP   T-BIRD
    [Documentation]     Update server profile BIOS settings
    Power off Servers in Profiles   ${edit_server_profiles}
    ${responses}=   Edit Server Profiles from variable   ${edit_server_profiles}
    Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=1800    interval=5
    Verify Resources for List  ${expected_edit_server_profiles}

Edit Server Profile Template Ethernet Connections and Storage Attachments
    [Tags]    EDIT-SPT   T-BIRD
    [Documentation]     Edit Ethernet Connections and Storage Attachments in server profile Template
    ${resplist}=  Edit Server Profile Templates from variable    ${edit_server_profiles_template}
    Wait for Task2  ${resplist}     timeout=120    interval=10
    Verify Resources for List  ${expected_edit_server_profiles_template}

Update Server Profiles From Template
    [Tags]    SP-SPT   T-BIRD
    [Documentation]     Update Server Profiles from Templates
    Power off Servers in Profiles   ${update_server_profiles_from_spt}
    ${resp_list}=  Update Server Profiles from Template  ${update_server_profiles_from_spt}
    Run Keyword If  ${resp_list} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2  ${resp_list}
    ...  timeout=3000  interval=5
    :FOR  ${profile}  IN  @{update_server_profiles_from_spt}
    \   Wait Until Keyword Succeeds    300s    ${interval}   Wait for Server-Profile to be in OK state   ${profile['serverHardwareUri']}
    Power on Servers in Profiles   ${update_server_profiles_from_spt}

Create Server Profiles From Updated Template
    [Tags]    SP   T-BIRD
    [Documentation]     Add Server Profiles from Updated Templates
    Power off Servers in Profiles   ${server_profiles_from_spt_system_validation}
    ${resp_list}=  Add Server Profiles from variable  ${server_profiles_from_spt_system_validation}
    Run Keyword If  ${resp_list} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2  ${resp_list}
    ...  timeout=3000  interval=5
    :FOR  ${profile}  IN  @{server_profiles_from_spt_system_validation}
    \   Wait Until Keyword Succeeds    300s    ${interval}   Wait for Server-Profile to be in OK state   ${profile['serverHardwareUri']}
    Power on Servers in Profiles   ${server_profiles_from_spt_system_validation}

UnAssign Existing Server Profiles From Server Hardware
    [Tags]    SP-UNASSIGN   T-BIRD
    [Documentation]     UnAssign an existing Server Profile from a Server
    Power off Servers in Profiles   ${unassign_server_profile}
    ${responses}=   Edit Server Profiles from variable    ${unassign_server_profile}
    Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=3000    interval=5
    Verify Resources for List  ${unassign_server_profile}