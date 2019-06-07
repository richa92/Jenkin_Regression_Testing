*** Settings ***
Documentation    Delete Base Storage Resources
Resource      ../resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure

*** Test Cases ***

Delete Base Storage Resources
    [Tags]    TEARDOWN     DELETE-ST-BASE
    [Documentation]        Remove Storage Volumes,Template, Pools and Storage Systems
    ${response_e} =  Remove Storage Volumes Async  ${delete_storage_volumes_from_OV_only}   ?suppressDeviceUpdates=true
    ${response_n} =  Remove Storage Volumes Async  ${storage_volumes_to_delete}  ?suppressDeviceUpdates=false
    Run Keyword If  ${response_e} is not ${null}    Run Keyword And Continue On Failure  Wait For Task2  ${response_e}
    Run Keyword If  ${response_n} is not ${null}    Run Keyword And Continue On Failure  Wait For Task2  ${response_n}
    Storage Volumes Should Not Be Found     ${delete_storage_volumes_from_OV_only}
    Storage Volumes Should Not Be Found     ${storage_volumes_to_delete}
    Remove All Storage Volume Templates Async
    Remove ALL Storage Systems Async
