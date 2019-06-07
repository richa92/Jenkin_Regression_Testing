*** Settings ***
Documentation		LE-add-remove.robot  -  delete\re-create LE for x cycles
...    1. before beginning cycle, checks the state of: LE, enclosures, LIs, icms, 
...       profiles, and blades
...    2. OPTIONAL: generate resource data and do detailed compare to golden file
...    3. for given cycles (def = 10): powers off blades, unassigns profiles, removes all LEs
...       creates all LEs, checks the state of: LE, enclosures, LIs, icms, re-assigns profiles
...       powers on blades, checks profiles and blades
...    NOTE: setup must be run seperately before running this test.
...    NOTE: the same datafile used for setup must be supplied to this test with -V (see below)
...    usage: pybot -d /tmp/logs/LE-add-remove -V <your tbird setup data variable file> -V <your test data variable file> LE-add-remove.robot
...
...                     Required arguments:
...                         -V /root/ci-fit/config_files/eaglexx_setup_data_variables.py
...                         -V /root/ci-fit/config_files/eaglexx_test_data_variables.py
...                         -v HA_FILE:/path/to/your/ha_file.conf
...                     Optional arguments:
...                         To trigger detailed resource checking, supply -vGOLDEN_FILE:<./dataFiles/golden-le-add-remove.json>  (Run test Generate-Resource-Json.robot to create golden file)
...                         To change the sender's name, use -vEMAIL_FROM:<email address>
...                         To override the default number of cycles, use -vCYCLES:<number of cycles>
...                         To proceed with PressAndHold when MomentaryPress fails with this errorCode, use -vPROCEED_WITH_PRESS_AND_HOLD:SERVER_MOMENTARY_PRESS_OFF_TIMEOUT
...                         To use graceful power off via ssh (this will require -v HA_FILE:<your ha file> arg, use -vPOWER_OFF_MODE:ssh
...                         Default profile throttle: 3, to override it use -vPROFILE_THROTTLE:[None|<number of profiles at a time>]
...                         To disable checking of etherchannel summary, use -vCHECK_ETH_SUMMARY:False
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                         To test for Nitro (if not specified it will try to find what you have in OneView), use -vHAFNIUM_MODEL:'Virtual Connect SE 100Gb F32 Module for Synergy'
...                         To ignore server hardware status, use -vIGNORE_BLADES:"<bay#s separated by SPACE>". Example: To ignore server hardware status of bays 1,5,12, use -vIGNORE_BLADES:"1 5 12"
...                         To do power on serially because of power issue/limitation, use -vPARALLEL_POWER_ON:False
...                         POWER_OFF_SLEEP is the maximum amount of time we consider OneView to transition powerState to Off since powering server off via ssh. To override that variable, use -vPOWER_OFF_SLEEP:<RF time format ex. 10m>

Variables           ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Library             Collections
Library             ../../resources/robustness-helper.py

*** Variables ***
${CYCLES}                       10
${SSH_PASS}                     hpvse1
${FUSION_IP}                    ${APPLIANCE_IP}
${GOLDEN_FILE}                  None
${EMAIL_FROM}                   ${EMAIL_TO}
${POWER_OFF_MODE}               api
${PROCEED_WITH_PRESS_AND_HOLD}  None
${HA_FILE}                      None
${CHECK_ETH_SUMMARY}            True
${SERVER_BONDING_CHECKS}        None
${DISABLE_BONDING_MULTI_TEST}   False
${UPDATE_LFCCACHE}              False
${tbirdEnv}                     None
${IGNORE_BLADES}                None
${PROFILE_THROTTLE}             3
${FORCE_PROFILE_APPLY}          all
${Num_Of_Var_File}              ${2}
${STOP_SCRIPT}                  /root/.stop_script
${X-API-VERSION}                ${null}
${HAFNIUM_MODEL}                ${Null}
${PARALLEL_POWER_ON}            True
${POWER_OFF_SLEEP}               5m
${TCS_HAFNIUM_SSH_INTERFACE}    eth0
${REMOTE_CHECKS_TAG}            -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}       &{EMPTY}
@{REMOTE_RUN_CHECKS}            @{EMPTY}
@{AllResourcesList}   ethNets  fcNets  fcoeNets  ic  ictype  networkset  uplinkset  lig  li  
...                   encGrp  encs  servers  profiles  users
# Some ignored attributes with associated Quix
# linkPortIsolated: QXCR1001496453
@{ignoreList}   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  
...             roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  
...             enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  
...             hpSmartUpdateToolStatus  connectorType  portStatusReason  linkPortIsolated  
...             mgmtPortState  mpFirmwareVersion  interconnectIP  ethernetSettings  
...             stackingDomainId  lagId  personalityChecksum  remotePortDescription  
...             remoteSystemDescription  deviceUri_ADD_romVersion  
...             interconnectUri_ADD_interconnectIP  installState  serverHwChecksum  portId

