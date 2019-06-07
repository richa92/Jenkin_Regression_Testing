*** Settings ***
Documentation		Removes resources from an appliance, returning it to a clean state. You can pass tags to pybot with -i <tag> to limit processing
...		            TAGS:   MINIMAL, POWER_OFF_SERVERS, PROFILES, ENCLOSURES, ENCLOSURE_GROUPS, LIGS, ETHERNET, FC, FCOE, NS, USERS, UNASSIGN_HARDWARE, LES, TENANTS, FABRIC_MANAGER, QuickMinimal, REPO
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
...                 QuickMinimal performs ICM potash power On/Off and performs LE force delete
...                 REPO removes external repository from OneView
...                 Example workflow: tbird teardown removing everything and putting enclosure and interconnects in monitored state
...                                   pybot -d /tmp/logs/eagle62-dev/tbird-teardown -V /root/ci-fit/config_files/eagle62_basic_data-devt.py -L TRACE tbird-teardown.robot
...                                   Optional arguments:
...                                   To use power off server via ssh, use -vPOWER_OFF_MODE:ssh -v HA_FILE:/path/to/your/ha_file.conf
...                                   To proceed with PressAndHold when MomentaryPress fails with this errorCode, use -vPROCEED_WITH_PRESS_AND_HOLD:SERVER_MOMENTARY_PRESS_OFF_TIMEOUT
...                                   To remove external repository, use -v REPOSITORY_NAME:name of repository
...                                   Default profile throttle: None, to override it use -vPROFILE_THROTTLE:[<number of profiles at a time>]
...                                   To power off the particular server profiles it use -v Server_Hardware:[None|<name of the server hardware>] (if multiple name of server hardware is required to be separated by ;)
...                                   To unassign the particular server profiles it use -v Unassign_Server_Profiles:[None|<name of the server profiles>](if multiple name of server profiles is required to be separated by ,)
...                                   To remove the particular server profiles it use -v Server_Profile_Name:[None|<name of the server profiles>] (if multiple name of server profiles is required to be separated by ,)
...                                   To remove the particular LE it use -v LE_Name:[None|<name of the le>]
...                                   To remove the particular LIG it use -v LIG_Name:[None|<name of the lig>](if multiple name of lig is required to be separated by ,)
...                                   To override the default POTASH_POWER_TIMEOUT, use -vPOTASH_POWER_TIMEOUT:<value in RG format like 90m>
...                                   To override the default power control POWER_OFF_MODE:api, use -vPOWER_CONTROL:PressAndHold
...                                   Default REPOSITORY_NAME: None,to override it use -v REPOSITORY_NAME:<name of external repository to be delete>
...                                   To test for Nitro (if not specified it will try to find what you have in OneView), use -vHAFNIUM_MODEL:'Virtual Connect SE 100Gb F32 Module for Synergy'

Suite Setup                     Get appliance IP and Login

Resource                        ../../../../resource/fusion_api_all_resource_files.txt
Resource	       	        resource/common.robot
Library                         Collections
Library                         ../robustness/resources/robustness-helper.py
Variables                       ../robustness/resources/data_variables.py

*** Variables ***
${X-API-VERSION}                   ${null}
${POWER_OFF_MODE}                  api
${POWER_CONTROL}                   MomentaryPress
${PROCEED_WITH_PRESS_AND_HOLD}     None
${PROFILE_THROTTLE}                ${Null}
${PROFILE_UNASSIGN_WAIT_TIMEOUT}   860m
${PROFILE_UNASSIGN_WAIT_INTERVAL}  3s
${FORCE_PROFILE_APPLY}             all
${tbirdEnv}                        ${True}
${REMOVE_LE_TIMEOUT}               20m
${REMOVE_LE_INTERVAL}              30s
${REMOVE_LIG_TIMEOUT}              60s
${REMOVE_LIG_INTERVAL}             30s
${REMOVE_SP_TIMEOUT}               2800s
${REMOVE_SP_INTERVAL}              30s
${Server_Hardware}                 None
${LE_Name}                         None
${Server_Profile_Name}             None
${LIG_Name}                        None
${Unassign_Server_Profiles}        None
${POTASH_POWER_TIMEOUT}            60m
${POTASH_POWER_INTERVAL}           30s
${REPOSITORY_NAME}                 None
${REMOVE_REPOSITORY_TIMEOUT}       2m
${REMOVE_REPOSITORY_INTERVAL}      2s
${HAFNIUM_MODEL}                   ${Null}

