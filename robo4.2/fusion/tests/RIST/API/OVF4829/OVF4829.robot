*** Settings ***
Documentation
...                   Description:  Q2 tests for 2 boot volume support on BladeSystem.  2 boot volumes are usually implemented
...                                 as a set of mirrored peer-persistent volumes on separate storage systems for increased
...                                 HA.  2 boot volumes are supported in OneView for FC and FCoE protocols, iSCSI mode is
...                                 not supported. This test exercises FC protocol only, FC and FCoE in OneView is considered
...                                 as equivalent by the dev team.
...
...                   Rally:  OVF4829
...
...                   HW Requirements:
...                       Servers Hardware Type(s):
...                           BL * gen 9 blade with FC mezz card (QMH2572,LPe1205A) in appropriate slot
...                           BL * gen 10 blade with FC mezz card (QMH2572,QMH2672,LPe1205A,LPe1605) in appropriate slot
...
...                   Interconnects
...                       Virtual Connect SE 16Gb FC Module for Synergy (Carbon) with 2 uplinks for 2 SANs
...
...                   Local Storage (BigBird/Natasha): Not needed
...
...                   Uplinks/Connections
...                       FC - uplinks for A and B side SANs ('VSAN20' and 'VSAN30' in the test data)
...
...                   External Storage
...                       Note: ideally this test would use a peer-persisted set of 2 StoreServs. Only 1 was available
...                             during development of both the OVF4829 feature code as well as this Q2 test suite, so
...                             both volumes are created on the same StoreServ. The StoreServ was configured on both the
...                             VSAN20 and VSAN30 SANs simulating 2 separate StoreServs.
...
...                             The StoreVirtuals are only present in this test suite to implement the negative test case
...                             verifying that iSCSI is not supported for 2 boot volumes
...                       Storage System Type(s):  StoreVirtual and StoreServ
...                       Storage Pools: StoreServ: FC_r1
...                                      StoreVirtual: dl801Cluster, dl802Cluster ()
...                       Storage Volumes:
...                           Existing:  None
...                           Created:  StoreServ: OVF4829_vol1, OVF4829_vol2 (ephemeral)
...                                                OVF4829_FixedVol1, OVF4829_FixedVol2 (fixed, created by suite setup,
...                                                                                      removed during suite teardown)
...                                     StoreVirtual: OVF4829_vol1, OVF4829_vol2 (not actually created, only used for
...                                                                               negative iSCSI testing)
...
...                   Other External Systems needed
...                       None
...
...                   Special Algorithms, Conversions, "Python Helpers" or Scripts
...                        Explain any "specials" that were created for this test or list: None
...                        All created Helpers and Scripts are in the repo:  .\Tools\Some_New_Tool
...
...                   Shared Keywords Created (Resources\api)
...                       If any New Keywords were created, list those here or list: None

Library             FusionLibrary
Library             BuiltIn
Library             Collections

Resource            ../global_variables.robot
Resource            ./../../../../Resources/api/fusion_api_resource.txt

Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Initialize the Variables and Log In as Administrator
...                 AND             Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
...                 AND             Add Fixed Volumes
Suite Teardown      Run Keywords    Initialize Appliance For Test Case
...                 AND             Remove Fixed Volumes
...                 AND             Fusion Api Logout Appliance

*** Variables ***
${SP_CREATE_TIMEOUT}  1200

*** Test Cases ***

OVF4829 TS1 - Create and Verify Gen9 UEFI 2 Target 2 Boot Volume FC Boot Profile
    [Tags]  SP  TS1
    [Documentation]  Verify Gen9 2 target 2 boot volume server profile
    Initialize Appliance For Test Case

    ${task}=  Add Server Profile  ${ts1_gen9_2_target_2_boot_volume_sp}
    Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10

    ${sp}=  Get Resource  SP:${PROFILE1_GEN9_NAME}

    Gen9 SP Should Match Server RIS  ${sp}  ${ris_node_gen9}
    SP Settings Should Match Storage System  ${sp}

OVF4829 TS1 - Create and Verify Gen10 UEFI 2 Target 2 Boot Volume FC Boot Profile
    [Tags]  SP  TS1
    [Documentation]  Verify Gen10 2 target 2 boot volume server profile
    Initialize Appliance For Test Case

    ${task}=  Add Server Profile  ${ts1_gen10_2_target_2_boot_volume_sp}
    Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10

    ${sp}=  Get Resource  SP:${PROFILE1_GEN10_NAME}

    Gen10 SP Should Match Server RIS  ${sp}  ${ris_node_gen10}
    SP Settings Should Match Storage System  ${sp}

