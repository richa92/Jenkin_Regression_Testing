*** Settings ***
Library    setup-helper.py
Library    DateTime

*** Keywords ***
###############
# Appliance
###############
Get appliance IP and Login
    [Documentation]   Setting appliance IP variable off that virtIpv4Addr attribute in data variable file.
    [Arguments]   ${appIPAttr}=virtIpv4Addr
    Run Keyword If   '${APPLIANCE_IP}' == '${null}'   Set Suite Variable   ${APPLIANCE_IP}   ${appliance['applianceNetworks'][0]['${appIPAttr}']}
    Run Keyword If   '${APPLIANCE_IP}' == '${null}'   Fail   msg=APPLIANCE_IP is ${APPLIANCE_IP}. Exiting...
    Run Keyword If   ${tbirdEnv} == ${null}   Detect Enclosure Type And Set Env
    Run Keyword If   ${tbirdEnv} == ${True}   Set Tbird Variables
    ${resp} =   Fusion Api Login Appliance   ${APPLIANCE_IP}   ${admin_credentials}
    Run Keyword If   '${X-Api-Version}' == '${null}'   Set Api Version To Current

Set Api Version To Current
    [Documentation]   Get OV's current API Version and set to use it.
    ${resp} =   Fusion Api Get Resource   /rest/version
    ${X-Api-Version} =   Convert To String   ${resp['currentVersion']}
    Set Suite Variable   ${X-Api-Version}

###############
# General
###############
Set Tbird Variables 
        [Documentation]   Setting up tbird setup variables.
	${FUSION_SSH_USERNAME} =		Set Variable	 ${ssh_credentials['userName']}
	${FUSION_SSH_PASSWORD} =		Set Variable	 ${ssh_credentials['password']}
	${APPLIANCE_IP} =		Set Variable 	${appliance['applianceNetworks'][0]['virtIpv4Addr']}
	Set Suite Variable		${APPLIANCE_IP}
	Set Suite Variable		${FUSION_IP} 	${APPLIANCE_IP}
	Set Suite Variable		${FUSION_SSH_USERNAME}
	Set Suite Variable		${FUSION_SSH_PASSWORD}

Check Network In Profiles
    [Documentation]   Verify that a network is being used by profile(s).
    [Arguments]   ${nsUri}   ${uriAttr}
    ${profiles} =   Fusion Api Get Resource   /rest/server-profiles
    :FOR   ${p}   IN   @{profiles['members']}
    \   ${used} =   Check Network Uri In Connections   ${nsUri}   ${p['connectionSettings']['connections']}   ${uriAttr}
    \   Return From Keyword If   ${used} is ${True}   ${True}
    [Return]   ${False}

Check Network Uri In Connections
    [Documentation]  Verify that network uri is in profile connections.
    [Arguments]   ${nsUri}   ${connections}   ${uriAttr}
    :FOR   ${c}   IN   @{connections}
    \   Return From Keyword If   '${c['${uriAttr}']}' == '${nsUri}'   ${True}
    [Return]   ${False}

Check Data
    [Documentation]   Check that LHS dictionary data is matching the RHS dictionary data. LHS could be a subset of RHS. This is similar to select data compare.
    [Arguments]    ${lhs}   ${rhs}
    ${mismatches} =   Create Dictionary
    :FOR   ${k}   IN   @{lhs.keys()}
    \   ${retval} =   Run Keyword If   '${lhs['${k}']}' == '${rhs['${k}']}'   Log   \nChecking ${k}...[OK]   console=${True}
    \   ...                     ELSE   Set Variable   ${False}
    \   Run Keyword If   ${retval} is ${False}   Set To Dictionary   ${mismatches}   ${k}='${k}' expected data '${lhs['${k}']}' is NOT equal to resource data '${rhs['${k}']}'.
    Run Keyword If   ${mismatches} != &{EMPTY}   \nLog All Data Mismatches   ${mismatches}
    Return From Keyword If   ${mismatches} != &{EMPTY}   ${False}
    [Return]   ${True}

Response Body Should Have Expected Members
    [Documentation]   Check that response body have expected length, count, and total.
    [Arguments]   ${response}   ${expLength}   ${expCount}   ${expTotal}
    Length Should Be   ${response['members']}   ${expLength}   msg=Response body does not contain the expected members length.
    Should Be Equal   ${response['count']}   ${expCount}   msg=Response body count is not ${expCount}.
    Should Be Equal   ${response['total']}   ${expTotal}   msg=Response body total is not ${expTotal}.

Filter Response By Attribute
   [Documentation]   Filter response by a key-value pair.
   [Arguments]   ${resp}   ${key}   ${value}
   :FOR   ${m}   IN   @{resp['members']}
   \   Return From Keyword If   '${m['${key}']}' == '${value}'   ${m}
   [Return]   ${null}

Sleep And Log Reason To Console
    [Documentation]   Sleep for a given time and log reason to both console and logfile. Sleep has a reason option but it won't log to console (only in logfile) so we are wrapping them here.
    [Arguments]   ${sleep}   ${reason}=${null}
    ${dateTime} =   Get Current Date
    Log To Console   \n[${dateTime}] ${reason}
    Sleep   ${sleep}   reason=${reason}

Resolve Uri By Name
    [Documentation]	Takes a string containing URI type + : + resource name, performs a lookup by type to determine
    ...  what the resource type is and then does a GET on that type to return the resource URI
    ...
    ...             Ex:    ${uri} =    Resolve Uri By Name    LIG:LIG1
    ...             Ex:    ${uri} =     Resolve Uri By Name    ServerProfileTemplateV4:480_G9_NoRaid
    [Arguments]    ${uri}
    @{words} =    Split String    ${uri}        :       1
    ${type} =     Get From List    ${words}    0
    Return From Keyword If    '${uri}' == '${type}'    ${uri}
    ${name} =    Get From List    ${words}    1

    #  Add lookup via short type name and/or full type.
    #  For multiple versions that utilize the same api call, you can specify V\\d* to be used as a regexp
    #  as in LogicalEnclosureV\\d*=Get Logical Enclosure URI
    #
    #  See "Get From Dictionary Key then Regexp" keyword helper below
    #
    ${lookup} =    Create Dictionary
    ...    DE=Get Drive Enclosure URI
    ...    drive-enclosure=Get Drive Enclosure URI
    ...    DriveEnclosureV\\d*=Get Drive Enclosure URI
    ...    EG=Get Enclosure Group URI
    ...    EnclosureGroupV\\d*=Get Enclosure Group URI
    ...    ENC=Get Enclosure URI
    ...    EnclosureV\\d*=Get Enclosure URI
    ...    ETH=Get Ethernet URI
    ...    ethernet-networkV\\d*=Get Ethernet URI
    ...    FC=Get FC URI
    ...    fc-networkV\\d*=Get FC URI
    ...    FCOE=Get FCoE URI
    ...    fcoe-networkV\\d*=GET FCoE URI
    ...    firmware-baselines=Get Firmware Bundle URI
    ...    HCP=Get Cluster Profile Uri by Name
    ...    HypervisorClusterProfileV\\d*=Get Cluster Profile Uri by Name
    ...    HHP=Get Host Profile Uri By Name
    ...    HypervisorHostProfileV\\d*=Get Host Profile Uri By Name
    ...    HM=Get Hypervisor Manager URI
    ...    HypervisorManagerV\\d*=Get Hypervisor Manager URI
    ...    IC=Get IC URI
    ...    InterconnectV\\d*=Get IC URI
    ...    ICTYPE=Get Interconnect Type URI
    ...    LE=Get Logical Enclosure URI
    ...    LI=Get LI URI
    ...    LIG=Get LIG URI
    ...    LogicalEnclosureV\\d*=Get Logical Enclosure URI
    ...    logical-interconnectV\\d*=Get LI URI
    ...    logical-interconnect-groupV\\d*=Get LIG URI
    ...    NS=Get Network Set URI
    ...    network-setV\\d*=Get Network Set URI
    ...    Osdp=Get OSDP URI
    ...    OsdpV\\d*=Get OSDP URI
    ...    SASIC=Get Sas Interconnect URI
    ...    SasInterconnectV\\d*=Get Sas Interconnect URI
    ...    SASICTYPE=Get Sas Interconnect type URI
    ...    sas-interconnect=Get Sas Interconnect URI
    ...    SASLIG=Get SASLIG URI
    ...    sas-logical-interconnect-groupV\\d*=Get SASLIG URI
    ...    SASLI=Get SAS LI URI
    ...    SASLJBOD=Get Sas Logical Jbod URI
    ...    sas-logical-jbod=Get Sas Logical Jbod URI
    ...    sas-logical-jbodV\\d*=Get Sas Logical Jbod URI
    ...    SASLJBODATT=Get Sas Logical Jbod Attachment URI
    ...    sas-logical-jbod-attachment=Get Sas Logical Jbod Attachment URI
    ...    server-hardware-\\d*=Get Server Hardware URI
    ...    SH=Get Server Hardware URI
    ...    SHT=common.Get Server Hardware Type URI
    ...    SP=Get Server Profile URI
    ...    ServerProfileV\\d*=Get Server Profile URI
    ...    SPT=Get Server Profile Template URI
    ...    ServerProfileTemplateV\\d*=Get Server Profile Template URI
    ...    US=Get Uplink Set URI
    ...    SAN=Get San Manager URI
    ...    SANManager=Get San Manager URI
    ...    FCDeviceManagerV\\d*=Get San Manager URI
    ...    FCPROV=Get Provider URI
    ...    FCProvider=Get Provider URI
    ...    FCSanV\\d*=Get Managed SAN URI
    ...    FCSan=Get Managed SAN URI
    ...    SSYS=Get Storage System URI
    ...    SVOL=Get Storage Volume URI
    ...    Scope=Get Scope URI By Name
    ...    ScopeV\\d*=Get Scope URI By Name
    ...    SPOOL=Get Storage Pool URI
    ...    SVT=Get Storage Volume Template URI
    ...    StorageVolumeTemplateV\\d*=Get Storage Volume Template URI
    ...    StoragePoolV\\d*=Get Storage Pool URI
    ...    StorageSystemV\\d*=Get Storage System URI
    ...    StorageVolumeV\\d*=Get Storage Volume URI
    ...    SWT=Get Switch Type Uri By Name
    ...    UserAndRoles=Get User URI
    ...    USER=Get User URI

    ${api} =    Get From Dictionary Key then Regexp     ${lookup}   ${type}

    Return From Keyword If    '${api}'=='ResourceTypeNotFound'    ResourceTypeNotFound:${type}

    ${uri} =    Run Keyword    ${api}    ${name}

	[Return]    ${uri}

Get From Dictionary Key then Regexp
    [Documentation]    First tries to use ${type} as a key to ${lookup}.
    ...    If that lookup fails then tries keys a Regexp to match ${type} for "wildcard" match
    [Arguments]    ${lookup}    ${type}

    ${status}     ${api} =  Run Keyword and Ignore Error    Get From Dictionary    ${lookup}   ${type}
    Return from Keyword If    '${status}'=='PASS'    ${api}

    ${keys} =    Get Dictionary Keys    ${lookup}
    :FOR    ${regexp_type}    in   @{keys}
    \    ${found_match} =    Run Keyword and Return Status    Should Match Regexp    ${type}    ^${regexp_type}$
    \    Return From Keyword If    '${found_match}'=='${True}'   ${lookup['${regexp_type}']}

    [Return]    ResourceTypeNotFound

Get Server Hardware Type URI
    [Documentation]    Get Server Hardware Type URI
	[Arguments]		${sht}
	Set Log Level	TRACE

    # this section added to support supplying of Mezz card info as Multiple blades can create multiple similar SHTs
    # caller can specify a name similar to:
    #       SY 480 Gen9:1:Smart Array P542D Controller:3:HPE Synergy 3520C 10/20Gb Converged Network Adapter
    #   syntax is Blade_Model:Slot #:Adapter_Model[:Slot #:Adapter_Model]
    #   default is to assume Mezz for Slot numbers.  :1: -> Mezz 1
    #   To specify FlexLOM for C7000 use Flb# or for Embedded use Lom#
    #   BL465c Gen8:Flb1:HP Flex-10 10Gb 2-port 530FLB Adapter:1:HP FlexFabric 10Gb 2-port 554M Adapter:2:HP LPe1205A 8Gb FC HBA for BladeSystem c-Class
    #   BL685c G7:Lom1:FlexFabric Embedded Ethernet:1:HP NC532m Dual Port Flex-10 10GbE Multifunction BL-c Adapter
    #
    #   SHT can be performed by indirect loookup by simply specifying the actual blade and get the sht uri
    #   as in:  SH:CN750163KD, bay 1
    #
	@{temp} =    Split String    ${sht}    :
    ${length} =    Get Length    ${temp}
    # user specifed lookup by Mezz/Flb slots and adapters
    Run Keyword and Return if    ${length}>1 and '${temp[0]}'!='SH'    common.Get Server Hardware Type URI By Name And Mezz    ${sht}
    # or did user specified lookup by Server Hardware
    Run Keyword and Return if    '${temp[0]}'=='SH'    common.Get Server Hardware Type URI By Server Hardware    ${temp[1]}

	${resp} = 	Fusion Api Get Server Hardware Types    param=?filter="'name'=='${sht}'"
	${count} =  Get From Dictionary  ${resp}  count
	Return from keyword if  ${count}==0  '/bad_sht_uri'
	${uri} = 	Get From dictionary 	${resp['members'][0]}	uri
	[Return]	${uri}

