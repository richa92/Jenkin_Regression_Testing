*** Settings ***
Documentation       Blade-Power-Control.robot  -  Performs any one of the blade power control operation such as MomentaryPress, PressAndHold, ColdBoot, or Reset on the servers
...                     Example workflow:
...                            pybot -T -d /tmp/logs/Blade-Power-Control -LTRACE -v Appliance_IP:15.186.X.XX -v powerControl:MomentaryPress  -v powerState:On -v ENC_NAME:Eag_115_MXQ70102XL -v BAYS:"1 2" -v Exclude_servers:"Eag_115_MXQ70102XL:1 Eag_115_MXQ70102XL:3" Blade-Power-Control.robot
...                     Required Arguments:
...                         -v powerControl: <Specify type of powercontrol which is required>
...                         -v powerState:<Specify type of power state according to the powerControl>
...                         To disable checking of etherchannel summary, use -vCHECK_ETH_SUMMARY:False
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                         To disable bonding multi test, use -vDISABLE_BONDING_MULTI_TEST:True
...                         To Perform bonding multi test HA_FILE is required, use -v HA_FILE:/path/to/your/ha_file.conf
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         To test for Nitro (if not specified it will try to find what you have in OneView), use -vHAFNIUM_MODEL:'Virtual Connect SE 100Gb F32 Module for Synergy'
...                         REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>
...                  OPTIONAL: -v ENC_NAME - Will perform power control operations in all the servers of the given enclosure, instead of all servers in the ME.
...                  OPTIONAL: -v BAYS - Will perform power control operations on the bay numbers given.  Can be used across all enclosures in an ME.
...                  OPTIONAL: -v Exclude_servers - Skips power on operation in given servers

Variables           ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Library             RoboGalaxyLibrary
Library             Collections
Library             ../../resources/robustness-helper.py

*** Variables ***
${FUSION_IP}                    ${APPLIANCE_IP}
${tbirdEnv}                     None
${ENC_NAME}                     None
${BAYS}                         None
${CYCLES}                       1
${STOP_SCRIPT}                  /root/.stop_script
${ONE_TIME_PASS}                None
${DO_ONLY}                      None
${GOLDEN_FILE}                  None
${EMAIL_FROM}                   ${EMAIL_TO}
${HA_FILE}                      None
${STOP_SCRIPT}                  /root/.stop_script
${FORCE}                        False
${CHECK_ETH_SUMMARY}            True
${SERVER_BONDING_CHECKS}        None
${DISABLE_BONDING_MULTI_TEST}   False
${UPDATE_LFCCACHE}              False
${Exclude_servers}              None
${POST_SERVER_ON_SLEEP}         30m
${HAFNIUM_MODEL}                ${Null}
${TCS_HAFNIUM_SSH_INTERFACE}    eth0
${REMOTE_CHECKS_TAG}            -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}       &{EMPTY}
@{REMOTE_RUN_CHECKS}            @{EMPTY}

*** Test Cases ***
Login Appliance And Set Test
    [Documentation]    Login to OneView and set suite variables appropriately
    Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Robustness blade power control
    [Documentation]   Performs power control operation on blades
    Check Suite Requirements
    ${ONE_TIME_PASS} =   Run Keyword If   "${ONE_TIME_PASS}" != "${null}"   Split String   ${ONE_TIME_PASS}   ${SPACE}
    ...                             ELSE   Set Variable   ${ONE_TIME_PASS}
    ${ONE_TIME_PASS} =   Set Test Variable   ${ONE_TIME_PASS}
    Check Common Resource Attributes
    Run Optional Data Compare   ${GOLDEN_FILE}   appliance.json
    ${DO_ONLY} =   Run Keyword If   "${DO_ONLY}" != "${null}"   Split String   ${DO_ONLY}   ${SPACE}
    Cycle    ${CYCLES}
    Run Optional Data Compare   ${GOLDEN_FILE}   appliance.json

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.

***Keywords***
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
    \   Process Enclosure for Blade Power Control

Process Enclosure for Blade Power Control
    [Documentation]    Gettting Enclosure and Verifying Devicebays
    ${operation} =   Set Variable   powerControl
    ${Enclosures} =   Run Keyword If   "${ENC_NAME}" != "${null}"   Fusion Api Get Enclosures   param=?filter="name=='${ENC_NAME}'"
    ...       ELSE   Fusion Api Get Enclosures
    Should Not Be Empty   ${Enclosures['members']}   msg=Given enclosure name not found.
    :FOR   ${enc}   IN   @{Enclosures['members']}
    \   Verify Device Bays    ${enc['deviceBays']}    ${operation}
    \    Run Keyword For List   ${enc['deviceBays']}   Ignore Power On Operation For Specified Blades    encName=${enc['name']}
    Sleep And Log Reason To Console   ${POST_SERVER_ON_SLEEP}   reason=Sleeping ${POST_SERVER_ON_SLEEP} after server power on.
    Check Common Resource Attributes
    # Reset link failure count to 0 since server starts from off
    Reset All Servers Link Failure Count Cache
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    Check For MeatGrinder Error
    Check For Multipath   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem
    common.Run Sequential Ping
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    All Etherchannel Summary Ports Should Be Linked   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}

Ignore Power On Operation For Specified Blades
    [Documentation]    Ignoring Power On Operation for Specified Blades
    [Arguments]     ${deviceBays}   ${encName}
    ${Exclude_servers} =   Split String   ${Exclude_servers}   ${SPACE}
    ${enc_baynum} =   Catenate    SEPARATOR=:    ${encName}   ${deviceBays['bayNumber']}
    ${contains} =   Evaluate   '${enc_baynum}' in ${Exclude_servers}
    Return From Keyword If   '${deviceBays['devicePresence']}' != 'Present'
    Run Keyword If   ${contains} == False   common.Power On Server Uri    ${deviceBays['deviceUri']}
