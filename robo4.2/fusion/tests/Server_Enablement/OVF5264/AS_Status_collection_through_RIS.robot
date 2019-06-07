*** Settings ***
Documentation    AS_Status_collection_through_RIS
Library            FusionLibrary
Library            RoboGalaxyLibrary
Library            OperatingSystem
Library            BuiltIn
Library            Collections
Library            XML
Library            String
Library            json
Library            Process
Suite Setup        Run keywords    Set log level    TRACE    AND
                    ...    Fusion Api Login Appliance    ${Appliance}     ${admin_credentials}
Suite Teardown    Fusion Api Logout Appliance
Resource        ../../../Resources/api/fusion_api_resource.txt
Variables        AS_Status_collection_through_RIS_datafile.py


*** Variables ***
${Appliance}        16.83.10.20

*** Test cases ***
AS_Status_collection_state0
    ${time}    Get time
    ${r}    Fusion Api Create Events    ${State0}
    ${dict1}    Get correct dictionary as per specified value    ${State0['eventDetails']}    AggregatedHealthStatus
    ${css}    Get Regexp Matches    ${dict1['eventItemValue']}    Critical
    ${lcss}    Get Length    ${css}
    ${stcss}    Run keyword if    ${lcss}==1    Get critical resource name    ${dict1}
    ${wss}    Get Regexp Matches    ${dict1['eventItemValue']}    Warning
    ${lwss}    Get length    ${wss}
    ${stwss}    Run keyword if    ${lwss}==1    Get warning resource name    ${dict1}
    ${dict2}    Get correct dictionary as per specified value    ${State0['eventDetails']}    resourceUri
    Check for alert message and resource health status    ${dict1}    ${dict2}    ${time}    ${lcss}    ${lwss}    ${stcss}    ${stwss}

AS_Status_collection_state1
    ${time}    Get time
    ${r}    Fusion Api Create Events    ${State1}
    ${dict1}    Get correct dictionary as per specified value    ${State1['eventDetails']}    AggregatedHealthStatus
    ${css}    Get Regexp Matches    ${dict1['eventItemValue']}    Critical
    ${lcss}    Get Length    ${css}
    ${stcss}    Run keyword if    ${lcss}==1    Get critical resource name    ${dict1}
    ${wss}    Get Regexp Matches    ${dict1['eventItemValue']}    Warning
    ${lwss}    Get length    ${wss}
    ${stwss}    Run keyword if    ${lwss}==1    Get warning resource name    ${dict1}
    ${dict2}    Get correct dictionary as per specified value    ${State1['eventDetails']}    resourceUri
    Check for alert message and resource health status    ${dict1}    ${dict2}    ${time}    ${lcss}    ${lwss}    ${stcss}    ${stwss}

AS_Status_collection_State2
    ${time}    Get time
    ${r}    Fusion Api Create Events    ${State2}
    ${dict1}    Get correct dictionary as per specified value    ${State2['eventDetails']}    AggregatedHealthStatus
    ${css}    Get Regexp Matches    ${dict1['eventItemValue']}    Critical
    ${lcss}    Get Length    ${css}
    ${stcss}    Run keyword if    ${lcss}==1    Get critical resource name    ${dict1}
    ${wss}    Get Regexp Matches    ${dict1['eventItemValue']}    Warning
    ${lwss}    Get length    ${wss}
    ${stwss}    Run keyword if    ${lwss}==1    Get warning resource name    ${dict1}
    ${dict2}    Get correct dictionary as per specified value    ${State2['eventDetails']}    resourceUri
    Check for alert message and resource health status    ${dict1}    ${dict2}    ${time}    ${lcss}    ${lwss}    ${stcss}    ${stwss}

