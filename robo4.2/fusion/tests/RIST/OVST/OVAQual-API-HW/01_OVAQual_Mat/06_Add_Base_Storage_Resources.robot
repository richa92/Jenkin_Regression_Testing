*** Settings ***
Documentation    Add Base Storage Resources to OneView
Resource                         ../resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure
*** Test Cases ***

Add Storage Systems and Pools
    [Tags]    SETUP        S-SYS
    [Documentation]        Add Storage Systems and Storage Pools to OneView
    ${responses}=  Connect and Add Storage Systems  ${storage_systems_with_pools}
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_storage_systems_with_pools}
    :FOR    ${ss}   IN      @{storage_systems_with_pools}
    \   Verify Storage Pool is Managed      ${ss['deviceSpecificAttributes']['managedPools']}

Edit the Storage Pools to Managed
    [Tags]    SETUP     S-POOL
    [Documentation]     Edit Storage Pool to change it from Discovered to Managed Status
    ${responses} =  Edit Storage Pools Async    ${storage_pools_toedit}
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure     Wait For Task2   ${responses}
    Verify Storage Pool is Managed      ${storage_pools_toedit}

Add Storage Volume Templates
    [Tags]    SETUP        SVT
    [Documentation]        Add Storage VOLUME TEMPLATES to OneView
    ${responses} =  Add Storage Volume Templates Async  ${storage_volume_templates}
    Verify Resources for List  ${expected_storage_volume_templates}

Add Storage Volumes
    [Tags]    SETUP        SV
    [Documentation]        Add Storage VOLUMES to OneView
    ${responses}=  Add Storage Volumes Async  ${storage_volumes}
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_storage_volumes}

DCS ONLY- Delete Storage Volume from OV for DCS
    [Tags]  DCS
    [Documentation]     This Test Cases is only for DCS Execution, the test delete some Volumes from OV only so they can be imported in next test case
    ${response}=    Remove Storage Volumes Async   ${delete_storage_volumes_from_DCS}  ?suppressDeviceUpdates=true
    Run Keyword If  ${response} is not ${null}    Run Keyword And Continue On Failure  Wait For Task2  ${response}

Add Already Existing Storage Volumes From Storage Systems
    [Tags]    SETUP        SV-E
    [Documentation]        Add Already Existing Storage Volumes to OneView
    ${responses}=  Add Existing Storage Volumes Async  ${add_existing_storage_volumes}
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_existing_storage_volumes}