OVF4829 TS2 - Create SPT From SP, Recreate SP From SPT, and Verify 2 Boot Volumes
    [Tags]  SP  TS2
    [Documentation]  Test SPT<->SP transitions
    Initialize Appliance For Test Case

    ${task}=  Add Server Profile  ${ts1_gen10_2_target_2_boot_volume_sp}
    Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10

    ${sp}=  Get Resource  SP:${ts1_gen10_2_target_2_boot_volume_sp['name']}
    Gen10 SP Should Match Server RIS  ${sp}  ${ris_node_gen10}
    SP Settings Should Match Storage System  ${sp}

    ${spt}=  Get Resource  ${sp['uri']}/new-profile-template

    # override default LoadBalanced priority so we can verify primary and secondary later
    :FOR  ${conn}  IN  @{spt['connectionSettings']['connections']}
    \   Run Keyword If  ${conn['id']} == 1  Set To Dictionary  ${conn['boot']}  priority=Primary
    \   Run Keyword If  ${conn['id']} == 2  Set To Dictionary  ${conn['boot']}  priority=Secondary

    Remove From Dictionary  ${spt}  status_code  headers
    Set To Dictionary  ${spt}  name=${PROFILE_TEMPLATE1_GEN10_NAME}
    ${task} =  Fusion Api Create Server Profile Template    body=${spt}
    Wait For Task2  ${task}  timeout=300  interval=10

    ${task}=  Remove Server Profiles by Server Hardware  ${server_hardware_uris}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${task}=  Add Server Profile  ${sp_from_spt_Gen10}
    Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10

    ${sp}=  Get Resource  SP:${PROFILE1_GEN10_NAME}
    Gen10 SP Should Match Server RIS  ${sp}  ${ris_node_gen10}
    SP Settings Should Match Storage System  ${sp}

OVF4829 TS3 - Create Gen9 2 fixed boot volume SP with 1 connection and verify
    [Tags]  SP  TS3
    [Documentation]  Verify Gen9 2 target 2 boot volume server profile with 1 connection and fixed volumes
    Initialize Appliance For Test Case

    ${task}=  Add Server Profile  ${ts3_gen9_2_target_2_boot_volume_1_conn_sp}
    Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10

    ${sp}=  Get Resource  SP:${ts3_gen9_2_target_2_boot_volume_1_conn_sp['name']}

    ${pconn}=  Get Connection by Boot Priority  ${sp["connectionSettings"]["connections"]}  Primary
    ${ptarget1}=  Set Variable  ${pconn['boot']['targets'][0]}
    ${ptarget2}=  Set Variable  ${pconn['boot']['targets'][1]}

    SP Settings Should Match Storage System  ${sp}

    # Verify that the server is configured correctly
    # Gen9 servers only have 2 DesiredBootDevices entries, elements which are not common between the 2 are empty
    ${ris}=  Get RIS Node  ${ris_node_gen9}

    WWNs Should Be Equal  ${ptarget1['arrayWwpn']}  ${ris['DesiredBootDevices'][0]['Wwn']}
    ${nrislun}=  Normalize RIS FC LUN  ${ris['DesiredBootDevices'][0]['Lun']}
    Should Be Equal  ${ptarget1['lun']}        ${nrislun}

    WWNs Should Be Equal  ${ptarget1['arrayWwpn']}  ${ris['DesiredBootDevices'][1]['Wwn']}
    ${nrislun}=  Normalize RIS FC LUN  ${ris['DesiredBootDevices'][1]['Lun']}
    Should Be Equal  ${ptarget2['lun']}        ${nrislun}

OVF4829 TS4 - Storage System Port Load Should Be Balanced
    [Tags]  SP  TS4
    [Documentation]  Create Gen9 and Gen10 2 target 2 boot volume profiles, storage port target WWPNs usage should be equally distributed
    Initialize Appliance For Test Case

    ${task}=  Add Server Profile  ${ts4_gen9_2_target_1_boot_volume_sp}
    Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10

    ${sp9}=  Get Resource  SP:${PROFILE1_GEN9_NAME}

    ${task}=  Add Server Profile  ${ts4_gen10_2_target_1_boot_volume_sp}
    Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10

    ${sp10}=  Get Resource  SP:${PROFILE1_GEN10_NAME}

    # Verify port load balancing
    ${pconn9}=   Get Connection by Boot Priority  ${sp9["connectionSettings"]["connections"]}   Primary
    ${sconn9}=   Get Connection by Boot Priority  ${sp9["connectionSettings"]["connections"]}   Secondary
    ${pconn10}=  Get Connection by Boot Priority  ${sp10["connectionSettings"]["connections"]}  Primary
    ${sconn10}=  Get Connection by Boot Priority  ${sp10["connectionSettings"]["connections"]}  Secondary

    ${target_port_usage}=  Initialized Target Port Usage  ${sp9['sanStorage']['volumeAttachments'][0]['volumeStorageSystemUri']}
    Increment Target Port Usage  ${target_port_usage}  ${pconn9['boot']['targets'][0]['arrayWwpn']}
    Increment Target Port Usage  ${target_port_usage}  ${pconn9['boot']['targets'][1]['arrayWwpn']}
    Increment Target Port Usage  ${target_port_usage}  ${sconn9['boot']['targets'][0]['arrayWwpn']}
    Increment Target Port Usage  ${target_port_usage}  ${sconn9['boot']['targets'][1]['arrayWwpn']}
    Increment Target Port Usage  ${target_port_usage}  ${pconn10['boot']['targets'][0]['arrayWwpn']}
    Increment Target Port Usage  ${target_port_usage}  ${pconn10['boot']['targets'][1]['arrayWwpn']}
    Increment Target Port Usage  ${target_port_usage}  ${sconn10['boot']['targets'][0]['arrayWwpn']}
    Increment Target Port Usage  ${target_port_usage}  ${sconn10['boot']['targets'][1]['arrayWwpn']}

    ${per_port_usage}=  Get Dictionary Values  ${target_port_usage}
    Sort List  ${per_port_usage}
    ${min_max_diff}=  Evaluate  ${per_port_usage[-1]} - ${per_port_usage[0]}
    Should be True  ${min_max_diff} < 2

