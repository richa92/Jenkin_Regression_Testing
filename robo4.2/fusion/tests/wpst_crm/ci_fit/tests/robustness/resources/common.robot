*** Settings ***
Library        DateTime

*** Keywords ***
################
# Login
################
Authenticate And Set Login
    [Documentation]   Login to OneView and set suite variables appropriately.
    ${APPLIANCE_IP} =   Get Variable Value   ${APPLIANCE_IP}
    Run Keyword If   "${APPLIANCE_IP}" == "${null}"   Fail   msg=Appliance IP is "${APPLIANCE_IP}", please specify APPLIANCE_IP either in data variable file or in the command line argument
    Set Log Level	TRACE
    Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log
    ${Response}    ${AUTHTOKEN}    Fusion Api Login Appliance   ${APPLIANCE_IP}   ${admin_credentials}
    Set Suite Variable   ${AUTHTOKEN}
    Log   ${AUTHTOKEN}   console=${True}
    Set Suite Variable    ${LOGGED}  ${True}
    Set Suite Variable    ${OV_IP}   ${APPLIANCE_IP}
	${tbirdEnv} =   Get Variable Value   ${tbirdEnv}
    Run Keyword If   ${tbirdEnv} == ${null}   Detect Enclosure Type And Set Env
    ${HAFNIUM_MODEL} =   Get Variable Value   ${HAFNIUM_MODEL}
    Set Suite Variable   ${HAFNIUM_MODEL}
    Run Keyword If   '${HAFNIUM_MODEL}' == '${Null}'   Set Hafnium Interconnect Model

Set Api Version To Current
    [Documentation]   Get OV's current API Version and set to use it.
    ${resp} =   Fusion Api Get Resource   /rest/version
    ${X-Api-Version} =   Convert To String   ${resp['currentVersion']}
    Set Suite Variable   ${X-Api-Version}
	
################
# Server Checks
################
Check For MeatGrinder Error
    [Documentation]   SSH to your server blade and grep the latest MeatGrinder log and fail on error.
    [Arguments]   ${string_of_hosts}=${null}
    ${CHECK_MEATGRINDER} =   Run Keyword If   "${string_of_hosts}" == '${null}'   Get Variable Value   ${CHECK_MEATGRINDER}
    ...   ELSE   Set Variable   ${string_of_hosts}
    Return From Keyword If   "${CHECK_MEATGRINDER}" == '${null}'
    ${CHECK_MEATGRINDER} =   Split String   ${CHECK_MEATGRINDER}   ${SPACE}
    ${cmd} =   Set Variable   cat `ls -t ${MEATGRINDER_DIR}/logs/mgerror* | awk '{print($0);exit}'` | grep 'Error [0-9]* '
    ${rc}=   Set Variable   ${1}
    ${failedServers} =   Create List
    ${passedServers} =   Create List
    :FOR   ${serverIP}   IN   @{CHECK_MEATGRINDER}
    \   Log To Console   \n Checking ${serverIP} MeatGrinder log for error...   no_newline=${True}
    \   ${Id}=    Open Connection    ${serverIp}
    \   ${returnStatus}   ${returnMsg} =    Run Keyword And Ignore Error   Login    ${SERVER_USERNAME}   ${SERVER_PASSWORD}
    \   Run Keyword If   "${returnStatus}" == "FAIL"   Log To Console   [${returnMsg}]
    \   Run Keyword If   "${returnStatus}" == "FAIL"   Append To List   ${failedServers}   ${serverIp}
    \   Continue For Loop If   "${returnStatus}" == "FAIL"
    \   ${stdout}    ${stderr}    ${rc} =    Execute Command   ${cmd}   return_stderr=True   return_rc=True
    \   Run Keyword If   ${rc} == 1   Log To Console   [OK]
    \   ...       ELSE   Log To Console   [FAILED]
    \   Run Keyword If   ${rc} == 1   Append To List   ${passedServers}   ${serverIp}
    \   ...       ELSE   Append To List   ${failedServers}   ${serverIp}
    Log   Servers passed: ${passedServers}
    Log   Servers failed: ${failedServers}
    ${e} =   Get Length   ${failedServers}
    Run Keyword If   ${e} != 0    Fail   msg=Servers failed in MeatGrinder check: ${failedServers}
    Close SSH Connection

Check For Multipath
    [Documentation]   SSH to your server blade and check for multipath based on the defined expected counts in your data_variables.py.
    ...               This requires a pre-defined server IP-to-number of multipaths mapping in the data variable file. See ../data_variables.py for example.
    [Arguments]   ${host_mpio_map}=${null}   ${hafnium_icm_model}=${HAFNIUM_MODEL}   ${iface}=eth0
    ${default_icm_data_collection_cmds} =   Run Keyword If   '${tbirdEnv}' == '${True}'   Create List   show clock   show interface description   show clock
    ...                                               ELSE    Create List
    ${HFSH_COMMANDS} =   Get Variable Value   ${HFSH_COMMANDS}   @{default_icm_data_collection_cmds}
    ${icm_names} =   Get All Interconnects Name By Model   ${hafnium_icm_model}
    Enter Into Hafnium Shell And Write Commands   ${icm_names}   hfsh_cmds=${HFSH_COMMANDS}   iface=${iface}
    ${CHECK_MULTIPATH} =   Run Keyword If   "${host_mpio_map}" == '${null}'   Get Variable Value   ${CHECK_MULTIPATH}
    ...   ELSE   Set Variable   ${host_mpio_map}
    Return From Keyword If   ${CHECK_MULTIPATH} is ${null}
    ${l} =  Get Length  ${CHECK_MULTIPATH}
    Return From Keyword If   ${l} == 0
    ${serverItems}=    Get Dictionary Items    ${CHECK_MULTIPATH}
    ${rc}=   Set Variable   ${1}
    ${failedServers} =   Create List
    ${passedServers} =   Create List
    :FOR  ${serverIP}  ${paths}    IN  @{serverItems}
    \   Log To Console   \n Checking server ${serverIp} multipath...   no_newline=${True}
    \   ${cmd} =   Set Variable   ${MULTIPATH_SCRIPT} ${paths}
    \   ${Id}=    Open Connection    ${serverIP}
    \   ${returnStatus}   ${returnMsg} =    Run Keyword And Ignore Error   Login    ${SERVER_USERNAME}   ${SERVER_PASSWORD}
    \   Run Keyword If   "${returnStatus}" == "FAIL"   Log To Console   [${returnMsg}]
    \   Run Keyword If   "${returnStatus}" == "FAIL"   Append To List   ${failedServers}   ${serverIp}
    \   Continue For Loop If   "${returnStatus}" == "FAIL"
    \   ${stdout}    ${stderr}    ${rc} =    Execute Command   ${cmd}   return_stderr=True   return_rc=True
    \   Run Keyword If   ${rc} == 1   Log To Console   [OK]
    \   ...       ELSE   Log To Console   [FAILED]
    \   Run Keyword If   ${rc} == 1   Append To List   ${passedServers}   ${serverIp}
    \   ...       ELSE   Append To List   ${failedServers}   ${serverIp}
    Log   Servers passed: ${passedServers}
    Log   Servers failed: ${failedServers}
    ${e} =   Get Length   ${failedServers}
    Run Keyword If   ${e} != 0    Fail   msg=Servers failed in multipath check: ${failedServers}
    Close SSH Connection

Check For Server In Read Only Filesystem
    [Documentation]   SSH to your server blade and test if it is in read-only filesystem.
    [Arguments]   ${string_of_hosts}=${null}
    ${CHECK_READONLY} =   Run Keyword If   "${string_of_hosts}" == '${null}'   Get Variable Value   ${CHECK_READONLY}
    ...   ELSE   Set Variable   ${string_of_hosts}
    Return From Keyword If   "${CHECK_READONLY}" == '${null}'
    ${CHECK_READONLY} =   Split String   ${CHECK_READONLY}   ${SPACE}
    ${cmd} =   Set Variable   mount | grep 'mount: warning: /etc/mtab is not writable (e.g. read-only filesystem)'
    ${rc}=   Set Variable   ${1}
    ${failedServers} =   Create List
    ${passedServers} =   Create List
    :FOR   ${serverIP}   IN   @{CHECK_READONLY}
    \   Log To Console   \n Checking server ${serverIp} for read-only...   no_newline=${True}
    \   ${Id}=    Open Connection    ${serverIP}
    \   ${returnStatus}   ${returnMsg} =    Run Keyword And Ignore Error   Login    ${SERVER_USERNAME}   ${SERVER_PASSWORD}
    \   Run Keyword If   "${returnStatus}" == "FAIL"   Log To Console   [${returnMsg}]
    \   Run Keyword If   "${returnStatus}" == "FAIL"   Append To List   ${failedServers}   ${serverIp}
    \   Continue For Loop If   "${returnStatus}" == "FAIL"
    \   ${stdout}    ${stderr}    ${rc} =    Execute Command   ${cmd}   return_stderr=True   return_rc=True
    \   Run Keyword If   ${rc} == 1   Log To Console   [OK]
    \   ...       ELSE   Log To Console   [FAILED]
    \   Run Keyword If   ${rc} == 1   Append To List   ${passedServers}   ${serverIp}
    \   ...       ELSE   Append To List   ${failedServers}   ${serverIp}
    Log   Servers passed: ${passedServers}
    Log   Servers failed: ${failedServers}
    ${e} =   Get Length   ${failedServers}
    Run Keyword If   ${e} != 0    Fail   msg=Servers failed in read only FS check: ${failedServers}
    Close SSH Connection

Run Sequential Ping
    [Documentation]   Run sequential ping from TCS to blades.
    ...               PING_HAFILE variable must be set to the path of your HA file.
    ...               Optional argument:
    ...                   script - path to your sequential ping script.
    [Arguments]   ${script}=${SEQUENTIAL_PING_SCRIPT}   ${target_ha_file}=${null}
    ${PING_HAFILE} =   Run Keyword If   "${target_ha_file}" == '${null}'   Get Variable Value   ${PING_HAFILE}
    ...   ELSE   Set Variable   ${target_ha_file}
    Return From Keyword If   "${PING_HAFILE}" == "${null}"
    Log To Console   \n Running sequential ping (ping logs are in /tmp, use tail to monitor the test)...   no_newline=${True}
    ${rc} =   Run And Return RC  ${script} ${PING_HAFILE} >/dev/null
    Run Keyword If   ${rc} == 1  Log To Console   [OK]
    ...       ELSE  Fail  msg=Check the sequential ping log for info.

Server Interfaces Should Be Up
    [Documentation]   Check that server interfaces are up.
    [Arguments]   ${string_of_hosts}=${null}
    ${CHECK_INTERFACE} =   Run Keyword If   "${string_of_hosts}" == '${null}'   Get Variable Value   ${CHECK_INTERFACE}
    ...   ELSE   Set Variable   ${string_of_hosts}
    Return From Keyword If   "${CHECK_INTERFACE}" == '${null}'
    ${CHECK_INTERFACE} =   Split String   ${CHECK_INTERFACE}   ${SPACE}
    ${cmd} =   Set Variable   ${null}
    ${failedServers} =   Create List
    ${passedServers} =   Create List
    :FOR   ${serverIP}   IN   @{CHECK_INTERFACE}
    \   Log To Console   \n Checking server ${serverIp} interfaces...   no_newline=${True}
    \   ${Id}=    Open Connection    ${serverIP}
    \   ${Output}=    Login    ${SERVER_USERNAME}   ${SERVER_PASSWORD}
    \   ${stdout}   ${stderr}   ${rc} =   Execute Command   cat /etc/redhat-release | grep 'Red Hat Enterprise Linux Server release 6' >/dev/null 2>&1   return_stderr=True   return_rc=True
    \   Run Keyword If   ${rc} == 0   Set Test Variable   ${cmd}   cat /sys/class/net/eth*/operstate | grep 'down' > /dev/null 2>&1
    \   ${stdout}   ${stderr}   ${rc} =   Run Keyword If   "${cmd}" == '${null}'   Execute Command   cat /etc/redhat-release | grep 'Red Hat Enterprise Linux Server release 7' >/dev/null 2>&1   return_stderr=True   return_rc=True
    \   Run Keyword If   ${rc} == 0   Set Test Variable   ${cmd}   cat /sys/class/net/ens*/operstate | grep 'down' > /dev/null 2>&1
    \   ...    ELSE IF   "${cmd}" == '${null}'   Fail   msg=Unable to recognize the OS. It appeared that it needs to be added in the supported OS logic.
    \   ${stdout}   ${stderr}   ${rc} =    Execute Command   ${cmd}   return_stderr=True   return_rc=True
    \   Run Keyword If   ${rc} == 0   Log To Console   [FAILED]
    \   ...    ELSE IF   ${rc} == 1   Log To Console   [OK]
    \   ...       ELSE   Log To Console   [UNABLE TO CHECK INTERFACE: ${rc}]
    \   Run Keyword If   ${rc} == 0   Append To List   ${failedServers}   ${serverIp}
    \   ...       ELSE   Append To List   ${passedServers}   ${serverIp}
    Log   Servers passed: ${passedServers}
    Log   Servers failed: ${failedServers}
    ${e} =   Get Length   ${failedServers}
    Run Keyword If   ${e} != 0    Log To Console   msg=Servers failed in interface check: ${failedServers}
    Close SSH Connection

Parse Bonding Interface And Collect Server Tcpdump
    [Documentation]   Parse server Slave Interfaces from bonding and collect tcpdump.
    [Arguments]   ${ipAddr}   ${bonding}   ${slaveInterfaces}   ${userName}=root   ${password}=rootpwd
    ${bondInterfaces} =   Create List
    :FOR   ${s}   IN   @{slaveInterfaces}
    \   ${sIface} =   Split String   ${s}
    \   Append To List   ${bondInterfaces}   ${sIface[2]}
    Put File To Remote Host   ${ipAddr}   ${userName}   ${password}   ${REPO_SERVER_SCRIPTS_DIR}/${TCPDUMP_SCRIPT}   ${SERVER_SCRIPTS_DIR}/${TCPDUMP_SCRIPT}   keepConnection=${True}
    ${stdout}   ${stderr}   ${rc} =   Execute Command   /root/tools/scripts/${TCPDUMP_SCRIPT} ${bonding} ${bondInterfaces[0]} ${bondInterfaces[1]} &   return_stderr=True   return_rc
    Close All Connections

