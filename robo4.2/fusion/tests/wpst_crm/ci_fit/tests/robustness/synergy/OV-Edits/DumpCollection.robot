*** Settings ***
Documentation       DumpCollection.robot- performs Creating Potash dump,dmesg,OV dump and LE dump and copying cidebug logs,var/log/messages along with the created dumps into the folder in TCS.
...     TAGS:          CREATE_HAFNIUM_DUMP, APPLIANCE_LOGS, DRIVER_INFO, DMESG, VAR_LOG_MESSAGE, CREATE_OV_DUMP, CREATE_LE_DUMP
...					   CREATE_HAFNIUM_DUMP - Creates Potash Dump
...					   APPLIANCE_LOGS     - Copies Appliance Logs To TCS
...					   DRIVER_INFO        - Copies Driver Info To TCS
...                    DMESG              - Copies Dmesg To TCS
...                    VAR_LOG_MESSAGE    - Copies Var/log/messages To TCS
...					   CREATE_OV_DUMP     - Creates And Download The Appliance Dump To TCS
...					   CREATE_LE_DUMP     - Creates And Download The LE Dump To TCS
...                    Example workflow :
...                              pybot -V /root/ci-fit/config_files/OV-Edit_data_variables.py -v Log_Dir:/data/logs/alldumps/ -v LEdump:yes -v OVdump:yes -v server_ip:"172.xx.x.xx,172.xx.x.xx" -v APPLIANCE_IP:15.186.9.xx -v HAFNIUM_MODEL:'Virtual Connect SE 40Gb F8 Module for Synergy' DumpCollection.robot
...            Required argument:
...            -V /root/ci-fit/config_files/OV-Edit_data_variables.py
...			   The above template for this file is available in
...			   fusion/tests/wpst_crm/ci_fit/tests/robustness/resources/ov_edits_data_variables_template.py
...                     Optional arguments:
...                         Default HAFNIUM_DUMP_SLEEP_TIME: 5m, to override it use -v HAFNIUM_DUMP_SLEEP_TIME:<value like 10m>
...                         Default HAFNIUM_MODEL: Null, to override it use -v HAFNIUM_MODEL:'name of the module'
...                         TCS_HAFNIUM_SSH_INTERFACE: Interface we use to SSH to Hafnium using IPv6 Link Local Address. Default: eth0

Variables           ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Library             Collections
Library             ../../resources/robustness-helper.py

Suite Setup         Suite Setup

*** Variables ***
${Log_Dir}                          ${CURDIR}    #Support Dump will be saved in Current Folder in TCS
${Potash_Dump_cmd}                  su - OneView
${Potash_Dump_cmd1}                 dump tech
${Grep_Interface}                   ls   /etc/sysconfig/network-scripts/ | grep -E ""eth[0-9]\\{1,\\}"|en"
${HAFNIUM_DUMP_SLEEP_TIME}          5m
${USE_HAFNIUM_RESOURCE_IPV4}        True
${OVdump}                           no
${LEdump}                           no
${server_profile_name}              None
${HAFNIUM_MODEL}                    ${Null}
${TCS_HAFNIUM_SSH_INTERFACE}        eth0

