*** Settings ***

Documentation       Networks Add And Delete             -  Below is the algorithm of this test suite:
...                                                      1. Login to the Appliance
...                                                      2. Create appliance backup
...                                                      3. Download the backup
...                                                      4. Select the Unique Networks which are to be deleted based on the LIgs available in the Appliance
...                                                      5. Make a note of the count the total number of networks available in the LIG for an Uplink set before deleting the selected network
...                                                      6. Delete the selected network and then again make a note of the count in the same LIG , same Uplink set  after deletion
...                                                      7. Compare the Network count before and after deletion and ensure the count is decreased appropriately based on the networks deleted
...                                                      8. Now Add the deleted networks with same VLAN ID & different name and verify the Add functionality in the Network page
...                                                      9. Loop step 4 through 8 in each cycle until ${CYCLES} complete
...                                                      10. Upload the backup of the appliance and restore the same once the ${CYCLES} completed
...                     Example:
...                              pybot -d /tmp/logs/Networks_Add_Delete -LTRACE -vAPPLIANCE_IP:<Appliance IP> -V <your test data variable file> Networks_Add_delete.robot
...                     Required arguments:
...                         -V /root/ci-fit/config_files/est_robustness_DVF.py
...						For the data variable file template please refer the path,  tests/wpst_crm/ci_fit/tests/robustness/resources/c7000_robustness_data_variables_template.py
...                     Optional arguments:
...                         To trigger detailed resource checking, supply -vGOLDEN_FILE:<backup restore golden json> (Run test Generate-Resource-Json.robot to create golden file)
...                         To change the sender's name, use -vEMAIL_FROM:<email address>
...                         To override the default number of cycles, use -vCYCLES:<number of cycles>

Variables           ../../../robustness/resources/data_variables.py
Resource            ../../../../../crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../../robustness/resources/common.robot
Library             ../../../robustness/resources/robustness-helper.py

Library             RoboGalaxyLibrary
Library             FusionLibrary
Library             OperatingSystem
Library             BuiltIn
Library             Collections
Library             XML
Library             String

*** Variables ***

${CYCLES}                             10
${FUSION_IP}                          ${APPLIANCE_IP}
${GOLDEN_FILE}                        None
${EMAIL_FROM}                         ${EMAIL_TO}
${ENC}                                None
${ONE_TIME_PASS}                      None
${tbirdEnv}                           None
${dataFilesDir}                       dataFiles
${backupFile}                         ${dataFilesDir}/backup-restore-test.bkp
${HA_FILE}                            None
${SERVER_BONDING_CHECKS}              None
${DISABLE_BONDING_MULTI_TEST}         True
${CHECK_ETH_SUMMARY}                  None
${UPDATE_LFCCACHE}                    False
${NET_REMOVE_OR_ADD_WAIT_TIMEOUT}     600s
${NET_REMOVE_OR_ADD_WAIT_INTERVAL}    30s

*** Test Cases ***

Login Appliance And Set Test
    [Tags]    LOGIN
    Set Log Level    TRACE
    Authenticate And Set Login

VerIfy for alerts or warnings
    [Tags]    VERIfYALERTS
    Set Log Level    TRACE
    Check Common Resource Attributes

Backup of the appliance
    [Tags]    APPLIANCE_BACKUP
    Set Log Level    TRACE
    Create Appliance Backup Download And Data Compare   wait_task_timeout=${CREATE_BACKUP_WAIT_TIMEOUT}   wait_task_interval=${CREATE_BACKUP_WAIT_INTERVAL}
    Log    Appliance Backup is taken successfully    console=${True}

Random Network Selection for Deleting a pair of networks and adding them back for every LIG
    [Tags]    SELECT_NET
    Set Log Level    TRACE
    ${resp1} =   Fusion Api Get Lig
    ${Total_ligs_length} =     Get Length    ${resp1['members']}
    :FOR    ${cycle_count}    IN RANGE    1    ${CYCLES}+1
    \   Log    Cycle:${cycle_count} of ${CYCLES} started    console=${True}  
    \   Fetch Network Count and Compare Count     ${resp1}    ${Total_ligs_length}
    \   Log    Cycle:${cycle_count} of ${CYCLES} Completed    console=${True}

