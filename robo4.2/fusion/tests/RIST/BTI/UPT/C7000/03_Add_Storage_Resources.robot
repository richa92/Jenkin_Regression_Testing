*** Settings ***
Documentation                   Adding Storage Systems, Storage Pools, Storage Volume Templates and Storage Volumes to OneView
Resource                        resource.txt
Suite Setup                     Suite Setup
Suite Teardown                  Suite Teardown

*** Test Cases ***
C7000 UPT Add Storage Resources Add Storage Systems and Pools
    [Documentation]  Add Storage Systems and Pools
    ${resplist} =  Add Storage Systems Async  ${storage_systems}
    wait for task2  ${resplist}  timeout=300  interval=10
    ${resplist} =  Edit Storage Systems Async  ${storage_systems}
    wait for task2  ${resplist}  timeout=300  interval=10

C7000 UPT Add Storage Resources Edit the Storage Pools to Managed
    [Documentation]  Edit the Storage Pools to Managed
    ${resplist} =  Edit Storage Pools Async  ${storage_pools}
    wait for task2  ${resplist}   timeout=300  interval=10

C7000 UPT Add Storage Resources Add Storage Volume Templates
    [Documentation]    Add SVT
    ${resplist} =  Add Storage Volume Templates Async  ${storage_volume_templates}

C7000 UPT Add Storage Resources Add Storage Volumes
    [Documentation]    Add SV
    ${responses}=  Add Storage Volumes Async  ${storage_volumes}
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure    Wait For Task2   ${responses}

C7000 UPT Add Storage Resources Verify Storage Resources
    [Documentation]  Verify storage resources
    Verify Storage Resources