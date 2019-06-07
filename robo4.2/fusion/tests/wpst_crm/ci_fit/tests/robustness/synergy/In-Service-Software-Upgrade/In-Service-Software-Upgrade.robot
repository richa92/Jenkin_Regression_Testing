*** Settings ***
Documentation        Upload SPP into OneView Firmware Bundles or load (an existing one) then perform Hafnium updates through Logical Interconnect Firmware Update.
...                  This was primarily written for ISSU Base Compatible - Case B - orchestrated ICM restart but should be generic enough for other ISSU cases.
...                  This will alternately do the update between SPP_BUNDLE_NAME and SPP_BUNDLE_NAME1.
...
...                  To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                  To test for Nitro (if not specified it will try to find what you have in OneView), use -vHAFNIUM_MODEL:'Virtual Connect SE 100Gb F32 Module for Synergy'
...                  REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>
...
...                  Example workflow (Upload ./SPPGen10Snap1.2017_0425.124.iso and ./SPPGen10Snap1FF.2017_0803.38.iso and update alternately):
...                      time pybot -T -d /tmp/logs/In-Service-Software-Upgrade/ -LTRACE -vSPP_BUNDLE_DIR:./ -vSPP_BUNDLE_NAME:SPPGen10Snap1.2017_0425.124.iso -vSPP_BUNDLE_DIR1:./ -vSPP_BUNDLE_NAME1:SPPGen10Snap1FF.2017_0803.38.iso -V /root/ci-fit/config_files/robustness/eagle63-issu.py In-Service-Software-Upgrade.robot
...                  Example workflow (Use an uploaded SPP Bundle Service Pack for ProLiant):
...                      time pybot -T -d /tmp/logs/In-Service-Software-Upgrade/ -LTRACE -vSPP_BUNDLE_NAME:SPPGen10Snap1.2017_0425.124 -vSPP_BUNDLE_NAME1:SPPGen10Snap1FF.2017_0803.38 -V /root/ci-fit/config_files/robustness/eagle63-issu.py In-Service-Software-Upgrade.robot

Variables           ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Library		    Collections
Library             ../../resources/robustness-helper.py

*** Variables ***
${CYCLES}                       30
${FUSION_IP}                    ${APPLIANCE_IP}
${GOLDEN_FILE}                  None
${EMAIL_FROM}                   ${EMAIL_TO}
${SPP_BUNDLE_DIR}		None
${SPP_BUNDLE_DIR1}		None
${STOP_SCRIPT}                  /root/.stop_script
${CHECK_ETH_SUMMARY}            True
${SERVER_BONDING_CHECKS}        None
${DISABLE_BONDING_MULTI_TEST}   False
${HA_FILE}                      None
${UPDATE_LFCCACHE}              False
${HAFNIUM_MODEL}                ${Null}
${TCS_HAFNIUM_SSH_INTERFACE}    eth0
${tbirdEnv}                     None
${REMOTE_CHECKS_TAG}            -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}       &{EMPTY}
@{REMOTE_RUN_CHECKS}            @{EMPTY}
@{AllResourcesList}             ethNets  fcNets  fcoeNets  ic  ictype  networkset  uplinkset  lig  li  encGrp  encs  servers  profiles  users
# Some ignored attributes with associated Quix
# linkPortIsolated: QXCR1001496453
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  portStatusReason  linkPortIsolated  mgmtPortState  mpFirmwareVersion  interconnectIP  remotePortDescription  remoteSystemDescription  interconnects_ADD_ports_15_portTypeExtended  interconnects_ADD_ports_15_connectorType  interconnectUri_ADD_ports_15_portTypeExtended  interconnectUri_ADD_ports_15_connectorType  deviceUri_ADD_romVersion

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Check For SPP Bundle Argument
    Run Keyword If   "${SPP_BUNDLE_NAME}" == "${null}" or "${SPP_BUNDLE_NAME1}" == "${null}"   Fail   msg=SPP_BUNDLE_NAME and SPP_BUNDLE_NAME1 are required arguments. Please provide it using -vSPP_BUNDLE_NAME:<SPP Name> and -vSPP_BUNDLE_NAME1:<SPP Name>.

Check For ICM Names Variable
    ${icmLocStat}   ${icmLocRetval} =   Run Keyword And Ignore Error   Variable Should Exist   ${ICM_NAMES}
    Variable Should Exist   ${ICM_NAMES}   ICM_NAMES is a required variable for this test. Please make sure it is set in the data_variables.py file and try again.

Check For Target LI Variable
    ${targetLiStat}   ${targetLiRetval} =   Run Keyword And Ignore Error   Variable Should Exist   ${TARGET_LI}
    Variable Should Exist   ${TARGET_LI}   TARGET_LI is a required variable for this test. Please make sure it is set in the data_variables.py file and try again.

Robustness ISSU
    ${icmLocStat}   ${icmLocRetval} =   Run Keyword And Ignore Error   Variable Should Exist   ${ICM_NAMES}
    ${targetLiStat}   ${targetLiRetval} =   Run Keyword And Ignore Error   Variable Should Exist   ${TARGET_LI}
    Check Suite Requirements
    Log Variables
    Check Common Resource Attributes
    Run Optional Data Compare   ${GOLDEN_FILE}   preFWUpdate.json
    Cycle
    Run Optional Data Compare   ${GOLDEN_FILE}   postFWUpdate.json

Send Email Notification
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.


*** Keywords ***
Cycle
    [Documentation]   Starts cycling tests.
    ${bundleUri1} =   Load SPP FW Bundle   bundle_dir=${SPP_BUNDLE_DIR}   bundle_name=${SPP_BUNDLE_NAME}   wait_task_timeout=${SPP_UPLOAD_WAIT_TIMEOUT}   wait_task_interval=${SPP_UPLOAD_WAIT_INTERVAL}
    ${bundleUri2} =   Load SPP FW Bundle   bundle_dir=${SPP_BUNDLE_DIR1}   bundle_name=${SPP_BUNDLE_NAME1}   wait_task_timeout=${SPP_UPLOAD_WAIT_TIMEOUT}   wait_task_interval=${SPP_UPLOAD_WAIT_INTERVAL}
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    :FOR   ${x}   IN RANGE   1   ${CYCLES}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n Cycle: ${x} of ${CYCLES}   console=${True}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   ${eval} =   Evaluate   ${x} % 2
    \   Run Keyword If  ${eval} == 1   Update Potash ICMs FW   ${bundleUri1}   failOnMismatch=${False}
    \   ...       ELSE   Update Potash ICMs FW   ${bundleUri2}   failOnMismatch=${False}
    \   Check Common Resource Attributes
    \   Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    \   Check For MeatGrinder Error
    \   Check For Multipath   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    \   Check For Server In Read Only Filesystem
    \   common.Run Sequential Ping
    \   Fping Should Have No Loss
    \   Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    \   All Etherchannel Summary Ports Should Be Linked   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    \   Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}
    \   Sleep And Log Reason To Console   ${END_OF_CYCLE_WAIT}   reason=Sleeping ${END_OF_CYCLE_WAIT} at the end of the cycle.
