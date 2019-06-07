*** Settings ***
Documentation       ICM-Reset-Parallel.robot  -  Resets ICM parallely and checks that they return to expected state
...                     Example:
...                              pybot -T -d /tmp/logs/ICM-Reset-Parallel -LTRACE -V /root/ci-fit/config_files/eaglexx_data_variables.py ICM-Reset-Parallel.robot
...                     Required argument:
...                         -V /root/ci-fit/config_files/eaglexx_data_variables.py
...                         -v HA_FILE:/path/to/your/tcs/HA_file.conf
...                     Optional arguments:
...                         To trigger detailed resource checking, supply -vGOLDEN_FILE:<./dataFiles/golden-icmReboot.json>  (Run test Generate-Resource-Json.robot to create golden file.)
...                         To change the sender name, use -vEMAIL_FROM:<email address>
...                         To override the default number of cycles, use -vCYCLES:<number of cycles>
...                         To target a specific LI, use -vTARGET_LI:<LI Name>
...                         To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                         To specify a single ICM to reboot, use -vDO_ONLY:<ICM number>
...                         To disable checking of etherchannel summary, use -vCHECK_ETH_SUMMARY:False
...                         To disable checking of Bonding Multi Test, use -DISABLE_BONDING_MULTI_TEST:True
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>
...                         To change the order that the ICMS are rebooted, supply -v ICM_ORDER:<order>
...                            valid choices for order are: random|alpha|ibsmaster|ibsslave
...                            random:    random order  #default
...                            alpha:     by enclosure, by interconnect bay number
...                            ibsmaster: by stackingDomainId, then stackingDomainRole, master first, then slave
...                            ibsslave:  by stackingDomainId, then by stackingDomainRole, slave first, then master


Variables           ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Library             Collections
Library             ../../resources/robustness-helper.py

*** Variables ***
${CYCLES}                       1
${ICM_ORDER}                    random    # random|alpha|ibsmaster|ibsslave
${SSH_PASS}                     hpvse1
${FUSION_IP}                    ${APPLIANCE_IP}
${GOLDEN_FILE}                  None
${EMAIL_FROM}                   ${EMAIL_TO}
${TARGET_LI}                    None
${DO_ONLY}                      None
${STOP_SCRIPT}                  /root/.stop_script
${CHECK_ETH_SUMMARY}            True
${SERVER_BONDING_CHECKS}        None
${DISABLE_BONDING_MULTI_TEST}   False
${HA_FILE}                      None
${UPDATE_LFCCACHE}              False
${tbirdEnv}                     None
${POST_ICM_RESET_SLEEP}         30m
${ICM_RESET_WAIT_TIMEOUT}       10m
${ICM_RESET_WAIT_INTERVAL}      2s
${RESET_INITIATING_SLEEP_TIME}  2m
${TCS_HAFNIUM_SSH_INTERFACE}    eth0
${REMOTE_CHECKS_TAG}            -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}       &{EMPTY}
@{REMOTE_RUN_CHECKS}            @{EMPTY}
@{AllResourcesList}             ethNets  fcNets  fcoeNets  ic  ictype  networkset  uplinkset  lig  li  encGrp  encs  servers  profiles  users
# Some ignored attributes with associated Quix
# linkPortIsolated: QXCR1001496453
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  linkPortIsolated  portStatusReason  remotePortDescription  remoteSystemDescription  interconnects_ADD_ports_15_portTypeExtended  interconnects_ADD_ports_15_connectorType  interconnectUri_ADD_interconnectIP  interconnectIP  personalityChecksum  installState  deviceUri_ADD_romVersion

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Robustness Reset ICM
    Check Suite Requirements
    Check Common Resource Attributes
    Run Optional Data Compare    ${GOLDEN_FILE}   preICMReset.json
    ${DO_ONLY} =   Run Keyword If   "${DO_ONLY}" != "${null}"   Split String   ${DO_ONLY}   ${SPACE}
    Cycle    ${CYCLES}
    Run Optional Data Compare    ${GOLDEN_FILE}   postICMReset.json

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.

*** Keywords ***
Cycle
    [Documentation]   Cycle up a test.
    [Arguments]     ${cycles}
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    :FOR    ${x}    IN RANGE    1   ${cycles}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n Cycle: ${x} of ${cycles}   console=${True}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   Check Interconnects LI And Run ICM Reset

Check Interconnects LI And Run ICM Reset
    [Documentation]   Checks Interconnects, LI to perform ICM reset either parallely or sequentially.
    ${icm_resp} =   Fusion Api Get Interconnect
    ${icms} =    Get From Dictionary     ${icm_resp}    members
    ${resp} =   Get LIs
    ${Enc_resp} =   Fusion Api Get Enclosures
    ${enc_len} =   Get Length   ${Enc_resp['members']}
    ${li_length}    Get Length    ${resp}
    Run Keyword If   ${li_length} == ${1} and ${enc_len} == ${1}   Fail   msg=This is Single ENC and Single LI setup so please use the ICM-Reset.robot script for ICM reset operation.
    ...   ELSE    Fetch ICMs For Parallel ICM Reset   ${icms}

