*** Settings ***
Documentation        Power Outage.
...                  This will power off the rack to simulate power outage scenario. This test requires it's own data variable file. You can copy Power-Outage/data_variables.py to your /root/ci-fit/config_files/ and modify it to match with your test environment.
...                  Required Argument:
...                      -V /root/ci-fit/config_files/<your power outage data variables file>
...                      -vGOLDEN_FILE:<path to your json golden file>
...                  Optional Arguments (PING_HAFILE is optional but highly recommended):
...                      -vPING_HAFILE:<path to your new profile HA file>
...                      -v HA_FILE:/path/to/your/tcs/HA_file.conf
...                      To disable checking of etherchannel summary, use -vCHECK_ETH_SUMMARY:False
...                      To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                      To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                      To test for Nitro (if not specified it will try to find what you have in OneView), use -vHAFNIUM_MODEL:'Virtual Connect SE 100Gb F32 Module for Synergy'
...                      REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>
...                  Example:
...                      time pybot -T -d /tmp/logs/synergy/Power-Outage/ -vGOLDEN_FILE:./eagle63.json -V /root/ci-fit/config_files/power-outage-robustness.py -L TRACE Power-Outage.robot

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
${CHECK_ETH_SUMMARY}            False
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
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  portStatusReason  linkPortIsolated  mgmtPortState  mpFirmwareVersion  interconnectIP  ethernetSettings  stackingDomainId  lagId  personalityChecksum  remotePortDescription  remoteSystemDescription  deviceUri_ADD_romVersion  interconnectUri_ADD_interconnectIP  installState

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Robustness Power Outage
    ${GOLDEN_FILE} =   Get Variable Value   ${GOLDEN_FILE}
    Run Keyword If   "${GOLDEN_FILE}" == "${null}"   Fail   msg=Resource data compare is required in this test. Please define your GOLDEN_FILE in data variable file or in your pybot command.
    Check Suite Requirements
    Check Common Resource Attributes
    Run Optional Data Compare   ${GOLDEN_FILE}   prePowerOutage.json
    Check For MeatGrinder Error
    Check For Multipath   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem
    common.Run Sequential Ping
    All Etherchannel Summary Ports Should Be Linked   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}
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
    \   Log   Performing power outage using iPDU outlet control...   console=${True}
    \   Send iPDU Outlet Control   ${iPDU_IP}   ${iPDU_OUTLET_CONTROL['OFF']}   port=${iPDU_PORT}
    \   Sleep And Log Reason To Console   ${POWER_OUTAGE_DURATION}   reason=Simulating power outage duration. Sleeping ${POWER_OUTAGE_DURATION}...
    \   Log   Performing power restore using iPDU outlet control...   console=${True}
    \   Send iPDU Outlet Control   ${iPDU_IP}   ${iPDU_OUTLET_CONTROL['ON']}   port=${iPDU_PORT}
    \   Sleep And Log Reason To Console   ${POWER_RESTORE_SLEEP}   reason=Sleeping ${POWER_RESTORE_SLEEP} to give time for the system to go back up and recover.
    \   Run Optional Data Compare   ${GOLDEN_FILE}   postPowerOutage.json
    # Reset link failure count to 0 since server starts from off
    \   Reset All Servers Link Failure Count Cache
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

