*** Settings ***
Documentation		Removes enclosure(s) from an appliance and add them back for x cycles.
...    1. before beginning cycle, checks the state of: enclosures, LIs, icms, profiles and blades
...    2. OPTIONAL: generate resource data and do detailed compare to golden file
...    3. for given cycles (def = 10): powers off blades, unassigns profiles, removes all LEs
...       creates all LEs, checks the state of: LE, enclosures, LIs, icms, re-assigns profiles
...       powers on blades, checks profiles and blades
...    NOTE: setup must be run seperately before running this test.
...    NOTE: the same datafile used for setup must be supplied to this test with -V (see below)
...                     Example:
...                            time pybot -T -d /tmp/logs/Appliance-Enc-Add-Remove.robot -LTRACE -V /root/ci-fit/config_files/eaglexx_setup_data_variables.py -V /root/ci-fit/config_files/eaglexx_test_data_variables.py Appliance-Enc-Add-Remove.robot 
...
...                     Required arguments:
...                         -V /root/ci-fit/config_files/eaglexx_setup_data_variables.py
...                         -V /root/ci-fit/config_files/eaglexx_test_data_variables.py
...                         -v HA_FILE:/path/to/your/tcs/HA_file.conf
...                     Optional arguments:
...                         To trigger detailed resource checking, supply -vGOLDEN_FILE:<./dataFiles/golden-encAddRemove.json>  (Run test Generate-Resource-Json.robot to create golden file)
...                         To change the sender's name, use -vEMAIL_FROM:<email address>
...                         To override the default number of cycles, use -vCYCLES:<number of cycles>
...                         To proceed with PressAndHold when MomentaryPress fails with this errorCode, use -vPROCEED_WITH_PRESS_AND_HOLD:SERVER_MOMENTARY_PRESS_OFF_TIMEOUT
...                         To use graceful power off via ssh (this will require -v HA_FILE:<your ha file> arg, use -vPOWER_OFF_MODE:ssh
...                         Default profile throttle: 3, to override it use -vPROFILE_THROTTLE:[None|<number of profiles at a time>]
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                         REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>

Library				RoboGalaxyLibrary
Library				FusionLibrary
Library				OperatingSystem
Library				BuiltIn
Library				Collections
Library				XML
Library				String

Variables	    ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Resource            ../../../configure_appliance/resource/common.robot
Library             ../../resources/robustness-helper.py

*** Variables ***
${VM}				vm-name
${VMSETUP}			no
${FTS}				no
${CONFIGURE}		        no
${FUSION_IP}                    ${APPLIANCE_IP}
${SSH_PASS}                     hpvse1
${CYCLES}                       15
${GOLDEN_FILE}                  None
${EMAIL_FROM}                   ${EMAIL_TO}
${POWER_OFF_MODE}               api
${PROCEED_WITH_PRESS_AND_HOLD}  None
${HA_FILE}                      None
${SERVER_BONDING_CHECKS}        None
${DISABLE_BONDING_MULTI_TEST}   True
${UPDATE_LFCCACHE}              False
${tbirdEnv}                     None
${FORCE_PROFILE_APPLY}          all
${PROFILE_THROTTLE}             3
${STOP_SCRIPT}                  /root/.stop_script
${X-API-VERSION}                ${null}
${REMOTE_CHECKS_TAG}            -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}       &{EMPTY}
@{REMOTE_RUN_CHECKS}            @{EMPTY}
@{AllResourcesList}             ethNets  fcNets  fcoeNets  ic  ictype  networkset  uplinkset  lig  li  encGrp  encs  servers  profiles  users
# Some ignored attributes with associated Quix
# linkPortIsolated: QXCR1001496453
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  portStatusReason  linkPortIsolated  mgmtPortState  mpFirmwareVersion  interconnectIP  ethernetSettings  stackingDomainId  lagId  personalityChecksum  deviceUri_ADD_romVersion  settingId  optionId  portId  remoteSystemName  migrationState


