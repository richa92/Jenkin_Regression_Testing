*** Settings ***
Documentation                   OVF3218 FC boot 2 targets: c7000 Gen9/Gen10 FC HBA

Library             FusionLibrary
Library             BuiltIn
Library             Collections

Resource            ../global_variables.robot
Resource            ./../../../../Resources/api/fusion_api_resource.txt

Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Initialize the Variables and Log In as Administrator
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
Suite Teardown      Run Keywords    Initialize Appliance For Test Case
...                 AND     Fusion Api Logout Appliance

*** Variables ***

*** Test Cases ***

OVF3218 TC1 - Create and Verify Gen9 UEFI 2 target FC Boot Profile
    [Tags]  SP  TC1
    [Documentation]  Create 2 connection, 2 targets per connection UEFI server profile, verify both RIS and CLP
    Initialize Appliance For Test Case

    ${my_sp} =  Copy Dictionary  ${simplified_UEFI_FC_2x_boot_from_managed_SAN_storage_volume}
    Set to Dictionary  ${my_sp}  serverHardwareUri=${GEN9_SH}
    ${resp_list} =  Add Server Profile  ${my_sp}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

    ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}=  Get Targets  ${PROFILE1_UEFI_NAME}

    Server Profile Target WWPNs Should Match Storage System WWPNs  ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}

    # Verify that the server is configured correctly
    # Gen9 servers only have 2 DesiredBootDevices entries, elements which are not common between the 2 are empty
    ${ris}=  Get RIS Node  ${gen9_ris_node}

    Should Be Empty  ${ris['DesiredBootDevices'][0]['Wwn']}
    ${nrislun}=  Normalize RIS FC LUN  ${ris['DesiredBootDevices'][0]['Lun']}
    Should Be Equal  ${ptarget1['lun']}        ${nrislun}

    Should Be Empty  ${ris['DesiredBootDevices'][1]['Wwn']}
    ${nrislun}=  Normalize RIS FC LUN  ${ris['DesiredBootDevices'][0]['Lun']}
    Should Be Equal  ${starget1['lun']}        ${nrislun}

    OA CLI Verify Blade CLP  ${gen9_2target_clp}

OVF3218 TC2 - Create and Verify Gen9 BIOS 2 target FC Boot Profile
    [Tags]  SP  TC2
    [Documentation]  Create 2 connection, 2 targets per connection legacy BIOS server profile, verify both iLO CQHORD EV and CLP
    Initialize Appliance For Test Case

    ${my_sp} =  Copy Dictionary  ${simplified_BIOS_FC_2x_boot_from_managed_SAN_storage_volume}
    Set to Dictionary  ${my_sp}  serverHardwareUri=${GEN9_SH}
    ${resp_list} =  Add Server Profile  ${my_sp}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

    # have to power on server and go through this set of POST states to get to final server state with valid boot info When in legacy BIOS mode
    Power on Server  ${my_sp['serverHardwareUri']}
    Wait for Server to reach POST State  ${my_sp['serverHardwareUri']}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s
    Wait for Server to reach POST State  ${my_sp['serverHardwareUri']}  post_state=IN_POST  timeout=15m  interval=10s
    Wait for Server to reach POST State  ${my_sp['serverHardwareUri']}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

    ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}=  Get Targets  ${PROFILE1_BIOS_NAME}

    Server Profile Target WWPNs Should Match Storage System WWPNs  ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}

    # Verify that the server is configured correctly
    ${server_ip}=  Get Server Hardware iLO IP  ${GEN9_SH}
    ${cqhord}=  Run cpqlocfg and Get CQHORD  ${server_ip}
    ${bco}=  get ilo legacy bios boot controller order  ${cqhord}
    ${bco_0}=  Get From List  ${bco}  0
    ${vid}=  Get From Dictionary  ${bco_0}  vendor_id
    ${did}=  Get From Dictionary  ${bco_0}  device_id
    ${slot}=  Get From Dictionary  ${bco_0}  slot
    Should Be Equal  ${vid}  ${HP_PCI_VENDOR_ID}  Non-HP device found for first boot option
    List Should Contain Value  ${VALID_GEN9_FC_PCI_DEVICE_IDS}  ${did}  Non-FC device found for first boot option
    Should Be Equal  ${slot}  ${GEN9_FC_DEVICE_MEZZ_SLOT}  Incorrect slot for first boot option

    OA CLI Verify Blade CLP  ${gen9_2target_clp}