AS_Status_collection_state3
    ${time}    Get time
    ${r}    Fusion Api Create Events    ${State3}
    ${dict1}    Get correct dictionary as per specified value    ${State3['eventDetails']}    AggregatedHealthStatus
    ${css}    Get Regexp Matches    ${dict1['eventItemValue']}    Critical
    ${lcss}    Get Length    ${css}
    ${stcss}    Run keyword if    ${lcss}==1    Get critical resource name    ${dict1}
    ${wss}    Get Regexp Matches    ${dict1['eventItemValue']}    Warning
    ${lwss}    Get length    ${wss}
    ${stwss}    Run keyword if    ${lwss}==1    Get warning resource name    ${dict1}
    ${dict2}    Get correct dictionary as per specified value    ${State3['eventDetails']}    resourceUri
    Check for alert message and resource health status    ${dict1}    ${dict2}    ${time}    ${lcss}    ${lwss}    ${stcss}    ${stwss}

AS_Status_collection_State4
    ${time}    Get time
    ${r}    Fusion Api Create Events    ${State4}
    ${dict1}    Get correct dictionary as per specified value    ${State4['eventDetails']}    AggregatedHealthStatus
    ${css}    Get Regexp Matches    ${dict1['eventItemValue']}    Critical
    ${lcss}    Get Length    ${css}
    ${stcss}    Run keyword if    ${lcss}==1    Get critical resource name    ${dict1}
    ${wss}    Get Regexp Matches    ${dict1['eventItemValue']}    Warning
    ${lwss}    Get length    ${wss}
    ${stwss}    Run keyword if    ${lwss}==1    Get warning resource name    ${dict1}
    ${dict2}    Get correct dictionary as per specified value    ${State4['eventDetails']}    resourceUri
    Check for alert message and resource health status    ${dict1}    ${dict2}    ${time}    ${lcss}    ${lwss}    ${stcss}    ${stwss}

AS_Status_collection_State5
    ${time}    Get time
    ${r}    Fusion Api Create Events    ${State5}
    ${dict1}    Get correct dictionary as per specified value    ${State5['eventDetails']}    AggregatedHealthStatus
    ${css}    Get Regexp Matches    ${dict1['eventItemValue']}    Critical
    ${lcss}    Get Length    ${css}
    ${stcss}    Run keyword if    ${lcss}==1    Get critical resource name    ${dict1}
    ${wss}    Get Regexp Matches    ${dict1['eventItemValue']}    Warning
    ${lwss}    Get length    ${wss}
    ${stwss}    Run keyword if    ${lwss}==1    Get warning resource name    ${dict1}
    ${dict2}    Get correct dictionary as per specified value    ${State5['eventDetails']}    resourceUri
    Check for alert message and resource health status    ${dict1}    ${dict2}    ${time}    ${lcss}    ${lwss}    ${stcss}    ${stwss}

AS_Status_collection_State6
    ${time}    Get time
    ${r}    Fusion Api Create Events    ${State6}
    ${dict1}    Get correct dictionary as per specified value    ${State6['eventDetails']}    AggregatedHealthStatus
    ${css}    Get Regexp Matches    ${dict1['eventItemValue']}    Critical
    ${lcss}    Get Length    ${css}
    ${stcss}    Run keyword if    ${lcss}==1    Get critical resource name    ${dict1}
    ${wss}    Get Regexp Matches    ${dict1['eventItemValue']}    Warning
    ${lwss}    Get length    ${wss}
    ${stwss}    Run keyword if    ${lwss}==1    Get warning resource name    ${dict1}
    ${dict2}    Get correct dictionary as per specified value    ${State6['eventDetails']}    resourceUri
    Check for alert message and resource health status    ${dict1}    ${dict2}    ${time}    ${lcss}    ${lwss}    ${stcss}    ${stwss}

