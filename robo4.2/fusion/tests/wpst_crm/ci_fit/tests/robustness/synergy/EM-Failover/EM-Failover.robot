*** Settings ***
Documentation		EM-Failover  -  Perform EM Failover and check that they return to the expected state.
...                     Example:
...                              pybot -T -d /tmp/logs/EM-Failover -LTRACE -V /root/ci-fit/config_files/eaglexx_test_data_variables.py EM-Failover.robot
...                     Required argument:
...                         -V /root/ci-fit/config_files/eaglexx_data_variables.py
...                         -v HA_FILE:/path/to/your/tcs/HA_file.conf
...                     Optional arguments:
...                         To trigger detailed resource checking, supply -vFAILOVER_GOLDEN_0:./dataFiles/golden-Failover1.json -vFAILOVER_GOLDEN_1:./dataFiles/golden-Failover2.json
...                            (Run test Generate-Resource-Json.robot to create golden files. Note: FAILOVER_GOLDEN_1 needs manual modification of the role...)
...                         To change the sender's name, use -vEMAIL_FROM:<email address>
...                         To override the default number of cycles, use -vCYCLES:<number of cycles>
...                         To override the default failover target (common practice is to direct failover at standby), use -vFAILOVER_TARGET:active
...                         To disable checking of etherchannel summary, use -vCHECK_ETH_SUMMARY:False
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                         REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>

Variables           ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Library		    Collections
Library             ../../resources/robustness-helper.py

*** Variables ***
${CYCLES}                       75
${FUSION_IP}                    ${APPLIANCE_IP}
${FAILOVER_GOLDEN_0}            None
${FAILOVER_GOLDEN_1}            None
${EMAIL_FROM}                   ${EMAIL_TO}
${FAILOVER_TARGET}              standby
${STOP_SCRIPT}                  /root/.stop_script
${CHECK_ETH_SUMMARY}            True
${SERVER_BONDING_CHECKS}        None
${DISABLE_BONDING_MULTI_TEST}   False
${HA_FILE}                      None
${UPDATE_LFCCACHE}              False
${TCS_HAFNIUM_SSH_INTERFACE}    eth0
${tbirdEnv}                     None
${REMOTE_CHECKS_TAG}            -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}       &{EMPTY}
@{REMOTE_RUN_CHECKS}            @{EMPTY}
@{AllResourcesList}             ethNets  fcNets  fcoeNets  ic  ictype  networkset  uplinkset  lig  li  encGrp  encs  servers  profiles  users
# Some ignored attributes with associated Quix
# linkPortIsolated: QXCR1001496453
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  linkPortIsolated  portStatusReason  mpFirmwareVersion  deviceUri_ADD_mpFirmwareVersion  interconnectIP  mgmtPortState  remotePortDescription  remoteSystemDescription  deviceUri_ADD_assetTag  personalityChecksum  installState  powerAvailableWatts  powerCapacityBoostWatts  deviceUri_ADD_romVersion

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Failover Target Should Exist
   Run Keyword If   "${FAILOVER_TARGET}" != "standby" and "${FAILOVER_TARGET}" != "active"   Fail   msg=Failover target has to be standby or active. Please define FAILOVER_TARGET variable as either active or standby.

Robustness EM Failover
    Check Suite Requirements
    Run Keyword If   "${FAILOVER_TARGET}" != "standby" and "${FAILOVER_TARGET}" != "active"   Fail   msg=There was a validation error. Please check the validation test case(s) and try again.
    ${enclosures} =    Get EM Enclosures
    Log to console      ${enclosures}
    Cycle    ${CYCLES}   ${enclosures}

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.


*** Keywords ***
Cycle
    [Documentation]   Cycle up a test.
    [Arguments]     ${cycles}  ${enclosures}
    Check Common Resource Attributes
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    Run Optional Alternating Data Compare   0   preFailover.json   ${FAILOVER_GOLDEN_0}   ${FAILOVER_GOLDEN_1}
    :FOR	${x}	IN RANGE	1	${cycles}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n Cycle: ${x} of ${cycles}   console=${True}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   Process Enclosures    ${enclosures}   sleep=${POST_EM_FAILOVER_SLEEP}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Run Optional Alternating Data Compare   ${x}   postFailover.json   ${FAILOVER_GOLDEN_0}   ${FAILOVER_GOLDEN_1}