OVF4829 TS5 - Backward Compatibility - SP with Primary and Secondary Boot Volumes API 800 Edit
    [Tags]  SP  TS5
    [Documentation]  Verify that a 2 boot volume SP can be edited using API 800 and retain 2 boot volume settings
    Initialize Appliance For Test Case
    ${edited_sp_description}=  Set Variable  ThisSPWasEdited

    ${task}=  Add Server Profile  ${ts1_gen10_2_target_2_boot_volume_sp}
    Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10

    ${sp}=  Get Resource  SP:${PROFILE1_GEN10_NAME}  api=800
    Set to Dictionary  ${sp}  description=${edited_sp_description}
    Remove From Dictionary  ${sp}  status_code  headers
    ${task} =    Fusion Api Edit Server Profile   body=${sp}    uri=${sp['uri']}  api=800
    Wait For Task2  ${task}  timeout=60  interval=2
    ${sp}=  Get Resource  SP:${PROFILE1_GEN10_NAME}
    Should Be Equal  ${sp['description']}  ${edited_sp_description}
    :FOR  ${va}  IN  @{sp['sanStorage']['volumeAttachments']}
    \   Run Keyword If  ${va['id']} == 1  Should Be Equal  ${va['bootVolumePriority']}  Primary
    \   Run Keyword If  ${va['id']} == 2  Should Be Equal  ${va['bootVolumePriority']}  Secondary

OVF4829 TS5 - Backward Compatibility - API 800 SP Edit Add Second Volume and Change It To The Boot Volume
    [Tags]  SP  TS5
    [Documentation]  Verify that a second volume can be added as new boot volume via API800
   Initialize Appliance For Test Case

    ${task}=  Add Server Profile  ${ts5_gen10_2_target_1_boot_volume_api800_sp}  api=800
    Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10

    ${sp}=  Get Resource  SP:${PROFILE1_GEN10_NAME}  api=800
    Should Be True  ${sp['sanStorage']['volumeAttachments'][0]['isBootVolume']}

    Set to Dictionary  ${sp['sanStorage']['volumeAttachments'][0]}  isBootVolume=False
    ${my_vol}=  Copy Dictionary  ${ts5_gen10_2_target_1_boot_volume_api800_sp_add_volume}
    ${lookup}=  Common URI Lookup by Name  ${my_vol['volumeStorageSystemUri']}
    Set to Dictionary  ${my_vol}  volumeStorageSystemUri=${lookup}
    ${lookup}=  Common URI Lookup by Name  ${my_vol['volume']['properties']['storagePool']}
    Set to Dictionary  ${my_vol['volume']['properties']}  storagePool=${lookup}
    Lookup Volume Template Uri  ${my_vol}
    Append to List  ${sp['sanStorage']['volumeAttachments']}  ${my_vol}
    Remove From Dictionary  ${sp}  status_code  headers
    ${task} =    Fusion API Edit Server Profile   body=${sp}    uri=${sp['uri']}  api=800
    Wait For Task2  ${task}  timeout=600  interval=10

    ${sp}=  Get Resource  SP:${PROFILE1_GEN10_NAME}  api=800
    :FOR  ${va}  IN  @{sp['sanStorage']['volumeAttachments']}
    \   Run Keyword If  ${va['id']} == 1  Should Not Be True  ${va['isBootVolume']}
    \   Run Keyword If  ${va['id']} == 2  Should Be True  ${va['isBootVolume']}

OVF4829 TS5 - Backward Compatibility - API 800 SP 1 Boot, 1 Data volume
    [Tags]  SP  TS5
    [Documentation]  Verify 1 boot, 1 data volume SP via API800
   Initialize Appliance For Test Case

    ${task}=  Add Server Profile  ${ts5_gen10_2_target_1_boot_volume_1_data_volume_api800_sp}  api=800
    Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10

    ${sp}=  Get Resource  SP:${PROFILE1_GEN10_NAME}
    :FOR  ${vol}  IN  @{sp['sanStorage']['volumeAttachments']}
    \   Run Keyword If  ${vol['id']} == 1  Should Be Equal  ${vol['bootVolumePriority']}  Primary
    \   Run Keyword If  ${vol['id']} == 2  Should Be Equal  ${vol['bootVolumePriority']}  NotBootable