OVF3218 TC3 - Create and Verify Gen9 UEFI 1 target FC Boot Profile
    [Documentation]  While this is not a 2 target boot, changes to 2 target boot management on the iLO necessitated changing 1 target as well
    [Tags]  SP  TC3
    Initialize Appliance For Test Case

    ${my_sp} =  Copy Dictionary  ${simplified_UEFI_FC_1x_boot_from_managed_SAN_storage_volume}
    Set to Dictionary  ${my_sp}  serverHardwareUri=${GEN9_SH}
    ${resp_list} =  Add Server Profile  ${my_sp}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

    ${sp}=  Get Resource  SP:${PROFILE1_UEFI_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    ${pconn}=  Get Connection by Boot Priority  ${sp["connectionSettings"]["connections"]}  Primary
    ${ptarget1}=  Set Variable  ${pconn['boot']['targets'][0]}
    ${ptarget2}=  Set Variable  ${pconn['boot']['targets'][1]}

    # Collect values from the storage system
    ${ssys}=  Get Resource  ${sp['sanStorage']['volumeAttachments'][0]['volumeStorageSystemUri']}
    ${ssys_WWNs}=  Get SAN Storage System WWNs  ${ssys['ports']}  ${FC_NETWORK_A_VSAN}  FC
    Length Should Be  ${ssys_WWNs}  2

    # Verify that the Server Profile primary targets reference WWNs associated with the storage system's primary connections
    ${ptarget_wwn1}=  Normalize WWN  ${ptarget1['arrayWwpn']}
    ${ptarget_wwn2}=  Normalize WWN  ${ptarget2['arrayWwpn']}
    Should Not Be Equal  ${ptarget_wwn1}  ${ptarget_wwn2}
    List Should Contain Value  ${ssys_WWNs}  ${ptarget_wwn1}
    List Should Contain Value  ${ssys_WWNs}  ${ptarget_wwn1}

    ${ris}=  Get RIS Node  ${gen9_ris_node}

    Should Be Equal  ${ptarget1['arrayWwpn']}  ${ris['DesiredBootDevices'][0]['Wwn']}
    ${nrislun}=  Normalize RIS FC LUN  ${ris['DesiredBootDevices'][0]['Lun']}
    Should Be Equal  ${ptarget1['lun']}        ${nrislun}

    Should Be Equal  ${ptarget2['arrayWwpn']}  ${ris['DesiredBootDevices'][1]['Wwn']}
    ${nrislun}=  Normalize RIS FC LUN  ${ris['DesiredBootDevices'][1]['Lun']}
    Should Be Equal  ${ptarget2['lun']}        ${nrislun}

    OA CLI Verify Blade CLP  ${gen9_1target_clp}

OVF3218 TC4 - Create and Verify Gen10 UEFI 2 target FC Boot Profile
    [Tags]  SP  TC4
    [Documentation]  Create 2 connection, 2 targets per connection UEFI server profile, verify both RIS and CLP
   Initialize Appliance For Test Case

    ${my_sp} =  Copy Dictionary  ${simplified_UEFI_FC_2x_boot_from_managed_SAN_storage_volume}
    Set to Dictionary  ${my_sp}  serverHardwareUri=${GEN10_SH}
    ${resp_list} =  Add Server Profile  ${my_sp}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

    ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}=  Get Targets  ${PROFILE1_UEFI_NAME}

    Server Profile Target WWPNs Should Match Storage System WWPNs  ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}

    # Verify that the server is configured correctly
    ${ris}=  Get RIS Node  ${gen10_ris_node}

    WWNs Should Be Equal  ${ptarget1['arrayWwpn']}  ${ris['DesiredBootDevices'][0]['Wwn']}
    ${nrislun}=  Normalize RIS FC LUN  ${ris['DesiredBootDevices'][0]['Lun']}
    Should Be Equal  ${ptarget1['lun']}        ${nrislun}

    WWNs Should Be Equal  ${starget1['arrayWwpn']}  ${ris['DesiredBootDevices'][1]['Wwn']}
    ${nrislun}=  Normalize RIS FC LUN  ${ris['DesiredBootDevices'][1]['Lun']}
    Should Be Equal  ${starget1['lun']}        ${nrislun}

    WWNs Should Be Equal  ${ptarget2['arrayWwpn']}  ${ris['DesiredBootDevices'][2]['Wwn']}
    ${nrislun}=  Normalize RIS FC LUN  ${ris['DesiredBootDevices'][2]['Lun']}
    Should Be Equal  ${ptarget2['lun']}        ${nrislun}

    WWNs Should Be Equal  ${starget2['arrayWwpn']}  ${ris['DesiredBootDevices'][3]['Wwn']}
    ${nrislun}=  Normalize RIS FC LUN  ${ris['DesiredBootDevices'][3]['Lun']}
    Should Be Equal  ${starget2['lun']}        ${nrislun}

    OA CLI Verify Blade CLP  ${gen10_clp}