Restore the appliance
    [Tags]    GROUND_STATE
    Set Log Level    TRACE
    ${EG} =      Pick One EG And Use It
    Upload Restore Backup And Perform Data Compare   upload_task_timeout=${UPLOAD_BACKUP_WAIT_TIMEOUT}   upload_task_interval=${UPLOAD_BACKUP_WAIT_INTERVAL}
    ...             restore_task_timeout=${RESTORE_BACKUP_WAIT_TIMEOUT}   restore_task_interval=${RESTORE_BACKUP_WAIT_INTERVAL}

Send Email Notification
    [Tags]    SEND_A_MAIL
    Set Log Level    TRACE
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.

*** Keywords ***

Fetch Network Count and Compare Count
    [Documentation]   Fetches the list of LIG response output for which networks are going to be deleted and compares the count
    [Arguments]    ${response_lig}     ${length_of_ligs}
    :FOR    ${lig_count}    IN RANGE     0     ${length_of_ligs}
    \   ${redundant_count_network} =      Create List
    \   Set Suite Variable     ${redundant_count_network}
    \   ${lig_us_count_of_network_name} =      Create Dictionary
    \   ${lig_uri} =    Set Variable    ${response_lig['members'][${lig_count}]['uri']}
    \   Log      LIG_URI : ${lig_uri}           INFO
    \   ${resp2} =   Fusion Api Get Lig    uri=${lig_uri}
    \   ${uplinkset_list_in_lig} =        Set Variable       ${resp2['uplinkSets']}
    \   ${x} =       Get Length          ${uplinkset_list_in_lig}
    \   Log      TOTAL UPLINK SETS AVAILABLE : ${x}         INFO
    \   ${uplink_set_list_selected} =      Fetch the Uplink Set Names alone    ${uplinkset_list_in_lig}
    \   Updating a new dictionary      ${lig_us_count_of_network_name}     ${uplink_set_list_selected}
    \   Log      BEFORE DELETION : LIG : ${response_lig['members'][${lig_count}]['name']} UplinkSetName : ${lig_us_count_of_network_name['uplinkset_name']} Total network Count : ${lig_us_count_of_network_name['networks_count']}
    \   ${Networks_to_be_deleted_list} =     Random selection of Networks from Uplink Sets     ${lig_us_count_of_network_name}
    \   Log      ${Networks_to_be_deleted_list}
    \   ${count_of_net_deleted} =      Get Length      ${Networks_to_be_deleted_list}
    \   Log     Number of Networks Deleted count :::::::: ${count_of_net_deleted}
    \   Should Be True      ${count_of_net_deleted} >= 2        Fails If ${Networks_to_be_deleted_list} is empty
    \   ${networks_to_be_Added_list} =      Fetch Network Name And VLAN ID to be Added      ${Networks_to_be_deleted_list}
    \   Set Suite Variable      ${networks_to_be_Added_list}
    \   Delete Selected Networks      ${Networks_to_be_deleted_list}
    \   ${resp2_after} =   Fusion Api Get Lig    uri=${lig_uri}
    \   ${uplinkset_list_in_lig_after} =        Set Variable       ${resp2_after['uplinkSets']}
    \   ${lig_us_count_of_network_name_after_del} =     Fetch the Uplink Set Networks Count after deletion     ${uplinkset_list_in_lig_after}     ${lig_us_count_of_network_name['uplinkset_name']}
    \   Log      AFTER DELETION : LIG : ${response_lig['members'][${lig_count}]['name']} UplinkSetName : ${lig_us_count_of_network_name_after_del['uplinkset_name']} Total network Count : ${lig_us_count_of_network_name_after_del['networks_count']}
    \   ${Network_count_before} =    Set Variable     ${lig_us_count_of_network_name['networks_count']}
    \   ${Network_count_after} =    Set Variable     ${lig_us_count_of_network_name_after_del['networks_count']}
    \   Should Be True      ${Network_count_before} == ${Network_count_after} + ${count_of_net_deleted}      Fails If networks deleted count mismatch
    \   Run Keyword If   ${networks_to_be_Added_list} is not ${null}       Add Networks from variable       ${networks_to_be_Added_list}

