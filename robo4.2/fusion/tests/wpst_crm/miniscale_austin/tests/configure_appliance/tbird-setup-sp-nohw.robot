*** Settings ***
Documentation       Configures an appliance with resources found in supplied data file. Pass in specific tags with pybot -i <tag(s)> to limit processing
...  TAGS:          [FTS, CONFIGURE], RENAME_ENCLOSURES,ETHERNET,BULK_ETHERNET_NETWORK, NS, NS_RANGES, FC,LIGS, LICENSES, ENCLOSURES,
...                 ENCLOSURE_GROUPS, LES, RANGES, POWER_OFF_SERVERS, PROFILES, SERVER_PROFILES, SERVER_PROFILE_TEMPLATES, SERVER_PROFILES_TEMPLATE, SPST, SET_ENV, SPTS, SERVER_PROFILES_NO_HW, SPSNOHW
...  CONFIGURE:     Run all tags except HWSETUP
...      MINIMAL:       Add logical enclosures then assign server profiles to server hardware.
...      SERVER_PROFILES: Add server profiles then assign profiles to server hardware.
...      SUPPORT_DUMP:Appliance(OV) support_dump and LE support_dump will be downloaded under supportdump folder in the current directory,
...                     Example workflow: Don't do FTS instead go straight to configuring your tbird based on the data variable you have
...                                       pybot -V C:\4.10\fusion\tests\wpst_crm\miniscale_austin\tests\configure_appliance\miniscale_austin_data_variables.py -v X-API-Version:800 -v tbirdEnv:True -v APPLIANCE_IP:15.186.9.3 -d C:\4.10\fusion\tests\wpst_crm\miniscale_austin\tests\configure_appliance\Logs\setup\ -L TRACE -v tbird-setup-sp-nohw.robot
Note : Follow the following steps if you want to integrate with performance listener.
       Edit your scripts Performance tag to match with fusion_conditions.py
       Path for fusion.conditions.py : Tools/performance/fusion_conditions.py
       Add the following to your pybot command:
--listener FusionLibrary.performance.listener -v PERFORMANCE_INDEX_NAME:miniscale_austin -v LOG_ACTIVITY:True -v LOG_ACTIVITY_TO_CIDEBUG:True

...                                       Optional arguments:
...                                       Default profile throttle: None, to override it use -vPROFILE_THROTTLE:[None|<number of profiles at a time>]

Resource         ../../../../resource/fusion_api_all_resource_files.txt
Resource        ../../../ci_fit/tests/configure_appliance/resource/common.robot
Library         Collections

Suite Setup     Get appliance IP and Login

*** Variables ***
${X-API-VERSION}         ${null}
${PROFILE_THROTTLE}              None
${PROFILE_ASSIGN_WAIT_TIMEOUT}   860m
${PROFILE_ASSIGN_WAIT_INTERVAL}  3s
${FORCE_PROFILE_APPLY}           all
${tbirdEnv}                      ${True}
${PressAndHold}                    PressAndHold
${file}             ${CURDIR}/support_dump/ci_dfrm_supportdump.sdmp
${decyrpt_file}     ${CURDIR}/support_dump/Decrypted/ci_dfrm_decrypted_supportdump.sdmp
${dump_file_path}   ${CURDIR}/support_dump
${LE_SUPPORT_DUMP_SLEEP}         30m
${OV_SUPPORT_DUMP_WAIT_INTERVAL}    15m
${WAIT_FOR_TASK_TIMEOUT}        30m
${WAIT_FOR_TASK_INTERVAL}       5s


***Test cases***
Rename Enclosures
    [Documentation]   Rename enclosure based on enc_names variable defined in data variable file. This will fail on error.
    [Tags]   CONFIGURE   RENAME_ENCLOSURES
    ${enc_names} =   Get Variable Value   ${enc_names}
    Run Keyword If   ${enc_names} is not ${null}   Rename Enclosures From Variable   ${enc_names}
    ...       ELSE   Log   enc_names not defined. Skipping enclosure rename...   WARN   console=${True}


Add Ethernet Networks
    [Documentation]   Add ethernet networks from variable file.
    [Tags]   CONFIGURE   ETHERNET
    ${ethernet_networks} =   Get Variable Value   ${ethernet_networks}
    Run Keyword If   ${ethernet_networks} is not ${null}   common.Add Ethernet Networks from variable   ${ethernet_networks}

