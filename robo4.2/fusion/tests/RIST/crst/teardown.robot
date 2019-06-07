*** Settings ***
Documentation		Removes resources from an appliance, returning it to a clean state. You can pass tags to pybot with -i <tag> to limit processing
...                         pybot -d /tmp/logs/crst/teardown -V /root/ci-fit/config_files/cr_dev_ov420.py -L TRACE teardown.robot
...                         Optional arguments:
...                         To use power off server via ssh, use -v HA_FILE:/path/to/your/ha_file.conf
...                         To proceed with PressAndHold when MomentaryPress fails with this errorCode, use -vPROCEED_WITH_PRESS_AND_HOLD:SERVER_MOMENTARY_PRESS_OFF_TIMEOUT
...                         Default profile throttle: None, to override it use -vPROFILE_THROTTLE:[None|<number of profiles at a time>]

Suite Setup   		Get appliance IP and Login   appIPAttr=app1Ipv4Addr

Resource   ../../resource/fusion_api_all_resource_files.txt
Resource   ../../wpst_crm/ci_fit/tests/configure_appliance/resource/common.robot
Library	   Collections
Library    ../../wpst_crm/ci_fit/tests/robustness/resources/robustness-helper.py
Variables  ../../wpst_crm/ci_fit/tests/robustness/resources/data_variables.py

*** Variables ***
${X-API-VERSION}	           ${null}
${POWER_OFF_MODE}                  api
${PROCEED_WITH_PRESS_AND_HOLD}     None
${tbirdEnv}                        ${False}
${PROFILE_THROTTLE}                ${Null}
${PROFILE_UNASSIGN_WAIT_TIMEOUT}   860m
${PROFILE_UNASSIGN_WAIT_INTERVAL}  3s
${FORCE_PROFILE_APPLY}             all
${ONEVIEW_INTEGRATION_SLEEP}       6m
${POWER_CONTROL}                   MomentaryPress

*** Test Cases ***
Power off ALL Servers
    [Documentation]   Poweroff each server, wait for task to complete and verify that powerState is Off.
    [Tags]    POWER_OFF_SERVERS     PROFILES    SERVER_PROFILES     MINIMAL
    Run Keyword If   '${poweroff_mode}' == 'api'   Power Off All Servers In Parallel   proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}  powerControl=${POWER_CONTROL}
    ...    ELSE IF   '${poweroff_mode}' == 'ssh'   Power Off All Servers Via Ssh In Parallel

Remove all Hypervisor Cluster Profiles
    [Documentation]   Removes all Hypervisor Cluster Profiles
    [Tags]    HYPER_CLUSTER_PROFILES     MINIMAL
    ${resp} =    fusion api get hypervisor cluster profile
    :FOR   ${hp}   IN   @{resp['members']}
    \    Log   ${hp['uri']}

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
    Remove All Server Profiles In Parallel   interval=0.5s

Remove All Server Profile Templates
    [Tags]    TEMPLATE     SERVER_PROFILE_TEMPLATES  SPTS
    Remove All Server Profile Templates In Parallel   interval=0.5s

Remove All Server Hardware
    [Documentation]   Remove all server hardware in parallel from OneView.
    [Tags]   MINIMAL   SERVER_HARDWARE   SH
    Remove All Server Hardware In OneView

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

Remove All Logical Switch
    [Documentation]   Removes all logical switches in OneView.
    [Tags]   MINIMAL   LSS
    ${resp} =   Fusion Api Get LS
    :FOR   ${lss}   IN   @{resp['members']}
    \   ${resp} =   Fusion Api Delete LS   uri=${lss['uri']}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   interval=0.1s
    \   Asynchronous Task Should Be Successful   ${task}

Remove All Logical Switch Groups
    [Documentation]   Remove all logical switch groups in OneView.
    [Tags]   MINIMAL   LSGS
    ${resp} =   Fusion Api Get LSG
    :FOR   ${lsg}   IN   @{resp['members']}
    \   ${resp} =   Fusion Api Delete LSG   name=${lsg['name']}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   interval=0.1s
    \   Asynchronous Task Should Be Successful   ${task}

# workaround for remove switches
# Remove Switches
#     [Documentation]   Remove switches from data file in OneView
#     [Tags]   MINIMAL   ONEVIEW_SWITCHES
#     ${switches} =   Get Variable Value   ${switch_names}
#     :FOR   ${switch}   IN   @{switches}
#     \   ${switch_uri} =   Get Switch Uri By Name   ${switch}
#     \   ${resp} =   Fusion Api Remove Switch   uri=${switch_uri}
#     \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=200s   interval=1s
#     \   Asynchronous Task Should Be Successful   ${task}

# Plexxi stuff starts...
Get Plexxi Connect Authentication Token
    [Documentation]   Login to Plexxi Connect to get authentication token
    [Tags]   MINIMAL   PLEXXI_TEARDOWN   PLEXXI_LOGIN   PLEXXI_CONTROL_CONFIG   PLEXXI_ONEVIEW_CONFIG
    Plexxi Api Login   ${plexxi_connect_host}   ${plexxi_connect_user}   ${plexxi_connect_password}

Remove OneView Configuration In Plexxi Connect
    [Documentation]   Remove OneView Configuration defined in data variable file from Plexxi Connect.
    [Tags]   MINIMAL   PLEXXI_TEARDOWN   PLEXXI_ONEVIEW_CONFIG
    ${oneview_config} =   Get Variable Value   ${oneview_config}
    Run Keyword If   ${oneview_config} is not ${Null}   Remove OneView Configuration From Variable In Plexxi Connect   ${oneview_config}
    Sleep And Log Reason To Console   ${ONEVIEW_INTEGRATION_SLEEP}
# Plexxi stuff ends...

Remove Fabrics
    [Documentation]   Remove fabrics from data file in OneView
    [Tags]   MINIMAL   ONEVIEW_FABRICS
    ${fabrics} =   Get Variable Value   ${plexxi_fabrics}
    :FOR   ${fabrics_body}   IN   @{fabrics}
    \   ${resp} =   Fusion Api Delete Fabric   ${fabrics_body['name']}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=200s   interval=1s
    \   Asynchronous Task Should Be Successful   ${task}

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

*** Keywords ***

