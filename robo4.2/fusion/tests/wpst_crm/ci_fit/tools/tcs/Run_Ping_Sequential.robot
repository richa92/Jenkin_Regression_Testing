*** Settings ***
Documentation        Run sequential ping for both north-south and east-west using fping.
...                  This script will accept a pre-generated IP list file or generate one from the HA file for north-south and individual servers HA file for the east-west.
...                  All of these are sequential bidirectional pings.
...                  Example:
...                          time pybot -d /tmp/logs/ping_sequential -LTRACE -V /root/ci-fit/config_files/robustness/Eagle62-63_robustness_data_variable.py Run_Ping_Sequential.robot
...                          time pybot -d /tmp/logs/Ping -LTRACE -V /root/ci-fit/config_files/robustness/Eagle62-63_robustness_data_variable.py -vVERBOSE_PING:-q Run_Ping_Sequential.robot
...                  Optional Arguments:
...                          CYCLES: Number of cycles you want the script to run sequential pings. Default: 1
...                          FPING_HOST_IP: To specify a remote host to run the ping from instead of local TCS. This may require FPING_HOST_USERNAME and FPING_HOST_PASSWORD to be set. Default: None
...                          IP_LIST_FILE: To specify an IP file for ping. If the file specified does not exists, the script will generate it based on the HA file you defined in data file or -vHA_FILE. Default: /tmp/.ip.lst
...                          BUILD_PROFILE_HA_FILE: Accepts boolean value to tell the script to generate server profiles HA files. When this is set to True, it also forces the script to regenerates IP_LIST_FILE. Default: False
...                          PROFILES_HA_FILES_DIR: To specify a directory for all the server profiles HA files. Default: ./profiles_ha_files
...                          VERBOSE_PING: Set this to -q to run ping in quiet mode. Default: ${EMPTY} which is an empty string ("")
...                          CLEAR_PING_LOGS: Purge all existing ping logs before starting ping. Default: False
...                  Optional Data Variable:
...                          NO_PING_SOURCE: List of profiles that we don't run ping source (these will be ping targets though). To set this, you will have to either edit the script or set it in your data file. Default: @{EMPTY}
...                  Requirements:
...                          fping: It must be installed in the server either from source or binary copy (I tried the latter in RHEL7.x from RHEL6.x binary and it worked).
...                          fping.sh: Must be in the server's /root/tools/scripts (or SERVER_SCRIPTS_DIR) directory.A
...                  To stop the script cleanly, create a file in the TCS /tmp/.stop_script (or touch /tmp/.stop_script)

Variables           ../../tests/robustness/resources/data_variables.py
Resource            ../../tests/robustness/resources/common.robot
Library             ../../tests/robustness/resources/robustness-helper.py
Library             OperatingSystem
Library             String
Library             SSHLibrary

*** Variables ***
${CYCLES}                       1
${FPING_HOST_IP}                ${Null}
${FPING_HOST_USERNAME}          root
${FPING_HOST_PASSWORD}          rootpwd
${IP_LIST_FILE}                 /tmp/.ip.lst
${BUILD_PROFILE_HA_FILE}        ${False}
${PROFILES_HA_FILES_DIR}        ./profiles_ha_files
${VERBOSE_PING}                 ${EMPTY}
${CLEAR_PING_LOGS}              ${False}
${STOP_SCRIPT}                  /tmp/.stop_script
${NO_PING_SOURCE}               @{EMPTY}

*** Test Cases ***
Run Fping
    Variable File Should Be Passed
    :FOR   ${x}  IN RANGE   1   ${CYCLES}+1
    \   Exit Test When Flag File Exists   flag_file=${STOP_SCRIPT}
    \   Log   \n Cycle: ${x} of ${CYCLES}   console=${True}
    \   Run Keyword If   "${FPING_HOST_IP}" == "${Null}"   Run Fping From Current Host   quietPing=${VERBOSE_PING}   generated_sp_ha_files_dir=${PROFILES_HA_FILES_DIR}
    \   ...       ELSE   Run Fping Via SSH   ${FPING_HOST_IP}   ${FPING_HOST_USERNAME}   ${FPING_HOST_PASSWORD}   quietPing=${VERBOSE_PING}