Collect Debugging Data
    [Documentation]   Get some interface data from TCS and server blade.
    [Arguments]   ${fpingLossLog}   ${serverUserName}=root   ${serverPassword}=rootpwd
    ${count} =   Set Variable   ${0}
    ${lossCount} =   Get Length   ${fpingLossLog}
    :FOR   ${f}   IN   @{fpingLossLog}
    \   Continue For Loop If   "${f}" == ""
    \   ${loss} =   Split String   ${f}   ,
    # server blade IP address
    \   ${ipAddr} =   Set Variable   ${loss[0]}
    \   ${ipAddr} =   Strip String   ${ipAddr}   characters=['
    \   ${vlanId} =   Set Variable   ${loss[2]}
    \   ${vlanId} =   Strip String   ${vlanId}   characters='
    \   ${network} =   Split String   ${ipAddr}   .
    \   ${output} =   Run   ip r show|grep " src "| grep -w ${network[0]}.${network[1]}.${network[2]}.1
    \   ${ipShow} =   Split String   ${output}
    \   ${aliasIface} =   Set Variable  ${ipShow[2]}
    \   ${aliasIface} =   Split String   ${aliasIface}   characters=.
    \   ${interface} =   Set Variable   ${aliasIface[0]}
    \   ${tcsVlanId} =   Get Variable Value   ${aliasIface[1]}   X
    # collecting tcs tcpdump data
    \   ${output} =   Run   /root/tools/scripts/tcpdump_capture_tcs.sh ${interface} ${tcsVlanId} &
    # collecting blade tcpdump data
    \   Open Connection   ${ipAddr}   timeout=15m
    \   Login   ${serverUserName}   ${serverPassword}
    \   ${stdout}   ${stderr}   ${rc} =   Execute Command   ip r show|grep " src "| grep -w ${ipAddr}   return_stderr=True   return_rc=True
    \   ${ipShow} =   Split String   ${stdout}
    \   ${aliasIface} =   Set Variable  ${ipShow[2]}
    \   ${aliasIface} =   Split String   ${aliasIface}   characters=.
    \   ${bondingIface} =   Set Variable   ${aliasIface[0]}
    \   ${stdout}   ${stderr}   ${rc} =   Execute Command   cat /proc/net/bonding/${bondingIface} | grep Interface   return_stderr=True   return_rc=True
    \   Close All Connections
    \   ${interfaces} =   Split String   ${stdout}   ${\n}
    \   Parse Bonding Interface And Collect Server Tcpdump   ${ipAddr}   ${bondingIface}   ${interfaces}
    \   ${count} =   Run Keyword If   ${count} < ${lossCount} and ${count} != ${2}   Evaluate   ${count}+1
    \   ...                    ELSE   ${count}
    \   Run Keyword If   ${count} == ${lossCount} or ${count} == ${2}   OperatingSystem.Create File   ${STOP_SCRIPT}
    \   Run Keyword If   ${count} == ${lossCount} or ${count} == ${2}   Fail   msg=fping loss detected and debugging data were collected.

Fping Should Have No Loss
    [Documentation]   Fail if fping log has packet loss greater than or equal to specified argument in the get-all-continuous-fping-loss.py -m option.
    ${CHECK_FPING_LOSS} =   Get Variable Value   ${CHECK_FPING_LOSS}   ${False}
    Return From Keyword If   ${CHECK_FPING_LOSS} is not ${True}
    ${rc}   ${o} =   Execute Command And Check For Error   ${FPING_HOST_IP}   ${FPING_HOST_USERNAME}   ${FPING_HOST_PASSWORD}   ${GET_FPING_LOSS_CMD}   verbose=${True}
    ${o} =   Split String   ${o}   ${\n}
    ${l} =   Get Length   ${o}
    Run Keyword If   ${l} >= 1   Collect Debugging Data   ${o}

Run Remote Check Servers Script
    [Documentation]   SSH to remote host (TCS) and run Check-Servers.robot script.
    [Arguments]   ${remote_run_data}   ${offline_interconnect}=${Null}   ${upd_lfccache}=False   ${tags}=-i PING -i BONDING_MULTI_TEST
    :FOR   ${remote}   IN   @{remote_run_data}
    \   ${rc}   ${o} =   Execute Command And Check For Error   ${remote['host']}   ${remote['username']}   ${remote['password']}   rm -f ${STOP_SCRIPT}   verbose=${True}
    \   ${now} =   Get Time   year month day hour min sec   NOW
    \   ${now}=  Evaluate  "".join($now)
    \   ${rc}   ${o} =   Execute Command And Check For Error   ${remote['host']}   ${remote['username']}   ${remote['password']}   cd ${remote['command']['scriptLocation']} && pybot -d /tmp/logs/${remote['command']['logDir']} -l /tmp/logs/${remote['command']['logDir']}/log-${now}.html -L TRACE -vREMOTE_RUN:True -vUPDATE_LFCCACHE:${upd_lfccache} -v HA_FILE:${remote['command']['haFile']} -vAPPLIANCE_IP:${APPLIANCE_IP} -vPOTASH_URI:${offline_interconnect} -V ${remote['command']['dataFile']} ${tags} ${remote['command']['script']}   verbose=${True}
    \   Run Keyword If   ${rc} != ${0}   Fail   msg=Something failed trying to run ${remote['command']} in ${remote['host']}.
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Fail   msg=Remote bonding interface checks failed. Please check RG log at http://${remote['host']}/rg_logs/${remote['command']['logDir']}/log-${now}.html

################
# Data Compare
################
Run Optional Data Compare
    [Documentation]   When golden file is provided or defined, it will generate your OneView resource data, compare it to your golden file and fail on mismatch.
    [Arguments]   ${golden_file}   ${current_file}
    Run Keyword If   "${golden_file}" != "${null}"   Generate OneView Resource Data And Compare    ${golden_file}   ${current_file}   moreIgnoreList=${ignoreList}   tbirdEnv=${tbirdEnv}   AllResourcesList=${AllResourcesList}

Run Optional Alternating Data Compare
    [Documentation]   When two golden files are provided or defined, it will generate your OneView resource data, alternately compare between the two golden files and fail on mismatch.
    ...               Commonly used on failovers that could result in two different resource data (EM Failover).
    [Arguments]   ${cycleCount}   ${currentJson}   ${golden_file_1}   ${golden_file_2}
    Run Keyword If   "${golden_file_1}" != "${null}" and "${golden_file_2}" != "${null}"   Generate OneView Resource Data And Switch Between Compare Files      ${cycleCount}    ${currentJson}   ${golden_file_1}   ${golden_file_2}

Generate OneView Resource Data And Switch Between Compare Files
    [Documentation]   This is to be able to switch between 2 compare files for data compare after a failover.
    [Arguments]   ${cycleCount}   ${currentJson}   ${golden_file_1}   ${golden_file_2}
    ${eval} =   Evaluate   ${cycleCount} % 2
    Run Keyword If  ${eval} == 0   Generate OneView Resource Data And Compare    ${golden_file_1}   ${currentJson}   moreIgnoreList=${ignoreList}   tbirdEnv=${tbirdEnv}   AllResourcesList=${AllResourcesList}
    ...       ELSE   Generate OneView Resource Data And Compare    ${golden_file_2}   ${currentJson}   moreIgnoreList=${ignoreList}   tbirdEnv=${tbirdEnv}   AllResourcesList=${AllResourcesList}

################
# Basic Resource Checks - OneView
################
Check Common Resource Attributes
    [Documentation]   Check that enclosures, interconnects, logical interconnects are in expected states based on DTO defined in the data variable file.
    [Arguments]   ${maxRetry}=${10}   ${retryInterval}=1m
    Enclosure Should Be In Expected State   maxRetry=${maxRetry}   retryInterval=${retryInterval}
    Logical Enclosure Should Be In Expected State   maxRetry=${maxRetry}   retryInterval=${retryInterval}
    Interconnect Should Be In Expected State   maxRetry=${maxRetry}   retryInterval=${retryInterval}
    Logical Interconnect Should Be In Expected State   maxRetry=${maxRetry}   retryInterval=${retryInterval}

################
# Enclosure Checks - OneView
################
Enclosure Should Be In Expected State
    [Documentation]   Check that enclosures are in expected states based on the DTO defined in the data variable file.
    [Arguments]   ${maxRetry}=${10}   ${retryInterval}=1m
    :FOR   ${retry}   IN RANGE   1   ${maxRetry}+1
    \   ${result} =   Compare Enclosure Attributes To Expected Values
    \   Run Keyword If   '${result}' == '${True}'   Exit For Loop
    \   ...    ELSE IF   ${retry} != ${maxRetry}   Sleep And Log Reason To Console   ${retryInterval}   reason=One or more enclosure attribute is not in the expected value. Sleeping for ${retryInterval} before a retry...
    \   ...       ELSE   Fail   msg=One or more enclosure attribute is not in the expected value and ${maxRetry} retries were exhausted.
    Log   \n Enclosures attributes compare completed in ${retry} attempt(s)   console=${True}

Compare Enclosure Attributes To Expected Values
    [Documentation]   Check that enclosures are in expected states. Returns boolean.
    Log   \n Checking OV Enclosures State...   console=${True}
    ${resp}=   Fusion Api Get Resource   /rest/enclosures
    ${encs}=   Get From Dictionary   ${resp}   members
    ${l}=   Get Length   ${encs}
    :FOR   ${x}   IN RANGE   0   ${l}
    \   ${encName}=   Get From Dictionary   ${encs[${x}]}    name
    \   ${enc} =   Evaluate   $ENCLOSURES.get($encName, {})
    \   Run Keyword If   ${enc} == &{EMPTY}   Log    Your data variable file ENCLOSURES dictionary does not contain '${encName}'.   WARN   console=${True}
    \   Log   \n \#\#\# Checking some attributes of enclosure ${encName} \#\#\#   console=${True}
    \   ${encExpected} =   Run Keyword If   ${enc} != &{EMPTY}   Check Data   ${enc}   ${encs[${x}]}
    \   ${emBaysExpected} =   Compare Enclosure Manager Attributes To Expected Values   ${encs[${x}]}
    \   Return From Keyword If   ${emBaysExpected} == ${False} or '${encExpected}' == '${False}'   ${False}
    [Return]   ${True}

Compare Enclosure Manager Attributes To Expected Values
    [Documentation]   Check that enclosure manager attributes are in expected states. Returns boolean.
    ...               Required argument is enclosures->members[${i}] dictionary value
    ...               Returns true on matching expected values. Otherwise, false
    [Arguments]   ${enc}   ${expectedDevicePresence}=Present   ${expectedLinkPortState}=Linked   ${expectedLinkPortStatus}=OK   ${expectedStatus}=OK
    ${emRoles} =   Create List   Active   Standby
    ${emBays} =   Create List   ${1}   ${2}
    :FOR   ${x}   IN RANGE   1   3
    \   ${encName} =   Get From Dictionary   ${enc}   name
    \   ${encMgrBay} =   Get Enclosure Manager Bay Data   ${enc}   ${x}
    \   ${bayNumber} =   Get From Dictionary   ${encMgrBay}   bayNumber
    \   ${role} =   Get From Dictionary   ${encMgrBay}   role
    \   ${devicePresence} =   Get From Dictionary   ${encMgrBay}   devicePresence 
    \   ${linkPortState} =   Run Keyword If   ${tbirdEnv} == ${True}   Get From Dictionary   ${encMgrBay}   linkPortState
    \   ${linkPortStatus} =   Run Keyword If   ${tbirdEnv} == ${True}   Get From Dictionary   ${encMgrBay}   linkPortStatus
    \   ${status} =   Run Keyword If   ${tbirdEnv} == ${True}   Get From Dictionary   ${encMgrBay}   status
    \   Log   \n \#\#\# Checking some attributes of enclosure manager for ${encName} \#\#\#   console=${True}
    \   Log   EM Bay Number: ${x}, Role: ${role}, Device Presence: ${devicePresence}, Link Port State: ${linkPortState}, Link Port Status: ${linkPortStatus}, Status: ${status}   console=${True}
    \   ${expectedRole}   ${emRoles} =   List Should Contain Value To Remove   ${emRoles}   ${role}
    \   ${expectedBay}   ${emBays} =   List Should Contain Value To Remove   ${emBays}   ${bayNumber}
    \   Return From Keyword If   '${expectedRole}'!='${role}' or '${expectedBay}'!='${bayNumber}' or '${expectedDevicePresence}'!='${devicePresence}'   ${False}
    \   Continue For Loop If   ${tbirdEnv} == ${False}
    \   Return From Keyword If   '${expectedLinkPortState}'!='${linkPortState}' or '${expectedLinkPortStatus}'!='${linkPortStatus}' or '${expectedStatus}'!='${status}'   ${False}
    [Return]   ${True}

Enclosure Manager Should Be In Expected State
    [Documentation]   Compare enclosure manager attributes to the expected values. Fail on mismatch.
    [Arguments]   ${encName}   ${emBayNumber}   ${expectedRole}   ${expectedDevicePresence}=Present   ${expectedLinkPortState}=Linked   ${expectedLinkPortStatus}=OK   ${expectedStatus}=OK   ${maxRetry}=${10}   ${retryInterval}=1m
    Set Test Variable   ${failTest}   ${False}
    :FOR   ${retry}   IN RANGE   1   ${maxRetry}+1
    \   ${resp} =   Fusion Api Get Resource   /rest/enclosures
    \   ${enc} =   Get Enclosure Match   ${resp}   ${encName}
    \   ${encMgrBay} =   Get Enclosure Manager Bay Data   ${enc}   ${emBayNumber}
    \   ${role} =   Get From Dictionary   ${encMgrBay}   role 
    \   ${devicePresence} =   Get From Dictionary   ${encMgrBay}   devicePresence 
    \   ${linkPortState} =   Get From Dictionary   ${encMgrBay}   linkPortState
    \   ${linkPortStatus} =   Get From Dictionary   ${encMgrBay}   linkPortStatus
    \   ${status} =   Get From Dictionary   ${encMgrBay}   status
    \   Log   \n \#\#\# Checking some attributes of enclosure manager ${encName} \#\#\#   console=${True}
    \   Log   Enclosure Name: ${encName}, Bay Number: ${emBayNumber}, Role: ${role}, Device Presence: ${devicePresence}, Link Port State: ${linkPortState}, Link Port Status: ${linkPortStatus}, Status: ${status}   console=${True}
    \   Run Keyword If   '${role}'!='${expectedRole}' or '${devicePresence}'!='${expectedDevicePresence}' or '${linkPortState}'!='${expectedLinkPortState}' or '${linkPortStatus}'!='${expectedLinkPortStatus}' or '${status}'!='${expectedStatus}'  Set Test Variable   ${failTest}   ${True}
    \   ...       ELSE   Exit For Loop
    \   Run Keyword If   ${retry} != ${maxRetry}   Sleep And Log Reason To Console   ${retryInterval}   reason=One or more enclosure manager attribute is not in the expected value. Sleeping for ${retryInterval} before a retry...
    Log   \n Enclosure manager attributes compare completed in ${retry} attempt(s)   console=${True}
    Run Keyword If   '${failTest}' == '${True}'   Fail   msg=One or more enclosure manager attribute is not in the expected value during validation.
    
Get Enclosure Manager Bay Data
   [Documentation]   Get enclosure manager bay data from OneView enclosures->members[${i}] dictionary value
   [Arguments]   ${enc}   ${bayNumber}
   Set Test Variable   ${bayFound}   ${False}
   ${emBays} =   Get From Dictionary   ${enc}   managerBays
   ${l} =   Get Length   ${emBays}
   :FOR   ${x}   IN RANGE   0   ${l}
   \   Run Keyword If   ${emBays[${x}]['bayNumber']} == ${bayNumber}   Set Test Variable   ${bayFound}   ${True}
   \   Run Keyword If   ${emBays[${x}]['bayNumber']} == ${bayNumber}   Exit For Loop
   Run Keyword If   '${bayFound}' == '${False}'   Fail   msg=Bay number ${bayNumber} was not found in managerBays->bayNumber.
   [Return]   ${emBays[${x}]}

Get Enclosure Match
   [Documentation]   Find enclosure match from the response body and return it.
   [Arguments]   ${resp}   ${encName}
   ${encs} =   Get From Dictionary   ${resp}   members
   ${l} =    Get Length   ${encs}
   :FOR   ${x}   IN RANGE   0   ${l}
   \   Log   ${encs[${x}]}
   \   Return From Keyword If   '${encName}' in '${encs[${x}]['name']}'   ${encs[${x}]}

################
# Logical Enclosure Checks - OneView
################
Logical Enclosure Should Be In Expected State
    [Documentation]   Check that logical enclosures are in expected states based on the DTO defined in the data variable file.
    [Arguments]   ${maxRetry}=${10}   ${retryInterval}=1m
    :FOR   ${retry}   IN RANGE   1   ${maxRetry}+1
    \   ${result} =   Compare Logical Enclosure Attributes To Expected Values
    \   Run Keyword If   '${result}' == '${True}'   Exit For Loop
    \   ...    ELSE IF   ${retry} != ${maxRetry}   Sleep And Log Reason To Console   ${retryInterval}   reason=One or more logical enclosure attribute is not in the expected value. Sleeping for ${retryInterval} before a retry...
    \   ...       ELSE   Fail   msg=One or more logical enclosure attribute is not in the expected value and ${maxRetry} retries were exhausted.
    Log   \n Logical enclosures attributes compare completed in ${retry} attempt(s)   console=${True}

Compare Logical Enclosure Attributes To Expected Values
    [Documentation]   Check that logical enclosures are in expected states. Returns boolean.
    Log   \n Checking OV Logical Enclosures State...   console=${True}
    ${resp}=   Fusion Api Get Resource   /rest/logical-enclosures
    ${les}=   Get From Dictionary   ${resp}   members
    ${l}=   Get Length   ${les}
    :FOR   ${x}   IN RANGE   0   ${l}
    \   ${leName}=   Get From Dictionary   ${les[${x}]}    name
    \   ${le} =   Evaluate   $LOGICAL_ENCLOSURES.get($leName, {})
    \   Run Keyword If   ${le} == &{EMPTY}   Log    Your data variable file LOGICAL_ENCLOSURES dictionary does not contain '${leName}'.   WARN   console=${True}
    \   Log   \n \#\#\# Checking some attributes of logical enclosure ${leName} \#\#\#   console=${True}
    \   ${leExpected} =   Run Keyword If   ${le} != &{EMPTY}   Check Data   ${le}   ${les[${x}]}
    \   Return From Keyword If   '${leExpected}' == '${False}'   ${False}
    [Return]   ${True}

################
# Interconnect Checks - OneView
################
Interconnect Should Be In Expected State
    [Documentation]   Check that interconnects are in expected states with retry. Fail on mismatch.
    [Arguments]   ${maxRetry}=${10}   ${retryInterval}=1m
    :FOR   ${retry}   IN RANGE   1   ${maxRetry}+1
    \   ${result} =   Compare Interconnect Attributes To Expected Values
    \   Run Keyword If   '${result}' == '${True}'   Exit For Loop
    \   ...    ELSE IF   ${retry} != ${maxRetry}   Sleep And Log Reason To Console   ${retryInterval}   reason=One or more interconnect attribute is not in the expected value. Sleeping for ${retryInterval} before a retry...
    \   ...       ELSE   Fail   msg=One or more interconnect attribute is not in the expected value and ${maxRetry} retries were exhausted.
    Log   \n Interconnects attributes compare completed in ${retry} attempt(s)   console=${True}

Compare Interconnect Attributes To Expected Values
    [Documentation]   Check that interconnects attributes are in expected values. Returns boolean.
    Log   \n Checking OV Interconnects State...   console=${True}
    ${resp}=   Fusion Api Get Resource   /rest/interconnects
    ${icms}=   Get From Dictionary   ${resp}   members
    # build stacking domain roles expectations based on number of potash
    ${count} =   Set Variable   ${0}
    :FOR   ${i}   IN   @{icms}
    \   Continue For Loop If   '${i['model']}' != '${HAFNIUM_MODEL}'
    \   ${count} =   Evaluate   ${count}+1
    ${eval} =   Evaluate   ${count} % 2
    Should Be Equal   ${eval}   ${0}   msg=Not all Hafnium ICMs are in the expected stackingDomainRole.
    ${expectedRoles}=   Create List   Subordinate   Master
    ${stackingDomainRoles}=   Create List
    :FOR   ${c}   IN RANGE   1   ${count}+1
    \   ${eval} =   Evaluate   ${c} % 2
    \   Append To List   ${stackingDomainRoles}   ${expectedRoles[${eval}]}
    ${l}=   Get Length   ${icms}
    :FOR   ${x}   IN RANGE   0   ${l}
    # There is an open issue in RF than when fixed can give us flexibilty of changing data variable file on the fly.
    # https://github.com/robotframework/robotframework/issues/2101
    # \   Re-import Data Variable Files   ${data_variable_files}
    \   ${icmName}=   Get From Dictionary   ${icms[${x}]}    name
    \   ${icm} =   Evaluate   $INTERCONNECTS.get($icmName, {})
    \   Run Keyword If   ${icm} == &{EMPTY}   Log    Your data variable file INTERCONNECTS does not contain '${icmName}'.   WARN   console=${True}
    \   Log   \n \#\#\# Checking some attributes of interconnect ${icmName} \#\#\#   console=${True}
    \   ${icmExpected} =   Run Keyword If   ${icm} != &{EMPTY}   Check Data   ${icm}   ${icms[${x}]}
    \   ${icmModel}=   Get From Dictionary   ${icms[${x}]}   model
    \   ${icmStackingDomainRole}=   Get From Dictionary   ${icms[${x}]}   stackingDomainRole
    \   Return From Keyword If   '${icmExpected}' == '${False}'   ${False}
    # do this on Potash only
    \   ${expectedDomainRole}   ${stackingDomainRoles} =   Run Keyword If   '${icmModel}' == '${HAFNIUM_MODEL}'   List Should Contain Value To Remove   ${stackingDomainRoles}   ${icmStackingDomainRole}
    \   ...                                                          ELSE   Set Variable   ${null}   ${stackingDomainRoles}
    \   Continue For Loop If   ${tbirdEnv} == ${False} or '${expectedDomainRole}' == '${null}'
    \   Return From Keyword If   '${expectedDomainRole}'!='${icmStackingDomainRole}'   ${False}
    [Return]   ${True}

List Should Contain Value To Remove
    [Documentation]   Fail if value does not exist in the list. Returns new list.
    [Arguments]   ${list}   ${value}
    ${n} =   Get Length   ${list}
    Run Keyword If   ${n} == ${1}   Set Test Variable   ${expectedValue}   ${list[0]}
    ...       ELSE   Set Test Variable   ${expectedValue}   ${value}
    List Should Contain Value   ${list}   ${value}
    ${i} =   Get Index From List   ${list}   ${value}
    Remove From List   ${list}   ${i}
    [Return]   ${expectedValue}   ${list}

Protocol Should Be In Lag States
    [Documentation]   Check that protocol matched to that of uplink sets.
    [Arguments]   ${protocol}   ${uplinkPortAttrs}
    :FOR   ${u}   IN   @{uplinkPortAttrs}
    \   ${passed} =    Run Keyword And Return Status   Evaluate    type(${u['lagStates']})
    \   ${type} =      Run Keyword If     ${passed}    Evaluate    type(${u['lagStates']})
    \   ${resp} =   Run Keyword If   "${type}" == "<type 'list'>"   List Should Contain Value   ${u['lagStates']}   ${LAG_STATES['${protocol}']}   msg=${LAG_STATES['${protocol}']} was not found in uplink sets lagStates: ${u['lagStates']}.
    \   ...                   ELSE   Fail   msg=lagStates attribute is not a list(lagStates: ${u['lagStates']}) for this uplink port attributes: ${u}.

Convert Uplink Sets Attributes To Hafnium Equivalent
    [Documentation]   Convert uplink-sets attributes (portName, interconnectName, operationSpeed) into hafnium equivalent.
    [Arguments]    ${uplinkSetsAttrs}
    ${ovPorts} =   Create List
    :FOR   ${a}   IN   @{uplinkSetsAttrs}
    \   ${portName} =   Strip String   ${a['portName']}   characters=Q
    \   ${icmName} =   Set Variable   ${INTERCONNECT_NAME['${a['interconnectName']}']}
    \   ${opSpeed} =   Set Variable   ${OPERATIONAL_SPEED['${a['operationalSpeed']}']}
    \   Append To List   ${ovPorts}   ${opSpeed}${icmName}/${portName}(P)
    [Return]   ${ovPorts}

Ports Should Match With Uplink Sets
    [Documentation]   Check that show ether summary ports matched with OneView uplink sets portName, interconnectName, operationSpeed.
    [Arguments]   ${ports}   ${uplinkSetsAttrs}
    ${combinedPorts} =   Create List
    :FOR   ${p}   IN   @{ports}
    \   ${splitPorts} =   Split String   ${p}   ,
    \   ${combinedPorts} =   Combine Lists   ${combinedPorts}   ${splitPorts}
    List Should Not Contain Duplicates   ${combinedPorts}
    ${l} =   Get Length   ${uplinkSetsAttrs}
    Length Should Be   ${combinedPorts}   ${l}   msg=Number of ports reflected in the show ether summary does not match with OneView uplink-sets for lagId:${uplinkSetsAttrs[0]['lagId']}.
    ${ovPorts} =   Convert Uplink Sets Attributes To Hafnium Equivalent   ${uplinkSetsAttrs}
    List Should Not Contain Duplicates   ${ovPorts}
    # compare OV and Hafnium
    Collections.Sort List   ${combinedPorts}
    Collections.Sort List   ${ovPorts}
    Lists Should Be Equal   ${combinedPorts}   ${ovPorts}
    # compare both OV and Hafnium to data variable file
    List Should Contain Sub List   ${EXPECTED_PORTS}   ${combinedPorts}

Ether Summary Should Match With Uplink Sets
    [Documentation]   Compare hafnium ether summary data to that of OneView uplink sets and verify some uplink sets attributes.
    ...               Accepts dictionary of ether summary data like: {'2': {'lagId': 2, 'portChannel': 'Po2(U)[AU,OU]','ports': ['Ten-GigabitEthernet0/0/1:1(P),Ten-GigabitEthernet0/0/1:2(P)', 'Ten-GigabitEthernet1/0/1:1(P),Ten-GigabitEthernet1/0/1:2(P)'], 'protocol': 'LACP'}
    ...               Accepts dictionary of uplink-sets list data like: {u'2': [{'portStatus': u'Linked', 'lagId': 2, 'lagStates': [u'LacpActivity', u'Aggregation', u'Synchronization', u'Collecting', u'Distributing'], 'portName': u'Q1:2', 'interconnectName': u'CN7545022V, interconnect 6', 'portStatusReason': u'Active', 'operationalSpeed': u'Speed_10G'}, {'portStatus': u'Linked', 'lagId': 2, 'lagStates': [u'LacpActivity', u'Aggregation', u'Synchronization', u'Collecting', u'Distributing'], 'portName': u'Q1:2', 'interconnectName': u'CN75140CR3, interconnect 3', 'portStatusReason': u'Active', 'operationalSpeed': u'Speed_10G'}, {'portStatus': u'Linked', 'lagId': 2, 'lagStates': [u'LacpActivity', u'Aggregation', u'Synchronization', u'Collecting', u'Distributing'], 'portName': u'Q1:1', 'interconnectName': u'CN7545022V, interconnect 6', 'portStatusReason': u'Active', 'operationalSpeed': u'Speed_10G'}, {'portStatus': u'Linked', 'lagId': 2, 'lagStates': [u'LacpActivity', u'Aggregation', u'Synchronization', u'Collecting', u'Distributing'], 'portName': u'Q1:1', 'interconnectName': u'CN75140CR3, interconnect 3', 'portStatusReason': u'Active', 'operationalSpeed': u'Speed_10G'}]}
    [Arguments]   ${etherSummary}   ${uplinkSets}
    ${etherSummaryItems}=    Get Dictionary Items    ${etherSummary}
    :FOR   ${lagIdStr}   ${value}   IN   @{etherSummaryItems}
    # We need to bypass vplag ids... They use 1000 and up.
    \   Continue For Loop If   ${lagIdStr} >= 1000
    \   ${uplinkSetsAttrs} =   Get From Dictionary   ${uplinkSets}   ${lagIdStr}
    # no need to compare lagId because it is our primary key
    # not comparing port-channel
    \   Protocol Should Be In Lag States   ${value['protocol']}   ${uplinkSetsAttrs}
    \   Ports Should Match With Uplink Sets   ${value['ports']}   ${uplinkSetsAttrs}
    # verify that portStatus is linked and portStatusReason is Active
    \   ${result} =   Port Status Should Be Linked And Active   ${uplinkSetsAttrs} 
    \   Run Keyword If   '${result}' == '${False}'   Fail   msg=One or more ICM attribute is not in the expected value.

Check Ls Output For File Or Dir
    [Documentation]   Check for the occurence of a file or directory from the ls command output.
    [Arguments]   ${o}   ${file_dir_name}
    ${out} =   Split String   ${o}   ${\n}
    :FOR   ${cli_out}   IN   @{out}
    \   ${cli_out} =   Strip String   ${cli_out}   characters=\r
    \   Return From Keyword If   "${cli_out}" == "ls: ${file_dir_name}: No such file or directory"   ${False}
    [Return]   ${True}

Check Test Return Code For Shell Command
    [Documentation]   Check for return code of a specific shell command.
    [Arguments]   ${o}
    ${out} =   Split String   ${o}   ${\n}
    :FOR   ${cli_out}   IN   @{out}
    \   ${cli_out} =   Strip String   ${cli_out}   characters=\r
    \   Return From Keyword If   "${cli_out}" == "${1}"   ${False}
    [Return]   ${True}

Gdbstacktrace Should Not Exists In Hafnium
    [Documentation]   Fail if gdbstacktrace exists in any of the following locations: /tmp, /data/logs, or /data/nos.
    [Arguments]   ${icm_name}   ${ip}   ${iface}   ${hf_username}=root   ${hf_password}=UnoVista
    ${trace_dirs} =   Create List   /tmp/  /data/logs/   /data/nos/
    :FOR   ${trace_dir}   IN   @{trace_dirs}
    \   Log To Console   Logging to ${icm_name}/${ip} to check for ${trace_dir}gdbstack* ..   no_newline=${True}
    \   ${o} =   Execute Command To Remote Host   ${ip}   ${hf_username}   ${hf_password}   test -n "$(find ${trace_dir} -maxdepth 1 -name 'gdbstack*' -print)"; echo $?   iface=${iface}
    \   ${trace_found} =   Check Test Return Code For Shell Command   ${o}
    \   Run Keyword If   "${trace_found}" == "${True}"   Fail   msg=[Failed: ISS crash detected in ${icm_name}/${ip} through gdbstacktrace in ${trace_dir}]
    \   ...       ELSE   Log To Console   [OK]

Check For ISS Crash
    [Documentation]   This requires SSH access to Hafnium as it logs into it and check for /tmp/gdbstacktrace_btfull.txt.
    [Arguments]   ${hf_username}=root   ${hf_password}=UnoVista   ${iface}=eth0
    ${CHECK_ISS_CRASH} =   Get Variable Value   ${CHECK_ISS_CRASH}   ${True}
    Run Keyword If   ${CHECK_ISS_CRASH} is not ${True}   Log   CHECK_ISS_CRASH was explicitly disabled by setting to ${CHECK_ISS_CRASH}.   WARN   console=${True}
    Return From Keyword If   ${CHECK_ISS_CRASH} is not ${True}
    ${resp} =   Fusion Api Get Interconnect
    ${icm_names} =   Create Dictionary
    :FOR   ${icm}   IN   @{resp['members']}
    \   Continue For Loop If   '${icm['model']}' != '${HAFNIUM_MODEL}'
    \   ${USE_HAFNIUM_RESOURCE_IPV4} =   Get Variable Value   ${USE_HAFNIUM_RESOURCE_IPV4}
    \   ${ipv4Addr} =   Run Keyword If   ${USE_HAFNIUM_RESOURCE_IPV4} is ${True}   Get Interconnect IP Address From OneView   ${icm['ipAddressList']}   Ipv4Dhcp
    \   ${ipv6Addr} =   Run Keyword If   ${USE_HAFNIUM_RESOURCE_IPV4} is not ${True}   Get Interconnect IP Address From OneView   ${icm['ipAddressList']}   Ipv6Dhcp
    \   ${ipv6Addr} =   Run Keyword If   '${ipv6Addr}' == '${Null}'   Get Interconnect IP Address From OneView   ${icm['ipAddressList']}   Ipv6LinkLocal
    \   ...                       ELSE   Set Variable   ${ipv6Addr}
    \   Run Keyword If   ${USE_HAFNIUM_RESOURCE_IPV4} is ${True} and '${ipv4Addr}' == '${Null}'   Fail   msg=Unable to get IPv4 address from ipAddressList of ${icm['name']}.
    \   Run Keyword If   ${USE_HAFNIUM_RESOURCE_IPV4} is ${True}   Run Keywords   Set To Dictionary   ${icm_names}   ${icm['name']}=${ipv4Addr}   AND   Set Test Variable   ${iface}   ${Null}
    \   ...                    ELSE   Set To Dictionary   ${icm_names}   ${icm['name']}=${ipv6Addr}
    :FOR   ${icm_name}   IN   @{icm_names.keys()}
    \   Gdbstacktrace Should Not Exists In Hafnium   ${icm_name}   ${icm_names['${icm_name}']}   ${iface}   hf_username=${hf_username}   hf_password=${hf_password}

IPv4 Address Should Exist In Potash
    [Documentation]   Query OneView for Hafnium resource data and make sure IPv4 Address exists when interconnect is in Configured state.
    ...               We found defect where IPv4 address disappeared after completion of connection redeployment from ICM efuse (QXCR1001629414 <- OVD26967: [CI-FIT] Potash IPv4 disappears after ICM Efuse Reset)
    ${resp} =   Fusion Api Get Interconnect
    ${icm_names} =   Create Dictionary
    :FOR   ${icm}   IN   @{resp['members']}
    \   Continue For Loop If   '${icm['model']}' != '${HAFNIUM_MODEL}'
    \   Continue For Loop If   '${icm['state']}' != 'Configured'
    \   ${ipAddr} =   Get Interconnect IP Address From OneView   ${icm['ipAddressList']}   Ipv4Dhcp
    \   Run Keyword If   '${ipAddr}' is '${null}'   OperatingSystem.Create File   ${STOP_SCRIPT}
    \   Run Keyword If   '${ipAddr}' is '${null}'   Fail   msg=Unable to get IPv4 address from ipAddressList of ${icm['name']}.

################
# Interconnects Helper
################
Get All Interconnects Name By Model
    [Documentation]   Query OneView and return the list of interconnect names by model.
    [Arguments]   ${model}
    ${icms} =   Create List
    ${resp} =   Fusion Api Get Interconnect
    :FOR   ${icm}   IN   @{resp['members']}
    \   Continue For Loop If   '${icm['model']}' != '${model}'
    \   Append To List   ${icms}   ${icm['name']}
    [Return]   ${icms}

Get Interconnects Attribute By Name
    [Documentation]   Accepts interconnects name and returns value of the attribute specified.
    [Arguments]   ${icm_name}   ${attr}
    ${resp} =   Fusion Api Get Interconnect   param=?filter="name='${icm_name}'"
    Length Should Be   ${resp['members']}   1   msg=${icm_name} query in OneView returned unexpected members length.
    ${value} =  Get From Dictionary  ${resp['members'][0]}    ${attr}
    [Return]   ${value}

Get Interconnects Uri By Name
    [Documentation]   Accepts list of interconnects name and return list of interconnects uri.
    [Arguments]   ${icm_names}
    ${icm_uris} =   Create List
    :FOR   ${icm}   IN   @{icm_names}
    \   ${icm_uri} =   Get Interconnects Attribute By Name    ${icm}   uri
    \   Append To List   ${icm_uris}   ${icm_uri}
    [Return]   ${icm_uris}

Get Interconnect OneView Credential
    [Documentation]   Get interconnect OneView credential by running a shell script. Returns dictionary.
    [Arguments]   ${encSN}   ${icmBay}
    ${sanitizedIP} =   Get Variable Value   ${FUSION_IP}
    ${sanitizedIP} =   Remove String Using Regexp   ${sanitizedIP}   (\\[|\\])
    Put File To Remote Host   ${sanitizedIP}   ${FUSION_SSH_USERNAME}   ${FUSION_SSH_PASSWORD}   ${ICM_SCRIPTS_DIR}/${ICM_PASSWD_SCRIPT}   /root/${ICM_PASSWD_SCRIPT}   keepConnection=${True}
    ${output} =  Execute Command   /root/${ICM_PASSWD_SCRIPT} "${encSN}" "${icmBay}"
    ${encICMPasswd} =   Create Dictionary
    ${dict} =   robustness-helper.String To Dictionary   ${output}
    Set To Dictionary   ${encICMPasswd}   ${dict['EnclosureSN']}_${dict['Bay']}   ${dict}
    [Return]   ${encICMPasswd}

Get Interconnect Match With ICM Model
    [Documentation]   Get intercoonect that matched the ICM_MODEL we are testing and return in ordered list.
    ${resp} =   fusion api get interconnect
    ${ic_list} =    Create List
    ${ics} =     Get From Dictionary     ${resp}    members
    ${l} = 	Get Length	${ics}
    :FOR	${x}	IN RANGE	0	${l}
    \   ${ic} =     Get From List   ${ics}    ${x}
    \ 	Run Keyword If 	'${ic['model']}' != '${ICM_MODEL}'		Continue For Loop
    \   Append to list      ${ic_list}  ${ic}
    ${ordered_list} =   robustness-helper.order_icms    ${ic_list}     ${ICM_ORDER}
    [Return]    ${ordered_list}

Create Interconnect Bay To Uri Map
    [Documentation]   Mapping interconnect bay number to uri.
    [Arguments]   ${enc_data}
    ${icms_uri} =   Create Bay Number To Uri Map   ${enc_data}   interconnectBays   interconnectUri
    [Return]   ${icms_uri}

IC Reached MultiActive
    [Documentation]    This keyword will get the current enclosure IC's stacking domain role and fail if it is not MultiActive
    [Arguments]     ${uri}
    ${resp} =   Fusion Api Get Resource     ${uri}
    Log   \t ${uri}: ${resp['stackingDomainRole']}   console=${True}
    Should Match Regexp     ${resp['stackingDomainRole']}    MultiActive
    [Return]    ${resp}

IC Reached Master
    [Documentation]    This keyword will get the current enclosure IC's stacking domain role and fail if it is not Master
    [Arguments]     ${uri}
    ${resp} =   Fusion Api Get Resource     ${uri}
    Log   \t ${uri}: ${resp['stackingDomainRole']}   console=${True}
    Should Match Regexp     ${resp['stackingDomainRole']}    Master
    [Return]    ${resp}

Wait Until Interconnect Reached State
    [Documentation]   Based on a certain timeout and pooling interval times, keyword will wait for the named interconnect to be in a certain state.
    [Arguments]   ${icm_name}   ${state}   ${timeout}   ${interval}
    ${resp} =   Fusion Api Get Interconnect   param=?filter="name=='${icm_name}'"
    ${uri} =   Get From Dictionary   ${resp['members'][0]}   uri
    Wait Until Keyword Succeeds   ${timeout}   ${interval}   IC reached state   ${uri}    ${state}

Wait Until Interconnect Reached MultiActive
    [Documentation]   Based on a certain timeout and pooling interval times, keyword will wait for the named interconnect to be in MultiActive role.
    [Arguments]   ${icm_name}   ${wait_timeout}   ${wait_interval}
    ${resp} =   Fusion Api Get Interconnect   param=?filter="name=='${icm_name}'"
    ${uri} =   Get From Dictionary   ${resp['members'][0]}   uri
    Wait Until Keyword Succeeds   ${wait_timeout}   ${wait_interval}   IC Reached MultiActive    ${uri}

Wait Until Interconnect Reached Master
    [Documentation]   Based on a certain timeout and pooling interval times, keyword will wait for the named interconnect to be in Master role.
    [Arguments]   ${icm_name}   ${wait_timeout}   ${wait_interval}
    ${resp} =   Fusion Api Get Interconnect   param=?filter="name=='${icm_name}'"
    ${uri} =   Get From Dictionary   ${resp['members'][0]}   uri
    Wait Until Keyword Succeeds   ${wait_timeout}   ${wait_interval}   IC Reached Master    ${uri}

Wait Until List Of ICMs Reached Configuring
    [Documentation]   Wait until list of interconnects reached configuring state.
    [Arguments]   ${icmNames}   ${wait_timeout}=30m   ${wait_interval}=5s
    :FOR   ${icmName}   IN   @{icmNames}
    \   Wait Until Interconnect Reached State   ${icmName}   Configuring   ${wait_timeout}   ${wait_interval}

Wait Until List Of ICMs Reached Configured
    [Documentation]   Wait until list of interconnects reached configured state.
    [Arguments]   ${icmNames}   ${wait_timeout}=30m   ${wait_interval}=30s
    :FOR   ${icmName}   IN   @{icmNames}
    \   Wait Until Interconnect Reached State   ${icmName}   Configured   ${wait_timeout}   ${wait_interval}

Wait Until List Of ICMs Reached Maintenance
    [Documentation]   Wait until list of interconnects reached maintenance state.
    [Arguments]   ${icmNames}   ${wait_timeout}=30m   ${wait_interval}=5s
    :FOR   ${icmName}   IN   @{icmNames}
    \   Wait Until Interconnect Reached State   ${icmName}   Maintenance   ${wait_timeout}   ${wait_interval}

Wait Until List Of ICMs Reached Master
    [Documentation]   Wait until list of interconnects reached stacking domain role Master.
    [Arguments]   ${icmNames}   ${wait_timeout}=30m   ${wait_interval}=15s
    :FOR   ${icmName}   IN   @{icmNames}
    \   Wait Until Interconnect Reached Master   ${icmName}   ${wait_timeout}   ${wait_interval}

Wait Until List Of ICMs By Uri Reached state
    [Documentation]   Wait until list of interconnects reached state.
    [Arguments]   ${icmUris}   ${ICM_state}   ${wait_timeout}=30m   ${wait_interval}=30s
    :FOR   ${icmUri}   IN   @{icmUris}
    \    Wait Until Keyword Succeeds   ${wait_timeout}   ${wait_interval}   IC reached state   ${icmUri}    ${ICM_state}

Update IC Port
    [Documentation]   Update interconnect uplink port.
    ...               Example:
    ...               Update IC Port     ${ENC1ICBAY3}   ${UpLinkPort}   ${disable_uplink}
    ...               Data Required:
    ...               disable_uplink = {
    ...                   "associatedUplinkSetUri": "<uplink set name>",
    ...                   "interconnectName": "<interconnect name>",
    ...                   "portType": "Uplink",
    ...                   "portId": "<interconnect id>:<uplink port>",
    ...                   "portHealthStatus": "Normal",
    ...                   "capability": ["EnetFcoe","Ethernet","FibreChannel"],
    ...                   "configPortTypes": ["EnetFcoe","Ethernet"],
    ...                   "enabled": False,
    ...                   "portName": "<uplink set name>",
    ...                   "portStatus": "Linked",
    ...                   "type": "port"}

    [Arguments]   ${IC}   ${port}   ${body}   ${stacking}=${False}   ${wait_task_timeout}=10m   ${wait_task_interval}=30s
    ${icUri} = 	 Get IC URI   ${IC}
    ${icId} =   Fetch From Right   ${icUri}   /
    ${portId} =   Set Variable   ${icId}:${port}
    Log   \nUpdating port   console=${True}
    ${us} =   Run Keyword If   ${stacking} == ${False}   Get From Dictionary   ${body}   associatedUplinkSetUri
    ${resolvedUS} =   Run Keyword If   '${us}' != '${null}'   Get Lines Matching Regexp   ${us}   /rest/uplink-sets/   partial_match=true
    ${usUri} =   Run Keyword If   ${stacking} == ${False} and '${resolvedUS}' == ''   Get Uplinkset URI   ${us}
    ...                    ELSE   Set Variable   ${us}
    Run Keyword If   ${stacking} == ${False}   Set to dictionary   ${body}   associatedUplinkSetUri   ${usUri}
    Set To Dictionary   ${body}   portId   ${portId}
    ${req_body} =   Create List
    Append To List   ${req_body}   ${body}
    ${resp} =   Fusion Api Edit Interconnect Ports   body=${req_body}   uri=${icUri}
    [return]   ${resp}

Toggle Uplink Ports
    [Documentation]   Disable/enable uplink port.
    [Arguments]   ${icm_name}   ${uplink_port}   ${uplink_body}   ${stacking}=${False}   ${wait_task_timeout}=30m   ${wait_task_interval}=15s
    Log   \nToggling uplink port ${uplink_port} for "${icm_name}" {'enabled':${uplink_body['enabled']}}.   console=${True}
    ${resp} =   Update IC Port   ${icm_name}   ${uplink_port}   ${uplink_body}   stacking=${stacking}
    ${status}   ${task_uri} =   Run Keyword and Ignore Error   Get From Dictionary   ${resp['headers']}   location
    Return From Keyword If   '${status}' == 'FAIL'   ${resp}   ${null}
    Log   The task URI is ${task_uri}.   console=${True}
    ${task} =   Fusion Api Get Task   uri=${task_uri}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    [Return]   ${resp}   ${task}

Toggle Uplink Ports And Check For Error
    [Documentation]   Check response body for error code.
    [Arguments]   ${icm_name}   ${uplink_port}   ${uplink_body}   ${stacking}=${False}   ${wait_task_timeout}=30m   ${wait_task_interval}=15s
    ${resp}   ${task} =   Toggle Uplink Ports   ${icm_name}   ${uplink_port}   ${uplink_body}   stacking=${stacking}   wait_task_timeout=${wait_task_timeout}   wait_task_interval=${wait_task_interval}
    ${statusCode} =   Check Response For Error   ${resp}
    Run Keyword If   ${statusCode} != ${202}   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task}

Negative Test Toggle Uplink Ports
    [Documentation]   Attempt to toggle uplink ports and check response body for expected error code.
    [Arguments]   ${icm_name}   ${uplink_port}   ${uplink_body}   ${stacking}=${False}   ${wait_task_timeout}=30m   ${wait_task_interval}=15s
    ${resp}   ${task} =   Toggle Uplink Ports   ${icm_name}   ${uplink_port}   ${uplink_body}   stacking=${stacking}   wait_task_timeout=${wait_task_timeout}   wait_task_interval=${wait_task_interval}
    ${statusCode} =   Check Response For Error   ${resp}
    Run Keyword If   ${statusCode} != ${202}   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task}

Negative Test Disable Stacking Port
    [Documentation]   Attempt to disable stacking port. Expected result will be errorCode CRM_STACKING_PORT_CAN_NOT_BE_DISABLED.
    [Arguments]   ${icm_name}   ${uplink_port}   ${uplink_body}   ${stacking}=${True}   ${wait_task_timeout}=30m   ${wait_task_interval}=15s
    ${resp}   ${task} =   Toggle Uplink Ports   ${icm_name}   ${uplink_port}   ${uplink_body}   stacking=${stacking}   wait_task_timeout=${wait_task_timeout}   wait_task_interval=${wait_task_interval}
    ${status} =   Run Keyword If   ${stacking} == ${True}   Response Should Contain Error Code   ${resp}   CRM_STACKING_PORT_CAN_NOT_BE_DISABLED

Attempt Toggling Stacking Ports Using REST API
    [Documentation]   Negative test case to attempt toggling the stacking ports using REST API.
    Negative Test Disable Stacking Port   ${ICM_NAMES[0]}   ${STACKING_PORT_1}   ${DISABLE_STACKING_PORT_1}
    Negative Test Disable Stacking Port   ${ICM_NAMES[1]}   ${STACKING_PORT_2}   ${DISABLE_STACKING_PORT_2}

