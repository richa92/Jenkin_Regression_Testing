*** Settings ***
Library             Collections
Library             String
Resource            ../resource.txt
Resource            ../../../../Resources/api/settings/appliance_networking.txt
Documentation       CDT Performance Test Cases.
Suite Setup         Setup for Performance
Suite Teardown      Performance Execution PostConditions

# Setup\Teardown for ALL test cases
Test Setup      Test Setup
Test Teardown   Test Teardown


*** Variables ***
${EDIT_SP_BATCH_SIZE}   3
${BATCH_SIZE}           1

*** Test Cases ***
Re-Create LIGs
    [Documentation]     Re-Create LIGs
    [Tags]              LogicalInterconnectGroup    LIG
    ${sas_ligs} =       Get Variable Value              ${sas_ligs}
    ${sas_resplist}=    Run Keyword If      ${sas_ligs} is not ${null}      Run Keyword for Dict    ${sas_ligs}     Add SAS LIG

    ${ligs} =           Get Variable Value          ${ligs}
    ${lig_resplist}=    Run Keyword If      ${ligs} is not ${null}      Run Keyword for Dict    ${ligs}     Add LIG from variable async

    ${resplist}=    Combine Lists    ${sas_resplist}    ${lig_resplist}
    Wait for task2      ${resplist}                     timeout=20m      interval=10

Re-Create EGs
    [Documentation]     Re-Create EGs
    [Tags]              EnclosureGroup    EG
    ${enc_group_dict} =    Evaluate    copy.deepcopy(${enc_groups})    modules=copy
    ${resplist}=           Run Keyword for Dict    ${enc_group_dict}
    ...                 Add Enclosure Group from variable
    Wait for task2      ${resplist}                     timeout=5m      interval=10

Re-Create LEs
    [Documentation]     Re-Create LEs
    [Tags]              LogicalEnclosure   Create_LE               Performance
    ...                 logical_enclosure-condition-single
    ${les} =            Get Variable Value              ${les}
    Create Logical Enclosures    ${les}
    Wait for resources to reach desired state    False
    ${task}    Get Task By Param    param=?filter="'name'='Create' AND associatedResource.resourceName='${les[0]['name']}'"&sort=created:descending&count=1
    ${alt}    Get Active Alert List    ${task['created']}
    ${len}    Get length    ${alt}
    Run keyword and continue on failure    Run keyword if    ${len}!=0    FAIL    Critical/Active alerts exist.
    Check uplink sets and uplink ports

Re-create Server Profile Templates
       [Documentation]     Re-create Server Profile Templates
       [Tags]              CREATE_SPT
       Assign Hardware type to SPT
       ${recreate_spts_dict} =    Evaluate    copy.deepcopy(${spts})    modules=copy
       ${resplist}=    Run Keyword for Dict    ${recreate_spts_dict}    Add Server Profile Template
       ${resp}=    Run Keyword for List    ${resplist}    Wait for Task2    timeout=60    interval=10

