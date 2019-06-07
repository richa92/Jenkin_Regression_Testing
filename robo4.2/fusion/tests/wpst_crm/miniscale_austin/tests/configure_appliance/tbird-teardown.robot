*** Settings ***
Documentation       Removes resources from an appliance, returning it to a clean state. You can pass tags to pybot with -i <tag> to limit processing
...                 TAGS:   MINIMAL, POWER_OFF_SERVERS, PROFILES, ENCLOSURES, ENCLOSURE_GROUPS, LIGS, ETHERNET, FC, FCOE, NS, USERS, UNASSIGN_HARDWARE, LES, TENANTS, FABRIC_MANAGER
...                 MINIMAL -  will POWER OFF SERVERS, unassign SERVER_PROFILES, and remove LOGICAL ENCLOSURES.  These steps are the minimum you need to remove enclosures cleanly.
...                 POWER OFF SERVERS powers off all servers, waiting for each power off task to complete
...                 UNASSIGN_HARDWARE unassign server profiles from server hardware
...                 PROFILES powers off servers, unassign profiles, removes all server profiles, remove all custom address ranges, enable generated address ranges
...                 SERVER_PROFILES powers off servers, unassign profiles, then removes all server profiles.
...                 REMOVE_PROFILES deletes server profiles, remove all custom address ranges, then enable generated address ranges.
...                 LES removes all logical enclosures, waiting for each task to complete
...                 ENCLOSURE GROUPS removes all enclosure groups
...                 LIGS removes all LIGs, waiting for each task to complete
...                 ETHERNET removes all Ethernet networks, waiting for each task to complete
...                 FC removes all FibreChannel networks, waiting for each task to complete
...                 FCOE removes all FCoE networks, waiting for each task to complete
...                 NETWORK SETS removes all network sets, waiting for each task to complete
...                 USERS removes all users
...                 SPTS removes all server profile templates
...                 TENANTS removes all tenants from fabric manager
...                 FABRIC_MANAGERS removes all fabric managers from OneView
...                 Example workflow: tbird teardown removing everything and putting enclosure and interconnects in monitored state
...                                   pybot -V C:\4.10\fusion\tests\wpst_crm\miniscale_austin\tests\configure_appliance\miniscale_austin_data_variables.py -v X-API-Version:800 -v tbirdEnv:True -v APPLIANCE_IP:15.186.9.3 -d C:\4.10\fusion\tests\wpst_crm\miniscale_austin\tests\configure_appliance\Logs\setup\ -L TRACE -v tbird-teardown.robot
Note : Follow the following steps if you want to integrate with performance listener.
       Edit your scripts Performance tag to match with fusion_conditions.py
       Path for fusion.conditions.py : Tools/performance/fusion_conditions.py
       Add the following to your pybot command:
--listener FusionLibrary.performance.listener -v PERFORMANCE_INDEX_NAME:miniscale_austin -v LOG_ACTIVITY:True -v LOG_ACTIVITY_TO_CIDEBUG:True
...                                   Optional arguments:
...                                   To use power off server via ssh, use -v HA_FILE:/path/to/your/ha_file.conf
...                                   To proceed with PressAndHold when MomentaryPress fails with this errorCode, use -vPROCEED_WITH_PRESS_AND_HOLD:SERVER_MOMENTARY_PRESS_OFF_TIMEOUT
...                                   Default profile throttle: 3, to override it use -vPROFILE_THROTTLE:[None|<number of profiles at a time>]

Suite Setup                     Get appliance IP and Login

Resource                        ../../../../resource/fusion_api_all_resource_files.txt
Resource        ../../../ci_fit/tests/configure_appliance/resource/common.robot
Library                         Collections
Library                         ../../../ci_fit/tests/robustness/resources/robustness-helper.py
Variables                       ../../../ci_fit/tests/robustness/resources/data_variables.py