Break DUS And Establish Again
    [Documentation]   Disable stacking port and enable it back.
    ...              This requires root access enabled in Hafnium interconnect.
    #NOTE: 3.10 behaves differently as it triggers MAD, issues alert that
    #      the stacking health, port status, and uplink set status are not
    #      being actively maintained and may not contain current values.
    #      Also, it requires re-insert of interconnects after re-connecting
    #      stacking cables.
    [Arguments]   ${encSN}   ${icmName}   ${icm_names}   ${iface}=eth0   ${wait_configured_timeout}=60m   ${wait_configured_interval}=15s   ${hafnium_icm_model}=${HAFNIUM_MODEL}
    ${IpAddressList}    Get Interconnects Attribute By Name   ${icmName}    ipAddressList
	${USE_HAFNIUM_RESOURCE_IPV4} =   Get Variable Value   ${USE_HAFNIUM_RESOURCE_IPV4}
    ${ipAddr} =   Run Keyword If   ${USE_HAFNIUM_RESOURCE_IPV4} is ${True}   Get Interconnect IP Address From OneView   ${IpAddressList}   Ipv4Dhcp
    ...                     ELSE   Get Interconnect IP Address From OneView   ${IpAddressList}   Ipv6Dhcp
    ${ipAddr} =   Run Keyword If   '${ipAddr}' == '${Null}'   Get Interconnect IP Address From OneView   ${IpAddressList}   Ipv6LinkLocal
    ...                     ELSE   Set Variable   ${ipAddr}
    Run Keyword If   "${ipAddr}" == "${Null}"   Log   \n Not able to fetch ipaddress from oneview!   WARN   console=${True}
    ${ipAddress} =   Run Keyword If   '${ipAddr}' == '${Null}' and '${USE_HAFNIUM_RESOURCE_IPV4}' == '${True}'   Get Interconnect IP Address Directly From ICM   ${encSN}   ${icmName}   IPV4
    ...   ELSE IF   '${ipAddr}' == '${Null}' and '${USE_HAFNIUM_RESOURCE_IPV4}' != '${True}'   Get Interconnect IP Address Directly From ICM   ${encSN}   ${icmName}   IPV6
    ...   ELSE   Set Variable   ${ipAddr}
    Wait Until List Of ICMs Reached Configured   ${icm_names}   ${wait_configured_timeout}   ${wait_configured_interval}
    Toggle Uplink Ports And Check For Error   ${ICM_NAMES[0]}   ${FC_UPLINK_PORT_SIDEA}   ${DISABLE_FC_UPLINK_SIDEA}   wait_task_timeout=${TOGGLE_UPLINK_WAIT_TIMEOUT}   wait_task_interval=${TOGGLE_UPLINK_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${STACKING_SLEEP}   reason=Sleeping for ${STACKING_SLEEP} to let things settle after disabling uplink port.
    Wait Until List Of ICMs Reached Configured   ${icm_names}   ${wait_configured_timeout}   ${wait_configured_interval}
    Check For Multipath   ${CHECK_MULTIPATH_LESS1FC}   hafnium_icm_model=${hafnium_icm_model}   iface=${iface}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    common.Run Sequential Ping
    Fping Should Have No Loss
    Check For ISS Crash   iface=${iface}
    Toggle Uplink Ports And Check For Error   ${ICM_NAMES[0]}   ${FC_UPLINK_PORT_SIDEA}   ${ENABLE_FC_UPLINK_SIDEA}   wait_task_timeout=${TOGGLE_UPLINK_WAIT_TIMEOUT}   wait_task_interval=${TOGGLE_UPLINK_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${STACKING_SLEEP}   reason=Sleeping for ${STACKING_SLEEP} to let things settle after re-enabling uplink port.
    Wait Until List Of ICMs Reached Configured   ${icm_names}   ${wait_configured_timeout}   ${wait_configured_interval}
    Check For Multipath   ${CHECK_MULTIPATH}   hafnium_icm_model=${hafnium_icm_model}   iface=${iface}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    common.Run Sequential Ping
    Fping Should Have No Loss
    Check For ISS Crash   iface=${iface}
    #Accessing icm thru ssh
    Toggle Stacking Ports Using BCMSH   0   ${ipAddress}   iface=${iface}
    #With the above note, not sure how we verify states after disconnect. So,
    #instead of this:
    #Wait Until Keyword Succeeds   ${wait_configured_timeout}   ${wait_configured_interval}   Stacking Ports Should Be Unlinked   ${icmName}
    #LI Stacking Health Should Be Disconnected   ${TARGET_LI}
    #doing this:
    Wait Until List Of ICMs Reached Maintenance   ${icm_names}   ${wait_configured_timeout}
    Sleep And Log Reason To Console   ${STACKING_SLEEP}   reason=Sleeping for ${STACKING_SLEEP} to let things settle while in MAD condition after disabling stacking ports.
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    common.Run Sequential Ping
    Check For Multipath   ${CHECK_MULTIPATH_BREAKDUS}   hafnium_icm_model=${hafnium_icm_model}   iface=${iface}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${iface}
    # Try to toggle uplink port and make sure it does not trigger configuring ICMs
    # There was a change in MAD traffic flow where 1 downlink will be down. Sathish (Aricent) confirmed that the stackingDomainRole side will be the one with downlink down.
    Toggle Uplink Ports And Check For Error   ${ICM_NAMES[0]}   ${FC_UPLINK_PORT_SIDEA}   ${DISABLE_FC_UPLINK_SIDEA}   wait_task_timeout=${TOGGLE_UPLINK_WAIT_TIMEOUT}   wait_task_interval=${TOGGLE_UPLINK_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${STACKING_SLEEP}   reason=Sleeping for ${STACKING_SLEEP} to let things settle after disabling uplink port while in MAD condition.
    ${icm_uris} =   Get Interconnects Uri By Name   ${icm_names}
    # Verify that configuration cannot be changed while in MAD state
    Check Interconnects   ${icm_uris}   state=Maintenance   status=Critical
    #and this:
    # NOTE: There was a change late in 4.00 (and also in later releases) to transition lower bay to MultiActive instead of both Master.
    Wait Until Interconnect Reached MultiActive   ${ICM3}  ${wait_configured_timeout}   ${wait_configured_interval}
    Wait Until Interconnect Reached Master   ${ICM6}   ${wait_configured_timeout}   ${wait_configured_interval}
    # There was a change in MAD traffic flow where 1 downlink will be down. Sathish (Aricent) confirmed that the stackingDomainRole side will be the one with downlink down.
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    common.Run Sequential Ping
    Check For Multipath   ${CHECK_MULTIPATH_BREAKDUS}   hafnium_icm_model=${hafnium_icm_model}   iface=${iface}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${iface}
    # Check that the bonding interfaces are in the expected state/status
    ${resp} =   Fusion Api Get Interconnect   param=?filter="name=='${ICM3}'"
    ${uri} =   Get From Dictionary   ${resp['members'][0]}   uri
    Run Keyword If   '${resp['members'][0]['model']}' == '${HAFNIUM_MODEL}'   Run Keywords   Bonding Interfaces Should Be In Expected States   ${uri}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}   AND   Set Test Variable   ${offline_interconnect}   ${uri}
    ...       ELSE   Set Test Variable   ${offline_interconnect}   ${Null}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${offline_interconnect}   tags=${REMOTE_CHECKS_TAG}
    # Enable stacking ports
    Toggle Stacking Ports Using BCMSH   1   ${ipAddress}   iface=${iface}
    Wait Until List Of ICMs Reached Configuring   ${icm_names}   ${wait_configured_timeout}
    Wait Until List Of ICMs Reached Configured   ${icm_names}   ${wait_configured_timeout}   ${wait_configured_interval}
    Sleep And Log Reason To Console   ${STACKING_SLEEP}   reason=Sleeping for ${STACKING_SLEEP} after ICMs in Configured state after re-enabling stacking ports. Letting things settle before running checks on multipaths.
    Wait Until Keyword Succeeds   ${wait_configured_timeout}   ${wait_configured_interval}   Stacking Ports Should Be Linked
    Wait Until Keyword Succeeds   ${wait_configured_timeout}   ${wait_configured_interval}   LI Stacking Health Should Be BiConnected   ${TARGET_LI}   Unknown   Warning   BiConnected   NOT_CONSISTENT   ${1}
    # Enable FC Uplink Side A
    Toggle Uplink Ports And Check For Error   ${ICM_NAMES[0]}   ${FC_UPLINK_PORT_SIDEA}   ${ENABLE_FC_UPLINK_SIDEA}   wait_task_timeout=${TOGGLE_UPLINK_WAIT_TIMEOUT}   wait_task_interval=${TOGGLE_UPLINK_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${STACKING_SLEEP}   reason=Sleeping for ${STACKING_SLEEP} to let things settle after re-enabling uplink port after MAD recovery.
    Wait Until List Of ICMs Reached Configured   ${icm_names}   ${wait_configured_timeout}   ${wait_configured_interval}
    Wait Until Keyword Succeeds   ${wait_configured_timeout}   ${wait_configured_interval}   Stacking Ports Should Be Linked
    Wait Until Keyword Succeeds   ${wait_configured_timeout}   ${wait_configured_interval}   LI Stacking Health Should Be BiConnected   ${TARGET_LI}   Unknown   Warning   BiConnected   NOT_CONSISTENT   ${1}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    common.Run Sequential Ping
    Check For Multipath   ${CHECK_MULTIPATH}   hafnium_icm_model=${hafnium_icm_model}   iface=${iface}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${iface}

Toggle Stacking Ports Using BCMSH
    [Documentation]   Disable/enable stacking ports via bcmsh. This will require root access to the interconnects.
    [Arguments]   ${en}   ${ipAddr}   ${iface}=eth0   ${timeout}=15m   ${userName}=root   ${password}=UnoVista
    ${toggle} =   Convert To String   ${en}
    ${message} =   Create Dictionary   0=Disconnecting stacking links/ports.   1=Connecting stacking links/ports.
    ${llAddr} =   Get Lines Matching Regexp   ${ipAddr}   ^fe80:   partial_match=true
    Run Keyword If   '${llAddr}' == '${EMPTY}'   Open Connection   ${ipAddr}   timeout=${timeout}
    ...    ELSE   Open Connection   ${ipAddr}%${iface}   timeout=${timeout}
    Login   ${userName}   ${password}
    Write   bcmsh
    ${o} =   Read Until Regexp   OneView[\>|\#]
    Write   hw "ps hg"
    ${o} =   Read Until Regexp   OneView[\>|\#]
    Log   ${message['${toggle}']}   console=${True}
    Write   hw "port hg en=${en}"
    ${o} =   Read Until Regexp   OneView[\>|\#]
    Close All Connections

Stacking Ports Should Be Unlinked
    [Documentation]   Check that stacking ports are unlinked and other attributes are in the expected states.
    [Arguments]   ${icmName}
    :FOR     ${ic}     IN   @{ICM_NAMES}
    \   ${resp} =   Fusion Api Get Interconnect   param=?filter="name='${ic}'"
    \   ${ports} =  Get From Dictionary  ${resp['members'][0]}    ports
    \   Run Keyword If   '${ic}' == '${icmName}'   Stacking Ports Should Be In Expected State   ${ports}   portStatus=Unlinked   operationalSpeed=Speed_0M   portHealthStatus=Disabled   portSplitMode=Unknown   status=Disabled
    \   ...       ELSE   Stacking Ports Should Be In Expected State   ${ports}   portStatus=Unknown   operationalSpeed=Speed_0M   portHealthStatus=Disabled   portSplitMode=Unknown   status=Disabled

Stacking Ports Should Be Linked
    [Documentation]   Check that stacking ports are linked and other attributes are in the expected states.
    :FOR     ${ic}     IN   @{ICM_NAMES}
    \   ${resp} =   Fusion Api Get Interconnect   param=?filter="name='${ic}'"
    \   ${ports} =  Get From Dictionary  ${resp['members'][0]}    ports
    \   Stacking Ports Should Be In Expected State   ${ports}

Stacking Ports Should Be In Expected State
    [Documentation]   Check that stackings ports are at expected state.
    [Arguments]   ${ports}   ${enabled}=${true}   ${operationalSpeed}=${Null}   ${portHealthStatus}=Normal   ${portSplitMode}=Unsplit   ${portStatus}=Linked   ${portType}=Stacking   ${portTypeExtended}=External   ${status}=OK
    ${operationalSpeed}=   Run Keyword If   '${operationalSpeed}' == '${Null}' and '${HAFNIUM_MODEL}' == '${NITRO}'   Set Variable   Speed100G
    ...                           ELSE IF   '${operationalSpeed}' == '${Null}' and '${HAFNIUM_MODEL}' == '${POTASH}'   Set Variable   Speed40G
    ...                           ELSE IF   '${operationalSpeed}' != '${Null}'   Set Variable   ${operationalSpeed}
    ...                           ELSE   Fail   msg=Unable to set appropriate default operationalSpeed. Unable to recognize the Hafnium model.
    ${portNames}=   Create List   Q7   Q8
    ${l} =   Get Length   ${ports}
    :FOR   ${x}   IN RANGE   0   ${l}
    \   ${cportName} =   Get From Dictionary   ${ports[${x}]}   portName
    \   Continue For Loop If   '${cportName}' != 'Q7' and '${cportName}' != 'Q8'
    \   ${cenabled} =   Get From Dictionary   ${ports[${x}]}   enabled
    \   ${coperationalSpeed} =   Get From Dictionary   ${ports[${x}]}   operationalSpeed
    \   ${cportHealthStatus} =   Get From Dictionary   ${ports[${x}]}   portHealthStatus
    \   ${cportSplitMode} =   Get From Dictionary   ${ports[${x}]}   portSplitMode
    \   ${cportStatus} =   Get From Dictionary   ${ports[${x}]}   portStatus
    \   ${cportType} =   Get From Dictionary   ${ports[${x}]}   portType
    \   ${cportTypeExtended} =   Get From Dictionary   ${ports[${x}]}   portTypeExtended
    \   ${cstatus} =   Get From Dictionary   ${ports[${x}]}   status
    \   ${cinterconnectName} =   Get From Dictionary   ${ports[${x}]}   interconnectName
    \   ${portName}   ${portNames} =   List Should Contain Value To Remove   ${portNames}   ${cportName}
    \   Log   Current select key-value pair as queried from OneView's ${cinterconnectName}: \nportName: ${cportName}, \nenabled: ${cenabled}, \noperationalSpeed: ${coperationalSpeed}, \nportHealthStatus: ${cportHealthStatus}, \nportSplitMode: ${cportSplitMode}, \nportStatus: ${cportStatus}, \nportType: ${cportType}, \nportTypeExtended: ${cportTypeExtended}, \nstatus: ${cstatus}   console=${True}
    \   Should Be Equal   ${portName}   ${cportName}   msg=Port portName is not the expected value.
    \   Should Be Equal   ${enabled}   ${cenabled}   msg=Port enabled is not the expected value.
    \   Should Be Equal   ${operationalSpeed}   ${coperationalSpeed}   msg=Port operationalSpeed is not the expected value.
    \   Should Be Equal   ${portHealthStatus}   ${cportHealthStatus}   msg=Port portHealthStatus is not the expected value.
    \   Should Be Equal   ${portSplitMode}   ${cportSplitMode}   msg=Port portSplitMode is not the expected value.
    \   Should Be Equal   ${portStatus}   ${cportStatus}   msg=Port portStatus is not the expected value.
    \   Should Be Equal   ${portType}   ${cportType}   msg=Port portType is not the expected value.
    \   Should Be Equal   ${portTypeExtended}   ${cportTypeExtended}   msg=Port portTypeExtended is not the expected value.
    \   Should Be Equal   ${status}   ${cstatus}  msg=Port status is not the expected value.

Get Master Interconnect Module
    [Documentation]   Get master interconnect module from list of ICMs and return the entire response body in a list.
    [Arguments]   ${icm_names}
    ${masterList} =   Create List
    :FOR   ${icm}   IN   @{icm_names}
    \   ${resp} =   Fusion Api Get Interconnect   param=?filter="name='${icm}'"
    \   Length Should Be   ${resp['members']}   1   msg=${icm} query in OneView returned unexpected members.
    \   Run Keyword If   '${resp['members'][0]['stackingDomainRole']}' == 'Master'   Append To List   ${masterList}   ${resp}
    ${count} =   Get Length   ${icm_names}
    ${eval} =   Evaluate   ${count} % 2
    Should Be Equal   ${eval}   ${0}   msg=Not all Hafnium ICMs are in the expected stackingDomainRole.
    [Return]   ${masterList}

Get Interconnect IP Address From OneView
    [Documentation]   Parse the requested IP Address from OneView Interconnect ipAddressList.
    [Arguments]   ${ipAddressList}   ${ipAddressType}
    :FOR   ${i}   IN   @{ipAddressList}
    \   Return From Keyword If   '${i['ipAddressType']}' == '${ipAddressType}'   ${i['ipAddress']}
    [Return]   ${null}

Get Ethernet Summary
    [Documentation]   Login to Master Hafnium and parse the ethernet summary. Returns ether summary as list.
    [Arguments]   ${icm_names}   ${iface}=eth0   ${timeout}=15m   ${userName}=root   ${password}=UnoVista   ${useOneViewCredential}=${False}
    ${respList} =   Get Master Interconnect Module   ${icm_names}
    ${icmBay} =   Fetch From Right   ${respList[0]['members'][0]['name']}   ${SPACE}
    ${resp} =   Fusion Api Get Resource   ${respList[0]['members'][0]['enclosureUri']}
    ${encICMPasswd} =   Get Interconnect OneView Credential   ${resp['serialNumber']}   ${icmBay}
    ${USE_HAFNIUM_RESOURCE_IPV4} =   Get Variable Value   ${USE_HAFNIUM_RESOURCE_IPV4}
    ${ipv4Addr} =   Run Keyword If   ${USE_HAFNIUM_RESOURCE_IPV4} is ${True}   Get Interconnect IP Address From OneView   ${respList[0]['members'][0]['ipAddressList']}   Ipv4Dhcp
    ${ipv6Addr} =   Run Keyword If   ${USE_HAFNIUM_RESOURCE_IPV4} is not ${True}   Get Interconnect IP Address From OneView   ${respList[0]['members'][0]['ipAddressList']}    Ipv6Dhcp
    ${ipv6Addr} =   Run Keyword If   '${ipv6Addr}' == '${Null}'   Get Interconnect IP Address From OneView   ${respList[0]['members'][0]['ipAddressList']}   Ipv6LinkLocal
    ...                       ELSE   Set Variable   ${ipv6Addr}
    Run Keyword If   ${USE_HAFNIUM_RESOURCE_IPV4} is ${True} and '${ipv4Addr}' is '${null}'   Fail   msg=Unable to get Ipv4Dhcp address from the resource data for ${respList[0]['members'][0]['name']}.
    ${llAddr} =   Get Lines Matching Regexp   ${ipv6Addr}   ^fe80:   partial_match=true
    Run Keyword If   ${USE_HAFNIUM_RESOURCE_IPV4} is ${True}   Open Connection   ${ipv4Addr}   timeout=${timeout}
    ...    ELSE IF   '${ipv6Addr}' != '${Null}' and '${llAddr}' == '${EMPTY}'   Open Connection   ${ipv6Addr}   timeout=${timeout}
    ...    ELSE IF   '${llAddr}' != '${EMPTY}'   Open Connection   ${ipv6Addr}%${iface}   timeout=${timeout}
    ...       ELSE   Open Connection   ${encICMPasswd['${resp['serialNumber']}_${icmBay}']['ipv6LinkLocal']}%${iface}   timeout=${timeout}
    Run Keyword If   ${useOneViewCredential} is ${True}   Login   ${encICMPasswd['${resp['serialNumber']}_${icmBay}']['User']}   ${encICMPasswd['${resp['serialNumber']}_${icmBay}']['Password']}
    ...       ELSE   Login   ${userName}   ${password}
    Run Keyword If   ${useOneViewCredential} is ${False}   Write   bcmsh
    ${o} =   Run Keyword If   ${useOneViewCredential} is ${False}   Read Until Regexp   OneView[\>|\#]
    Write   set cli pagination off
    ${o} =   Read Until Regexp   OneView[\>|\#]
    Write   show ether summary
    ${o} =   Read Until Regexp   OneView[\>|\#]
    Close All Connections
    ${etherSummary} =   Split String   ${o}   ${\n}
    ${m} =   Set Variable   ${False}
    ${parsedEtherSummary} =   Create List
    :FOR   ${e}   IN   @{etherSummary}
    \   ${e} =   Strip String   ${e}   characters=\r
    \   Run Keyword If   ${m} is ${True}   Append To List   ${parsedEtherSummary}   ${e}
    \   Continue For Loop If   '${e}' != '-------------------------------------------------------------------------'
    \   ${m} =   Set Variable   ${True}
    [Return]   ${parsedEtherSummary}

Enter Into Hafnium Shell And Write Commands
    [Documentation]   Enter into Hafnium (OneView) Shell (/bin/hfsh) and write commands in hfsh_cmds list.
    [Arguments]   ${icm_names}   ${iface}=eth0   ${userName}=root   ${password}=UnoVista   ${open_connection_timeout}=15m   ${useOneViewCredential}=${False}   ${hfsh_cmds}=@{EMPTY}
    Run Keyword If   ${hfsh_cmds} == @{EMPTY}   Log    No Hafnium Shell Command specified!   WARN   console=${True}
    Return From Keyword If   ${hfsh_cmds} == @{EMPTY}   ${False}
    ${respList} =   Get Master Interconnect Module   ${icm_names}
    ${icmBay} =   Fetch From Right   ${respList[0]['members'][0]['name']}   ${SPACE}
    ${resp} =   Fusion Api Get Resource   ${respList[0]['members'][0]['enclosureUri']}
    ${encICMPasswd} =   Get Interconnect OneView Credential   ${resp['serialNumber']}   ${icmBay}
    ${USE_HAFNIUM_RESOURCE_IPV4} =   Get Variable Value   ${USE_HAFNIUM_RESOURCE_IPV4}
    ${ipv4Addr} =   Run Keyword If   ${USE_HAFNIUM_RESOURCE_IPV4} is ${True}   Get Interconnect IP Address From OneView   ${respList[0]['members'][0]['ipAddressList']}    Ipv4Dhcp
    ${ipv6Addr} =   Run Keyword If   ${USE_HAFNIUM_RESOURCE_IPV4} is not ${True}   Get Interconnect IP Address From OneView   ${respList[0]['members'][0]['ipAddressList']}    Ipv6Dhcp
    ${ipv6Addr} =   Run Keyword If   '${ipv6Addr}' == '${Null}'   Get Interconnect IP Address From OneView   ${respList[0]['members'][0]['ipAddressList']}   Ipv6LinkLocal
    ...                       ELSE   Set Variable   ${ipv6Addr}
    Run Keyword If   ${USE_HAFNIUM_RESOURCE_IPV4} is ${True} and '${ipv4Addr}' is '${null}'   Fail   msg=Unable to get Ipv4Dhcp address from the resource data for ${respList[0]['members'][
    ${llAddr} =   Get Lines Matching Regexp   ${ipv6Addr}   ^fe80:   partial_match=true
    Run Keyword If   ${USE_HAFNIUM_RESOURCE_IPV4} is ${True}   Open Connection   ${ipv4Addr}   timeout=${open_connection_timeout}
    ...    ELSE IF   '${ipv6Addr}' != '${Null}' and '${llAddr}' == '${EMPTY}'   Open Connection   ${ipv6Addr}   timeout=${open_connection_timeout}
    ...    ELSE IF   '${llAddr}' != '${EMPTY}'   Open Connection   ${ipv6Addr}%${iface}   timeout=${open_connection_timeout}
    ...       ELSE   Open Connection   ${encICMPasswd['${resp['serialNumber']}_${icmBay}']['ipv6LinkLocal']}%${iface}   timeout=${open_connection_timeout}
    Run Keyword If   ${useOneViewCredential} is ${True}   Login   ${encICMPasswd['${resp['serialNumber']}_${icmBay}']['User']}   ${encICMPasswd['${resp['serialNumber']}_${icmBay}']['Passwo
    ...       ELSE   Login   ${userName}   ${password}
    Run Keyword If   ${useOneViewCredential} is ${False}   Write   bcmsh
    ${o} =   Run Keyword If   ${useOneViewCredential} is ${False}   Read Until Regexp   OneView[\>|\#]
    Write   set cli pagination off
    ${o} =   Read Until Regexp   OneView[\>|\#]
    Run Hafnium OneView Shell Commands   ${hfsh_cmds}
    Close All Connections

Update Potash ICMs FW
    [Documentation]   Use the uploaded SPP FW Bundle to update Hafnium ICMs FW
    [Arguments]   ${bundleUri}   ${wait_task_timeout}=${FW_UPDATE_WAIT_TIMEOUT}   ${wait_task_interval}=${FW_UPDATE_WAIT_INTERVAL}   ${failOnMismatch}=${True}
    Log   \nValidating the interconnect firmware before LI update   console=${True}
    ${fwVersions} =   Create Dictionary
    :FOR     ${icmName}     IN   @{ICM_NAMES}
    \   ${resp} =   Fusion Api Get Interconnect   param=?filter="name='${icmName}'"
    \   ${preFWVersion} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion
    \   Log   \n Firmware version of Interconnect ${icmName} is :${preFWVersion}   console=${True}
    \   Set To Dictionary   ${fwVersions}   ${icmName}=${preFWVersion}
    Log   \nUpdating firmware through LI page   console=${True}
    ${liUri} = 	Get LI Uri   ${TARGET_LI}
    Set to dictionary     ${LI_UPDATE_BODY}     sppUri    ${bundleUri}
    ${resp} =    Fusion Api Li Upgrade Firmware    ${LI_UPDATE_BODY}    ${liUri}
    ${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   ${wait_task_timeout}   ${wait_task_interval}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task} 

    Log   \nValidating the interconnects firmware version after LI update   console=${True}
    :FOR   ${icmName}   IN   @{ICM_NAMES}
    \   ${resp} =   Fusion Api Get Interconnect   param=?filter="name='${icmName}'"
    \   ${postFWVersion} =  Get From Dictionary   ${resp['members'][0]}   firmwareVersion 
    \   Log   \n Firmware version of Interconnect ${icmName} is :${postFWVersion}   console=${True}
    #NOTE: We are intentionally failing here to make sure we are in a compatible FW version that will guarantee a warm reboot.
    #      In a case of Potash Warm Reboot test.
    \   Run Keyword If   '${postFWVersion}' == '${fwVersions['${icmName}']}'   Log   \nFirmware version is the same for ${icmName}   console=${True}
    \   ...    ELSE IF   ${failOnMismatch} is ${True}   Fail   msg=Firmware version mismatch after the update.
    \   ...    ELSE      Log   \nFirmware version is not the same for ${icmName}   console=${True}

Run Hafnium OneView Shell Commands
    [Documentation]   Run Hafnium OneView Shell (/bin/hfsh) commands from list provided.
    [Arguments]   ${hfsh_commands}
    :FOR   ${cmd}   IN   @{hfsh_commands}
    \   Log To Console   Executing ${cmd}
    \   Write   ${cmd}
    \   ${o} =   Read Until Regexp   OneView[\>|\#]

All Etherchannel Summary Ports Should Be Linked
    [Documentation]   Run bcmsh's show etherchannel summary command and fail on unlinked port.
    [Arguments]   ${iface}=eth0
    Return From Keyword If   "${CHECK_ETH_SUMMARY}" == '${null}'
    Log To Console   Checking Master Hafnium interconnect for port down...   no_newline=${True}
    ${resp} =   Fusion Api Get Interconnect
    ${icm_names} =   Create List
    :FOR   ${icm}   IN   @{resp['members']}
    \    Continue For Loop If   '${icm['model']}' != '${HAFNIUM_MODEL}'
    \    Append To List   ${icm_names}   ${icm['name']}
    ${parsedEtherSummary} =   Get Ethernet Summary   ${icm_names}   iface=${iface}
    ${unlinkedPorts} =   Create List
    :FOR   ${ports}   IN   @{parsedEtherSummary}
    \   ${port} =   Get Lines Matching Regexp   ${ports}   (D)   partial_match=true
    \   Run Keyword Unless   '${port}' == ''   Append To List   ${unlinkedPorts}   ${port}
    Run Keyword If   ${unlinkedPorts} != @{EMPTY}   Log To Console   [FAILED]
    ...       ELSE    Log To Console   [OK]
    Run Keyword If   ${unlinkedPorts} != @{EMPTY}   Run Keywords   Log Groups With Port Down To Console   ${unlinkedPorts}   AND   Fail

Create Interconnects To LI Mapping
    [Documentation]   Returns a dictionary of Interconnect to LI URI mapping.
    ${resp} =   Fusion Api Get Interconnect
    Run Keyword If   ${resp['count']} == 0   Fail    msg=\n GET /rest/interconnects returned count of zero(0)!
    ${icm_to_li} =   Create Dictionary
    :FOR   ${i}   IN   @{resp['members']}
    \   Set to Dictionary   ${icm_to_li}   ${i['uri']}   ${i['logicalInterconnectUri']}
    [Return]   ${icm_to_li}

Get Logical Interconnect Uri By ICM Uri
    [Documentation]   Get logical interconnect uri of an interconnect uri.
    [Arguments]   ${icm_uri}
    # Identying offline_interconnect LI
    ${resp} =   Run Keyword If   '${icm_uri}' != '${Null}'   Fusion Api Get Interconnect   uri=${icm_uri}
    ${logicalInterconnectUri} =   Run Keyword If   ${resp} != ${Null}   Get From Dictionary   ${resp}   logicalInterconnectUri
    [Return]   ${logicalInterconnectUri}

Get All Subordinate Interconnect Module
	[Documentation]   Get all subordinate interconnect module from OneView and return a list with added attributes for Enclosure name and ICM bay number.
	${Icm_list}    Create List
	${ic_dict} =    Create Dictionary    Enclosure=${None}
    ...                                  Bay_No=${None}
	...                                  FW_version=${None}
	${icms} =     Get IC
	:FOR   ${ic}   IN   @{icms}
	\    Run Keyword If   '${ic['stackingDomainRole']}' != 'Subordinate'		Continue For Loop
	\    ${icmName}   Get From Dictionary   ${ic}   name
	\    ${name}   Fetch From Left  ${icmName}   ,
	\    ${name_enc}   Fetch From Right  ${name}   _
	\    set to dictionary   ${ic_dict}   Enclosure   ${name_enc}
	\    ${No}   Fetch From Right  ${icmName}   ${SPACE}
	\    set to dictionary   ${ic_dict}   Bay_No   ${No}
	\    ${version}   Get From Dictionary   ${ic}   firmwareVersion
	\    set to dictionary   ${ic_dict}   FW_version   ${version}
	\    ${model}   Get From Dictionary   ${ic}   model
	\    set to dictionary   ${ic_dict}   icm_model   ${model}
	\    Append To List   ${Icm_list}   ${ic_dict}
    [Return]    ${Icm_list}

################
# Server Profiles Helper
################
Get Server Hardware Uris From Profiles
    [Documentation]   Get server profiles' serverHardwareUri and return them as list.
    [Arguments]     ${profiles}
    Set Log Level	TRACE
    ${blades} =         Create List
    ${l} = 	Get Length	${profiles}
    :FOR	${x}	IN RANGE	0	${l}
    \   ${profile} =        Get From List   ${profiles}    ${x}
    \
    \   append to list    ${blades}   ${profile['serverHardwareUri']}
    [Return]    ${blades}

Assign Server Profiles
        [Documentation]   Update server profiles in OneView by assigning the server hardware's valid uri. Argument requires list of dictionary of profiles that contains a valid server profile uri and serverHardwareUri (e.g: [{'uri': '/rest/server-profiles/8e2ec303-1274-4b9e-9871-b08f77bcc675', 'serverHardwareUri': '/rest/server-hardware/36343537-3338-4A48-3542-4E5030303533'}]).
        ...               NOTE: See robustness' LE-add-remove.txt script for example.
        [Arguments]     ${profiles}   ${timeout}=860m   ${interval}=15s  ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}   ${forceProfileApply}=false   ${throttle}=${Null}
        ${param} =   Run Keyword If   '${forceProfileApply}' != 'false'   Set Variable   ?force="${forceProfileApply}"
        ...                    ELSE   Set Variable   ${EMPTY}
	Set Log Level	TRACE
        ${valDict} =    Create Dictionary   status_code=${200}
        ...                                 taskState=Completed
        ${respList} =   Create List
        Set Suite Variable   ${forkedErrorFound}   ${False}
	:FOR	${p}	IN    @{profiles}
        \   ${profile} =    Fusion Api Get Resource    uri=${p['uri']}
        \   set to dictionary    ${profile}   serverHardwareUri=${p['serverHardwareUri']}
        \   remove from dictionary    ${profile}   status_code    headers
        \   fusion_api_appliance_setup.Log to console and logfile  	Assigning server hardware URI \"${p['uri']}\" to profile \"${p['name']}\"
        \   ${resp} =   fusion api edit server profile    uri=${p['uri']}   body=${profile}   param=${param}
        \   Continue For Loop If   ${waitForTask} != ${True}
        \   Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
        \   ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${timeout}   ${interval}   ${validate}
        \       Continue For Loop If   '${throttle}' == '${Null}'
        \       Continue For Loop If   ${parallel} != ${True}
        \       ${respLength} =   Get Length   ${respList}
        \       Continue For Loop If   ${respLength} != ${throttle}
        \       ${respList} =   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${timeout}   ${interval}   ${validate}   throttle=${throttle}
        Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${timeout}   ${interval}   ${validate}
        Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=Not all forked tasks state finished with Completed.

Check Server Bonding Interfaces
    [Documentation]   Connect to the server using pingable IP and check all bonding interfaces based on defined checks argument.
    [Arguments]   ${checks}   ${target_ha_file}
    Return From Keyword If   "${checks}" == '${null}'
    ${NO_CHECK_BONDS} =   Get Variable Value   ${NO_CHECK_BONDS}   @{EMPTY}
    ${reachable_ips} =   robustness-helper.get_server_reachable_ip   ${HA_FILE}
    ${reachable_ips_items} =   Get Dictionary Items   ${reachable_ips}
    ${failedServers} =   Create List
    ${passedServers} =   Create List
    ${incompleteServers} =   Create List
    ${unexpectedServers} =   Create List
    :FOR   ${profile}  ${ip}   IN   @{reachable_ips_items}
    \   Run Keyword If   '${profile}' in @{NO_CHECK_BONDS}   Log   Profile \"${profile}\" is listed in NO_CHECK_BONDS, skipping!   WARN   console=${True}
    \   Continue For Loop If   '${profile}' in @{NO_CHECK_BONDS}
    \   Log To Console   \n Checking ${ip} bonding interfaces...   no_newline=${True}
    \   ${Id} =   Open Connection   ${ip}
    \   ${Output} =   Login   ${SERVER_USERNAME}   ${SERVER_PASSWORD}
    \   ${stdout}   ${stderr}   ${rc} =   Execute Command   ${CHECK_BONDS_SCRIPT} ${checks} ${target_ha_file}   return_stderr=True   return_rc=True
    \   Run Keyword If   ${rc} == 0   Log To Console   [OK]
    \   ...    ELSE IF   ${rc} == 1   Log To Console   [FAILED]
    \   ...    ELSE IF   ${rc} == 2   Log To Console   [INCOMPLETE]
    \   ...       ELSE   Log To Console   [UNEXPECTED EXIT CODE: ${rc}]
    \   Run Keyword If   ${rc} == 0   Append To List   ${passedServers}   ${ip}
    \   ...    ELSE IF   ${rc} == 1   Append To List   ${failedServers}   ${ip}
    \   ...    ELSE IF   ${rc} == 2   Append To List   ${incompleteServers}   ${ip}
    \   ...    ELSE   Append To List   ${unexpectedServers}   ${ip}
    Log   Servers passed check: ${passedServers}
    Log   Servers failed check: ${failedServers}
    Log   Servers incomplete check: ${incompleteServers}
    Log   Servers unexpected check: ${unexpectedServers}
    ${e} =   Get Length   ${failedServers}
    Run Keyword If   ${e} != 0    Log To Console   msg=Servers failed in bonding interface check: ${failedServers}
    ${e} =   Get Length   ${incompleteServers}
    Run Keyword If   ${e} != 0    Log To Console   msg=Servers with incomplete bonding interface check: ${incompleteServers}
    ${e} =   Get Length   ${unexpectedServers}
    Run Keyword If   ${e} != 0    Log To Console   msg=Servers with unexpected bonding interface check: ${unexpectedServers}
    Close SSH Connection
    Run Keyword If   ${e} != 0   Fail   msg=Not all servers passed the check server test for the following: ${checks}

################
# Blades Helper
################
Create Blade Bay To Uri Map
    [Documentation]   Mapping blade bay number to uri.
    [Arguments]   ${enc_data}
    ${blades_uri} =   Create Bay Number To Uri Map   ${enc_data}   deviceBays   deviceUri
    [Return]   ${blades_uri}

################
# Logical Interconnect Helper
################
Logical Interconnect Should Be In Expected State
    [Documentation]   Check that logical interconnects are in expected states with retry. Fail on mismatch.
    [Arguments]   ${maxRetry}=${10}   ${retryInterval}=1m   ${filterByName}=${null}
    :FOR   ${retry}   IN RANGE   1   ${maxRetry}+1
    \   ${result} =   Compare Logical Interconnect Attributes To Expected Values   filterByName=${filterByName}
    \   Run Keyword If   '${result}' == '${True}'   Exit For Loop
    \   ...    ELSE IF   ${retry} != ${maxRetry}   Sleep And Log Reason To Console   ${retryInterval}   reason=One or more logical interconnect attribute is not in the expected value. Sleeping ${retryInterval} before a retry...
    \   ...       ELSE   Fail   msg=One or more logical interconnect attribute is not in the expected value and ${maxRetry} retries were exhausted.
    Run Keyword If   ${maxRetry} > ${1}   Log   \n Logical interconnect attributes compare completed in ${retry} attempt(s)   console=${True}

Compare Logical Interconnect Attributes To Expected Values
    [Documentation]   Check that logical interconnects attributes are in expected values. Returns boolean.
    [Arguments]   ${filterByName}=${null}
    Log   \n Checking OV Logical Interconnects State...   console=${True}
    ${resp}=   Fusion Api Get Resource   /rest/logical-interconnects
    ${lis}=   Get From Dictionary   ${resp}   members
    ${l}=   Get Length   ${lis}
    : FOR   ${x}   IN RANGE   0   ${l}
    \   ${liName}=   Get From Dictionary   ${lis[${x}]}    name
    \   ${li} =   Evaluate   $LOGICAL_INTERCONNECTS.get($liName, {})
    \   Run Keyword If   ${li} == &{EMPTY}   Log    Your data variable file LOGICAL_INTERCONNECTS does not contain '${liName}'.   WARN   console=${True}
    \   Continue For Loop If   '${filterByName}' != '${null}' and '${filterByName}' != '${liName}'
    \   Log   \n \#\#\# Checking some attributes of logical interconnect ${liName} \#\#\#   console=${True}
    \   ${liExpected} =   Run Keyword If   ${li} != &{EMPTY}   Check Data   ${li}   ${lis[${x}]}
    \   Return From Keyword If   '${liExpected}' == '${False}'  ${False}
    [Return]   ${True}

LI Stacking Health Should Be Disconnected
    [Documentation]   Check that logical interconnects stacking health is disconnected and other attributes are in the expected states.
    [Arguments]   ${liName}    ${expectedState}=Unknown   ${expectedStatus}=OK   ${expectedStackingHealth}=Disconnected   ${expectedConsistencyStatus}=CONSISTENT   ${maxRetry}=${5}   ${retryInterval}=1m
    #JMP: Known issue OVD2000 LI state is always Unknown 
    Logical Interconnect Should Be In Expected State   maxRetry=${maxRetry}   retryInterval=${retryInterval}   filterByName=${liName}

LI Stacking Health Should Be BiConnected
    [Documentation]   Check that logical interconnects stacking health is redundantly connected and other attributes are in the expected states.
    [Arguments]   ${liName}   ${expectedState}=Unknown   ${expectedStatus}=OK   ${expectedStackingHealth}=BiConnected   ${expectedConsistencyStatus}=CONSISTENT   ${maxRetry}=${5}   ${retryInterval}=1m
    Logical Interconnect Should Be In Expected State   ${maxRetry}   ${retryInterval}   ${liName}

LI Factory Reset
    [Documentation]   Performs Factory Reset in LI.
    [Arguments]    ${li_factory_reset_value}=ReapplyConfiguration    ${wait_task_timeout}=30m   ${wait_task_interval}=2s
    ${LI} =    Get LIs
    :FOR   ${li}   IN   @{LI}
    \   ${data} =   Create Dictionary   op=replace
    \   ...                             path=/factoryResetState
    \   ...                             value=${li_factory_reset_value}
    \   ${body} =   Create List     ${data}
    \   ${resp} =   Fusion Api Patch Interconnect   body=${body}    uri=${li['uri']}
    \   ${task} =   fusion_api_appliance_setup.Wait for Task   ${resp}  timeout=${wait_task_timeout}   interval=${wait_task_interval}
    \   ${valDict} =    Create Dictionary       status_code=${200}
    \   ...                                 taskState=Completed
    \   fusion_api_validation.Validate Response       ${task}   ${valDict}
    \   Check Asynchronous Task Response For Error   ${task}
    \   ${ICM_URIs} =    Get From Dictionary   ${li}   interconnects
    \   Wait Until List Of ICMs By Uri Reached state   ${ICM_URIs}    Configured    ${ICM_STATE_WAIT_TIMEOUT}     ${ICM_STATE_WAIT_INTERVAL}

################
# Appliance Backup-Restore: specific to backup and restore keywords
################
Run Robustness Backup And Restore
    [Documentation]   Perform robustness backup and restore.
    [Arguments]     ${cycles}    ${factoryResetValue}=ReapplyConfiguration    ${factoryReset_timeout}=30m    ${factoryReset_interval}=2s
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    ${REMOTE_RUN_CHECKS} =   Get Variable Value   ${REMOTE_RUN_CHECKS}   @{EMPTY}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    :FOR   ${x}   IN RANGE   1   ${cycles}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n Cycle: ${x} of ${cycles}   console=${True}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   Create Appliance Backup Download And Data Compare   wait_task_timeout=${CREATE_BACKUP_WAIT_TIMEOUT}   wait_task_interval=${CREATE_BACKUP_WAIT_INTERVAL}
    \   Edit OneView Configuration And Perform Data Compare
	\   LI Factory Reset    li_factory_reset_value=${factoryResetValue}    wait_task_timeout=${factoryReset_timeout}    wait_task_interval=${factoryReset_interval}
    \   Upload Restore Backup And Perform Data Compare   upload_task_timeout=${UPLOAD_BACKUP_WAIT_TIMEOUT}   upload_task_interval=${UPLOAD_BACKUP_WAIT_INTERVAL}   restore_task_timeout=${RESTORE_BACKUP_WAIT_TIMEOUT}   restore_task_interval=${RESTORE_BACKUP_WAIT_INTERVAL}

Create Appliance Backup Download And Data Compare
    [Documentation]   Create OneView appliance backup and download it to your local disk. This involved asynchronous operation for create backup.
    [Arguments]   ${wait_task_timeout}=15m   ${wait_task_interval}=2s
    ${retStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.Directory Should Exist   ${dataFilesDir}
    Run Keyword If   "${retStatus}" == "FAIL"   OperatingSystem.Create Directory   ${dataFilesDir}
    ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${backupFile}
    Run Keyword If   "${returnStatus}" == "PASS"   OperatingSystem.Remove File   ${backupFile}
    ${resp} =   Fusion Api Create Backup
    ${taskResp} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    ${resp} =   Fusion Api Download Backup  /rest/backups/archive/${taskResp['associatedResource']['resourceName']}  ${backupFile}
    Run Keyword If   ${resp['status_code']} != ${200}   Fail   msg=Download failed for backup: ${backupFile}

Pick One EG And Use It
    [Documentation]   Issue a query to OneView and set EG suite variable to the first in the list.
    ${resp} =   Fusion Api Get Resource   /rest/enclosure-groups?sort=name:ascending
    Set Suite Variable   ${EG}   ${resp['members'][0]['name']}

Edit OneView Configuration And Perform Data Compare
    [Documentation]   Edit OneView config by renaming EG to EG_renamed then verify that it was successfully renamed with state being Normal and status OK.
    Set EG   ${EG}   name=${EG}_renamed
    #Verify that EG renamed, EG state is Normal, and EG status is OK
    ${resp}  ${uri}=    Get Enclosure Group    ${EG}_renamed
    Run Keyword If   "${resp['name']}" != "${EG}_renamed"   or   "${resp['state']}" != "Normal"   or   "${resp['status']}" != "OK"   Fail   msg=One or more EG attribute is not in the expected value after edit EG: name=${resp['name']}, state=${resp['state']}, status=${resp['status']}.

Upload Restore Backup And Perform Data Compare
    [Documentation]   Upload backup, restore backup, and perform some checks.
    [Arguments]   ${expectedState}=Normal   ${expectedStatus}=OK   ${upload_task_timeout}=1m   ${upload_task_interval}=2s   ${restore_task_timeout}=60m   ${restore_task_interval}=2s   ${unassign_reassign_profiles}=${null}   ${hafnium_icm_model}=${HAFNIUM_MODEL}   ${iface}=eth0
    ${resp} =   Fusion Api Upload Backup   ${backupFile}
    #JMP: There is a defect being clarified with Atlas on the status_code. It is async and should be getting 202 instead of 200.
    Run Keyword If   ${resp['status_code']} != ${200}   Fail   msg=Upload backup failed: ${backupFile}
    #JMP: Instead of parsing this in fusion_api_appliance_setup.txt, I am doing it here because copy.Deep Copy will crash in Validate Response
    #JMP: 05/03/2017: Seems like OneView changed their response data and we no longer need this block of code. At least for now...
    #${content} =   Get From Dictionary   ${resp}   _content
    #${content} =   Evaluate   json.loads('''${content}''')   json
    #${task_uri} =   Get From Dictionary   ${content}   taskUri
    #JMP: 05/31/2017: After updating my working copy, I found that Yulong Gu made change to FusionLibrary request.py to print nice response body that make this useless.
    #${task_uri} =   Run Keyword If   ${tbirdEnv} == ${True}   Parse Task Uri From Content   ${resp}
    #...                       ELSE   Get From Dictionary   ${resp}   taskUri
    ${task_uri} =   Get From Dictionary   ${resp}   taskUri
    Should Not Be Empty    ${task_uri}    msg=Unable to retrive task uri from the response body: ${resp}
    ${resp} =   Fusion Api Get Task    uri=${task_uri}
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${upload_task_timeout}   interval=${upload_task_interval}   status_code=${200}
    ${requestBody} =   Create Dictionary   type=RESTORE
    ...                                    uriOfBackupToRestore=${task['associatedResource']['resourceUri']}
    ${resp} =   Fusion Api Restore Backup   ${requestBody}
    fusion_api_appliance_setup.Wait For Task   ${resp}  taskType=Restore  timeout=${restore_task_timeout}   interval=${restore_task_interval}
    #Let things settle down
    Sleep And Log Reason To Console   ${POST_RESTORE_SLEEP}   reason=Sleeping ${POST_RESTORE_SLEEP} to let things settle after a backup restore.
    #Re-authenticate
    Authenticate And Set Login
    #Verify that EG name restored, EG state is Normal, and EG status is OK
    ${resp}  ${uri}=    Get Enclosure Group    ${EG}
    Run Keyword If   "${resp['name']}"!="${EG}" or "${resp['state']}"!='${expectedState}' or "${resp['status']}"!='${expectedStatus}'  Fail   msg=One or more EG attribute is not in the expected value after edit EG: name=${resp['name']}, state=${resp['state']}, status=${resp['status']}.
    Run Keyword If   "${unassign_reassign_profiles}"!="${null}"   Check server status after appliance restoration   ${unassign_reassign_profiles}
    Check Common Resource Attributes
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    ${REMOTE_RUN_CHECKS} =   Get Variable Value   ${REMOTE_RUN_CHECKS}   @{EMPTY}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    Check For MeatGrinder Error
    Check For Multipath   hafnium_icm_model=${hafnium_icm_model}   iface=${iface}
    Check For Server In Read Only Filesystem
    common.Run Sequential Ping
    Fping Should Have No Loss
    Check For ISS Crash   iface=${iface}
    All Etherchannel Summary Ports Should Be Linked   iface=${iface}
    Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}

################
# Blade Hot Plug: specific to blade hot plug keywords
################
Process Blades For Synergy Blade Hot Plug
    [Documentation]   Process server blades for Synergy blade hot plug test.
    [Arguments]     ${blades}   ${state_timeout}=30m   ${state_interval}=2s   ${remove_timeout}=30m   ${remove_interval}=2s   ${insert_timeout}=30m   ${insert_interval}=2s   ${sleep}=1m   ${onlyProfileApplied}=${False}   ${poweroff_mode}=api   ${iface}=eth0
    Set Log Level	TRACE
    ${poweroff_mode} =    Evaluate    '${poweroff_mode}'.lower()
    ${em_sessions} =   Create Dictionary
    :FOR	${bl}	IN    @{blades}
    \   Continue For Loop If   ${onlyProfileApplied} is ${True} and '${bl['state']}' != 'ProfileApplied'
    \   Run Keyword If   '${poweroff_mode}' == 'api' and ${FORCE} == False   common.Power Off Server Uri   ${bl['uri']}   proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}
    \   ...    ELSE IF   '${poweroff_mode}' == 'ssh' and ${FORCE} == False   Get IP And Power Off Server Via Ssh As Possible   ${bl}
    \   ${resp} =   Fusion Api Get Resource   ${bl['locationUri']}
    \   ${enc} =    Fetch from left     ${bl['name']}    ,
    \   ${bay} =    Fetch from right    ${bl['name']}    ${SPACE}
    \   ${pass} =   Check For One Time Pass   ${enc}:${bay}
    \   Run Keyword If   ${pass}   Continue For Loop
    \   ${skip} =   Run Keyword If   "${DO_ONLY}" != "${null}"   Run Keyword And Return Status   List Should Not Contain Value   ${DO_ONLY}   ${bay}
    \   Run Keyword If   ${skip}   Continue For Loop
    \   ${EM_IP} =   Get Variable Value   ${em_sessions['${resp['serialNumber']}']['ip']}
    \   Run Keyword If   '${EM_IP}' == '${Null}'   Run Keywords   Set To Dictionary    ${em_sessions}   ${resp['serialNumber']}=&{EMPTY}   AND   Get EM IP   ${resp['serialNumber']}   iface=${iface}   AND   Set To Dictionary   ${em_sessions['${resp['serialNumber']}']}   ip=${EM_IP}
    \   ${EM_TOKEN} =   Get Variable Value   ${em_sessions['${resp['serialNumber']}']['token']}
    \   Run Keyword If   '${EM_TOKEN}' == '${Null}'   Run Keywords   Get EM Token   ${resp['serialNumber']}   AND   Set To Dictionary   ${em_sessions['${resp['serialNumber']}']}   token=${EM_TOKEN}
    \   Log   \t Waiting for Enclosure: ${enc}, Blade in Bay:${bay} to reach original state: ${bl['state']}   console=${True}
    \   Wait Until Keyword Succeeds     ${state_timeout}   ${state_interval}      Attribute Should Reach Expected Value    ${bl['uri']}    state   ${bl['state']}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    [EFUSE ON via RIS (REMOVE BLADE)]
    \   EFuse Blade   EFuseOn     ${bay}
    \   Log   \t Waiting for Enclosure: ${enc}, Blade in Bay:${bay} to be removed   console=${True}
    \   Wait Until Keyword Succeeds     ${remove_timeout}   ${remove_interval}      Blade is removed    ${bl['uri']}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    [EFUSE OFF via RIS (INSERT BLADE)]
    \   Efuse Blade   EFuseOff    ${bay}
    \   Log   \t Waiting for Enclosure: ${enc}, Blade in Bay:${bay} to be inserted   console=${True}
    \   ${expected} =    Get Length   ${blades}
    \   ${resp} =    Wait Until Keyword Succeeds     ${insert_timeout}   ${insert_interval}      Blade exists      ${expected}
    \   Log   \t Waiting for Enclosure: ${enc}, Blade in Bay:${bay} to reach original state: ${bl['state']}   console=${True}
    \   Wait Until Keyword Succeeds     ${state_timeout}   ${state_interval}      Attribute Should Reach Expected Value    ${bl['uri']}    state   ${bl['state']}
    \   Sleep And Log Reason To Console   ${sleep}   reason=Sleeping ${sleep} to let things settle (DTO may update a little late) after a blade hot plug.
    \   common.Power On Server Uri   ${bl['uri']}
    \   Reset Server Link Failure Count Cache By Profile   ${bl['serverProfileUri']}

Process Blades For C7000 Blade Hot Plug
    [Documentation]   Process server blades for C-Series blade hot plug test.
    [Arguments]    ${blades_uri}   ${blade_parsed}   ${remove_timeout}=30m   ${remove_interval}=2s   ${remove_sleep}=2m   ${cycle_sleep}=5m   ${state_timeout}=35m   ${state_interval}=15s   ${onlyProfileApplied}=${False}   ${poweroff_mode}=api
    Set Log Level	TRACE
    ${blades_uriItems}=    Get Dictionary Items    ${blades_uri}
    ${poweroff_mode} =    Evaluate    '${poweroff_mode}'.lower()
    :FOR  ${bay}  ${uri}    IN  @{blades_uriItems}
    \   Continue For Loop If   ${onlyProfileApplied} is ${True} and '${blade_parsed['${bay}']['state']}' != 'ProfileApplied'
    \   Run Keyword If   '${poweroff_mode}' == 'api' and ${FORCE} == False   common.Power Off Server Uri   ${uri}   proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}
    \   ...    ELSE IF   '${poweroff_mode}' == 'ssh' and ${FORCE} == False   Get IP And Power Off Server Via Ssh As Possible   ${bay}
    \   ${enc} =    Fetch from left     ${blade_parsed['${bay}']['name']}    ,
    \   ${pass} =   Check For One Time Pass   ${enc}:${bay}
    \   Run Keyword If   ${pass}   Continue For Loop
    \   Check Common Blade Attributes   ${blade_parsed}   ${bay}   ${uri}   state_timeout=${state_timeout}   state_interval=${state_interval}
    \   Execute OA Diag Command   efuse blade ${bay} off
    \   Log   \t Waiting for blade in Bay:${bay} to reach errorCode RESOURCE_NOT_FOUND   console=${True}
    \   Wait Until Keyword Succeeds     ${remove_timeout}  ${remove_interval}      Attribute Should Reach Expected Value    ${uri}    errorCode   RESOURCE_NOT_FOUND
    \   Sleep And Log Reason To Console   ${remove_sleep}   reason=Sleeping ${remove_sleep} after blade removed.
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    [EFUSE ON via OA (INSERT BLADE)]
    \   Execute OA Diag Command   efuse blade ${bay} on
    \   Log   \t Waiting for blade in Bay:${bay} to reach state ProfileApplied   console=${True}
    \   Wait Until Keyword Succeeds     ${state_timeout}  ${state_interval}      Attribute Should Reach Expected Value    ${uri}    state   ProfileApplied
    \   Sleep And Log Reason To Console   ${cycle_sleep}   reason=Sleeping ${cycle_sleep} after blade hot plug cycle to let things settle (DTO may update a little late).
    \   common.Power On Server Uri   ${uri}
    \   Check Common Blade Attributes   ${blade_parsed}   ${bay}   ${uri}   state_timeout=${state_timeout}   state_interval=${state_interval}
    \   Reset Server Link Failure Count Cache By Profile   ${blade_parsed['${bay}']['serverProfileUri']}

Check Common Blade Attributes
    [Documentation]   Check common blade attributes like state, status, and powerState.
    [Arguments]   ${blade_parsed}   ${bay}   ${uri}   ${state_timeout}=35m   ${state_interval}=15s
    Log   \t Waiting for blade in Bay:${bay} to reach state original state: ${blade_parsed['${bay}']['state']}   console=${True}
    Wait Until Keyword Succeeds     ${state_timeout}   ${state_interval}      Attribute Should Reach Expected Value    ${uri}    state   ${blade_parsed['${bay}']['state']}
    Log   \t Waiting for blade in Bay:${bay} to reach state original status: ${blade_parsed['${bay}']['status']}   console=${True}
    Wait Until Keyword Succeeds     ${state_timeout}   ${state_interval}      Attribute Should Reach Expected Value    ${uri}    status   ${blade_parsed['${bay}']['status']}
    Log   \t Waiting for blade in Bay:${bay} to reach state original state: ${blade_parsed['${bay}']['powerState']}   console=${True}
    Wait Until Keyword Succeeds     ${state_timeout}   ${state_interval}      Attribute Should Reach Expected Value    ${uri}    powerState   ${blade_parsed['${bay}']['powerState']}

Attribute Should Reach Expected Value
    [Documentation]   Check that a certain resource attribute reached the expected value.
    ...               Returns response of OneView Resource Query.
    [Arguments]	    ${uri}   ${attr}   ${value}
    Set Log Level	TRACE
    ${resp} =   fusion api get resource     ${uri}
    Log   \t ${uri}: ${resp['${attr}']}   console=${True}
    Should Match Regexp 	${resp['${attr}']}    ${value}
    [Return]	${resp}

Blade Exists
    [Documentation]   Test that server hardware is at the expected number.
    [Arguments]	    ${expected}
    Set Log Level	TRACE
    ${resp} =   Fusion api get server hardware
    ${l} =  get length    ${resp['members']}
    should be equal as integers  ${l}   ${expected}
    [Return]	${resp}

Blade Is Removed
    [Documentation]   Test that blade was removed based on the given server hardware URI.
    [Arguments]	    ${uri}  ${status_code}=404
    ${resp} =   Resource Uri Should Have Expected Status Code   ${uri}  ${status_code}
    [Return]	${resp}

Get Blades
    [Documentation]   Get server hardware and parse the name, uri, state, status and return it as list of dictionary.
    ${resp} =   fusion api get server hardware
    ${blades} =    Create List
    ${blades_list} =     Get From Dictionary     ${resp}    members
    ${l} = 	Get Length	${blades_list}
    :FOR	${x}	IN RANGE	0	${l}
    \   ${bl} =     Get From List   ${blades_list}    ${x}
    \   ${blade_details} =    Create Dictionary     name=${bl['name']}
    \   ...                                         uri=${bl['uri']}
    \   ...                                         state=${bl['state']}
    \   ...                                         status=${bl['status']}
    \   ...                                         locationUri=${bl['locationUri']}
    \   ...                                         serverProfileUri=${bl['serverProfileUri']}
    \   append to list    ${blades}   ${blade_details}
    [Return]    ${blades}

Get From Blade
    [Documentation]   Get an attribute from blade json data.
    [Arguments]     ${dict}   ${element}
    ${resp} =   Get An Element From Dictionary   ${dict}   ${element}
    [Return]    ${resp}

Process Blades For Synergy Blade Hot Plug Parallel
    [Documentation]   Process server blades in parallel for Synergy blade hot plug test.
    [Arguments]     ${blades}   ${state_timeout}=30m   ${state_interval}=2s   ${remove_timeout}=30m   ${remove_interval}=2s   ${insert_timeout}=30m   ${insert_interval}=2s   ${sleep}=1m   ${onlyProfileApplied}=${False}   ${poweroff_mode}=api   ${connectionSettingsApi}=${600}   ${iface}=eth0   ${proceedPressAndHold}=${Null}
    Set Log Level	TRACE
    ${blade_list}    Create List
    ${l} = 	Get Length	${blades}
    Run Keyword If   '${poweroff_mode}' == 'api'   Power Off All Servers In Parallel   onlyProfileApplied=${onlyProfileApplied}   proceedPressAndHold=${proceedPressAndHold}
    ...    ELSE IF   '${poweroff_mode}' == 'ssh'   Power Off All Servers Via Ssh In Parallel   onlyProfileApplied=${onlyProfileApplied}
    ...    ELSE   Fail   msg=Unsupported power off mode provided: ${poweroff_mode}
    ${em_sessions} =   Create Dictionary
    :FOR	${x}	IN RANGE	0	${l}
    \   ${bl} =     Get From List   ${blades}    ${x}
    \   Continue For Loop If   ${onlyProfileApplied} is ${True} and '${bl['state']}' != 'ProfileApplied'
    \   ${resp} =   Fusion Api Get Resource   ${bl['locationUri']}
    \   ${enc} =    Fetch from left     ${bl['name']}    ,
    \   ${bay} =    Fetch from right    ${bl['name']}    ${SPACE}
    \   ${pass} =   Check For One Time Pass   ${enc}:${bay}
    \   Run Keyword If   ${pass}   Continue For Loop
    \   ${skip} =   Run Keyword If   "${DO_ONLY}" != "${null}"   Run Keyword And Return Status   List Should Not Contain Value   ${DO_ONLY}   ${bay}
    \   Run Keyword If   ${skip}   Continue For Loop
    \   ${EM_IP} =   Get Variable Value   ${em_sessions['${resp['serialNumber']}']['ip']}
    \   Run Keyword If   '${EM_IP}' == '${Null}'   Run Keywords   Set To Dictionary    ${em_sessions}   ${resp['serialNumber']}=&{EMPTY}   AND   Get EM IP   ${resp['serialNumber']}   iface=${iface}   AND   Set To Dictionary   ${em_sessions['${resp['serialNumber']}']}   ip=${EM_IP}
    \   ${EM_TOKEN} =   Get Variable Value   ${em_sessions['${resp['serialNumber']}']['token']}
    \   Run Keyword If   '${EM_TOKEN}' == '${Null}'   Run Keywords   Get EM Token   ${resp['serialNumber']}   AND   Set To Dictionary   ${em_sessions['${resp['serialNumber']}']}   token=${EM_TOKEN}
    \   set to dictionary   ${bl}   bay_num   ${bay}
    \   set to dictionary   ${bl}    enc_name  ${enc}
    \   set to dictionary   ${bl}   em_ip   ${em_ip}
    \   set to dictionary   ${bl}    em_token  ${em_token}
    \   append to list    ${blade_list}   ${bl}
    Wait Until Keyword Succeeds     ${state_timeout}   ${state_interval}      Attribute Should Reach Expected Value For Parallel Efuse    ${blade_list}    state
    Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    [EFUSE ON In Parallel via RIS (REMOVE BLADE)]
    Efuse Blades In Parallel    EFuseOn     ${blade_list}
    Wait Until Keyword Succeeds     ${remove_timeout}   ${remove_interval}      Blades Should Have Been Removed    ${blade_list}
    Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    [EFUSE OFF In Parallel via RIS (INSERT BLADE)]
    Efuse Blades In Parallel   EFuseOff    ${blade_list}
    ${expected} =    Get Length   ${blades}
    ${resp} =    Wait Until Keyword Succeeds     ${insert_timeout}   ${insert_interval}      Blade exists      ${expected}
    Wait Until Keyword Succeeds     ${state_timeout}   ${state_interval}      Attribute Should Reach Expected Value For Parallel Efuse    ${blade_list}    state
    Sleep And Log Reason To Console   ${sleep}   reason=Sleeping ${sleep} to let things settle (DTO may update a little late) after a blade hot plug.
    Power On All Servers In Parallel   onlyProfileApplied=${onlyProfileApplied}
    :FOR   ${bl}   IN   @{blade_list}
    \   Reset Server Link Failure Count Cache By Profile   ${bl['serverProfileUri']}

Attribute Should Reach Expected Value For Parallel Efuse
    [Documentation]   Check that a certain resource attribute reached the expected value for a given servers.
    [Arguments]    ${blade_list}    ${attribute}
    :FOR	${blade}	IN    @{blade_list}
    \    Attribute Should Reach Expected Value    ${blade['uri']}    ${attribute}    ${blade['state']}

Efuse Blades In Parallel
    [Documentation]    Perform an efuse action on a Blades. Action = EFuseOff | EFuseOn
    [Arguments]    ${Action}    ${blade_list}
    :FOR    ${bay}    IN    @{blade_list}
    \    ${Header}    Set Variable    "X-Auth-Token":"${bay['em_token']}"
    \    ${Data}      Set Variable    {"Action":"${Action}"}
    \    Log   \t Issuing ${Action} for Server:${bay['bay_num']}    console=${True}
    \    ${Output}    Execute SSH Command
    \    ...    curl -ikX POST --tlsv1 -H ${Header} --data-ascii '${data}' https://${bay['em_ip']}/rest/v1/BladeBays/${bay['bay_num']}
    \    Should Contain    ${Output}    { "Action": "${Action}" }
    \    ...    msg=EFuse action failed \n${Output}

Blades Should Have Been Removed
   [Documentation]    Removing all blades from the OV.Fails if one or more blade was not removed.
   [Arguments]    ${blade_list}
   :FOR	   ${blade}	IN    @{blade_list}
   \    Blade is removed    ${blade['uri']}

################
# CIM Hot Plug: specific to CIM hot plug keywords
################
Perform CIMs Efuse
    [Documentation]   Perform CIM efuse reset via EM ssh session.
    [Arguments]   ${bayList}   ${sleep}=40m
    Collections.Sort List   ${bayList}
    ${l} =   Get Length   ${bayList}
    :FOR    ${x}    IN RANGE    0       ${l}
    \   EFuse CIM   ${bayList[${x}]}
    \   Sleep And Log Reason To Console   ${sleep}   reason=Sleeping ${sleep} after a CIM Hot Plug.

################
# CIM Failover: specific to CIM failover keywords
################
CIM Failover
    [Documentation]   Get the roles, perform failover and verify that role changed.
    [Arguments]   ${wait_task_timeout}=60m   ${wait_task_interval}=2s   ${cycle_sleep}=60m
    ${preFailoverRoles} =   Get HA Nodes
    Set To Dictionary   ${preFailoverRoles['Active']}   role=Standby
    Log   \nActivating standby CIM...   console=${True}
    Log   Current active: ${preFailoverRoles['Active']['name']}   console=${True}
    Log   Current standby: ${preFailoverRoles['Standby']['name']}   console=${True}
    ${resp} =   Fusion Api Edit HA Nodes   ${preFailoverRoles['Active']}   ${preFailoverRoles['Active']['uri']}
    fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    Sleep And Log Reason To Console   ${cycle_sleep}   reason=Sleeping ${cycle_sleep} after CIM failover.
    Log   Standby CIM activation complete.\n   console=${True}
    ${postFailoverRoles} =   Get HA Nodes
    CIM Role Should Have Changed   ${preFailoverRoles}   ${postFailoverRoles}
    
Get HA Nodes
    [Documentation]   Build roles dictionary for ease-of-access.
    Log To Console   Getting HA Nodes and building dictionary off it...
    ${resp} =   Fusion Api Get HA Nodes   /rest/appliance/ha-nodes
    ${roles} =   Create Dictionary
    :FOR   ${c}   IN   @{resp['members']}
    \   Set To Dictionary   ${roles}   ${c['role']}=${c}
    [Return]   ${roles}

CIM Role Should Have Changed
    [Documentation]   Verify that role changed and fail if not.
    [Arguments]   ${pre}   ${post}
    Log   Verifying that CIM role has changed, state is OK, status is OK and uri is correct...   console=${True}
    Log   Previous active: ${pre['Active']['name']}   console=${True}
    Log   Current active: ${post['Active']['name']}   console=${True}
    Log   Active State: ${post['Standby']['state']}   console=${True}
    Log   Active Status: ${post['Standby']['status']}   console=${True}
    Should Be Equal As Strings   ${pre['Active']['name']}   ${post['Standby']['name']}   msg=The expected new active CIM should now be ${pre['Standby']['name']}.
    Should Be Equal As Strings   ${pre['Active']['state']}   ${post['Standby']['state']}   msg=The expected state should be ${pre['Standby']['state']}.
    Should Be Equal As Strings   ${pre['Active']['status']}   ${post['Standby']['status']}   msg=The expected status should be ${pre['Standby']['status']}.
    Should Be Equal As Strings   ${pre['Active']['uri']}   ${post['Standby']['uri']}   msg=The expected uri should be ${pre['Standby']['uri']}.
    Log   CIM role change was successful.   console=${True}

Remove Standby CIM
    [Documentation]   Remove the standby CIM from the HA Nodes.
    [Arguments]   ${standbyCIM}   ${wait_task_timeout}=60m   ${wait_task_interval}=2s
    Log To Console   Removing standby CIM...
    Set To Dictionary   ${standbyCIM}   role=Unused
    ${resp} =   Fusion Api Edit HA Nodes   ${standbyCIM}   ${standbyCIM['uri']}
    ${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task}
    Log To Console   Remove standby appliance complete.

################
# EM Failover: specific to EM failover keywords
################
Process Enclosures
    [Documentation]   Process enclosure for EM Failover test.
    [Arguments]     ${enclosures}   ${sleep}=5m   ${hafnium_icm_model}=${HAFNIUM_MODEL}   ${iface}=eth0
    ${l} = 	Get Length	${enclosures}
    ${em_sessions} =   Create Dictionary
    :FOR	${x}	IN RANGE	0	${l}
    \   ${enc} =     Get From List   ${enclosures}    ${x}
    \   Log to console      ${enc}
    \   ${EM_IP} =   Get Variable Value   ${em_sessions['${enc}']['ip']}
    \   Run Keyword If   '${EM_IP}' == '${Null}'   Run Keywords   Set To Dictionary    ${em_sessions}   ${enc}=&{EMPTY}   AND   Get EM IP   ${enc}   iface=${iface}   AND   Set To Dictionary   ${em_sessions['${enc}']}   ip=${EM_IP}
    \   ${EM_TOKEN} =   Get Variable Value   ${em_sessions['${enc}']['token']}
    \   Run Keyword If   '${EM_TOKEN}' == '${Null}'   Run Keywords   Get EM Token   ${enc}   AND   Set To Dictionary   ${em_sessions['${enc}']}   token=${EM_TOKEN}
    \   ${bayNumber} =   Run Keyword If   "${FAILOVER_TARGET}" == "standby"   Get EM Standby Bay
    \   ...              ELSE             "${FAILOVER_TARGET}" == "active"    Get EM Active Bay
    \   Enclosure Manager Should Be In Expected State   ${enc}   ${bayNumber}   Standby
    \   EM Failover   ${bayNumber}
    \   Log to console   Sleeping. Waiting ${POST_EM_FAILOVER_SLEEP} for failover recovery.
    \   Sleep And Log Reason To Console   ${sleep}   reason=Sleeping ${sleep} after EM failover.
    \   Enclosure Manager Should Be In Expected State   ${enc}   ${bayNumber}   Active
    \   Check Common Resource Attributes
    \   Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    \   ${REMOTE_RUN_CHECKS} =   Get Variable Value   ${REMOTE_RUN_CHECKS}   @{EMPTY}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    \   Check For MeatGrinder Error
    \   Check For Multipath   hafnium_icm_model=${hafnium_icm_model}   iface=${iface}
    \   Check For Server In Read Only Filesystem
    \   common.Run Sequential Ping
    \   Fping Should Have No Loss
    \   Check For ISS Crash   iface=${iface}
    \   All Etherchannel Summary Ports Should Be Linked   iface=${iface}
    \   Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}

################
# ICM Hot Plug: specific to ICM hot plug keywords
################
Process ICMs For Synergy ICM Efuse Reset
    [Documentation]   Process interconnect modules for Synergy interconnect EFuseReset test.
    [Arguments]     ${icms}   ${wait_time}=150m   ${wait_interval}=15s   ${cycle_sleep}=60m   ${hafnium_icm_model}=${HAFNIUM_MODEL}   ${iface}=eth0
    Set Log Level	TRACE
    ${l} = 	Get Length	${icms}
    ${liUri} =   Run Keyword If   '${TARGET_LI}' != '${Null}'   Get LI Uri By Name   ${TARGET_LI}
    ${em_sessions} =   Create Dictionary
    :FOR	${x}	IN RANGE	0	${l}
    \   ${ic} =     Get From List   ${icms}    ${x}
    \   Continue For Loop If   '${liUri}' != '${Null}' and '${ic['logicalInterconnectUri']}' != '${liUri}'
    \   Log to console      ${ic['name']} ${ic['uri']}
    \   ${bay} =    Fetch from right    ${ic['name']}    ${SPACE}
    \   ${pass} =   Check For One Time Pass   ${ic['enclosureName']}:${bay}
    \   Run Keyword If   ${pass}   Continue For Loop
    \   ${skip} =   Run Keyword If   "${DO_ONLY}" != "${null}"   Run Keyword And Return Status   List Should Not Contain Value   ${DO_ONLY}   ${bay}
    \   Run Keyword If   ${skip}   Continue For Loop
    \   ${resp} =   Fusion Api Get Resource   ${icms[${x}]['enclosureUri']}
    \   ${EM_IP} =   Get Variable Value   ${em_sessions['${resp['serialNumber']}']['ip']}
    \   Run Keyword If   '${EM_IP}' == '${Null}'   Run Keywords   Set To Dictionary    ${em_sessions}   ${resp['serialNumber']}=&{EMPTY}   AND   Get EM IP   ${resp['serialNumber']}   iface=${iface}   AND   Set To Dictionary   ${em_sessions['${resp['serialNumber']}']}   ip=${EM_IP}
    \   ${EM_TOKEN} =   Get Variable Value   ${em_sessions['${resp['serialNumber']}']['token']}
    \   Run Keyword If   '${EM_TOKEN}' == '${Null}'   Run Keywords   Get EM Token   ${resp['serialNumber']}   AND   Set To Dictionary   ${em_sessions['${resp['serialNumber']}']}   token=${EM_TOKEN}
    \   Log   \t Waiting for ICM in Bay:${bay} to reach state:Configured|Monitored   console=${True}
    \   Wait Until Keyword Succeeds     ${wait_time}   ${wait_interval}      IC reached state    ${ic['uri']}    Configured|Monitored
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    [EFuseReset via RIS (RESET ICM)]
    \   Efuse ICM   EFuseReset     ${bay}
    \   Log   \t Waiting for ICM in Bay:${bay} to reach state:Configured|Monitored   console=${True}
    \   Wait Until Keyword Succeeds     ${wait_time}   ${wait_interval}      IC reached state    ${ic['uri']}    Configured|Monitored
    \   Sleep And Log Reason To Console   ${cycle_sleep}   reason=Sleeping ${cycle_sleep} after ICM EFuseReset to let things settle (DTO may update a little late).
    \   Check Common Resource Attributes
    \   Bonding Interfaces Should Be In Expected States   ${ic['uri']}   update_link_failure_count=${True}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    \   Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    \   Check For MeatGrinder Error
    \   Check For Multipath   hafnium_icm_model=${hafnium_icm_model}   iface=${iface}
    \   Check For Server In Read Only Filesystem
    \   common.Run Sequential Ping
    \   Fping Should Have No Loss
    \   Check For ISS Crash   iface=${iface}
    \   All Etherchannel Summary Ports Should Be Linked   iface=${iface}
    \   Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}

Process ICMs For Synergy ICM Hot Plug
    [Documentation]   Process interconnect modules for Synergy interconnect hot plug test.
    [Arguments]     ${icms}   ${wait_time}=35m   ${wait_interval}=15s   ${cycle_sleep}=60m   ${hafnium_icm_model}=${HAFNIUM_MODEL}   ${iface}=eth0
    Set Log Level	TRACE
    ${l} = 	Get Length	${icms}
    ${liUri} =   Run Keyword If   '${TARGET_LI}' != '${Null}'   Get LI Uri By Name   ${TARGET_LI}
    ${em_sessions} =   Create Dictionary
    :FOR	${x}	IN RANGE	0	${l}
    \   ${ic} =     Get From List   ${icms}    ${x}
    \   Continue For Loop If   '${liUri}' != '${Null}' and '${ic['logicalInterconnectUri']}' != '${liUri}'
    \   Log to console      ${ic['name']} ${ic['uri']}
    \   ${bay} =    Fetch from right    ${ic['name']}    ${SPACE}
    \   ${pass} =   Check For One Time Pass   ${ic['enclosureName']}:${bay}
    \   Run Keyword If   ${pass}   Continue For Loop
    \   ${skip} =   Run Keyword If   "${DO_ONLY}" != "${null}"   Run Keyword And Return Status   List Should Not Contain Value   ${DO_ONLY}   ${bay}
    \   Run Keyword If   ${skip}   Continue For Loop
    \   ${resp} =   Fusion Api Get Resource   ${icms[${x}]['enclosureUri']}
    \   ${EM_IP} =   Get Variable Value   ${em_sessions['serialNumber']['ip']}
    \   Run Keyword If   '${EM_IP}' == '${Null}'   Run Keywords   Set To Dictionary    ${em_sessions}   ${resp['serialNumber']}=&{EMPTY}   AND   Get EM IP   ${resp['serialNumber']}   iface=${iface}   AND   Set To Dictionary   ${em_sessions['${resp['serialNumber']}']}   ip=${EM_IP}
    \   ${EM_TOKEN} =   Get Variable Value   ${em_sessions['serialNumber']['token']}
    \   Run Keyword If   '${EM_TOKEN}' == '${Null}'   Run Keywords   Get EM Token   ${resp['serialNumber']}   AND   Set To Dictionary   ${em_sessions['${resp['serialNumber']}']}   token=${EM_TOKEN}
    \   Log   \t Waiting for ICM in Bay:${bay} to reach state:Configured|Monitored   console=${True}
    \   Wait Until Keyword Succeeds     ${wait_time}   ${wait_interval}      IC reached state    ${ic['uri']}    Configured|Monitored
    # Remove ICM
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    [EFUSE ON via RIS (REMOVE ICM)]
    \   Efuse ICM   EFuseOn     ${bay}
    \   Log   \t Waiting for ICM in Bay:${bay} to reach state:Absent   console=${True}
    \   Wait Until Keyword Succeeds     ${wait_time}   ${wait_interval}      IC reached state    ${ic['uri']}    Absent
    # Check that the bonding interfaces are in the expected state/status
    \   Run Keyword If   '${ic['model']}' == '${HAFNIUM_MODEL}'   Run Keywords   Bonding Interfaces Should Be In Expected States   ${ic['uri']}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}   AND   Set Test Variable   ${offline_interconnect}   ${ic['uri']}
    \   ...       ELSE   Set Test Variable   ${offline_interconnect}   ${Null}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${offline_interconnect}   tags=${REMOTE_CHECKS_TAG}
    # Insert ICM
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    [EFUSE OFF via RIS (INSERT ICM)]
    \   Efuse ICM   EFuseOff    ${bay}
    \   Log   \t Waiting for ICM in Bay:${bay} to reach state:Configured|Monitored   console=${True}
    \   Wait Until Keyword Succeeds     ${wait_time}   ${wait_interval}      IC reached state    ${ic['uri']}    Configured|Monitored
    \   Sleep And Log Reason To Console   ${cycle_sleep}   reason=Sleeping ${cycle_sleep} after ICM Hot Plug to let things settle (DTO may update a little late).
    \   Check Common Resource Attributes
    \   Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    \   Check For MeatGrinder Error
    \   Check For Multipath   hafnium_icm_model=${hafnium_icm_model}   iface=${iface}
    \   Check For Server In Read Only Filesystem
    \   common.Run Sequential Ping
    \   Fping Should Have No Loss
    \   Check For ISS Crash   iface=${iface}
    \   All Etherchannel Summary Ports Should Be Linked   iface=${iface}
    \   Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}

Process ICMs For C7000 ICM Hot Plug
    [Documentation]   Process interconnect modules for C-Series interconnect hot plug test.
    [Arguments]    ${icms_uri}   ${state_timeout}=35m   ${state_interval}=15s   ${remove_sleep}=2m   ${cycle_sleep}=15m
    Set Log Level	TRACE
    ${icms_uriItems}=    Get Dictionary Items    ${icms_uri}
    :FOR  ${bay}  ${uri}    IN  @{icms_uriItems}
    \   ${icmResp} =   Fusion Api Get Resource   ${uri}
    \   ${pass} =   Check For One Time Pass   ${icmResp['enclosureName']}:${bay}
    \   Run Keyword If   ${pass}   Continue For Loop
    \   Log   \t Waiting for ICM in Bay:${bay} to reach state:Configured|Monitored   console=${True}
    \   Wait Until Keyword Succeeds     ${state_timeout}   ${state_interval}      IC reached state    ${uri}    Configured|Monitored
    \   Execute OA Diag Command   efuse iom ${bay} off
    \   Log   \t Waiting for ICM in Bay:${bay} to reach state:Absent   console=${True}
    \   Wait Until Keyword Succeeds     ${state_timeout}   ${state_interval}      IC reached state    ${uri}    Absent
    \   Sleep And Log Reason To Console   ${remove_sleep}   reason=Sleeping ${remove_sleep} after removing an ICM.
    \   Bonding Interfaces Should Be In Expected States   ${uri}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    [EFUSE ON via OA (INSERT ICM)]
    \   Execute OA Diag Command   efuse iom ${bay} on
    \   Log   \t Waiting for ICM in Bay:${bay} to reach state:Configured|Monitored   console=${True}
    \   Wait Until Keyword Succeeds     ${state_timeout}   ${state_interval}      IC reached state    ${uri}    Configured|Monitored
    \   Sleep And Log Reason To Console   ${cycle_sleep}   reason=Sleeping ${cycle_sleep} after ICM Hot Plug cycle to let things settle (DTO may update a little late).
    \   Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}

################
# ICM Reboot: specific to ICM Reboot keywords
################
Process ICMs For Synergy ICM Reboot
    [Documentation]   Process interconnect modules for Synergy interconnect reboot test.
    [Arguments]     ${icms}   ${power_wait_timeout}=60m   ${power_wait_interval}=2s   ${maintenance_timeout}=60m   ${maintenance_interval}=30s   ${configure_timeout}=60m   ${configure_interval}=30s   ${alert_timeout}=240m   ${alert_interval}=30s   ${sleep}=30m   ${hafnium_icm_model}=${HAFNIUM_MODEL}   ${iface}=eth0
    Set Log Level	TRACE
    ${icm_len} = 	Get Length	${icms}
    ${liUri} =   Run Keyword If   '${TARGET_LI}' != '${Null}'   Get LI Uri By Name   ${TARGET_LI}
    :FOR	${x}	IN RANGE	0	${icm_len}
    \   ${ic} =     Get From List   ${icms}    ${x}
    \   Continue For Loop If   '${liUri}' != '${Null}' and '${ic['logicalInterconnectUri']}' != '${liUri}'
    \   ${bay} =   Fetch From Right   ${ic['name']}   ${SPACE}
    \   ${pass} =   Check For One Time Pass   ${ic['enclosureName']}:${bay}
    \   Run Keyword If   ${pass}   Continue For Loop
    \   ${skip} =   Run Keyword If   "${DO_ONLY}" != "${null}"   Run Keyword And Return Status   List Should Not Contain Value   ${DO_ONLY}   ${bay}
    \   Run Keyword If   ${skip}   Continue For Loop
    \   Log to console      ${ic['name']} ${ic['uri']}
    \   Power request    ${ic['uri']}   Off   power_wait_timeout=${power_wait_timeout}   power_wait_interval=${power_wait_interval}
    \   Log   \t Waiting for ${ic['uri']} to reach state:Maintenance   console=${True}
    \   Wait Until Keyword Succeeds     ${maintenance_timeout}   ${maintenance_interval}      IC reached state    ${ic['uri']}    Maintenance
    # Check that the bonding interfaces are in the expected state/status
    \   Run Keyword If   '${ic['model']}' == '${HAFNIUM_MODEL}'   Run Keywords   Bonding Interfaces Should Be In Expected States   ${ic['uri']}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}   AND   Set Test Variable   ${offline_interconnect}   ${ic['uri']}
    \   ...       ELSE   Set Test Variable   ${offline_interconnect}   ${Null}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${offline_interconnect}   tags=${REMOTE_CHECKS_TAG}
    \   Power request    ${ic['uri']}   On   power_wait_timeout=${power_wait_timeout}   power_wait_interval=${power_wait_interval}
    \   Log   \t Waiting for ${ic['uri']} to reach state:Configured   console=${True}
    \   Wait Until Keyword Succeeds     ${configure_timeout}   ${configure_interval}      IC reached state    ${ic['uri']}    Configured
    \   Log   \t Waiting for ConnectionInstance Alerts to reach zero...   console=${True}
    \   Wait Until Keyword Succeeds     ${alert_timeout}   ${alert_interval}      ConnectionInstance Alert Count Should Be Zero
    \   Run Keyword If   '${ICM_MODEL}' != '${CARBON}'   Sleep And Log Reason To Console   ${sleep}   reason=It is not a Carbon interconnect module. Sleeping for ${sleep} to let the resources recover from alerts/errors...
    \   Check Common Resource Attributes
    \   Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    \   Check For MeatGrinder Error
    \   Check For Multipath   hafnium_icm_model=${hafnium_icm_model}   iface=${iface}
    \   Check For Server In Read Only Filesystem
    \   common.Run Sequential Ping
    \   Fping Should Have No Loss
    \   Check For ISS Crash   iface=${iface}
    \   All Etherchannel Summary Ports Should Be Linked   iface=${iface}
    \   Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}

Power request
    [Documentation]   Send an interconnect power request to OneView.
    [Arguments]     ${uri}    ${power}   ${power_wait_timeout}=60m   ${power_wait_interval}=2s   ${wait_time}=10m   ${interval}=20s
    ${data} =   Create Dictionary   op=replace
    ...                             path=/powerState
    ...                             value=${power}
    ${body} =   Create List     ${data}
    Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    Powering ${power}: ${uri}
    ${resp} =   Fusion Api Patch Interconnect   body=${body}    uri=${uri}
    ${task} =   fusion_api_appliance_setup.Wait for Task   ${resp}  timeout=${power_wait_timeout}   interval=${power_wait_interval}
    ${valDict} =    Create Dictionary       status_code=${200}
    ...                                 taskState=Completed
    fusion_api_validation.Validate Response       ${task}   ${valDict}
    Log   \t Waiting for ${uri} to reach powerState:${power}   console=${True}
    Wait Until Keyword Succeeds     ${wait_time}   ${interval}      Should Match Interconnect Power State    ${uri}    ${power}

ConnectionInstance Alert Count Should Be Zero
    [Documentation]   Check that ConnectionInstance alerts are all cleared.
    ...               That is https://localhost/rest/alerts?filter="alertState='Active'"\&filter="healthCategory='ConnectionInstance'"
    ${uri} =   set variable   /rest/alerts?filter="alertState='Active'"&filter="healthCategory='ConnectionInstance'"
    ${resp} =   fusion api get resource     ${uri}
    Should Be Equal As Integers  	${resp['count']}    0

Should Match Interconnect Power State
    [Documentation]   Current interconnect power state should match to the value of ${state} argument
    [Arguments]	    ${uri}  ${state}
    Set Log Level	TRACE
    ${resp} =   fusion api get resource     ${uri}
    Log   \t ${uri}: ${resp['powerState']}   console=${True}
    Should Match Regexp 	${resp['powerState']}    ${state}
    [Return]	${resp}

Get Interconnects
    [Documentation]   Get interconnects from OneView
    ${resp} =   Fusion Api Get Interconnect
    ${ic_list} =    Create List
    ${ics} =     Get From Dictionary     ${resp}    members
    ${ic_len} = 	Get Length	${ics}
    :FOR	${x}	IN RANGE	0	${ic_len}
    \   ${ic} =     Get From List   ${ics}    ${x}
    \ 	Run Keyword If 	'${ic['model']}' != '${ICM_MODEL}'		Continue For Loop
    \   Append to list      ${ic_list}  ${ic}
    ${ordered_list} =   robustness-helper.order_icms    ${ic_list}     ${ICM_ORDER}
    [Return]    ${ordered_list}

Process ICMs For C7000 ICM Reboot
    [Documentation]   Process interconnect modules for C-Series interconnect reboot test.
    [Arguments]    ${icms_uri}   ${reboot_sleep}=2m   ${configure_timeout}=35m   ${configure_interval}=15s   ${cycle_sleep}=5m   ${retry_max}=3   ${retry_interval}=10s
    Set Log Level	TRACE
    ${icms_uriItems}=    Get Dictionary Items    ${icms_uri}
    :FOR  ${bay}  ${uri}    IN  @{icms_uriItems}
    \   ${icmResp} =   Fusion Api Get Resource   ${uri}
    \   ${pass} =   Check For One Time Pass   ${icmResp['enclosureName']}:${bay}
    \   Run Keyword If   ${pass}   Continue For Loop
    \   Log   \t Restarting ICM in Bay:${bay}   console=${True}
    \   WPST Execute Oacli Command   ${OA_CREDENTIAL_DATA}  restart interconnect ${bay}
    #NOTE: No need to do this. Had chat with Scot Greenidge and in normal case OneView will not change state.
    #      Change of state only occurs when OA returns power state off as a consequence of interconnect reset.
    #\   Log   \t Waiting for ICM in Bay:${bay} to reach state:Absent   console=${True}
    #\   Wait Until Keyword Succeeds     ${wait_time}   ${interval}      IC reached state    ${uri}    Absent
    \   Sleep And Log Reason To Console   ${reboot_sleep}   reason=Sleeping ${reboot_sleep} just in case OA returns power state off after the reset.
    \   Log   \t Waiting for ICM in Bay:${bay} to reach state:Configured|Monitored   console=${True}
    \   Wait Until Keyword Succeeds     ${configure_timeout}   ${configure_interval}      IC reached state    ${uri}    Configured|Monitored
    \   Sleep And Log Reason To Console   ${cycle_sleep}   reason=Sleeping ${cycle_sleep} to let things settle after an ICM Reboot (DTO may update a little late).
    \   Bonding Interfaces Should Be In Expected States   ${uri}   update_link_failure_count=${True}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    \   Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}

################
# ICM Reset: specific to ICM Reset keywords
################
Process ICMs For ICM Reset
    [Documentation]   Process interconnect modules for Synergy interconnect reset test.
    [Arguments]     ${icms}   ${wait_task_timeout}=2m   ${wait_task_interval}='2s'   ${sleep}=10m   ${hafnium_icm_model}=${HAFNIUM_MODEL}   ${iface}=eth0
    Set Log Level	TRACE
    ${icm_len} = 	Get Length	${icms}
    ${liUri} =   Run Keyword If   '${TARGET_LI}' != '${Null}'   Get LI Uri By Name   ${TARGET_LI}
    :FOR	${x}	IN RANGE	0	${icm_len}
    \   ${ic} =     Get From List   ${icms}    ${x}
    \   Continue For Loop If   '${liUri}' != '${Null}' and '${ic['logicalInterconnectUri']}' != '${liUri}'
    \   ${bay} =   Fetch From Right   ${ic['name']}   ${SPACE}
    \   ${skip} =   Run Keyword If   "${DO_ONLY}" != "${null}"   Run Keyword And Return Status   List Should Not Contain Value   ${DO_ONLY}   ${bay}
    \   Run Keyword If   ${skip}   Continue For Loop
    \   Log to console      ${ic['name']} ${ic['uri']}
    \   ${data} =   Create Dictionary   op=replace
    \   ...                             path=/deviceResetState
    \   ...                             value=Reset
    \   ${body} =   Create List     ${data}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    Resetting: ${ic['name']} ${ic['uri']}
    \   ${resp} =   Fusion Api Patch Interconnect   body=${body}    uri=${ic['uri']}
    \   ${task} =   fusion_api_appliance_setup.Wait for Task   ${resp}  timeout=${wait_task_timeout}   interval=${wait_task_interval}

    \   ${valDict} =    Create Dictionary       status_code=${200}
    \   ...                                 taskState=Completed
    \   fusion_api_validation.Validate Response       ${task}   ${valDict}
    # Check that the bonding interfaces are in the expected state/status
    \   Run Keyword If   '${ic['model']}' == '${HAFNIUM_MODEL}'   Run Keywords   Bonding Interfaces Should Be In Expected States   ${ic['uri']}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}   AND   Set Test Variable   ${offline_interconnect}   ${ic['uri']}
    \   ...       ELSE   Set Test Variable   ${offline_interconnect}   ${Null}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${offline_interconnect}   tags=${REMOTE_CHECKS_TAG}
    \   Sleep And Log Reason To Console   ${sleep}   reason=Sleeping ${sleep} after an ICM Reset.

    \   Log   -Verify it's reset   console=${True}
    \   ${ic} =     Get Interconnect Filter By Name  ${ic['name']}
    \   ${deviceResetState} =   Get From Dictionary   ${ic}   deviceResetState
    \   Should Be Equal As Strings    ${deviceResetState}  Normal
    \   Check Common Resource Attributes
    \   Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    \   Check For MeatGrinder Error
    \   Check For Multipath   hafnium_icm_model=${hafnium_icm_model}   iface=${iface}
    \   Check For Server In Read Only Filesystem
    \   common.Run Sequential Ping
    \   Fping Should Have No Loss
    \   Check For ISS Crash   iface=${iface}
    \   All Etherchannel Summary Ports Should Be Linked   iface=${iface}
    \   Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}

Get Interconnect Filter By Name
    [Documentation]   Get interconnect filtered by name and return interconnect json data
    [Arguments]     ${ic_name}
    ${resp} =   fusion api get interconnect
    ${ics} =     Get From Dictionary     ${resp}    members
    ${l} =  Get Length      ${ics}
    :FOR    ${x}    IN RANGE        0       ${l}
    \   ${ic} =     Get From List   ${ics}    ${x}
    \       Exit For Loop If        '${ic['name']}' == '${ic_name}'
    [Return]    ${ic}

################
# LE Add Remove: specific to LE Add Remove keywords
################
Get LEs
    [Documentation]   Get logical enclosures attributes and return them as list of dictionary.
    ${resp} =   fusion api get logical enclosure
    ${les} =    Create List
    ${le_list} =     Get From Dictionary     ${resp}    members
    ${l} = 	Get Length	${le_list}
    :FOR	${x}	IN RANGE	0	${l}
    \   ${le} =     Get From List   ${le_list}    ${x}
    \   ${le_details} =    Create Dictionary     name=${le['name']}
    \   ...                                      uri=${le['uri']}
    \   ...                                      state=${le['state']}
    \   ...                                      status=${le['status']}
    \   ...                                      enclosureUris=${le['enclosureUris']}
    \   append to list    ${les}   ${le_details}
    [Return]    ${les}

Check LEs and enclosures
    [Documentation]   Check that logical enclosures are OK and Consistent state and that enclosures are OK and Configured state.
    ...   NOTE: This keyword is DEPRECATED. See 'Check Common Resource Attributes'.
    [Arguments]     ${les}
    Set Log Level	TRACE
    Log to console   \nChecking LEs and enclosures....
    ${valDict} = 	Create Dictionary	state=Consistent
    ...						status=OK
    ${l} = 	Get Length	${les}
    :FOR	${x}	IN RANGE	0	${l}
    \   ${le} =     Get From List   ${les}    ${x}
    \   fusion_api_validation.Validate Response   ${le}   ${valDict}
    \   Check enclosures    ${le['enclosureUris']}

Get LIs
    [Documentation]   Get logical interconnects attributes and return it as list of dictionary.
    ${resp} =   fusion api get li
    ${lis} =    Create List
    ${li_list} =     Get From Dictionary     ${resp}    members
    ${l} = 	Get Length	${li_list}
    :FOR	${x}	IN RANGE	0	${l}
    \   ${li} =     Get From List   ${li_list}    ${x}
    \   ${li_details} =    Create Dictionary     name=${li['name']}
    \   ...                                      uri=${li['uri']}
    \   ...                                      state=${li['state']}
    \   ...                                      status=${li['status']}
    \   ...                                      interconnects=${li['interconnects']}
    \   append to list    ${lis}   ${li_details}
    [Return]    ${lis}

Get LI Uri By Name
    [Documentation]   Get logical interconnect uri by the given name.
    [Arguments]   ${liName}
    ${resp} =   Fusion Api Get LI
    ${liData} =   Filter Attribute From Response Body   ${resp}   name   ${liName}
    ${uri} =   Get Variable Value   ${liData['uri']}
    Run Keyword If   '${uri}' == '${Null}'   Fail   msg=Unable to find uri for logical interconnect: ${liName}
    [Return]   ${uri}

Check LIs And Interconnects
    [Documentation]   Check that logical interconnects and interconnects are in the expected state.
    ...    NOTE: This keyword is DEPRECATED. See 'Check Common Resources Attributes'.
    [Arguments]     ${lis}
    Set Log Level	TRACE
    Log to console   \nChecking LIs and interconnects....
    # NOTE: For Logical Interconnects state has the following possible values:
    # Active, Degraded, Failed and Unknown. When the logical interconnect is
    # newly created it is placed in Unknown state. However, I am only seeing
    # Unknown state for LI so I wrote this quix: QXCR1001495111:
    # [CI-FIT] LI state is always Unknown
    ${valDict} = 	Create Dictionary	state=Unknown
    ...						status=((?i)OK|Warning)
    ${l} = 	Get Length	${lis}
    :FOR	${x}	IN RANGE	0	${l}
    \   ${li} =        Get From List   ${lis}    ${x}
    \   ${li_uri} =    Get from Dictionary   ${li}   uri
    \   ${resp} =       Fusion Api Get Resource    ${li_uri}
    \   fusion_api_validation.Validate Response Regex   ${resp}   ${valDict}
    \   Check interconnects    ${li['interconnects']}

Check Interconnects
    [Documentation]   Check that interconnects are OK and Configured state.
    ...    NOTE: This keyword is DEPRECATED. See 'Check Common Resources Attributes'.
    [Arguments]     ${icms}   ${state}=Configured   ${status}=OK
    Set Log Level	TRACE
    ${valDict} = 	Create Dictionary	state=${state}
    ...					status=${status}
    ${l} = 	Get Length	${icms}
    :FOR	${x}	IN RANGE	0	${l}
    \   ${icm} =        Get From List   ${icms}    ${x}
    \   ${resp} =       Fusion Api Get Resource    ${icm}
    \   fusion_api_validation.Validate Response   ${resp}   ${valDict}

Check Enclosures
    [Documentation]   Check that enclosures are OK and Configured state.
    [Arguments]     ${encs}
    Set Log Level	TRACE
    ${valDict} = 	Create Dictionary	state=Configured
    ...					status=OK
    ${l} = 	Get Length	${encs}
    :FOR	${x}	IN RANGE	0	${l}
    \   ${enc} =        Get From List   ${encs}    ${x}
    \   ${resp} =       Fusion Api Get Resource    ${enc}
    \   fusion_api_validation.Validate Response   ${resp}   ${valDict}

Blade Should Be In Expected State
    [Documentation]   Fail if blade is not in the expected state or status.
    ...               The keyword-level argument ignore_blade_bay is to exclude status checking of the blade (remove status from valDict) if it is listed in IGNORE_BLADES variable.
    [Arguments]     ${blade}   ${ignore_blade_bay}=${Null}
    Set Log Level	TRACE
    ${resp} =       Fusion Api Get Resource    ${blade}
    ${valDict} = 	Create Dictionary	state=((?i)Monitored|Unmanaged|ProfileApplied)
    ...									status=OK
    ${ignore_blade_bay} =   Convert To String   ${ignore_blade_bay}
    :FOR   ${b}   IN   @{IGNORE_BLADES}
    \    Run Keyword If   '${ignore_blade_bay}' == '${b}'   Remove From Dictionary   ${valDict}   status
    fusion_api_validation.Validate Response Regex  ${resp}   ${valDict}

################
# Profiles Helper
################
Create New Server Profile And Assign Server Hardware
    [Documentation]   Create new server profile and assign server hardware to it.
    [Arguments]   ${server_profiles_nohw}   ${server_profile_to_bay_map}   ${forceProfileApply}=false
    ${param} =   Run Keyword If   '${forceProfileApply}' != 'false'   Set Variable   ?force="${forceProfileApply}"
    ...                    ELSE   Set Variable   ${EMPTY}
    Add Server Profiles from variable no hardware   ${server_profiles_nohw}   ${server_profile_to_bay_map}
    common.Assign Server Hardware To Existing Profiles From Variable   ${server_profiles_nohw}   ${server_profile_to_bay_map}   timeout=30m   interval=5m   waitForTask=${True}   forceProfileApply=${forceProfileApply}

Create Profile Connection
    [Documentation]   Create a profile connection of a given profile name.
    [Arguments]   ${profileName}   ${connectionBody}   ${message}=Creating profile connection.   ${wait_task_timeout}=15m   ${wait_task_interval}=10s   ${forceProfileApply}=false
    ${param} =   Run Keyword If   '${forceProfileApply}' != 'false'   Set Variable   ?force="${forceProfileApply}"
    ...                    ELSE   Set Variable   ${EMPTY}
    ${resp} =   Fusion Api Get Resource   /rest/server-profiles?filter=name='${profileName}'
    ${profile} =   Get From Dictionary   ${resp}   members
    ${profile} =   Set Variable   ${profile[0]}
    common.Power Off Server Uri   ${profile['serverHardwareUri']}
    Append To List   ${profile['connectionSettings']['connections']}   ${connectionBody}
    #There is something here that REST call can do but not GUI: recreate
    #a connection and re-using the connection id.
    Log   ${message}   console=${True}
    ${resp} =   Fusion Api Edit Server Profile    uri=${profile['uri']}   body=${profile}   param=${param}
    ${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task}
    common.Power On Server Uri   ${profile['serverHardwareUri']}

Assign Server Hardware To Existing Profiles From Variable
	[Documentation]	Update Server Profiles from a variable with server hardware assigned to profile from mapping variable
        ...             NOTE: If ${waitForTask} is false, ${parallel} and ${validate} becomes moot. Just fork the process and exit.
	[Arguments]		${profiles}   ${server_profile_to_bay_map}   ${timeout}=860m   ${interval}=15s  ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}   ${forceProfileApply}=false   ${throttle}=${Null}
        ${param} =   Run Keyword If   '${forceProfileApply}' != 'false'   Set Variable   ?force="${forceProfileApply}"
        ...                    ELSE   Set Variable   ${EMPTY}
	${existing_profiles} =  	Fusion Api Get Server Profiles
	${profile_members}	Get From Dictionary	${existing_profiles}	members
	${Count} =	Get From Dictionary	${existing_profiles}	count
        ${valDict} =    Create Dictionary   status_code=${200}
        ...                                 taskState=Completed
        ${respList} =   Create List
        Set Suite Variable   ${forkedErrorFound}   ${False}
	:FOR 	${Index}	IN RANGE	0	${Count}
	\	${sp}		Get From List	${profile_members}	${Index}
        \       Continue For Loop If   '${server_profile_to_bay_map['${sp['name']}']}' == '${null}'
	\	${shUri} = 	Get Server Hardware URI    ${server_profile_to_bay_map['${sp['name']}']}
        \       ${profile} =    Fusion Api Get Resource    uri=${sp['uri']}
	\       Set To Dictionary    ${profile}   serverHardwareUri=${shUri}
        \       Remove From Dictionary    ${profile}   status_code    headers
        \	Log To Console 	 \nAssigning server hardware URI \"${shUri}\" to profile \"${sp['name']}\"
        \       ${resp} =   Fusion Api Edit Server Profile    uri=${sp['uri']}   body=${profile}   param=${param}
        \       Continue For Loop If   ${waitForTask} != ${True}
        \       Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
        \       ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${timeout}   ${interval}   ${validate}
        \       Continue For Loop If   '${throttle}' == '${Null}'
        \       Continue For Loop If   ${parallel} != ${True}
        \       ${respLength} =   Get Length   ${respList}
        \       Continue For Loop If   ${respLength} != ${throttle}
        \       ${respList} =   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${timeout}   ${interval}   ${validate}   throttle=${throttle}
        Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${timeout}   ${interval}   ${validate}
        Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=Not all forked tasks state finished with Completed.

Unassign Server Profiles
        [Documentation]   Update server profiles in OneView by unassigning the server hardware from it. Argument requires list of dictionary of profiles that contains a valid server profile uri (e.g.: [{'uri': '/rest/server-profiles/8e2ec303-1274-4b9e-9871-b08f77bcc675'}]).
        ...               NOTE: See robustness' LE-add-remove.txt script for example.
        [Arguments]     ${profiles}    ${timeout}=860m   ${interval}=15s  ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}   ${forceProfileApply}=false   ${throttle}=${Null}
        Set Log Level	TRACE
        ${param} =   Run Keyword If   '${forceProfileApply}' != 'false'   Set Variable   ?force="${forceProfileApply}"
        ...                    ELSE   Set Variable   ${EMPTY}
        ${valDict} =    Create Dictionary   status_code=${200}
        ...                                 taskState=Completed
        ${respList} =   Create List
        Set Suite Variable   ${forkedErrorFound}   ${False}
        :FOR   ${p}   IN   @{profiles}
        \   ${profile} =    Fusion Api Get Resource    uri=${p['uri']}
        \   fusion_api_appliance_setup.Log to console and logfile  	Unassigning server hardware URI \"${profile['serverHardwareUri']}\" from profile \"${p['name']}\"
        \   set to dictionary    ${profile}   serverHardwareUri=${None}
        \   set to dictionary    ${profile}   enclosureBay=${None}
        \   set to dictionary    ${profile}   enclosureUri=${None}
        \   remove from dictionary    ${profile}   status_code    headers
        \   ${resp} =   fusion api edit server profile    uri=${p['uri']}   body=${profile}   param=${param}
        \   Continue For Loop If   ${waitForTask} != ${True}
        \   Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
        \   ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${timeout}   ${interval}   ${validate}
        \       Continue For Loop If   '${throttle}' == '${Null}'
        \       Continue For Loop If   ${parallel} != ${True}
        \       ${respLength} =   Get Length   ${respList}
        \       Continue For Loop If   ${respLength} != ${throttle}
        \       ${respList} =   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${timeout}   ${interval}   ${validate}   throttle=${throttle}
        Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${timeout}   ${interval}   ${validate}
        Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=Not all forked tasks state finished with Completed.

Update Profile Connection
    [Documentation]   Update a profile connection attribute of the given profile name and connection id.
    [Arguments]   ${profileName}   ${connectionId}   ${key}   ${value}   ${wait_task_timeout}=15m   ${wait_task_interval}=10s   ${forceProfileApply}=false
    ${param} =   Run Keyword If   '${forceProfileApply}' != 'false'   Set Variable   ?force="${forceProfileApply}"
    ...                    ELSE   Set Variable   ${EMPTY}
    ${resp} =   Fusion Api Get Resource   /rest/server-profiles?filter=name='${profileName}'
    ${profile} =   Get From Dictionary   ${resp}   members
    ${profile} =   Set Variable   ${profile[0]}
    common.Power Off Server Uri   ${profile['serverHardwareUri']}
    ${connections} =   Create List
    :FOR   ${c}   IN   @{profile['connectionSettings']['connections']}
    \   Run Keyword If   ${c['id']} == ${connectionId}   Set To Dictionary   ${c}   ${key}=${value}
    \   Append To List   ${connections}   ${c}
    Set To Dictionary   ${profile['connectionSettings']}   connections=${connections}
    Log   \nUpdating profile ${profileName} connection ${connectionId} key-value pair to ${key}:${value}.   console=${True}
    ${resp} =   Fusion Api Edit Server Profile    uri=${profile['uri']}   body=${profile}   param=${param}
    ${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task}
    common.Power On Server Uri   ${profile['serverHardwareUri']}

Delete Profile Connection
    [Documentation]   Delete a profile connection of a given profile name and return the deleted connection.
    [Arguments]   ${profileName}   ${connectionId}   ${message}=Deleting profile connection.   ${wait_task_timeout}=15m   ${wait_task_interval}=10s   ${proceedPressAndHold}=${Null}
    ${resp} =   Fusion Api Get Resource   /rest/server-profiles?filter=name='${profileName}'
    ${profile} =   Get From Dictionary   ${resp}   members
    ${profile} =   Set Variable   ${profile[0]}
    common.Power Off Server Uri   ${profile['serverHardwareUri']}   proceedPressAndHold=${proceedPressAndHold}
    ${connections} =   Create List
    ${connectionToDelete} =   Set Variable   ${null}
    :FOR   ${c}   IN   @{profile['connectionSettings']['connections']}
    \   Run Keyword If   ${c['id']} == ${connectionId}   Set Test Variable   ${connectionToDelete}   ${c}
    \   Run Keyword If   ${c['id']} == ${connectionId}   Continue For Loop
    \   Append To List   ${connections}   ${c}
    Set To Dictionary   ${profile['connectionSettings']}   connections=${connections}
    Log   ${message}   console=${True}

    ${resp} =   Fusion Api Edit Server Profile    uri=${profile['uri']}   body=${profile}
    ${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task}
    Run Keyword If   ${connectionToDelete} is ${null}   Log   Connection id $[connectionId} not found in profile name "${profileName}".   WARN
    common.Power On Server Uri   ${profile['serverHardwareUri']}
    [Return]   ${connectionToDelete}

Asynchronous Task Should Contain Error Code
    [Documentation]   Check that an asynchronous task contains the expected error code and fail if not.
    [Arguments]   ${response}   ${expectedErrorCode}
    ${errorFound} =   Set Variable   ${False}
    ${l} =   Get Length   ${response['taskErrors']}
    :FOR   ${i}   IN RANGE   0   ${l}
    \   Log   \n errorCode: ${response['taskErrors'][${i}]['errorCode']} \n errorSource: ${response['taskErrors'][${i}]['errorSource']} \n message: ${response['taskErrors'][${i}]['message']}
    \   Run Keyword If   '${response['taskErrors'][${i}]['errorCode']}' == '${expectedErrorCode}'   Set Test Variable   ${errorFound}   ${True}
    Run Keyword If   '${errorFound}' == '${False}'   Fail   msg=Unable to find the expected errorCode: ${expectedErrorCode}

Delete Profile Connection With Primary Boot
    [Documentation]   Delete a profile connection with primary boot of a given profile name and return the deleted connection.
    [Arguments]   ${profileName}   ${connectionId}   ${message}=Deleting profile connection.   ${wait_task_timeout}=15m   ${wait_task_interval}=10s
    ${resp} =   Fusion Api Get Resource   /rest/server-profiles?filter=name='${profileName}'
    ${profile} =   Get From Dictionary   ${resp}   members
    ${profile} =   Set Variable   ${profile[0]}
    common.Power Off Server Uri   ${profile['serverHardwareUri']}
    ${connections} =   Create List
    ${connectionToDelete} =   Set Variable   ${null}
    :FOR   ${c}   IN   @{profile['connectionSettings']['connections']}
    \   Run Keyword If   ${c['id']} == ${connectionId}   Set Test Variable   ${connectionToDelete}   ${c}
    \   Run Keyword If   ${c['id']} == ${connectionId}   Continue For Loop
    \   Append To List   ${connections}   ${c}
    Set To Dictionary   ${profile['connectionSettings']}   connections=${connections}
    Log   ${message}   console=${True}

    ${resp} =   Fusion Api Edit Server Profile    uri=${profile['uri']}   body=${profile}
    ${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Asynchronous Task Should Contain Error Code   ${task}   INVALID_SECONDARY_BOOT_CONNECTION
    common.Power On Server Uri   ${profile['serverHardwareUri']}

Get Profiles
    [Documentation]   Get server profiles attributes and return them as list of dictionary.
    [Arguments]   ${connectionSettingsApi}=${600}
    ${resp} =             fusion api get server profiles
    ${profiles} =         Create List
    ${profile_list} =     Get From Dictionary     ${resp}    members
    ${l} = 	Get Length	${profile_list}
    :FOR	${x}	IN RANGE	0	${l}
    \   ${profile} =     Get From List   ${profile_list}    ${x}
    \   ${profile_details} =    Create Dictionary     name=${profile['name']}
    \   ...                                           uri=${profile['uri']}
    \   ...                                           state=${profile['state']}
    \   ...                                           status=${profile['status']}
    \   ...                                           serverHardwareUri=${profile['serverHardwareUri']}
    \   ...                                           connectionSettings=&{EMPTY}
    \   ${connectionSettings} =   Evaluate   ${profile}.get('connectionSettings', None)
    \   ${connections} =   Run Keyword If   ${X-API-Version} >= ${connectionSettingsApi} and ${connectionSettings} is not ${null}   Evaluate   ${profile['connectionSettings']}.get("connections",None)
    \   ...                          ELSE   Evaluate   ${profile}.get("connections",None)
    \   Run Keyword If   ${X-API-Version} >= ${connectionSettingsApi}   Set to Dictionary   ${profile_details['connectionSettings']}  connections=${connections}
    \   ...       ELSE   Run Keywords   Remove From Dictionary   ${profile_details}   connectionSettings   AND   Set to Dictionary   ${profile_details}   connections=${connections}
    \   append to list    ${profiles}   ${profile_details}
    [Return]    ${profiles}

Get Blades From Profiles
    [Documentation]   Get blades uri from server profiles.
    [Arguments]     ${profiles}
    ${resp} =   Get Server Hardware Uris From Profiles   ${profiles}
    [Return]    ${resp}

Check Profiles And Blades
    [Documentation]   Check that server profiles and server hardware are in expected states.
    [Arguments]     ${profiles}
    Set Log Level	TRACE
    Log to console   \nChecking profiles and blades....
    ${valDict} = 	Create Dictionary	state=Normal
    ...					status=((?i)OK|Warning)
    ${l} = 	Get Length	${profiles}
    :FOR	${x}	IN RANGE	0	${l}
    \   ${profile} =        Get From List   ${profiles}    ${x}
    \   ${resp} =       Fusion Api Get Resource    ${profile['uri']}
    \   fusion_api_validation.Validate Response Regex   ${resp}   ${valDict}
    \   Run Keyword If  '${profile['serverHardwareUri']}' != '${null}'    Blade Should Be In Expected State    ${profile['serverHardwareUri']}   ignore_blade_bay=${resp['enclosureBay']}

Delete Server Profiles From Variable
    [Documentation]   Delete server profiles from data variable.
    [Arguments]   ${server_profiles}   ${wait_timeout}=300m   ${wait_interval}=15s  ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}
    ${deleteCreateProfiles} =   Create List
    :FOR   ${p}   IN   @{server_profiles}
    \   ${profiles} =   Fusion Api Get Server Profiles  param=?filter="name='${p['name']}'"
    \   Append To List   ${deleteCreateProfiles}   ${profiles}
    ${valDict} =   Create Dictionary   status_code=${200}
    ...                                taskState=Completed
    ${respList} =   Create List
    Set Suite Variable   ${forkedErrorFound}   ${False}
    :FOR   ${profile}   IN   @{deleteCreateProfiles}
    \   common.Power Off Server Uri   ${profile['members'][0]['serverHardwareUri']}
    \   ${resp} =   Fusion Api Delete Server Profile   uri=${profile['members'][0]['uri']}
    \   Continue For Loop If   ${waitForTask} != ${True}
    \   Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
    \   ...   ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${wait_timeout}   ${wait_interval}   ${validate}
    Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${wait_timeout}   ${wait_interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=Not all forked tasks state finished with Completed.

Add Unassigned Server Profiles
	[Documentation]	Adds Server Profiles to an appliance from a variable file in without assigning server hardware.
	[Arguments]		${profiles}   ${server_profile_to_bay_map}   ${waitTime}=300m   ${interval}=2s   ${validate}=${True}
	Log   \n\nAdding SERVER PROFILES...  console=${True}
        ${valDict} =    Create Dictionary   status_code=${200}
        ...                                 taskState=Completed
        ${respList} =   Create List
	:FOR	${profile}	IN	@{profiles}
	\       ${profile} =    fusion_api_appliance_setup.Copy Dictionary     ${profile}
        \       ${spaceName} =   Check For Whitespace From String   ${profile['name']}
        \       Run Keyword If   ${spaceName} is ${True}   Fail   msg=Profile name contains whitespace. This is not allowed in CI-FIT naming convention.
        \       ${resp} =   Run Keyword If   '${server_profile_to_bay_map['${profile['name']}']}' == '${null}'   Fusion Api Get Server Hardware
        \       ${shUri} =   Run Keyword If   ${resp} == ${null}   Get Server Hardware URI    ${server_profile_to_bay_map['${profile['name']}']}
        \       ...                    ELSE   Set Variable   ${resp['members'][0]['uri']}
        \       ${serverHW} =    Fusion Api Get Resource    uri=${shUri}
	\       Set To Dictionary    ${profile}   serverHardwareTypeUri=${serverHW['serverHardwareTypeUri']}
	\	${eg} = 	Get from Dictionary	${profile}	enclosureGroupUri
	\	@{words} = 	Split String	${eg}	:
	\	${type} = 	Get From List	${words}	0
	\	${eg} = 	Get From List	${words}	1
	\	${uri} = 	Get Enclosure Group URI	${eg}
        \       ${profile} =   Resolve Profile Template Uri   ${profile}
	\	Set to Dictionary	${profile}	enclosureGroupUri	${uri}
        \       ${profile} =   Resolve Profile Connections   ${profile}
	\	${resp} = 	Fusion Api Create Server Profile		body=${profile}
	\       Request Should Be Successful   ${resp}   expectedStatusCode=${202}
	\       fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${waitTime}   ${interval}   ${validate}

Resolve Profile Connections
    [Documentation]   Update profile connections based on the X-API-Version. This look up the connections and resolve the corresponding uris. Returns updated profile.
    [Arguments]   ${profile}   ${connectionSettingsApi}=${600}
    ${connectionSettings} =   Evaluate   ${profile}.get('connectionSettings', None)
    ${connections} =   Run Keyword If   ${X-API-Version} >= ${connectionSettingsApi} and ${connectionSettings} is not ${null}   Evaluate   ${profile['connectionSettings']}.get("connections",None)
    ...                          ELSE   Evaluate   ${profile}.get("connections",None)
    ${connections} =   Run Keyword If   ${connections} is not ${null}   Lookup Connection Uris	${connections}
    Return From Keyword If   ${connections} is ${null}   ${profile}
    Run Keyword If   ${X-API-Version} >= ${connectionSettingsApi}   Set to Dictionary   ${profile['connectionSettings']}  connections     ${connections}
    ...       ELSE   Set to Dictionary   ${profile}   connections     ${connections}
    [Return]   ${profile}

Resolve Profile Template Uri
    [Documentation]   Query OneView and resolve profile template uri by name.
    [Arguments]   ${profile}
    ${template} =   Evaluate   ${profile}.get("serverProfileTemplateUri",None)
    ${templateUri} =   Run Keyword If   '${template}' != '${null}'   Get Server Profile Template Uri   ${profile['serverProfileTemplateUri']}
    Run Keyword If   '${templateUri}' != '${null}'   Set To Dictionary   ${profile}   serverProfileTemplateUri   ${templateUri}
    [Return]   ${profile}

Remove All Server Profiles In Parallel
	[Documentation]	Querys the appliance for all Server Profiles and then removes them
    ...             NOTE: If ${waitForTask} is false, ${parallel} and ${validate} becomes moot. Just fork the process and exit.
    [Arguments]   ${waitTime}=300m   ${interval}=5s  ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}
	${log_message} =   Run Keyword If   '${parallel}' == '${True}'   Set Variable   \n\nRemoving SERVER PROFILES in parallel (status may not reflect right away)...
	...                ELSE   Set Variable   \n\nRemoving SERVER PROFILES
	log   ${log_message}   console=${True}
	${profiles} = 	Fusion Api Get Server Profiles  param=?sort=name:ascending
    ${valDict} =    Create Dictionary   status_code=${200}
    ...                                 taskState=Completed
    ${respList} =   Create List
    Set Suite Variable   ${forkedErrorFound}   ${False}
	:FOR	${profile}	IN	@{profiles['members']}
	\	${resp} = 	Fusion Api Delete Server Profile		uri=${profile['uri']}
	\       Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \       Continue For Loop If   ${waitForTask} != ${True}
    \       Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
    \       ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=Not all forked tasks state finished with Completed.
		
###############
# Server Profile Templates
###############
Add Server Profile Templates From Variable
    [Documentation]   Adds Server Profile Templates to an appliance from a variable which contains a list of dicts with the entire payload
    [Arguments]   ${profileTemplates}   ${waitTime}=300m   ${interval}=5s   ${connectionSettingsApi}=${600}   ${waitForTask}=${True}  ${parallel}=${False}   ${validate}=${True}
    ${log_message} =   Run Keyword If   '${parallel}' == '${True}'   Set Variable   \n\nAdding SERVER PROFILE TEMPLATES in parallel (status may not reflect right away)...
	...                ELSE   Set Variable   \n\nAdding SERVER PROFILE TEMPLATES
	log   ${log_message}   console=${True}
    ${valDict} =    Create Dictionary   status_code=${200}
    ...                                 taskState=Completed
    ${respList} =   Create List
    Set Suite Variable   ${forkedErrorFound}   ${False}
    :FOR   ${profile}   IN   @{profileTemplates}
    \   ${profile} =   fusion_api_appliance_setup.Copy Dictionary   ${profile}
    \   ${resp} =   Fusion Api Get Server Hardware
    \   ${serverHW} =    Fusion Api Get Resource    uri=${resp['members'][0]['uri']}
    \   Set To Dictionary    ${profile}   serverHardwareTypeUri=${serverHW['serverHardwareTypeUri']}
    \   ${eg} =   Get from Dictionary   ${profile}   enclosureGroupUri
    \   @{words} =   Split String   ${eg}   :
    \   ${type} =   Get From List   ${words}   0
    \   ${eg} =   Get From List   ${words}   1
    \   ${uri} =   Get Enclosure Group URI   ${eg}
    \   Set to Dictionary   ${profile}   enclosureGroupUri   ${uri}
    \   ${profile} =   Resolve Profile Connections   ${profile}   connectionSettingsApi=${connectionSettingsApi}
    \   ${resp} =   Fusion Api Create Server Profile template   body=${profile}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   Append To List   ${respList}   ${resp}
    common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=Not all forked tasks state finished with Completed.

Remove All Server Profile Templates In Parallel
    [Documentation]   Remove all server profiles templates from OneView.
    [Arguments]   ${waitTime}=300m   ${interval}=5s  ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}
    Log   \n\nRemoving SERVER PROFILE Templates...   console=${True}
    ${templates} =   Fusion Api Get Server Profile Templates
    ${valDict} =    Create Dictionary   status_code=${200}
    ...                                 taskState=Completed
    ${respList} =   Create List
    Set Suite Variable   ${forkedErrorFound}   ${False}
    :FOR	${profileT}	IN	@{templates['members']}
    \	${resp} = 	Fusion Api Delete Server Profile Template   uri=${profileT['uri']}
    \       Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \       Continue For Loop If   ${waitForTask} != ${True}
    \       Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
    \       ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=Not all forked tasks state finished with Completed.
		