Add Ethernet Networks In Bulk
    [Documentation]   Bulk create ethernet networks from data variable file.
    [Tags]   CONFIGURE   ETHERNET_BULK
    ${bulk_ethernet_network} =   Get Variable Value   ${bulk_ethernet_network}
    ${resp} =   Run Keyword If   ${bulk_ethernet_network} is not ${null}   Fusion Api Create Ethernet Bulk Networks   ${bulk_ethernet_network}
    Pass Execution If   ${resp} is ${null}   Skipping create ethernet bulk networks due to bulk_ethernet_network being NoneType.
    Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=60m   interval=5s
    Asynchronous Task Should Be Successful   ${task}   checkAssociatedResourceUri=${False}

Add Network Sets
    [Documentation]   Add network sets from data variable file.
    [Tags]    CONFIGURE   NS
    ${network_sets} =   Get Variable Value  ${network_sets}
    Run Keyword If   ${network_sets} is ${null}    Fail   msg=network_sets variable is ${null}. Please check your data variable file.
    common.Add Network Sets from variable   ${network_sets}

Add FC Networks
    [Documentation]   Add Fibre Channel networks from data variable.
    [Tags]   CONFIGURE   FC
    ${fc_networks} =   Get Variable Value   ${fc_networks}
    Run Keyword If   ${fc_networks} is not ${null}   common.Add FC Networks from variable   ${fc_networks}

Add LIGS
    [Tags]    CONFIGURE   LIGS
    [Documentation]    Add Logical Interconnect from group
    ${ligs} =   Get Variable Value  ${ligs}
    Run Keyword If  ${ligs} is ${null}   Fail   msg=ligs variable is ${null}. Please check your data variable file.
        ${l} =   Get Length   ${ligs}
    :FOR   ${x}   IN RANGE   0   ${l}
    \   ${task} =  Add LIG from variable   ${ligs[${x}]}
        \   Asynchronous Task Should Be Successful   ${task}

Add Enclosure Groups
    [Tags]    CONFIGURE   ENCLOSURE_GROUPS  EGS
    [Documentation]    Add Enclosure group
    ${enc_groups} = Get Variable Value  ${enc_groups}
    Run Keyword If  ${enc_groups} is ${null}   Fail   msg=enc_groups variable is ${null}. Please check your data variable file.
        ${l} =   Get Length   ${enc_groups}
    :FOR   ${x}   IN RANGE   0   ${l}
    \   ${resp} =   Add Enclosure Group from variable   ${enc_groups[${x}]}
    \   Request Should Be Successful   ${resp}

Add Logical Enclosures
    [Tags]    CONFIGURE   MINIMAL   LOGICAL_ENCLOSURES    LES
    [Documentation]    Add Logical Enclosure
    ${les} =    Get Variable Value  ${les}
    Run Keyword If   ${les} is ${null}    Fail   msg=les variable is ${null}. Please check your data variable file.
    ${l} =   Get Length   ${les}
    :FOR   ${x}   IN RANGE   0   ${l}
    \   ${task} =   Add Logical Enclosure from variable   ${les[${x}]}
    \   Asynchronous Task Should Be Successful   ${task}

Power Off Servers
    [Documentation]   Poweroff servers.
    [Tags]   CONFIGURE   POWER_OFF_SERVERS
    Power Off All Servers In Parallel    powerControl=${PressAndHold}    proceedPressAndHold=${Null}

Add Server Profiles No Hardware Assigned
    [Documentation]   Create server profiles from variable without assigning to server hardware.
    [Tags]   CONFIGURE   PROFILES   SERVER_PROFILES   SERVER_PROFILES_NO_HW   SPSNOHW
    Set Log Level    Trace
    ${server_profiles} =   Get Variable Value   ${server_profiles_nohw}
    Run Keyword If   ${server_profiles} is not ${null}   Add Unassigned Server Profiles   ${server_profiles}   ${server_profile_to_bay_map}