Log To Console Errors In Dictionary
    [Documentation]   Log to console all the errors and details stored in dictionary.
    [Arguments]   ${dict_of_issues}
    :FOR   ${issue}   IN   @{dict_of_issues.keys()}
    \   Log To Console   \n${issue}, ${dict_of_issues['${issue}']}

###############
# Error Checking
###############
Check Asynchronous Task Response For Error
    [Documentation]   Check asynchronous request response body and parse error(s) if any.
    [Arguments]    ${resp}   ${processErrorCode}=${Null}
    ${location} =    Get Variable Value    ${resp['headers']['location']}
    ${taskUri} =    Run Keyword If    '${location}' is not 'None'   Get Variable Value    ${location}
    ...                     ELSE IF   ${resp['associatedResource']} is not ${null}   Get From Dictionary	${resp['associatedResource']}	resourceUri
    ...                        ELSE   Get From Dictionary   ${resp}   uri
    ${resourceName} = 	Run Keyword If   ${resp['associatedResource']} is not ${null}   Get From Dictionary	${resp['associatedResource']}	resourceName
    Run Keyword If   '${taskUri}' == '${null}'   Log To Console   Resource name ${resourceName} has a uri of ${null}. Checking error if any...
    Log   \n Task: [${resp['category']}:${resp['name']}] is: ${resp['taskState']} for resource: ${resourceName}   console=${True}
    ${l} =   Get Length   ${resp['taskErrors']}
    ${errorCodeFound} =   Set Variable   ${False}
    :FOR   ${i}   IN RANGE   0   ${l}
    \   Log   \n errorCode: ${resp['taskErrors'][${i}]['errorCode']} \n errorSource: ${resp['taskErrors'][${i}]['errorSource']} \n message: ${resp['taskErrors'][${i}]['message']} \n recommendedActions: ${resp['taskErrors'][${i}]['recommendedActions']}   console=${True}
    \   Run Keyword If   '${resp['taskErrors'][${i}]['errorCode']}' == '${processErrorCode}'   Set Test Variable   ${errorCodeFound}   ${True}
    Run Keyword If   ${l} > ${0} and '${processErrorCode}' == '${null}'   Fail   msg=Task [${resp['category']}:${resp['name']}] for resource ${resourceName} failed.
    ...    ELSE IF   '${processErrorCode}' != '${null}' and ${errorCodeFound} is ${True}   Return From Keyword   ${processErrorCode}
    ...    ELSE   Return From Keyword   ${Null}
    [Return]   ${Null}

Asynchronous Task Should Be Successful
    [Documentation]   Check that asynchronous task was successful and resourceUri is not null.
    ...               This does not follow the task and assumed task response was from wait for task keyword.
    [Arguments]    ${task}   ${checkAssociatedResourceUri}=${True}
    Run Keyword If   ${task} == ${null}   Fail  msg=Task is ${null}.
    ${associatedResourceUri} = 	Get From Dictionary	${task['associatedResource']}	resourceUri
    ${associatedResourceName} = 	Get From Dictionary	${task['associatedResource']}	resourceName
    Run Keyword If   '${associatedResourceUri}' == '${null}'   Log   \n associatedResourceName is ${null} and resourceUri is ${null} for this resource. Parsing task for errors (if any)...   console=${True}
    Log   \n Task: [${task['category']}:${task['name']}] is: ${task['taskState']} for resource: ${associatedResourceName}   console=${True}
    ${l} =   Get Length   ${task['taskErrors']}
    :FOR   ${i}   IN RANGE   0   ${l}
    \   Log   \n errorCode: ${task['taskErrors'][${i}]['errorCode']}\n errorSource: ${task['taskErrors'][${i}]['errorSource']}\n message: ${task['taskErrors'][${i}]['message']}\n recommendedActions: ${task['taskErrors'][${i}]['recommendedActions']}   console=${True}
    Run Keyword If   ${checkAssociatedResourceUri} == ${True} and '${associatedResourceUri}' == '${null}'   Fail   msg=Failed to create ${associatedResourceName}.
    Run Keyword If   ${l} > 0   Fail   msg=Task error was found!

Request Should Be Successful
    [Documentation]   Check that a request has expected status code.
    [Arguments]   ${resp}   ${expectedStatusCode}=${201}
    Return From Keyword If   ${resp['status_code']} == ${expectedStatusCode}   ${resp['status_code']}
    Fail   msg=Request failed!\n errorCode: ${resp['errorCode']}\n errorSource: ${resp['errorSource']}\n message: ${resp['message']}\n details: ${resp['details']}\n recommendedActions: ${resp['recommendedActions']}

Response Should Contain Error Code
    [Documentation]   Check that response body contain the expected error code.
    [Arguments]   ${response}   ${expectedErrorCode}
    Run Keyword If   '${response['errorCode']}' != '${expectedErrorCode}'   Fail   msg=Response body did not contain the expected error code: ${expectedErrorCode}

Response Should Not Contain Error
    [Documentation]   Check that response body does not contain error.
    [Arguments]   ${response}   ${expectedStatusCode}=${204}   ${wait_task_timeout}=60m   ${wait_task_interval}=2s
    Request Should Be Successful   ${response}   expectedStatusCode=${expectedStatusCode}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${response}   ${wait_task_timeout}   ${wait_task_interval}   status_code=${expectedStatusCode}
    Asynchronous Task Should Be Successful   ${task}

Wait For Forked Tasks
    [Documentation]    Wait for forked tasks (off the response body list of dictionary) to reach end state
    [Arguments]    ${respList}    ${valDict}    ${timeout}=60m    ${interval}=5s    ${validate}=${True}   ${processErrorCode}=${Null}   ${throttle}=${Null}
    ${respList} =   Wait Until Keyword Succeeds    ${timeout}    ${interval}    common.Forked Tasks Reached Endstate     ${respList}   ${valDict}   ${validate}   proceedPressAndHold=${processErrorCode}   throttle=${throttle}
    [Return]   ${respList}

Forked Tasks Reached Endstate
    [Documentation]    Look up through all the forked tasks to see if they reached end state
    [Arguments]    ${respList}    ${valDict}    ${validate}=${True}   ${proceedPressAndHold}=${Null}   ${throttle}=${Null}
    ${match} =    Set Variable    ${0}
    ${l} = 	  Get Length    ${respList}
    ${taskStateList} =    Create List    Warning  Unknown  Terminated  Killed  Error  Completed
    :FOR    ${x}    IN RANGE   0    ${l}
    \    ${location} =    Get Variable Value    ${respList[${x}]['headers']['location']}
    \    ${task_uri} =    Run Keyword If    '${location}' is 'None'    Get From Dictionary    ${respList[${x}]}    uri
    \    ...     ELSE    Get Variable Value    ${location}
    \    Should Not Be Empty    ${task_uri}    msg=No task uri could be retreived from response.
    \    ${task} =    Fusion Api Get Task    uri=${task_uri}
    \    ${match} =    Run Keyword If    ${validate} == ${True}    Count Values In List   ${taskStateList}    ${task['taskState']}
    \    Run Keyword If    ${match} > ${0}    Remove From List     ${respList}    ${x}
    \    Run Keyword If    ${validate} == ${True}    Log To Console   \t Task: [${task['category']}:${task['name']}] is: ${task['taskState']} for resource: ${task['associatedResource']['resourceName']} ${task['associatedResource']['resourceUri']}
    \   ${retstatus}   ${retval} =   Run Keyword And Ignore Error   Check Asynchronous Task Response For Error   ${task}   processErrorCode=${proceedPressAndHold}
    \   Run Keyword If   '${retval}' != '${Null}' and '${retstatus}' == 'PASS'   common.Power Off Server Uri   ${task['associatedResource']['resourceUri']}   powerControl=PressAndHold
    \   ...    ELSE IF   ${task['taskErrors']} != @{EMPTY}   Set Suite Variable   ${forkedErrorFound}   ${True}
    # When throttle is on, return the respList so we can push one when we pop one
    # If there is a match and we are not throttling, continue with loop. Otherwise, fail the keyword so it will re-attempt until keyword succeeds
    \   Run Keyword If   ${match} > ${0} and '${throttle}' != '${Null}'   Return From Keyword    ${respList}
    \   ...    ELSE IF   ${match} == ${0}    FAIL   msg=Forked task is still in progress. Polling for task state...

Check Response For Error
   [Documentation]   Check response body for error and parse if any.
   [Arguments]   ${resp}
   Return From Keyword If   ${resp['status_code']} == ${200} or ${resp['status_code']} == ${202}   ${resp['status_code']}
   Fail   msg=\n errorCode: ${resp['errorCode']} \n errorSource: ${resp['errorSource']} \n message: ${resp['message']} \n recommendedActions: ${resp['recommendedActions']}

###############
# Server Profile Templates
###############
Add Server Profile Templates From Variable
    [Documentation]   Adds Server Profile Templates to an appliance from a variable which contains a list of dicts with the entire payload
    [Arguments]   ${profileTemplates}   ${waitTime}=300m   ${interval}=5s   ${connectionSettingsApi}=${600}   ${waitForTask}=${True}  ${parallel}=${False}   ${validate}=${True}
    ${log_message} =   Run Keyword If   '${parallel}' == '${True}'   Set Variable   \n\nAdding SERVER PROFILE TEMPLATES in parallel (status may not reflect right away)...
    ...   ELSE   Set Variable   \n\nAdding SERVER PROFILE TEMPLATES...
    Log   ${log_message}   console=${True}
    ${valDict} =   Create Dictionary   status_code=${200}
    ...                                taskState=Completed
    ${respList} =   Create List
    Set Suite Variable   ${forkedErrorFound}   ${False}
    :FOR   ${profile}   IN   @{profileTemplates}
    \   ${profile} =   fusion_api_appliance_setup.Copy Dictionary   ${profile}
    \   ${resp} =   Fusion Api Get Server Hardware
    \   ${serverHW} =    Fusion Api Get Resource    uri=${resp['members'][0]['uri']}
    \   Set To Dictionary    ${profile}   serverHardwareTypeUri=${serverHW['serverHardwareTypeUri']}
    \   ${eg} =   Get from Dictionary   ${profile}   enclosureGroupUri
    \   @{words} =   Split String   ${eg}   :
    \   ${type} =   Get From List   ${words}   0
    \   ${eg} =   Get From List   ${words}   1
    \   ${uri} =   Get Enclosure Group URI   ${eg}
    \   Set to Dictionary   ${profile}   enclosureGroupUri   ${uri}
    \   ${profile} =   Resolve Profile Connections   ${profile}   connectionSettingsApi=${connectionSettingsApi}
    \   ${resp} =   Fusion Api Create Server Profile template   body=${profile}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \       Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
    \       ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Add Rack-mount Server Profile Templates From Variable
    [Documentation]   Adds rack-mount Server Profile Templates to an appliance from a variable which contains a list of dicts with the entire payload
    [Arguments]   ${profileTemplates}   ${waitTime}=300m   ${interval}=5s   ${connectionSettingsApi}=${600}   ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}
    ${log_message} =   Run Keyword If   '${parallel}' == '${True}'   Set Variable   \n\nAdding rack-mount SERVER PROFILE TEMPLATES in parallel (status may not reflect right away)...
    ...   ELSE   Set Variable   \n\nAdding rack-mount SERVER PROFILE TEMPLATES...
    Log   ${log_message}   console=${True}
    ${valDict} =   Create Dictionary   status_code=${200}
    ...                                taskState=Completed
    ${respList} =   Create List
    Set Suite Variable   ${forkedErrorFound}   ${False}
    :FOR   ${profile}   IN   @{profileTemplates}
    \   ${profile} =   fusion_api_appliance_setup.Copy Dictionary   ${profile}
    \   ${sht_uri} =   Resolve Uri By Name   ${profile['serverHardwareTypeUri']}
    \   Set To Dictionary    ${profile}   serverHardwareTypeUri=${sht_uri}
    \   ${profile} =   Resolve Profile Connections   ${profile}   connectionSettingsApi=${connectionSettingsApi}
    \   ${resp} =   Fusion Api Create Server Profile template   body=${profile}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \       Continue For Loop If   ${waitForTask} != ${True}
    \       Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
    \       ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Get Server Profile Template Uri
    [Documentation]   Query OneView for server profile template name and return matching uri.
    [Arguments]   ${name}
    ${resp} =   Fusion Api Get Server Profile Templates   param=?filter=name='${name}'
    [Return]   ${resp['members'][0]['uri']}

Remove All Server Profile Templates In Parallel
    [Documentation]   Remove all server profiles templates from OneView.
    [Arguments]   ${waitTime}=300m   ${interval}=5s  ${waitForTask}=${True}  ${parallelAssign}=${True}   ${validate}=${True}
    Log   \n\nRemoving SERVER PROFILE Templates...   console=${True}
    ${templates} =   Fusion Api Get Server Profile Templates
    ${valDict} =    Create Dictionary   status_code=${200}
    ...                                 taskState=Completed
    ${respList} =   Create List
    Set Suite Variable   ${forkedErrorFound}   ${False}
    :FOR	${profileT}	IN	@{templates['members']}
    \	${resp} = 	Fusion Api Delete Server Profile Template   uri=${profileT['uri']}
    \       Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \       Continue For Loop If   ${waitForTask} != ${True}
    \       Run Keyword If   ${parallelAssign} == ${True}   Append To List   ${respList}   ${resp}
    \       ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${parallelAssign} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

