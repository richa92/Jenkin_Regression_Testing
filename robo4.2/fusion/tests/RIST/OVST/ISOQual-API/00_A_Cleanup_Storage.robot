*** Settings ***
Documentation    Cleanup Storage System
Resource    resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure

*** Test Cases ***
Cleanup Storage System
   [Documentation]   Cleanup Storage3par Data
   [Tags]   CLEANUP-HW
   Storage3par Open Connection    ${storage_credentials['host']}    ${storage_credentials['username']}   ${storage_credentials['password']}
   Cleanup Storage3par Data
   Storage3par Close Connection

*** Keywords ***
Cleanup Storage3par Data
   [Documentation]   Cleanup Storage3par Data
   Cleanup All Vluns
   :FOR    ${vol}   IN  @{cleanup_volumes}
   \    ${data}=  Storage3par Delete Volume   ${vol['name']}
   \    Run Keyword and Expect Error   *   Storage3par Volume Should Exist   ${vol['name']}
   :FOR    ${host}   IN  @{cleanup_hosts}
   \    ${data}=  Storage3par Delete Host   ${host['name']}
   \    Run Keyword and Expect Error   *   Storage3par Host Should Exist   ${host['name']}
   ${listvlun}=   Storage3par Get Vluns
   ${vluncount}=  Get Length    ${listvlun}
   Log   List of Vluns Associated Volumes still present in the storage system: Vlun count=${vluncount}\n@{listvlun}   console=True
   ${listvolumes}=   Storage3par Get Volumes
   ${volcount}=   Get Length   ${listvolumes}
   Log   List of Volumes present in the storage system: Volumes count=${volcount}\n@{listvolumes}   console=True
   ${listhosts}=   Storage3par Get Hosts
   ${hostcount}=   Get Length   ${listhosts}
   Log   List of Hosts still present in the storage system: Hosts count=${hostcount}\n@{listhosts}    console=True


Storage3par Vlun Exists
    [Documentation]   Check if Storage3par Vlun Exists
    [Arguments]    ${vlun}
    ${lunid}=   Get From Dictionary   ${vlun}    lun
    ${host}=   Get From Dictionary   ${vlun}    hostname
    ${vol}=    Get From Dictionary   ${vlun}    volumeName
    Run Keyword and Expect Error   *   Storage3par Vlun Should Exist   ${host}   ${vol}   ${lunid}

Cleanup All Vluns
    [Documentation]   Cleanup all vlun data
    ${vluns}=   Storage3par Get Vluns
    :FOR    ${vlun}   IN  @{vluns}
    \     ${status}=    List of Volume Dict Contain Value    ${vlun['volumeName']}
    \     Run Keyword If    '${status}'=='True'   Remove Vlun    ${vlun}
    \     Run Keyword If    '${status}'=='True'   Storage3par Vlun Exists   ${vlun}

List of Volume Dict Contain Value
   [Documentation]   List of Volume Dict Contain Value
   [Arguments]   ${volume}
   :FOR    ${vol}  IN  @{cleanup_volumes}
   \    ${status}=   Run Keyword And Return Status    Dictionary Should Contain Value    ${vol}     ${volume}
   \    Return from keyword if  '${status}' == 'True'    ${status}

Remove Vlun
     [Documentation]   Remove vlun
     [Arguments]   ${vlun}
     ${lunid}=   Get From Dictionary   ${vlun}    lun
     ${host}=   Get From Dictionary   ${vlun}    hostname
     ${vol}=    Get From Dictionary   ${vlun}    volumeName
     ${status}   ${portdict}=   Run Keyword and Ignore Error  Get From Dictionary   ${vlun}    portPos
     ${data}=     Run keyword if    '${status}'=='PASS'   Storage3par Delete Vlun   ${vol}   ${lunid}   ${host}   ${portdict}
                  ...   ELSE      Storage3par Delete Vlun   ${vol}   ${lunid}   ${host}