Fetch the Uplink Set Names alone
    [Documentation]   Fetches the Uplink Set name in an LIG for which networks will be deleted
    [Arguments]     ${uplink_set_names_common}
    ${uplink_Set_selected} =     Set Variable
    Set Suite Variable   ${uplink_Set_selected}
    ${uplink_set_list_selected} =     Set Variable
    Set Suite Variable      ${uplink_set_list_selected}
    ${new_list_with_tagged_us} =     Create List
    ${flag_for_one_net_case} =     Set Variable     0
    :FOR    ${us_in_lig}    IN    @{uplink_set_names_common}
    \   ${match_type_net_type} =    Set Variable     ${us_in_lig['ethernetNetworkType']}
    \   Run keyword If      '${match_type_net_type}' == 'Tagged'       Append To List   ${new_list_with_tagged_us}      ${us_in_lig}
    ${uplink_set_length_modIfied} =     Get Length    ${new_list_with_tagged_us}
    :FOR    ${us_in_lig}    IN RANGE     0     ${uplink_set_length_modIfied}
    \   ${gets_uplink_set_names} =      Set Variable    ${new_list_with_tagged_us[${us_in_lig}]['name']}
    \   ${match_type_net_type} =    Set Variable     ${new_list_with_tagged_us[${us_in_lig}]['ethernetNetworkType']}
    \   ${uplink_Set_selected_1}     ${uplink_set_list_selected_1} =      Run keyword If        '${match_type_net_type}' == 'Tagged'      Fetch the Uplink Set with Valid Networks with VLAN ID   ${new_list_with_tagged_us[${us_in_lig}]}     ${flag_for_one_net_case}
    \   Run keyword If      '${uplink_Set_selected_1}' != '' and '${uplink_Set_selected_1}' != 'None'      Exit For Loop
    \   ${flag_for_one_net_case} =     Set Variable If      '${uplink_Set_selected_1}' == '' or '${uplink_Set_selected_1}' == 'None'     1
    ${uplink_Set_selected}     ${uplink_set_list_selected} =     Run keyword If     '${uplink_Set_selected_1}' == '' or '${uplink_Set_selected_1}' == 'None' and ${flag_for_one_net_case} == 1     Fetch the Uplink Set with Valid Networks with VLAN ID      ${new_list_with_tagged_us[0]}     1
    ...                   ELSE    Set Variable   ${uplink_Set_selected_1}      ${uplink_set_list_selected_1}
    Log     ${uplink_Set_selected}
    Should Be True      '${uplink_Set_selected}' != '' and '${uplink_Set_selected}' != 'None'        Fails If ${uplink_Set_selected} is empty
    [RETURN]       ${uplink_set_list_selected}