*** Test Cases***
Login To Hafnium And Create Dump
    [Documentation]    Create hafnium dump and copy to TCS.
    [Tags]    CREATE_HAFNIUM_DUMP
    ${Alias}    Create List
    Set Suite Variable    ${Alias}
    ${resp} =   Fusion Api Get Interconnect
    :FOR   ${icm}   IN   @{resp['members']}
    \   Continue For Loop If   '${icm['model']}' != '${HAFNIUM_MODEL}'
    \   ${USE_HAFNIUM_RESOURCE_IPV4} =   Get Variable Value   ${USE_HAFNIUM_RESOURCE_IPV4}
    \   ${HAFNIUM_IP} =   Run Keyword If   ${USE_HAFNIUM_RESOURCE_IPV4} is ${True}   common.Get Interconnect IP Address From OneView   ${icm['ipAddressList']}   Ipv4Dhcp
    \   ...                     ELSE   Get Interconnect IP Address From OneView   ${icm['ipAddressList']}   Ipv6Dhcp
    \   ${HAFNIUM_IP} =   Run Keyword If   '${HAFNIUM_IP}' == '${Null}'   Get Interconnect IP Address From OneView   ${icm['ipAddressList']}   Ipv6LinkLocal
    \   ...                     ELSE   Set Variable   ${HAFNIUM_IP}
    \   Continue For Loop If   "${HAFNIUM_IP}" == "None"
    \   ${icmname}    Get From Dictionary   ${icm}    name
    \   Append To List    ${Alias}    ${icmname}
    \   ${llAddr} =   Get Lines Matching Regexp   ${HAFNIUM_IP}   ^fe80:   partial_match=true
    \   Run Keyword If   '${llAddr}' == '${EMPTY}'   SSHLibrary.Open Connection    ${HAFNIUM_IP}    alias=${icmname}
    \   ...       ELSE   SSHLibrary.Open Connection    ${HAFNIUM_IP}%${TCS_HAFNIUM_SSH_INTERFACE}    alias=${icmname}
    \   SSHLibrary.Login     ${HAFNIUM_USERNAME}     ${HAFNIUM_PASSWORD}
    \   SSHLibrary.Write    ${Potash_Dump_cmd}
    \   ${o} =   Read Until Regexp   OneView[\>|\#]
    \   SSHLibrary.Write    ${Potash_Dump_cmd1}
    Run Keyword If   "${HAFNIUM_IP}" == "${Null}"   Fail   msg=Unable to get both IPv4 and IPv6 address from the resource data for ${icm['name']}.
    Sleep  ${HAFNIUM_DUMP_SLEEP_TIME}
    Getting Potash Dump    ${Alias}

Get CI Debug Logs And Copying Logs From OV To TCS
	[Documentation]    Copying cidebug logs from OV to TCS.
	[Tags]    APPLIANCE_LOGS
        ${sanitizedIP} =   Get Variable Value   ${APPLIANCE_IP}
        ${sanitizedIP} =   Remove String Using Regexp   ${sanitizedIP}   (\\[|\\])
        ${llAddr} =   Get Lines Matching Regexp   ${sanitizedIP}   ^fe80:   partial_match=true
        Run Keyword If   '${llAddr}' == '${EMPTY}'   SSHLibrary.Open Connection  ${sanitizedIP}
        ...       ELSE   SSHLibrary.Open Connection  ${sanitizedIP}%${TCS_HAFNIUM_SSH_INTERFACE}
	SSHLibrary.Login     ${FUSION_SSH_USERNAME}     ${FUSION_SSH_PASSWORD}
	Write       resize
	Write    cd /ci/logs
    ${o}=     Read until    logs]#
	SSHLibrary.Write    ls | grep ciDebug
	${cidebug_log_list}     Read
    ${cidebug_logs} =   Get Lines Matching Regexp   ${cidebug_log_list}   ciDebug.*   partial_match=true
    ${cidebug_log} =   Split String   ${cidebug_logs}   ${\n}
	${cidebug_log_len}    Get Length   ${cidebug_log}
	Run Keyword And Ignore Error    SSHLibrary.Get File    /ci/logs/ciDebug.*     ${Log_Dir}//${Prefix}/
    ${Count}=    OperatingSystem.Count Files In Directory    path=${Log_Dir}//${Prefix}    pattern=ciDebug.*
    Run Keyword If    '${count}'!= '${cidebug_log_len}'   Fail    ELSE    LOG   \n CiDebug logs copied successfully    console=${True}

Login To Server And Copying Driver Details To TCS
	[Documentation]   Copying driver details to TCS
	[Tags]    DRIVER_INFO
	${split_server_ip}=    String.Split String    ${server_ip}    ,
	${sever_ip_length}=    Get Length    ${split_server_ip}
	:FOR	${x}	IN RANGE	0	${sever_ip_length}
	\   Exit For Loop If    '${server_ip}'=='${None}'
	\   Open Connection      ${split_server_ip[${x}]}
	\   Login     ${SERVER_USERNAME}	     ${SERVER_PASSWORD}
	\   ${server_profile_name}    Getting Server Profile Name    ${split_server_ip[${x}]}
	\	${stdout}=	Execute Command		${Grep_Interface}    return_stdout=True	return_rc=False
	\   ${output} =   Get Lines Matching Regexp    ${stdout}    ifcfg    partial_match=true
    \   ${interface_list} =   Split String   ${output}   ${\n}
    \	${interface}   Get From List    ${interface_list}   0
	\   ${interfcae_name}    Fetch From Right   ${interface}     -
    \	${driver_details}=	Execute Command    ethtool -i ${interfcae_name}
	\   Collecting Data From Server    ${server_profile_name}    ${driver_details}   ethtool.txt

