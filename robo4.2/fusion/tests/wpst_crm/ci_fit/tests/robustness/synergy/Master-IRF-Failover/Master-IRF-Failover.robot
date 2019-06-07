*** Settings ***
Documentation        Master IRF TOR Switch Failover.
...                  This will power off the Master device (59XX), wait for mac persistent time (6m), power the device back on. 59XX switches, hafnium, server blades, and OneView will be verified to make sure they are in the expected states.
...                  Some setup requirements:
...                  1. 59XX switches in IRF setup
...                  2. SSH access to Hafnium
...                  3. data_variables.py file for your test environment. You can reference to Master-IRF-Failover/data_variables.py by copying it and putting it in /root/ci-fit/config_files/
...                  Required Arguments:
...                      -V /root/ci-fit/config_files/<your master IRF data variables file>
...                      -v GOLDEN_FILE:/path/to/your/golden.json
...                  Optional Arguments (PING_HAFILE is optional but highly recommended):
...                      -vPING_HAFILE:<path to your new profile HA file>
...                      -v HA_FILE:/path/to/your/tcs/HA_file.conf
...                      To disable checking of etherchannel summary, use -vCHECK_ETH_SUMMARY:False
...                      To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                      To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                      To test for Nitro (if not specified it will try to find what you have in OneView), use -vHAFNIUM_MODEL:'Virtual Connect SE 100Gb F32 Module for Synergy'
...                      REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>
...                  Example:
...                      time pybot -T -d /tmp/logs/synergy/Master-IRF-Failover/ -L TRACE -V /root/ci-fit/config_files/master-irf-failover-robustness.py -v GOLDEN_FILE:/root/ci-fit/config_files/goldenMasterIrfFailover.json Master-IRF-Failover.robot

Variables           ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Library             RoboGalaxyLibrary
Library             Collections
Library             ../../resources/robustness-helper.py

*** Variables ***
${CYCLES}                       10
${SSH_PASS}                     hpvse1
${FUSION_IP}                    ${APPLIANCE_IP}
${EMAIL_FROM}                   ${EMAIL_TO}
${STOP_SCRIPT}                  /root/.stop_script
${CHECK_ETH_SUMMARY}            True
${SERVER_BONDING_CHECKS}        None
${DISABLE_BONDING_MULTI_TEST}   False
${HA_FILE}                      None
${UPDATE_LFCCACHE}              False
${HAFNIUM_MODEL}                ${Null}
${tbirdEnv}                     None
${TCS_HAFNIUM_SSH_INTERFACE}    eth0
${REMOTE_CHECKS_TAG}            -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}       &{EMPTY}
@{REMOTE_RUN_CHECKS}            @{EMPTY}
@{AllResourcesList}             ic  ictype  uplinkset  li  servers  profiles
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  portStatusReason  linkPortIsolated  mgmtPortState  mpFirmwareVersion  interconnectIP  ethernetSettings  lagId  personalityChecksum  remotePortDescription  remoteSystemDescription  deviceUri_ADD_romVersion  interconnectUri_ADD_interconnectIP  installState  interconnects_ADD_ports_25_connectorType   interconnects_ADD_ports_15_connectorType   interconnects_ADD_ports_20_connectorType   interconnects_ADD_ports_10_connectorType   dcbxPgReason  interconnects_ADD_interconnectIP