Assign Server Hardware To Profile
    [Tags]  CONFIGURE   MINIMAL   PROFILES   SERVER_PROFILES   ASSIGN_HARDWARE
    server_profiles-condition-CIFIT_5MECL10
    [Documentation]    Assign Server Hardware To Profile
    ${server_profiles} =   Get Variable Value   ${server_profiles_nohw}
    Log   \n\nAssigning Server Hardware to Profiles   console=${True}
    Run Keyword If  ${server_profiles} is not ${null}    common.Assign Server Hardware To Existing Profiles From Variable   ${server_profiles}   ${server_profile_to_bay_map}   timeout=${PROFILE_ASSIGN_WAIT_TIMEOUT}   interval=${PROFILE_ASSIGN_WAIT_INTERVAL}   waitForTask=${True}   forceProfileApply=${FORCE_PROFILE_APPLY}   throttle=${PROFILE_THROTTLE}

Power On All Servers
    [Documentation]   Power up server by hitting momentary press
    [Tags]   POWER_ON_SERVERS
    ${POWER_ON_SERIALLY} =   Get Variable Value   ${POWER_ON_SERIALLY}
    Run Keyword If   '${POWER_ON_SERIALLY}' == '${null}'   Power On All Servers In Parallel
    ...       ELSE   Power ON ALL Servers

Create support dump for LE
    [Documentation]   creates support dump for LE
    [Tags]    LE_DUMP
    Create Directory   ${dump_file_path}
    ${LE_Resp} =   Fusion Api Get Logical Enclosure
    ${LE_id} =   Get from dictionary   ${LE_Resp['members'][0]}   uri
    ${LE_id} =   Split String From Right   ${LE_id}    /   1
    Log   \n Le id is : ${LE_id[-1]}   console=${True}
    ${resp}   Fusion Api Get Logical Enclosure Support Dump   ${LE_SUPPORTDUMP_PAYLOAD}   ${LE_id[-1]}
    ${task_resp} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${WAIT_FOR_TASK_TIMEOUT}    interval=${WAIT_FOR_TASK_INTERVAL}
    Empty Directory   ${dump_file_path}
    ${supportDumpUri} =   Get From Dictionary   ${task_resp['associatedResource']}   resourceUri
    Log   \n Downloading LE support dump...   console=${True}
    ${resp} =   Fusion Api Download Support Dump   uri=${supportDumpUri}   localfile=${file}
    Run Keyword If  '${resp['status_code']}' != '200'   Fail ELSE  Log   \n downloading support dump
    Log   \n LE suport dump is downloading...please wait for ${LE_SUPPORT_DUMP_SLEEP} to complete
    sleep    ${LE_SUPPORT_DUMP_SLEEP}

Create OV support dump
    [Documentation]   creates support dump for OV
    [Tags]   OV_DUMP
    ${dump_file_path} =   Catenate   SEPARATOR=/   ${dump_file_path}   Decrypted
    ${decryptor_path} =   Set Variable      #Making the path as null since encryption not required
    Create Directory   ${dump_file_path}
    Empty Directory   ${dump_file_path}
    Log   \n Creating OV support dump  console=${True}
    ${resp}   Fusion Api Create Support Dump   ${SUPPORT_DUMP}
    Run Keyword If  '${resp['status_code']}' != '200'   Fail ELSE  Log  \nSuccessfully created support dump
    ${uri} =   Get From Dictionary   ${resp}   uri
    Log   \n Downloading OV support dump...   console=${True}
    ${resp} =   Fusion Api Download Support Dump   uri=${uri}   localfile=${decyrpt_file}
    Run Keyword If  '${resp['status_code']}' != '200'   Fail ELSE  Log   \n downloading support dump
    Log   \n OV suport dump is downloading... please wait for ${OV_SUPPORT_DUMP_WAIT_INTERVAL} to complete
    sleep   ${OV_SUPPORT_DUMP_WAIT_INTERVAL}