*** Test Cases ***
Login Appliance And Set Test
    Run Keyword If   '${POWER_OFF_MODE}' == 'ssh' and '${HA_FILE}' == '${Null}'   Fail   msg=Power off mode via ssh was selected while HA_FILE is ${Null}. Please set your HA_FILE!
    Authenticate And Set Login
    Run Keyword If   '${X-Api-Version}' == '${null}'   Set Api Version To Current

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Remove Add Enclosure
    Run Keyword If   "${SERVER_BONDING_CHECKS}" != "${Null}" and '${SERVER_HAFILE}' == '${Null}'   Fail   msg=SERVER_BONDING_CHECKS was enabled but SERVER_HAFILE is not set. Please set the SERVER_HAFILE in your pybot command or data variable file.
    Run Keyword If   "${DISABLE_BONDING_MULTI_TEST}" == "${False}" and '${HA_FILE}' == '${Null}' or '${SERVER_HAFILE}' == '${Null}'   Fail   msg=DISABLE_BONDING_MULTI_TEST is False but HA_FILE or SERVER_HAFILE is not set. Please set the HA_FILE and SERVER_HAFILE in your pybot command or data variable file.
    Run Keyword If   "${HA_FILE}" != "${Null}"   OperatingSystem.File Should Exist   ${HA_FILE}
    Variable File Should Be Passed   num=${2}
    ${xprofiles} =    Get Profiles
    ${xblades} =      Get Blades from profiles   ${xprofiles}
    Run Keyword If   "${GOLDEN_FILE}" == "${null}"   Check profiles and blades   ${xprofiles}
    Check Common Resource Attributes
    Run Optional Data Compare    ${GOLDEN_FILE}   preEncAddRm.json
    Cycle    ${CYCLES}    ${xprofiles}   ${xblades}
    Run Optional Data Compare    ${GOLDEN_FILE}   postEncAddRm.json

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.

*** Keywords ***
Cycle
    [Documentation]   Run one or more cycles of appliance enclosure add remove based on value set in CYCLES variable.
    [Arguments]     ${cycles}  ${xprofiles}  ${xblades}
    ${enclosures} =	Get Variable Value	${encs}
    ${orig_enclosures} =   WPST Deep Copy   ${enclosures}
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    :FOR	${x}	IN RANGE	1	${cycles}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n Cycle: ${x} of ${cycles}   console=${True}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   Run Keyword If   '${poweroff_mode}' == 'api'   Power Off All Servers Serially   proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}
    \   ...    ELSE IF   '${poweroff_mode}' == 'ssh'   Power Off All Servers Via Ssh
    \   Log to console   \nUnassigning profiles....
    \   common.Unassign Server Profiles       ${xprofiles}   timeout=${UNASSIGN_SERVER_WAIT_TIMEOUT}   interval=${UNASSIGN_SERVER_WAIT_INTERVAL}   forceProfileApply=${FORCE_PROFILE_APPLY}   throttle=${PROFILE_THROTTLE}
    \   common.Remove ALL Enclosures   remove_timeout=${REMOVE_ENC_WAIT_TIMEOUT}   remove_interval=${REMOVE_ENC_WAIT_INTERVAL}
    \   Run Keyword If   ${enclosures} is not ${null}   Add Enclosures from variable   ${enclosures}
    \   Sleep And Log Reason To Console   ${POST_ADD_ENC_SLEEP}   reason=Sleeping for ${POST_ADD_ENC_SLEEP}, giving time for post add enclosures activities...
    \   ${xlis} =         Get LIs
    \   Check LIs and interconnects    ${xlis}
    \   Log to console   \nRe-assigning profiles....
    \   common.Assign Server Profiles         ${xprofiles}   timeout=${ASSIGN_SERVER_WAIT_TIMEOUT}   interval=${ASSIGN_SERVER_WAIT_INTERVAL}   forceProfileApply=${FORCE_PROFILE_APPLY}   throttle=${PROFILE_THROTTLE}
    \   Sleep And Log Reason To Console   ${POST_ASSIGN_PROFILE_SLEEP}   reason=Sleeping for ${POST_ASSIGN_PROFILE_SLEEP}, giving time for post assign profile activities...
    \   Run Keyword for List           ${xblades}    common.Power on server uri   wait_task_timeout=${SERVER_POWERON_WAIT_TIMEOUT}   wait_task_interval=${SERVER_POWERON_WAIT_INTERVAL}
    #   RNB  Added sleep here, as it seems some blades refuse to obey shutdown if they are still starting...
    \   Sleep And Log Reason To Console   ${POST_SERVER_ON_SLEEP}   reason=Sleeping for ${POST_SERVER_ON_SLEEP}, giving time for post server poweron activities...
    \   Run Keyword If   "${GOLDEN_FILE}" == "${null}"   Check profiles and blades      ${xprofiles}
    \   Check Common Resource Attributes
    # Reset link failure count to 0 since server starts from off
    \   Reset Select Servers Link Failure Count Cache   ${xprofiles}
    \   Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    \   Check For MeatGrinder Error
    \   Check For Multipath
    \   Check For Server In Read Only Filesystem
    \   common.Run Sequential Ping
    \   Fping Should Have No Loss
    \   Check For ISS Crash
    \   Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}
    \   ${enclosures} =   WPST Deep Copy   ${orig_enclosures}