###############
# Server Profiles
###############
Add Rack-mount Server Profiles From Variable
    [Documentation]   Add rack-mount server profiles from data variable file.
    [Arguments]   ${server_profiles}   ${timeout}=860m   ${interval}=5s   ${endstate}=((?i)Warning|Completed)    ${forceProfileApply}=false   ${waitForTask}=${True}   ${parallel}=${True}   ${validate}=${True}
    ${param} =   Run Keyword If   '${forceProfileApply}' != 'false'   Set Variable   ?force="${forceProfileApply}"
    ...                    ELSE   Set Variable   ${EMPTY}
    ${log_message} =   Run Keyword If   '${parallel}' == '${True}'   Set Variable   \n\nAdding SERVER PROFILES in parallel (status may not reflect right away)...
    ...   ELSE   Set Variable   \n\nAdding SERVER PROFILES...
    Log   ${log_message}   console=${True}
    ${respList} =   Create List
    Set Suite Variable   ${forkedErrorFound}   ${False}
    ${valDict} =    Create Dictionary   status_code=${200}
    ...                                 taskState=Completed
    :FOR   ${profile}   IN   @{server_profiles}
    \   ${profile} =    fusion_api_appliance_setup.Copy Dictionary     ${profile}
    \   ${space} =   Check For Whitespace From String   ${profile['name']}
    \   Run Keyword If   ${space} is ${True}   Fail   msg=Profile name contains whitespace. This is not allowed in CI-FIT naming convention.
    \	${shuri} = 	Get from Dictionary	${profile}	serverHardwareUri
    \	${uri} = 	Get Server Hardware URI		${shuri}
    \	Set to Dictionary	${profile}	serverHardwareUri	${uri}
    \	${profile} = 	Update connections in profile    ${profile}
    \	${resp} = 	Fusion Api Create Server Profile		body=${profile}   param=${param}
    \       Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   Continue For Loop If   ${waitForTask} != ${True}
    \   Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
    \   ...   ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${timeout}   ${interval}   ${validate}
    Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${timeout}   ${interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Remove All Server Profiles In Parallel
	[Documentation]	Querys the appliance for all Server Profiles and then removes them
    ...             NOTE: If ${waitForTask} is false, ${parallel} and ${validate} becomes moot. Just fork the process and exit.
    [Arguments]   ${waitTime}=300m   ${interval}=5s  ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}    ${force}=${False}
	${log_message} =   Run Keyword If   '${parallel}' == '${True}'   Set Variable   \n\nRemoving SERVER PROFILES in parallel (status may not reflect right away)...
	...                ELSE   Set Variable   \n\nRemoving SERVER PROFILES
	log   ${log_message}   console=${True}
	${param} =  set variable if  ${force}==${False}  ${Empty}  ?force=${True}
	${profiles} = 	Fusion Api Get Server Profiles  param=?sort=name:ascending
    ${valDict} =    Create Dictionary   status_code=${200}
    ...                                 taskState=Completed
    ${respList} =   Create List
    Set Suite Variable   ${forkedErrorFound}   ${False}
	:FOR	${profile}	IN	@{profiles['members']}
	\	${resp} = 	Fusion Api Delete Server Profile		uri=${profile['uri']}       param=${param}
	\       Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \       Continue For Loop If   ${waitForTask} != ${True}
    \       Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
    \       ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Add Unassigned Server Profiles
	[Documentation]	Adds Server Profiles to an appliance from a variable file in without assigning server hardware.
	[Arguments]		${profiles}   ${server_profile_to_bay_map}   ${waitTime}=860m   ${interval}=2s   ${waitForTask}=${True}  ${parallel}=${False}   ${validate}=${True}
        ${log_message} =   Run Keyword If   '${parallel}' == '${True}'   Set Variable   \n\nAdding SERVER PROFILES in parallel (status may not reflect right away)...
        ...   ELSE   Set Variable   \n\nAdding SERVER PROFILES...
        Log   ${log_message}   console=${True}
        ${valDict} =    Create Dictionary   status_code=${200}
        ...                                 taskState=Completed
        ${respList} =   Create List
        Set Suite Variable   ${forkedErrorFound}   ${False}
	:FOR	${profile}	IN	@{profiles}
	\       ${profile} =    fusion_api_appliance_setup.Copy Dictionary     ${profile}
        \       ${spaceName} =   Check For Whitespace From String   ${profile['name']}
        \       Run Keyword If   ${spaceName} is ${True}   Fail   msg=Profile name contains whitespace. This is not allowed in CI-FIT naming convention.
        \       ${resp} =   Run Keyword If   '${server_profile_to_bay_map['${profile['name']}']}' == '${null}'   Fusion Api Get Server Hardware
        \       ${shUri} =   Run Keyword If   ${resp} == ${null}   Get Server Hardware URI    ${server_profile_to_bay_map['${profile['name']}']}
        \       ...                    ELSE   Set Variable   ${resp['members'][0]['uri']}
        \       ${serverHW} =    Fusion Api Get Resource    uri=${shUri}
	\       Set To Dictionary    ${profile}   serverHardwareTypeUri=${serverHW['serverHardwareTypeUri']}
	\	${eg} = 	Get from Dictionary	${profile}	enclosureGroupUri
	\	@{words} = 	Split String	${eg}	:
	\	${type} = 	Get From List	${words}	0
	\	${eg} = 	Get From List	${words}	1
	\	${uri} = 	Get Enclosure Group URI	${eg}
        \       ${profile} =   Resolve Profile Template Uri   ${profile}
	\	Set to Dictionary	${profile}	enclosureGroupUri	${uri}
        \       ${profile} =   Resolve Profile Connections   ${profile}
	\	${resp} = 	Fusion Api Create Server Profile		body=${profile}
	\       Request Should Be Successful   ${resp}   expectedStatusCode=${202}
        \       Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
        \       ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${waitTime}   ${interval}   ${validate}
        Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}
        Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Add Unassigned Rack-mount Server Profiles
	[Documentation]	Adds rack-mount Server Profiles to an appliance from a variable file in without assigning server hardware.
	[Arguments]		${profiles}   ${server_profile_to_bay_map}   ${waitTime}=860m   ${interval}=1s   ${waitForTask}=${True}   ${parallel}=${True}   ${validate}=${True}
        ${log_message} =   Run Keyword If   '${parallel}' == '${True}'   Set Variable   \n\nAdding Rack-mount SERVER PROFILES in parallel (status may not reflect right away)...
        ...   ELSE   Set Variable   \n\nAdding Rack-mount SERVER PROFILES...
        Log   ${log_message}   console=${True}
        ${respList} =   Create List
        Set Suite Variable   ${forkedErrorFound}   ${False}
        ${valDict} =    Create Dictionary   status_code=${200}
        ...                                 taskState=Completed
	:FOR	${profile}	IN	@{profiles}
	\       ${profile} =    fusion_api_appliance_setup.Copy Dictionary     ${profile}
        \       ${spaceName} =   Check For Whitespace From String   ${profile['name']}
        \       Run Keyword If   ${spaceName} is ${True}   Fail   msg=Profile name contains whitespace. This is not allowed in CI-FIT naming convention.
        \       ${resp} =   Run Keyword If   '${server_profile_to_bay_map['${profile['name']}']}' == '${null}'   Fusion Api Get Server Hardware
        \       ${shUri} =   Run Keyword If   ${resp} == ${null}   Get Server Hardware URI    ${server_profile_to_bay_map['${profile['name']}']}
        \       ...                    ELSE   Set Variable   ${resp['members'][0]['uri']}
        \       ${serverHW} =    Fusion Api Get Resource    uri=${shUri}
	\       Set To Dictionary    ${profile}   serverHardwareTypeUri=${serverHW['serverHardwareTypeUri']}
        \       ${profile} =   Resolve Profile Template Uri   ${profile}
        \       ${profile} =   Resolve Profile Connections   ${profile}
	\	${resp} = 	Fusion Api Create Server Profile		body=${profile}
	\       Request Should Be Successful   ${resp}   expectedStatusCode=${202}
        \   Continue For Loop If   ${waitForTask} != ${True}
        \   Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
	\   ...   ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${waitTime}   ${interval}   ${validate}
        Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}
        Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Assign Server Hardware To Existing Profiles From Variable
	[Documentation]	Update Server Profiles from a variable with server hardware assigned to profile from mapping variable
        ...             NOTE: If ${waitForTask} is false, ${parallel} and ${validate} becomes moot. Just fork the process and exit.
	[Arguments]		${profiles}   ${server_profile_to_bay_map}   ${timeout}=860m   ${interval}=15s  ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}   ${forceProfileApply}=false   ${throttle}=${Null}
        ${param} =   Run Keyword If   '${forceProfileApply}' != 'false'   Set Variable   ?force="${forceProfileApply}"
        ...                    ELSE   Set Variable   ${EMPTY}
	${existing_profiles} =  	Fusion Api Get Server Profiles
	${profile_members}	Get From Dictionary	${existing_profiles}	members
	${Count} =	Get From Dictionary	${existing_profiles}	count
        ${valDict} =    Create Dictionary   status_code=${200}
        ...                                 taskState=Completed
        ${respList} =   Create List
        Set Suite Variable   ${forkedErrorFound}   ${False}
	:FOR 	${Index}	IN RANGE	0	${Count}
	\	${sp}		Get From List	${profile_members}	${Index}
        \       Continue For Loop If   '${server_profile_to_bay_map['${sp['name']}']}' == '${null}'
	\	${shUri} = 	Get Server Hardware URI    ${server_profile_to_bay_map['${sp['name']}']}
        \       ${profile} =    Fusion Api Get Resource    uri=${sp['uri']}
	\       Set To Dictionary    ${profile}   serverHardwareUri=${shUri}
        \       Remove From Dictionary    ${profile}   status_code    headers
        \	Log To Console 	 \nAssigning server hardware URI \"${shUri}\" to profile \"${sp['name']}\"
        \       ${resp} =   Fusion Api Edit Server Profile    uri=${sp['uri']}   body=${profile}   param=${param}
        \       Continue For Loop If   ${waitForTask} != ${True}
        \       Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
        \       ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${timeout}   ${interval}   ${validate}
        \       Continue For Loop If   '${throttle}' == '${Null}'
        \       Continue For Loop If   ${parallel} != ${True}
        \       ${respLength} =   Get Length   ${respList}
        \       Continue For Loop If   ${respLength} != ${throttle}
        \       ${respList} =   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${timeout}   ${interval}   ${validate}   throttle=${throttle}
        Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${timeout}   ${interval}   ${validate}
        Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Unassign Server Profiles
        [Documentation]   Update server profiles in OneView by unassigning the server hardware from it. Argument requires list of dictionary of profiles that contains a valid server profile uri (e.g.: [{'uri': '/rest/server-profiles/8e2ec303-1274-4b9e-9871-b08f77bcc675'}]).
        ...               NOTE: See robustness' LE-add-remove.txt script for example.
        [Arguments]     ${profiles}    ${timeout}=860m   ${interval}=15s  ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}   ${forceProfileApply}=false   ${throttle}=${Null}
        Set Log Level	TRACE
        ${param} =   Run Keyword If   '${forceProfileApply}' != 'false'   Set Variable   ?force="${forceProfileApply}"
        ...                    ELSE   Set Variable   ${EMPTY}
        ${valDict} =    Create Dictionary   status_code=${200}
        ...                                 taskState=Completed
        ${respList} =   Create List
        Set Suite Variable   ${forkedErrorFound}   ${False}
        :FOR   ${p}   IN   @{profiles}
        \   ${profile} =    Fusion Api Get Resource    uri=${p['uri']}
        \   Log   \n\nUnassigning server hardware URI \"${profile['serverHardwareUri']}\" from profile \"${p['name']}\"   console=${True}
        \   set to dictionary    ${profile}   serverHardwareUri=${None}
        \   set to dictionary    ${profile}   enclosureBay=${None}
        \   set to dictionary    ${profile}   enclosureUri=${None}
        \   remove from dictionary    ${profile}   status_code    headers
        \   ${resp} =   fusion api edit server profile    uri=${p['uri']}   body=${profile}   param=${param}
        \   Continue For Loop If   ${waitForTask} != ${True}
        \   Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
        \   ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${timeout}   ${interval}   ${validate}
        \       Continue For Loop If   '${throttle}' == '${Null}'
        \       Continue For Loop If   ${parallel} != ${True}
        \       ${respLength} =   Get Length   ${respList}
        \       Continue For Loop If   ${respLength} != ${throttle}
        \       ${respList} =   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${timeout}   ${interval}   ${validate}   throttle=${throttle}
        Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${timeout}   ${interval}   ${validate}
        Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Resolve Profile Connections
    [Documentation]   Update profile connections based on the X-API-Version. This look up the connections and resolve the corresponding uris. Returns updated profile.
    [Arguments]   ${profile}   ${connectionSettingsApi}=${600}
    ${connectionSettings} =   Evaluate   ${profile}.get('connectionSettings', None)
    ${connections} =   Run Keyword If   ${X-API-Version} >= ${connectionSettingsApi} and ${connectionSettings} is not ${null}   Evaluate   ${profile['connectionSettings']}.get("connections",None)
    ...                          ELSE   Evaluate   ${profile}.get("connections",None)
    ${connections} =   Run Keyword If   ${connections} is not ${null}   Lookup Connection Uris	${connections}
    Return From Keyword If   ${connections} is ${null}   ${profile}
    Run Keyword If   ${X-API-Version} >= ${connectionSettingsApi}   Set to Dictionary   ${profile['connectionSettings']}  connections     ${connections}
    ...       ELSE   Set to Dictionary   ${profile}   connections     ${connections}
    [Return]   ${profile}