*** Keywords ***
# -----------------------------------------------------------------------------
#   Tbird Hardware Setup
# -----------------------------------------------------------------------------
Invoke Hardware Setup
    [Documentation]  SSH to the Tbird appliance and invoke hardware setup via REST, only on Tbird platform
    ...              Example:
    ...                Invoke Hardware Setup
    ...                Invoke Hardware Setup  timeout=60  interval=2
    ...                Invoke Hardware Setup  api=300 timeout=60  interval=5
    ...                Data Varables Required:
    ...                ${X-API-VERSION}              300              # X-API-VERSION
    ...                ${FUSION_IP}                  ${APPLIANCE_IP}  # Fusion Appliance IP
    ...                ${FUSION_SSH_USERNAME}        root             # Fusion SSH Username
    ...                ${FUSION_SSH_PASSWORD}        hponeview        # Fusion SSH Password
    ...                ${FUSION_PROMPT}              \#               # Fusion Appliance Prompt
    ...
    [Arguments]  ${api}=${X-API-VERSION}  ${timeout}=60  ${interval}=5
    Log   \n\n[Invoking Hardware Setup]   console=${True}
    Login to Fusion via SSH
    Log   \nX-API-Version: ${api}   console=${True}
    ${output} =   Execute SSH Command     curl -k -X POST -H "X-API-Version:${api}" https://localhost/rest/appliance/tech-setup
    ${resp} =   Get Task By Param   param=?filter='name'='Discover hardware'&sort=created:descending&count=1
    Log   \nDiscovering Hardware...  console=${True}
    ${valDict} =   Create Dictionary   taskState=Completed
    Set Suite Variable   ${forkedErrorFound}   ${False}
    common.Wait For Forked Tasks   ${resp['members']}   ${valDict}   ${timeout}   interval=${interval}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=Not all forked tasks state finished with Completed.

Get Task By Param
        [Documentation]    Get task by param
        ...    Examples:
        ...    Get Task By Param param=?filter='name'=='Discover hardware'&sort=created:descending&count=1
        ...    Get Task By Param param=?filter="'name'='Add' AND associatedResource.resourceName='${name}'"&sort=created:descending&count=1
        [Arguments]    ${param}
        ${resp}=    Fusion Api Get Task    param=${param}
        Log   ${resp}   TRACE   console=${True}
        ${status} =    Run keyword and return status    Dictionary should contain key    ${resp}    'errorCode'
        Return from keyword if    ${status}==${True}    ${resp}
        ${count} =    Get From Dictionary    ${resp}    count
        Return from keyword if    ${count}==0    ${resp}
        [Return]    ${resp}

####### Modify Server Profile Test
Modify Server Profile
    [Documentation]   Edit server profile based on a given request body.
    [Arguments]    ${SP}   ${forceProfileApply}=false
    ${param} =   Run Keyword If   '${forceProfileApply}' != 'false'   Set Variable   ?force="${forceProfileApply}"
    ...                    ELSE   Set Variable   ${EMPTY}
    Log Dictionary    ${SP}
    ${Response} =    Fusion API Edit Server Profile    ${SP}    ${SP['uri']}   param=${param}
    Should Be Equal as Strings   ${Response['status_code']}   202   msg=Failed to initiate Edit SP.
    ${Retry Interval}    Convert To Number     60
    ${Retries}           Convert To Integer    15
    ${Response} =   Fusion API Wait For Task To Complete   ${Response['uri']}   sleep_time=${Retry Interval}   retries=${Retries}
    ${Errors} =   Get From Dictionary   ${Response}   taskErrors
    ${Errors} =   Get Length   ${Errors}
    Run Keyword If   ${Errors} != 0
    ...    Log    Errors encountered while creating Server Profile.   level=WARN
    [Return]    ${Response}

Rename Enclosures From Variable
    [Documentation]   Rename enclosures defined in a dictionary of old:new names.
    [Arguments]   ${enc_names}
    ${body} =   Create List
    ${headers} =   Create Dictionary   If-Match=*   Content-Type=application/json   X-Api-Version=${X-API-VERSION}
    :FOR   ${key}   IN   @{enc_names.keys()}
    \   ${resp} =   Fusion Api Get Enclosures   param=?filter="name='${key}'"
    \   Continue For Loop If   ${resp['members']} == @{EMPTY}
    \   ${request} =   Create Dictionary   op=replace   path=/name   value=${enc_names['${key}']}
    \   Append To List   ${body}   ${request}
    \   ${resp} =   Fusion Api Patch Enclosure   ${body}   ${resp['members'][0]['uri']}   headers=${headers}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=200s   interval=5s
    \   Asynchronous Task Should Be Successful   ${task}
    \   ${body} =   Create List
