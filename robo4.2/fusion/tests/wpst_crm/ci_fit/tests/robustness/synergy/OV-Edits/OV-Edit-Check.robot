*** Settings ***
Documentation       OV-Edit-Check.robot - performs Appliance pre-check to ensure that the components are in a Configured state. Edits different components in an appliance with resources found in supplied data file and performs post-check for the OV setup to ensure that they return to the expected state
...     TAGS:          CREATE_BACKUP, EDIT_ALL, TOGGLE_UPLINK, TOGGLE_DOWNLINK, REAPPLY_LI, UFG, REAPPLY_LE, OV_DUMP, LE_DUMP, POWERON_EDIT, POWEROFF_SERVERS1, POWEROFF_SERVERS2, UNASSIGN_SERVERS, ASSIGN_SERVERS, POWEROFF_CONNECTION_EDIT, POWEROFF_CONNECTION_DELETE, APP_BACKUP
...                 EDIT_ALL          - Run all tags
...                 POWEROFF_SERVERS1 - Power off the specified servers then unassign server profiles to server hardware
...                 POWEROFF_SERVERS2 - Power off the specified servers then assign server profiles to server hardware
...                 SERVER_CHECK      - Perform the pre-checks for enc,LE,LI,IC and for servers
...                 Example Workflow :
...                               pybot -T -d /tmp/logs/OV-Edits -LTRACE -V /root/ci-fit/config_files/OV-Edit_data_variables.py -V /root/ci-fit/config_files/max_vlan_data_variables_robustness_cl10.py -v Appliance_IP:15.186.X.XX  OV-Edit-Check.robot
...                 Required argument:
...                         -V /root/ci-fit/config_files/OV-Edit_data_variables.py
...                         -V /root/ci-fit/config_files/max_vlan_data_variables_robustness_cl10.py
...                         To proceed with PressAndHold when MomentaryPress fails with this errorCode, use -vPROCEED_WITH_PRESS_AND_HOLD:SERVER_MOMENTARY_PRESS_OFF_TIMEOUT
...                         To disable checking of etherchannel summary, use -vCHECK_ETH_SUMMARY:False
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         To disable bonding multi test, use -vDISABLE_BONDING_MULTI_TEST:True
...                         To Perform bonding multi test HA_FILE is required, use -v HA_FILE:/path/to/your/ha_file.conf
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                         To test for Nitro (if not specified it will try to find what you have in OneView), use -vHAFNIUM_MODEL:'Virtual Connect SE 100Gb F32 Module for Synergy'
...                         REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>

Variables           ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Library             ../../resources/robustness-helper.py
Library             Process

Suite Setup         Authenticate And Set Login

***Variables***
${FUSION_IP}                      ${APPLIANCE_IP}
${LE_uri}                         /rest/logical-enclosures/
${tbirdEnv}                       True
${LE_dump_file}                   ${LE_dump_file_Dir}/ci_dfrm_supportdump.sdmp
${LE_dump_file_Dir}               DataFiles/LE_support_dump
${OV_support_dump_file}           ${OV_dump_file_Dir}/ci_dfrm_decrypted_supportdump.sdmp
${OV_dump_file_Dir}               DataFiles/OV_support_dump
${dataFilesDir}                   DataFiles/APP_BACKUP
${backupFile}                     ${dataFilesDir}/backup-restore-test.bkp
${EG}                             None
${PROCEED_WITH_PRESS_AND_HOLD}    None
${DISABLE_BONDING_MULTI_TEST}     False
${UPDATE_LFCCACHE}                False
${CHECK_ETH_SUMMARY}              True
${HA_FILE}                        None
${SERVER_BONDING_CHECKS}          None
${STOP_SCRIPT}                    /root/.stop_script
${HAFNIUM_MODEL}                  ${Null}
${TCS_HAFNIUM_SSH_INTERFACE}      eth0
${REMOTE_CHECKS_TAG}            -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}         &{EMPTY}
@{REMOTE_RUN_CHECKS}              @{EMPTY}

***Test cases***