################
# Server Hardware Helper
################
Power OFF Server Bay
    [Documentation]    Querys the appliance for a server bay number and enclosure then powers it off.
    ...                NOTE: Power Off Server Uri is more efficient than this and highly recommended unless for some reason you'll have to really use this approach.
    ...                      Use-case of this keyword is when you don't have server-hardware uri and want to target power off off the bay number and enclosure name.
    [Arguments]     ${enc}   ${bay}   ${wait_task_timeout}=30m   ${wait_task_interval}=15s   ${powerControl}=MomentaryPress
    Log   Powering off ${enc}, server bay: ${bay}   console=${True}
    ${body} =   Create Dictionary   powerState=Off
    ...              powerControl=${powerControl}
    ${servers} =    Fusion Api Get Server Hardware   param=?filter="position=${bay}"
    :FOR   ${member}   IN   @{servers['members']}
    \   ${resp} =   Fusion Api Get Resource   ${member['locationUri']}
    \   Continue For Loop If   '${resp['name']}' != '${enc}'
    \   ${resp} =    Fusion Api Edit Server Hardware Power State     body=${body}    uri=${member['uri']}
    \   ${statusCode} =   Check Response For Error   ${resp}
    \   ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task}

Power ON Server Bay
    [Documentation]    Querys the appliance for a server bay number and enclosure then powers it on.
    ...                NOTE: Power On Server Uri is more efficient than this and highly recommended unless for some reason you'll have to really use this approach.
    ...                      Use-case of this keyword is when you don't have server-hardware uri and want to target power on off the bay number and enclosure name.
    [Arguments]     ${enc}   ${bay}   ${wait_task_timeout}=45m   ${wait_task_interval}=30s   ${powerControl}=MomentaryPress
    Log   Powering on ${enc}, server bay: ${bay}   console=${True}
    ${body} =   Create Dictionary    powerState=On
    ...                               powerControl=${powerControl}
    ${servers} =   Fusion Api Get Server Hardware   param=?filter="position=${bay}"
    :FOR   ${member}   IN   @{servers['members']}
    \   ${resp} =   Fusion Api Get Resource   ${member['locationUri']}
    \   Continue For Loop If   '${resp['name']}' != '${enc}'
    \   ${resp} =    Fusion Api Edit Server Hardware Power State     body=${body}    uri=${member['uri']}
    \   ${statusCode} =   Check Response For Error   ${resp}
    \   ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    \   ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    \   Check Asynchronous Task Response For Error   ${task}

