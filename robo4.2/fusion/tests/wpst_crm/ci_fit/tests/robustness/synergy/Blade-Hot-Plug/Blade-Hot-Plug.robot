*** Settings ***
Documentation		Blade-Hot-Plug.robot  -  uses EM based eFuse to add-remove blades and check that they return to the expected state
...                     Example:
...                              pybot -T -d /tmp/logs/Blade-Hot-Plug -LTRACE -V /root/ci-fit/config_files/eaglexx_test_data_variables.py Blade-Hot-Plug.robot
...                     Required argument:
...                         -V /root/ci-fit/config_files/eaglexx_data_variables.py
...                         -v HA_FILE:/path/to/your/ha_file.conf
...                     Optional arguments:
...                         To trigger detailed resource checking, supply -vGOLDEN_FILE:<./dataFiles/golden-icmHotplug.json>  (Run test Generate-Resource-Json.robot to create golden file.)
...                         To bypass blade bay(s) 1 and 2 in first cycle for enclosure Eagle63_CN754404R3, use -vONE_TIME_PASS:'Eagle63_CN754404R3:1 Eagle63_CN754404R3:2'
...                         To specify which blades to hot plug, use -vDO_ONLY:'<blade bay numbers space delimited>'
...                         To change the sender's name, use -vEMAIL_FROM:<email address>
...                         To override the default number of cycles, use -vCYCLES:<number of cycles>
...                         To only hot plug server hardware with 'ProfileApplied', use -vONLY_PROFILE_APPLIED:True
...                         To proceed with PressAndHold when MomentaryPress fails with this errorCode, use -vPROCEED_WITH_PRESS_AND_HOLD:SERVER_MOMENTARY_PRESS_OFF_TIMEOUT
...                         To use graceful power off via ssh (this will require -v HA_FILE:<your ha file> arg, use -vPOWER_OFF_MODE:ssh
...                         To use non-graceful power off (efuse without powering off server), use -v FORCE:True
...                         To disable checking of etherchannel summary, use -vCHECK_ETH_SUMMARY:False
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                         To test for Nitro (if not specified it will try to find what you have in OneView), use -vHAFNIUM_MODEL:'Virtual Connect SE 100Gb F32 Module for Synergy'
...                         REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>
...                         To achieve parallel Efuse use -v PARALLEL_EFUSE:True

Variables           ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Library             Collections
Library             ../../resources/robustness-helper.py

*** Variables ***
${CYCLES}                       50
${SSH_PASS}                     hpvse1
${FUSION_IP}                    ${APPLIANCE_IP}
${GOLDEN_FILE}                  None
${ONE_TIME_PASS}                None
${DO_ONLY}                      None
${EMAIL_FROM}                   ${EMAIL_TO}
${POWER_OFF_MODE}               api
${PROCEED_WITH_PRESS_AND_HOLD}  None
${HA_FILE}                      None
${STOP_SCRIPT}                  /root/.stop_script
${FORCE}                        False
${CHECK_ETH_SUMMARY}            True
${SERVER_BONDING_CHECKS}        None
${DISABLE_BONDING_MULTI_TEST}   False
${UPDATE_LFCCACHE}              False
${HAFNIUM_MODEL}                ${Null}
${tbirdEnv}                     None
${TCS_HAFNIUM_SSH_INTERFACE}    eth0
${REMOTE_CHECKS_TAG}            -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}       &{EMPTY}
@{REMOTE_RUN_CHECKS}            @{EMPTY}
@{AllResourcesList}             ethNets  fcNets  fcoeNets  ic  ictype  networkset  uplinkset  lig  li  encGrp  encs  servers  profiles  users
# Some ignored attributes with associated Quix
# linkPortIsolated: QXCR1001496453
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  portStatusReason  linkPortIsolated  mgmtPortState  mpFirmwareVersion  interconnectIP  intelligentProvisioningVersion  installState  personalityChecksum  remotePortDescription  remoteSystemDescription  deviceUri_ADD_romVersion  deviceBayWatts  powerCapacityBoostWatts  powerAvailableWatts  powerAllocatedWatts  powerAllocationWatts  deviceUri_ADD_assetTag
${PARALLEL_EFUSE}               False
${X-API-VERSION}                ${null}