TC1 Perform the pre-checks before proceeding to edit scenarios
    [Documentation]   Pre-checks the status of Enclosure,LE,IC,LI and server's MG,Multipath,Sequential_ping,Readonly,ISS crash,Fping loss
    [Tags]     EDIT_ALL   CREATE_BACKUP   TOGGLE_UPLINK   TOGGLE_DOWNLINK   REAPPLY_LI   UFG   REAPPLY_LE   OV_DUMP   LE_DUMP   POWERON_EDIT   POWEROFF_SERVERS2   ASSIGN_SERVERS   APP_BACKUP   SERVER_CHECK
    ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    Return From Keyword If   "${returnStatus}" == "PASS"
    Log  \n Performing the pre-checks before proceeding to ov-edits   console=${True}
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache
    Server check

TC2 create backup of the Appliance
    [Documentation]   creates backup of the appliance
    [Tags]    CREATE_BACKUP   EDIT_ALL
	common.Create Appliance Backup Download And Data Compare    ${WAIT_FOR_TASK_WAIT_TIME}   ${WAIT_FOR_TASK_INTERVAL}
    Sleep And Log Reason To Console   ${BACKUP_DOWNLOAD_SLEEP}   reason=Sleeping for ${BACKUP_DOWNLOAD_SLEEP} to complete the backup download process...
    Server check

TC3 Toggle Uplink Ports in Interconnects
    [Documentation]   Disable/enable uplink port
    [Tags]    UPLINK   EDIT_ALL
    ${ICM_len} =   Get Length   ${ICM_NAMES}
    :FOR   ${x}   IN RANGE   0    ${ICM_len}
	\    ${IC_uri} =    Get IC URI    ${ICM_NAMES[${x}]}
    \    ${Resp} =   Get IC Port    ${IC_uri}    ${UPLINK_PORT_NAME[${x}]}
    \    Set to Dictionary   ${Resp}   enabled    False
    \    Log   \n Disabling Uplink ${UPLINK_PORT_NAME[${x}]} of interconnect ${ICM_NAMES[${x}]}\n   console=${True}
    \    ${Return}    Toggle Uplink Ports And Check For Error    ${ICM_NAMES[${x}]}    ${UPLINK_PORT_NAME[${x}]}    ${Resp}
	\    Log   \n Enabling Uplink ${UPLINK_PORT_NAME[${x}]} of interconnect ${ICM_NAMES[${x}]}\n   console=${True}
	\    Set to Dictionary   ${Resp}   enabled    True
	\    Toggle Uplink Ports And Check For Error    ${ICM_NAMES[${x}]}    ${UPLINK_PORT_NAME[${x}]}    ${Resp}
    \    Sleep And Log Reason To Console   ${TOGGLE_INTERCONNECT_PORT_SLEEP}   reason=Sleeping for ${TOGGLE_INTERCONNECT_PORT_SLEEP} to let things settle after toggling uplink ports...
	\    Log   \n Performing the Server check after completion of uplink port toggle...    console=${True}
    \    Server check

TC4 Toggle Downlink Ports in Interconnects
    [Documentation]   Disable/enable uplink port
    [Tags]    DOWNLINK   EDIT_ALL
    ${ICM_len} =   Get Length   ${ICM_NAMES}
    :FOR   ${x}   IN RANGE   0    ${ICM_len}
	\    ${IC_uri} =    Get IC URI    ${ICM_NAMES[${x}]}
    \    ${Resp} =   Get IC Port    ${IC_uri}    ${DOWNLINK_PORT_NAME[${x}]}
    \    Set to Dictionary   ${Resp}   enabled    False
    \    Log   \n Disabling Downlink ${DOWNLINK_PORT_NAME[${x}]} of interconnect ${ICM_NAMES[${x}]}\n   console=${True}
    \    Toggle Uplink Ports And Check For Error    ${ICM_NAMES[${x}]}    ${DOWNLINK_PORT_NAME[${x}]}    ${Resp}
	\    Log   \n Enabling Downlink ${DOWNLINK_PORT_NAME[${x}]} of interconnect ${ICM_NAMES[${x}]}\n   console=${True}
	\    Set to Dictionary   ${Resp}   enabled    True
	\    Toggle Uplink Ports And Check For Error    ${ICM_NAMES[${x}]}    ${DOWNLINK_PORT_NAME[${x}]}    ${Resp}
    \    Sleep And Log Reason To Console   ${TOGGLE_INTERCONNECT_PORT_SLEEP}   reason=Sleeping for ${TOGGLE_INTERCONNECT_PORT_SLEEP} to let things settle after toggling downlink ports...
	\    Log   \n Performing the Server check after completion of Downlink port toggle...    console=${True}
    Server check