*** Variables ***
${X-API-VERSION}                   ${null}
${POWER_OFF_MODE}                  api
${PressAndHold}                    PressAndHold
${PROFILE_THROTTLE}                None
${PROFILE_UNASSIGN_WAIT_TIMEOUT}   860m
${PROFILE_UNASSIGN_WAIT_INTERVAL}  3s
${FORCE_PROFILE_APPLY}             all
${tbirdEnv}                        ${True}
${decyrpt_file}     ${CURDIR}/support_dump/Decrypted/ci_dfrm_decrypted_supportdump.sdmp
${dump_file_path}   ${CURDIR}/support_dump
${OV_SUPPORT_DUMP_WAIT_INTERVAL}    15m
${WAIT_FOR_TASK_TIMEOUT}        30m
${WAIT_FOR_TASK_INTERVAL}       5s

*** Test Cases ***
Power off ALL Servers
    [Documentation]   Poweroff each server, wait for task to complete and verify that powerState is Off.
    [Tags]   POWER_OFF_SERVERS   PROFILES   SERVER_PROFILES   MINIMAL
    Run Keyword If   '${poweroff_mode}' == 'api'   Power Off All Servers In Parallel   powerControl=${PressAndHold}    proceedPressAndHold=${Null}
    ...    ELSE IF   '${poweroff_mode}' == 'ssh'   Power Off All Servers Via Ssh In Parallel

Remove Tenants From Fabric Manager
    [Tags]   TENANTS
    [Documentation]    Remove Tenants From Fabric Manager
    ${fabric_manager} =   Fusion Api Get Fabric Manager
    :FOR   ${fm}   IN   @{fabric_manager['members']}
    \   Remove All Monitored Tenants From Fabric Manager   ${fm}

Remove Fabric Manager
    [Tags]   FABRIC_MANAGERS
    [Documentation]    Remove Fabric Manager
    ${fabric_manager} =   Fusion Api Get Fabric Manager
    :FOR   ${fm}   IN   @{fabric_manager['members']}
    \   Delete Fabric Manager By Name   ${fm['name']}

Unassign All Server Profiles
    [Documentation]   Query OneView for list of profiles then unassign server profiles from server hardware.
    [Tags]   PROFILES   SERVER_PROFILES   UNASSIGN_HARDWARE   MINIMAL
    ${resp} =   Fusion Api Get Server Profiles
    ${profiles} =   Create List
    ${profile_list} =   Get From Dictionary   ${resp}   members
    common.Unassign Server Profiles   ${profile_list}   timeout=${PROFILE_UNASSIGN_WAIT_TIMEOUT}   interval=${PROFILE_UNASSIGN_WAIT_INTERVAL}   forceProfileApply=${FORCE_PROFILE_APPLY}   throttle=${PROFILE_THROTTLE}

Remove All Server Profiles
    [Documentation]   Remove all server profiles in parallel and fail on error.
    [Tags]   PROFILES   SERVER_PROFILES   REMOVE_PROFILES
    Remove All Server Profiles In Parallel

Remove All Server Profile Templates
    [Tags]    TEMPLATE     SERVER_PROFILE_TEMPLATES  MINIMAL  SPTS
    [Documentation]   Remove All Server Profile Templates
    Remove All Server Profile Templates In Parallel

Remove All CUSTOM Address Ranges
    [Documentation]   Remove custom address ranges and warn on status code mismatch.
    [Tags]    RANGES    CUSTOM  PROFILES   REMOVE_PROFILES
    ${pools} =  Create List     /rest/id-pools/vmac /rest/id-pools/vwwn /rest/id-pools/vsn
    :FOR   ${pool}   IN   @{pools}
    \   Remove Custom Address Range   ${pool}

Enable GENERATED Address Ranges
    [Documentation]   Enable generated address and identifier ranges.
    [Tags]    RANGES    GENERATED   PROFILES   REMOVE_PROFILES
    ${pools} =  Create List     /rest/id-pools/vmac /rest/id-pools/vwwn /rest/id-pools/vsn
    :FOR   ${pool}   IN   @{pools}
    \   ${resp} =   Enable ALL Generated Address And ID Ranges   ${pool}

Remove ALL Logical Enclosures
    [Documentation]   Remove logical enclosures and fail on error.
    [Tags]   LES   MINIMAL
    Remove All Logical Enclosures