Fetch the Uplink Set with Valid Networks with VLAN ID
    [Documentation]   Fetches the Uplink Set name in an LIG for which networks belong to both Ethernet and FCOE
    [Arguments]     ${uplink_set}     ${flag}
    ${networks_available} =      Set Variable      ${uplink_set['networkUris']}
    ${match_for_fcoe_network} =     Get Match Count     ${networks_available}     regexp=.*fcoe.*      VerIfied the Uplink Set for FCOE Networks
    Set Suite Variable      ${match_for_fcoe_network}
    ${match_for_ethernet_network} =     Get Match Count     ${networks_available}     regexp=.*ethernet.*      VerIfied the Uplink Set for Ethernet Networks
    Set Suite Variable      ${match_for_ethernet_network}
    ${uplink_Set_selected} =      Set Variable If       ${match_for_fcoe_network} >= 1 and ${match_for_ethernet_network} >= 1    ${uplink_set['name']}
    ...     ${match_for_fcoe_network} <= 1 and ${flag} == 0    ${NULL}
    ...     ${match_for_ethernet_network} <= 1 and ${flag} == 0    ${NULL}
    ...     ${match_for_fcoe_network} <= 1 and ${flag} != 0    ${uplink_set['name']}
    ...     ${match_for_ethernet_network} <= 1 and ${flag} != 0    ${uplink_set['name']}
    ${uplink_set_list_selected} =     Set Variable     ${uplink_set}
    Log     ${uplink_Set_selected}
    [RETURN]     ${uplink_Set_selected}     ${uplink_set_list_selected}

Updating a new dictionary
    [Documentation]   Updates a dictionary with the keys and values specIfied
    [Arguments]     ${new_dict}    ${old_dict}
    ${uplinksetname_temp} =     Set Variable            ${old_dict['name']}
    ${enet_uri_temp} =     Set Variable      ${old_dict['networkUris']}
    ${enet_count_temp} =   Get Length          ${old_dict['networkUris']}
    Set to Dictionary    ${new_dict}    uplinkset_name    ${uplinksetname_temp}
    ...                                 enet_uri          ${enet_uri_temp}
    ...                                 networks_count    ${enet_count_temp}
    [RETURN]    ${new_dict}

Random selection of Networks from Uplink Sets
    [Documentation]   Picks selective network URis from a  range .
    [Arguments]     ${list_of_uris}
    ${Networks_to_be_Deleted_list} =    Create List
    ${list_of_uris_length} =     Get Length     ${list_of_uris['enet_uri']}
    :FOR    ${uri_enet_fcoe}    IN RANGE     0     2
    \   ${fcoe_uri} =     Run Keyword If    ${match_for_fcoe_network} >= 1      Random Number Generation for FCOE Network    ${list_of_uris_length}     ${list_of_uris['enet_uri']}
    \   Run Keyword If     '${fcoe_uri}' != '' and '${fcoe_uri}' != 'None'    Append To List     ${Networks_to_be_Deleted_list}      ${fcoe_uri}
    \   ${ethernet_uri} =     Run Keyword If    ${match_for_ethernet_network} >= 1      Random Number Generation for Ethernet Network    ${list_of_uris_length}     ${list_of_uris['enet_uri']}
    \   Run Keyword If     '${ethernet_uri}' != '' and '${ethernet_uri}' != 'None'    Append To List     ${Networks_to_be_Deleted_list}      ${ethernet_uri}
    [RETURN]     ${Networks_to_be_Deleted_list}

Random Number Generation for FCOE Network
    [Documentation]   Generates a Random number based on the range specified .
    [Arguments]     ${LENGTH}     ${list_item}
    ${actual_len} =     Evaluate   ${LENGTH} - 1
    :FOR    ${uri}    IN RANGE     0     ${actual_len}
    \   ${random_num} =     Evaluate    random.randint(0,${actual_len})     random
	\	Log    ${list_item[${random_num}]}    console=${True}
    \   ${uri_match} =    Get Lines Matching Regexp     ${list_item[${random_num}]}     (?i).*fcoe.*
    \   Run Keyword If      '${uri_match}' != '' and '${uri_match}' != 'None'     Append To List     ${redundant_count_network}     ${random_num}
    \   ${redundant_count_compare} =        Run Keyword If      '${uri_match}' != '' and '${uri_match}' != 'None'       Get Count        ${redundant_count_network}    ${random_num}
    \   Run Keyword If      ${redundant_count_compare} == 1      Exit For Loop
    ...             ELSE     Continue For Loop
    \   Run Keyword If      '${uri_match}' != '' and '${uri_match}' != 'None'      Exit For Loop
    ...             ELSE     Continue For Loop
    [RETURN]    ${uri_match}

