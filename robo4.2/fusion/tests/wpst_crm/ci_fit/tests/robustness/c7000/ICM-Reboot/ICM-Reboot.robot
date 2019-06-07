*** Settings ***
Documentation		ICM-Reboot.robot  -  uses OA-based restart interconnect to reboot interconnect module. Then, check that they return to the expected state
...                     Example:
...                              time pybot -T -d /tmp/logs/ICM-Reboot.robot -LTRACE -vENC:CI-FIT-16 -V /root/ci-fit/config_files/eaglexx_test_data_variables.py ICM-Reboot.robot
...
...                     IMPORTANT NOTE: This requires -vENC:<encName> argument. This also requires user to setup their enclosure credentials in the ../../resources/credentials_cifit.py credential file (you can refer to existing ones on how). The name you provided in credential file must be the same name you pass in -vENC:<encName> and the same name that is managed by OneView.
...
...                     Required argument:
...                         -V /root/ci-fit/config_files/eaglexx_test_data_variables.py
...                         -v HA_FILE:/path/to/your/tcs/HA_file.conf
...                     Optional arguments:
...                         To trigger detailed resource checking, supply -vGOLDEN_FILE:<./dataFiles/golden-icmReboot.json>  (Run test Generate-Resource-Json.robot to create golden file.)
...                         To bypass interconnect bay(s) 1 and 2 in first cycle for enclosure C15M_Bmark, use -vONE_TIME_PASS:'C15M_Bmark:1 C15M_Bmark:2'
...                         To change the sender's name, use -vEMAIL_FROM:<email address>
...                         To override the default number of cycles, use -vCYCLES:<number of cycles>
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                         REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>

Variables           ../../resources/data_variables.py
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Library             Collections
Library             ../../../../../../wpst_crm/crm_austin/lib/WPSTUtil.py

Variables           ../../../../../../wpst_crm/crm_austin/resources/defaults.py
Variables           ../../resources/credentials_cifit.py  ${ENC}
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords.txt
Resource            ../../resources/common.robot
Library             ../../resources/robustness-helper.py

*** Variables ***
${CYCLES}                       10
${SSH_PASS}                     hpvse1
${FUSION_IP}                    ${APPLIANCE_IP}
${GOLDEN_FILE}                  None
${EMAIL_FROM}                   ${EMAIL_TO}
${ENC}                          None
${ONE_TIME_PASS}                None
${STOP_SCRIPT}                  /root/.stop_script
${SERVER_BONDING_CHECKS}        None
${DISABLE_BONDING_MULTI_TEST}   True
${HA_FILE}                      None
${UPDATE_LFCCACHE}              False
${tbirdEnv}                     None
${REMOTE_CHECKS_TAG}            -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}       &{EMPTY}
@{REMOTE_RUN_CHECKS}            @{EMPTY}
@{AllResourcesList}             ethNets  fcNets  fcoeNets  ic  ictype  networkset  uplinkset  lig  li  encGrp  encs  servers  profiles  users
# Some ignored attributes with associated Quix
# linkPortIsolated: QXCR1001496453
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  linkPortIsolated  portStatusReason  optionId  settingId  deviceUri_ADD_romVersion

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

ICM Off-On and check state Absent-Configured
    Run Keyword If   "${APPLIANCE_IP}" == "${Null}"   Fail   msg=APPLIANCE_IP was not specified in the command or set in data variable file.
    Run Keyword If   "${SERVER_BONDING_CHECKS}" != "${Null}" and '${SERVER_HAFILE}' == '${Null}'   Fail   msg=SERVER_BONDING_CHECKS was enabled but SERVER_HAFILE is not set. Please set the SERVER_HAFILE in your pybot command or data variable file.
    Run Keyword If   "${DISABLE_BONDING_MULTI_TEST}" == "${False}" and '${HA_FILE}' == '${Null}' or '${SERVER_HAFILE}' == '${Null}'   Fail   msg=DISABLE_BONDING_MULTI_TEST is False but HA_FILE or SERVER_HAFILE is not set. Please set the HA_FILE and SERVER_HAFILE in your pybot command or data variable file.
    Run Keyword If   "${HA_FILE}" != "${Null}"   OperatingSystem.File Should Exist   ${HA_FILE}
    Variable File Should Be Passed
    ${ONE_TIME_PASS} =   Run Keyword If   "${ONE_TIME_PASS}" != "${null}"   Split String   ${ONE_TIME_PASS}   ${SPACE}
    ...                             ELSE   Set Variable   ${ONE_TIME_PASS}
    ${ONE_TIME_PASS} =   Set Test Variable   ${ONE_TIME_PASS}
    ${resp} =   Fusion Api Get Resource   /rest/enclosures
    ${encs} =   Get From Dictionary   ${resp}   members
    ${l} =   Get Length   ${encs}
    :FOR   ${x}   IN RANGE   0   ${l}
    \   Log   ${encs[${x}]}
    \   Run Keyword If   '${encs[${x}]['name']}' != '${ENC}'   Continue For Loop
    \   ${icms_uri} =   Create Interconnect Bay To Uri Map   ${encs[${x}]}
    Check Common Resource Attributes
    Run Optional Data Compare    ${GOLDEN_FILE}   preICMReboot.json
    Cycle    ${CYCLES}   ${icms_uri}
    Run Optional Data Compare    ${GOLDEN_FILE}   postICMReboot.json

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.


*** Keywords ***
Cycle
    [Documentation]   Cycle up a test.
    [Arguments]     ${cycles}   ${icms_uri}
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    :FOR	${x}	IN RANGE	1	${cycles}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n Cycle: ${x} of ${cycles}   console=${True}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   Process ICMs For C7000 ICM Reboot   ${icms_uri}   reboot_sleep=${POST_ICM_REBOOT_SLEEP}   configure_timeout=${ICM_REBOOT_CONFIGURED_WAIT_TIMEOUT}   configure_interval=${ICM_REBOOT_CONFIGURED_WAIT_INTERVAL}   cycle_sleep=${ICM_REBOOT_CYCLE_SLEEP}
    \   Check Common Resource Attributes
    \   Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    \   Check For MeatGrinder Error
    \   Check For Multipath
    \   Check For Server In Read Only Filesystem
    \   common.Run Sequential Ping
    \   Fping Should Have No Loss
    \   Check For ISS Crash
    \   Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}