Remove ALL Enclosure Groups
    [Documentation]  Get all enclosure groups in OneView and remove them failing on error.
    [Tags]    ENCLOSURE_GROUPS   EGS
    ${egs} =   Fusion Api Get Enclosure Groups
    ${REMOVE_EG_TIMEOUT} =   Get Variable Value   ${REMOVE_EG_TIMEOUT}
    ${REMOVE_EG_INTERVAL} =   Get Variable Value   ${REMOVE_EG_INTERVAL}
    ${REMOVE_EG_TIMEOUT} =   Run Keyword If   ${REMOVE_EG_TIMEOUT} is ${null}   Set Variable   240s
    ${REMOVE_EG_INTERVAL} =   Run Keyword If   ${REMOVE_EG_INTERVAL} is ${null}   Set Variable   2s
    Log   \n\nRemoving all enclosure groups...   console=${True}
    :FOR   ${eg}   IN   @{egs['members']}
    \   ${resp} =   Fusion Api Delete Enclosure Group   uri=${eg['uri']}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${204}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   ${REMOVE_EG_TIMEOUT}   ${REMOVE_EG_INTERVAL}   status_code=${204}
    \   Asynchronous Task Should Be Successful   ${task}

Remove ALL LIGs
    [Documentation]   Remove All Ligs and fail on error using fusion_api_appliance_teardown KW.
    [Tags]   LIGS
    Remove ALL LIGs

Remove ALL Ethernet Networks
    [Documentation]   Remove all ethernet networks except those network still being used by profile(s). Warn user for used network not being removed.
    [Tags]   ETHERNET
    Log   \n\nRemoving all unused ethernet networks...   console=${True}
    ${nets} =   Fusion Api Get Ethernet Networks
    ${REMOVE_NET_TIMEOUT} =   Get Variable Value   ${REMOVE_NET_TIMEOUT}
    ${REMOVE_NET_INTERVAL} =   Get Variable Value   ${REMOVE_NET_INTERVAL}
    ${REMOVE_NET_TIMEOUT} =   Run Keyword If   ${REMOVE_NET_TIMEOUT} is ${null}   Set Variable   240s
    ${REMOVE_NET_INTERVAL} =   Run Keyword If   ${REMOVE_NET_INTERVAL} is ${null}   Set Variable   2s
    :FOR   ${net}   IN   @{nets['members']}
    \   ${associatedProfiles} =   Fusion Api Get Resource   ${net['uri']}/associatedProfiles
    \   ${resp} =   Run Keyword If   ${associatedProfiles['_content']} == @{EMPTY}   Fusion Api Delete Ethernet Network   uri=${net['uri']}
    \   ...                   ELSE   Log   Will not delete ethernet network '${net['name']}' because it is associated to profile: \n${associatedProfiles['_content']}.   WARN   console=${True}
    \   ${task} =   Run Keyword If   ${associatedProfiles['_content']} == @{EMPTY}   fusion_api_appliance_setup.Wait For Task   ${resp}   ${REMOVE_NET_TIMEOUT}   ${REMOVE_NET_INTERVAL}
    \   ...                   ELSE   Continue For Loop

Remove ALL FC Networks
    [Documentation]   Remove all FC networks except those network still being used by profile(s). Warn user for used network not being removed.
    [Tags]    FC
    Log   \n\nRemoving all unused FC networks...   console=${True}
    ${nets} =   Fusion Api Get FC Networks
    ${REMOVE_FC_TIMEOUT} =   Get Variable Value   ${REMOVE_FC_TIMEOUT}
    ${REMOVE_FC_INTERVAL} =   Get Variable Value   ${REMOVE_FC_INTERVAL}
    ${REMOVE_FC_TIMEOUT} =   Run Keyword If   ${REMOVE_FC_TIMEOUT} is ${null}   Set Variable   240s
    ${REMOVE_FC_INTERVAL} =   Run Keyword If   ${REMOVE_FC_INTERVAL} is ${null}   Set Variable   2s
    :FOR   ${net}   IN   @{nets['members']}
    \   ${associatedProfiles} =   Fusion Api Get Resource   ${net['uri']}/associatedProfiles
    \   ${resp} =   Run Keyword If   ${associatedProfiles['_content']} == @{EMPTY}   Fusion Api Delete FC Network   uri=${net['uri']}
    \   ...                   ELSE   Log   Will not delete FC network '${net['name']}' because it is associated to profile: \n${associatedProfiles['_content']}.   WARN   console=${True}
    \   ${task} =   Run Keyword If   ${associatedProfiles['_content']} == @{EMPTY}   fusion_api_appliance_setup.Wait For Task   ${resp}   ${REMOVE_FC_TIMEOUT}   ${REMOVE_FC_INTERVAL}
    \   ...                   ELSE   Continue For Loop

