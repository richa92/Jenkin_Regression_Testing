*** Settings ***
Documentation
...     This Test Suite adds Storage System, Edit storage pools to be managed, Storage Volume Templates, Storage Volumes and existing storage volumes
...     These Setup Tests are prerequisite for other EPIC MAT Test Suites.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ./resource_tbird.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
#Variables                       ./data_variables_tbird.py

*** Test Cases ***

Add Storage Systems and Pools
    [Tags]    SETUP        S-SYS
    [Documentation]        Add Storage Systems and Storage Pools to OneView
    ${responses}=  Connect and Add Storage Systems  ${storage_systems_with_pools}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_storage_systems_with_pools}

Edit the Storage Pools to Managed
    [Tags]    SETUP     S-POOL
    [Documentation]     Edit Storage Pool to change it from Discovered to Managed Status
    ${responses} =  Edit Storage Pools Async    ${storage_pools_toedit}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Storage Pool is Managed      ${storage_pools_toedit}

Add Storage Volumes
    [Tags]    SETUP        SV
    [Documentation]        Add Storage VOLUMES to OneView
    Run Keyword If  ${storage_volumes} is not ${null}     ${responses}=  Add Storage Volumes Async  ${storage_volumes}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Run Keyword If  ${expected_storage_volumes} is not ${null}     Verify Resources for List  ${expected_storage_volumes}

Add Already Existing Storage Volumes From Storage Systems
    [Tags]    SETUP     SV-E
    [Documentation]     Add Already Existing Storage Volumes to OneView
    ${responses}=  Add Existing Storage Volumes Async  ${storage_volumes_add}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_existing_storage_volumes}