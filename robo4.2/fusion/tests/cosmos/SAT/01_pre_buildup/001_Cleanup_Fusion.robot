*** Settings ***
Documentation      Tests to Cleanup OA and ilo
Resource           ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***

Cleanup-OA
    [Documentation]   Cleanup OA VC Mode and Restart OA
    [TAGS]    Cleanup  CleanupOA    C7000
    # Power Off All Blades, Clear VC Mode and Restart oa
    :For    ${oa}    In     @{cleanup_oa}
    \    Log    Powering off all blades  console=True
    \    ${status} =   Power off all blades   ${oa}
    \    Log  ${status}
    \    Log   Clearing VC Mode  console=True
    \    ${clear_status} =    Clear Oa Vc Mode    ${oa}
    \    Log   ${clear_status}
    \    Log    Restarting ${oa['hostname']} OA  console=True
    \    ${restart_status}=   Restart Oa    ${oa}
    \    Log  ${restart_status}
    \    Ping OA IP    ${oa['hostname']}

Cleanup-ilo
    [Documentation]   Cleanup ilo by removing sso certificates
    [TAGS]    Cleanup  Cleanupilo    T-BIRD  C7000
    :FOR    ${ilo}    IN    @{cleanup_ilo}
    \  ${status}=  Run Keyword And Continue On Failure  remove all sso certificates blade   ${ilo}
    \  Run Keyword If   '${status}'=='True'   Log  SSO Certificate successfully deleted in ${ilo['ilo']}  console=yes
    \  Run Keyword If   '${status}'=='False'  Log  SSO Certificate is not present in ${ilo['ilo']}  console=yes
    \  ${ilo_snmp_settings}=    Run Cpqlocfg and Get SNMP Settings    ${ilo['ilo']}    ${ilo['username']}    ${ilo['password']}
    \  ${response}=    Run cpqlocfg and Clear SNMP Settings    ${ilo['ilo']}    ${ilo['username']}    ${ilo['password']}
    \  Check iLO SNMP User Presence    ${ilo_snmp_settings}    user=Administrator    expected=False

Cleanup Zones
    [Documentation]   Cleanup Zones
    [TAGS]    Cleanup    CleanZone    T-BIRD  C7000
    Clear Zones     ${cleanup_zone}



*** Keywords ***

Ping OA IP
    [Documentation]   Ping OA ip
    [arguments]     ${ip}
    ${output} =    Run    ping ${ip} -4 -n 1
    Should Contain    ${output}    time
    Log    OA is up and pinging    console=yes

Get Zone List
    [Documentation]   Get Zone List
    ${resp}=    Get resource by URI    /rest/fc-sans/zones
    ${zone_list}=    Create List
    Return from Keyword if    '${resp['status_code']}'!='200'    Fail    msg= Get query on Zones has failed
    ${zone_count}=    Run Keyword if    '${resp['status_code']}'=='200'    Set Variable    ${resp['count']}
    Return from keyword if    ${zone_count} == 0
    [Return]    ${resp['members']}

Get Uri from ZoneList
    [Documentation]   Get Zone Uri by SanName
    [Arguments]    ${zone}    ${sanName}
    ${zone_list}=    Create List
    Run Keyword if    '${zone['sanName']}'=='${sanName}'    run keywords
    ...    Run Keyword if    '${zone['uri']}' != 'None'    Append to List   ${zone_list}     ${zone['uri']}    AND
    ...    Log    List of Zone Uri:${zone['uri']}    console=True
    [Return]    ${zone_list}

Delete Zones from Zonelist
    [Documentation]    Delete zones from given list
    [Arguments]    ${actual_zone}    @{cleanup_zone}
    :FOR    ${temp}    IN    @{cleanup_zone}
    \    ${uri}=    Get Uri from ZoneList    ${actual_zone}    ${temp['sanName']}
    \    ${count}=    Get Length    ${uri}
    \    Run Keyword if    ${count} != 0    Run Keywords    Log    Deleting Zone:${uri[0]}    console=True    AND
    \    ...    Delete Zone by Uri    ${uri[0]}

Delete Zone by Uri
    [Documentation]    Delete Zone by Uri
    [Arguments]    ${zone_uri}
    ${response} =   Fusion Api Delete Resource   ${zone_uri}
    Log   ${response}
    Run Keyword If   '${response['status_code']}' != '202'   Log    Delete Zones has failed: ${response['status_code']}   WARN   console=True
    ...    ELSE    Log    Zones are deleted Successfull    console=True

Clear Zones
    [Documentation]   Clear Zones
    [Arguments]    ${cleanup_zone}
    ${zone_list}=    Create List
    ${zones}=    Get Zone List
    Log    ZONES:${zones}
    Return from Keyword if     ${zones} == ${None}
    :FOR    ${zone}    IN    @{zones}
    \   Delete Zones from Zonelist   ${zone}     @{cleanup_zone}