Re-create Assigned Server Profiles with new Server Hardware
    [Documentation]  Recreate server profiles on different server hardware of the same server hardware type.
    [Tags]    Profiles
    # Get All Server Hardware by type
    ${AllSH}=   Get All Server Hardware By Type As Dictionary

    # Create new dictionary for new profile to bay mapping
    ${profile_to_bay_map}=    Create Dictionary
    ${server_exclude_list}    Create List
    ${SP_exclude_list_length}    Get Length    ${SP_rotation_exclude_list}
    ${SP_exclude_list_exists}    Set variable    ${None}
    ${SP_exclude_list_exists}    Run keyword if    ${SP_exclude_list_length}!=0    Set variable    ${True}
    # Randomly Update Server Hardware on each profile
    ${sp_len}=     Evaluate    len(${assigned_sps})
    :FOR   ${index}  in range  0   ${sp_len}
    \    ${exclude_server}    Run keyword if    '${SP_exclude_list_exists}'=='True' and '${assigned_sps[${index}]['name']}' in ${SP_rotation_exclude_list}
    \    ...    Fetch From Right    ${assigned_sps[${index}]['serverHardwareUri']}    :
    \    Run keyword if    '${SP_exclude_list_exists}'=='True' and '${assigned_sps[${index}]['name']}' in ${SP_rotation_exclude_list} and '${exclude_server}'!='None'
    \    ...    Append to list    ${server_exclude_list}    ${exclude_server}
    \    Run keyword if    '${SP_exclude_list_exists}'=='True' and '${assigned_sps[${index}]['name']}' in ${SP_rotation_exclude_list}
    \    ...    Set To Dictionary    ${profile_to_bay_map}    ${assigned_sps[${index}]['name']}    ${exclude_server}
    :FOR   ${index}  in range  0   ${sp_len}
    \    # Select random server hardware
    \    Run keyword if    '${SP_exclude_list_exists}'=='True' and '${assigned_sps[${index}]['name']}' in ${SP_rotation_exclude_list}    continue for loop
    \    ${SHT}=    Get Variable Value    ${assigned_sps[${index}]['serverHardwareTypeUri']}
    \    ${SHT}=    Fetch From Right    ${SHT}    :
    \    ${ENC}=    Get Variable Value    ${assigned_sps[${index}]['serverHardwareUri']}
    \    ${ENC}=    Fetch From Right    ${ENC}    :
    \    ${ENC}=    Fetch From Left    ${ENC}    ,
    \    ${enc_uri}=    Common URI lookup by name   ENC:${ENC}
    \    ${sh}=     Get Random Server Hardware by Type from Available Server Hardware    ${SHT}    ${AllSH}    ${enc_uri}    ${server_exclude_list}
    \
    \    # Update Profile Details
    \    Set To Dictionary    ${assigned_sps[${index}]}    serverHardwareUri        SH:${sh}
    \
    \    # Update Assigned Profile to SH map
    \    Set To Dictionary    ${profile_to_bay_map}    ${assigned_sps[${index}]['name']}  ${sh}

    Log List    ${assigned_sps}
    Log List    ${profile_to_bay_map}

    # Power Off Servers
    ${servers}=     Get Dictionary Values       ${profile_to_bay_map}
    Power Off Servers Async                     ${servers}    control=PressAndHold

    # Create Assigned Server Profiles by Batch size
    Create Assigned Server Profiles by Batch size    ${assigned_sps}    ${BATCH_SIZE}

Delete and Recreate Assigned Server Profiles Testcase
    [Tags]              Recreate_Assigned_SP     Profiles    Performance     server_profiles-condition-jbods
    [Documentation]     Delete and Recreate Assigned Server Profiles
    ${del_create_sp_len}=     Evaluate            len(${Delete_recreate_sp})
    Log                 Total profiles to be deleted and created: ${del_create_sp_len}              console=True
    :FOR    ${index}    in range    0    ${del_create_sp_len}    ${BATCH_SIZE}
    \    ${range}=    Evaluate    ${index}+${BATCH_SIZE}
    \    Log    Deleting and Adding profiles ${index} through ${range}    console=True
    \    ${resplist}=    Delete and Recreate Assigned Server Profiles    ${recreate_sp_list[${index}:${range}]}
    \    Run Keyword If    ${resplist} is not ${null}    run keyword and continue on failure    Wait For Task2    ${resplist}    timeout=7200

Edit Server Profile Firmware Baseline With Installation Method as FirmwareOnlyOfflineMode
    [Tags]              EDIT_SP_FIRMWAREONLYOFFLINEMODE                     performance     server_profile-condition-firmware
    [Documentation]     Edit Server Profile Firmware Baseline With Installation Method as FirmwareOnlyOfflineMode
    ${resplist}=        Edit Server Profile With Firmware Baseline from variable offline
    Run Keyword If      ${resplist} is not ${null}
    ...                 run keyword and continue on failure         Verify Any Critical Alert In Server Profile
    ...                 ${resplist}

Edit Server Profile Firmware Baseline With Installation Method as FirmwareAndOSDrivers
    [Tags]              EDIT_SP_FIRMWAREANDOSDRIVERS             performance         server_profile-condition-firmware
    [Documentation]     Edit Server Profile Firmware Baseline With Installation Method as FirmwareAndOSDrivers
    ${resplist}=        Edit Server Profile With Firmware Baseline from variable online
    Run Keyword If      ${resplist} is not ${null}
    ...                 run keyword and continue on failure         Verify Any Critical Alert In Server Profile
    ...                 ${resplist}

Edit Server Profile - BIOS Settings
    [Tags]              EDIT_SP_BIOS        performance                     server_profile-condition-BIOS
    [Documentation]     Edit Server Profile BIOS With Custom POST Message
    ${resplist}=        Edit Server Profile BIOS from variable
    Run Keyword If      ${resplist} is not ${null}
    ...                 run keyword and continue on failure         Verify Any Critical Alert In Server Profile
    ...                 ${resplist}