Login To Server And Copying Dmesg To TCS
	[Documentation]   Copying dmesg from server to TCS
	[Tags]    DMESG
	${split_server_ip}=    String.Split String    ${server_ip}    ,
	${sever_ip_length}=    Get Length    ${split_server_ip}
	:FOR	${x}	IN RANGE	0	${sever_ip_length}
	\   Exit For Loop If    '${server_ip}'=='${None}'
	\   Open Connection      ${split_server_ip[${x}]}
	\   Login     ${SERVER_USERNAME}	     ${SERVER_PASSWORD}
	\   ${server_profile_name}    Getting Server Profile Name    ${split_server_ip[${x}]}
	\   ${dmesg_output}    Execute Command    dmesg
	\   Collecting Data From Server    ${server_profile_name}	${dmesg_output}    dmesg.txt

Login To Server And Copying Var/log/messages To TCS
	[Documentation]   Copying var/log/messages from server to TCS
	[Tags]    VAR_LOG_MESSAGE
	${split_server_ip}=    String.Split String    ${server_ip}    ,
	${sever_ip_length}=    Get Length    ${split_server_ip}
	:FOR	${x}	IN RANGE	0	${sever_ip_length}
	\   Exit For Loop If    '${server_ip}'=='${None}'
	\   Open Connection      ${split_server_ip[${x}]}
	\   Login     ${SERVER_USERNAME}	     ${SERVER_PASSWORD}
	\   ${server_profile_name}    Getting Server Profile Name    ${split_server_ip[${x}]}
	\	Run Keyword And Ignore Error    SSHLibrary.Get File    /var/log/messages
	\	${Count}=    OperatingSystem.Count Files In Directory    path=.    pattern=messages
    \	Run Keyword If    ${Count}==0    Log  Did not find any /var/log/messages   WARN   console=${True}
    \	Pass Execution If    ${Count}==0    Did not find any var/log/messages
    \	${Files}    OperatingSystem.List Files In Directory    path=.    pattern=messages
    \	Should Not Be Empty    ${Files}
    \	...    msg=Did not find any var/log/messages
	\   Move File    ${Files[0]}   ${server_profile_name}-messages.txt
    \   Move File    ${server_profile_name}-messages.txt    ${Log_Dir}/${Prefix}

Creating OV Support Dump And Download To TCS
    [Documentation]   Creating OV support dump.
	[Tags]    CREATE_OV_DUMP
	Run Keyword If   '${OVdump}' =='yes'    common.Create OV Support Dump And Download

Creating LE Support Dump And Download To TCS
    [Documentation]   Creating LE support dump.
	[Tags]    CREATE_LE_DUMP
    Run Keyword If   '${LEdump}' =='yes'    common.Create LE Support Dump And Download   ${LE}
	Log    All downloaded dumps will save with current date and time in ${Log_Dir}/${prefix}    console=${True}

*** Keywords ***
Getting Potash Dump
	[Documentation]   Getting potash dump.
	[Arguments]    ${Alias}
	${alias_length} = 	Get Length	${Alias}
	:FOR	${x}	IN RANGE	0	${alias_length}
 	\	SSHLibrary.Switch Connection    ${Alias[${x}]}
	\	SSHLibrary.Read Until    Tech-support
	\	Run Keyword And Ignore Error    SSHLibrary.Get File    /tmpfs/tmp/tech-support_*
    \	${Count}=    OperatingSystem.Count Files In Directory    path=.    pattern=tech-support_*
    \	Run Keyword If    ${Count}==0    Log    \nDid not find any tech-support logs   WARN   console=${True}
    \	Pass Execution If    ${Count}==0    msg=Did not find any tech-support logs
	\	${Files}    OperatingSystem.List Files In Directory    path=.    pattern=tech-support_*
    \	Should Not Be Empty    ${Files}
    \	...    msg=Did not find any tech-support logs
    \   Move File    ${Files[0]}    ${Log_Dir}/${Prefix}