*** Test Cases ***
Login Appliance And Set Test
    [Tags]  LOGIN
    Run Keyword If   '${POWER_OFF_MODE}' == 'ssh' and '${HA_FILE}' == '${Null}'   Fail   msg=Power off mode via ssh was selected while HA_FILE is ${Null}. Please set your HA_FILE!
    Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

EFuse Blade Off-On and check state Absent-Configured
    Check Suite Requirements
    ${ONE_TIME_PASS} =   Run Keyword If   "${ONE_TIME_PASS}" != "${null}"   Split String   ${ONE_TIME_PASS}   ${SPACE}
    ...                             ELSE   Set Variable   ${ONE_TIME_PASS}
    ${ONE_TIME_PASS} =   Set Test Variable   ${ONE_TIME_PASS}
    ${blades} =   Get Blades
    Check Common Resource Attributes
    Run Optional Data Compare   ${GOLDEN_FILE}   appliance.json
    ${DO_ONLY} =   Run Keyword If   "${DO_ONLY}" != "${null}"   Split String   ${DO_ONLY}   ${SPACE}
    Cycle    ${CYCLES}    ${blades}
    Run Optional Data Compare   ${GOLDEN_FILE}   appliance.json

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.


*** Keywords ***
Cycle
    [Documentation]   Cycle up a test.
    [Arguments]     ${cycles}    ${blades}
    ${ONLY_PROFILE_APPLIED} =   Get Variable Value   ${ONLY_PROFILE_APPLIED}
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    :FOR	${x}	IN RANGE	1	${cycles}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n Cycle: ${x} of ${cycles}   console=${True}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   Run Keyword If   "${PARALLEL_EFUSE}" == "${False}"    Process Blades For Synergy Blade Hot Plug    ${blades}   state_timeout=${BLADE_HOTPLUG_STATE_WAIT_TIMEOUT}   state_interval=${BLADE_HOTPLUG_STATE_WAIT_INTERVAL}   remove_timeout=${BLADE_REMOVE_WAIT_TIMEOUT}   remove_interval=${BLADE_REMOVE_WAIT_INTERVAL}   insert_timeout=${BLADE_INSERT_WAIT_TIMEOUT}   insert_interval=${BLADE_INSERT_WAIT_INTERVAL}   sleep=${BLADE_HOTPLUG_CYCLE_SLEEP}   onlyProfileApplied=${ONLY_PROFILE_APPLIED}   poweroff_mode=${POWER_OFF_MODE}  proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}
    \   ...                             ELSE    Process Blades For Synergy Blade Hot Plug Parallel    ${blades}   state_timeout=${BLADE_HOTPLUG_STATE_WAIT_TIMEOUT}   state_interval=${BLADE_HOTPLUG_STATE_WAIT_INTERVAL}   remove_timeout=${BLADE_REMOVE_WAIT_TIMEOUT}   remove_interval=${BLADE_REMOVE_WAIT_INTERVAL}   insert_timeout=${BLADE_INSERT_WAIT_TIMEOUT}   insert_interval=${BLADE_INSERT_WAIT_INTERVAL}   sleep=${BLADE_HOTPLUG_CYCLE_SLEEP}   onlyProfileApplied=${ONLY_PROFILE_APPLIED}   poweroff_mode=${POWER_OFF_MODE}   proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}
    \   Sleep And Log Reason To Console   ${BLADE_HOTPLUG_CYCLE_SLEEP}   reason=Sleeping ${BLADE_HOTPLUG_CYCLE_SLEEP} to let things settle (DTO may update a little late) at the end of a cycle.
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

