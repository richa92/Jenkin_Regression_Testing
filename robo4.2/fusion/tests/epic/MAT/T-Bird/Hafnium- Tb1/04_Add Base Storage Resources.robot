*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials to add Storage Systems, Storage Pools and Storage Volumes.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      STORAGE
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
Variables                       ./data_variables.py

*** Test Cases ***

Add Storage System Async
    [Tags]    ADDSTORAGESYS
    [Documentation]     Connect and Add Storage System to OneView
    ${responses}=  Connect and Add Storage Systems  ${storage_systems}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_storage_systems}

Edit the Storage Pools to Managed
    [Tags]    S-POOL
    [Documentation]     Edit Storage Pool to change it from Discovered to Managed Status
    Run Keyword If  '${PREV TEST STATUS}'=='FAIL'     Pause Execution    message=Add StorageSystem Async failed. Press OK to continue..
    ${responses} =  Edit Storage Pools Async    ${storage_pools}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Storage Pool is Managed      ${storage_pools}

Add Storage Volume Templates
    [Tags]    SETUP     SVT
    [Documentation]     Add Storage VOLUME TEMPLATES to OneView
    ${responses} =  Add Storage Volume Templates Async  ${storage_volume_templates}
    Verify Resources for List  ${expected_storage_volume_templates}

Add Storage Volumes
    [Tags]    SETUP        SV
    [Documentation]        Add Storage VOLUMES to OneView
    ${responses}=  Add Storage Volumes Async  ${storage_volumes}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_storage_volumes}

Add Already Existing Storage Volumes From Storage Systems
    [Tags]    ADDEXSTORAGEVOL
    [Documentation]     Add Already Existing Storage Volumes to OneView
    ${responses}=  Add Existing Storage Volumes Async  ${storage_volumes_add}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_existing_storage_volumes}