*** Test Cases ***
Login Appliance And Set Test
    [Tags]   LOGIN
    Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Robustness Master IRF Failover
    ${GOLDEN_FILE} =   Get Variable Value   ${GOLDEN_FILE}
    Run Keyword If   "${GOLDEN_FILE}" == "${null}"   Fail   msg=Resource data compare is required in this test. Please define your GOLDEN_FILE in data variable file or in your pybot command.
    Check Suite Requirements
    Check Common Resource Attributes
    Run Optional Data Compare   ${GOLDEN_FILE}   preMasterIrfFailover.json
    Check For MeatGrinder Error
    Check For Multipath   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem
    common.Run Sequential Ping
    ${parsedEtherSummary} =   Get Ethernet Summary   ${ICM_NAMES}   userName=${HAFNIUM_USERNAME}   password=${HAFNIUM_PASSWORD}
    ${dictEtherSummary} =   Convert Ether Summary To Dictionary   ${parsedEtherSummary}
    ${uplinkSets} =   Get Uplink Sets Attributes   ${TARGET_US}   ${TARGET_ATTRIBUTES}
    # compare ether summary against uplink-sets data
    Ether Summary Should Match With Uplink Sets   ${dictEtherSummary}   ${uplinkSets}
    Cycle

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.


*** Keywords ***
Cycle
    [Documentation]   Cycle up a test.
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    :FOR   ${x}   IN RANGE   1   ${CYCLES}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n Cycle: ${x} of ${CYCLES}   console=${True}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   Wait Until List Of ICMs Reached Configured   ${ICM_NAMES}   ${ICM_CONFIGURE_WAIT_TIMEOUT}   2s
    \   ${preRoles} =   Get 59XX Roles   ${SW_59XX_IPADDR}   userName=${SW_59XX_USERNAME}   password=${SW_59XX_PASSWORD}
    \   Log   Bringing down Master IRF switch...   console=${True}
    \   Perform iPDU Outlet Control   ${SW_iPDU_XML['${preRoles['Master']['cpu-mac']}']['off']}   port=${iPDU_PORT}
    \   Sleep And Log Reason To Console   ${MASTER_IRF_FAILOVER_WAIT}   reason=Master IRF switch going down and let Standby takes the master role over (usually this should be at least the same wait time as 'Mac persistent' setting). Sleeping ${MASTER_IRF_FAILOVER_WAIT}...
    # TODO: Need to figure out a way to know which ICM is affected by Master IRF power off
    # Check that the bonding interfaces are in the expected state/status
    # \   Run Keyword If   '${ic['model']}' == '${HAFNIUM_MODEL}'   Run Keywords   Bonding Interfaces Should Be In Expected States   ${ic['uri']}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}   AND   Set Test Variable   ${offline_interconnect}   ${ic['uri']}
    # \   ...       ELSE   Set Test Variable   ${offline_interconnect}   ${Null}
    # \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${offline_interconnect}   tags=${REMOTE_CHECKS_TAG}
    \   Log   Bringing up the previous Master IRF switch...   console=${True}
    \   Perform iPDU Outlet Control   ${SW_iPDU_XML['${preRoles['Master']['cpu-mac']}']['on']}   port=${iPDU_PORT}
    \   Wait Until List Of ICMs Reached Configured   ${ICM_NAMES}   ${ICM_CONFIGURE_WAIT_TIMEOUT}   2s
    \   Sleep And Log Reason To Console   ${END_OF_CYCLE_SLEEP}   reason=Previous master IRF switch brought back up and will let things settle. Sleeping ${END_OF_CYCLE_SLEEP}...
    \   ${postRoles} =   Get 59XX Roles   ${SW_59XX_IPADDR}   userName=${SW_59XX_USERNAME}   password=${SW_59XX_PASSWORD}
    \   Switch Roles Should Have Transitioned   ${preRoles}   ${postRoles}
    \   ${parsedEtherSummary} =   Get Ethernet Summary   ${ICM_NAMES}   userName=${HAFNIUM_USERNAME}   password=${HAFNIUM_PASSWORD}
    \   ${dictEtherSummary} =   Convert Ether Summary To Dictionary   ${parsedEtherSummary}
    \   ${uplinkSets} =   Get Uplink Sets Attributes   ${TARGET_US}   ${TARGET_ATTRIBUTES}
    # compare ether summary against uplink-sets data
    \   Ether Summary Should Match With Uplink Sets   ${dictEtherSummary}   ${uplinkSets}
    \   Run Optional Data Compare   ${GOLDEN_FILE}   postMasterIrfFailover.json
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