*** Keywords ***
Run Fping From Current Host
    [Documentation]   Run fping wrapper from the current host.
    [Arguments]   ${generated_sp_ha_files_dir}=./profiles_ha_files   ${quietPing}=${EMPTY}
    Run Fping In Servers   generated_sp_ha_files_dir=${generated_sp_ha_files_dir}   quietPing=${quietPing}
    # North-South ping from TCS
    ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${IP_LIST_FILE}
    Run Keyword If   "${returnStatus}" == "PASS" and ${BUILD_PROFILE_HA_FILE} is not ${True}   Log To Console   \n IP file ${IP_LIST_FILE} found, using it for ping...   no_newline=${True}
    ...       ELSE   Run Keywords   Log To Console   \n Generating IP file ${IP_LIST_FILE} from HA File...   AND   Generate IP File From HA File   filename=${IP_LIST_FILE}
    Run Keyword If   '${CLEAR_PING_LOGS}' == '${True}'   Run Keywords   Log To Console   Clearing existing ping logs...   no_newline=${True}   AND   Remove Directory   ./logs   recursive=True   AND   Log To Console   [OK]
    Log To Console   \nStarting north-south ping (from TCS)...   no_newline=${True}
    ${exitStatus}   ${output} =   Run And Return Rc And Output   ./fping.sh ${quietPing} -m seqPing ${IP_LIST_FILE}
    Log Sequential Ping Output To Console   ${output}   ${exitStatus}
    Run Keyword If   ${exitStatus} == 1  Log To Console   Completed north-south ping (from TCS)!
    ...    ELSE IF   ${exitStatus} == 0  Fail  msg=Check the sequential ping log for more info.
    ...    ELSE   Fail   msg=Unable to perform sequential ping, please check log for more info.

Run Fping Via SSH
    [Documentation]   Ssh to a host and run fping.
    [Arguments]   ${remoteHost}   ${remoteUser}   ${remotePasswd}   ${quietPing}=${EMPTY}   ${generated_sp_ha_files_dir}=./profiles_ha_files
    Run Fping In Servers   generated_sp_ha_files_dir=${generated_sp_ha_files_dir}   quietPing=${quietPing}
    Open Connection And Login To Host   ${remoteHost}   ${remoteUser}   ${remotePasswd}
    ${output}   ${stderr}   ${rc} =   Execute Command   test -f ${IP_LIST_FILE}   return_stderr=True   return_rc=True
    Run Keyword If   '${rc}' == '0' and ${BUILD_PROFILE_HA_FILE} is not ${True}   Log To Console   \n IP file ${IP_LIST_FILE} found, using it for ping...   no_newline=${True}
    ...       ELSE   Run Keywords   Log To Console   \n Generating IP file ${IP_LIST_FILE} from HA File...   no_newline=${True}   AND   Generate IP File From HA File   filename=${IP_LIST_FILE}
    # Transfer the generated file to remote host
    Put File To Remote Host   ${remoteHost}   ${remoteUser}   ${remotePasswd}   ${IP_LIST_FILE}   ${IP_LIST_FILE}   keepConnection=${True}
    Log To Console   Clearing existing ping logs...   no_newline=${True}
    ${output}   ${stderr}   ${rc} =   Run Keyword If   '${CLEAR_PING_LOGS}' == '${True}'   Execute Command   rm -rf ./logs   return_stderr=True   return_rc=True
    Run Keyword If   ${rc} == ${0}   Log To Console   [OK]
    ...    ELSE IF   '${rc}' != '${Null}'   Run Keywords   Log To Console   [Failed: ${stderr}]   AND   Fail   msg=Unable to delete existing ping logs.
    ${output}   ${stderr}   ${rc} =   Execute Command   ${TOPLEVEL_DIR}/tests/wpst_crm/ci_fit/tools/tcs/fping.sh ${quietPing} -m seqPing ${IP_LIST_FILE}   return_stderr=True   return_rc=True
    Log Sequential Ping Output To Console   ${output}   ${rc}

Generate IP File From HA File
    [Documentation]   Parses the IP address from your HA File and redirect them to the specified filename (default: /tmp/.ip.lst).
    [Arguments]   ${filename}=/tmp/.ip.lst
    Run   cut -d " " -f8 ${HA_FILE} > ${filename}

Log Sequential Ping Output To Console
    [Documentation]   Log sequential ping output to console
    [Arguments]   ${output}   ${exitStatus}
    ${outputList} =   Split String   ${output}   ${\n}
    :FOR   ${o}   IN   @{outputList}
    \   Log To Console   ${o}
    Run Keyword If   ${exitStatus} == ${0}   Fail   msg=Ping loss found!