OVF4829 TS5 - Backward Compatibility - SPT with Primary and Secondary Boot Volumes API 800 Edit
    [Tags]  SP  TS5
    [Documentation]  Verify that a 2 boot volume SP can be edited using API 800 and retain 2 boot volume settings
   Initialize Appliance For Test Case
   ${edited_spt_description}=  Set Variable  ThisSPTWasEdited

    ${task}=  Add Server Profile Template  ${ts5_gen10_2_target_2_boot_volume_spt}
    Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10

    ${spt}=  Get Resource  SPT:${PROFILE_TEMPLATE1_GEN10_NAME}  api=800
    Set to Dictionary  ${spt}  description=${edited_spt_description}
    Remove From Dictionary  ${spt}  status_code  headers
    ${task} =    Fusion Api Edit Server Profile Template  body=${spt}    uri=${spt['uri']}  api=800
    Wait For Task2  ${task}  timeout=60  interval=2
    ${spt}=  Get Resource  SPT:${PROFILE_TEMPLATE1_GEN10_NAME}
    Should Be Equal  ${spt['description']}  ${edited_spt_description}
    :FOR  ${va}  IN  @{spt['sanStorage']['volumeAttachments']}
    \   Run Keyword If  ${va['id']} == 1  Should Be Equal  ${va['bootVolumePriority']}  Primary
    \   Run Keyword If  ${va['id']} == 2  Should Be Equal  ${va['bootVolumePriority']}  Secondary

OVF4829 TS5 - Backward Compatibility - API 800 SPT Edit Add Second Volume and Change It To The Boot Volume
    [Tags]  SP  TS5
    [Documentation]  Verify that a second volume can be added as new boot volume via API800
   Initialize Appliance For Test Case

    ${task}=  Add Server Profile Template  ${ts5_gen10_2_target_1_boot_volume_api800_spt}  api=800
    Wait For Task2  ${task}  timeout=600  interval=10

    ${spt}=  Get Resource  SPT:${PROFILE_TEMPLATE1_GEN10_NAME}  api=800
    Should Be True  ${spt['sanStorage']['volumeAttachments'][0]['isBootVolume']}

    Set to Dictionary  ${spt['sanStorage']['volumeAttachments'][0]}  isBootVolume=False
    ${my_vol}=  Copy Dictionary  ${ts5_gen10_2_target_1_boot_volume_api800_spt_add_volume}
    ${lookup}=  Common URI Lookup by Name  ${my_vol['volumeStorageSystemUri']}
    Set to Dictionary  ${my_vol}  volumeStorageSystemUri=${lookup}
    ${lookup}=  Common URI Lookup by Name  ${my_vol['volume']['properties']['storagePool']}
    Set to Dictionary  ${my_vol['volume']['properties']}  storagePool=${lookup}
    Lookup Volume Template Uri  ${my_vol}
    Append to List  ${spt['sanStorage']['volumeAttachments']}  ${my_vol}
    Remove From Dictionary  ${spt}  status_code  headers
    ${task} =    Fusion API Edit Server Profile Template   body=${spt}    uri=${spt['uri']}  api=800
    Wait For Task2  ${task}  timeout=600  interval=10

    ${spt}=  Get Resource  SPT:${PROFILE_TEMPLATE1_GEN10_NAME}  api=800
    :FOR  ${va}  IN  @{spt['sanStorage']['volumeAttachments']}
    \   Run Keyword If  ${va['id']} == 1  Should Not Be True  ${va['isBootVolume']}
    \   Run Keyword If  ${va['id']} == 2  Should Be True  ${va['isBootVolume']}

OVF4829 TS5 - Backward Compatibility - API 800 SPT 1 Boot, 1 Data volume
    [Tags]  SP  TS5
    [Documentation]  Verify 1 boot, 1 data volume SPT via API800
   Initialize Appliance For Test Case

    ${task}=  Add Server Profile Template  ${ts5_gen10_2_target_1_boot_volume_1_data_volume_api800_spt}  api=800
    Wait For Task2  ${task}  timeout=600  interval=10

    ${spt}=  Get Resource  SPT:${PROFILE_TEMPLATE1_GEN10_NAME}
    :FOR  ${vol}  IN  @{spt['sanStorage']['volumeAttachments']}
    \   Run Keyword If  ${vol['id']} == 1  Should Be Equal  ${vol['bootVolumePriority']}  Primary
    \   Run Keyword If  ${vol['id']} == 2  Should Be Equal  ${vol['bootVolumePriority']}  NotBootable