AS_Status_collection_State7
    ${time}    Get time
    ${r}    Fusion Api Create Events    ${State7}
    ${dict1}    Get correct dictionary as per specified value    ${State7['eventDetails']}    AggregatedHealthStatus
    ${css}    Get Regexp Matches    ${dict1['eventItemValue']}    Critical
    ${lcss}    Get Length    ${css}
    ${stcss}    Run keyword if    ${lcss}==1    Get critical resource name    ${dict1}
    ${wss}    Get Regexp Matches    ${dict1['eventItemValue']}    Warning
    ${lwss}    Get length    ${wss}
    ${stwss}    Run keyword if    ${lwss}==1    Get warning resource name    ${dict1}
    ${dict2}    Get correct dictionary as per specified value    ${State7['eventDetails']}    resourceUri
    Check for alert message and resource health status    ${dict1}    ${dict2}    ${time}    ${lcss}    ${lwss}    ${stcss}    ${stwss}

AS_Status_collection_State8
    ${time}    Get time
    ${r}    Fusion Api Create Events    ${State8}
    ${dict1}    Get correct dictionary as per specified value    ${State8['eventDetails']}    AggregatedHealthStatus
    ${css}    Get Regexp Matches    ${dict1['eventItemValue']}    Critical
    ${lcss}    Get Length    ${css}
    ${stcss}    Run keyword if    ${lcss}==1    Get critical resource name    ${dict1}
    ${wss}    Get Regexp Matches    ${dict1['eventItemValue']}    Warning
    ${lwss}    Get length    ${wss}
    ${stwss}    Run keyword if    ${lwss}==1    Get warning resource name    ${dict1}
    ${dict2}    Get correct dictionary as per specified value    ${State8['eventDetails']}    resourceUri
    Check for alert message and resource health status    ${dict1}    ${dict2}    ${time}    ${lcss}    ${lwss}    ${stcss}    ${stwss}

AS_Status_collection_State9
    ${time}    Get time
    ${r}    Fusion Api Create Events    ${State9}
    ${dict1}    Get correct dictionary as per specified value    ${State9['eventDetails']}    AggregatedHealthStatus
    ${dict2}    Get correct dictionary as per specified value    ${State9['eventDetails']}    resourceUri
    Check for health status with all resouces OK    ${dict1}    ${dict2}    ${time}