*** Test Cases ***
Power off ALL Servers
    [Documentation]   Poweroff each server, wait for task to complete and verify that powerState is Off.
    [Tags]   POWER_OFF_SERVERS   PROFILES   SERVER_PROFILES   MINIMAL   QuickMinimal
    Run Keyword If   "${Server_Hardware}" != 'None'    Power Off specified ServerHardware    ${Server_Hardware}
    ...       ELSE IF   '${POWER_OFF_MODE}' == 'api'   Power Off All Servers In Parallel   powerControl=${POWER_CONTROL}   proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}
    ...       ELSE IF   '${POWER_OFF_MODE}' == 'ssh'   Power Off All Servers Via Ssh In Parallel

Power Off All Hafnium Interconnects
    [Documentation]    Power off all hafium interconnect modules
    [Tags]    QuickMinimal
	Set Suite Variable   ${ICM_MODEL}   ${HAFNIUM_MODEL}
    ${icms} =     Get IC
    ${icm_len} =    Get Length  ${icms}
    :FOR    ${x}    IN RANGE    0   ${icm_len}
    \   ${ic} =     Get From List   ${icms}    ${x}
    \   ${uri} =    Get From IC     ${ic}   uri
    \   Interconnect Power request    ${uri}   Off   power_wait_timeout=${POTASH_POWER_TIMEOUT}   power_wait_interval=${POTASH_POWER_INTERVAL}
    \   fusion_api_appliance_setup.Log to console and logfile   \t Waiting for ${uri} to reach state:Maintenance
    \   Wait Until Keyword Succeeds     ${POTASH_POWER_TIMEOUT}   ${POTASH_POWER_INTERVAL}      IC reached state    ${ic['uri']}    Maintenance

Remove Tenants From Fabric Manager
    [Tags]   TENANTS
    ${fabric_manager} =   Fusion Api Get Fabric Manager
    :FOR   ${fm}   IN   @{fabric_manager['members']}
    \   Remove All Monitored Tenants From Fabric Manager   ${fm}

Remove Fabric Manager
    [Tags]   FABRIC_MANAGERS
    ${fabric_manager} =   Fusion Api Get Fabric Manager
    :FOR   ${fm}   IN   @{fabric_manager['members']}
    \   Delete Fabric Manager By Name   ${fm['name']}

Unassign All Server Profiles
    [Documentation]   Query OneView for list of profiles then unassign server profiles from server hardware.
    [Tags]   PROFILES   SERVER_PROFILES   UNASSIGN_HARDWARE   MINIMAL   Performance   server_profiles-condition-CIFIT_5MECL10
    ${resp} =   Fusion Api Get Server Profiles
    ${profiles} =   Create List
    ${profile_list} =   Get From Dictionary   ${resp}   members
    Run Keyword If    "${Unassign_Server_Profiles}" != 'None'     Unassign server profiles for particular servers   ${Unassign_Server_Profiles}
    \    ...     ELSE    common.Unassign Server Profiles   ${profile_list}   timeout=${PROFILE_UNASSIGN_WAIT_TIMEOUT}   interval=${PROFILE_UNASSIGN_WAIT_INTERVAL}   forceProfileApply=${FORCE_PROFILE_APPLY}   throttle=${PROFILE_THROTTLE}

Remove All Server Profiles
    [Documentation]   Remove all server profiles in parallel and fail on error.
    [Tags]   PROFILES   SERVER_PROFILES   REMOVE_PROFILES   Performance   server_profiles-condition-CIFIT_5MECL10   QuickMinimal
	${Quick_Minimal_force}    is_tag_present
    Run Keyword If   "${Server_Profile_Name}" != 'None'    Remove Server Profiles    ${Server_Profile_Name}
    ...     ELSE    Remove All Server Profiles In Parallel    force=${Quick_Minimal_force}