Power On Servers Assigned In Profile From Variable
    [Documentation]   Power on server blades assigned in profile from data variable.
    [Arguments]   ${server_profiles}
    ${listProfiles} =   Create List
    :FOR   ${p}   IN   @{server_profiles}
    \   ${profiles} =   Fusion Api Get Server Profiles  param=?filter="name='${p['name']}'"
	\   Should Be Equal   ${profiles['total']}   ${1}   msg=Response body total is not as expected.
    \   Append To List   ${listProfiles}   ${profiles['members'][0]}
    :FOR   ${profile}   IN   @{listProfiles}
    \   common.Power On Server Uri   ${profile['serverHardwareUri']}

Power Off Servers Assigned In Profile From Variable
    [Documentation]   Power off server blades assigned in profile from data variable.
    [Arguments]   ${server_profiles}
    ${listProfiles} =   Create List
    :FOR   ${p}   IN   @{server_profiles}
    \   ${profiles} =   Fusion Api Get Server Profiles  param=?filter="name='${p['name']}'"
	\   Should Be Equal   ${profiles['total']}   ${1}   msg=Response body total is not as expected.
    \   Append To List   ${listProfiles}   ${profiles['members'][0]}
    :FOR   ${profile}   IN   @{listProfiles}
    \   common.Power Off Server Uri   ${profile['serverHardwareUri']}    proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}