Transfer Server Profiles HA Files And Ping
    [Documentation]   Transfer server profiles HA files to servers and starts ping.
    [Arguments]   ${sourceHAFilesDir}   ${remoteUser}=root   ${remotePassword}=rootpwd   ${quietPing}=""
    ${profiles} =   OperatingSystem.List Directory   ${sourceHAFilesDir}
    :FOR   ${profile_name}   IN   @{profiles}
    \   Log To Console   \nSearching pingable IP for server profile: ${profile_name}...   no_newline=${True}
    \   ${pingable_ip} =   get_server_reachable_ip   ${HA_FILE}   server_profile=${profile_name}
    \   Log To Console   [Found: ${pingable_ip}]
    \   Log To Console   Transferring ${profile_name} HA file...   no_newline=${True}
    \   Put File To Remote Host   ${pingable_ip}   ${remoteUser}   ${remotePassword}   ${sourceHAFilesDir}/${profile_name}   ${SERVER_SCRIPTS_DIR}/${profile_name}   keepConnection=${True}
    \   Log To Console   [Done]
    \   ${output}   ${stderr}   ${rc} =   Execute Command   test -f ${IP_LIST_FILE}   return_stderr=True   return_rc=True
    \   Run Keyword If   ${rc} == ${0} and ${BUILD_PROFILE_HA_FILE} is not ${True}   Log To Console   IP file ${IP_LIST_FILE} found, using it for ping...   no_newline=${True}
    \   ...       ELSE   Log To Console   Generating IP file ${IP_LIST_FILE} from server profile HA file...   no_newline=${True}
    # generate IP file in the server using profile HA file
    \   ${output}   ${stderr}   ${rc} =   Run Keyword If   ${rc} == ${1} or ${BUILD_PROFILE_HA_FILE} is ${True}   Execute Command   cut -d " " -f8 ${SERVER_SCRIPTS_DIR}/${profile_name} > ${IP_LIST_FILE}   return_stderr=True   return_rc=True
    \   Log To Console   [OK]
    \   Log To Console   Clearing existing ping logs...   no_newline=${True}
    \   ${output}   ${stderr}   ${rc} =   Run Keyword If   '${CLEAR_PING_LOGS}' == '${True}'   Execute Command   rm -rf ./logs   return_stderr=True   return_rc=True
    \   Run Keyword If   ${rc} == ${0}   Log To Console   [OK]
    \   ...    ELSE IF   '${rc}' != '${Null}'   Run Keywords   Log To Console   [Failed: ${stderr}]   AND   Fail   msg=Unable to delete existing ping logs.
    \   ${contains} =   Evaluate   '${profile_name}' in ${NO_PING_SOURCE}
    \   Run Keyword If   ${contains} == True   Run Keywords   Log To Console   Skipping "${profile_name}" as ping source...   AND   Continue For Loop
    \   Log To Console   Starting north-south, east-west ping...   no_newline=${True}
    \   ${output}   ${stderr}   ${rc} =   Execute Command   ${SERVER_SCRIPTS_DIR}/fping.sh ${quietPing} -m seqPing ${IP_LIST_FILE}   return_stderr=True   return_rc=True
    \   Log Sequential Ping Output To Console   ${output}   ${rc}
    \   Run Keyword If   ${rc} == 1  Log To Console   Completed north-south, east-west ping!
    \   ...    ELSE IF   ${rc} == 0  Fail  msg=Check the sequential ping log for more info.
    \   ...    ELSE   Fail   msg=Unable to perform sequential ping, please check log for more info.

Run Fping In Servers
    [Documentation]   Starts ping in the servers for north-south and east-west.
    [Arguments]   ${generated_sp_ha_files_dir}=./profiles_ha_files   ${quietPing}=${EMPTY}
    Run Keyword If   '${BUILD_PROFILE_HA_FILE}' == '${True}'   Run Keywords   Remove Directory   ${generated_sp_ha_files_dir}   recursive=True   AND   Create Directory   ${generated_sp_ha_files_dir}   AND   Generate Server Profiles HA Files   ${HA_FILE}   AND   Transfer Server Profiles HA Files And Ping   ${generated_sp_ha_files_dir}   quietPing=${quietPing}
    ...       ELSE   Transfer Server Profiles HA Files And Ping   ${generated_sp_ha_files_dir}   quietPing=${quietPing}
