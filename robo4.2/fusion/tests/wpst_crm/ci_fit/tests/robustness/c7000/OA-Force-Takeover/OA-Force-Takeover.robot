*** Settings ***
Documentation		OA-Force-Takeover -  Check appliance state, perform OA Force Takeover, and check that check for expected state/status.
...                     pybot -T -d /tmp/logs/OA-Force-Takeover -LTRACE -vENC:CI-FIT-1 -V /root/ci-fit/config_files/ci-fit_robustness_data_variables.py OA-Force-Takeover.robot
...                     Required argument:
...                         -V /root/ci-fit/config_files/robustness_test_data_variables.py
...                         -v HA_FILE:/path/to/your/tcs/HA_file.conf
...                     Optional arguments:
...                         To trigger detailed resource checking, supply -vGOLDEN_FILE:./dataFiles/CI-FIT-1_golden.json
...                            (Run test Generate-Resource-Json.robot to create golden json file.)
...                         To send email notification, use -vEMAIL_TO:<recipient emails separated by ,>
...                         To change the sender's name, use -vEMAIL_FROM:<email address>
...                         To override the default number of cycles, use -vCYCLES:<number of cycles>
...                         To check server multipath based on pre-defined IP-to-path_counts mapping 
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                         REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>

Variables           ../../resources/data_variables.py
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Library		    Collections
Library             ../../../../../../wpst_crm/crm_austin/lib/WPSTUtil.py

Variables           ../../../../../../wpst_crm/crm_austin/resources/defaults.py
Variables           ../../resources/credentials_cifit.py  ${ENC}
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords.txt
Resource            ../../resources/common.robot
Library             ../../resources/robustness-helper.py

*** Variables ***
${CYCLES}                       25
${GOLDEN_FILE}                  None
${EMAIL_FROM}                   ${EMAIL_TO}
${PRE_ACTIVE_BAY}               ${None}
${CURRENT_ACTIVE_BAY}           ${None}
${START_TEST}                   None
${STOP_SCRIPT}                  /root/.stop_script
${SERVER_BONDING_CHECKS}        None
${DISABLE_BONDING_MULTI_TEST}   True
${HA_FILE}                      None
${UPDATE_LFCCACHE}              False
${tbirdEnv}                     None
${REMOTE_CHECKS_TAG}            -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}       &{EMPTY}
@{REMOTE_RUN_CHECKS}            @{EMPTY}
# Below is the OA CLI list for checking on OA side
@{OA_CLIS}                      show enclosure info  show enclosure status  show vcmode  show oa status all  show oa info  show oa info all  show oa network  show oa network all  show interconnect list  show interconnect info all  show server list  show server info all
@{AllResourcesList}             ethNets  fcNets  fcoeNets  ic  ictype  networkset  uplinkset  lig  li  encGrp  encs  servers  profiles  users
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  linkPortIsolated  portStatusReason  mpFirmwareVersion  deviceUri_ADD_mpFirmwareVersion  interconnectIP  mgmtPortState  role  enclosureUris_ADD_standbyOaPreferredIP  settingId  optionId  deviceUri_ADD_romVersion