Power On Server Uri
    [Documentation]   Powers on a server for a given URI
    [Arguments]     ${serverUri}   ${wait_task_timeout}=60m   ${wait_task_interval}=2s   ${powerControl}=MomentaryPress
    Log   Powering on server using ${serverUri}   console=${True}
    ${body} =   Create Dictionary   powerState=On
    ...                             powerControl=${powerControl}
    ${resp} =   Fusion Api Edit Server Hardware Power State   body=${body}   uri=${serverUri}
    ${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task}

Power On Server Hardware In Profile Members
    [Documentation]   Power on a server hardware
    [Arguments]     ${profiles}   ${wait_task_timeout}=60m   ${wait_task_interval}=2s   ${powerControl}=MomentaryPress    ${waitForTask}=${True}   ${parallel}=${True}   ${validate}=${True}   ${throttle}=${Null}
    ${body} =   Create Dictionary   powerState=On
    ...                             powerControl=${powerControl}
	${valDict} =    Create Dictionary   status_code=${200}
        ...                                 taskState=Completed
	${respList} =   Create List
	Set Suite Variable   ${forkedErrorFound}   ${False}
	:FOR   ${server}  IN   @{profiles}
    \    ${resp} =   Fusion Api Edit Server Hardware Power State   body=${body}   uri=${server['serverHardwareUri']}
	\    Continue For Loop If   ${waitForTask} != ${True}
	\    Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
	\   ...       ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${wait_task_timeout}   ${wait_task_interval}   ${validate}
	\    Continue For Loop If   '${throttle}' == '${Null}'
    \    Continue For Loop If   ${parallel} != ${True}
    \    ${respLength} =   Get Length   ${respList}
    \    Continue For Loop If   ${respLength} != ${throttle}
	\    ${respList} =   common.Wait For Forked Tasks   ${respList}   ${valDict}   timeout=${wait_task_timeout}   interval=${wait_task_interval}   ${validate}
	Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${wait_task_timeout}   ${wait_task_interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=Not all forked tasks state finished with Completed

Power On All Servers In Parallel
    [Documentation]    Querys the appliance for all servers and then powers them on in parallel.
    [Arguments]   ${waitTime}=300m   ${interval}=5s   ${powerControl}=MomentaryPress      ${onlyProfileApplied}=${False}
    Log   \n\nPowering On SERVERS in parallel (status may not reflect right away)...   console=${True}
    ${body} =   Create Dictionary   powerState=On
    ...                             powerControl=${powerControl}
    ${valDict} =   Create Dictionary   status_code=${200}
    ...                                taskState=Completed
    ${respList} =   Create List
    ${servers} =   Fusion Api Get Server Hardware
    Set Suite Variable   ${forkedErrorFound}   ${False}
    :FOR   ${server}   IN   @{servers['members']}
    \   Continue For Loop If    '${server['powerState']}'!='Off'
    \   Continue For Loop If   ${onlyProfileApplied} is ${True} and '${server['state']}' != 'ProfileApplied'
    \   ${resp} =    Fusion Api Edit Server Hardware Power State        body=${body}    uri=${server['uri']}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   Append To List   ${respList}   ${resp}
    common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=One or more forked tasks has error.

Server Power Reached State
    [Documentation]   Check that server power reached a certain state specified in the argument.
    [Arguments]   ${serverUri}   ${powerState}
    ${resp} =   Fusion Api Get Resource     ${serverUri}
    Log To Console   \t ${serverUri}: ${resp['powerState']}   console=${True}
    Should Match Regexp   ${resp['powerState']}   ${powerState}

All Servers Power State Should Reach Off
    [Documentation]   Query OneView server hardware powerState and fail if one did not transition to powerState Off.
    [Arguments]   ${serverUris}
    :FOR   ${serverUri}   IN   @{serverUris}
    \   ${resp} =   Fusion Api Get Server Hardware   uri=${serverUri}
    \   Log To Console   \nChecking ${resp['name']} powerState Off...   no_newline=${True}
    \   Run Keyword If   '${resp['powerState']}' == 'Off'   Log To Console   [Off]
    \   ...       ELSE   Log To Console   [${resp['powerState']}]
    \   Run Keyword If   '${resp['powerState']}' == 'Off'   Remove Values From List   ${serverUris}   ${serverUri}
    Should Be Empty   ${serverUris}   msg=Not all servers transitioned to powerState Off.

Wait Until Server Power State Reached Off
    [Documentation]   Wait until server powerState reached Off.
    [Arguments]   ${serverUri}   ${timeout}=30m  ${interval}=5s
    Wait Until Keyword Succeeds   ${timeout}   ${interval}   Server Power Reached State   ${serverUri}    Off

Power Off Server Via Ssh
    [Documentation]   Powers off a single server via SSH using the specified command and monitor the powerState transition via the resource and name.
    [Arguments]   ${ipAddr}   ${profileName}   ${poweroffCmd}=poweroff
    Log To Console   \nPowering off ${ipAddr}...
    ${Id} =   Open Connection   ${ipAddr}
    ${Output} =   Login   ${SERVER_USERNAME}   ${SERVER_PASSWORD}
    ${stdout}   ${stderr}   ${rc} =   Execute Command   ${poweroffCmd}   return_stderr=True   return_rc=True
    Close SSH Connection
    # Monitor powerState transition
    ${resp} =   Fusion Api Get Server Profiles  param=?filter="name='${profileName}'"
    Length Should Be   ${resp['members']}   1   msg=Profile name '${profileName}' query in OneView returned unexpected members length.
    Wait Until Server Power State Reached Off    ${resp['members'][0]['serverHardwareUri']}

Power Off Server Via Ssh Without Waiting
    [Documentation]   Powers off a single server via SSH using the specified command without monitoring the powerState transition.
    [Arguments]   ${ipAddr}   ${profileName}   ${poweroffCmd}=poweroff
    Log To Console   \nPowering off ${ipAddr}...
    ${Id} =   Open Connection   ${ipAddr}
    ${Output} =   Login   ${SERVER_USERNAME}   ${SERVER_PASSWORD}
    ${stdout}   ${stderr}   ${rc} =   Execute Command   ${poweroffCmd}   return_stderr=True   return_rc=True
    Close SSH Connection

Get IP And Power Off Server Via Ssh As Possible
    [Documentation]   Get pingable IP from HA File and power off server via SSH.
    ...               Use ssh if server profile is assigned, otherwise, use api (MomentaryPress/PressAndHold).
    [Arguments]   ${blade}   ${poweroffCmd}=poweroff
    ${resp} =   Run Keyword If   '${blade['state']}' == 'ProfileApplied'   Fusion Api Get Server Profiles   uri=${blade['serverProfileUri']}
    ...                      ELSE   Create Dictionary
    Log To Console   \nSearching for reachable IP Address from HA file...
    ${pingable_ip} =   Run Keyword If   ${resp} != &{EMPTY}   robustness-helper.get_server_reachable_ip   ${HA_FILE}   ${resp['name']}
    Run Keyword If   '${pingable_ip}' != 'None'   Power Off Server Via Ssh   ${pingable_ip}   ${resp['name']}
    ...       ELSE   common.Power Off Server Uri   ${blade['uri']}   proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}

Power Off All Servers Via Ssh
    [Documentation]   Powers off all servers in HA_FILE using specified command via SSH.
    [Arguments]   ${poweroffCmd}=poweroff
    ${reachable_ips} =   robustness-helper.get_server_reachable_ip   ${HA_FILE}
    :FOR   ${k}   IN   @{reachable_ips.keys()}
    \   Power Off Server Via Ssh   ${reachable_ips['${k}']}   ${k}   ${poweroffCmd}

Power Off All Servers Via Ssh In Parallel
    [Documentation]   Powers off all servers in HA_FILE using specified command via SSH and proceed with api.
    [Arguments]   ${poweroffCmd}=poweroff   ${timeout}=180m  ${interval}=10s   ${server_off_sleep}=5m
    ${reachable_ips} =   robustness-helper.get_server_reachable_ip   ${HA_FILE}
    :FOR   ${k}   IN   @{reachable_ips.keys()}
    \   Power Off Server Via Ssh Without Waiting   ${reachable_ips['${k}']}   ${k}   ${poweroffCmd}
	Sleep And Log Reason To Console   ${server_off_sleep}   reason=Sleeping ${server_off_sleep} after server power off.
    ${resp} =   Fusion Api Get Server Hardware
    ${serverUris} =   Create List
    :FOR   ${s}   IN   @{resp['members']}
    \   Log To Console   \nChecking ${s['name']} powerState Off...   no_newline=${True}
    \   Run Keyword If   '${s['powerState']}' == 'Off'   Log To Console   [Off]
    \   ...       ELSE   Run Keywords    Log To Console   [${s['powerState']}]   AND   Append To List   ${serverUris}   ${s['uri']}   AND   common.Power Off Server Uri   ${s['uri']}    proceedPressAndHold=${PROCEED_WITH_PRESS_AND_HOLD}
    Wait Until Keyword Succeeds   ${timeout}   ${interval}   All Servers Power State Should Reach Off   ${serverUris}

Power Off Server Uri
    [Documentation]   Powers off a server for a given URI
    ...               proceedPressAndHold accepts errorCode that will trigger PressAndHold powerControl if found(ie: SERVER_MOMENTARY_PRESS_OFF_TIMEOUT).
    [Arguments]     ${serverUri}   ${wait_task_timeout}=60m   ${wait_task_interval}=2s   ${powerControl}=MomentaryPress   ${proceedPressAndHold}=${Null}
    Log   Powering off server using ${serverUri} using ${powerControl}   console=${True}
    ${body} =   Create Dictionary   powerState=Off
    ...                             powerControl=${powerControl}
    ${resp} =   Fusion Api Edit Server Hardware Power State   body=${body}   uri=${serverUri}
    ${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    ${retval} =   Check Asynchronous Task Response For Error   ${task}   processErrorCode=${proceedPressAndHold}
    Run Keyword If   '${retval}' != '${Null}'   common.Power Off Server Uri   ${serverUri}   wait_task_timeout=${wait_task_timeout}   wait_task_interval=${wait_task_interval}   powerControl=PressAndHold

Power Off All Servers Serially
    [Documentation]    Query the appliance for all servers and then powers them off based on powerControl argument.
    ...               proceedPressAndHold accepts errorCode that will trigger PressAndHold powerControl if found(ie: SERVER_MOMENTARY_PRESS_OFF_TIMEOUT).
    [Arguments]   ${powerControl}=MomentaryPress   ${wait_task_timeout}=30m   ${wait_task_interval}=5s   ${proceedPressAndHold}=${Null}
    Log to console   \nPowering off all servers using ${powerControl}...
    ${body} =   Create Dictionary   powerState=Off
    ...                             powerControl=${powerControl}
    ${servers} =   Fusion Api Get Server Hardware
    :FOR   ${server}   IN   @{servers['members']}
    \   Continue For Loop If   '${server['powerState']}' != 'On'
    \   ${resp} =   Fusion Api Edit Server Hardware Power State   body=${body}   uri=${server['uri']}
    \   ${statusCode} =   Check Response For Error   ${resp}
    \   ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    \   ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    \   ${retval} =   Check Asynchronous Task Response For Error   ${task}   processErrorCode=${proceedPressAndHold}
    \   Run Keyword If   '${retval}' != '${Null}'   common.Power Off Server Uri   ${server['uri']}   wait_task_timeout=${wait_task_timeout}   wait_task_interval=${wait_task_interval}   powerControl=PressAndHold

Power Off All Servers In Parallel
    [Documentation]    Querys the appliance for all servers and then powers them off in parallel.
    ...               proceedPressAndHold accepts errorCode that will trigger PressAndHold powerControl if found(ie: SERVER_MOMENTARY_PRESS_OFF_TIMEOUT).
    [Arguments]   ${waitTime}=300m   ${interval}=5s   ${powerControl}=MomentaryPress   ${proceedPressAndHold}=${Null}   ${onlyProfileApplied}=${False}
    Log To Console   \n\nPowering off all servers using ${powerControl}...
    ${body} =   Create Dictionary   powerState=Off
    ...                             powerControl=${powerControl}
    ${valDict} =   Create Dictionary   status_code=${200}
    ...                                taskState=Completed
    ${respList} =   Create List
    ${servers} =   Fusion Api Get Server Hardware
    Set Suite Variable   ${forkedErrorFound}   ${False}
    :FOR   ${server}   IN   @{servers['members']}
    \   Continue For Loop If    '${server['powerState']}'!='On'
    \   Continue For Loop If   ${onlyProfileApplied} is ${True} and '${server['state']}' != 'ProfileApplied'
    \   ${resp} =    Fusion Api Edit Server Hardware Power State    body=${body}    uri=${server['uri']}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   Append To List   ${respList}   ${resp}
    common.Wait For Forked Tasks   ${respList}   ${valDict}   ${waitTime}   ${interval}   processErrorCode=${proceedPressAndHold}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=Not all forked tasks state finished with Completed.

Get iLO IP Addresses
    [Documentation]   Get all the servers iLO IP Addresses.
    Log To Console   Getting all the servers iLO IP addresses...
    ${resp} =   Fusion Api Get Server Hardware
    ${iLOHostInfo} =   Create Dictionary
    :FOR   ${m}   IN   @{resp['members']}
    \   ${name} =   Set Variable   ${m['name']}
    \   ${iLOIpAddresses} =   Set Variable   ${m['mpHostInfo']['mpIpAddresses']}
    \   ${iLOIpAddresses} =   Build IP Address List   ${iLOIpAddresses}
    \   ${mpModel} =    Evaluate    '${m['mpModel']}'.lower()
    \   ${mpHostInfo} =   Create Dictionary   mpIpAddresses=${iLOIpAddresses}   mpHostName=${m['mpHostInfo']['mpHostName']}   mpModel=${mpModel}
    \   Set To Dictionary   ${iLOHostInfo}    ${name}=${mpHostInfo}
    [Return]   ${iLOHostInfo}

Build IP Address List
    [Documentation]   Parse mpIpAddresses and return list of IP addresses based on this order: DHCP, Lookup, LinkLocal
    [Arguments]   ${mpIpAddresses}
    ${dhcpIp} =   Get IP Address By Type   DHCP   ${mpIpAddresses}
    ${lookupIp} =   Get IP Address By Type   Lookup   ${mpIpAddresses}
    ${linkLocalIp} =   Get IP Address By Type   LinkLocal   ${mpIpAddresses}
    ${iLOIpAddresses} =   Create List   ${dhcpIp}   ${lookupIp}   ${linkLocalIp}
    [Return]   ${iLOIpAddresses}

Get IP Address By Type
    [Documentation]   Get IP Address by type from mpIpAddresses.
    [Arguments]   ${type}   ${mpIpAddresses}
    ${ip} =   Set Variable   ${null}
    :FOR   ${m}   IN   @{mpIpAddresses}
    \   Continue For Loop If   '${m['type']}' != '${type}'
    \   ${ip} =   Run Keyword If   '${ip}' == '${null}'   Set Variable   ${m['address']}
    \   ...                 ELSE   Fail   msg=There are more than one ${type} type found.
    [Return]   ${ip}

Verify Device Bays
    [Documentation]   Verify device bays
    [Arguments]   ${Devices}   ${operation}
    :FOR   ${d}   IN   @{Devices}
	\   ${uri} =   Get From Dictionary   ${d}   deviceUri
	\   ${bay} =   Get From Dictionary   ${d}   bayNumber
    \   ${present} =   Get From Dictionary   ${d}   devicePresence
    \   Continue For Loop If   '${present}' == 'Absent'
    \   Run Keyword If   '${BAYS}' == '${null}' and '${operation}' == 'console'   Launch iLO Remote Console   ${uri}
    \   Run Keyword If   '${BAYS}' == '${null}' and '${operation}' == 'web'   Launch iLO Webpage   ${uri}
    \   Run Keyword If   '${BAYS}' == '${null}' and '${operation}' == 'powerControl'   Blade power control   ${uri}
    \   Run Keyword If   '${BAYS}' != '${null}'   Traverse Device Bay   ${d}   ${uri}   ${BAYS}   ${operation}

Traverse Device Bay
    [Documentation]   Traverse Device Bay
    [Arguments]   ${d}   ${uri}   ${BAYS}   ${operation}
    ${BAYS} =   Run Keyword If   "${BAYS}" != "${null}"   Split String   ${BAYS}   ${SPACE}
    :FOR   ${bay}   IN   @{BAYS}
	\   ${pos} =   Get From Dictionary   ${d}   bayNumber
	\   Run Keyword If   '${bay}' == '${pos}' and '${operation}' == 'console'   Launch iLO Remote Console   ${uri}
	\   Run Keyword If   '${bay}' == '${pos}' and '${operation}' == 'web'   Launch iLO Webpage   ${uri}
    \   Run Keyword If   '${bay}' == '${pos}' and '${operation}' == 'powerControl'   Blade power control   ${uri}

Launch iLO Remote Console
    [Documentation]   Launch iLO Remote Console
    [Arguments]   ${uri}
	${console_url} =   fusion api get server hardware remote console url   ${uri}
	Launch browser   ${IEPATH}   ${console_url['remoteConsoleUrl']}

Launch iLO Webpage
    [Documentation]   Launch iLO webpage
    [Arguments]   ${uri}
    ${console_url} =   fusion_api_get_server_hardware_ilo_sso_url   ${uri}
	Launch browser   ${IEPATH}   ${console_url['iloSsoUrl']}

################
# Appliance Reboot: specific to appliance reboot keywords
################
Run Robustness Appliance Reboot
    [Documentation]   Run robustness appliance reboot based on a given number of cycles.
    [Arguments]     ${cycles}   ${wait_task_timeout}=45m   ${wait_task_interval}=2s   ${sleep}=45m   ${hafnium_icm_model}=${HAFNIUM_MODEL}   ${iface}=eth0
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    ${REMOTE_RUN_CHECKS} =   Get Variable Value   ${REMOTE_RUN_CHECKS}   @{EMPTY}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    :FOR	${x}	IN RANGE	1	${cycles}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n Cycle: ${x} of ${cycles}   console=${True}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   ${resp} =   Fusion Api Appliance Shutdown  mode=REBOOT
    \   ${taskResp} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    \   Sleep And Log Reason To Console   ${sleep}   reason=Sleeping ${sleep} after an appliance reboot.
    \   Check Common Resource Attributes
    \   Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    \   Check For MeatGrinder Error
    \   Check For Multipath   hafnium_icm_model=${hafnium_icm_model}   iface=${iface}
    \   Check For Server In Read Only Filesystem
    \   common.Run Sequential Ping
    \   Fping Should Have No Loss
    \   Check For ISS Crash   iface=${iface}
    \   All Etherchannel Summary Ports Should Be Linked   iface=${iface}
    \   Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}