OVF3218 TC5 - Create and Verify Gen10 BIOS 2 target FC Boot Profile
    [Tags]  SP  TC5
    [Documentation]  Create 2 connection, 2 targets per connection legacy BIOS server profile, verify both iLO CQHORD EV and CLP
    Initialize Appliance For Test Case

    ${my_sp} =  Copy Dictionary  ${simplified_BIOS_FC_2x_boot_from_managed_SAN_storage_volume}
    Set to Dictionary  ${my_sp}  serverHardwareUri=${GEN10_SH}
    ${resp_list} =  Add Server Profile  ${my_sp}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

    # have to power on server and go through this set of POST states to get to final server state with valid boot info When in legacy BIOS mode
    Power on Server  ${my_sp['serverHardwareUri']}
    Wait for Server to reach POST State  ${my_sp['serverHardwareUri']}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s
    Wait for Server to reach POST State  ${my_sp['serverHardwareUri']}  post_state=IN_POST  timeout=15m  interval=10s
    Wait for Server to reach POST State  ${my_sp['serverHardwareUri']}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

    ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}=  Get Targets  ${PROFILE1_BIOS_NAME}

    Server Profile Target WWPNs Should Match Storage System WWPNs  ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}

    # Verify that the server is configured correctly
    ${server_ip}=  Get Server Hardware iLO IP  ${GEN10_SH}
    ${cqhord}=  Run cpqlocfg and Get CQHORD  ${server_ip}
    ${bco}=  get ilo legacy bios boot controller order  ${cqhord}
    ${bco_0}=  Get From List  ${bco}  0
    ${vid}=  Get From Dictionary  ${bco_0}  vendor_id
    ${did}=  Get From Dictionary  ${bco_0}  device_id
    ${slot}=  Get From Dictionary  ${bco_0}  slot
    Should Be Equal  ${vid}  ${HP_PCI_VENDOR_ID}  Non-HP device found for first boot option
    List Should Contain Value  ${VALID_GEN10_FC_PCI_DEVICE_IDS}  ${did}  Non-FC device found for first boot option
    Should Be Equal  ${slot}  ${GEN10_FC_DEVICE_MEZZ_SLOT}  Incorrect slot for first boot option

    OA CLI Verify Blade CLP  ${gen10_clp}

OVF3218 TC5 - Create and Verify Gen8 BIOS 2 target FC Boot Profile
    [Tags]  SP  TC5
    [Documentation]  Negative test, Gen8 should not support 2 targets per connection server profile
    Initialize Appliance For Test Case

    ${my_sp} =  Copy Dictionary  ${simplified_BIOS_FC_2x_boot_from_managed_SAN_storage_volume}
    Set to Dictionary  ${my_sp}  serverHardwareUri=${GEN8_SH}
    ${task} =  Add Server Profile  ${my_sp}
    ${status}  ${return}=  Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=3600  interval=10
    Run Keyword If  '${status}' == 'PASS'  Fail
    ${task_result}=  Get Resource  ${task['uri']}
    Should Be Equal  ${task_result['taskState']}  Error
    Should Be Equal  ${task_result['stateReason']}  ValidationError
    Should Be Equal  ${task_result['taskErrors'][0]['errorCode']}  UnsupportedBootMode