OVF4829 T6 - Edit SP Switching Primary and Secondary Volumes
    [Tags]  SP  TS6  OVD23741
    [Documentation]  Verify concurrent switch of primary and secondary boot volumes
    Initialize Appliance For Test Case

    ${task}=  Add Server Profile  ${ts1_gen10_2_target_2_boot_volume_sp}
    Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10

    ${sp}=  Get Resource  SP:${PROFILE1_GEN10_NAME}

    Gen10 SP Should Match Server RIS  ${sp}  ${ris_node_gen10}
    SP Settings Should Match Storage System  ${sp}

    :FOR  ${va}  IN  @{sp['sanStorage']['volumeAttachments']}
    \   Run Keyword If  ${va['id']} == 1  Set to Dictionary  ${va}  bootVolumePriority=Secondary
    \   Run Keyword If  ${va['id']} == 2  Set to Dictionary  ${va}  bootVolumePriority=Primary

    Remove From Dictionary  ${sp}  status_code  headers
    ${task} =    Fusion Api Edit Server Profile   body=${sp}    uri=${sp['uri']}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${sp}=  Get Resource  SP:${PROFILE1_GEN10_NAME}

    :FOR  ${va}  IN  @{sp['sanStorage']['volumeAttachments']}
    \   Run Keyword If  ${va['id']} == 1  Should Be Equal  ${va['bootVolumePriority']}  Secondary
    \   Run Keyword If  ${va['id']} == 2  Should Be Equal  ${va['bootVolumePriority']}  Primary

    Gen10 SP Should Match Server RIS  ${sp}  ${ris_node_gen10}
    SP Settings Should Match Storage System  ${sp}

OVF4829 T7 - Negative Test - 2 Boot Volumes Not Supported on iSCSI
    [Tags]  SP  TS7
    [Documentation]  2 boot volumes are not supported for iSCSI connections
   Initialize Appliance For Test Case

    ${task}=  Add Server Profile  ${ts7_2_target_2_boot_volumes_iscsi_sp}
    ${status}  ${return}=  Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10
    Run Keyword If  '${status}' == 'PASS'  Fail
    ${task_result}=  Get Resource  ${task['uri']}
    Should Be Equal  ${task_result['taskState']}  Error
    Should Be Equal  ${task_result['stateReason']}  ValidationError
    Should Be Equal  ${task_result['taskErrors'][0]['errorCode']}  MultipleBootVolumesNotAllowedForNonFC

OVF4829 T7 - Negative Test - 2 Boot Volumes Not Supported on API 800
    [Tags]  SP  TS7
    [Documentation]  2 boot volumes are not supported on API800
    Initialize Appliance For Test Case

    ${task}=  Add Server Profile  ${ts7_gen10_2_target_2_boot_volume_api800_sp}  api=800
    ${status}  ${return}=  Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10
    Run Keyword If  '${status}' == 'PASS'  Fail
    ${task_result}=  Get Resource  ${task['uri']}
    Should Be Equal  ${task_result['taskState']}  Error
    Should Be Equal  ${task_result['stateReason']}  ValidationError
    Should Be Equal  ${task_result['taskErrors'][0]['errorCode']}  MultipleBootVolumeModification

OVF4829 T7 - Negative Test - Secondary Boot Volume with missing Primary Boot Volume
    [Tags]  SP  TS7
    [Documentation]  Can't specify a SP with only a secondary boot volume
    Initialize Appliance For Test Case

    ${task}=  Add Server Profile  ${ts7_gen9_2_target_1_secondary_boot_volume_sp}
    ${status}  ${return}=  Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10
    Run Keyword If  '${status}' == 'PASS'  Fail
    ${task_result}=  Get Resource  ${task['uri']}
    Should Be Equal  ${task_result['taskState']}  Error
    Should Be Equal  ${task_result['stateReason']}  ValidationError
    Should Be Equal  ${task_result['taskErrors'][0]['errorCode']}  InvalidSecondaryBootVolumePriority

OVF4829 T7 - Negative Test - 2 Primary Boot Volumes
    [Tags]  SP  TS7
    [Documentation]  Can't specify a SP with 2 primary boot volumes
    Initialize Appliance For Test Case

    ${task}=  Add Server Profile  ${ts7_gen9_2_target_2_primary_boot_volumes_sp}
    ${status}  ${return}=  Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10
    Run Keyword If  '${status}' == 'PASS'  Fail
    ${task_result}=  Get Resource  ${task['uri']}
    Should Be Equal  ${task_result['taskState']}  Error
    Should Be Equal  ${task_result['stateReason']}  ValidationError
    Should Be Equal  ${task_result['taskErrors'][0]['errorCode']}  DuplicateBootVolumePriority

OVF4829 T7 - Negative Test - 2 Boot Volumes 1 Data Volume API 800 Change Data to Boot and Boot to Data
    [Tags]  SP  TS7
    [Documentation]  Can't do an API800 SP edit with multiple boot volumes specified
    Initialize Appliance For Test Case

    ${task}=  Add Server Profile  ${ts7_gen9_2_target_2_boot_volumes_1_data_volume_sp}
    Wait For Task2  ${task}  timeout=${SP_CREATE_TIMEOUT}  interval=10

    ${sp}=  Get Resource  SP:${PROFILE1_GEN9_NAME}  api=800

    :FOR  ${va}  IN  @{sp['sanStorage']['volumeAttachments']}
    \   Run Keyword If  ${va['id']} == 2  Set to Dictionary  ${va}  isBootVolume=False
    \   Run Keyword If  ${va['id']} == 3  Set to Dictionary  ${va}  isBootVolume=True

    Remove From Dictionary  ${sp}  status_code  headers
    ${task} =    Fusion Api Edit Server Profile   body=${sp}    uri=${sp['uri']}  api=800
    ${status}  ${return}=  Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=600  interval=10
    Run Keyword If  '${status}' == 'PASS'  Fail
    ${task_result}=  Get Resource  ${task['uri']}
    Should Be Equal  ${task_result['taskState']}  Error
    Should Be Equal  ${task_result['stateReason']}  ValidationError
    Should Be Equal  ${task_result['taskErrors'][0]['errorCode']}  MultipleBootVolumeModification