Remove All Server Profile Templates
    [Tags]    TEMPLATE     SERVER_PROFILE_TEMPLATES  MINIMAL  SPTS
    Remove All Server Profile Templates In Parallel

Remove All CUSTOM Address Ranges
    [Documentation]   Remove custom address ranges and warn on status code mismatch.
    [Tags]    RANGES    CUSTOM  PROFILES   REMOVE_PROFILES   QuickMinimal
    ${pools} =  Create List		/rest/id-pools/vmac	/rest/id-pools/vwwn	/rest/id-pools/vsn
    :FOR   ${pool}   IN   @{pools}
    \   Remove Custom Address Range   ${pool}

Enable GENERATED Address Ranges
    [Documentation]   Enable generated address and identifier ranges.
    [Tags]    RANGES    GENERATED   PROFILES   REMOVE_PROFILES
	${pools} =  Create List		/rest/id-pools/vmac	/rest/id-pools/vwwn	/rest/id-pools/vsn
    :FOR   ${pool}   IN   @{pools}
    \   ${resp} =   Enable ALL Generated Address And ID Ranges   ${pool}

Remove ALL Logical Enclosures
    [Documentation]   Remove logical enclosures and fail on error.
    [Tags]   LES   MINIMAL   Performance  logical_enclosures-condition-CIFIT_5MECL10   QuickMinimal
	${Quick_Minimal_force}    is_tag_present
    Run Keyword If   "${LE_Name}" != 'None'    Remove Logical Enclosures    ${LE_Name}
    ...     ELSE    Remove All Logical Enclosures   timeout=${REMOVE_LE_TIMEOUT}   interval=${REMOVE_LE_INTERVAL}   force=${Quick_Minimal_force}

Power On All Hafnium Interconnects
    [Documentation]    Power on all hafnium interconnect modules
    [Tags]    QuickMinimal
    ${icms} =        Get IC
    ${icm_len} =    Get Length  ${icms}
    :FOR    ${x}    IN RANGE    0   ${icm_len}
    \   ${ic} =     Get From List   ${icms}    ${x}
    \   ${uri} =    Get From IC     ${ic}   uri
    \   Interconnect Power request    ${uri}   On   power_wait_timeout=${POTASH_POWER_TIMEOUT}   power_wait_interval=${POTASH_POWER_INTERVAL}
    \   fusion_api_appliance_setup.Log to console and logfile   \t Waiting for ${uri} to reach state:Monitored
    \   Wait Until Keyword Succeeds     ${POTASH_POWER_TIMEOUT}   ${POTASH_POWER_INTERVAL}      IC reached state    ${ic['uri']}    Monitored

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
    Run Keyword If   "${LIG_Name}" != 'None'    Remove LIG    ${LIG_Name}
    ...     ELSE    Remove ALL LIGs

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

Remove ALL Users
    [Documentation]   Remove all users in OneView.
    [Tags]    USERS
    Remove All Users In OneView

Remove All Scopes
    [Documentation]   Remove all scopes in OneView.
    [Tags]   SCOPES
    Remove All Scopes In OneView

Remove Repository
    [Documentation]    Remove repository from the appliance.
    [Tags]    REPO
	Pass Execution If   "${REPOSITORY_NAME}"=="None"    Did not find any repository name.
	${resp}     Fusion Api Get Repository    param=?filter="name='${REPOSITORY_NAME}'"
	Length Should Be   ${resp['members']}   1   msg=${REPOSITORY_NAME} query in OneView returned unexpected members.
    ${uri}    Get From Dictionary    ${resp['members'][0]}    uri
	${resp}    Fusion Api Delete Repository    ${uri}
	${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   ${REMOVE_REPOSITORY_TIMEOUT}   ${REMOVE_REPOSITORY_INTERVAL}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task}