Resolve Profile Template Uri
    [Documentation]   Query OneView and resolve profile template uri by name.
    [Arguments]   ${profile}
    ${template} =   Evaluate   ${profile}.get("serverProfileTemplateUri",None)
    ${templateUri} =   Run Keyword If   '${template}' != '${null}'   Get Server Profile Template Uri   ${profile['serverProfileTemplateUri']}
    Run Keyword If   '${templateUri}' != '${null}'   Set To Dictionary   ${profile}   serverProfileTemplateUri   ${templateUri}
    [Return]   ${profile}

Add Server Profiles Using Template From Variable
    [Documentation]   Get template data, update template with profile data variable, create profile.
    [Arguments]   ${profiles}   ${server_profile_to_bay_map}   ${waitTime}=300m   ${interval}=2s   ${validate}=${True}   ${connectionSettingsApi}=${600}   ${waitForTask}=${True}  ${parallel}=${False}   ${validate}=${True}
    ${log_message} =   Run Keyword If   '${parallel}' == '${True}'   Set Variable   \n\nAdding SERVER PROFILES from TEMPLATES in parallel (status may not reflect right away)...
    ...   ELSE   Set Variable   \n\nAdding SERVER PROFILES from TEMPLATES...
    Log   ${log_message}   console=${True}
    ${valDict} =   Create Dictionary   status_code=${200}
    ...                                taskState=Completed
    ${respList} =   Create List
    Set Suite Variable   ${forkedErrorFound}   ${False}
    :FOR   ${profile}   IN   @{profiles}
    \   ${profile} =    fusion_api_appliance_setup.Copy Dictionary     ${profile}
    \   ${templateResp} =   Fusion Api Get Server Profile Templates   param=?filter="name='${profile['serverProfileTemplateUri']}'"
    \   Response Body Should Have Expected Members   ${templateResp}   ${1}   ${1}   ${1}
    \   ${templateResp} =   Fusion Api Get Server Profile Template New Profile   uri=${templateResp['members'][0]['uri']}
    # This sucks but FusionLibrary modified response body to include status_code and headers so we'll have to remove it here (and of course utilize status_code first).
    \   Request Should Be Successful   ${templateResp}   expectedStatusCode=${200}
    \   Remove From Dictionary   ${templateResp}  status_code   headers
    \   ${spaceName} =   Check For Whitespace From String   ${profile['name']}
    \   Run Keyword If   ${spaceName} is ${True}   Fail   msg=Profile name contains whitespace. This is not allowed in CI-FIT naming convention.
    \   ${resp} =   Run Keyword If   '${server_profile_to_bay_map['${profile['name']}']}' == '${null}'   Fusion Api Get Server Hardware
    \   ${shUri} =   Run Keyword If   ${resp} == ${null}   Get Server Hardware URI    ${server_profile_to_bay_map['${profile['name']}']}
    \   ...                    ELSE   Set Variable   ${resp['members'][0]['uri']}
    \   ${serverHW} =   Fusion Api Get Resource    uri=${shUri}
    \   Set To Dictionary    ${profile}   serverHardwareTypeUri=${serverHW['serverHardwareTypeUri']}
    \   Set To Dictionary   ${profile}   serverHardwareUri=${shUri}
    \   ${profile} =   Resolve Profile Template Uri   ${profile}
    \   ${profile} =   Resolve Profile Connections   ${profile}
    \   ${profile} =   Merge Two Dictionaries   ${templateResp}   ${profile}
    \	${resp} =   Fusion Api Create Server Profile		body=${profile}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \       Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
    \       ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Add Rack-mount Server Profiles Using Template From Variable
    [Documentation]   Get template data, update template with rack-mount server profile data variable, create profile.
    [Arguments]   ${profiles}   ${waitTime}=300m   ${interval}=5s   ${validate}=${True}   ${connectionSettingsApi}=${600}   ${parallel}=${True}   ${waitForTask}=${True}   ${throttle}=${Null}
    ${log_message} =   Run Keyword If   '${parallel}' == '${True}'   Set Variable   \n\nAdding rack-mount SERVER PROFILES from template in parallel (status may not reflect right away)
    ...   ELSE   Set Variable   \n\nAdding rack-mount SERVER PROFILES from template...
    Log   ${log_message}   console=${True}
    ${valDict} =   Create Dictionary   status_code=${200}
    ...                                taskState=Completed
    ${respList} =   Create List
    Set Suite Variable   ${forkedErrorFound}   ${False}
    :FOR   ${s}   IN   @{profiles}
    \      ${resp} =    Create SP from SPT for legacy BIOS    ${s['name']}    ${s['serverProfileTemplateUri']}   ${s['serverHardwareUri']}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   Continue For Loop If   ${waitForTask} != ${True}
    \   Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
    \   ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    \       Continue For Loop If   '${throttle}' == '${Null}'
    \       Continue For Loop If   ${parallel} != ${True}
    \       ${respLength} =   Get Length   ${respList}
    \       Continue For Loop If   ${respLength} != ${throttle}
    \       ${respList} =   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}   throttle=${throttle}
    Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Create SP from SPT for legacy BIOS
    [Documentation]             Creates a new server profile named <spname> from SPT named <sptname> and assigns it to
    ...                         server hardware <shuri>.  Legacy BIOS does not allow 'boot' settings in connections,
    ...                         so those are removed
    [Arguments]                 ${spname}    ${sptname}   ${shuri}
    ${spt_uri} =                Resolve Uri By Name   ${sptname}
    ${profile} =                Fusion Api Get Server Profile Template New Profile      ${spt_uri}
    remove from dictionary      ${profile}                     status_code                 headers
    set to dictionary           ${profile}                     name                        ${spname}
    # This is the special logic for Legacy BIOS profiles.  boot setting is not supported.
    ${conns} =       get from dictionary   ${profile['connectionSettings']}    connections
    :FOR    ${c}   IN   @{conns}
    \    remove from dictionary    ${c}   boot
    set to dictionary   ${profile['connectionSettings']}    connections    ${conns}
    ${sh_uri} =    Get Server Hardware URI   ${shuri}
    set to dictionary   ${profile}    serverHardwareUri    ${sh_uri}
    ${resp} =       fusion api create server profile     body=${profile}    param=?force=ignoreServerHealth
    [Return]         ${resp}

###############
# Addresses
###############
Remove Custom Address Range
    [Documentation]    Querys the appliance for all CUSTOM vmac, vwwn, vsn ranges and then removes them
    [Arguments]   ${uri}   ${status_code}=${204}
    Log   \nRemoving custom address range: ${uri}...   console=${True}
    ${pool} =   Fusion Api Get Pool   uri=${uri}
    ${rangeUris} =   Get From Dictionary   ${pool}   rangeUris
    :FOR   ${rangeUri}   IN   @{rangeUris}
    \   ${poolType} =   Get From Dictionary   ${pool}   poolType
    \   ${resp} =   Run Keyword If   '${poolType}' == 'VWWN'   common.Remove VWWN Range   ${rangeUri}
    \   ...   ELSE IF   '${poolType}' == 'VMAC'   common.Remove VMAC Range   ${rangeUri}
    \   ...   ELSE IF   '${poolType}' == 'VSN'   common.Remove VSN Range    ${rangeUri}
    \   ...   ELSE   Log   Invalid or unsupported poolType: ${poolType}.   WARN   console=${True}
    \   Continue For Loop If   ${resp} is ${null}
    \   Run Keyword If   ${resp['status_code']} != ${status_code}   Log   Failed to remove poolType ${poolType}   WARN   console=${True}

Remove VMAC Range
    [Documentation]   Removes a CUSTOM VMAC range
    [Arguments]   ${uri}   ${trangeCategory}=Custom
    ${range} =   Fusion Api Get VMAC Range   uri=${uri}
    ${rangeCategory} =   Get From Dictionary   ${range}   rangeCategory
    ${resp} =   Run Keyword If   '${rangeCategory}'=='${trangeCategory}'   Fusion Api Delete VMAC Range   uri=${uri}
    [Return]   ${resp}

Remove VWWN Range
    [Documentation]   Removes a CUSTOM VWWN range
    [Arguments]   ${uri}   ${trangeCategory}=Custom
    ${range} =   Fusion Api Get VWWN Range   uri=${uri}
    ${rangeCategory} =   Get From Dictionary   ${range}   rangeCategory
    ${resp} =   Run Keyword If   '${rangeCategory}'=='${trangeCategory}'   Fusion Api Delete VWWN Range   uri=${uri}
    [Return]   ${resp}

Remove VSN Range
    [Documentation]   Removes a CUSTOM VSN range
    [Arguments]   ${uri}   ${trangeCategory}=Custom
    ${range} =   Fusion Api Get VSN Range   uri=${uri}
    ${rangeCategory} =   Get From Dictionary   ${range}   rangeCategory
    ${resp} =   Run Keyword If   '${rangeCategory}'=='${trangeCategory}'   Fusion Api Delete VSN Range   uri=${uri}
    [Return]   ${resp}

Enable ALL Generated Address And ID Ranges
    [Documentation]	Enables ALL of the auto-generated Ranges on an appliance
    [Arguments]	  ${uri}   ${status_code}=${200}
    ${pool} =   Fusion API Get Pool   uri=${uri}
    ${rangeUris} =   Get From Dictionary   ${pool}   rangeUris
    :FOR   ${rangeUri}   IN   @{rangeUris}
    \   ${poolType} =   Get From Dictionary   ${pool}   poolType
    \   ${resp} =   Run Keyword If   '${poolType}' == 'VWWN'   common.Enable Generated VMAC Range   ${rangeUri}
    \   ...                ELSE IF   '${poolType}' == 'VMAC'	common.Enable Generated VMAC Range   ${rangeUri}
    \   ...                ELSE IF   '${poolType}' == 'VSN'	common.Enable Generated VSN Range   ${rangeUri}
    \   ...                ELSE   Log   Invalid or unsupported poolType: ${poolType}.   WARN   console=${True}
    \   Run Keyword If   ${resp['status_code']} != ${status_code}   Log   Failed to enable poolType ${poolType}   WARN   console=${True}

Enable Generated VMAC Range
    [Documentation]   Enables the generated VMAC Range on an appliance
    [Arguments]   ${uri}   ${trangeCategory}=Generated
    ${range} = 	 Fusion Api Get VMAC Range   uri=${uri}
    ${rangeCategory} = 	 Get From Dictionary   ${range}   rangeCategory
    ${body} =   Create Dictionary   type=Range   enabled=true
    Run Keyword If   '${rangeCategory}' == '${trangeCategory}'   Log   \nEnabling generated VMAC range: ${uri}...   console=${True}
    ${resp} =   Run Keyword If   '${rangeCategory}' == '${trangeCategory}'   Fusion Api Edit VMAC Range   body=${body}   uri=${uri}
    [Return]   ${resp}

Enable Generated VWWN Range
    [Documentation]   Enables the generated VWWN Range on an appliance
    [Arguments]   ${uri}   ${trangeCategory}=Generated
    ${range} =   Fusion Api Get VWWN Range   uri=${uri}
    ${rangeCategory} = 	 Get From Dictionary   ${range}   rangeCategory
    ${body} =   Create Dictionary   type=Range   enabled=true
    Run Keyword If   '${rangeCategory}' == '${trangeCategory}'   Log   \nEnabling generated VWWN range: ${uri}...   console=${True}
    ${resp} =   Run Keyword If   '${rangeCategory}' == '${trangeCategory}'   Fusion Api Edit VWWN Range   body=${body}   uri=${uri}
    [Return]   ${resp}

Enable Generated VSN Range
    [Documentation]   Enables the generated VSN Range on an appliance
    [Arguments]   ${uri}   ${trangeCategory}=Generated
    ${range} =   Fusion Api Get VSN Range   uri=${uri}
    ${rangeCategory} = 	 Get From Dictionary   ${range}   rangeCategory
    ${body} =   Create Dictionary   type=Range   enabled=true
    Run Keyword If   '${rangeCategory}' == '${trangeCategory}'   Log   \nEnabling generated VSN range: ${uri}...   console=${True}
    ${resp} =   Run Keyword If   '${rangeCategory}' == '${trangeCategory}'   Fusion Api Edit VSN Range   body=${body}   uri=${uri}
    [Return]   ${resp}

Disable ALL Generated ID Ranges
    [Documentation]   Disables ALL of the auto-generated Ranges on an appliance
    [Arguments]   ${uri}   ${status_code}=${200}
    ${pool} =   Fusion API Get Pool   uri=${uri}
    ${rangeUris} =   Get From Dictionary   ${pool}   rangeUris
    :FOR   ${rangeUri}   IN   @{rangeUris}
    \   ${poolType} =   Get From Dictionary   ${pool}   poolType
    \   ${resp} =   Run Keyword If   '${poolType}' == 'VWWN'   Disable Generated VMAC Range   ${rangeUri}
    \   ...                ELSE IF   '${poolType}' == 'VMAC'   Disable Generated VMAC Range   ${rangeUri}
    \   ...                ELSE IF   '${poolType}' == 'VSN'   Disable Generated VSN Range   ${rangeUri}
    \   ...                ELSE   Log   Invalid or unsupported poolType: ${poolType}.   WARN   console=${True}
    \   Run Keyword If   ${resp['status_code']} != ${status_code}   Log   Failed to enable poolType ${poolType}   WARN   console=${True}