Edit Server Profile - Server Connections
    [Tags]              EDIT_SP_Connections     performance         server_profile-condition-connections_only
    [Documentation]     Edit Server Profile Connections
    ${resplist}=        Edit Server Profile Connections from variable
    Run Keyword If      ${resplist} is not ${null}
    ...                 run keyword and continue on failure         Verify Any Critical Alert In Server Profile
    ...                 ${resplist}

Edit LIG and LI Update from group
    [Documentation]             Performing the edit LIG and LI update from group
    [Tags]                      EDIT_SP_LI_UPDATEFROMGROUP     Performance   logical-interconnect-condition-updatefromgroup
    ${Net_2200} =               Get Variable Value      ${Net_2200}
    Run Keyword If              ${Net_2200} is not ${null}                      Add Ethernet Networks from variable async
    ...                         ${Net_2200}
    ${lig_uri}=                 Get LIG URI             ${PotashLIG['name']}
    ${resp}=                    Get LIG member          ${PotashLIG['name']}
    ${networks} =               Get From Dictionary     ${Ethernet_Tagged_new}                  networkUris
    ${ethernetUris} =           Get Ethernet URIs       ${networks}
    ${Ethernet_Tagged_us_old}=                          Get From Dictionary     ${potash_us}    Ethernet-Tagged
    ${networks_1} =             Get From Dictionary     ${Ethernet_Tagged_us_old}               networkUris
    ${ethernetUris_1} =         Get Ethernet URIs       ${networks_1}
    ${network_combined} =       combine lists           ${networks_1}           ${networks}
    Set to dictionary           ${Ethernet_Tagged_us_old}                       networkUris=${network_combined}
    Set to dictionary           ${potash_us}            Ethernet-Tagged=${Ethernet_Tagged_us_old}
    ${potash_dict_values} =     Get Dictionary Values   ${potash_us}
    Set to dictionary           ${PotashLIG}            uplinkSets=${potash_dict_values}
    ${body} =                   Build LIG Body          ${PotashLIG}
    ${resp_edit}=               Fusion API Edit LIG     ${body}                 ${lig_uri}
    ${task} =                   Wait For Task           ${resp_edit}            120s            10s
    ${valDict} =                Create Dictionary       status_code=${200}
    ...                         taskState=Completed
    Validate Response           ${task}                 ${valDict}
    Update Logical Interconnect from Group for performance              ${LI}
    Update Network Set          ${network_sets_update_add}

Edit Server Profile to add volumes
    [Documentation]     Edit Server Profiles to add volumes
    [Tags]              EDIT_SP_Volumes     Performance     server_profile-condition-everything
    :FOR    ${pr}    in    @{edit_server_profiles_san_volumes}
    \    Edit Server Profile to add san volumes multiple times    ${pr}
    :FOR    ${pr}    in    @{edit_server_profiles_local_volumes}
    \    Edit Server Profile to add Bigbird volumes multiple times    ${pr}

Restart Configured Appliance
    [Documentation]     Restart Appliance
    [Tags]              Appliance_Restart   Configured
    ${payload}=         resource.Restart Appliance
    # Re-login to the appliance
    Fusion Api Login Appliance              ${APPLIANCE_IP}                 ${admin_credentials}
    Login to Fusion Via SSH
    # Post data to ELK
    Set To Dictionary   ${payload}          condition                       configured
    Run Keyword If      "${production_env}" == "${True}"
    ...                 Post Data to ELK    ${cdt-ci-restart_elk_index}     ${payload}

*** Keywords ***

Setup for Performance
    [Documentation]     Pre-conditions for CDT Test Suite to prevent test executions if Setup/Initial Config fails.
    ...                 Initial Configuration Suite should pass.
    ...                 Environment Validation should pass.
    #Should be true      ${initialConfigSuccess}     Initial Configuration failed to complete successfully.

    # Delete Server Profiles, LEs, EGs, and LIGs
    Test Setup
    Teardown Profiles
    Teardown Logical Elements

    Validate Environment

Performance Execution PostConditions
    [Documentation]    Performance Suite Post execution condition status check
    Set Global variable     ${performanceSuiteSuccess}     ${None}
    Run Keyword If      '${SUITE_STATUS}' == 'PASS'     Set Global variable     ${performanceSuiteSuccess}     ${TRUE}