*** Test Cases ***
Validate Appliance IP And Setup Test
    Authenticate And Set Login
    Set Suite Variable    ${OA_IP}   ${OA_CREDENTIAL_DATA['oaIpAddress']}
    Set Suite Variable    ${OA_USR}  ${OA_CREDENTIAL_DATA['oaUsername']}
    Set Suite Variable    ${OA_PW}   ${OA_CREDENTIAL_DATA['oaPassword']}
    Run Keyword If   "${OA_IP}" == "${EMPTY}"   Fail   msg=OA IP is EMPTY, 
    ...   please specify OA_CREDENTIAL_DATA['oaIpAddress'] in data variable file 
    Run Keyword If   "${OA_USR}" == "${EMPTY}"   Fail   msg=OA USER is EMPTY, 
    ...   please specify OA_CREDENTIAL_DATA['oaUsername'] in data variable file 
    Run Keyword If   "${OA_PW}" == "${EMPTY}"   Fail   msg=OA PASSWORD is EMPTY, 
    ...   please specify OA_CREDENTIAL_DATA['oaPassword'] in data variable file 
    keywords.Log to console and logfile   \n \#\#\# OV Auth: ${AUTHTOKEN} \#\#\#
    keywords.Log to console and logfile   \n \#\#\# Enclosure Name: ${ENC}, Appliance IP: ${OV_IP}, OA IP: ${OA_IP} \#\#\#

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Robustness OA Force Takeover
    Run Keyword If   "${SERVER_BONDING_CHECKS}" != "${Null}" and '${SERVER_HAFILE}' == '${Null}'   Fail   msg=SERVER_BONDING_CHECKS was enabled but SERVER_HAFILE is not set. Please set the SERVER_HAFILE in your pybot command or data variable file.
    Run Keyword If   "${DISABLE_BONDING_MULTI_TEST}" == "${False}" and '${HA_FILE}' == '${Null}' or '${SERVER_HAFILE}' == '${Null}'   Fail   msg=DISABLE_BONDING_MULTI_TEST is False but HA_FILE or SERVER_HAFILE is not set. Please set the HA_FILE and SERVER_HAFILE in your pybot command or data variable file.
    Run Keyword If   "${HA_FILE}" != "${Null}"   OperatingSystem.File Should Exist   ${HA_FILE}
    Variable File Should Be Passed
    Collect Resource Data Status
    Check Common Resource Attributes 
    Run Optional Data Compare    ${GOLDEN_FILE}   preOA-force-takeover.json
    common.Run Sequential Ping
    Fping Should Have No Loss
    Check For ISS Crash
    Cycle    ${CYCLES}
    Collect Resource Data Status 
    Run Optional Data Compare    ${GOLDEN_FILE}   postOA-force-takeover.json

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename}=   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.


*** Keywords ***
Cycle
    [Documentation]   Cycle up a test.
    [Arguments]     ${cycles}
    Log   \n Start OA Force Takeover Test Cycles   console=${True}
    Set Suite Variable    ${START_TEST}   True
    ${oaCmd}=   Create List  show oa status all
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    :FOR   ${x}   IN RANGE   1   ${cycles}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n \#\#\#\#\#\# Cycle: ${x} of ${cycles} \#\#\#\#\#\#   console=${True}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   ${oaStatus}=   OA CLI CMDS    ${oaCmd}   ${OA_IP}   ${OA_USR}   ${OA_PW}
    \   Log  ${oaStatus}
    \   Run Keyword If   '${CURRENT_ACTIVE_BAY}'!='${null}'   Log to console   ==> OA force takeover from Active bay ${CURRENT_ACTIVE_BAY}
    \   ${oaRc}=   OA CLI CMD WITH INTERACTIVE    FORCE TAKEOVER   
    \   ...   ${OA_IP}   ${OA_USR}   ${OA_PW}
    \   ...   Are you sure you want to switch the roles of the Onboard Administrators?   
    \   ...   YES   Logging out
    \   Log   ${oaRc}
    \   Sleep And Log Reason To Console  ${POST_OA_TAKEOVER_SLEEP}   reason=Sleeping ${POST_OA_TAKEOVER_SLEEP} after an OA force takeover.
    \   ${oaStatus}=   OA CLI CMDS    ${oaCmd}   ${OA_IP}   ${OA_USR}   ${OA_PW}
    \   Log  ${oaStatus}
    \   Gather Enclosures Info
    \   Check For MeatGrinder Error
    \   Check For Multipath
    \   Check For Server In Read Only Filesystem
    \   common.Run Sequential Ping
    \   Fping Should Have No Loss
    \   Check For ISS Crash
    \   Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}
    \   Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}

Collect Resource Data Status
    [Documentation]   Get multiple resources data 
    Gather OA Info Via OA CLI
    Gather Appliance Info
    Gather Enclosures Info
    Gather Server VC Info
    Gather Server HW Info
    Gather Server Profiles Info

Gather OA Info Via OA CLI
    [Documentation]   Get OA info using CLI.
    ${oaResults}=   OA CLI CMDS   ${OA_CLIS}   ${OA_IP}   ${OA_USR}   ${OA_PW}