Remove ALL FCoE Networks
    [Documentation]   Remove all FCoE networks except those network still being used by profile(s). Warn user for used network not being removed.
    [Tags]    FCOE
    Log   \n\nRemoving all unused FCoE networks...   console=${True}
    ${nets} =   Fusion Api Get FCoE Networks
    ${REMOVE_FCOE_TIMEOUT} =   Get Variable Value   ${REMOVE_FCOE_TIMEOUT}
    ${REMOVE_FCOE_INTERVAL} =   Get Variable Value   ${REMOVE_FCOE_INTERVAL}
    ${REMOVE_FCOE_TIMEOUT} =   Run Keyword If   ${REMOVE_FCOE_TIMEOUT} is ${null}   Set Variable   240s
    ${REMOVE_FCOE_INTERVAL} =   Run Keyword If   ${REMOVE_FCOE_INTERVAL} is ${null}   Set Variable   2s
    :FOR   ${net}   IN   @{nets['members']}
    \   ${used} =   Check Network In Profiles   ${net['uri']}   networkUri
    \   ${resp} =   Run Keyword If   ${used} is ${False}  Fusion Api Delete FCoE Network   uri=${net['uri']}
    \   ...                   ELSE   Log   Will not delete FCoE network '${net['name']}' because it is associated to profile(s).   WARN   console=${True}
    \   ${task} =   Run Keyword If   ${used} is ${False}   fusion_api_appliance_setup.Wait For Task   ${resp}   ${REMOVE_FCOE_TIMEOUT}   ${REMOVE_FCOE_INTERVAL}
    \   ...                   ELSE   Continue For Loop

Remove ALL Network Sets
    [Documentation]   Remove all network sets except those network sets still being used by profile(s). Warn user for used network set(s) not being removed.
    [Tags]    NS
    Log   \n\nRemoving all unused network sets...   console=${True}
    ${nets} =   Fusion Api Get Network Set
    ${REMOVE_NS_TIMEOUT} =   Get Variable Value   ${REMOVE_NS_TIMEOUT}
    ${REMOVE_NS_INTERVAL} =   Get Variable Value   ${REMOVE_NS_INTERVAL}
    ${REMOVE_NS_TIMEOUT} =   Run Keyword If   ${REMOVE_NS_TIMEOUT} is ${null}   Set Variable   240s
    ${REMOVE_NS_INTERVAL} =   Run Keyword If   ${REMOVE_NS_INTERVAL} is ${null}   Set Variable   2s
    :FOR   ${net}   IN   @{nets['members']}
    \   ${used} =   Check Network In Profiles   ${net['uri']}   networkUri
    \   ${resp} =   Run Keyword If   ${used} is ${False}   Fusion Api Delete Network Set   uri=${net['uri']}
    \   ...                   ELSE   Log   Will not delete network set '${net['name']}' because it is associated to profile(s).   WARN   console=${True}
    \   ${task} =   Run Keyword If   ${used} is ${False}   fusion_api_appliance_setup.Wait For Task   ${resp}   ${REMOVE_NS_TIMEOUT}   ${REMOVE_NS_INTERVAL}
    \   ...                   ELSE   Continue For Loop

Remove ALL Users
    [Documentation]   Remove all users in OneView.
    [Tags]    USERS
    Remove All Users In OneView

Remove All Scopes
    [Documentation]   Remove all scopes in OneView.
    [Tags]   SCOPES
    Remove All Scopes In OneView

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