TC5 Reapply config in LI
    [Documentation]   re-applies the configuration to Logical interconnect
    [Tags]    REAPPLY_LI   EDIT_ALL
	Run Keyword If  ${LI} is not ${null}    common.Reapply config in Logical Interconnect   ${LI}
    Log  Performing the Server check after completion of downlink port toggle...   console=${True}
    Server check

TC6 Delete Uplink sets from LI and Perform Update from group
    [Documentation]   Performs deletion of uplinkset in LI and Update from group
    [Tags]    UFG   EDIT_ALL
	${ICM_NAME} =   Get Dictionary Keys    ${INTERCONNECTS}
    ${uplink_len} =   Get Length   ${DELETE_UPLINKSET_NAME}
    :FOR   ${x}   IN RANGE   0   ${uplink_len}
	\    Run Keyword If  ${DELETE_UPLINKSET_NAME} is not ${null}    common.Delete Uplink Set   ${DELETE_UPLINKSET_NAME[${x}]}   ${ICM_NAME} 
	Run Keyword If  ${LI} is not ${null}    common.Update from group in LI   ${LI}   wait_task_timeout=${UPDATE_FROM_GROUP_WAIT_TIME}   wait_task_interval=${UPDATE_FROM_GROUP_WAIT_INTERVAL}
    Log   \n Performing the Server check after completion of UFG in LI   console=${True}
    Server check

TC7 Reapply config in LE
    [Documentation]   re-applies the configuration to Logical interconnect
    [Tags]    REAPPLY_LE   EDIT_ALL
    Run Keyword If  ${LE} is not ${null}    common.Reapply config in Logical Enclosure   ${LE}
	Log   \n Performing the Server check after completion of LE Reapply...   console=${True}
    Server check

TC8 Creating OV support dump
    [Documentation]   creates support dump for OV
    [Tags]   OV_DUMP   EDIT_ALL
    common.Create OV Support Dump And Download
    Sleep And Log Reason To Console   ${OV_SUPPORT_DUMP_SLEEP}   reason=Sleeping for ${OV_SUPPORT_DUMP_SLEEP} to let things settle after OV dump download process...
    Log   \n Performing the Server check after creating the OV support dump scenario    console=${True}
    Server check

TC9 Create support dump for LE
    [Documentation]    create support dump for LE
    [Tags]    LE_DUMP 	EDIT_ALL
    common.Create LE Support Dump And Download   ${LE}
    Sleep And Log Reason To Console   ${LE_SUPPORT_DUMP_SLEEP}   reason=Sleeping for ${LE_SUPPORT_DUMP_SLEEP} to let things settle after OV dump download process...
    Log   \n Performing the Server check after creating the LE support dump scenario    console=${True}
    Server check

TC10 Server poweron edit negative scenarios
    [Documentation]   Editing server profile while server is in poweron mode
    [Tags]   POWERON_EDIT1   EDIT_ALL
    ${Server_items}=    Get Dictionary Items    ${SERVER_PROFILE_ONLINE_OFFLINE_EDIT}
    :FOR  ${profile}  ${hardware}    IN  @{Server_items}
	\   ${HW} =   Fusion Api Get Server Hardware  param=?filter="name='${hardware}'"
    \   Should Be Equal   ${HW['total']}   ${1}   msg=Response body total is not as expected.
	\   ${Serverhw_uri}=    Set Variable      ${HW['members'][0]['uri']}
    \   common.Power On Server Uri   ${Serverhw_uri}
    \   ${resp} =   Fusion Api Get Server Profiles   param=?filter="'name'=='${profile}'"
    \   Should Be Equal   ${resp['total']}   ${1}   msg=Response body total is not as expected.
    \   ${sp_uri} =   Set Variable   ${resp['members'][0]['uri']}
    \   ${profile} =   Fusion Api Get Resource   uri=${sp_uri}
    \   Set To Dictionary   ${profile['connectionSettings']['connections'][0]}   portId   None
    \   set to dictionary   ${profile}   serverHardwareUri=${None}
    \   set to dictionary   ${profile}   enclosureBay=${None}
    \   set to dictionary   ${profile}   enclosureUri=${None}
    \   Remove From Dictionary   ${profile}   status_code   headers
    \   ${resp} =   Fusion Api Edit Server Profile   uri=${sp_uri}   body=${profile}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${WAIT_FOR_TASK_WAIT_TIME}   interval=${WAIT_FOR_TASK_INTERVAL}
    \   ${error_message} =   Get From dictionary   ${task['taskErrors'][0]}   errorCode
    \   Should Match Regexp   ${error_message}   ((?i)ServerNotOffProfileEdit|ServerNotOffUnassigningGen9AndNewer|ProfileEditNotAllowedServerPoweredOnError)
    Log   Performing the Server check After completion of POWERON_EDIT scenario...    console=${True}
    Server check

