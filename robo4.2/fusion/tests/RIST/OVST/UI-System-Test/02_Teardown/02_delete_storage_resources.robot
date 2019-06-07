*** Settings ***
Resource          ../resource.txt
Suite Setup       Fusion Api Login Appliance  ${appliance_ip}  ${credentials}
Suite Teardown    Fusion Api Logout Appliance
Force Tags        TBIRD  C7000

*** Test Cases ***
Delete Storage Resources
    [Tags]  TEARDOWN  R-STORAGE-BASE  C7000  TBIRD
    [Documentation]   Remove Storage Volumes,Template, Pools and Storage Systems
    Remove Storage Volumes Async   ${storage_volumes}  ?suppressDeviceUpdates=true
    Remove All Storage Volume Templates Async
    Remove ALL Storage Systems Async