*** Keywords ***
Initialize the Variables and Log In as Administrator
    [Documentation]  Set the log level to TRACE, initialize the variables and, login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Initialize Appliance For Test Case
    [Documentation]  Initialize the appliance state
    Power Off Server  ${SERVER_GEN9}  powerControl=PressAndHold
    Power Off Server  ${SERVER_GEN10}  powerControl=PressAndHold
    ${task}=  Remove Server Profiles by Server Hardware  ${server_hardware_uris}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${spt}=  Create Dictionary  name=${PROFILE_TEMPLATE1_GEN9_NAME}
    Remove Server Profile Template If Exists  ${spt}
    ${spt}=  Create Dictionary  name=${PROFILE_TEMPLATE1_GEN10_NAME}
    Remove Server Profile Template If Exists  ${spt}

Add Fixed Volumes
    [Documentation]  Add the fixed volumes
    ${task}=  Add Storage Volumes Async  ${fixed_vols}
    Wait For Task2  ${task}  timeout=600  interval=5

Remove Fixed Volumes
    [Documentation]  Remove the fixed volumes
    ${task}=  Remove Storage Volumes Async  ${fixed_vols}  param=?suppressDeviceUpdates=false
    Wait For Task2  ${task}  timeout=600  interval=10

Remove Server Profile Template If Exists
    [Documentation]  Remove an existing SPT, otherwise just return
    [Arguments]  ${spt}
    ${status}  ${task} =  Run Keyword and Ignore Error  Remove Server Profile Template  ${spt}
    Run Keyword If  '${status}'=='PASS' and ${task['status_code']}!=404  Wait For Task2  ${task}  timeout=300  interval=2

Boot Connections
    [Documentation]  Given a SP, return the connections for Primary and Secondary boot
    [Arguments]  ${sp}
    ${pconn}=  Set Variable  ${None}
    ${sconn}=  Set Variable  ${None}
    :FOR  ${conn}  IN  @{sp['connectionSettings']['connections']}
    \   ${pconn}=  Set Variable If  '${conn['boot']['priority']}' == 'Primary'    ${conn}  ${pconn}
    \   ${sconn}=  Set Variable If  '${conn['boot']['priority']}' == 'Secondary'  ${conn}  ${sconn}
    [Return]  ${pconn}  ${sconn}

Boot Volume LUNs
    [Documentation]  Given a SP, return the LUNs for the Primary and Secondary boot volumes
    [Arguments]  ${sp}
    ${plun}=  Set Variable  ${None}
    ${slun}=  Set Variable  ${None}
    :FOR  ${va}  IN  @{sp['sanStorage']['volumeAttachments']}
    \   ${plun}=  Set Variable If  '${va['bootVolumePriority']}' == 'Primary'    ${va['lun']}  ${plun}
    \   ${slun}=  Set Variable If  '${va['bootVolumePriority']}' == 'Secondary'  ${va['lun']}  ${slun}
    [Return]  ${plun}  ${slun}

Get Connection by Boot Priority
    [Documentation]  Given a list of SP Connections, find the connection with the specified boot priority
    [Arguments]  ${connections}  ${bootPriority}
    :FOR  ${conn}  IN  @{connections}
    \   Return From Keyword If  '${conn['boot']['priority']}' == '${bootPriority}'  ${conn}
    [Return]  ${None}

Get SAN Storage System WWNs
    [Documentation]  Given a list of storage system ports, return a list for the given VSAN and protocal type
    [Arguments]  ${ssys_ports}  ${vsan}  ${protocol}
    @{ret}=  Create List
    :FOR  ${port}  IN  @{ssys_ports}
    \   Continue For Loop If  '${port['actualSanName']}' != '${vsan}' or '${port['protocolType']}' != '${protocol}'
    \   ${wwn}=  Normalize WWN  ${port['address']}
    \   Append To List  ${ret}  ${wwn}
    [Return]  @{ret}

Normalize WWN
    [Documentation]  Given a WWN string, normalize it to be all uppercase and remove all ':' separators
    [Arguments]  ${wwn}
    ${ret}=  Remove String  ${wwn}  :
    ${ret}=  Convert To Uppercase  ${ret}
    [Return]  ${ret}