TC11a Power Off Servers
    [Documentation]   Query OneView for list of profiles then Power Off Servers from server hardware.
    [Tags]  POWEROFF_SERVERS1   POWEROFF_SERVERS2   EDIT_ALL
    ${HARDWARE_NAMES}   Create List
    ${HARDWARE_NAMES}   Get Dictionary Values  ${SERVER_PROFILE_TO_BAY_MAP}
    :FOR   ${p}   IN   @{HARDWARE_NAMES}
	\   ${profiles} =    Run Keyword If   '${p}' != '${None}'   Fusion Api Get Server Hardware  param=?filter="name='${p}'"
	\   ...   ELSE    Continue For Loop
    \   Should Be Equal   ${profiles['total']}   ${1}   msg=Response body total is not as expected.
	\   ${Serverhw_uri}=    Set Variable      ${profiles['members'][0]['uri']}
    \   common.Power Off Server Uri   ${Serverhw_uri}   proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}
    Log  \n Poweredoff successfully   console=${True}

TC11b UnAssign Server Hardware From Profile
    [Documentation]   Query OneView for list of profiles then Unassign server profiles from server hardware.
    [Tags]  UNASSIGN_SERVERS1  POWEROFF_SERVERS1    EDIT_ALL
	${PROFILE_NAMES}   Create List
	${PROFILE_NAMES}   Get Dictionary Keys    ${SERVER_PROFILE_TO_BAY_MAP}
    ${Profileunassign} =   Create List
    :FOR    ${profile}  IN  @{PROFILE_NAMES}
	\    ${profile_resp} =    Run Keyword If  "${SERVER_PROFILE_TO_BAY_MAP['${profile}']}" != "${null}"   Fusion Api Get Server Profiles   param=?filter="'name'=='${profile}'"
	\   ...   ELSE    Continue For Loop
    \   Should Be Equal   ${profile_resp['total']}   ${1}   msg=Response body total is not as expected.
	\   ${profile_members}   Set Variable   ${profile_resp['members'][0]}
    \   Append To List   ${Profileunassign}   ${profile_members}
	common.Unassign Server Profiles   ${Profileunassign}

TC12 Assign Server Hardware To Profile
    [Documentation]   Query OneView for list of profiles then Assign server hardwares to server profiles.
    [Tags]  POWEROFF_SERVERS2    EDIT_ALL
    ${Server_items}=    Get Dictionary Items    ${SERVER_PROFILE_TO_BAY_MAP}
    ${IGNORE_SERVER_HEALTH} =   Get Variable Value   ${IGNORE_SERVER_HEALTH}
    Run Keyword If  ${Server_items} is not ${null}    common.Assign Server Hardware To Existing Profiles From Variable   ${Server_items}   ${SERVER_PROFILE_TO_BAY_MAP}  timeout=${SERVER_HW_ASSIGN_WAIT_TIME}   interval=${SERVER_HW_ASSIGN_INTERVAL}   waitForTask=${True}
    :FOR  ${profile}  ${hardware}    IN  @{Server_items}
    \   ${shUri} =    Run Keyword If  "${SERVER_PROFILE_TO_BAY_MAP['${profile}']}" != "${null}"   Fusion Api Get Server Hardware   param=?filter="'name'=='${hardware}'"
	\   ...   ELSE    Continue For Loop
    \   Should Be Equal   ${shUri['total']}   ${1}   msg=Response body total is not as expected.
    \   ${Serverhw_uri} =   Set Variable   ${shUri['members'][0]['uri']}
    \   common.Power On Server Uri   ${Serverhw_uri}
    Sleep And Log Reason To Console   ${SERVER_POWERON_SLEEP}   reason=Sleeping for ${SERVER_POWERON_SLEEP} to let the servers to poweron...
    Log   \n Performing the Server check After Assigning the server    console=${True}
    Server check

