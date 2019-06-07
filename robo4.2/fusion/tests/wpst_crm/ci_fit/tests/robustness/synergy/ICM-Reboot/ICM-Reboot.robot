*** Settings ***
Documentation		ICM-Reboot.robot  -  Powers Off/On ICMs and check that they return to the expected state
...                     Example:
...                              pybot -T -d /tmp/logs/ICM-Reboot -LTRACE -V /root/ci-fit/config_files/eaglexx_data_variables.py ICM-Reboot.robot
...                     Required argument:
...                         -V /root/ci-fit/config_files/eaglexx_data_variables.py
...                         -v HA_FILE:/path/to/your/tcs/HA_file.conf
...                     Optional arguments:
...                         To override ICM_MODEL from default, use -vICM_MODEL:<interconnect model name used by OneView>. Example (Carbon): -vICM_MODEL:"Virtual Connect SE 16Gb FC Module for Synergy"
...                         To bypass interconnect bay(s) 1 and 2 in first cycle for enclosure Eagle63_CN754404R3, use -vONE_TIME_PASS:'Eagle63_CN754404R3:1 Eagle63_CN754404R3:2'
...                         To trigger detailed resource checking, supply -vGOLDEN_FILE:<./dataFiles/golden-icmHotplug.json>  (Run test Generate-Resource-Json.robot to create golden file.)
...                         To change the sender's name, use -vEMAIL_FROM:<email address>
...                         To override the default number of cycles, use -vCYCLES:<number of cycles>
...                         To target a specific Logical Interconnect, use -vTARGET_LI:<LI Name>
...                         To specify a single ICM to reboot, use -vDO_ONLY:<ICM number>
...                         To disable checking of etherchannel summary, use -vCHECK_ETH_SUMMARY:False
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                         To test for Nitro (if not specified it will try to find what you have in OneView), use -vHAFNIUM_MODEL:'Virtual Connect SE 100Gb F32 Module for Synergy'
...                         REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>
...                         To change the order that the ICMS are rebooted, supply -vICM_ORDER:<order>
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
${CYCLES}                       50
${ICM_MODEL}                    ${POTASH}
${ICM_ORDER}                    random    # random|alpha|ibsmaster|ibsslave
${SSH_PASS}                     hpvse1
${FUSION_IP}                    ${APPLIANCE_IP}
${EMAIL_FROM}                   ${EMAIL_TO}
${TARGET_LI}                    None
${ONE_TIME_PASS}                None
${GOLDEN_FILE}                  None
${DO_ONLY}                      None
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
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  linkPortIsolated  portStatusReason  remotePortDescription  remoteSystemDescription  interconnects_ADD_interconnectIP  interconnectUri_ADD_interconnectIP  interconnectIP  personalityChecksum  installState  deviceUri_ADD_romVersion  migrationState  powerAvailableWatts  powerCapacityBoostWatts  deviceUri_ADD_assetTag

*** Test Cases ***
Login Appliance And Set Test
    [Tags]   Login   debug
    Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Robustness Reboot ICM
    [Tags]  run
    Check Suite Requirements
    ${ONE_TIME_PASS} =   Run Keyword If   "${ONE_TIME_PASS}" != "${null}"   Split String   ${ONE_TIME_PASS}   ${SPACE}
    ...                             ELSE   Set Variable   ${ONE_TIME_PASS}
    ${ONE_TIME_PASS} =   Set Test Variable   ${ONE_TIME_PASS}
    ${icms} =     Get Interconnects
    Run Keyword If   ${icms} is ${Null}   Fail   msg=Unable to find "${ICM_MODEL}" in your Interconnects. Please use -vICM_MODEL:<Existing ICM Model> to specify interconnect model to test.
    Check Common Resource Attributes
    Run Optional Data Compare    ${GOLDEN_FILE}   preICMReboot.json
    ${DO_ONLY} =   Run Keyword If   "${DO_ONLY}" != "${null}"   Split String   ${DO_ONLY}   ${SPACE}
    Cycle    ${CYCLES}    ${icms}
    Run Optional Data Compare    ${GOLDEN_FILE}   postICMReboot.json

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.

*** Keywords ***
Cycle
    [Documentation]   Cycle up a test.
    [Arguments]     ${cycles}    ${icms}
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    :FOR	${x}	IN RANGE	1	${cycles}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n Cycle: ${x} of ${cycles}   console=${True}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   Process ICMs For Synergy ICM Reboot    ${icms}   power_wait_timeout=${ICM_POWER_REQUEST_WAIT_TIMEOUT}   power_wait_interval=${ICM_POWER_REQUEST_WAIT_INTERVAL}   maintenance_timeout=${ICM_REBOOT_MAINTENANCE_WAIT_TIMEOUT}   maintenance_interval=${ICM_REBOOT_MAINTENANCE_WAIT_INTERVAL}   configure_timeout=${ICM_REBOOT_CONFIGURED_WAIT_TIMEOUT}   configure_interval=${ICM_REBOOT_CONFIGURED_WAIT_INTERVAL}   alert_timeout=${ICM_REBOOT_ALERT_WAIT_TIMEOUT}   alert_interval=${ICM_REBOOT_ALERT_WAIT_INTERVAL}   sleep=${POTASH_SERVER_RECOVERY_SLEEP}   iface=${TCS_HAFNIUM_SSH_INTERFACE}