*** Keywords ***
Initialize the Variables and Log In as Administrator
    [Documentation]  Set the log level to TRACE, initialize the variables and, login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Initialize Appliance For Test Case
    [Documentation]  Initialize the appliance state
    Power Off Server  ${GEN8_SH}  powerControl=PressAndHold
    Power Off Server  ${GEN9_SH}  powerControl=PressAndHold
    Power Off Server  ${GEN10_SH}  powerControl=PressAndHold
    ${task}=  Remove Server Profiles by Server Hardware  ${server_hardware_uris}
    Wait For Task2  ${task}  timeout=600  interval=10

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

WWNs Should Be Equal
    [Documentation]  compare 2 WWNs after normalizing them
    [Arguments]  ${wwn1}  ${wwn2}
    ${nwwn1}=  Normalize WWN  ${wwn1}
    ${nwwn2}=  Normalize WWN  ${wwn2}
    Should Be Equal  ${nwwn1}  ${nwwn2}

Get Targets
    [Documentation]  Given a SP, return primary and secondary targets for 2 targets per connection
    [Arguments]  ${spName}
    ${sp}=  Get Resource  SP:${spName}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    ${pconn}=  Get Connection by Boot Priority  ${sp["connectionSettings"]["connections"]}  Primary
    ${ptarget1}=  Set Variable  ${pconn['boot']['targets'][0]}
    ${ptarget2}=  Set Variable  ${pconn['boot']['targets'][1]}
    ${sconn}=  Get Connection by Boot Priority  ${sp["connectionSettings"]["connections"]}  Secondary
    ${starget1}=  Set Variable  ${sconn['boot']['targets'][0]}
    ${starget2}=  Set Variable  ${sconn['boot']['targets'][1]}
    [Return]  ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}

Server Profile Target WWPNs Should Match Storage System WWPNs
    [Documentation]  Given a Server Profile, verify that the settings match the storage system
    [Arguments]  ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}
    # Collect values from the storage system
    ${ssys}=  Get Resource  ${sp['sanStorage']['volumeAttachments'][0]['volumeStorageSystemUri']}
    ${ssys_primary_WWNs}=  Get SAN Storage System WWNs  ${ssys['ports']}  ${FC_NETWORK_A_VSAN}  FC
    Length Should Be  ${ssys_primary_WWNs}  2
    ${ssys_secondary_WWNS}=  Get SAN Storage System WWNs  ${ssys['ports']}  ${FC_NETWORK_B_VSAN}  FC
    Length Should Be  ${ssys_secondary_WWNs}  2

    # Verify that the Server Profile primary targets reference WWNs associated with the storage system's primary connections
    ${ptarget_wwn1}=  Normalize WWN  ${ptarget1['arrayWwpn']}
    ${ptarget_wwn2}=  Normalize WWN  ${ptarget2['arrayWwpn']}
    Should Not Be Equal  ${ptarget_wwn1}  ${ptarget_wwn2}
    List Should Contain Value  ${ssys_primary_WWNs}  ${ptarget_wwn1}
    List Should Contain Value  ${ssys_primary_WWNs}  ${ptarget_wwn1}

    # Verify that the Server Profile secondary targets reference WWNs associated with the storage system's secondary connections
    ${starget_wwn1}=  Normalize WWN  ${starget1['arrayWwpn']}
    ${starget_wwn2}=  Normalize WWN  ${starget2['arrayWwpn']}
    Should Not Be Equal  ${starget_wwn1}  ${starget_wwn2}
    List Should Contain Value  ${ssys_secondary_WWNs}  ${starget_wwn1}
    List Should Contain Value  ${ssys_secondary_WWNs}  ${starget_wwn1}

Normalize RIS FC LUN
    [Documentation]  RIS FC Luns don't follow the normal convention, convert it
    [Arguments]  ${ris_lun}
    # There is a complex algorithm to convert the LUN in DesiredBootDevices to integer.  Since we should always be
    # creating LUN 1 with this server profile assume that LUN is 1 but do a sanity check vs. implementing the real
    # algorithm.  If this fails we'll need to invest the time to implement the real algorithm at
    # http://www.t10.org/ftp/t10/document.06/06-003r1.pdf
    Should Be Equal  ${ris_lun}  1000000000000
    [Return]  1