Ranges Should Exist In OneView
    [Documentation]   Fail if ranges defined in data file does not exists in OneView.
    [Arguments]   ${address_ranges}   ${ranges_uris}
    ${range_not_found} =   Create Dictionary
    :FOR   ${range}   IN   @{address_ranges}
    \   ${resp} =   Fusion Api Get Resource   ${ranges_uris['${range['category']}']}
    \   Should Not Be Empty   ${resp['rangeUris']}   msg=rangeUris is empty in OneView.
    \   ${range_exists} =   Start And End Address Exist In OneView   ${resp['rangeUris']}    ${range}
    \   Run Keyword If   ${range_exists} is ${False}   Set To Dictionary   ${range_not_found}   ${ranges_uris['${range['category']}']}=Range not found: {startAddress:${range['startAddress']}, endAddress:${range['endAddress']}}
    Run Keyword If   ${range_not_found} != &{EMPTY}   Run Keywords   Log To Console Errors In Dictionary   ${range_not_found}   AND   Fail

Start And End Address Exist In OneView
    [Documentation]   Fail if start and end address defined in data file is not found in OneView.
    ...               Returns boolean.
    [Arguments]   ${rangeUris}   ${range}
    ${rangeFound} =   Set Variable   ${False}
    :FOR   ${r}   IN   @{rangeUris}
    \   ${resp} =   Fusion Api Get Resource   ${r}
    \   ${startAddress} =   Get Variable Value   ${resp['startAddress']}
    \   ${contains} =   Run Keyword And Return Status   Should Contain   ${resp['uri']}   /rest/id-pools/vwwn
    \   ${r_startAddress} =   Run Keyword If   ${contains} is ${True}   Convert To Lowercase   ${range['startAddress']}
    \   ...   ELSE   Convert To Uppercase   ${range['startAddress']}
    \   ${endAddress} =   Get Variable Value   ${resp['endAddress']}
    \   ${r_endAddress} =   Run Keyword If   ${contains} is ${True}   Convert To Lowercase   ${range['endAddress']}
    \   ...   ELSE   Convert To Uppercase   ${range['endAddress']}
    \   ${rangeFound} =   Run Keyword If   '${startAddress}' == '${r_startAddress}' and '${endAddress}' == '${r_endAddress}'   Set Variable   ${True}
    \   ...   ELSE   Set Variable   ${rangeFound}
    [Return]   ${rangeFound}

Create ID Pools IPv4 Subnet
    [Documentation]   Adds IPv4 subnet to an appliance from a variable which contains a list of dicts with the entire payload.
    ...             Data File Example :
    ...             ipv4_subnet = [{"type": "Subnet","networkId": "15.146.152.0","subnetmask": "255.255.248.0","gateway": "15.146.152.1",
    ...                             "dnsServers": ["16.110.135.51", "16.110.135.52"],"domain": "ind.hp.com"}]
    [Arguments]   ${ipv4_subnets}   ${expected_status_code}=${200}
    Log To Console   \nAdding IPv4 subnets
    :FOR   ${subnet}   IN   @{ipv4_subnets}
    \   ${resp} =   Fusion Api Create Ipv4 Subnet   ${subnet}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${expected_status_code}

Get ID Pools IPV4 Subnet Uri By Name
    [Documentation]   Get ID Pools IPV4 Subnet Uri using name as filter.
    [Arguments]   ${subnet_name}
    ${resp} =   Fusion Api Get Ipv4 Subnet
    ${total} =   Convert To Integer   ${resp['total']}
    Should Be True   ${total} > ${0}   msg=Response body total is not as expected: ${total}.
    :FOR   ${subnet}   in   @{resp['members']}
    \   ${subnet_uri} =   Run Keyword If   '${subnet['name']}' == '${subnet_name}'   Get From Dictionary   ${subnet}   uri
    \   Return From Keyword If   '${subnet_uri}' != '${Null}'   ${subnet_uri}
    [Return]   ${Null}

Create ID Pools IPv4 Ranges
    [Documentation]   Adds IPv4 ranges to an appliance from a variable which contains a list of dicts with the entire payload.
    ...               Data File Example :
    ...               ipv4_ranges = [{"type": "Range","name": "IPV4","startAddress": "15.146.152.100","endAddress": "15.146.152.200",
    ...               "subnetUri": "<Pass network id used while registering subnet, without '<>' >"}]
    [Arguments]   ${ipv4_ranges}   ${expected_status_code}=${200}
    Log To Console   \nAdding IPv4 Ranges
    :FOR   ${range}   IN   @{ipv4_ranges}
    \   ${uri} =   Get ID Pools IPv4 Subnet Uri By Name   ${range['subnetUri']}
    \   Set to Dictionary   ${range}   subnetUri=${uri}
    \   ${resp} =   Fusion Api Create IPv4 Range   ${range}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${expected_status_code}

###############
# Users
###############
Add Users from variable
    [Documentation]   Add users to an appliance from a variable which contains a list of dicts with the entire payload
    [Arguments]   ${users}
    Log   \n\nAdding USERS...   console=${True}
    :FOR   ${user}   IN   @{users}
    \   ${permissions} =   Resolve Scope Uri In User Permissions   ${user['permissions']}
    \   Set To Dictionary   ${user}   permissions=${permissions}
    \   ${resp} =   Fusion Api Add User   body=${user}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${200}

Resolve Scope Uri In User Permissions
    [Documentation]   Loops through permissions and resolve scope uri by name if any.
    [Arguments]   ${permissions}
    :FOR   ${p}   IN   @{permissions}
    \   ${scopeUriName} =   Get Variable Value   ${p['scopeUri']}
    \   ${uri} =   Run Keyword If   '${scopeUriName}' == '${null}'   Continue For Loop
    \   ...                  ELSE   Resolve Scope Uri By Name   ${scopeUriName}
    \   Set To Dictionary   ${p}   scopeUri=${uri}
    [Return]   ${permissions}

Remove All Users In OneView
    [Documentation]   Remove all users in OneView.
    ${users} =   Fusion Api Get User
    Log   \n\nRemoving users in OneView...
    :FOR   ${u}   IN   @{users['members']}
    \   ${resp} =   Fusion Api Remove User   uri=${u['uri']}
    \   Run Keyword If   '${u['userName']}' == 'Administrator' or '${u['userName']}' == 'administrator'   Response Should Contain Error Code   ${resp}   INSUFFICIENT_PRIVILEGES
    \   ...    ELSE IF   '${u['userName']}' == 'HardwareSetup'   Response Should Contain Error Code   ${resp}   REQUEST_FORBIDDEN_ERROR
    \   ...    ELSE   Response Should Not Contain Error   ${resp}   ${204}

###############
# Networks
###############
Add Ethernet Networks from variable
    [Documentation]   Add Ethernet networks to an appliance from a variable which contains a list of dicts with the entire payload.
    [Arguments]   ${networks}
    Log   \n\nAdding ETHERNET NETWORKS...   console=${True}
    :FOR   ${net}   IN   @{networks}
    \   ${subnetUri} =   Get Variable Value   ${net['subnetUri']}
    \   ${subnetUri} =   Run Keyword If   '${subnetUri}' != '${Null}'   Get ID Pools IPv4 Subnet Uri By Name   ${net['subnetUri']}
    \   Run Keyword If   '${subnetUri}' != '${Null}'   Set to Dictionary   ${net}   subnetUri=${subnetUri}
    \   ${resp} =   Fusion Api Create Ethernet Network   body=${net}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=240s   interval=5s
    \   Asynchronous Task Should Be Successful   ${task}

Create Ethernet Range
    [Documentation]   Create a range of Ethernet networks based on provided range in variable.
    [Arguments]	${range}
    Set Log Level	TRACE
    Log   \n\nAdding ETHERNET NETWORK RANGES...   console=${True}
    ${body} =   fusion_api_appliance_setup.Copy Dictionary   ${range}
    Remove From Dictionary   ${body}   prefix   suffix   start   end
    :FOR   ${x}   IN RANGE   ${range['start']}   ${range['end']}+1
    \   Set To Dictionary   ${body}   name   ${range['prefix']}${x}${range['suffix']}
    \   Set To Dictionary   ${body}   vlanId   ${x}
    \	${resp} =   Fusion Api Create Ethernet Network   body=${body}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=240s   interval=5s
    \   Asynchronous Task Should Be Successful   ${task}

Add Network Sets from variable
    [Documentation]   Add Network sets to an appliance from a variable which contains a list of dicts with the entire payload.
    [Arguments]   ${networks}
    Log   \n\nAdding NETWORK SETS...   console=${True}
    :FOR   ${net}   IN   @{networks}
    \   ${networkUris} =   Get Ethernet URIs   ${net['networkUris']}
    \   Set to dictionary   ${net}   networkUris   ${networkUris}
    \   ${nativeNetworkUri} =   Run Keyword If   '${net['nativeNetworkUri']}' != 'None'   Get Ethernet URI   ${net['nativeNetworkUri']}
    \   Set To Dictionary   ${net}   nativeNetworkUri   ${nativeNetworkUri}
    \   ${resp} =   Fusion Api Create Network Set   body=${net}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=240s   interval=5s
    \   Asynchronous Task Should Be Successful   ${task}

Create Network Set range
    [Documentation]   Create a range of Network Sets based on provided range
    [Arguments]   ${range}
    Set Log Level   TRACE
    Log   \n\nAdding NETWORK SET RANGES...   console=${True}
    ${body} =   fusion_api_appliance_setup.Copy Dictionary   ${range}
    Remove From Dictionary   ${body}   prefix   suffix   start   end
    ${netlist} =   Create List
    :FOR   ${x}   IN RANGE   ${range['start']}   ${range['end']}+1
    \   Append To List   ${netlist}   ${range['prefix']}${x}${range['suffix']}
    ${networkUris} =   Get Ethernet URIs   ${netlist}
    Set To Dictionary   ${body}   networkUris   ${networkUris}
    ${nativeNetworkUri} =   Run Keyword If   '${range['nativeNetworkUri']}' != 'None'   Get Ethernet URI   ${range['nativeNetworkUri']}
    Set To Dictionary   ${body}   nativeNetworkUri   ${nativeNetworkUri}
    ${resp} =   Fusion Api Create Network Set   body=${body}
    Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=240s   interval=5s
    Asynchronous Task Should Be Successful   ${task}

Add FC Networks from variable
    [Documentation]   Adds FC networks to an appliance from a variable which contains a list of dicts with the entire payload
    [Arguments]   ${networks}
    Log   \n\nAdding FC NETWORKS...   console=${True}
    :FOR   ${net}   IN   @{networks}
    \   ${resp} =   Fusion Api Create FC Network   body=${net}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=240s   interval=5s
    \   Asynchronous Task Should Be Successful   ${task}

Add FCoE Networks from variable
    [Documentation]	Adds FCoE networks to an appliance from a variable which contains a list of dicts with the entire payload
    [Arguments]   ${networks}
    Log   \n\nAdding FCOE NETWORKS...   console=${True}
    :FOR   ${net}   IN   @{networks}
    \   ${resp} =   Fusion Api Create FCoE Network   body=${net}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=240s   interval=5s
    \   Asynchronous Task Should Be Successful   ${task}

Create fcoe range
    [Documentation]   Creates a range of FCoE networks based on range data provided
    [Arguments]   ${range}
    Log   \n\nAdding FCOE NETWORK RANGES...   console=${True}
    :FOR   ${x}   IN RANGE   ${range['start']}   ${range['end']}+1
    \   ${body} =   Create Dictionary   name=${range['prefix']}${x}${range['suffix']}   vlanId=${x}   type=${range['type']}
    \   ${resp} =   Fusion Api Create Fcoe Network   body=${body}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=240s   interval=5s
    \   Asynchronous Task Should Be Successful   ${task}

###############
# Enclosures
###############
Remove All Enclosures
    [Documentation]   Querys the appliance for all Enclosures and then removes them
    [Arguments]   ${remove_timeout}=60m   ${remove_interval}=10s
    Log   \n\nRemoving ENCLOSURES...   console=${True}
    ${encs} =   Fusion Api Get Enclosures
    :FOR   ${enc}   IN   @{encs['members']}
    \   ${resp} =   Fusion Api Remove Enclosure   uri=${enc['uri']}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   ${remove_timeout}    ${remove_interval}
    \   ${val} =   Create Dictionary   taskState=Completed
    \   ${result} =   fusion_api_validation.Validate Response   ${task}   ${val}

