*** Settings ***
Documentation                   Add Storage Resources to OneView
Resource    resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown

*** Test Cases ***

Add Storage Systems and Pools
    [Documentation]        Add Storage Systems and Storage Pools to OneView
    [Tags]    SETUP        S-SYS
    ${responses}=  Connect and Add Storage Systems  ${storage_systems_with_pools}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_storage_systems_with_pools}

Edit the Storage Pools to Managed
    [Documentation]     Edit Storage Pool to change it from Discovered to Managed Status
    [Tags]    SETUP     S-POOL
    ${responses} =  Edit Storage Pools Async    ${storage_pools_toedit}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Storage Pool is Managed      ${storage_pools_toedit}

Add Storage Volume Templates
    [Documentation]     Add Storage VOLUME TEMPLATES to OneView
    [Tags]    SETUP     SVT
    ${responses} =  Add Storage Volume Templates Async  ${storage_volume_templates}
    Verify Resources for List  ${expected_storage_volume_templates}

Add Storage Volumes
    [Documentation]        Add Storage VOLUMES to OneView
    [Tags]    SETUP        SV
    ${responses}=  Add Storage Volumes Async  ${storage_volumes}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_storage_volumes}

Add Already Existing Storage Volumes From Storage Systems
    [Documentation]     Add Already Existing Storage Volumes to OneView
    [Tags]    SETUP     SV-E
    ${responses}=  Add Existing Storage Volumes Async  ${add_existing_storage_volumes}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_existing_storage_volumes}