Random Number Generation for Ethernet Network
    [Documentation]   Generates a Random number based on the range specified .
    [Arguments]     ${LENGTH}     ${list_item}
    ${actual_len} =     Evaluate   ${LENGTH} - 1
    :FOR    ${uri}    IN RANGE     0     ${actual_len}
    \   ${random_num} =     Evaluate    random.randint(0,${actual_len})     random
    \   ${uri_del} =     Set Variable      ${list_item[${random_num}]}
	\	Log    ${list_item[${random_num}]}    console=${True}
    \   ${uri_match} =    Get Lines Matching Regexp     ${list_item[${random_num}]}     (?i).*fcoe.*
    \   Run Keyword If      '${uri_match}' == '' or '${uri_match}' == 'None'     No Operation
    ...           ELSE     Continue For Loop
    \   ${uri2} =     Set Variable    associatedProfiles
    \   ${uri_net} =    Catenate    SEPARATOR=/     ${list_item[${random_num}]}    ${uri2}
    \   Log     ${uri_net}
    \   ${resp3} =    Run Keyword If     '${uri_match}' == '' or '${uri_match}' == 'None'       Fusion Api Get Resource   ${uri_net}
    \   ${ENET_LEN} =     Run Keyword If      '${uri_match}' == '' or '${uri_match}' == 'None'      Get Length     ${resp3['_content']}
    \   Run keyword if   ${ENET_LEN} > 1     Exit For Loop
    ...         ELSE     Continue For Loop
    \   Run Keyword If      '${uri_match}' == '' or '${uri_match}' == 'None'      Append To List     ${redundant_count_network}     ${random_num}
    \   ${redundant_count_compare} =        Run Keyword If      '${uri_match}' == '' or '${uri_match}' == 'None'       Get Count         ${redundant_count_network}    ${random_num}
    \   Run Keyword If      ${redundant_count_compare} == 1      Exit For Loop
    ...             ELSE     Continue For Loop
    [RETURN]    ${uri_del}

Delete Selected Networks
    [Documentation]   Deletes Dummy Networks
    [Arguments]     ${networks}
    Set Log Level    TRACE
    :FOR    ${net_uri}     IN       @{networks}
    \   ${uri_match_enet} =       Get Lines Matching Regexp    ${net_uri}    (?i).*ethernet.*
    \   ${uri_match_fcoe} =       Get Lines Matching Regexp    ${net_uri}    (?i).*fcoe.*
    \   ${resp_del} =     Run Keyword If   '${uri_match_enet}' != '' and '${uri_match_enet}' != 'None'       Fusion Api Delete Ethernet Network      uri=${net_uri}
    ...    ELSE      Run Keyword If   '${uri_match_fcoe}' != '' and '${uri_match_fcoe}' != 'None'       Fusion Api Delete FCoE Network        uri=${net_uri}
    \   ${task} =  fusion_api_appliance_setup.Wait For Task    ${resp_del}    ${NET_REMOVE_OR_ADD_WAIT_TIMEOUT}    ${NET_REMOVE_OR_ADD_WAIT_INTERVAL}

Fetch the Uplink Set Networks Count after deletion
    [Documentation]  Fetches the list of Uplink Set Network Count after deletion by taking the LIG response .
    [Arguments]     ${list_of_us_avail}       ${selected_us_name}
    :FOR     ${count_after_del_in_us}     IN        @{list_of_us_avail}
    \   ${dict_new_del} =     Create Dictionary
    \   Run Keyword If       '${count_after_del_in_us['name']}' == '${selected_us_name}'       Updating a new dictionary       ${dict_new_del}    ${count_after_del_in_us}
    \   Run Keyword If       '${count_after_del_in_us['name']}' == '${selected_us_name}'        Exit For Loop
    ...      ELSE      Continue For Loop
    [RETURN]     ${dict_new_del}

