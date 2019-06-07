*** Settings ***
Documentation
...     This Test Suite uses AD Storage Group User credentials for Storage Tests.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${ad_storage_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Add Storage Systems and Pools
    [Tags]    SETUP  S-SYS  T-BIRD  C7000
    [Documentation]        Add Storage Systems and Storage Pools to OneView
    ${responses}=  Connect and Add Storage Systems  ${storagesystems}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_storagesystem}
    :FOR    ${ss}   IN      @{storagesystems}
    \   Verify Storage Pool is Managed      ${ss['deviceSpecificAttributes']['managedPools']}

Edit the Storage Pools to Managed
    [Tags]    SETUP  S-POOL  T-BIRD  C7000
    [Documentation]     Edit Storage Pool to change it from Discovered to Managed Status
    ${responses} =  Edit Storage Pools Async    ${storage_pools}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Storage Pool is Managed      ${storage_pools}

Add Storage Volume Templates
    [Tags]    SETUP  SVT  T-BIRD  C7000
    [Documentation]        Add Storage VOLUME TEMPLATES to OneView
    ${responses} =  Add Storage Volume Templates Async  ${volume_templates}
    Verify Resources for List  ${expected_volume_templates}

Create New Storage Volumes
    [Tags]    SETUP  SV  T-BIRD  C7000
    [Documentation]        Add Storage VOLUMES to OneView
    ${responses}=  Add Storage Volumes Async  ${new_volumes_add}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_newvolumes}

Export Virtual Volumes To Host - 3PAR iSCSI SP
    [Tags]    SETUP  3PAR-VOL  T-BIRD
    [Documentation]        Export Virtual Volumes To Host - 3PAR iSCSI SP
    Storage3par Open Connection    ${storage_system[0]["hostname"]}    ${storage_system[0]["username"]}   ${storage_system[0]["password"]}
    : For  ${host}  IN  @{potash_iscsi_shared_volumes}
    \     ${status}  ${vlun}    Run Keyword and Ignore Error   storage3par_create_vlun   volume_name=${host["name"]}  hostname=${three_par_host_name[0]["name"]}  auto=True
    \     Run Keyword if   '${status}' != 'PASS'    FAIL   Failed to export virtual volume ${three_par_host_name[0]["name"]}
    \     ${status}  ${vlun}    Run Keyword and Ignore Error  storage3par_create_vlun   volume_name=${host["name"]}  hostname=${three_par_host_name[1]["name"]}  auto=True
    \     Run Keyword if   '${status}' != 'PASS'    FAIL   Failed to export virtual volume ${three_par_host_name[1]["name"]}
    Storage3par Close Connection

Export Virtual Volumes To Host - 3PAR iSCSI SP - C7000
    [Tags]    SETUP  3PAR-VOL  C7000
    [Documentation]        Export Virtual Volumes To Host - 3PAR iSCSI SP
    Storage3par Open Connection    ${storage_system[0]["hostname"]}    ${storage_system[0]["username"]}   ${storage_system[0]["password"]}
    : For  ${host}  IN  @{potash_iscsi_shared_volumes}
    \     ${status}  ${vlun}    Run Keyword and Ignore Error   storage3par_create_vlun   volume_name=${host["name"]}  hostname=${three_par_host_name[0]["name"]}  auto=True
    \     Run Keyword if   '${status}' != 'PASS'    FAIL   Failed to export virtual volume ${three_par_host_name[0]["name"]}
    Storage3par Close Connection