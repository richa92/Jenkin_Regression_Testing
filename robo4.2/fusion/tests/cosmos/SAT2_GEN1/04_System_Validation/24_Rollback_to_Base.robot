*** Settings ***
Documentation    Tests for Rollback to Base resources
...     This Test Suite uses admin credentials for modifying base Ethernet, Storage, Server profile resources.
...     Test Data is defined in Python Data Variable file
...     TAGS:                   SP-REASSIGN, REM-SP, EDIT-SPT, EDIT-SP, SP-SPT, SP, NW-SETS, REM-NETSET, REM-VOL, REM-FW
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
ReAssign an existing Server Profile from Server hardware
    [Tags]    SP-REASSIGN  T-BIRD
    [Documentation]     ReAssign an existing Server Profile from a Server
    ${responses}=   Edit Server Profiles from variable    ${reassign_server_profile}
    Run Keyword If  ${responses} is not ${null}     Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=3000    interval=5
    Power on Servers in Profiles   ${reassign_server_profile}
    Verify Resource  ${reassign_server_profile}

Remove Server Profiles From Updated Template
    [Tags]    REM-SP  T-BIRD
    [Documentation]     Remove Server Profiles from Updated Templates
    Power off Servers in Profiles   ${server_profiles_from_spt_system_validation}
    ${responses} =  Remove Server Profiles from variable  ${server_profiles_from_spt_system_validation}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}   timeout=3000    interval=5
    Run Keyword If  ${responses} is not ${Null}  Server Profile Should Not Exist   ${server_profiles_from_spt_system_validation}

Edit Server Profile Template Ethernet Connections
    [Tags]    EDIT-SPT  T-BIRD
    [Documentation]     Update Ethernet connections in server profile templates
    ${resp_list}=  Edit Server Profile Templates from variable    ${edit_server_profiles_template_rollback}
    Run Keyword If  ${resp_list} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2  ${resp_list}
    ...  timeout=1200  interval=5
    Verify Resources for List  ${expected_edit_server_profile_templates_rollback}

Edit Server Profiles to delete storage attachments
    [Tags]    EDIT-SP  T-BIRD
    [Documentation]     Edit Server Profiles to delete storage attachments
    Power off Servers in Profiles   ${edit_server_profiles_storage_rollback}
    ${resp_list} =    Edit Server Profiles from variable  ${edit_server_profiles_storage_rollback}
    Run Keyword If  ${resp_list} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2  ${resp_list}
    ...  timeout=1200  interval=5

Update Server Profiles From Template
    [Tags]    SP-SPT  T-BIRD
    [Documentation]     Update Server Profiles from Templates
    Power off Servers in Profiles   ${update_server_profiles_from_spt}
    ${resp_list}=  Update Server Profiles from Template  ${update_server_profiles_from_spt}
    Run Keyword If  ${resp_list} is not ${null}   Run Keyword And Continue On Failure    Wait For Task2  ${resp_list}
    ...  timeout=1200  interval=5
    :FOR  ${profile}  IN  @{update_server_profiles_from_spt}
    \   Wait Until Keyword Succeeds    300s    ${interval}   Wait for Server-Profile to be in OK state   ${profile['serverHardwareUri']}
    Power on Servers in Profiles   ${update_server_profiles_from_spt}

Remove shared Storage Volumes Added in System Validation
    [Tags]    REM-VOL  T-BIRD
    [Documentation]     Remove Storage Volumes
    ${response} =  Remove Storage Volumes Async  ${delete_storage_shared_volumes_rollback}  ?suppressDeviceUpdates=false
    Run Keyword If  ${response} is not ${null}    Run Keyword And Continue On Failure  Wait For Task2  ${response}
    ...  timeout=1200  interval=5
    Storage Volumes Should Not Be Found     ${delete_storage_shared_volumes_rollback}

Edit Network Sets
    [Tags]    NW-SETS  T-BIRD
    [Documentation]     Remove Networks from Network Sets
    Run Keyword If    ${update_network_sets_rollback} is not ${null}     Update Network Set  ${update_network_sets_rollback}
    ${count}=  Existing Network Set Should Be Updated With Networks    ${edit_network_set_system_validation}    TRUE
    Run Keyword If    '${count}'!='0'   FAIL   Failed to update the network set

Remove Network Sets Added in System Validation
    [Tags]    REM-NETSET   T-BIRD
    [Documentation]     Remove NetworkSets from OneView appliance
    Remove Networks Sets From Variable    ${network_sets_system_validation}      ${VERIFY}

Remove Ethernet Networks Added in System Validation
    [Tags]    REM-ETH  T-BIRD
    [Documentation]     Remove Ethernet Networks from OneView appliance
    Remove Ethernet Networks Async  ${ethernet_networks_delete_rollback}   ${VERIFY}

Remove Firmware Bundle
    [Tags]    REM-FW  T-BIRD
    [Documentation]     Remove SPP Firmware Bundles from OneView appliance
    ${resp} =   Remove Firmware Bundle By Version   ${spp_version}
    Run Keyword If  ${resp} is not ${null}     Wait For Task2   ${resp}
    Firmware Bundle should not exist   ${spp_version}