################
# MultiActive Detection and Recovery: specific to MAD and recover test keywords
################
Run Robustness MultiActive Detection And Recovery
    [Documentation]   Run MAD and recover robustness test.
    [Arguments]   ${cycles}   ${targetEnc}   ${targetICM}   ${hafnium_icm_model}=${HAFNIUM_MODEL}   ${iface}=eth0
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    :FOR	${x}	IN RANGE	1	${cycles}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n Cycle: ${x} of ${cycles}   console=${True}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   Log To Console   Negative test, attempting to toggle stacking ports using REST API...   no_newline=${True}
    \   Attempt Toggling Stacking Ports Using REST API
    \   Break DUS And Establish Again   ${targetEnc}   ${targetICM}   ${ICM_NAMES}   wait_configured_timeout=${STACKING_LINK_WAIT_TIMEOUT}   wait_configured_interval=${STACKING_LINK_WAIT_INTERVAL}   iface=${iface}
    \   Check Common Resource Attributes
    \   Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    \   Check For MeatGrinder Error
    \   Check For Multipath   hafnium_icm_model=${hafnium_icm_model}   iface=${iface}
    \   Check For Server In Read Only Filesystem
    \   common.Run Sequential Ping
    \   Fping Should Have No Loss
    \   Check For ISS Crash   iface=${iface}
    \   All Etherchannel Summary Ports Should Be Linked   iface=${iface}
    \   Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}
    \   Set To Dictionary   ${DISABLE_FC_UPLINK_SIDEA}   associatedUplinkSetUri=${FC_UPLINK_SET_SIDEA}
    \   Set To Dictionary    ${ENABLE_FC_UPLINK_SIDEA}   associatedUplinkSetUri=${FC_UPLINK_SET_SIDEA}

################
# General Helper
################
Check Network In Profiles
    [Documentation]   Verify that a network is being used by profile(s).
    [Arguments]   ${nsUri}   ${uriAttr}
    ${profiles} =   Fusion Api Get Resource   /rest/server-profiles
    :FOR   ${p}   IN   @{profiles['members']}
    \   ${used} =   Check Network Uri In Connections   ${nsUri}   ${p['connectionSettings']['connections']}   ${uriAttr}
    \   Return From Keyword If   ${used} is ${True}   ${True}
    [Return]   ${False}

Check Network Uri In Connections
    [Documentation]  Verify that network uri is in profile connections.
    [Arguments]   ${nsUri}   ${connections}   ${uriAttr}
    :FOR   ${c}   IN   @{connections}
    \   Return From Keyword If   '${c['${uriAttr}']}' == '${nsUri}'   ${True}
    [Return]   ${False}
	
Detect Enclosure Type And Set Env
    [Documentation]   Get enclosure type and set the environment.
    Log   \n Detecting enclosure type...   console=${True}
    ${encType} =    Get Enclosure Type
    Log   Enclosure Type: ${encType}   console=${True}
    Run Keyword If    '${encType}' == 'C7000'    Set Suite Variable   ${tbirdEnv}   ${False}
    ...    ELSE IF    '${encType}' == 'SY12000'    Set Suite Variable   ${tbirdEnv}   ${True}
    ...    ELSE   Fail   msg=Unable to determine the enclosure type ${encType}.

Check For One Time Pass
    [Documentation]   Check that a bay number is listed in the ONE_TIME_PASS argument.
    [Arguments]   ${b}
    ${b} =   Convert To String   ${b}
    ${status} =   Run Keyword If   "${ONE_TIME_PASS}" != "${null}"   Run Keyword And Return Status   List Should Contain Value   ${ONE_TIME_PASS}   ${b}
    ...                     ELSE   Set Variable   ${False}
    Remove Values From List   ${ONE_TIME_PASS}   ${b}
    ${ONE_TIME_PASS} =   Set Test Variable   ${ONE_TIME_PASS}
    [Return]   ${status}

Create Bay Number To Uri Map
    [Documentation]   Mapping bay number to uri. Returns dictionary of bayAttr: uriAttr format.
    [Arguments]   ${enc_data}   ${baysDataSource}   ${uriAttr}  ${bayAttr}=bayNumber
    ${uriDict} =   Create Dictionary
    ${baysData} =   Get From Dictionary   ${enc_data}   ${baysDataSource}
    ${l} =   Get Length   ${baysData}
    :FOR   ${x}   IN RANGE   0   ${l}
    \   Run Keyword If   '${baysData[${x}]['${uriAttr}']}' != "${null}"   Set To Dictionary   ${uriDict}   ${baysData[${x}]['${bayAttr}']}   ${baysData[${x}]['${uriAttr}']}

    [Return]   ${uriDict}

Resource Uri Should Have Expected Status Code
    [Documentation]    Query OneView based on the given URI and test that status code is of the expected value.
    [Arguments]	    ${uri}  ${status_code}=404
    Set Log Level	TRACE
    ${resp} =   fusion api get resource     ${uri}
    Log   \t ${uri}: ${resp['status_code']}   console=${True}
    should be equal as integers  	${resp['status_code']}    ${status_code}
    [Return]	${resp}

Get An Element From Dictionary
    [Documentation]   Get an element from dictionary.
    [Arguments]     ${dict}   ${element}
    ${return} =     Get From Dictionary     ${dict}   ${element}
    [Return]    ${return}

Filter Attribute From Response Body
    [Documentation]   Filter out attribute from the resource query response body.
    ...               Example: ${icmData} =   Filter Attribute From Response Body   ${resp}   name   ${icmName}
    [Arguments]    ${resp}   ${filterKey}   ${filterValue}
    :FOR   ${member}   IN   @{resp['members']}
    \   Return From Keyword If  '${member['${filterKey}']}' == '${filterValue}'   ${member}
    [Return]   ${null}

Response Should Contain Error Code
    [Documentation]   Check that response body contain the expected error code.
    [Arguments]   ${response}   ${expectedErrorCode}
    Run Keyword If   '${response['errorCode']}' != '${expectedErrorCode}'   Fail   msg=Response body did not contain the expected error code: ${expectedErrorCode}

Create New Network And Uplink Set
    [Documentation]   Create new network and uplink set.
    [Arguments]   ${networks}   ${uplink_sets}   ${icm_names}   ${message}=Creating new networks and uplink sets from data variable file.   ${wait_timeout}=15m   ${wait_interval}=15s
    Log   ${message}   console=${True}
    Run Keyword If   'fc-network' in '${networks[0]['type']}'   common.Add FC Networks from variable   ${networks}
    ...    ELSE IF   'fcoe-network' in '${networks[0]['type']}'   common.Add FCoE Networks from variable   ${networks}
    ...    ELSE IF   'ethernet-network' in '${networks[0]['type']}'   common.Add Ethernet Networks from variable   ${networks}
    ...    ELSE   Fail   msg=Network type you are trying to create is not known: ${networks['type']}.
    Create New Uplink Set   ${uplink_sets}   ${icm_names}   wait_timeout=${wait_timeout}   wait_interval=${wait_interval}

Parse Task Uri From Content
    [Documentation]   Parse _content from response body and return task uri.
    [Arguments]   ${resp}
    ${content} =   Get From Dictionary   ${resp}   _content
    ${content} =   Evaluate   json.loads('''${content}''')   json
    ${task_uri} =   Get From Dictionary   ${content}   taskUri
    [Return]   ${task_uri}

Check Data
    [Documentation]   Check that LHS dictionary data is matching the RHS dictionary data. LHS could be a subset of RHS. This is similar to select data compare.
    [Arguments]    ${lhs}   ${rhs}
    ${mismatches} =   Create Dictionary
    :FOR   ${k}   IN   @{lhs.keys()}
    \   ${retval} =   Run Keyword If   '${lhs['${k}']}' == '${rhs['${k}']}'   Log   Checking ${k}...[OK]   console=${True}
    \   ...                     ELSE   Set Variable   ${False}
    \   Run Keyword If   ${retval} is ${False}   Set To Dictionary   ${mismatches}   ${k}='${k}' expected data '${lhs['${k}']}' is NOT equal to resource data '${rhs['${k}']}'.
    Run Keyword If   ${mismatches} != &{EMPTY}   Log All Data Mismatches   ${mismatches}
    Return From Keyword If   ${mismatches} != &{EMPTY}   ${False}
    [Return]   ${True}

Log All Data Mismatches
    [Documentation]   Log all data mismatches.
    [Arguments]   ${mismatches}
    :FOR   ${k}   IN   @{mismatches.keys()}
    \   Log   Checking ${k}...[Failed]   console=${True}
    \   Log   Failure: ${mismatches['${k}']}   console=${True}

Re-import Data Variable Files
    [Documentation]   Re-import data variable files.
    [Arguments]   ${data_variable_files}
    :FOR   ${f}   IN   @{data_variable_files}
    \   Import Variables   ${f}
    Log   ${INTERCONNECTS}

Sleep And Log Reason To Console
    [Documentation]   Sleep for a given time and log reason to both console and logfile. Sleep has a reason option but it won't log to console (only in logfile) so we are wrapping them here.
    [Arguments]   ${sleep}   ${reason}=${null}
    ${dateTime} =   Get Current Date
    Log To Console   \n[${dateTime}] ${reason}
    Sleep   ${sleep}   reason=${reason}

Get Attributes From Response Body Member
    [Documentation]   Get attributes from response body member.
    ...               Returns dictionary of attributes.
    [Arguments]   ${respMember}   ${attrList}
    ${attr} =   Create Dictionary
    :FOR   ${a}   IN   @{attrList}
    \   Set To Dictionary   ${attr}   ${a}=${respMember['${a}']}
    [Return]   ${attr}

Get Value From User On Console
    [Documentation]   Prompt user with something and return the STDIN string.
    [Arguments]    ${prompt}
    Evaluate    sys.__stdout__.write("""\n${prompt}""")    sys
    ${input} =    Evaluate    unicode(raw_input()).lower()
    [Return]    ${input}

Log Groups With Port Down To Console
    [Documentation]   Print to console all the groups with port down.
    [Arguments]   ${list}
    Log To Console   Group${SPACE * 2}Port-channel${SPACE * 11}Protocol${SPACE * 3}Ports
    Log To Console   -------------------------------------------------------------------------
    :FOR   ${l}   IN   @{list}
    \   Log To Console   ${l}
    Log To Console   Port(s) with down/unlinked state found! Check the above list for details...

Wait For Forked Tasks
    [Documentation]    Wait for forked tasks (off the response body list of dictionary) to reach end state
    [Arguments]    ${respList}    ${valDict}    ${timeout}=60m    ${interval}=5s    ${validate}=${True}   ${processErrorCode}=${Null}   ${throttle}=${Null}
    ${respList} =   Wait Until Keyword Succeeds    ${timeout}    ${interval}    common.Forked Tasks Reached Endstate     ${respList}   ${valDict}   ${validate}   proceedPressAndHold=${processErrorCode}   throttle=${throttle}
    [Return]   ${respList}

Forked Tasks Reached Endstate
    [Documentation]    Look up through all the forked tasks to see if they reached end state
    [Arguments]    ${respList}    ${valDict}    ${validate}=${True}   ${proceedPressAndHold}=${Null}   ${throttle}=${Null}
    ${match} =    Set Variable    ${0}
    ${l} = 	  Get Length    ${respList}
    ${taskStateList} =    Create List    Warning  Unknown  Terminated  Killed  Error  Completed
    :FOR    ${x}    IN RANGE   0    ${l}
    \    ${location} =    Get Variable Value    ${respList[${x}]['headers']['location']}
    \    ${task_uri} =    Run Keyword If    '${location}' is 'None'    Get From Dictionary    ${respList[${x}]}    uri
    \    ...     ELSE    Get Variable Value    ${location}
    \    Should Not Be Empty    ${task_uri}    msg=No task uri could be retreived from response.
    \    ${task} =    Fusion Api Get Task    uri=${task_uri}
    \    ${match} =    Run Keyword If    ${validate} == ${True}    Count Values In List   ${taskStateList}    ${task['taskState']}
    \    Run Keyword If    ${match} > ${0}    Remove From List     ${respList}    ${x}
    \    Run Keyword If    ${validate} == ${True}    Log To Console   \t Task: [${task['category']}:${task['name']}] is: ${task['taskState']} for resource: ${task['associatedResource']['resourceName']} ${task['associatedResource']['resourceUri']}
    \   ${retstatus}   ${retval} =   Run Keyword And Ignore Error   Check Asynchronous Task Response For Error   ${task}   processErrorCode=${proceedPressAndHold}
    \   Run Keyword If   '${retval}' != '${Null}' and '${retstatus}' == 'PASS'   common.Power Off Server Uri   ${task['associatedResource']['resourceUri']}   powerControl=PressAndHold
    \   ...    ELSE IF   ${task['taskErrors']} != @{EMPTY}   Set Suite Variable   ${forkedErrorFound}   ${True}
    # When throttle is on, return the respList so we can push one when we pop one
    # If there is a match and we are not throttling, continue with loop. Otherwise, fail the keyword so it will re-attempt until keyword succeeds
    \   Run Keyword If   ${match} > ${0} and '${throttle}' != '${Null}'   Return From Keyword    ${respList}
    \   ...    ELSE IF   ${match} == ${0}    FAIL   msg=Forked task is still in progress. Polling for task state...

Parse Bonding Data From Profile
    [Documentation]   Parse bonding data from server profile.
    [Arguments]   ${profile}   ${offline_interconnect}   ${profile_connections}   ${icm_to_li}   ${ignoreAttributes}=&{EMPTY}
    # Identying offline_interconnect LI
    ${logicalInterconnectUri} =   Get Logical Interconnect Uri By ICM Uri   ${offline_interconnect}
    ${bonding_data} =   Create Dictionary
    :FOR   ${connection}   IN   @{profile_connections}
    \   ${status} =   Run Keyword If   '${offline_interconnect}' == '${Null}'   Set Variable   bothUp
    \   ...                  ELSE IF   '${connection['interconnectUri']}' == '${offline_interconnect}'   Set Variable   down
    \   ...                     ELSE   Set Variable   up
    # Check that ${connection['interconnectUri']} belongs to the same LI as offline_interconnect
    \   ${same_li} =   Run Keyword If   '${icm_to_li['${connection['interconnectUri']}']}' == '${logicalInterconnectUri}'   Set Variable   ${True}
    \   ...                      ELSE   Set Variable   ${False}
    # Skip even physical port
    \   ${tmpPortId} =   Split String   ${connection['portId']}   -
    \   ${l} =   Get Length   ${tmpPortId}
    \   Continue For Loop If   ${l} <= 1
    \   ${split_portId} =   Split Port Id   ${connection['portId']}
    \   ${eval} =   Evaluate   int(${split_portId['phyPort']}) % 2
    \   Continue For Loop If   ${eval} == 0
    \   ${bond}   ${data} =   Get Bond Interface Data   ${profile}   ${connection['mac']}   ${connection['maximumMbps']}   ${status}   ${HA_FILE}   ${same_li}
    \   Continue For Loop If   ${data} == &{EMPTY}
    \   Run Keyword If   ${ignoreAttributes} == &{EMPTY}   Run Keywords   Set To Dictionary   ${data}   ignoredAttributes=[]   AND   Set To Dictionary   ${bonding_data}   ${bond}=${data}   AND   Continue For Loop
    \   ${all_profiles_ignored_attr} =   Evaluate   $ignoreAttributes.get('All', {})
    # {} meaning there's no All at profiles level
    # get ignored attributes for this profile name
    \   ${profile_ignored_attr} =   Run Keyword If   ${all_profiles_ignored_attr} == &{EMPTY}   Evaluate   $ignoreAttributes.get($profile, {})
    \   ...                                   ELSE   Set Variable   ${all_profiles_ignored_attr}
    \   Run Keyword If   ${profile_ignored_attr} == &{EMPTY}   Run Keywords   Set To Dictionary   ${data}   ignoredAttributes=[]   AND   Set To Dictionary   ${bonding_data}   ${bond}=${data}   AND   Continue For Loop
    # evaluate to see if we are ignoring attr for all bonds
    \   ${all_bonds_ignored_attr} =   Evaluate   $profile_ignored_attr.get('All', [])
    \   ${bond_ignored_attr} =   Run Keyword If   ${all_bonds_ignored_attr} == @{EMPTY}   Evaluate   $profile_ignored_attr.get($bond, [])
    \   ...                                ELSE   Set Variable   ${all_bonds_ignored_attr}
    \   Run Keyword If   ${bond_ignored_attr} == @{EMPTY}   Run Keywords   Set To Dictionary   ${data}   ignoredAttributes=[]   AND   Set To Dictionary   ${bonding_data}   ${bond}=${data}   AND   Continue For Loop
    \   Set To Dictionary   ${data}   ignoredAttributes=${bond_ignored_attr}
    \   Set To Dictionary   ${bonding_data}   ${bond}=${data}
    [Return]   ${bonding_data}

Update Link Failure Count Cache
    [Documentation]   Update bonding interfaces link failure count cache.
    [Arguments]   ${userName}=root   ${password}=rootpwd
    Return From Keyword If   ${DISABLE_BONDING_MULTI_TEST} is ${True}
    ${reachable_ips} =   robustness-helper.get_server_reachable_ip   ${HA_FILE}
    ${reachable_ips_items} =   Get Dictionary Items   ${reachable_ips}
    ${NO_CHECK_BONDS} =   Get Variable Value   ${NO_CHECK_BONDS}   @{EMPTY}
    :FOR   ${profile}  ${ip}   IN   @{reachable_ips_items}
    \   Run Keyword If   '${profile}' in @{NO_CHECK_BONDS}   Log   Profile \"${profile}\" is listed in NO_CHECK_BONDS, skipping!   WARN   console=${True}
    \   Continue For Loop If   '${profile}' in @{NO_CHECK_BONDS}
    \   Log To Console   Updating server with profile ${profile}...
    \   ${rc}   ${o} =   Execute Command And Check For Error   ${ip}   ${userName}   ${password}   ${CHECK_BONDS_SCRIPT} --cache-link-failure-count ${SERVER_HAFILE}   verbose=${True}   fail_fast=${True}

Update Link Failure Count Cache By Offline Interconnect
    [Documentation]   Update bonding interfaces link failure count cache based on offline interconnect uri.
    [Arguments]   ${offline_interconnect}   ${profile_bonding_dir}=/root/tools/scripts/profiles_bonding   ${userName}=root   ${password}=rootpwd
    Bonding Interfaces Should Be In Expected States   ${offline_interconnect}   profile_bonding_dir=${profile_bonding_dir}   userName=${userName}   password=${password}   update_link_failure_count=${True}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}

