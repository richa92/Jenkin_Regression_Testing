*** Settings ***
Resource          ../resource.txt
Suite Setup       Fusion Api Login Appliance  ${appliance_ip}  ${credentials}
Suite Teardown    Fusion Api Logout Appliance
Force Tags        TBIRD  C7000

*** Test Cases ***
Add Storage Systems and Pools
    [Tags]    SETUP  S-SYS  TBIRD  C7000
    [Documentation]  Add Storage Systems and Storage Pools to OneView
    ${responses}=    Connect and Add Storage Systems  ${storage_systems_with_pools}
    Run Keyword If   ${responses} is not ${null}  Wait For Task2  ${responses}
    Verify Resources for List  ${expected_storage_systems_with_pools}
    :FOR  ${ss}  IN  @{storage_systems_with_pools}
    \   Verify Storage Pool is Managed  ${ss['deviceSpecificAttributes']['managedPools']}

Edit the Storage Pools to Managed
    [Tags]    SETUP  S-POOL  TBIRD  C7000
    [Documentation]  Edit Storage Pool to change it from Discovered to Managed Status
    ${responses} =   Edit Storage Pools Async  ${storage_pools_toedit}
    Run Keyword If   ${responses} is not ${null}  Wait For Task2  ${responses}
    Verify Storage Pool is Managed  ${storage_pools_toedit}

Add Storage Volume Templates
    [Tags]    SETUP  SVT  TBIRD  C7000
    [Documentation]  Add Storage VOLUME TEMPLATES to OneView
    ${responses} =   Add Storage Volume Templates Async  ${storage_volume_templates}
    Verify Resources for List  ${expected_storage_volume_templates}

Add Storage Volumes
    [Tags]    SETUP  SV  TBIRD  C7000
    [Documentation]  Add Storage VOLUMES to OneView
    ${responses}=    Add Storage Volumes Async  ${storage_volumes}
    Run Keyword If   ${responses} is not ${null}  Wait For Task2  ${responses}
    Verify Resources for List  ${expected_storage_volumes}
