*** Settings ***
Documentation       Cleaup
Suite Setup         Run Keywords  Cleanup Dir  ${LOG_DIR}
...                               AND  Cleanup Dir  ${UPDATEBIN_DIR}
Resource            resource.txt

*** Test Cases ***
Synergy UPT Cleanup Remove Storage3par Data
    [Documentation]  Remove Storage3par Data
    Storage3par Open Connection   ${storeserv_systems_attributes[0]['hostname']}   ${storage_credentials['username']}  ${storage_credentials['password']}
    Cleanup Storage3par Data
    Storage3par Close Connection

*** Keywords ***
Cleanup Storage3par Data
    [Documentation]  Cleanup Storage3par Data
    Log  \nRemove vluns...  console=True
    Remove Vluns
    Log  \nRemove hosts...  console=True
    :FOR   ${host}  IN  @{cleanup_storeserv_hosts}
    \   ${rtn}=  storage3par_get_host  ${host}
    \   Run Keyword if  ${rtn}!=${None}  Log  Remove ${host}...  console=True
    \   Run Keyword if  ${rtn}!=${None}  Storage3par Delete Host  ${host}
    Log  \nRemove volumes...  console=True
    :FOR   ${vol}  IN  @{cleanup_storeserv_volumes}
    \   ${rtn}=   storage3par_get_volume  ${vol}
    \   Run Keyword if  ${rtn}!=${None}  Log  Remove ${vol}...  console=True
    \   Run Keyword if  ${rtn}!=${None}  Storage3par Delete Volume  ${vol}

Remove Vluns
    [Documentation]  Remove vluns
    ${vluns}=  Storage3par Get Vluns
    :FOR   ${vlun}  IN  @{vluns}
    \    ${status}=   Run Keyword And Return Status  List Should Contain Value  @{cleanup_host}  ${vlun['hostname']}
    \    Run Keyword If   '{status}'=='PASS'  Remove Vlun  ${vlun}
    \    ...   ELSE  log  Not Remove ${vlun['hostname']}

Remove Vlun
     [Documentation]  Remove vlun
     [Arguments]  ${vlun}
     Log  \nRemoving ${vlun}...  console=True
     ${lunid}=  Get From Dictionary  ${vlun}   lun
     ${host}=  Get From Dictionary  ${vlun}   hostname
     ${vol}=   Get From Dictionary  ${vlun}   volumeName
     ${status}  ${portdict}=  Run Keyword and Ignore Error  Get From Dictionary  ${vlun}   portPos
     ${data}=    Run keyword if   '${status}'=='PASS'  Storage3par Delete Vlun  ${vol}  ${lunid}  ${host}  ${portdict}
                 ...  ELSE    Storage3par Delete Vlun  ${vol}  ${lunid}  ${host}