Bonding Interfaces Should Be In Expected States
    [Documentation]   Check that all bonding interfaces are in expected states.
    [Arguments]   ${offline_interconnect}   ${profile_bonding_dir}=/root/tools/scripts/profiles_bonding   ${userName}=root   ${password}=rootpwd   ${update_link_failure_count}=${False}   ${ignoreAttributes}=&{EMPTY}
    Run Keyword If   ${DISABLE_BONDING_MULTI_TEST} is ${True}   Log   Bonding interface multi test has been disabled! Please set DISABLE_BONDING_MULTI_TEST to False.   WARN
    Return From Keyword If   ${DISABLE_BONDING_MULTI_TEST} is ${True}
    ${NO_CHECK_BONDS} =   Get Variable Value   ${NO_CHECK_BONDS}   @{EMPTY}
    ${retStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.Directory Should Exist   ${profile_bonding_dir}
    Run Keyword If   "${retStatus}" == "FAIL"   OperatingSystem.Create Directory   ${profile_bonding_dir}
    ${resp} =   Fusion Api Get Server Profiles
    Run Keyword If   ${resp['total']} < 1   Fail    msg=\nUnable to retrieve server profiles!
    ${profile_bonding_data} =   Create Dictionary
    ${icm_to_li} =   Create Interconnects To LI Mapping
    ${failed_outputs} =   Create Dictionary
    :FOR   ${profile}   IN   @{resp['members']}
    \   Run Keyword If   '${profile['name']}' in @{NO_CHECK_BONDS}   Log   Profile \"${profile['name']}\" is listed in NO_CHECK_BONDS, skipping!   WARN   console=${True}
    \   Continue For Loop If   '${profile['name']}' in @{NO_CHECK_BONDS}
    \   Log To Console   Checking server with profile ${profile['name']} now...
    \   ${profile_name} =   Get From Dictionary   ${profile}   name
    \   ${bonding_data} =   Parse Bonding Data From Profile   ${profile_name}   ${offline_interconnect}   ${profile['connectionSettings']['connections']}   ${icm_to_li}   ignoreAttributes=${ignoreAttributes}
    \   ${pingable_ip} =   get_server_reachable_ip   ${HA_FILE}   server_profile=${profile_name}
    \   Save Obj   ${profile_bonding_dir}/${profile_name}.py   expected_bonding_data   ${bonding_data}
    \   Put File To Remote Host   ${pingable_ip}   ${userName}   ${password}   ${profile_bonding_dir}/${profile_name}.py   ${SERVER_SCRIPTS_DIR}/${profile_name}.py
    \   ${output} =   Run Keyword If   ${update_link_failure_count} is ${False}   Execute Multi-test Command In Server   ${pingable_ip}   ${userName}   ${password}   ${profile_name}
    \   ...       ELSE   Execute Update Link Failure Count Command In Server   ${pingable_ip}   ${userName}   ${password}   ${profile_name}
    \   Run Keyword If   ${output} != @{EMPTY}   Set To Dictionary   ${failed_outputs}   ${profile_name}=${output}
    # Parsing of actual failures
    Run Keyword If   ${failed_outputs} != &{EMPTY}   Log To Console Bonding With Failure   ${failed_outputs}

Reset Server Link Failure Count Cache By Profile
    [Documentation]   Reset server link failure count cache using server profile data.
    [Arguments]   ${serverProfile}   ${profile_bonding_dir}=/root/tools/scripts/profiles_bonding   ${userName}=root   ${password}=rootpwd
    ${icm_to_li} =   Create Interconnects To LI Mapping
    ${passed} =    Run Keyword And Return Status   Evaluate    type(${serverProfile})
    ${type} =      Run Keyword If     ${passed}    Evaluate    type(${serverProfile})
    ${resp} =   Run Keyword If   "${type}" == "<type 'dict'>"   Set Variable   ${serverProfile}
    ...                   ELSE   Fusion Api Get Server Profiles   uri=${serverProfile}
    ${server_profile} =   Get From Dictionary   ${resp}   name
    ${NO_CHECK_BONDS} =   Get Variable Value   ${NO_CHECK_BONDS}   @{EMPTY}
    Run Keyword If   '${server_profile}' in @{NO_CHECK_BONDS}   Run Keywords   Log   Profile \"${server_profile}\" is listed in NO_CHECK_BONDS, skipping!   WARN   console=${True}   AND   Return From Keyword
    Log To Console   Resetting Link Failure Count Cache for server with profile ${server_profile} now...
    ${bonding_data} =   Parse Bonding Data From Profile   ${server_profile}   ${Null}   ${resp['connectionSettings']['connections']}   ${icm_to_li}
    ${pingable_ip} =   get_server_reachable_ip   ${HA_FILE}   server_profile=${server_profile}
    Save Obj   ${profile_bonding_dir}/${server_profile}.py   expected_bonding_data   ${bonding_data}
    Put File To Remote Host   ${pingable_ip}   ${userName}   ${password}   ${profile_bonding_dir}/${server_profile}.py   ${SERVER_SCRIPTS_DIR}/${server_profile}.py
    ${rc}   ${o} =   Execute Command And Check For Error   ${pingable_ip}   ${userName}   ${password}   ${CHECK_BONDS_SCRIPT} --reset-link-failure-count ${SERVER_SCRIPTS_DIR}/${serverProfile}.py ${SERVER_HAFILE}   verbose=${True}   fail_fast=${True}

Reset All Servers Link Failure Count Cache
    [Documentation]   Reset link failure count cache of all servers with profiles applied.
    [Arguments]   ${profile_bonding_dir}=/root/tools/scripts/profiles_bonding   ${userName}=root   ${password}=rootpwd
    ${resp} =   Fusion Api Get Server Profiles
    Run Keyword If   ${resp['total']} < 1   Fail    msg=\nUnable to retrieve server profiles!
    :FOR   ${member}   IN   @{resp['members']}
    \   Reset Server Link Failure Count Cache By Profile   ${member}   profile_bonding_dir=${profile_bonding_dir}   userName=${userName}   password=${password}

Reset Select Servers Link Failure Count Cache
    [Documentation]   Reset link failure count cache of select servers with profiles applied. Select servers are list of dictionary of select servers data (like from Get Profiles KW).
    [Arguments]   ${members}   ${profile_bonding_dir}=/root/tools/scripts/profiles_bonding   ${userName}=root   ${password}=rootpwd
    :FOR   ${member}   IN   @{members}
    \   Reset Server Link Failure Count Cache By Profile   ${member}   profile_bonding_dir=${profile_bonding_dir}   userName=${userName}   password=${password}

Log To Console Bonding With Failure
    [Documentation]   Log to console bonding with failure during server bonding-related operations. Accepts dictionary of data from bonding operation in profile_name-list of output (key-value) pair.
    [Arguments]   ${bonding_failures}
    Log To Console   \n\nCheck bond script reported failure in the following:
    :FOR   ${profile_name}   IN   @{bonding_failures.keys()}
    \   ${all_failures} =   Get Matches   ${bonding_failures['${profile_name}']}   regexp=.*\\[Failed.*\\]
    \   Log To Console   Server with Profile: ${profile_name}
    \   Run Keyword For List   ${all_failures}   Log To Console
    Fail

Exit Test When Flag File Exists
    [Documentation]   Exit test when flag file exists.
    [Arguments]   ${flag_file}=/tmp/.stop_script
    ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${flag_file}
    Pass Execution If   "${returnStatus}" == "PASS"   \n ${flag_file} found, exiting...   console=${True}

Check Suite Requirements
    [Documentation]   Check for suite requirements
    [Arguments]   ${Num_Of_Var_File}=${1}
    Run Keyword If   "${SERVER_BONDING_CHECKS}" != "${Null}" and '${SERVER_HAFILE}' == '${Null}'   Fail   msg=SERVER_BONDING_CHECKS was enabled but SERVER_HAFILE is not set. Please set the SERVER_HAFILE in your pybot command or data variable file.
    Run Keyword If   "${DISABLE_BONDING_MULTI_TEST}" == "${False}" and '${HA_FILE}' == '${Null}' or '${SERVER_HAFILE}' == '${Null}'   Fail   msg=DISABLE_BONDING_MULTI_TEST is False but HA_FILE or SERVER_HAFILE is not set. Please set the HA_FILE and SERVER_HAFILE in your pybot command or data variable file.
    Run Keyword If   "${HA_FILE}" != "${Null}"   OperatingSystem.File Should Exist   ${HA_FILE}
    Variable File Should Be Passed    ${Num_Of_Var_File}

Set Hafnium Interconnect Model
    [Documentation]  Detect which Hafnium interconnect model is being used and set suite variable.
    Return From Keyword If   '${HAFNIUM_MODEL}' != '${Null}'
    ${resp} =   Fusion Api Get Interconnect
    Run Keyword If   ${resp['total']} == 0   Fail    msg=\n GET /rest/interconnects returned total of zero(0)!
    :FOR   ${icm}   IN   @{resp['members']}
    \   ${contains} =   Evaluate   '${icm['model']}' in ${HAFNIUM_ICM_MODELS}
    \   Run Keyword If   ${contains} == True   Run Keywords   Set Suite Variable   ${HAFNIUM_MODEL}   ${icm['model']}   AND   Return From Keyword

################
# Error Handling
################
Request Should Be Successful
    [Documentation]   Check that a request has expected status code.
    [Arguments]   ${resp}   ${expectedStatusCode}=${201}
    Return From Keyword If   ${resp['status_code']} == ${expectedStatusCode}   ${resp['status_code']}
    Fail   msg=Request failed!\n errorCode: ${resp['errorCode']}\n errorSource: ${resp['errorSource']}\n message: ${resp['message']}\n details: ${resp['details']}\n recommendedActions: ${resp['recommendedActions']}

Check Asynchronous Task Response For Error
    [Documentation]   Check asynchronous request response body and parse error(s) if any.
    [Arguments]    ${resp}   ${processErrorCode}=${Null}
    ${location} =    Get Variable Value    ${resp['headers']['location']}
    ${taskUri} =    Run Keyword If    '${location}' is not 'None'   Get Variable Value    ${location}
    ...                     ELSE IF   ${resp['associatedResource']} is not ${null}   Get From Dictionary	${resp['associatedResource']}	resourceUri
    ...                        ELSE   Get From Dictionary   ${resp}   uri
    ${resourceName} = 	Run Keyword If   ${resp['associatedResource']} is not ${null}   Get From Dictionary	${resp['associatedResource']}	resourceName
    Run Keyword If   '${taskUri}' == '${null}'   Log   Something seems wrong and resource name ${resourceName} has a uri of ${null}. Parsing task errors...   WARN
    Log   \n Task: [${resp['category']}:${resp['name']}] is: ${resp['taskState']} for resource: ${resourceName}   console=${True}
    ${l} =   Get Length   ${resp['taskErrors']}
    ${errorCodeFound} =   Set Variable   ${False}
    :FOR   ${i}   IN RANGE   0   ${l}
    \   Log   \n errorCode: ${resp['taskErrors'][${i}]['errorCode']} \n errorSource: ${resp['taskErrors'][${i}]['errorSource']} \n message: ${resp['taskErrors'][${i}]['message']} \n recommendedActions: ${resp['taskErrors'][${i}]['recommendedActions']}   console=${True}
    \   Run Keyword If   '${resp['taskErrors'][${i}]['errorCode']}' == '${processErrorCode}'   Set Test Variable   ${errorCodeFound}   ${True}
    Run Keyword If   ${l} > ${0} and '${processErrorCode}' == '${null}'   Fail   msg=Task [${resp['category']}:${resp['name']}] for resource ${resourceName} failed.
    ...    ELSE IF   '${processErrorCode}' != '${null}' and ${errorCodeFound} is ${True}   Return From Keyword   ${processErrorCode}
    ...    ELSE   Return From Keyword   ${Null}

Asynchronous Task Should Be Successful
    [Documentation]   Check that asynchronous task was successful and resourceUri is not null.
    ...               This does not follow the task and assumed task response was from wait for task keyword.
    [Arguments]    ${task}   ${checkAssociatedResourceUri}=${True}
    Run Keyword If   ${task} == ${null}   Fail  msg=Task is ${null}.
    ${associatedResourceUri} = 	Get From Dictionary	${task['associatedResource']}	resourceUri
    ${associatedResourceName} = 	Get From Dictionary	${task['associatedResource']}	resourceName
    Run Keyword If   '${associatedResourceUri}' == '${null}'   Log   \n associatedResourceName is ${null} and resourceUri is ${null} for this resource. Parsing task for errors (if any)...   console=${True}
    Log   \n Task: [${task['category']}:${task['name']}] is: ${task['taskState']} for resource: ${associatedResourceName}   console=${True}
    ${l} =   Get Length   ${task['taskErrors']}
    :FOR   ${i}   IN RANGE   0   ${l}
    \   Log   \n errorCode: ${task['taskErrors'][${i}]['errorCode']}\n errorSource: ${task['taskErrors'][${i}]['errorSource']}\n message: ${task['taskErrors'][${i}]['message']}\n recommendedActions: ${task['taskErrors'][${i}]['recommendedActions']}   console=${True}
    Run Keyword If   ${checkAssociatedResourceUri} == ${True} and '${associatedResourceUri}' == '${null}'   Fail   msg=Failed to create ${associatedResourceName}.
    Run Keyword If   ${l} > 0   Fail   msg=Task error was found!	

Check Response For Error
    [Documentation]   Check response body for error and parse if any.
    [Arguments]   ${resp}
    Return From Keyword If   ${resp['status_code']} == ${200} or ${resp['status_code']} == ${202}   ${resp['status_code']}
    Fail   msg=\n errorCode: ${resp['errorCode']} \n errorSource: ${resp['errorSource']} \n message: ${resp['message']} \n recommendedActions: ${resp['recommendedActions']}

################
# Uplinks
################
Create Uplink Set From Variable
    [Documentation]   Create uplink set defined in data_variables.py
    [Arguments]    ${uplink_sets}   ${wait_task_timeout}=15m   ${wait_task_interval}=15s
    ${uplink_sets_resolved} =   Resolve Uplink Set Uris   ${uplink_sets}
    :FOR   ${x}   IN   @{uplink_sets_resolved}    
    \   ${resp} =   Fusion Api Create Uplink Set   body=${x}   
    \   ${statusCode} =   Check Response For Error   ${resp}
    \   ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    \   ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    \   Check Asynchronous Task Response For Error   ${task}
 
Create New Uplink Set
    [Documentation]   Check that ICMs are in configured state before creating new uplink set.
    [Arguments]   ${uplink_sets}   ${icm_names}   ${message}=Creating new uplink set from data variable file.   ${wait_timeout}=15m   ${wait_interval}=15s
    Log   ${message}   console=${True}
    Wait Until List Of ICMs Reached Configured   ${icm_names}   ${wait_timeout}   ${wait_interval}
    Create Uplink Set From Variable   ${uplink_sets}   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    Wait Until List Of ICMs Reached Configured   ${icm_names}   ${wait_timeout}   ${wait_interval}

Resolve Uplink Set Uris
    [Documentation]   Make a query to OneView with the uri name and return the real uri to uplink set body.
    [Arguments]   ${uplinkSets}
    ${l} =   Get Length   ${uplinkSets}
    #resolve networkUris, logicalInterconnectUri, and nativeNetworkUri
    :FOR   ${x}	  IN RANGE   0   ${l}
    \   ${networkType} =   Get From Dictionary   ${uplinkSets[${x}]}   networkType
    \   ${resolvedLI} =   Get Lines Matching Regexp   ${uplinkSets[${x}]['logicalInterconnectUri']}   /rest/   partial_match=true
    \   ${liUri} =   Run Keyword If   '${resolvedLI}' == ''   Get LI URI   ${uplinkSets[${x}]['logicalInterconnectUri']}
    \   ...                    ELSE   Set Variable   ${uplinkSets[${x}]['logicalInterconnectUri']}
    \   Set To Dictionary   ${uplinkSets[${x}]}   logicalInterconnectUri   ${liUri}
    \   ${nativeNetworkUri} =   Get Variable Value   ${uplinkSets[${x}]['nativeNetworkUri']}
    \   ${resolvedUri} =   Run Keyword If   '${nativeNetworkUri}' != '${null}'   Get Lines Matching Regexp   ${nativeNetworkUri}   /rest/   partial_match=true
    \   ${nativeNetworkUri} =   Run Keyword If   '${resolvedUri}' == '' and '${nativeNetworkUri}' != '${null}'   Get Ethernet Uri   ${nativeNetworkUri}
    \   ...                               ELSE   Set Variable   ${nativeNetworkUri}
    \   Set To Dictionary   ${uplinkSets[${x}]}   nativeNetworkUri   ${nativeNetworkUri}
    \   ${resolvedUri} =   Run Keyword If   ${uplinkSets[${x}]['networkUris']} != @{EMPTY}   Get Lines Matching Regexp   ${uplinkSets[${x}]['networkUris'][0]}   /rest/   partial_match=true
    \   ${networkUris} =   Run Keyword If   '${resolvedUri}' == ''   Get Ethernet URIs   ${uplinkSets[${x}]['networkUris']}
    \   ...                          ELSE   Set Variable   ${uplinkSets[${x}]['networkUris']}
    \   Set To Dictionary   ${uplinkSets[${x}]}   networkUris   ${networkUris}
    \   ${resolvedUri} =   Run Keyword If   ${uplinkSets[${x}]['fcoeNetworkUris']} != @{EMPTY}   Get Lines Matching Regexp   ${uplinkSets[${x}]['fcoeNetworkUris'][0]}   /rest/   partial_match=true
    \   ${fcoeNetworkUris} =   Run Keyword If   '${resolvedUri}' == ''   Get FCoE Uris   ${uplinkSets[${x}]['fcoeNetworkUris']}
    \   ...                              ELSE   Set Variable   ${uplinkSets[${x}]['fcoeNetworkUris']}
    \   Set To Dictionary   ${uplinkSets[${x}]}   fcoeNetworkUris   ${fcoeNetworkUris}
    \   Run Keyword If   '${networkType}' == 'Ethernet'	  Continue For Loop
    \   ${resolvedUri} =   Run Keyword If   ${uplinkSets[${x}]['fcNetworkUris']} != @{EMPTY}   Get Lines Matching Regexp   ${uplinkSets[${x}]['fcNetworkUris'][0]}   /rest/   partial_match=true
    \   ${fcNetworkUris} =   Run Keyword If   '${resolvedUri}' == ''   Get FC Uris   ${uplinkSets[${x}]['fcNetworkUris']}
    \   ...                            ELSE   Set Variable   ${uplinkSets[${x}]['fcNetworkUris']}
    \   Set To Dictionary   ${uplinkSets[${x}]}   fcNetworkUris   ${fcNetworkUris}
    \   Run Keyword If   '${networkType}' == 'FibreChannel'   Continue For Loop
    [Return]   ${uplinkSets}

Edit Uplink Set
    [Documentation]   Edit uplink set and fail on error.
    [Arguments]    ${uplink_set}   ${icm_names}   ${message}=Editing existing uplink set.   ${wait_task_timeout}=15m   ${wait_task_interval}=15s
    ${uplink_set} =   Resolve Uplink Set Uris   ${uplink_set}
    Log   ${message}   console=${True}
    :FOR  ${x}  IN   @{uplink_set}  
    \   ${uri} =   Get Uplinkset Uri   ${x['name']}
    \   Set To Dictionary   ${x}   uri=${uri} 
    \   ${resp} =   Fusion Api Edit Uplink Set   body=${x}   uri=${uri}
    \   ${statusCode} =   Check Response For Error   ${resp}
    \   ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    \   ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    \   Wait Until List Of ICMs Reached Configured   ${icm_names}   ${wait_task_timeout}   ${wait_task_interval}

Delete Uplink Set
    [Documentation]   Delete an existing Uplink Set
    [Arguments]   ${name}   ${icm_names}   ${message}=Deleting existing uplink set.   ${wait_task_timeout}=15m   ${wait_task_interval}=15s
    Log   ${message}   console=${True}
    ${resp} =   Fusion Api Delete Uplink Set   ${name}
    ${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task}
    Wait Until List Of ICMs Reached Configured   ${icm_names}   ${wait_task_timeout}   ${wait_task_interval}

Recreate Uplink Set
    [Documentation]   Recreate a deleted Uplink Set.
    [Arguments]   ${uplink_set}   ${icm_names}   ${message}=Recreating a deleted uplink set.   ${wait_task_timeout}=15m   ${wait_task_interval}=15s
    Log   ${message}   console=${True}
    Create Uplink Set From Variable   ${uplink_set}   wait_task_timeout=${wait_task_timeout}   wait_task_interval=${wait_task_interval}
    Wait Until List Of ICMs Reached Configured   ${icm_names}   ${wait_task_timeout}   ${wait_task_interval}

Get Port Config Infos Port
    [Documentation]   Get portUri attributes of the portConfigInfos.
    ...               This also verifies that lagId is the same for a particular portConfigInfos.
    ...               Returns key string and value like: <priKey>    [{<attributes1>},{<attributes2>},..{<attributesn>}].
    [Arguments]   ${portConfigInfos}   ${attrList}   ${priKey}=lagId
    ${lagAttr} =   Create List
    ${prevpKey} =   Set Variable   ${0}
    :FOR   ${p}   IN   @{portConfigInfos}
    \   ${resp} =   Fusion Api Get Resource   ${p['portUri']}
    \   ${attr} =   Get Attributes From Response Body Member   ${resp}   ${attrList}
    \   ${pKey} =   Convert To String   ${attr['${priKey}']}
    # make sure we only have 1 lagId
    \   Run Keyword If   ${prevpKey} != ${0}   Should Be Equal As Strings   ${prevpKey}   ${pKey}   msg=More than one lagId is found for this portConfigInfos.
    \   Append To List   ${lagAttr}   ${attr}
    \   ${prevpKey} =   Set Variable   ${pKey}
    [Return]   ${pKey}   ${lagAttr}

Get Uplink Sets Attributes
    [Documentation]   Get uplink sets based on the provided list of names and attributes.
    ...               Returns list of dictionaries.
    [Arguments]   ${uplinkSetNames}   ${uplinkSetAttrs}
    ${selectUS} =   Create Dictionary
    :FOR   ${u}   IN   @{uplinkSetNames}
    \   ${resp} =   Fusion Api Get Uplink Set   param=?filter="name='${u}'"
    \   Length Should Be   ${resp['members']}   1   msg=Uplink Set '${u}' query in OneView returned unexpected members.
    \   ${pKey}   ${lagAttr} =   Get Port Config Infos Port   ${resp['members'][0]['portConfigInfos']}   ${uplinkSetAttrs}
    \   Set To Dictionary   ${selectUS}   ${pKey}=${lagAttr}
    [Return]   ${selectUS}

Port Status Should Be Linked And Active
    [Documentation]   Check that portStatus is Linked.
    [Arguments]   ${uplinkSetsAttrs}
    ${EXPECTED_PORTS_ATTRIBUTES} =   Get Variable Value   ${EXPECTED_PORTS_ATTRIBUTES}
    :FOR   ${u}   IN   @{uplinkSetsAttrs}
    \   ${portsExpected} =   Run Keyword If   ${EXPECTED_PORTS_ATTRIBUTES} != &{EMPTY}   Check Data   ${EXPECTED_PORTS_ATTRIBUTES}   ${u}
    \   ...                            ELSE   Log    Your data variable file does not contain 'EXPECTED_PORTS_ATTRIBUTES' dictionary for portUri attributes to check.   WARN   console=${True}
    \   Return From Keyword If   '${portsExpected}' == '${False}'   ${False}
    [Return]   ${True}

################
# SSH/SCP
################
Put File To Remote Host
    [Documentation]   Copy file to remote host over ssh.
    [Arguments]   ${remoteHost}   ${remoteUser}   ${remotePasswd}   ${source}   ${destination}   ${keepConnection}=${False}   ${verbose}=${False}   ${iface}=eth0
    Open Connection And Login To Host   ${remoteHost}   ${remoteUser}   ${remotePasswd}   verbose=${verbose}   iface=${iface}
    SSHLibrary.Put File    ${source}    ${destination}
    Run Keyword If   ${verbose} is ${True}   Log To Console     Files transferred to ${remoteHost}:${destination}
    Run Keyword If   ${keepConnection} == ${False}   Close All Connections

Execute Command To Remote Host
    [Documentation]   Open ssh connection and login to remote host then execute the command.
    [Arguments]   ${remoteHost}   ${remoteUser}   ${remotePasswd}   ${command}   ${verbose}=${False}   ${iface}=eth0   ${readOutputWaitTime}=2s
    ${readOutputWaitTime} =   Get Variable Value   ${SSH_READ_WAIT}   ${readOutputWaitTime}
    Open Connection And Login To Host   ${remoteHost}   ${remoteUser}   ${remotePasswd}   verbose=${verbose}   iface=${iface}
    Write   ${command}
    ${o} =   Read   delay=${readOutputWaitTime}
    Close All Connections
    ${out} =   Split String   ${o}   ${\n}
    :FOR   ${i}   IN   @{out}
    \   Run Keyword If   ${verbose} is not ${False}   Log   \nDEBUG: ${i}   console=${True}
    [Return]   ${o}

Execute Command And Check For Error
    [Documentation]   Open ssh connection and login to remote host then execute the command without using write.
    [Arguments]   ${remoteHost}   ${remoteUser}   ${remotePasswd}   ${command}   ${verbose}=${False}   ${iface}=eth0   ${fail_fast}=${True}
    Open Connection And Login To Host   ${remoteHost}   ${remoteUser}   ${remotePasswd}   verbose=${verbose}   iface=${iface}
    ${o}   ${stderr}   ${rc} =    Execute Command   ${command}   return_stderr=True   return_rc=True
    Close All Connections
    ${out} =   Split String   ${o}   ${\n}
    :FOR   ${i}   IN   @{out}
    \   Run Keyword If   ${verbose} is not ${False}   Log   \nDEBUG: ${i}   console=${True}
    Run Keyword If   '${rc}' != '0' and ${fail_fast} == ${True}   Fail   msg=\nCommand returned a non-zero return code, check for error and try again: ${command}, ${rc}
    ...    ELSE IF   '${rc}' != '0'   Log   \nCommand returned a non-zero return code, check for error and try again: ${command}, ${rc}   WARN   console=${True}
    [Return]   ${rc}   ${o}

Open Connection And Login To Host
    [Documentation]   Open ssh connection and login to remote host.
    [Arguments]   ${remoteHost}   ${remoteUser}   ${remotePasswd}   ${verbose}=${True}   ${iface}=eth0
    ${sanitizedHost} =   Get Variable Value   ${remoteHost}
    ${sanitizedHost} =   Remove String Using Regexp   ${sanitizedHost}   (\\[|\\])
    ${llAddr} =   Get Lines Matching Regexp   ${sanitizedHost}   ^fe80:   partial_match=true
    Run Keyword If   '${llAddr}' == '${EMPTY}'   Open Connection  ${sanitizedHost}
    ...       ELSE   Open Connection  ${sanitizedHost}%${iface}
    Login   ${remoteUser}   ${remotePasswd}
    Run Keyword If   ${verbose} is ${True}   Log To Console     Logged in to host: ${sanitizedHost}   no_newline=${True}

Execute Multi-test Command In Server
    [Documentation]   Run check_bonds.py's multi-test in the server.
    [Arguments]   ${pingable_ip}   ${userName}   ${password}   ${profile_name}   ${icm_sleep}=0   ${fail_fast}=${False}
    ${rc}   ${o} =   Execute Command And Check For Error   ${pingable_ip}   ${userName}   ${password}   ${CHECK_BONDS_SCRIPT} --time ${icm_sleep} --multi-test ${SERVER_SCRIPTS_DIR}/${profile_name}.py ${SERVER_HAFILE}   verbose=${True}   fail_fast=${fail_fast}
    ${out} =   Run Keyword If   ${rc} != 0 and ${fail_fast} == ${True}   Fail   msg=\n\nFailed to pass all bonding interfaces checks for the following:\n${profile_name}, ${o}
    ...    ELSE IF   ${rc} != 0 and ${fail_fast} == ${False}   Split String   ${o}   ${\n}
    ...    ELSE IF   ${rc} != 0   Fail   msg=Invalid value was provided for argument fail_fast: ${fail_fast). Please provide a valid Boolean value.
    ...    ELSE   Create List
    [Return]   ${out}

Execute Update Link Failure Count Command In Server
    [Documentation]   Perform an update on link failure count cache in the server.
    [Arguments]   ${pingable_ip}   ${userName}   ${password}   ${profile_name}   ${fail_fast}=${False}
    ${rc}   ${o} =   Execute Command And Check For Error   ${pingable_ip}   ${userName}   ${password}   ${CHECK_BONDS_SCRIPT} --update-link-failure-count ${SERVER_SCRIPTS_DIR}/${profile_name}.py ${SERVER_HAFILE}   verbose=${True}   fail_fast=${fail_fast}
    ${out} =   Run Keyword If   ${rc} != 0 and ${fail_fast} == ${True}   Fail   msg=\n\nFailed to update link failure count cache:\n${profile_name}, ${o}
    ...    ELSE IF   ${rc} != 0 and ${fail_fast} == ${False}   Split String   ${o}   ${\n}
    ...    ELSE IF   ${rc} != 0   Fail   msg=Invalid value was provided for argument fail_fast: ${fail_fast). Please provide a valid Boolean value.
    ...    ELSE   Create List
    [Return]   ${out}

################
# Firmware Management
################
Load SPP FW Bundle
    [Documentation]    Load SPP FW Bundle when SPP_BUNDLE_DIR has none noneType value.
    [Arguments]   ${bundle_dir}=${SPP_BUNDLE_DIR}   ${bundle_name}=${SPP_BUNDLE_NAME}   ${wait_task_timeout}=60m   ${wait_task_interval}=30s
    Run Keyword If   '${bundle_dir}' != '${null}'  Upload SPP FW Bundle   wait_task_timeout=${wait_task_timeout}   wait_task_interval=${wait_task_interval}
    ${resp} =   Fusion Api Get Firmware Driver
    Run Keyword If   ${resp['count']} == 0   Fail    msg=\n No SPP bundle was found in OneView!
    :FOR   ${member}   IN   @{resp['members']}
    \   Return From Keyword If   '${member['isoFileName']}' == '${bundle_name}.iso'   ${member['uri']}
    Fail   msg=\n SPP Bundle name "${bundle_name}" not found!

Upload SPP FW Bundle
    [Documentation]   Delete existing same version SPP from OneView if any then upload SPP FW Bundle.
    [Arguments]   ${wait_task_timeout}=60m   ${wait_task_interval}=30s
    Log   \nChecking for existing same version SPP FW Bundle...   console=${True}
    ${fwDrivers} =   Fusion Api Get Firmware Driver
    :FOR   ${f}   IN   @{fwDrivers['members']}
    \   Run Keyword If   ${SPP_BUNDLE_PATH.__contains__('${f['version']}')}==True   Remove Existing Firmware Driver   ${f['uri']}   wait_task_timeout=${wait_task_timeout}   wait_task_interval=${wait_task_interval}
    \   ...                         ELSE   Continue For Loop
    Log   \nUploading SPP Bundle For The FW Update...   console=${True}
    ${resp} =   Fusion Api Upload Firmware Bundle   localfile=${SPP_BUNDLE_PATH}
    ${statusCode} =   Check Response For Error   ${resp}
    Run Keyword If   ${statusCode} != ${202}   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    #JMP: Instead of parsing this in fusion_api_appliance_setup.txt, I am doing it here because copy.Deep Copy will crash in Validate Response
    #JMP: 05/31/2017: After updating my working copy, I found that Yulong Gu made change to FusionLibrary request.py to print nice response body that make this useless.
    # ${task_uri} =   Parse Task Uri From Content   ${resp}
    ${task_uri} =   Get From Dictionary   ${resp}   uri
    ${resp} =    Fusion Api Get Task    uri=${task_uri} 
    ${task} =   Run Keyword If   '${SPP_BUNDLE_DIR}' != '${null}'   fusion_api_appliance_setup.Wait For Task   ${resp}   ${wait_task_timeout}   ${wait_task_interval}   status_code=${200}
    Run Keyword If   '${SPP_BUNDLE_DIR}' != '${null}'   Check Asynchronous Task Response For Error   ${task}

Remove Existing Firmware Driver
    [Documentation]   Remove and existing SPP FW Bundle.
    [Arguments]   ${uri}   ${wait_task_timeout}=60m   ${wait_task_interval}=30s
    ${resp} =   Fusion Api Remove Firmware Driver   uri=${uri}
    ${statusCode} =   Check Response For Error   ${resp}
    Run Keyword If   ${statusCode} != ${202}   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    ${task_uri} =   Get From Dictionary   ${resp}   uri
    ${resp} =    Fusion Api Get Task    uri=${task_uri} 
    ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   ${wait_task_timeout}   ${wait_task_interval}   status_code=${200}
    Check Asynchronous Task Response For Error   ${task}

Create Custom Firmware Bundle
    [Documentation]   Create a custom firmware bundle with the SPP and all rpms that are currently uploaded to the appliance.  All non-iso files will be treated as RPMs and will be included in the custom SPP package.
    [Arguments]   ${SPP_BUNDLE_NAME}   ${SPP_UPLOAD_WAIT_TIMEOUT}   ${SPP_UPLOAD_WAIT_INTERVAL}   ${wait_task_timeout}=60m   ${wait_task_interval}=30s 
    ${resp} =   Fusion Api Get Firmware Driver
    ${baselineUri} =   Load SPP FW Bundle   bundle_dir=None   bundle_name=${SPP_BUNDLE_NAME}   wait_task_timeout=${SPP_UPLOAD_WAIT_TIMEOUT}   wait_task_interval=${SPP_UPLOAD_WAIT_INTERVAL}
    @{hotfixUris} =   Create List
    :FOR   ${member}   IN   @{resp['members']}
    \   ${contains} =   Evaluate   'iso' in '${member['isoFileName']}'
    \   Run Keyword If   ${contains} == False   Append To List   ${hotfixUris}   ${member['uri']}
    ${CUSTOM_FW_BODY} =   Create Dictionary   baselineUri=${baselineUri}   hotfixUris=@{hotfixUris}   customBaselineName=${CUSTOM_SPP_BUNDLE_NAME}
    ${resp} =   fusion api create firmware bundle   ${CUSTOM_FW_BODY}
    ${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   ${wait_task_timeout}   ${wait_task_interval}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task}  

Remove Custom Firmware Bundle
    [Documentation]   Remove the specified custom firmware bundle.  
    [Arguments]   ${customUri}   ${wait_task_timeout}=60m   ${wait_task_interval}=30s
    ${resp} =   fusion api remove firmware driver   uri=${customUri}
    ${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   ${wait_task_timeout}   ${wait_task_interval}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task}

##########
# Networks
##########

Create Ethernet Range
    [Documentation]   Create a range of Ethernet networks based on provided range in variable.
    [Arguments]	${range}
    Set Log Level	TRACE
    Log   \n\nAdding ETHERNET NETWORK RANGES...   console=${True}
    ${body} =   fusion_api_appliance_setup.Copy Dictionary   ${range}
    Remove From Dictionary   ${body}   prefix   suffix   start   end
    :FOR   ${x}   IN RANGE   ${range['start']}   ${range['end']}+1
    \   Set To Dictionary   ${body}   name   ${range['prefix']}${x}${range['suffix']}
    \   Set To Dictionary   ${body}   vlanId   ${x}
    \	${resp} =   Fusion Api Create Ethernet Network   body=${body}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=240s   interval=5s
    \   Asynchronous Task Should Be Successful   ${task}

Add Network Sets from variable
    [Documentation]   Add Network sets to an appliance from a variable which contains a list of dicts with the entire payload.
    [Arguments]   ${networks}
    Log   \n\nAdding NETWORK SETS...   console=${True}
    :FOR   ${net}   IN   @{networks}
    \   ${networkUris} =   Get Ethernet URIs   ${net['networkUris']}
    \   Set to dictionary   ${net}   networkUris   ${networkUris}
    \   ${nativeNetworkUri} =   Run Keyword If   '${net['nativeNetworkUri']}' != 'None'   Get Ethernet URI   ${net['nativeNetworkUri']}
    \   Set To Dictionary   ${net}   nativeNetworkUri   ${nativeNetworkUri}
    \   ${resp} =   Fusion Api Create Network Set   body=${net}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=240s   interval=5s
    \   Asynchronous Task Should Be Successful   ${task}

Add FC Networks from variable
    [Documentation]   Adds FC networks to an appliance from a variable which contains a list of dicts with the entire payload
    [Arguments]   ${networks}
    Log   \n\nAdding FC NETWORKS...   console=${True}
    :FOR   ${net}   IN   @{networks}
    \   ${resp} =   Fusion Api Create FC Network   body=${net}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=240s   interval=5s
    \   Asynchronous Task Should Be Successful   ${task}

Add FCoE Networks from variable
    [Documentation]	Adds FCoE networks to an appliance from a variable which contains a list of dicts with the entire payload
    [Arguments]   ${networks}
    Log   \n\nAdding FCOE NETWORKS...   console=${True}
    :FOR   ${net}   IN   @{networks}
    \   ${resp} =   Fusion Api Create FCoE Network   body=${net}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=240s   interval=5s
    \   Asynchronous Task Should Be Successful   ${task}

################
# Network Helper
################
Add Ethernet Networks from variable
    [Documentation]   Add Ethernet networks to an appliance from a variable which contains a list of dicts with the entire payload.
    [Arguments]   ${networks}
    Log   \n\nAdding ETHERNET NETWORKS...   console=${True}
    :FOR   ${net}   IN   @{networks}
    \   ${resp} =   Fusion Api Create Ethernet Network   body=${net}
    \   Request Should Be Successful   ${resp}   expectedStatusCode=${202}
    \   ${task} =   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=240s   interval=5s
    \   Asynchronous Task Should Be Successful   ${task}
    
Delete FC Networks
    [Documentation]   Remove FC networks from variable.
    [Arguments]   ${fcNetworks}   ${wait_timeout}=4m   ${wait_interval}=2s   ${waitForTask}=${True}  ${parallel}=${True}   ${validate}=${True}
    Log   Removing FC NETWORKS   console=${True}
    ${respList} =   Create List
    ${valDict} =   Create Dictionary   status_code=${200}
    ...                                taskState=Completed
    Set Suite Variable   ${forkedErrorFound}   ${False}
    :FOR   ${net}   IN   @{fcNetworks}
    \    ${resp} =   Fusion Api Get FC Networks   param=?filter="name='${net['name']}'"
    \    ${resp} =   Fusion Api Delete FC Network    uri=${resp['members'][0]['uri']}
    \   Run Keyword If   ${parallel} == ${True}   Append To List   ${respList}   ${resp}
    \   ...   ELSE   fusion_api_appliance_setup.Wait For Task And Validate Response   ${resp}   ${valDict}   ${wait_timeout}   ${wait_interval}   ${validate}
    Run Keyword If   ${parallel} == ${True} and ${waitForTask} is ${True}   common.Wait For Forked Tasks   ${respList}   ${valDict}   ${wait_timeout}   ${wait_interval}   ${validate}
    Run Keyword If   ${forkedErrorFound} is ${True}   Fail   msg=Not all forked tasks state finished with Completed.

################
# TOR Switches
################
Get 59XX Roles
    [Documentation]   Get 59xx roles of an IRF enabled setup.
    ...               This will return a dictionary of roles with MemberID, Priority, CPU-Mac.
    [Arguments]   ${host}   ${timeout}=15m   ${userName}=admin   ${password}=password   ${readOutputWaitTime}=2s   ${iface}=eth0
    Log   Logging in to the switch...   console=${True}
    ${readOutputWaitTime} =   Get Variable Value   ${SSH_READ_WAIT}   ${readOutputWaitTime}
    ${llAddr} =   Get Lines Matching Regexp   ${host}   ^fe80:   partial_match=true
    Run Keyword If   '${llAddr}' == '${EMPTY}'   Open Connection  ${host}   timeout=${timeout}
    ...       ELSE   Open Connection  ${host}%${iface}   timeout=${timeout}
    Login   ${userName}   ${password}
    Log   Getting irf data...   console=${True}
    Write   display irf
    ${o} =   Read   delay=${readOutputWaitTime}
    Close All Connections
    ${irf} =   Split String   ${o}   ${\n}
    :FOR   ${i}   IN   @{irf}
    \   Log   \nDEBUG: ${i}   console=${True}
    ${master} =   Get From List   ${irf}   ${IRF_DISPLAY_NUMBER}
    ${master} =   Evaluate   ' '.join($master.split())
    ${IRF_DISPLAY_NUMBER} =   Evaluate   ${IRF_DISPLAY_NUMBER}+1
    ${standby} =   Get From List   ${irf}   ${IRF_DISPLAY_NUMBER}
    ${standby} =   Evaluate   ' '.join($standby.split())
    ${master} =   Split String   ${master}   ${SPACE}
    ${standby} =   Split String   ${standby}   ${SPACE}
    ${attr} =   Create Dictionary   memberid=${master[0]}   role=${master[1]}   priority=${master[2]}   cpu-mac=${master[3]}
    ${roles} =   Create Dictionary   ${master[1]}=${attr}
    ${attr} =   Create Dictionary   memberid=${standby[0]}   role=${standby[1]}   priority=${standby[2]}   cpu-mac=${standby[3]}
    Set To Dictionary   ${roles}   ${standby[1]}=${attr}
    [Return]   ${roles}

Switch Roles Should Have Transitioned
    [Documentation]   Verify that role changed and fail if not.
    [Arguments]   ${pre}   ${post}
    Log   Verifying that Master IRF role has changed...   console=${True}
    Log   Previous Master: ${pre}   console=${True}
    Log   Current active: ${post}   console=${True}
    Should Be Equal As Strings   ${pre['Master']['cpu-mac']}   ${post['Standby']['cpu-mac']}   msg=The expected new Master IRF should now be ${pre['Standby']['cpu-mac']}.
    Log   Master IRF role change was successful.   console=${True}

Reapply config in Logical Interconnect
    [Documentation]	   Re-applies the configuration to Logical Interconnect
    [Arguments]     ${LI}    ${wait_task_timeout}=30m   ${wait_task_interval}=5s
    ${LI_len}  Get Length	${LI}
	:FOR	${x}	IN RANGE	0	${LI_len}
	\    Log   \n Reapplying configuration in LI ${LI[${x}]} \n   console=${True}
    \    ${li_uri} =   Get LI URI   ${LI[${x}]}
    \   ${resp}    Fusion Api Reapply LI Configuration   ${li_uri}
	\   ${statusCode} =   Check Response For Error   ${resp}
    \   ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    \   ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    \   Check Asynchronous Task Response For Error   ${task}

Reapply config in Logical Enclosure
    [Documentation]	   Re-applies the configuration to Logical Enclosure
	[Arguments]   ${LE}   ${wait_task_timeout}=45m   ${wait_task_interval}=5s
    ${LE_len}  Get Length	${LE}
	:FOR	${x}	IN RANGE	0	${LE_len}
    \    Log   \n Reapply configuration in LE ${LE[${x}]} \n   console=${True}
    \    ${LE_URI} =   Get LE URI   ${LE[${x}]}
    \    ${resp}   Fusion Api Reapply Le Configuration   ${LE_URI}
	\   ${statusCode} =   Check Response For Error   ${resp}
    \   ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    \   ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    \   Check Asynchronous Task Response For Error   ${task}

Update from group in LI
    [Documentation]	   Performs update from group in LI page
	[Arguments]   ${LI}   ${wait_task_timeout}=45m   ${wait_task_interval}=5s
    ${LI_len}  Get Length	${LI}
	:FOR	${x}	IN RANGE	0	${LI_len}
	\    ${LI_URI} =   Get LI URI   ${LI[${x}]}
    \    ${resp} =   Fusion Api Update from group   ${LI_URI}
	\   ${statusCode} =   Check Response For Error   ${resp}
    \   ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    \   ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    \   Check Asynchronous Task Response For Error   ${task}
    \    Log   \n checking consistency status of LI   console=${True}
    \    ${li_resp} =   Fusion Api Get Li   ${LI_URI}
    \    Run keyword unless  '${li_resp['consistencyStatus']}' == 'CONSISTENT'   Fail   ${LI_URI} is ${li_resp['consistencyStatus']} when consistencyStatus:CONSISTENT is expected.

Create OV Support Dump And Download
    [Documentation]	   Performs OV support dump creation and download operation
	[Arguments]   ${wait_task_timeout}=60m   ${wait_task_interval}=5s
    ${retStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.Directory Should Exist   ${OV_dump_file_Dir}
    Run Keyword If   "${retStatus}" == "FAIL"   OperatingSystem.Create Directory   ${OV_dump_file_Dir}
    ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${OV_support_dump_file}
    Run Keyword If   "${returnStatus}" == "PASS"   OperatingSystem.Remove File   ${OV_support_dump_file}
	Log   \n Creating OV support dump...   console=${True}
    ${resp}   Fusion Api Create Support Dump   ${SUPPORT_DUMP}
    Run Keyword If  '${resp['status_code']}' != '200'   Fail ELSE  Log  \nSuccessfully created support dump
    ${dump_uri} =   Get From Dictionary   ${resp}   uri
    Log   \n Downloading OV support dump...   console=${True}
    ${resp} =   Fusion Api Download Support Dump   uri=${dump_uri}   localfile=${OV_support_dump_file}
    Run Keyword If  '${resp['status_code']}' != '200'   Fail ELSE  Log   \n downloading support dump

Create LE Support Dump And Download
    [Documentation]	   Performs LE support dump creation and download operation
	[Arguments]   ${LE}   ${wait_task_timeout}=30m   ${wait_task_interval}=5s
    ${retStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.Directory Should Exist   ${LE_dump_file_Dir}
    Run Keyword If   "${retStatus}" == "FAIL"   OperatingSystem.Create Directory   ${LE_dump_file_Dir}
    ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${LE_dump_file}
    Run Keyword If   "${returnStatus}" == "PASS"   OperatingSystem.Remove File   ${LE_dump_file}
    :FOR    ${x}  IN  @{LE}
	\    ${resp}    Fusion Api Get Logical Enclosure    param=?filter="'name'=='${x}'"
    \    Should Be Equal   ${resp['total']}   ${1}   msg=Response body total is not as expected.
	\    ${LEuri} =	Get from dictionary		${resp['members'][0]}	uri
	\    ${LE_id} =  Split String From Right		${LEuri}	/	1
	\    Log		\n Le id is : ${LE_id[-1]}    console=True
	\    ${resp}    	Fusion Api Get Logical Enclosure Support Dump    ${LE_SupportDump_Payload}    ${LE_id[-1]}
	\    ${task_resp} =    fusion_api_appliance_setup.Wait For Task    ${resp}    ${wait_task_timeout}   ${wait_task_interval}
	\    ${supportDumpUri}=          Get From Dictionary     ${task_resp['associatedResource']}   resourceUri
	\     Log   \n Downloading LE support dump  console=${True}
	\    ${resp} =    Fusion Api Download Support Dump    uri=${supportDumpUri}          localfile=${LE_dump_file}
	\    Run Keyword If  '${resp['status_code']}' != '200'    Fail ELSE  Log   \n downloading support dump

Unassign reassign the required profiles
    [Documentation]	   Unassign reassign the profiles which are in critical state after restoration
    [Arguments]   ${PROFILES}
    Power Off Servers Assigned In Profile From Variable    ${PROFILES}
	common.Unassign Server Profiles   ${PROFILES}
	common.Assign Server Profiles     ${PROFILES}
	Power On Servers Assigned In Profile From Variable    ${PROFILES}
    Sleep And Log Reason To Console   ${SERVER_UNASSIGN_REASSIGN_SLEEP}   reason=Sleeping for ${SERVER_UNASSIGN_REASSIGN_SLEEP} to let the servers to poweron...

Check server status after appliance restoration
    [Documentation]	   Checks server status after appliance restoration
    [Arguments]   ${PROFILES}
    ${PROFILE_LIST}     Create List
	${Profile_len} =   Run Keyword If  "${PROFILES}" != "${null}"   Get Length   ${PROFILES}
	:FOR   ${x}   IN RANGE   0   ${Profile_len}
	\   ${profile_resp} =    Fusion Api Get Server Profiles   param=?filter="'name'=='${PROFILES[${x}]}'"
    \    Should Be Equal   ${profile_resp['total']}   ${1}   msg=Response body total is not as expected.
	\   ${profile_members}   Set Variable   ${profile_resp['members'][0]}
	\   Run Keyword If  "${profile_members['status']}" == "Critical"   Append To List   ${PROFILE_LIST}    ${profile_members}
	Run Keyword If  "${PROFILE_LIST}" != "${null}"   Unassign reassign the required profiles    ${PROFILE_LIST}

Get Interconnect IP Address Directly From ICM
    [Documentation]    Fetches interconnect IP address directly from ICM
    [Arguments]    ${encSN}   ${icmName}   ${IP_Type}   ${iface}=eth0   ${timeout}=15m   ${userName}=root   ${password}=UnoVista
    ${icmBay} =   Fetch From Right   ${icmName}   ${SPACE}
    ${encICMPasswd} =   Get Interconnect OneView Credential   ${encSN}   ${icmBay}
    ${Ipv6_Addr} =    set variable  ${encICMPasswd['${encSN}_${icmBay}']['ipv6LinkLocal']}
    Return From Keyword If   '${IP_Type}'=='IPV6'   ${Ipv6_Addr}   
    Open Connection   ${Ipv6_Addr}%${iface}   timeout=${timeout}
    Login   ${userName}   ${password}
    Write   udhcpc -i eth0
    Write    ${\n}
    Read
    ${o} =   Read Until Regexp   [\#]
    close connection
    ${cmd_output} =    Get Regexp Matches    ${o}    Lease\\s+of\\s+\\d+\\.\\d+\\.\\d+.\\d+
    ${Ipv4_Addr} =   Fetch From Right   ${cmd_output[0]}   ${SPACE}
    [Return]   ${Ipv4_Addr}


Blade power control
    [Documentation]   Performs power control operation for a given blade URI
    [Arguments]     ${serverUri}   ${wait_task_timeout}=60m   ${wait_task_interval}=2s
    ${body} =   Create Dictionary   powerState=${powerState}
    ...                             powerControl=${powerControl}
    ${resp} =   Fusion Api Edit Server Hardware Power State   body=${body}   uri=${serverUri}
    ${statusCode} =   Check Response For Error   ${resp}
    ${task} =   Run Keyword If   ${statusCode} == ${202}   fusion_api_appliance_setup.Wait For Task   ${resp}   timeout=${wait_task_timeout}   interval=${wait_task_interval}
    ...                   ELSE   Fail   msg=Asynchronous task returned status code ${resp['status_code']}.
    Check Asynchronous Task Response For Error   ${task}

################
# iPDU
################
Perform iPDU Outlet Control
    [Documentation]   Accepts dictionary of power control data for the iPDU power control operation. Data is in the format of <IP>:<XML File> key-value pair. This keyword will iterates over the dictionary of data for the IP and XML file to feed into iPDU.
    [Arguments]   ${power_control_data}   ${port}=50443
    :FOR   ${ipAddr}   IN   @{power_control_data.keys()}
    \   Send iPDU Outlet Control   ${ipAddr}   ${power_control_data['${ipAddr}']}
