*** Settings ***
Documentation        Create and remove networks and network sets
...                  This script will use the data variable file from the setup script to create and remove the networks and network sets
...                  To run this script, there should be no networks or network sets configured in the appliance
...                  Example:
...                          time pybot -d /tmp/logs/Server-Profiles-Add-Remove/ -LTRACE -v APPLIANCE_IP:15.186.9.62 -V /root/ci-fit/config_files/eagle62_basic_data-devt.py Networks-Add-Remove

Variables           ../../resources/data_variables.py
Resource                ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource		../../resources/common.robot
Library			Collections


*** Variables ***
${cycles}                        10
${X-API-VERSION}                 ${null}
${FUSION_PROMPT}                 \#
${FUSION_TIMEOUT}                60
${PROFILE_THROTTLE}              3
${PROFILE_ASSIGN_WAIT_TIMEOUT}   860m
${PROFILE_ASSIGN_WAIT_INTERVAL}  3s
${FORCE_PROFILE_APPLY}           all
${tbirdEnv}                      ${True}
${sleep}                         15m

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Begin Cycles
    Cycle   ${cycles}

*** Keywords ***
Cycle
    [Documentation]   Cycle up a test.
    [Arguments]     ${cycles}
    ${orig_network_sets} =   WPST Deep Copy   ${network_sets}
    :FOR	${x}	IN RANGE	1	${cycles}+1
    \   Log To Console   Beginning cycle ${x} of ${cycles}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   Remove ALL Ethernet Networks
    \   Remove ALL FC Networks
    \   Remove ALL FCoE Networks
    \   Remove ALL Network Sets
    \   Sleep And Log Reason To Console   ${sleep}   reason=Sleeping ${sleep} to allow OneView to settle
    \   Add Ethernet Networks
    \   Add Ethernet Ranges
    \   Add Ethernet Networks In Bulk
    \   Sleep And Log Reason To Console   ${sleep}   reason=Sleeping ${sleep} to allow OneView to settle
    \   Add Network Sets
    \   Add Network Set Ranges
    \   Add FC Networks
    \   Add FCoE Networks
    \   Add FCoe Ranges
    \   Sleep And Log Reason To Console   ${sleep}   reason=Sleeping ${sleep} to allow OneView to settle
    \   ${network_sets} =   WPST Deep Copy   ${orig_network_sets}
    \   Set Suite Variable   ${network_sets}


Add Ethernet Networks
    [Documentation]   Add ethernet networks from variable file.
    ${ethernet_networks} =   Get Variable Value   ${ethernet_networks}
    Run Keyword If   ${ethernet_networks} is not ${null}   common.Add Ethernet Networks from variable   ${ethernet_networks}

Add Ethernet Ranges
    [Documentation]   Add ethernet ranges from data variable file.
    ${ethernet_ranges} =   Get Variable Value   ${ethernet_ranges}
    Run Keyword If   ${ethernet_ranges} is not ${null}   Run Keyword for List   ${ethernet_ranges}   common.Create Ethernet Range

Add Ethernet Networks In Bulk
    [Documentation]   Bulk create ethernet networks from data variable file.
    ${bulk_ethernet_network} =   Get Variable Value   ${bulk_ethernet_network}
    ${resp} =   Run Keyword If   ${bulk_ethernet_network} is not ${null}   Fusion Api Create Ethernet Bulk Networks   ${bulk_ethernet_network}
    Pass Execution If   ${resp} is ${null}   Skipping create ethernet bulk networks due to bulk_ethernet_network being NoneType.
    Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=60m   interval=5s
    Asynchronous Task Should Be Successful   ${task}   checkAssociatedResourceUri=${False}

Add Network Sets
    [Documentation]   Add network sets from data variable file.
    ${network_sets} =	Get Variable Value	${network_sets}
    Run Keyword If   ${network_sets} is ${null}    Fail   msg=network_sets variable is ${null}. Please check your data variable file.
    common.Add Network Sets from variable   ${network_sets}

Add Network Set Ranges
    [Documentation]   Add network set ranges from data variable file.
    ${network_set_ranges} =   Get Variable Value   ${network_set_ranges}
    Run Keyword If   ${network_set_ranges} is not ${null}   Run Keyword for List   ${network_set_ranges}   common.Create Network Set Range

Add FC Networks
    [Documentation]   Add Fibre Channel networks from data variable.
    ${fc_networks} =   Get Variable Value   ${fc_networks}
    Run Keyword If   ${fc_networks} is not ${null}   common.Add FC Networks from variable   ${fc_networks}

Add FCoE Networks
    [Documentation]   Add FCoE networks from data variable file.
    ${fcoe_networks} =   Get Variable Value   ${fcoe_networks}
    Run Keyword If   ${fcoe_networks} is not ${null}   common.Add FCoE Networks from variable   ${fcoe_networks}

Add FCoe Ranges
    [Documentation]   Adds the FCoE Ranges from the data variable file.
 	${fcoe_ranges} =	Get Variable Value	${fcoe_ranges}
 	Run Keyword If	${fcoe_ranges} is not ${null}	Run Keyword for List	${fcoe_ranges}	common.Create FCoE Range

Remove ALL Ethernet Networks
    [Documentation]   Remove all ethernet networks except those network still being used by profile(s). Warn user for used network not being removed.
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