Normalize RIS FC LUN
    [Documentation]  RIS FC Luns don't follow the normal convention, convert it if necessary
    [Arguments]  ${ris_lun}
    # There is a complex algorithm to convert the LUN in DesiredBootDevices to integer.  Since we should always be
    # creating LUN 1 with this server profile assume that LUN is 1 or 2 but do a sanity check vs. implementing the real
    # algorithm.  If this fails we'll need to invest the time to implement the real algorithm at
    # http://www.t10.org/ftp/t10/document.06/06-003r1.pdf
    Return From Keyword If  '${ris_lun}' == '1000000000000'  1
    Return From Keyword If  '${ris_lun}' == '2000000000000'  2
    [Return]  ${ris_lun}

WWNs Should Be Equal
    [Documentation]  compare 2 WWNs after normalizing them
    [Arguments]  ${wwn1}  ${wwn2}
    ${nwwn1}=  Normalize WWN  ${wwn1}
    ${nwwn2}=  Normalize WWN  ${wwn2}
    Should Be Equal  ${nwwn1}  ${nwwn2}

LUNs Should Be Equal
    [Documentation]  compare 2 LUNs after normalizing them
    [Arguments]  ${lun1}  ${lun2}
    ${nlun1}=  Normalize RIS FC LUN  ${lun1}
    ${nlun2}=  Normalize RIS FC LUN  ${lun2}
    Should Be Equal  ${nlun1}  ${nlun2}

SP Settings Should Match Storage System
    [Documentation]  Given a Server Profile, verify that the settings match the storage system
    [Arguments]  ${sp}
    ${plun}  ${slun}=  Boot Volume LUNs  ${sp}
    ${pconn}  ${sconn}=  Boot Connections  ${sp}
    ${ptarget1}=  Set Variable  ${pconn['boot']['targets'][0]}
    ${ptarget2}=  Set Variable  ${pconn['boot']['targets'][1]}
    ${starget1}=  Set Variable If  ${sconn} != ${None}  ${sconn['boot']['targets'][0]}  ${None}
    ${starget2}=  Set Variable If  ${sconn} != ${None}  ${sconn['boot']['targets'][1]}  ${None}
    # Collect values from the storage system
    ${ssys}=  Get Resource  ${sp['sanStorage']['volumeAttachments'][0]['volumeStorageSystemUri']}
    ${ssys_primary_WWNs}=  Get SAN Storage System WWNs  ${ssys['ports']}  ${FC_NETWORK_A_VSAN}  FC
    Length Should Be  ${ssys_primary_WWNs}  2
    ${ssys_secondary_WWNS}=  Run Keyword If  ${starget1} != ${None}  Get SAN Storage System WWNs  ${ssys['ports']}  ${FC_NETWORK_B_VSAN}  FC
    Run Keyword If  ${starget1} != ${None}  Length Should Be  ${ssys_secondary_WWNs}  2

    # Verify that the Server Profile primary targets reference WWNs associated with the storage system's primary connections
    ${ptarget_wwn1}=  Normalize WWN  ${ptarget1['arrayWwpn']}
    ${ptarget_wwn2}=  Normalize WWN  ${ptarget2['arrayWwpn']}
    List Should Contain Value  ${ssys_primary_WWNs}  ${ptarget_wwn1}
    List Should Contain Value  ${ssys_primary_WWNs}  ${ptarget_wwn1}

    # Verify that the Server Profile secondary targets reference WWNs associated with the storage system's secondary connections
    ${starget_wwn1}=  Run Keyword If  ${sconn} != ${None}  Normalize WWN  ${starget1['arrayWwpn']}
    ${starget_wwn2}=  Run Keyword If  ${sconn} != ${None}  Normalize WWN  ${starget2['arrayWwpn']}
    Run Keyword If  ${sconn} != ${None}  List Should Contain Value  ${ssys_secondary_WWNs}  ${starget_wwn1}
    Run Keyword If  ${sconn} != ${None}  List Should Contain Value  ${ssys_secondary_WWNs}  ${starget_wwn1}

Gen9 SP Should Match Server RIS
    [Documentation]  Given a Gen9 Server Profile with 2 connections and 2 boot volumes, verify that the settings match the server
    [Arguments]  ${sp}  ${server_ris_credentials}
    ${plun}  ${slun}=  Boot Volume LUNs  ${sp}
    ${pconn}  ${sconn}=  Boot Connections  ${sp}
    ${ptarget1}=  Set Variable  ${pconn['boot']['targets'][0]}
    ${ptarget2}=  Set Variable  ${pconn['boot']['targets'][1]}
    ${starget1}=  Set Variable  ${sconn['boot']['targets'][0]}
    ${starget2}=  Set Variable  ${sconn['boot']['targets'][1]}

    # Verify that the server is configured correctly
    # Gen9 servers only have 2 DesiredBootDevices entries, elements which are not common between the 2 are empty
    ${ris}=  Get RIS Node  ${server_ris_credentials}

    WWNs Should Be Equal  ${ptarget1['arrayWwpn']}  ${ris['DesiredBootDevices'][0]['Wwn']}
    Run Keyword If  '${ptarget1['lun']}' != '${ptarget2['lun']}'  Should Be Empty  ${ris['DesiredBootDevices'][0]['Lun']}
    Run Keyword If  '${ptarget1['lun']}' == '${ptarget2['lun']}'  Should Be Equal  ${ptarget1['lun']}  ${ris['DesiredBootDevices'][0]['Lun']}

    WWNs Should Be Equal  ${starget1['arrayWwpn']}  ${ris['DesiredBootDevices'][1]['Wwn']}
    Run Keyword If  '${starget1['lun']}' != '${starget2['lun']}'  Should Be Empty  ${ris['DesiredBootDevices'][1]['Lun']}
    Run Keyword If  '${starget1['lun']}' == '${starget2['lun']}'  Should Be Equal  ${starget1['lun']}  ${ris['DesiredBootDevices'][1]['Lun']}