Gather Appliance Info
    [Documentation]   Get appliance information.
    Run Keyword If   "${APPLIANCE_IP}" == "${EMPTY}"     Fail   
    ...   msg=There was a validation error. Please check the validation test case(s) and try again.
    ${resp}=    Fusion Api Get Appliance Version
    ${swVersion}=    Get from Dictionary    ${resp}    softwareVersion
    ${swDate}=    Get from Dictionary    ${resp}    date
    ${resp}=   Fusion Api Get Resource   /rest/appliance/configuration/networkconfig
    ${applName}=    Get from Dictionary    ${resp}    hostname
    keywords.Log to console and logfile    \n \#\#\# Obtaining Appliance Information \#\#\#
    keywords.Log to console and logfile    \n ==> OV Hostname: ${applName}, Version: ${swVersion}, Date: ${swDate}

Gather Enclosures Info
    [Documentation]   Get enclosure information.
    ${oa}=   Get Enclosure Data
    keywords.Log to console and logfile   
    ...  \n ==> Enclosure Name: ${ENC}, State: ${ENCL_STATE}, Refresh State: ${ENCL_REFRESH_STATE}, Status: ${ENCL_STATUS}
    Check Enclosure State
    keywords.Log to console and logfile   \n \#\#\# Obtaining Enclosure ${ENC} OA Information \#\#\#
    Get OA Info   ${oa}

Gather Server VC Info
    [Documentation]   Get interconnects information.
    keywords.Log to console and logfile   \n \#\#\# Gather Server VC Info \#\#\#
    ${resp}=   Fusion Api Get Resource   /rest/interconnects?sort=name:ascending
    ${ics}=   Get From Dictionary   ${resp}   members
    Get Object Info   ${ics}

Gather Server HW Info
    [Documentation]   Get server hardware information.
    keywords.Log to console and logfile   \n \#\#\# Gather Server HW Info \#\#\#
    ${resp}=   Fusion Api Get Resource   /rest/server-hardware?sort=name:ascending
    ${serHWs}=   Get From Dictionary   ${resp}   members
    Get Object Info   ${serHWs}

Gather Server Profiles Info
    [Documentation]   Get server profiles information.
    keywords.Log to console and logfile   \n \#\#\# Gather Server Profiles Info \#\#\#
    ${resp}=   Fusion Api Get Resource   /rest/server-profiles?sort=name:ascending
    ${serProfiles}=   Get From Dictionary   ${resp}   members
    Get Object Info   ${serProfiles}   inProgress

Get Enclosure Data
    [Documentation]   Get enclosure data.
    ${resp}=   Fusion Api Get Resource   /rest/enclosures?filter=name='${ENC}'
    ${encs}=   Get From Dictionary   ${resp}   members
    ${enc_count}=   Get Length   ${encs}
    Should Be Equal   ${enc_count}   ${1}   msg=Failed to get ${ENC} enclosure
    ${en}   Get From List   ${encs}   0

    ${encName}=   Get From Dictionary   ${en}    name
    ${encState}=   Get From Dictionary   ${en}   state
    ${refreshState}=   Get From Dictionary   ${en}   refreshState
    ${encStatus}=   Get From Dictionary   ${en}   status
    Set Suite Variable    ${ENCL_STATE}   ${encState}
    Set Suite Variable    ${ENCL_REFRESH_STATE}   ${refreshState}
    Set Suite Variable    ${ENCL_STATUS}   ${encStatus}
    ${oaVcmMode}=   Get From Dictionary   ${en}    vcmMode
    ${oaActiveIP}=   Get From Dictionary   ${en}   activeOaPreferredIP
    Log to console   
    ...  \n ==> Enclosure Name: ${encName}, Active OA IP: ${oaActiveIP}, State: ${ENCL_STATE}, Refresh State: ${ENCL_REFRESH_STATE}, Status: ${ENCL_STATUS}, vcmMode: ${oaVcmMode}

    ${oa}=   Get From Dictionary   ${en}   managerBays
    [return]   ${oa}

Get OA Info
    [Documentation]   Get Onboard Administrator information.
    [Arguments]     ${oas}
    ${l}=   Get Length   ${oas}
    Log to console    \n ==> Number of OA: ${l}
    :FOR   ${x}   IN RANGE   0   ${l}
    \   ${oaBay}=   Get From Dictionary   ${oas[${x}]}    bayNumber
    \   ${oaIP}=   Get From Dictionary   ${oas[${x}]}    ipAddress
    \   ${oaDevice}=   Get From Dictionary   ${oas[${x}]}    devicePresence
    \   ${oaVer}=   Get From Dictionary   ${oas[${x}]}    fwVersion
    \   ${oaRole}=   Get From Dictionary   ${oas[${x}]}    role
    \   keywords.Log to console and logfile    \n ==> Bay: ${oaBay}, IP: ${oaIP}, Version: ${oaVer}, Role: ${oaRole}, Device: ${oaDevice}
    \   Run Keyword If   '${oaRole}'=='Active' and '${START_TEST}'=='True'   Active OA Action   ${oaBay}
    