*** Keywords ***
Get critical resource name
    [Documentation]    Get critical resource name
    [Arguments]    ${State}
    ${css}    Get Regexp Matches    ${State['eventItemValue']}    Critical
    ${lcss}    Get Length    ${css}
    ${stcss}    Run keyword if    ${lcss}==1    split string    ${State['eventItemValue']}    ${SPACE}
    ${critical_res}    Set variable    ${None}
    :FOR    ${item}    in    @{stcss}
    \    ${match}    ${value}    Run Keyword And Ignore Error    Should Contain    ${item}    Critical
    \    ${res}    Run keyword if    '${match}' == 'PASS'    Fetch from left    ${item}    =
    \    ${critical_res}    Set variable if    '${match}' == 'PASS'    ${res}
    \    Exit for loop if    '${match}' == 'PASS'
    ${sign}    ${value1}    Run Keyword And Ignore Error    Should Contain    ${critical_res}    {
    ${result}    Run keyword if    '${sign}' == 'PASS'    Fetch from right    ${critical_res}    {
    ${critical_res}    Set variable if    '${sign}' == 'PASS'    ${result}    ${critical_res}
    Return from keyword if    '${critical_res}'!='None'    ${critical_res}

Get warning resource name
    [Documentation]    Get warning resource name
    [Arguments]    ${State}
    ${wss}    Get Regexp Matches    ${State['eventItemValue']}    Warning
    ${lwss}    Get length    ${wss}
    ${stwss}    Run keyword if    ${lwss}==1    split string    ${State['eventItemValue']}    ${SPACE}
    ${warning_res}    Set variable    ${None}
    :FOR    ${item}    in    @{stwss}
    \    ${match}    ${value}    Run Keyword And Ignore Error    Should Contain    ${item}    Warning
    \    ${res}    Run keyword if    '${match}' == 'PASS'    Fetch from left    ${item}    =
    \    ${warning_res}    Set variable if    '${match}' == 'PASS'    ${res}
    \    Exit for loop if    '${match}' == 'PASS'
    ${sign}    ${value1}    Run Keyword And Ignore Error    Should Contain    ${warning_res}    {
    ${result}    Run keyword if    '${sign}' == 'PASS'    Fetch from right    ${warning_res}    {
    ${warning_res}    Set variable if    '${sign}' == 'PASS'    ${result}    ${warning_res}
    Return from keyword if    '${warning_res}'!='None'    ${warning_res}

Check if one resource is in critical or warning state
    [Documentation]    Check if one resource is in critical or warning state
    [Arguments]    ${State}
    ${css}    Get Regexp Matches    ${State['eventDetails'][0]['eventItemValue']}    Critical
    ${lcss}    Get Length    ${css}
    ${stcss}    Run keyword if    ${lcss}==1    Get critical resource name    ${State0}
    ${wss}    Get Regexp Matches    ${State['eventDetails'][0]['eventItemValue']}    Warning
    ${lwss}    Get length    ${wss}
    ${stwss}    Run keyword if    ${lwss}==1    Get warning resource name    ${State0}

Get time
    [Documentation]    Get time
    ${resp}=    get appliance time and locale
    ${time}=    Get Variable Value      ${resp['dateTime']}
    [Return]    ${time}

Get correct dictionary as per specified value
    [Documentation]    Get correct dictionary as per specified value
    [Arguments]    ${l}    ${value}
    ${val}    Set variable    ${None}
    :FOR    ${d}    in    @{l}
    \    ${stat}=    Run keyword and ignore error    Dictionary should contain value    ${d}    ${value}
    \    ${val}    Set variable if    '${stat[0]}'=='PASS'    ${d}
    \    Run keyword if    '${stat[0]}'=='PASS'    Exit for loop
    [Return]    ${val}

Check for alert message and resource health status
    [Documentation]    Check for alert message and resource health status
    [Arguments]    ${input_dict1}    ${input_dict2}    ${time}    ${critical_length}=0    ${warning_length}=0    ${stcss}=None    ${stwss}=None
    ${alerts}=    Get ALL Alerts by Param    param=?filter="associatedResource.resourceUri='${input_dict2['eventItemValue']}' AND created gt ${time} AND alertState = 'Active'"&sort=created:descending&count=1
    Run keyword if    ${critical_length}>1 or ${warning_length}>1    Should Be Equal    '${alerts['members'][0]['description']}'    'The health status of multiple subcomponents is degraded'
    ...    ELSE IF    ${critical_length}==1    Should be Equal    '${alerts['members'][0]['description']}'    'The health status of ${stcss} subcomponent is critical'
    ...    ELSE IF    ${warning_length}==1    Should be Equal    '${alerts['members'][0]['description']}'    'The health status of ${stwss} subcomponent is warning'
    ${value}    Get resource by uri    ${alerts['members'][0]['associatedEventUris'][0]}
    :FOR    ${v}    in    @{value['eventDetails']}
    \    continue for loop if    '${v['eventItemName']}'!='AggregatedHealthStatus'
    \    Run keyword if    '${v['eventItemValue']}'!='${input_dict1['eventItemValue']}'    FAIL

Check for health status with all resouces OK
    [Documentation]    Check for health status with all resouces OK
    [Arguments]    ${input_dict1}    ${input_dict2}    ${time}
    ${alerts}=    Get ALL Alerts by Param    param=?filter="associatedResource.resourceUri='${input_dict2['eventItemValue']}' AND modified gt ${time} AND alertState = 'Cleared'"&sort=created:descending&count=1
    Run keyword if    ${alerts['count']} == 0    FAIL
    ${value}    Get resource by uri    ${alerts['members'][0]['associatedEventUris'][0]}
    :FOR    ${v}    in    @{value['eventDetails']}
    \    continue for loop if    '${v['eventItemName']}'!='AggregatedHealthStatus'
    \    Run keyword if    '${v['eventItemValue']}'!='${input_dict1['eventItemValue']}'    FAIL