Getting Server Profile Name
    [Documentation]    Fetching server profile name.
	[Arguments]    ${server_ip}
	Open Connection      ${server_ip}
	Login     ${SERVER_USERNAME}	     ${SERVER_PASSWORD}
	${system_serial_number}    Execute Command    dmidecode -s system-serial-number
	${serial_number}  Fetch From Right   ${system_serial_number}   \n
	${server_Profile_name}    Getting Server Info   ${serial_number}    ${server_ip}
	[Return]     ${server_profile_name}

Getting Server Info
	[Documentation]   Getting server info
	[Arguments]    ${system_serial_number}    ${server_ip}
	${profiles} =   Fusion Api Get Server Profiles
    ${server_profiles} =     Get From Dictionary     ${profiles}    members
	${sever_length}=    Get Length    ${server_profiles}
	:FOR	${x}	IN RANGE	0	${sever_length}
	\    ${serial_num}    Get From Dictionary    ${server_profiles[${x}]}    serialNumber
	\    ${res}    Get Lines Matching Pattern	   ${serial_num}    ${system_serial_number}    	case_insensitive=True
	\    ${server_profile_name}    Run Keyword If    '${res}' != ''    Get From Dictionary    ${server_profiles[${x}]}    name
	\   ...    ELSE    Continue For Loop
	\	Run Keyword If    '${server_profile_name}' != '${null}'   Exit For Loop
	Run Keyword If    '${server_profile_name}' == '${None}'    Log    Unable to find serial number "${system_serial_number}" in the current list of server profiles in OneView.    WARN    console=${True}
	${profile_name}   Run Keyword If    '${server_profile_name}' != '${None}'   Set Variable   ${server_profile_name}
	...   ELSE   Set Variable    ${server_ip}
	[Return]    ${profile_name}

Collecting Data From Server
    [Documentation]    Collecting data from server to TCS
    [Arguments]    ${server_profile}    ${Command_output}    ${file_name}
    Append To File    ${Server_Profile}-${file_name}    ${Command_output}
    Run Keyword And Ignore Error    SSHLibrary.Get File   ${Server_Profile}-${file_name}
    ${Count}=    OperatingSystem.Count Files In Directory    path=.    pattern=${Server_Profile}-${file_name}
    Run Keyword If    ${Count}==0    Log  Did not find any ${file_name}   WARN   console=${True}
    Pass Execution If    ${Count}==0    Did not find any ${file_name}
    ${Files}    OperatingSystem.List Files In Directory    path=.    pattern=${Server_Profile}-${file_name}
    Should Not Be Empty    ${Files}
    ...    msg=Did not find any dmesg
    Move File    ${Files[0]}    ${Log_Dir}/${Prefix}

Creating Directory With Current Date And Time
    [Documentation]    Creating directory with current date and time in TCS.
    [Tags]   CREATE_HAFNIUM_DUMP   APPLIANCE_LOGS   DRIVER_INFO   DMESG   VAR_LOG_MESSAGE   CREATE_OV_DUMP   CREATE_LE_DUMP
    # Prefix files with date/time stamp
    ${yyyy}    ${mmon}    ${dd}    ${hh}    ${mmin}    ${ss}    Get Time    year,month,day,hour,min,sec
    ${Prefix}    Set Variable    ${yyyy}-${mmon}-${dd}-${hh}-${mmin}${ss}-
    Set Suite Variable    ${Prefix}
    Create Directory    ${Log_Dir}//${Prefix}
    ${resp} =    Fusion Api Get Appliance Interfaces
    ${hostname} =   Get From Dictionary    ${resp['applianceNetworks'][0]}    hostname
    ${OVfile}    Set Variable    ${hostname}-CI-${prefix}.sdmp
    ${OV_dump_file_Dir}    Set Variable    ${Log_Dir}//${Prefix}
    ${OV_support_dump_file}     Set Variable    ${OV_dump_file_Dir}/${OVfile}
    ${LEfile}    Set Variable    ${hostname}-LI-${prefix}.sdmp
    ${LE_dump_file_Dir}    Set Variable    ${Log_Dir}//${Prefix}
    ${LE_dump_file}     Set Variable    ${LE_dump_file_Dir}/${LEfile}
    Set Suite Variable    ${OV_dump_file_Dir}
    Set Suite Variable	  ${OV_support_dump_file}
    Set Suite Variable    ${LE_dump_file_Dir}
    Set Suite Variable	  ${LE_dump_file}

Suite Setup
    [Documentation]   Authenticate to OneView and set necessary variables and directory.
    Authenticate And Set Login
    Creating Directory With Current Date And Time