###############
# Servers
###############
Add Server Hardware From Variable
    [Documentation]   Adds rack-mount servers from variable for management by the OneView appliance.
    [Arguments]   ${shs}   ${timeout}=300m   ${interval}=0.1s  ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}
    ${respList} =   Create List
    Set Suite Variable   ${forkedErrorFound}   ${False}
    ${valDict} =   Create Dictionary   status_code=${200}
    ...                                taskState=Completed
    ${log_message} =   Run Keyword If   '${parallel}' == '${True}'   Set Variable   \n\nAdding RACK-MOUNT SERVER HARDWARE in parallel (status may not reflect right away)...
    ...   ELSE   Set Variable   \n\nAdding RACK-MOUNT SERVER HARDWARE...
    Log   ${log_message}   console=${True}
    :FOR   ${sh}   IN   @{shs}
    \   ${resp} =   Fusion Api Add Server Hardware   ${sh}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   Continue For Loop If   ${waitForTask} != ${True}
    \   Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
    \   ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${timeout}   ${interval}   ${validate}
    Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${timeout}   ${interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Remove All Server Hardware In OneView
    [Documentation]   Remove all server hardware in OneView.
    [Arguments]   ${timeout}=300m   ${interval}=0.1s  ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}
    ${respList} =   Create List
    Set Suite Variable   ${forkedErrorFound}   ${False}
    ${valDict} =   Create Dictionary   status_code=${200}
    ...                                taskState=Completed
    ${resp} =   Fusion Api Get Server Hardware
    Return From Keyword If   '${resp['count']}' == '${0}'
    Log   Removing All Server Hardware In OneView   console=${True}
    ${log_message} =   Run Keyword If   '${parallel}' == '${True}'   Set Variable   \n\nRemoving All SERVER HARDWARE from OneView in parallel (status may not reflect right away)...
    ...   ELSE   Set Variable   \n\nRemoving All SERVER HARDWARE from OneView...
    Log   ${log_message}   console=${True}
    :FOR   ${sh}   IN   @{resp['members']}
    \   ${resp} =   Fusion Api Delete Server Hardware   name=${sh['name']}
    \   Continue For Loop If   ${waitForTask} != ${True}
    \   Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
    \   ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${timeout}   ${interval}   ${validate}
    Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${timeout}   ${interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Power Off Server Uri
    [Documentation]   Powers off a server for a given URI
    ...               proceedPressAndHold accepts errorCode that will trigger PressAndHold powerControl if found(ie: SERVER_MOMENTARY_PRESS_OFF_TIMEOUT).
    [Arguments]     ${serverUri}   ${wait_task_timeout}=60m   ${wait_task_interval}=2s   ${powerControl}=MomentaryPress   ${proceedPressAndHold}=${Null}
    Log   Powering off server using ${serverUri} using ${powerControl}   console=${True}
    ${body} =   Create Dictionary   powerState=Off
    ...                             powerControl=${powerControl}
    ${resp} =   Fusion Api Edit Server Hardware Power State   body=${body}   uri=${serverUri}
    ${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    ${retval} =   Check Asynchronous Task Response For Error   ${task}   processErrorCode=${proceedPressAndHold}
    Run Keyword If   '${retval}' != '${Null}'   common.Power Off Server Uri   ${serverUri}   wait_task_timeout=${wait_task_timeout}   wait_task_interval=${wait_task_interval}   powerControl=PressAndHold

Power Off All Servers In Parallel
    [Documentation]    Querys the appliance for all servers and then powers them off in parallel.
    ...               proceedPressAndHold accepts errorCode that will trigger PressAndHold powerControl if found(ie: SERVER_MOMENTARY_PRESS_OFF_TIMEOUT).
    [Arguments]   ${waitTime}=300m   ${interval}=5s   ${powerControl}=MomentaryPress   ${proceedPressAndHold}=${Null}
    Log To Console   \n\nPowering off all servers using ${powerControl}...
    ${body} =   Create Dictionary   powerState=Off
    ...                             powerControl=${powerControl}
    ${valDict} =   Create Dictionary   status_code=${200}
    ...                                taskState=Completed
    ${respList} =   Create List
    ${servers} =   Fusion Api Get Server Hardware
    Set Suite Variable   ${forkedErrorFound}   ${False}
    :FOR   ${server}   IN   @{servers['members']}
    \    Continue For Loop If    '${server['powerState']}'!='On'
    \    ${resp} =    Fusion Api Edit Server Hardware Power State    body=${body}    uri=${server['uri']}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \    Append To List   ${respList}   ${resp}
    common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   processErrorCode=${proceedPressAndHold}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Power On All Servers In Parallel
    [Documentation]    Querys the appliance for all servers and then powers them on in parallel.
    [Arguments]   ${waitTime}=300m   ${interval}=5s   ${powerControl}=MomentaryPress
    Log   \n\nPowering On SERVERS in parallel (status may not reflect right away)...   console=${True}
    ${body} =   Create Dictionary   powerState=On
    ...                             powerControl=${powerControl}
    ${valDict} =   Create Dictionary   status_code=${200}
    ...                                taskState=Completed
    ${respList} =   Create List
    ${servers} =   Fusion Api Get Server Hardware
    Set Suite Variable   ${forkedErrorFound}   ${False}
    :FOR   ${server}   IN   @{servers['members']}
    \    Continue For Loop If    '${server['powerState']}'!='Off'
    \    ${resp} =    Fusion Api Edit Server Hardware Power State        body=${body}    uri=${server['uri']}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \    Append To List   ${respList}   ${resp}
    common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Power Off Server Via Ssh
    [Documentation]   Powers off a single server via SSH using the specified command and monitor the powerState transition via the resource and name.
    [Arguments]   ${ipAddr}   ${profileName}   ${poweroffCmd}=poweroff   ${iface}=eth0
    Log To Console   \nPowering off ${ipAddr}...
    ${llAddr} =   Get Lines Matching Regexp   ${ipAddr}   ^fe80:   partial_match=true
    ${Id} =   Run Keyword If   '${llAddr}' == '${EMPTY}'   Open Connection  ${ipAddr}
    ...       ELSE   Open Connection  ${ipAddr}%${iface}
    ${Output} =   Login   ${SERVER_USERNAME}   ${SERVER_PASSWORD}
    ${stdout}   ${stderr}   ${rc} =   Execute Command   ${poweroffCmd}   return_stderr=True   return_rc=True
    SSHLibrary.Close Connection

All Servers Power State Should Reach Off
    [Documentation]   Query OneView server hardware powerState and fail if one did not transition to powerState Off.
    [Arguments]   ${serverUris}
    :FOR   ${serverUri}   IN   @{serverUris}
    \   ${resp} =   Fusion Api Get Server Hardware   uri=${serverUri}
    \   Log To Console   \nChecking ${resp['name']} powerState Off...   no_newline=${True}
    \   Run Keyword If   '${resp['powerState']}' == 'Off'   Log To Console   [Off]
    \   ...       ELSE   Log To Console   [${resp['powerState']}]
    \   Run Keyword If   '${resp['powerState']}' == 'Off'   Remove Values From List   ${serverUris}   ${serverUri}
    Should Be Empty   ${serverUris}   msg=Not all servers transitioned to powerState Off.

Get IP And Power Off Server Via Ssh As Possible
    [Documentation]   Get pingable IP from HA File and power off server via SSH.
    ...               Use ssh if server profile is assigned, otherwise, use api (MomentaryPress/PressAndHold).
    [Arguments]   ${blade}   ${poweroffCmd}=poweroff
    ${resp} =   Run Keyword If   '${blade['state']}' == 'ProfileApplied'   Fusion Api Get Server Profiles   uri=${blade['serverProfileUri']}
    ...                      ELSE   Create Dictionary
    Log To Console   \nSearching for reachable IP Address from HA file...
    ${pingable_ip} =   Run Keyword If   ${resp} != &{EMPTY}   robustness-helper.get_server_reachable_ip   ${HA_FILE}   filterByProfile=${resp['name']}
    ...                   ELSE   Create Dictionary
    ${l} =   Get Length   ${pingable_ip}
    ${name} =   Get Dictionary Keys   ${pingable_ip}
    Run Keyword If   ${l} == 1   Power Off Server Via Ssh   ${pingable_ip['${name[0]}']}   ${resp['name']}
    ...    ELSE IF   ${l} == 0   common.Power Off Server Uri   ${blade['uri']}   proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}
    ...       ELSE   Fail   msg=Unexpected contents in pingable_ip: ${pingable_ip}.

Power Off All Servers Via Ssh In Parallel
    [Documentation]   Powers off all servers in HA_FILE using specified command via SSH.
    [Arguments]   ${poweroffCmd}=poweroff   ${timeout}=180m  ${interval}=10s
    ${reachable_ips} =   robustness-helper.get_server_reachable_ip   ${HA_FILE}
    :FOR   ${k}   IN   @{reachable_ips.keys()}
    \   Power Off Server Via Ssh   ${reachable_ips['${k}']}   ${k}   ${poweroffCmd}
    ${resp} =   Fusion Api Get Server Hardware
    ${serverUris} =   Create List
    :FOR   ${s}   IN   @{resp['members']}
    \   Log To Console   \nChecking ${s['name']} powerState Off...   no_newline=${True}
    \   Run Keyword If   '${s['powerState']}' == 'Off'   Log To Console   [Off]
    \   ...       ELSE   Log To Console   [${s['powerState']}]
    \   Run Keyword If   '${s['powerState']}' != 'Off'   Append To List   ${serverUris}   ${s['uri']}
    Wait Until Keyword Succeeds   ${timeout}   ${interval}   All Servers Power State Should Reach Off   ${serverUris}

###############
# Backup
###############
Update Backup Config
    [Documentation]   Update backup config in OneView.
    [Arguments]   ${remote_backup}   ${wait_timeout}=200s   ${wait_interval}=5s
    ${resp} =   Fusion Api Get Backup   uri=/rest/backups/config
    Set To Dictionary   ${remote_backup}   eTag=${resp['eTag']}
    ${resp} =   Fusion Api Update Backup Config   body=${remote_backup}
    Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_timeout}   interval=${wait_interval}
    Asynchronous Task Should Be Successful   ${task}

###############
# Scopes
###############
Create Scopes
    [Documentation]   Create scopes in OneView.
    [Arguments]   ${scopes}
    Log   \n\nAdding SCOPES...   console=${True}
    :FOR   ${s}   IN   @{scopes}
    \   ${scope} =   Resolve Scope Uris   ${s}
    \   ${resp} =   Fusion Api Create Scope   body=${s}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=200s   interval=5s
    \   Asynchronous Task Should Be Successful   ${task}

Resolve Added Resource Uris
    [Documentation]   Get addedResourceUris attribute from data variable and query OneView for the actual uris.
    [Arguments]   ${scope}
    ${addedResourceUris} =   Get Variable Value   ${scope['addedResourceUris']}   @{EMPTY}
    ${newAddedResourceUris} =   Create List
    :FOR   ${s}   IN   @{addedResourceUris}
    \   @{addedResourceUri} =   Split String   ${s}   :
    \   ${resource} =   Get From List   ${addedResourceUri}   0
    \   ${name} =   Get From List   ${addedResourceUri}   1
    \   ${resp} =   Fusion Api Get Resource   /rest/${resource}?filter="name='${name}'"
    \   ${members} =   Evaluate   ${resp}.get('members', None)
    \   Run Keyword If   ${members} is not ${null}   Response Body Should Have Expected Members   ${resp}   ${1}   ${1}   ${1}
    \   Run Keyword If   ${members} is ${null}   Append To List   ${newAddedResourceUris}   ${resp['uri']}
    \   ...       ELSE   Append To List   ${newAddedResourceUris}   ${resp['members'][0]['uri']}
    [Return]   ${newAddedResourceUris}

Resolve Initial Scope Uris
    [Documentation]   Get initialScopeUris attribute from data variable and query OneView for the actual uris.
    [Arguments]   ${scope}
    ${initialScopeUris} =   Get Variable Value   ${scope['initialScopeUris']}   @{EMPTY}
    ${newInitialScopeUris} =   Create List
    :FOR   ${s}   IN   @{initialScopeUris}
    \   ${uri} =   Resolve Scope Uri By Name   ${s}
    \   Append To List   ${newInitialScopeUris}   ${uri}
    [Return]   ${newInitialScopeUris}

Resolve Scope Uris
    [Documentation]   Make a query to OneView based on the resource name and retrieve the list of uris for added resource and initial scope.
    [Arguments]   ${scope}
    ${addedResourceUris} =   Resolve Added Resource Uris   ${scope}
    ${initialScopeUris} =   Resolve Initial Scope Uris   ${scope}
    Run Keyword If   ${addedResourceUris} != @{EMPTY}   Set To Dictionary   ${scope}   addedResourceUris=${addedResourceUris}
    Run Keyword If   ${initialScopeUris} != @{EMPTY}   Set To Dictionary   ${scope}   initialScopeUris=${initialScopeUris}
    [Return]   ${scope}

Resolve Scope Uri By Name
    [Documentation]   Make a query to OneView for scope uri using the name.
    [Arguments]   ${scopeName}
    ${resp} =   Fusion Api Get Scope
    ${member} =   Filter Response By Attribute   ${resp}   name   ${scopeName}
    Run Keyword If   ${member} is not ${null}   Return From Keyword   ${member['uri']}
    ...       ELSE   Fail   msg=Unable to find uri for scope name ${scopeName}.

Remove All Scopes In OneView
    [Documentation]   Query OneView and remove all scopes.
    [Arguments]   ${waitTimeout}=5m   ${waitInterval}=1s
    Log   \n\nRemoving scopes in OneView...   console=${True}
    ${resp} =   Fusion Api Get Scope
    :FOR   ${s}   IN   @{resp['members']}
    \   ${resp} =   Fusion Api Delete Scope   uri=${s['uri']}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${waitTimeout}   interval=${waitInterval}
    \   Asynchronous Task Should Be Successful   ${task}