Get Object Info
    [Documentation]   Get some object data and print to console and log file.
    [Arguments]     ${obj}   ${alist}=${EMPTY}
    Log  ${obj}
    ${l}=   Get Length   ${obj}
    :FOR   ${x}   IN RANGE   0   ${l}
    \   ${objName}=   Get From Dictionary   ${obj[${x}]}    name
    \   ${objState}=   Get From Dictionary   ${obj[${x}]}    state
    \   ${objStatus}=   Get From Dictionary   ${obj[${x}]}   status
    \   ${objOther}=   Run Keyword Unless   '${alist}'=='${EMPTY}'      Get From Dictionary   ${obj[${x}]}   ${alist}
    \   Run Keyword If   '${alist}'!='${EMPTY}'   
    \   ...     keywords.Log to console and logfile   ==> Name: ${objName}, State: ${objState}, Status: ${objStatus}, InProgress: ${objOther}
    \   ...   ELSE   keywords.Log to console and logfile   ==> Name: ${objName}, State: ${objState}, Status: ${objStatus}

Active OA Action
    [Documentation]   Check that Onboard Administrator role has changed.
    [Arguments]     ${active_bay}
    Log to console   >>> Debugging...PRE_ACTIVE_BAY=${PRE_ACTIVE_BAY}, CURRENT_ACTIVE_BAY=${CURRENT_ACTIVE_BAY}
    Run Keyword If   '${PRE_ACTIVE_BAY}'=='${CURRENT_ACTIVE_BAY}' and '${CURRENT_ACTIVE_BAY}'!='${null}'
    ...   Fail    msg=Same active bay before failover, OA did not get failover
    ...   ELSE    Set Suite Variable    ${PRE_ACTIVE_BAY}  ${CURRENT_ACTIVE_BAY}
    Set Suite Variable   ${CURRENT_ACTIVE_BAY}  ${active_bay}
    Log to console   >>> Debugging...PRE_ACTIVE_BAY=${PRE_ACTIVE_BAY}, CURRENT_ACTIVE_BAY=${CURRENT_ACTIVE_BAY}

Check Enclosure State
    [Documentation]   Check enclosure state.
    [Arguments]   ${NUM_RETRY}=5   ${SLEEP_TIME}=30
    keywords.Log to console and logfile  \n \#\#\# Checking Enclosure State \#\#\#
    Log to console   \n >>> Debugging...Checking OV Enclosure State=${ENCL_STATE}, refreshState=${ENCL_REFRESH_STATE}, and Status=${ENCL_STATUS}
    : FOR   ${retry}   IN RANGE   1   ${NUM_RETRY}+1
    \   ${status_ok}=   Run Keyword If   '${ENCL_STATE}'=='Configured' and '${ENCL_REFRESH_STATE}'=='NotRefreshing'   Set Variable   True
    \   ${en_status}=   Run Keyword If   '${ENCL_STATUS}'=='Warning' or '${ENCL_STATUS}'=='OK'   Set Variable   True
    \   Run Keyword If   '${status_ok}'=='True' and '${en_status}'=='True'   Exit For Loop
    \   ...         ELSE   Sleep And Log Reason To Console   ${SLEEP_TIME}   reason=Sleeping ${SLEEP_TIME} before attempting a check enclosure state retry.
    \   Get Enclosure Data
    Log to console   \n >>> Debugging...Checking OV Status status_ok=${status_ok}, en_status=${en_status}
    Run Keyword If   '${status_ok}'!='True' or '${en_status}'!='True'   Fail
    ...   msg=Enclosure State=${ENCL_STATE}, Status=${ENCL_STATUS}, and Refresh State=${ENCL_REFRESH_STATE} after ${NUM_RETRY} retries with ${SLEEP_TIME} sleep time between each try

