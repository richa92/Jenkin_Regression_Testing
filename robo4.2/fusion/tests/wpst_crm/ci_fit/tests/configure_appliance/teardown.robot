*** Settings ***
Documentation		Removes resources from an appliance, returning it to a clean state. You can pass tags to pybot with -i <tag> to limit processing
...		            TAGS:   MINIMAL, POWER_OFF_SERVERS, PROFILES, SERVER_PROFILES, ENCLOSURES, ENCLOSURE_GROUPS, LIGS, ETHERNET, FC, FCOE, NETWORK_SETS, USERS, UNASSIGN_HARDWARE, FABRIC_MANAGER, TENANTS
...                 MINIMAL -  will POWER OFF SERVERS, unassign PROFILES, and remove ENCLOSURES.  These steps are the minimum you need to remove enclosures cleanly.
...                 POWER OFF SERVERS powers off all servers, waiting for each power off task to complete
...                 UNASSIGN_HARDWARE unassign server profiles from server hardware
...                 PROFILES powers off servers, unassign profiles, removes all server profiles, remove all custom address ranges, enable generated address ranges
...                 SERVER_PROFILES powers off all servers, unassign profiles from server hardware, then delete server profiles.
...                 REMOVE_PROFILES deletes server profiles, remove all custom address ranges, then enable generated address ranges.
...                 ENCLOSURES removes all enclosures, waiting for each task to complete
...                 ENCLOSURE GROUPS removes all enclosure groups
...                 LIGS removes all LIGs, waiting for each task to complete
...                 ETHERNET removes all Ethernet networks, waiting for each task to complete
...                 FC removes all FibreChannel networks, waiting for each task to complete
...                 FCOE removes all FCoE networks, waiting for each task to complete
...                 NS removes all network sets, waiting for each task to complete
...                 USERS removes all users
...                 TENANTS removes all Tenants from Fabric Managers
...                 FABRIC_MANAGER removes all fabric managers
...                 Example:
...                         pybot -d /tmp/logs/ci-fit-est/teardown -V /root/ci-fit/config_files/I12-EST-static-DVF-FIT14_OV400.py -L TRACE teardown.robot
...                         Optional arguments:
...                         To use power off server via ssh, use -v HA_FILE:/path/to/your/ha_file.conf
...                         To proceed with PressAndHold when MomentaryPress fails with this errorCode, use -vPROCEED_WITH_PRESS_AND_HOLD:SERVER_MOMENTARY_PRESS_OFF_TIMEOUT
...                         Default profile throttle: None, to override it use -vPROFILE_THROTTLE:[<number of profiles at a time>]

Suite Setup   		Get appliance IP and Login

Resource		        ../../../../resource/fusion_api_all_resource_files.txt
Resource		        resource/common.robot
Library			        Collections
Library                         ../robustness/resources/robustness-helper.py
Variables                       ../robustness/resources/data_variables.py

*** Variables ***
${X-API-VERSION}	           ${null}
${POWER_OFF_MODE}                  api
${PROCEED_WITH_PRESS_AND_HOLD}     None
${tbirdEnv}                        ${False}
${PROFILE_THROTTLE}                ${Null}
${PROFILE_UNASSIGN_WAIT_TIMEOUT}   860m
${PROFILE_UNASSIGN_WAIT_INTERVAL}  3s
${FORCE_PROFILE_APPLY}             all
${REMOVE_ENC_TIMEOUT}              60m
${REMOVE_ENC_INTERVAL}             10s

*** Test Cases ***
Power off ALL Servers
    [Documentation]   Poweroff each server, wait for task to complete and verify that powerState is Off.
    [Tags]    POWER_OFF_SERVERS     PROFILES    SERVER_PROFILES     MINIMAL
    Run Keyword If   '${POWER_OFF_MODE}' == 'api'   Power Off All Servers In Parallel   proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}
    ...    ELSE IF   '${POWER_OFF_MODE}' == 'ssh'   Power Off All Servers Via Ssh In Parallel

Remove Tenants From Fabric Manager
    [Tags]   TENANTS
    ${fabric_manager} =   Fusion Api Get Fabric Manager 
    :FOR   ${fm}   IN   @{fabric_manager['members']}
    \   Remove All Tenants From Fabric Manager   ${fm}
    
Remove Fabric Manager
    [Tags]   FABRIC_MANAGER
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
    [Tags]    PROFILES     SERVER_PROFILES   REMOVE_PROFILES
    Remove All Server Profiles In Parallel

Remove All Server Profile Templates
    [Tags]    TEMPLATE     SERVER_PROFILE_TEMPLATES  SPTS
    Remove All Server Profile Templates In Parallel

Remove All CUSTOM Address Ranges
    [Documentation]   Remove custom address ranges and warn on status code mismatch.
    [Tags]   RANGES   CUSTOM   PROFILES   REMOVE_PROFILES
    ${pools} =   Create List   /rest/id-pools/vmac   /rest/id-pools/vwwn   /rest/id-pools/vsn
    :FOR   ${pool}   IN   @{pools}
    \   Remove Custom Address Range   ${pool}

Enable GENERATED Address Ranges
    [Documentation]   Enable generated address and identifier ranges.
    [Tags]    RANGES    GENERATED   PROFILES   REMOVE_PROFILES
    ${pools} =   Create List   /rest/id-pools/vmac   /rest/id-pools/vwwn   /rest/id-pools/vsn
    :FOR   ${pool}   IN   @{pools}
    \   ${resp} =   Enable ALL Generated Address And ID Ranges   ${pool}

Remove ALL Enclosures
    [Tags]    ENCLOSURES    MINIMAL
    common.Remove All Enclosures   remove_timeout=${REMOVE_ENC_TIMEOUT}   remove_interval=${REMOVE_ENC_INTERVAL}

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
    [Tags]    LIGS
    Remove ALL LIGs

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

Remove ALL Ethernet Networks
    [Documentation]   Remove all ethernet networks except those network still being used by profile(s). Warn user for used network not being removed.
    [Tags]    ETHERNET
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

Remove ALL Users
    [Documentation]   Remove all users in OneView.
    [Tags]    USERS
    Remove All Users In OneView

Remove All Scopes
    [Documentation]   Remove all scopes in OneView.
    [Tags]   SCOPES
    Remove All Scopes In OneView
