*** Settings ***
Documentation
...     This Test Suite uses AD Storage Group User credentials for Storage Tests.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      EXECUTION    STORAGE
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${ad_storage_credentials}
#Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
#...                             AND  Regression Test Teardown
Suite Teardown                  Regression Test Teardown

*** Test Cases ***

Add Storage Systems and Pools
    [Tags]    EXECUTION  S-SYS  T-BIRD  C7000
    [Documentation]        Add Storage Systems and Storage Pools to OneView
    ${responses}=  Connect and Add Storage Systems  ${exec_storage_systems}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${exec_expected_storage_systems}

Edit the Storage Pools to Managed
    [Tags]    EXECUTION  S-POOL   T-BIRD  C7000
    [Documentation]     Edit Storage Pool to change it from Discovered to Managed Status
    ${responses} =  Edit Storage Pools Async    ${storage_pools_toedit_manage}
    Run Keyword If  ${responses} is not ${null}   Run Keyword And Continue On Failure     Wait For Task2   ${responses}
    Verify Storage Pool is Managed      ${storage_pools_toedit_manage}

Add Storage Volumes
    [Tags]    EXECUTION  SV  T-BIRD  C7000
    [Documentation]        Add Storage VOLUMES to OneView
    ${responses}=  Add Storage Volumes Async  ${exec_volumes_add}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${exec_expected_volumes}

Add Storage Volume Templates
    [Tags]    SETUP  SVT  T-BIRD  C7000
    [Documentation]        Add Storage VOLUME TEMPLATES to OneView
    ${responses} =  Add Storage Volume Templates Async  ${volume_templates_post_upgrade}
    Verify Resources for List  ${expected_volume_templates_post_upgrade}

Update Storage Volume Templates
    [Tags]    SETUP  UPDATE-SVT  T-BIRD  C7000
    [Documentation]        Edit Storage VOLUMES to OneView
    ${responses}=  Edit Storage Volume Templates  ${edit_storage_volume_templates}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_edit_storage_volume_templates}

Edit the Storage Pools to Discover
    [Tags]    EXECUTION  S-POOL-DIS   T-BIRD  C7000
    [Documentation]     Edit Storage Pool to change it from Discovered to Managed Status
    ${responses} =  Edit Storage Pools Async    ${storage_pools_toedit_discover}
    Run Keyword If  ${responses} is not ${null}   Run Keyword And Continue On Failure     Wait For Task2   ${responses}
    Verify Storage Pool is Discover      ${storage_pools_toedit_discover}

Update Storage Volumes
    [Tags]    EXECUTION  UPDATE-SV  T-BIRD  C7000
    [Documentation]        Edit Storage VOLUMES to OneView
    ${responses}=  Edit Storage Volumes Async  ${exec_edit_storage_volumes}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${exec_expected_edit_storage_volumes}

Create Snapshot of Storage Volume
    [Tags]    EXECUTION  SV-SNAPSHOT  T-BIRD  C7000
    [Documentation]        Create Storage VOLUME snapshot
    ${responses} =  Create Storage Volume Snapshot      ${exec_storage_volumes_snapshot}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Storage Volume Snapshot Should Exist   ${exec_expected_storage_vol_snapshot_dto}

Delete Storage Volume Snapshot
    [Tags]    EXECUTION  DELETE-SV-SNAPSHOT  T-BIRD  C7000
    [Documentation]        Delete Storage VOLUME snapshot
    ${responses} =  Remove Storage Volume Snapshots Async    ${exec_delete_storage_volumes_snapshots}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}

Delete Storage Volumes
    [Tags]    EXECUTION  DELETE-SV  T-BIRD  C7000
    [Documentation]        Delete Storage VOLUMES
    ${responses} =  Remove Storage Volumes Async  ${exec_delete_storage_volumes}  ?suppressDeviceUpdates=false
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}

Delete Storage Systems
    [Tags]    EXECUSION  REMOVE-SS   T-BIRD  C7000
    [Documentation]     Remove storage systems
    :FOR    ${ss}  in  @{exec_storage_system_to_remove}
    \    Remove Storage System By Name   ${ss}