*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials to add Storage Systems, Storage Pools and Storage Volumes.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      STORAGE
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown

*** Test Cases ***

Add Storage System Async
    [Tags]    STORAGE  ADD-SS
    [Documentation]     Connect and Add Storage System to OneView
    ${responses}=  Connect and Add Storage Systems  ${storage_systems}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_storage_systems}

Edit the Storage Pools to Managed
    [Tags]    STORAGE  S-POOL
    [Documentation]     Edit Storage Pool to change it from Discovered to Managed Status
    Run Keyword If  '${PREV TEST STATUS}'=='FAIL'     Pause Execution    message=Add StorageSystem Async failed. Press OK to continue..
    ${responses} =  Edit Storage Pools Async    ${storage_pools}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Storage Pool is Managed      ${storage_pools}

Add Already Existing Storage Volumes From Storage Systems
    [Tags]    STORAGE  ADD-EX-SV
    [Documentation]     Add Already Existing Storage Volumes to OneView
    ${responses}=  Add Existing Storage Volumes Async  ${storage_volumes_add}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_existing_storage_volumes}