###############
# Fabric Manager
###############
Add Fabric Manager
    [Documentation]   Adds Fabric Manager with Certificate to OneView
    [Arguments]   ${fabric_manager}   ${apic_certificate}
    ${name} =   Get Variable Value   ${fabric_manager['name']}
    ${apic_certificate} =   Get Variable Value   ${apic_certificate}
    ${apic_host} =   Set Variable   ${fabric_manager['fabricManagerClusterNodeInfo'][0]['oobMgmtAddr']}
    Add APIC Server Certificate To OneView    ${apic_certificate}   apic_host=${apic_host}
    ${resp} =   Fusion Api Create Fabric Manager   ${fabric_manager}
    Response Should Not Contain Error   ${resp}   ${202}

Add APIC Server Certificate To OneView
    [Documentation]   Adds APIC Server Certificate to OneView
    ...               Define the below dictionary in datafile:
    ...               apic_certificate = {"type": "CertificateInfoV2", "certificateDetails": [{"base64Data": "", "aliasName": "", "type": "CertificateDetailV2"}]}
    ...               Retrieve base64Data from APIC if empty string was provided.
    [Arguments]   ${apic_certificate}   ${apic_host}
    ${apic_certificate} =   Get Variable Value   ${apic_certificate}
    ${apic_host} =   Get Variable Value   ${apic_host}
    ${base64Data} =   Get Variable Value   ${apic_certificate['certificateDetails'][0]['base64Data']}
    ${resp} =   Run Keyword If   "${base64Data}" == ""   Fusion Api Get Remote Certificate   ip=${apic_host}
    ${base64Data} =   Run Keyword If   "${base64Data}" == ""   Get From Dictionary   ${resp['certificateDetails'][0]}   base64Data
    Set To Dictionary   ${apic_certificate['certificateDetails'][0]}   base64Data   ${base64Data}
    ${resp} =   Fusion Api Import Server Certificate   ${apic_certificate}
    Response Should Not Contain Error   ${resp}   ${202}
 
Get Fabric Manager Uri By Name
    [Documentation]   Gets the Fabric Manager URI by name.
    [Arguments]   ${name}
    ${resp} =   Fusion Api Get Fabric Manager   param=?filter="'name'=='${name}'"
    Length Should Be   ${resp['members']}   1   msg=Response body does not contain the expected members length.
    ${Uri} =   Get From Dictionary   ${resp['members'][0]}   uri
    [Return]    ${Uri}

Get Fabric Manager Tenant Uri By Name
    [Documentation]   Get the Tenant URI from OneView by Tenant name.
    [Arguments]   ${fabric_manager_uri}    ${tenant_name}
    ${resp} =   Fusion Api Get Fabric Manager Tenants   ${fabric_manager_uri}
    :FOR   ${member}   IN   @{resp['members']}
    \   Return From Keyword If   '${member['name']}' == '${tenant_name}'   ${member['uri']}
    Fail   msg=Tenant with name ${tenant_name} was not found.

Get All Monitored Tenants From Fabric Manager Name
    [Documentation]   Get all the tenants from a fabric manager name.
    [Arguments]   ${fabric_manager_name}
    ${resp} =   Fusion Api Get Fabric Manager   param=?filter="'name'=='${fabric_manager_name}'"
    Length Should Be   ${resp['members']}   1   msg=Response body does not contain the expected members length. Check that Fabric Manager named "${fabric_manager_name}" contains.
    ${added_tenants} =   Create List
    :FOR   ${tenant}   IN   @{resp['members'][0]['tenants']}
    \    Run Keyword If   '${tenant['monitored']}' == '${True}'   Append To List   ${added_tenants}   ${tenant}
    [Return]   ${added_tenants}

Set Tenant To Monitored State
    [Documentation]   Setting a Tenant Monitored attribute to true.
    [Arguments]   ${fabric_manager}   ${tenant_name}
    ${fabric_manager_uri} =   Get Fabric Manager Uri By Name   ${fabric_manager['name']}
    ${tenant_uri} =   Get Fabric Manager Tenant Uri By Name   ${fabric_manager_uri}   ${tenant_name}
    ${new_tenant} =   Create Dictionary   name=${tenant_name}   uri=${tenant_uri}   type=Tenant   monitored=true
    Append To List   ${fabric_manager['tenants']}   ${new_tenant}
    Set To Dictionary   ${fabric_manager}   uri   ${fabric_manager_uri}
    Set To Dictionary   ${fabric_manager}   userName=${APIC_CREDENTIAL['userName']}   password=${APIC_CREDENTIAL['password']}
    ${resp} =    Fusion Api Edit Fabric Manager    ${fabric_manager}   ${fabric_manager_uri}
    Response Should Not Contain Error   ${resp}   ${202}
 
Add Tenant To Fabric Manager
    [Documentation]  Add Tenant to OneView Fabric Manager.
    [Arguments]   ${fabric_manager}   ${tenant_name}
    ${added_tenants} =   Get All Monitored Tenants From Fabric Manager Name   ${fabric_manager['name']}
    Set To Dictionary   ${fabric_manager}   tenants   ${added_tenants}
    Set Tenant To Monitored State   ${fabric_manager}   ${tenant_name}

Unset Tenant From Monitored State
    [Documentation]   Remove a Tenant from the Monitored list.
    [Arguments]   ${fabric_manager}   ${tenant_name}
    ${filtered_tenants} =   Create List
    :FOR   ${t}   IN   @{fabric_manager['tenants']}
    \   Run Keyword Unless   '${t['name']}' != '${tenant_name}'   Append To List   ${filtered_tenants}   ${t}
    ${fabric_manager_uri} =   Get Fabric Manager Uri By Name   ${fabric_manager['name']}
    Set To Dictionary   ${fabric_manager}   tenants   ${filtered_tenants}
    Set To Dictionary   ${fabric_manager}   uri   ${fabric_manager_uri}
    Set To Dictionary   ${fabric_manager}   userName=${APIC_CREDENTIAL['userName']}   password=${APIC_CREDENTIAL['password']}
    ${resp} =    Fusion Api Edit Fabric Manager    ${fabric_manager}   ${fabric_manager_uri}
    Response Should Not Contain Error   ${resp}   ${202}

Remove Tenant From Fabric Manager By Name
    [Documentation]   Remove Tenant from Fabric Manager as defined in data variable.
    [Arguments]   ${fabric_manager}   ${tenant_name}
    ${added_tenants} =   Get All Monitored Tenants From Fabric Manager Name   ${fabric_manager['name']}
    Set To Dictionary   ${fabric_manager}   tenants   ${added_tenants}
    Unset Tenant From Monitored State   ${fabric_manager}   ${tenant_name}

Remove All Monitored Tenants From Fabric Manager
    [Documentation]   Remove all Tenants from Fabric Manager.
    [Arguments]   ${fabric_manager}
    Log   DEBUG: ${fabric_manager['uri']}
    ${tenants} =   Get All Monitored Tenants From Fabric Manager Name   ${fabric_manager['name']}
    :FOR   ${tenant}   IN   @{tenants}
    \   Remove Tenant From Fabric Manager By Name   ${fabric_manager}   ${tenant['name']}

Delete Fabric Manager By Name
    [Documentation]   Delete Fabric Manager and the APIC Server Certificate in OneView.
    [Arguments]   ${fabric_manager_name}
    ${resp} =   Fusion Api Get Fabric Manager   param=?filter="'name'=='${fabric_manager_name}'"
    Length Should Be   ${resp['members']}   1   msg=Response body does not contain the expected members length. Check that Fabric Manager named "${fabric_manager_name}" exists.
    ${resp} =   Fusion Api Delete Fabric Manager   ${fabric_manager_name}
    Response Should Not Contain Error   ${resp}   ${202}
    Remove APIC Server Certificate In OneView   ${fabric_manager_name}

Remove APIC Server Certificate In OneView
    [Documentation]   Delete the APIC Server Certificate in OneView.
    [Arguments]   ${fabric_manager_name}
    ${resp} =   Fusion Api Get Server Certificate   ${fabric_manager_name}
    Dictionary Should Contain Key   ${resp}   certificateDetails
    ${resp} =   Fusion Api Delete Server Certificate   ${fabric_manager_name}
    Response Should Not Contain Error   ${resp}   ${202}

###############
# Plexxi
###############
Discover Plexxi Fabrics From Variable
    [Documentation]   Discovery Plexxi fabrics in Composable Fabric Manager
    [Arguments]   ${plexxi_fabrics}
    :FOR   ${body}   IN   @{plexxi_fabrics}
    \   ${resp} =   Plexxi Api Discover Fabric   ${body}
    \   Run Keyword If  ${resp['status_code']} is not 200    Fail      status_code:${resp['status_code']}


Add OneView Configuration To Plexxi Connect From Variable
    [Documentation]   Add OneView Configuration to Plexxi Connect Packs
    [Arguments]   ${oneview_config}
    :FOR   ${body}   IN   @{oneview_config}
    \   Run Keyword If   '${APPLIANCE_IP}' != '${Null}'   Set To Dictionary   ${body}   host   ${APPLIANCE_IP}
    \   ${resp} =   Plexxi Api Add OneView Configuration   ${body}
    \   Run Keyword If  ${resp['status_code']} is not 200    Fail      status_code:${resp['status_code']}


Remove OneView Configuration From Variable In Plexxi Connect
    [Documentation]   Remove OneView configuration defined in data file from Plexxi Connect
    [Arguments]   ${oneview_config}
    ${resp} =   Plexxi Api Get OneView Configuration
    ${unable_to_find} =   Create List
    :FOR   ${ov}   IN   @{resp['result']}
    \   Run Keyword If   '${ov['host']}' == '${APPLIANCE_IP}'   Plexxi Api Delete OneView Configuration   ${ov['uuid']}
    \   ...       ELSE   Append To List   ${unable_to_find}   ${ov['host']}
    :FOR   ${f}   IN   @{unable_to_find}
    \   Log To Console   \n\tUnable to find OneView config host to remove: ${f}
    Run Keyword If   ${unable_to_find} != @{EMPTY}   Fail   \tUnable to find one or more OneView config to remove.

Wait Until List Of Switches Are Healthy And Synced
    [Documentation]   Polling for switches health and status to be healthy and synced.
    [Arguments]   ${sw_macs}   ${wait_timeout}=30m   ${wait_interval}=5s
    Wait Until Keyword Succeeds   ${wait_timeout}   ${wait_interval}   Switches Should Be Healthy And Synced   ${sw_macs}

Switches Should Be Healthy And Synced
    [Documentation]   Query CFM and fail if one or more switches is not healthy and sycned.
    [Arguments]   ${sw_macs}   ${wait_timeout}=30m   ${wait_interval}=2s
    ${length} =    Get Length    ${sw_macs}
    ${resp} =   Plexxi Api Get Switches
    Should Be True   '${resp['count']}' >= '${length}'   msg=Response count(${resp['count']}) is not as expected(${length}).
    :FOR   ${s}   IN   @{resp['result']}
    \   ${contains} =   Evaluate   '${s['mac_address']}' in ${sw_macs}
    \   Continue For Loop If   ${contains} == False
    \   Log To Console   Health: ${s['health']}, Status: ${s['status']}
    \   Log To Console   Checking for switch named ${s['name']}...   no_newline=${True}
    \   Run Keyword If   '${s['health']}' == 'HEALTHY' and '${s['status']}' == 'SYNCED'   Log To Console   [OK]
    \   ...       ELSE   Log To Console   [Failed, polling...]
    \   Run Keyword If   '${s['health']}' == 'HEALTHY' and '${s['status']}' == 'SYNCED'   Remove Values From List   ${sw_macs}   ${s['mac_address']}
    Should Be Empty   ${sw_macs}   msg=Not all switches are in HEALTHY and SYNCED: ${sw_macs}

###############
# Fabrics
###############
Get Fabric Uri By Name
    [Documentation]   Get fabric uri by name
    [Arguments]   ${fabric_name}
    ${resp} =   Fusion Api Get Fabric
    ${total} =   Convert To Integer   ${resp['total']}
    Should Be True   ${total} > ${0}   msg=Response body total is not as expected.
    :FOR   ${fabric}   IN   @{resp['members']}
    \   Return From Keyword If   '${fabric['name']}' == '${fabric_name}'   ${fabric['uri']}
    Fail   msg=Unable to find uri for fabric name ${fabric_name}.

Wait Until Fabric Reached State
   [Documentation]   Wait until fabric reached state
   [Arguments]   ${fabric_name}   ${fabric_state}   ${wait_timeout}=12m   ${wait_interval}=5s
   Wait Until Keyword Succeeds   ${wait_timeout}   ${wait_interval}   Fabric Reached State    ${fabric_name}   ${fabric_state}

Fabric Reached State
    [Documentation]   Fabric reached a certain state.
    [Arguments]   ${fabric_name}   ${fabric_state}
    ${resp} =   Fusion Api Get Fabric
    ${total} =   Convert To Integer   ${resp['total']}
    Should Be True   ${total} > ${0}   msg=Response body total is not as expected.
    :FOR   ${fabric}   IN   @{resp['members']}
    \   Run Keyword If   '${fabric['name']}' == '${fabric_name}'   Should Be Equal   ${fabric['state']}   ${fabric_state}