TC13 Poweroff_Server Profile edit
    [Documentation]   Editing server profile while server is in poweroff mode
    [Tags]   POWEROFF_CONNECTION_EDIT   EDIT_ALL
	${Server_items}=    Get Dictionary Items    ${SERVER_PROFILE_ONLINE_OFFLINE_EDIT}
    :FOR  ${profile}  ${hardware}    IN  @{Server_items}
    \    ${HW} =   Fusion Api Get Server Hardware  param=?filter="name='${hardware}'"
    \    Should Be Equal   ${HW['total']}   ${1}   msg=Response body total is not as expected.
	\    ${Serverhw_uri}=    Set Variable      ${HW['members'][0]['uri']}
    \    common.Power Off Server Uri   ${Serverhw_uri}   proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}
    \    ${resp} =   Fusion Api Get Server Profiles   param=?filter="'name'=='${profile}'"
    \    Should Be Equal   ${resp['total']}   ${1}   msg=Response body total is not as expected.
    \    ${sp_uri} =   Set Variable   ${resp['members'][0]['uri']}
    \    ${sp_resp} =   Fusion Api Get Resource   uri=${sp_uri}
    \    Set To Dictionary   ${sp_resp['connectionSettings']['connections'][0]}   portId   None
    \    Set To Dictionary   ${sp_resp['connectionSettings']['connections'][0]}   requestedMbps   ${REQUESTEDMBPS}
    \    Remove From Dictionary   ${sp_resp}   status_code   headers
    \    Log   \n editing server profile ${profile}   console=${True}
    \    ${resp} =   Fusion Api Edit Server Profile   uri=${sp_uri}   body=${sp_resp}
    \    ${valDict} =   Create Dictionary   status_code=${200}
    \    ...                                taskState=Completed
    \    fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   timeout=${WAIT_FOR_TASK_WAIT_TIME}   interval=${WAIT_FOR_TASK_INTERVAL}

TC14 Poweroff_Server Connection Delete
    [Documentation]   Delete server profile Connection when server is in poweroff mode
    [Tags]    POWEROFF_CONNECTION_DELETE   EDIT_ALL
    ${PROFILE_NAMES}   Create List
	${PROFILE_NAMES}   Get Dictionary Keys    ${SERVER_PROFILE_ONLINE_OFFLINE_EDIT}
	:FOR    ${x}   IN    @{PROFILE_NAMES}
	\   ${resp}   Delete Profile Connection   ${x}   ${CONNECTION_ID}   message=Deleting profile connection wait_task_timeout=${WAIT_FOR_TASK_WAIT_TIME}   wait_task_interval=${WAIT_FOR_TASK_INTERVAL}   proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}
    Sleep And Log Reason To Console   ${SERVER_POWERON_SLEEP}   reason=Sleeping for ${SERVER_POWERON_SLEEP} to let the servers to poweron...

TC15 Restoring of the backup
    [Documentation]   Restore the appliance from created backup
    [Tags]    APP_BACKUP   EDIT_ALL
    ${PROFILE_NAMES}   Create List
	${PROFILE_NAMES}   Get Dictionary Keys    ${SERVER_PROFILE_TO_BAY_MAP}
    Run Keyword If   "${EG}" == "${null}"   Pick One EG And Use It
    common.Upload Restore Backup And Perform Data Compare     unassign_reassign_profiles=${PROFILE_NAMES}  

***keywords***
Server check
    [Documentation]   Checks the status of Enc,LE,IC,LI,server's MG,Multipath,Sequential_ping,Readonly,ISS crash,Fping loss,Bonding Interfaces and port status
    Check Common Resource Attributes
    Check For Multipath   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For MeatGrinder Error
    Check For Server In Read Only Filesystem
    common.Run Sequential Ping
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    All Etherchannel Summary Ports Should Be Linked   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Fping Should Have No Loss

Get IC Port
    [Documentation]    Returns the port info of the named port of specified interconnect uri
    [Arguments]     ${uri}    ${portName}
    ${return} =    Create List
    ${resp} =    fusion api get interconnect ports    uri=${uri}
    ${ports} =    Get From Dictionary    ${resp}    members
    :FOR    ${port}    IN    @{ports}
    \    ${return} =    Run Keyword If    '${port['portName']}' == '${portName}'    set variable    ${port}
    \    Exit for loop if    '${port['portName']}' == '${portName}'
    [Return]    ${return}
