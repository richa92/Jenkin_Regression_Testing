*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials to Teardown the appliance.
...     First Test is to unassign Server Profile before removing all the resources that were added in other EPIC MAT Test Suites.
...     TAGS:                      CLEAN UP
Resource                        ./resource.txt
Suite Setup                     MAT Suite Setup     ${admin_credentials}
Suite Teardown                  MAT Suite Teardown
Variables                       ./data_variables.py

*** Test Cases ***

Remove Server Profiles Async
    [Tags]    TEARDOWN  REMOVEPROFILE
    [Documentation]     Remove Server Profiles for BL and DL servers
    ${profiles} =    Fusion Api Get Server Profiles
    :FOR    ${profile}  IN  @{profiles['members']}
    \   Run Keyword If  '${profile['serverHardwareUri']}' == 'None'     Continue For Loop
    \   ${server} =   Fusion Api Get Server Hardware  uri=${profile['serverHardwareUri']}
    \   Power off Server    ${server['name']}
    ${responses}=  Remove All Server Profiles Async
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=600    interval=5
    Run Keyword If   ${responses} is not ${Null}   Verify Server profile exists

Remove Server Profile Templates
    [Tags]    TEARDOWN  REMOVE-SPT
    [Documentation]        Remove Server Profiles Templates for servers
    Remove All SPT
    Verify Server Profile Templates exist

Remove Logical Enclosure from OV
    [Tags]    TEARDOWN  REMOVELE
    [Documentation]        Remove Logical Enclosures from OneView
    Remove All LEs Async

Delete Base Storage Resources
    [Tags]    TEARDOWN        DELETE-STORAGE-BASE
    [Documentation]        Remove Storage Volumes,Template, Pools and Storage Systems
    ${response_e} =  Remove Storage Volumes Async  ${delete_storage_volumes_from_OV_only}   ?suppressDeviceUpdates=true
    ${response_n} =  Remove Storage Volumes Async  ${storage_volumes_to_delete}  ?suppressDeviceUpdates=false
    Run Keyword If  ${response_e} is not ${null}  Wait For Task2  ${response_e}
    Run Keyword If  ${response_n} is not ${null}  Wait For Task2  ${response_n}
    ${response} =   Remove ALL Storage Volumes Async    ?suppressDeviceUpdates=true
    Run Keyword If  ${response} is not ${null}  Run Keyword for List    ${response}  Wait For Task2
    Remove All Storage Volume Templates Async
    Remove ALL Storage Systems Async