Fetch ICMs For Parallel ICM Reset
    [Documentation]   Fetches interconnect modules for parallel interconnect reset test.
    [Arguments]     ${icms}   ${sleep}=10m
    ${A_list} =  Create List
    ${B_list} =  Create List
    :FOR   ${IC}   IN   @{icms}
    \    ${a_side} =    Get ICM List for Parallel Reset    ${IC}    ${Parallel_Aside}
    \    Run Keyword If   ${a_side} != ${None}  Append to list   ${A_list}    ${a_side}
    \    ${b_side} =   Get ICM List for Parallel Reset     ${IC}    ${Parallel_Bside}
    \    Run Keyword If   ${b_side} != ${None}   Append to list   ${B_list}    ${b_side}
    Process ICMs For Parallel ICM Reset   ${A_list}   wait_task_timeout=${ICM_RESET_WAIT_TIMEOUT}   wait_task_interval=${ICM_RESET_WAIT_INTERVAL}    sleep=${POST_ICM_RESET_SLEEP}   reset_initiating_sleep_time=${RESET_INITIATING_SLEEP_TIME}
    Process ICMs For Parallel ICM Reset   ${B_list}   wait_task_timeout=${ICM_RESET_WAIT_TIMEOUT}   wait_task_interval=${ICM_RESET_WAIT_INTERVAL}    sleep=${POST_ICM_RESET_SLEEP}   reset_initiating_sleep_time=${RESET_INITIATING_SLEEP_TIME}

Get ICM List for Parallel Reset
    [Documentation]   Gets Icm List for parallel reset process
    [Arguments]     ${icm}    ${Bay_num_parallel_reset}
    ${icmName}=   Get From Dictionary   ${icm}    name
    ${icmBay} =   Fetch From Right   ${icmName}   ${SPACE}
    ${ic_a} =   Count Values In List   ${Bay_num_parallel_reset}   ${icmBay}
    Return From Keyword If   '${ic_a}' != '${0}'   ${icm}

Process ICMs For Parallel ICM Reset
    [Documentation]   Process interconnect modules for Synergy interconnect parallel reset test.
    [Arguments]     ${icms}    ${wait_task_timeout}=10m   ${wait_task_interval}=2s   ${waitForTask}=${True}    ${validate}=${True}    ${throttle}=${Null}   ${sleep}=10m   ${reset_initiating_sleep_time}=2m
    Set Log Level	TRACE
    ${icm_len} = 	Get Length	${icms}
	${respList}    Create List
	${valDict} =    Create Dictionary       status_code=${200}
    ...                                 taskState=Completed
	Set Suite Variable   ${forkedErrorFound}   ${False}
    ${liUri} =   Run Keyword If   '${TARGET_LI}' != '${Null}'   Get LI Uri By Name   ${TARGET_LI}
    :FOR	${x}	IN RANGE	0	${icm_len}
    \   ${ic} =     Get From List   ${icms}    ${x}
    \   Continue For Loop If   '${liUri}' != '${Null}' and '${ic['logicalInterconnectUri']}' != '${liUri}'
    \   ${bay} =   Fetch From Right   ${ic['name']}   ${SPACE}
    \   ${skip} =   Run Keyword If   "${DO_ONLY}" != "${null}"   Run Keyword And Return Status   List Should Not Contain Value   ${DO_ONLY}   ${bay}
    \   Run Keyword If   ${skip}   Continue For Loop
    \   Log to console      ${ic['name']} ${ic['uri']}
    \   ${data} =   Create Dictionary   op=replace
    \   ...                             path=/deviceResetState
    \   ...                             value=Reset
    \   ${body} =   Create List     ${data}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    Resetting: ${ic['name']} ${ic['uri']}
    \   ${resp} =   Fusion Api Patch Interconnect   body=${body}    uri=${ic['uri']}
    \   ${contains} =   Evaluate   '${ic['model']}' in ${HAFNIUM_ICM_MODELS}
    \   Run Keyword If  '${contains}' == '${True}'    Run Keywords   Sleep And Log Reason To Console   ${reset_initiating_sleep_time}   reason=Sleeping ${reset_initiating_sleep_time} while ICM reset is initiating   AND   common.Run Sequential Ping
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   tags=-i PING
    \   Continue For Loop If   ${waitForTask} != ${True}
    \   Append To List   ${respList}   ${resp}
    \       Continue For Loop If   '${throttle}' == '${Null}'
    \       ${respLength} =   Get Length   ${respList}
    \       Continue For Loop If   ${respLength} != ${throttle}
    \       ${respList} =   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${wait_task_timeout}   ${wait_task_interval}   ${validate}   throttle=${throttle}
    Run Keyword If   ${waitForTask} is ${True}   Run Keywords   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${wait_task_timeout}   ${wait_task_interval}   ${validate}   AND
	...    Sleep And Log Reason To Console   ${sleep}   reason=Sleeping ${sleep} after an ICM Reset.
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=Not all forked tasks state finished with Completed.
	Check Servers And OV After ICM Reset    ${icms}

Check Servers And OV After ICM Reset
    [Documentation]    Checking For Servers And OV After ICM Reset.
    [Arguments]     ${icms}
	${icm_len} = 	Get Length	${icms}
	:FOR	${x}	IN RANGE	0	${icm_len}
    \   ${ic} =     Get From List   ${icms}    ${x}
    \   Log   -Verify it's reset   console=${True}
    \   ${ic} =     Get Interconnect Filter By Name  ${ic['name']}
    \   ${deviceResetState} =   Get From Dictionary   ${ic}   deviceResetState
    \   Should Be Equal As Strings    ${deviceResetState}  Normal
    Check Common Resource Attributes
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    Check For MeatGrinder Error
    Check For Multipath   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem
    common.Run Sequential Ping
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    All Etherchannel Summary Ports Should Be Linked   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}