Update Reserved Vlan Id Range
    [Documentation]   Update reserved vlan id range for the fabric.
    [Arguments]   ${reserved_vlan}
    ${fabric} =   Fusion Api Get Fabric
    #TODO: We need to find out if there's a chance we can get more than 1 members in FabricCollection and update this.
    ${resp} =   Fusion Api Update Fabric Reserved Vlan Range   ${reserved_vlan}   ${fabric['members'][0]['uri']}
    Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=200s   interval=5s
    Asynchronous Task Should Be Successful   ${task}
    ${resp} =   Fusion Api Get Fabric Reserved Vlan Range   ${fabric['members'][0]['uri']}
    ${result} =   Check Data   ${reserved_vlan}   ${resp}
    Run Keyword If   ${result} == ${False}   Fail   msg=Fabric Reserved Vlan Id Range did not match to expected values.

Negative Update Reserved Vlan Id Range
    [Documentation]   Attempt update reserved vlan id range for the fabric with expected error code.
    [Arguments]   ${reserved_vlan}
    ${fabric} =   Fusion Api Get Fabric
    #TODO: We need to find out if there's a chance we can get more than 1 members in FabricCollection and update this.
    ${resp} =   Fusion Api Update Fabric Reserved Vlan Range   ${reserved_vlan}   ${fabric['members'][0]['uri']}
    Response Should Contain Error Code   ${resp}   CRM_EDITING_RESERVED_VLAN_RANGE_DISALLOWED_ON_VM

###############
# Switches
###############
Get Switch Uri By Name
    [Documentation]   Get switch uri by name
    [Arguments]   ${switch_name}
    ${resp} =   Fusion Api Get Switch
    ${total} =   Convert To Integer   ${resp['total']}
    Should Be True   ${total} > ${0}   msg=Response body total is not as expected.
    :FOR   ${switch}   IN   @{resp['members']}
    \   Return From Keyword If   '${switch['chassisId']}' == '${switch_name}'   ${switch['uri']}
    Fail   msg=Unable to find uri for switch name ${switch_name}.

Wait Until Switches Reached State
   [Documentation]   Wait until switches reached state
   [Arguments]   ${switch_names}   ${switch_state}   ${wait_timeout}=8m   ${wait_interval}=0.5s
   Wait Until Keyword Succeeds   ${wait_timeout}   ${wait_interval}   Switches Reached State    ${switch_names}   ${switch_state}

Switches Reached State
    [Documentation]   Switches reached a certain state.
    [Arguments]   ${switch_names}   ${switch_state}
    ${resp} =   Fusion Api Get Switch
    ${length} =    Get Length    ${switch_names}
    Should Be True   '${resp['total']}' >= '${length}'   msg=Response body total(${resp['total']}) is not as expected(${length}).
    :FOR   ${switch}   IN   @{resp['members']}
    \   Log To Console   Name: ${switch['name']}, State: ${switch['state']}
    \   Log To Console   Checking for switch named ${switch['name']}...   no_newline=${True}
    \   ${contains} =   Evaluate   '${switch['chassisId']}' in ${switch_names}
    \   Continue For Loop If   ${contains} == False
    \   Run Keyword If   '${switch['state']}' == '${switch_state}'   Log To Console   [OK]
    \   ...       ELSE   Log To Console   [Failed, polling...]\n\n
    \   Run Keyword If   '${switch['state']}' == '${switch_state}'   Remove Values From List   ${switch_names}   ${switch['chassisId']}
    Should Be Empty   ${switch_names}   msg=Not all switches are in OneView or in state ${switch_state} for the following: ${switch_names}

###############
# Logical Switches
###############
Add Logical Switch From Variable For Composable Rack
    [Documentation]   Adds a Logical Switch to an appliance from a variable for composable rack which contains a list of dicts with the entire payload
    [Arguments]   ${ls}   ${timeout}=5m   ${interval}=0.1s
    fusion_api_appliance_setup.Log to console and logfile  	\nAdding LOGICAL SWITCH for Composable Rack
    ${lsguri} =   Get From Dictionary   ${ls['logicalSwitch']}   logicalSwitchGroupUri
    ${lsguri} =   Common URI Lookup by name   ${lsguri}
    Set to dictionary   ${ls['logicalSwitch']}   logicalSwitchGroupUri   ${lsguri}
    ${swuris} =   Create List
    :FOR   ${sw}   IN   @{ls['logicalSwitch']['switchUris']}
    \   ${swuri} =   Get Switch Uri By Name   ${sw}
    \   Append To List   ${swuris}   ${swuri}
    Set to dictionary   ${ls['logicalSwitch']}   switchUris   ${swuris}
    ${resp} =   Fusion Api Create LS   ${ls}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   ${timeout}   ${interval}
    [Return]  ${task}

#############
# Delete specified resource
#############
Remove LIG
    [Documentation]     Specifically removing LIG in OV
	[Arguments]     ${LIG_Name}     ${REMOVE_LIG_TIMEOUT}=60s     ${REMOVE_LIG_INTERVAL}=30s
	${name} =   Split String   ${LIG_Name}   ,
	:FOR   ${lig}   IN   @{name}
	\    ${resp}    Fusion Api Get Lig    param=?filter="'name'=='${lig}'"
	\    Should Be Equal   ${resp['total']}   ${1}   msg=Response body total is not as expected
    \    ${Response}   Fusion Api Delete Lig    uri=${resp['members'][0]['uri']}
	${task} =   fusion_api_appliance_setup.Wait For Task   ${Response}   timeout=${REMOVE_LIG_TIMEOUT}   interval=${REMOVE_LIG_INTERVAL}

Remove Logical Enclosures
	[Documentation]    Removing LE specifically
	[Arguments]    ${LE_Name}    ${REMOVE_LE_TIMEOUT}=20m     ${REMOVE_LE_INTERVAL}=60s
	:FOR   ${le}   IN   @{LE_Name}
    \    ${resp}    Fusion Api Get Logical Enclosure    param=?filter="'name'=='${le}'"
	\    Should Be Equal   ${resp['total']}   ${1}   msg=Response body total is not as expected
    \    ${Response}    Fusion Api Delete Logical Enclosure    uri=${resp['members'][0]['uri']}
	${task} =   fusion_api_appliance_setup.Wait For Task   ${Response}   timeout=${REMOVE_LE_TIMEOUT}   interval=${REMOVE_LE_INTERVAL}

Remove Server Profiles
    [Documentation]    Removing server profile specifically
	[Arguments]    ${Server_Profile_Name}    ${waitTime}=300m   ${interval}=5s  ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}   ${throttle}=${Null}
	${log_message}    Run Keyword If   '${parallel}' == '${True}'    Set Variable    \n\nRemoving SERVER PROFILES in parallel(status may not reflect right away)...
    ...                         ELSE    Set Variable    \n\nRemoving SERVER PROFILES
	Log    ${log_message}    console=${True}
	${valDict} =    Create Dictionary   status_code=${200}
        ...                                 taskState=Completed
    ${respList} =   Create List
	Set Suite Variable   ${forkedErrorFound}   ${False}
	${servers} =   Split String   ${Server_Profile_Name}   ,
	:FOR   ${server_name}   IN   @{servers}
	\    ${resp}    Fusion Api Get Server Profiles    param=?filter="'name'=='${server_name}'"
	\    Should Be Equal   ${resp['total']}   ${1}   msg=Response body total is not as expected.
    \    ${Response}    Fusion Api Delete Server Profile    uri=${resp['members'][0]['uri']}
	\    Request Should Be Successful   ${Response}   expectedStatusCode=${202}
	\    Continue For Loop If   ${waitForTask} != ${True}
	\    Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${Response}
	\    ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${Response}   ${valDict}   ${waitTime}   ${interval}   ${validate}
	\    Continue For Loop If   '${throttle}' == '${Null}'
	\    Continue For Loop If   ${parallel} != ${True}
	\    ${respLength} =   Get Length   ${respList}
	\    Continue For Loop If   ${respLength} != ${throttle}
	\    ${respList} =   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}   throttle=${throttle}
    Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Power Off specified ServerHardware
    [Documentation]    Specifically powerOff the server hardware
	[Arguments]     ${Server_Hardware}   ${waitTime}=300m   ${interval}=5s   ${powerControl}=MomentaryPress   ${proceedPressAndHold}=${Null}   ${parallel}=${True}   ${waitForTask}=${True}   ${throttle}=${Null}   ${validate}=${True}
	Log To Console   \n\nPowering off servers using ${powerControl}...
	${body} =   Create Dictionary   powerState=Off
    ...                             powerControl=${powerControl}
    ${valDict} =   Create Dictionary   status_code=${200}
    ...                                taskState=Completed
	${respList} =   Create List
	Set Suite Variable   ${forkedErrorFound}   ${False}
	${server_HW} =   Split String   ${Server_Hardware}   ;
	:FOR   ${hardware}   IN   @{server_HW}
    \    ${resp}    Fusion Api Get Server Hardware   param=?filter="'name'=='${hardware}'"
	\    Should Be Equal   ${resp['total']}   ${1}   msg=Response body total is not as expected
	\    Continue For Loop If    '${resp['members'][0]['powerState']}'!='On'
	\    ${resp} =    Fusion Api Edit Server Hardware Power State    body=${body}    uri=${resp['members'][0]['uri']}
	\    Request Should Be Successful   ${resp}   expectedStatusCode=${202}
	\    Continue For Loop If   ${waitForTask} != ${True}
	\    Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
    \    ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${waitTime}   ${interval}   ${validate}
	\    Continue For Loop If   '${throttle}' == '${Null}'
	\    Continue For Loop If   ${parallel} != ${True}
	\    ${respLength} =   Get Length   ${respList}
	\    Continue For Loop If   ${respLength} != ${throttle}
	\    ${respList} =   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}   throttle=${throttle}
	Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   processErrorCode=${proceedPressAndHold}   validate=${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error

Unassign server profiles for particular servers
    [Documentation]    Unassign server profiles particular servers
	[Arguments]        ${Unassign_Server_Profiles}
	${profiles} =   Create List
	${profile_unassign} =   Split String   ${Unassign_Server_Profiles}   ,
	:FOR   ${profile}   IN  @{profile_unassign}
    \   ${profile_resp}    Fusion Api Get Server Profiles   param=?filter="'name'=='${profile}'"
	\   Should Be Equal   ${profile_resp['total']}   ${1}   msg=Response body total is not as expected
	\   ${profile_members}   Set Variable   ${profile_resp['members'][0]}
	\   Append To List   ${profiles}   ${profile_members}
	common.Unassign Server Profiles   ${profiles}   timeout=${PROFILE_UNASSIGN_WAIT_TIMEOUT}   interval=${PROFILE_UNASSIGN_WAIT_INTERVAL}   forceProfileApply=${FORCE_PROFILE_APPLY}   throttle=${PROFILE_THROTTLE}

##########
# ICM power On/Off
##########
Interconnect Power request
    [Documentation]   Send an interconnect power request to OneView
    [Arguments]     ${uri}    ${power}   ${power_wait_timeout}=60m   ${power_wait_interval}=2s
    ${data} =   Create Dictionary   op=replace
    ...                             path=/powerState
    ...                             value=${power}
    ${body} =   Create List     ${data}
    Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    Powering ${power}: ${uri}
    ${resp} =   Fusion Api Patch Interconnect   body=${body}    uri=${uri}
    ${task} =   fusion_api_appliance_setup.Wait for Task   ${resp}  timeout=${power_wait_timeout}   interval=${power_wait_interval}
    ${valDict} =    Create Dictionary       status_code=${200}
    ...                                 taskState=Completed
    fusion_api_validation.Validate Response       ${task}   ${valDict}
    Log   \t Waiting for ${uri} to reach powerState:${power}   console=${True}
    Wait Until Keyword Succeeds     ${power_wait_timeout}   ${power_wait_interval}      Should Match Interconnect Power State    ${uri}    ${power}

Should Match Interconnect Power State
    [Documentation]   Current interconnect power state should match to the value of ${state} argument
    [Arguments]	    ${uri}  ${state}
    ${resp} =   fusion api get resource     ${uri}
    Log   \t ${uri}: ${resp['powerState']}   console=${True}
    Should Match Regexp 	${resp['powerState']}    ${state}
    [Return]	${resp}

###############
# Logical Interconnects
###############
stackingDomainMAC Should Exist In Nitro LI
    [Documentation]   Fail if stackingDomainMAC does not exists in an LI for Nitro
    ${resp} =   Fusion Api Get LI
    Should Not Be Empty   ${resp['members']}   msg=There's no logical interconnect in OneView.
    :FOR   ${li}   IN   @{resp['members']}
    \   ${nitroLI} =   LI Is Nitro   ${li['interconnectMap']['interconnectMapEntries']}
    \   Run Keyword If   ${nitroLI} is ${True}   Should Not Be Equal   ${li['stackingDomainMAC']}   ${Null}   msg=stackingDomainMAC is ${Null} for Nitro LI: ${li['name']}.

LI Is Nitro
    [Documentation]   Returns True boolean if it is a Nitro LI
    [Arguments]   ${interconnectMapEntries}
    :FOR   ${i}   IN   @{interconnectMapEntries}
    \   ${resp} =   Fusion Api Get Interconnect   uri=${i['interconnectUri']}
    \   Should Not Be Empty   ${resp}   msg=Response body is empty for GET ${i['interconnectUri']}.
    \   Return From Keyword If   '${resp['model']}' == '${NITRO_MODEL_NAME}'   ${True}
    [Return]   ${False}