Gen10 SP Should Match Server RIS
    [Documentation]  Given a Gen10 Server Profile with 2 connections and 2 boot volumes, verify that the settings match the server
    [Arguments]  ${sp}  ${server_ris_credentials}
    ${plun}  ${slun}=  Boot Volume LUNs  ${sp}
    ${pconn}  ${sconn}=  Boot Connections  ${sp}
    ${ptarget1}=  Set Variable  ${pconn['boot']['targets'][0]}
    ${ptarget2}=  Set Variable  ${pconn['boot']['targets'][1]}
    ${starget1}=  Set Variable  ${sconn['boot']['targets'][0]}
    ${starget2}=  Set Variable  ${sconn['boot']['targets'][1]}

    ${ris}=  Get RIS Node  ${server_ris_credentials}

    # Verify first boot entry is Primary connection to the Primary boot volume
    WWNs Should Be Equal  ${ptarget1['arrayWwpn']}  ${ris['DesiredBootDevices'][0]['Wwn']}
    LUNs Should Be Equal  ${plun}  ${ris['DesiredBootDevices'][0]['Lun']}
    LUNs Should Be Equal  ${ptarget1['lun']}  ${ris['DesiredBootDevices'][0]['Lun']}

    # Verify second boot entry is Secondary connection to the Primary boot volume
    WWNs Should Be Equal  ${starget1['arrayWwpn']}  ${ris['DesiredBootDevices'][1]['Wwn']}
    LUNs Should Be Equal  ${plun}  ${ris['DesiredBootDevices'][1]['Lun']}
    LUNs Should Be Equal  ${starget1['lun']}  ${ris['DesiredBootDevices'][1]['Lun']}

    # Verify third boot entry is Primary connection to the Secondary boot volume
    WWNs Should Be Equal  ${ptarget2['arrayWwpn']}  ${ris['DesiredBootDevices'][2]['Wwn']}
    LUNs Should Be Equal  ${slun}  ${ris['DesiredBootDevices'][2]['Lun']}
    LUNs Should Be Equal  ${ptarget2['lun']}  ${ris['DesiredBootDevices'][2]['Lun']}

    # Verify fourth boot entry is Secondary connection to the Secondary boot volume
    WWNs Should Be Equal  ${starget2['arrayWwpn']}  ${ris['DesiredBootDevices'][3]['Wwn']}
    LUNs Should Be Equal  ${slun}  ${ris['DesiredBootDevices'][3]['Lun']}
    LUNs Should Be Equal  ${starget2['lun']}  ${ris['DesiredBootDevices'][3]['Lun']}

Initialized Target Port Usage
    [Documentation]  Initialize a dictionary of target port WWPNs to track usage counts
    [Arguments]  ${ssys_URI}
    ${target_port_usage}=  Create Dictionary
    ${ssys}=  Get Resource  ${ssys_URI}
    ${ssys_port_WWPNs}=  Get SAN Storage System WWNs  ${ssys['ports']}  ${FC_NETWORK_A_VSAN}  FC
    :FOR  ${wwpn}  IN  @{ssys_port_WWPNs}
    \   ${nwwpn}=  Normalize WWN  ${wwpn}
    \   Set to Dictionary  ${target_port_usage}  ${nwwpn}=0
    ${ssys_port_WWPNs}=  Get SAN Storage System WWNs  ${ssys['ports']}  ${FC_NETWORK_B_VSAN}  FC
    :FOR  ${wwpn}  IN  @{ssys_port_WWPNs}
    \   ${nwwpn}=  Normalize WWN  ${wwpn}
    \   Set to Dictionary  ${target_port_usage}  ${nwwpn}=0
    [Return]  ${target_port_usage}


Increment Target Port Usage
    [Documentation]  Increment usage count for a specified WWPN in a WWPN dictionary
    [Arguments]  ${target_wwpns}  ${wwpn}
    ${nwwpn}=  Normalize WWN  ${wwpn}
    ${references}=  Get from Dictionary  ${target_wwpns}  ${nwwpn}
    ${references}=  Evaluate  ${references} + 1
    Set to Dictionary  ${target_wwpns}  ${nwwpn}=${references}