*** Test Cases ***
Login Appliance And Set Test
    [Documentation]   Login appliance
    Run Keyword If   '${POWER_OFF_MODE}' == 'ssh' and '${HA_FILE}' == '${Null}'   Fail   msg=Power off mode via ssh was selected while HA_FILE is ${Null}. Please set your HA_FILE!
    Authenticate And Set Login
    Run Keyword If   '${X-Api-Version}' == '${null}'   Set Api Version To Current

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Create LE - Delete LE
    [Documentation]   Create and Delete LE
    Check Suite Requirements    ${Num_Of_Var_File}
    # collect environment in private variables, names different than datafile!
    ${resp}    fusion api get server profiles
	${xprofiles}    Evaluate     $resp.get('members', [])
	Run Keyword If    "${xprofiles}" == "@{EMPTY}"    Log   \nQuery in OneView returned empty members indicating there is no server profiles.    WARN   console=${True}
    ...    ELSE    Check Common Resource Attributes
    # To get the test going with some known server status issue (status goes Critical causing test to fail)
    ${IGNORE_BLADES} =   Run Keyword If   '${IGNORE_BLADES}' != '${Null}'   Split String   ${IGNORE_BLADES}   ${SPACE}
    ...                            ELSE   Create List
    Set Suite Variable   ${IGNORE_BLADES}
    Run Keyword If   "${GOLDEN_FILE}" == "${null}"   Check profiles and blades     ${xprofiles}
    Run Optional Data Compare    ${GOLDEN_FILE}   preLEAddRm.json
    Cycle    ${CYCLES}    ${xprofiles}
    Run Optional Data Compare    ${GOLDEN_FILE}   postLEAddRm.json

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   
    ...   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.


*** Keywords ***
Cycle
    [Documentation]   Cycle up a test.
    [Arguments]     ${cycles}    ${xprofiles}
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    :FOR	${x}	IN RANGE	1	${cycles}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n Cycle: ${x} of ${cycles}   console=${True}
    \   Run Keyword If   '${POWER_OFF_MODE}' == 'api'   Power Off All Servers In Parallel   proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}
    \   ...    ELSE IF   '${POWER_OFF_MODE}' == 'ssh'   Power Off All Servers Via Ssh In Parallel    server_off_sleep=${POWER_OFF_SLEEP}
    \   Log to console   \nUnassigning profiles....
    \   common.Unassign Server Profiles   ${xprofiles}   timeout=${UNASSIGN_SERVER_WAIT_TIMEOUT}   interval=${UNASSIGN_SERVER_WAIT_INTERVAL}   forceProfileApply=${FORCE_PROFILE_APPLY}   throttle=${PROFILE_THROTTLE}
    \   Remove All Logical Enclosures
    \   Run Keyword for List	       ${les}        Add Logical Enclosure from variable   # les is from the datafile
    \   Sleep And Log Reason To Console   ${POST_ADD_LE_SLEEP}   reason=Sleeping ${POST_ADD_LE_SLEEP} after create logical enclosure.
    \   Check Common Resource Attributes
    \   Log to console   \nRe-assigning profiles....
    \   common.Assign Server Profiles   ${xprofiles}   timeout=${ASSIGN_SERVER_WAIT_TIMEOUT}   interval=${ASSIGN_SERVER_WAIT_INTERVAL}   forceProfileApply=${FORCE_PROFILE_APPLY}   throttle=${PROFILE_THROTTLE}
    \   common.Power On Server Hardware In Profile Members    ${xprofiles}    parallel=${PARALLEL_POWER_ON}
    #   RNB  Added sleep here, as it seems some blades refuse to obey shutdown if they are still starting...
    \   Sleep And Log Reason To Console   ${POST_SERVER_ON_SLEEP}   reason=Sleeping ${POST_SERVER_ON_SLEEP} after server power on.
    \   Run Keyword If   "${GOLDEN_FILE}" == "${null}"   Check profiles and blades      ${xprofiles}
    \   Check Common Resource Attributes
    # Reset link failure count to 0 since server starts from off
    \   Reset Select Servers Link Failure Count Cache   ${xprofiles}
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