Fetch Network Name And VLAN ID to be Added
    [Documentation]  Fetches Network Names & VLAN Ids for the URI inputs .
    [Arguments]     ${list_of_uris_enet}
    ${Network_Body_List} =      Create List
    ${Network_Body_Dict} =      Create Dictionary
    :FOR     ${net_uris}     IN        @{list_of_uris_enet}
    \   ${response} =      Fusion Api Get Ethernet Networks    uri=${net_uris}
    \   Append to List     ${Network_Body_List}     ${response}
    Log      ${Network_Body_List}
    ${list_of_net_body_addition} =      Create Network body     ${Network_Body_List}
    [RETURN]     ${list_of_net_body_addition}

Create Network body
    [Documentation]   Creates a list of dictionary containing network body .
    [Arguments]     ${network_uri_resp}
    ${network_addition_list} =    Create List
    ${network_uri_addition_count} =    Get Length     ${network_uri_resp}
    :FOR    ${net_uri}     IN RANGE     0      ${network_uri_addition_count}
    \   ${network_addition_dict} =    Create Dictionary
    \   ${temp_name1} =     Set Variable        ${network_uri_resp[${net_uri}]['name']}
    \   ${temp_name} =     Catenate    SEPARATOR=-     ${temp_name1}    test
    \   ${uri_match_enet} =       Get Lines Matching Regexp    ${network_uri_resp[${net_uri}]['type']}    (?i).*ethernet.*
    \   ${uri_match_fcoe} =       Get Lines Matching Regexp    ${network_uri_resp[${net_uri}]['type']}    (?i).*fcoe.*
    \   Run Keyword If    '${uri_match_enet}' != '' and '${uri_match_enet}' != 'None'       Set to Dictionary    ${network_addition_dict}      name     ${temp_name}
    ...                                                    type     ${network_uri_resp[${net_uri}]['type']}
    ...                                                    vlanId   ${network_uri_resp[${net_uri}]['vlanId']}
    ...                                                    purpose  ${network_uri_resp[${net_uri}]['purpose']}
    ...                                                    smartLink     ${network_uri_resp[${net_uri}]['smartLink']}
    ...                                                    privateNetwork      ${network_uri_resp[${net_uri}]['privateNetwork']}
    ...                                                    connectionTemplateUri     ${null}
    ...                                                    ethernetNetworkType     ${network_uri_resp[${net_uri}]['ethernetNetworkType']}
    \   Run Keyword If     '${uri_match_fcoe}' != '' and '${uri_match_fcoe}' != 'None'     Set to Dictionary    ${network_addition_dict}      name     ${temp_name}
    ...                                                    type     ${network_uri_resp[${net_uri}]['type']}
    ...                                                    vlanId   ${network_uri_resp[${net_uri}]['vlanId']}
    ...                                                    connectionTemplateUri     ${null}
    \   Append to List     ${network_addition_list}      ${network_addition_dict}
    [RETURN]     ${network_addition_list}

Add Networks from variable
    [Documentation]   Adds ethernet or fcoe networks from variable file.
    [Arguments]     ${networks}
    :FOR    ${net_uri}     IN       @{networks}
    \   ${uri_match_enet} =       Get Lines Matching Regexp    ${net_uri['type']}    (?i).*ethernet.*
    \   ${uri_match_fcoe} =       Get Lines Matching Regexp    ${net_uri['type']}    (?i).*fcoe.*
    \   ${resp} =      Run Keyword If   '${uri_match_enet}' != '' and '${uri_match_enet}' != 'None'       Fusion Api Create Ethernet Network     body=${net_uri}
        ...     ELSE         Fusion Api Create FCoE Network         body=${net_uri}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task    ${resp}    ${NET_REMOVE_OR_ADD_WAIT_TIMEOUT}    ${NET_REMOVE_OR_ADD_WAIT_INTERVAL}