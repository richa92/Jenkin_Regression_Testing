*** Settings ***
Documentation		read_block10_data_snmpget.robot - Check subordinate ICMs has block 10 data and the subordinate ICM is responding to SNMP requests by running SNMP-GET commands on OneView CLI prompt
...					Tags: READ_BLOCK10_DATA
...					READ_BLOCK10_DATA - Reading block 10 data to use in verifying FW version and domain role status of subordinate interconnect module using snmp command
...					Example Workflow:
... 					pybot -T -d /tmp/logs/cerner_check -LTRACE -V /root/ci-fit/config_files/eagleXX_robustness_data_variable.py -v Appliance_IP:15.186.X.XX read_block10_data_snmpget.robot
...                 Required arguments:
...                         -V /root/ci-fit/config_files/eagleXX_robustness_data_variable.py
...                 Pre-requisties:
...                         Snmp utils packages should installed in TCS
...                 To change interface use to access ICM via snmp (default: eth0), use -vINTERFACE:eth1

Variables           ../../tests/robustness/resources/data_variables.py
Resource            ../../../crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../tests/robustness/resources/common.robot
Library            ../../tests/robustness/resources/robustness-helper.py
Library             Collections

Suite Setup         Authenticate And Set Login

*** Variables ***
${FUSION_IP}                            ${APPLIANCE_IP}
${INTERFACE}                            eth0
${FW_VERSION_OOID}                      ${Null}
${FW_VERSION_OOID_POTASH}               .1.3.6.1.4.1.11.5.7.5.8.1.81.1.3.0
${FW_VERSION_OOID_NITRO}                .1.3.6.1.4.1.11.5.7.5.9.1.81.1.3.0
${STACKING_DOMAIN_STATUS_OOID}          ${Null}
${STACKING_DOMAIN_STATUS_OOID_POTASH}   .1.3.6.1.4.1.11.5.7.5.8.1.99.1.4.0
${STACKING_DOMAIN_STATUS_OOID_NITRO}    .1.3.6.1.4.1.11.5.7.5.9.1.99.1.4.0

*** Test Cases ***
Using SNMP command to check FW version and domain role status of subordinate potash module
	[Documentation]   Checks FW version and domain role status of subordinate potash module
	[Tags]    READ_BLOCK10_DATA
        Set Suite Variable   ${ICM_MODEL}   ${HAFNIUM_MODEL}
	${resp}    Get All Subordinate Interconnect Module
	:FOR   ${x}  IN  @{resp}
	\    ${encICMPasswd} =   Get Interconnect OneView Credential   ${x['Enclosure']}   ${x['Bay_No']}
	\    Log To Console    \n Comparing version from snmpget output to that of OneView
        \    ${FW_VERSION_OOID}   ${STACKING_DOMAIN_STATUS_OOID} =   Run Keyword If   "${x['icm_model']}" == "${NITRO}"   Set Variable   ${FW_VERSION_OOID_NITRO}   ${STACKING_DOMAIN_STATUS_OOID_NITRO}
        \    ...                           ELSE IF   "${x['icm_model']}" == "${POTASH}"   Set Variable   ${FW_VERSION_OOID_POTASH}   ${STACKING_DOMAIN_STATUS_OOID_POTASH}
        \    ...                           ELSE   Fail   msg=Unable to find OOID for your interconnect model: ${x['icm_model']}
	\    ${rc}    ${out} =   Run And Return Rc And Output    snmpget -v3 -l authPriv -u ${encICMPasswd['${x['Enclosure']}_${x['Bay_No']}']['User']} -A ${encICMPasswd['${x['Enclosure']}_${x['Bay_No']}']['Password']} -a SHA -x AES -X ${encICMPasswd['${x['Enclosure']}_${x['Bay_No']}']['Password']} udp6:[${encICMPasswd['${x['Enclosure']}_${x['Bay_No']}']['ipv6LinkLocal']}%${INTERFACE}]/161 ${FW_VERSION_OOID}
	\    ${version}    Run Keyword If   ${rc} == 0    Get Regexp Matches    ${out}    .*\\:\\s"(.*)".*   1
	\    ...                    ELSE    FAIL    msg=snmpget has non-zero return code (${rc}). Error:${out}
	\    ${ver}    Fetch From Left  ${version[0]}    ${SPACE}
	\    ${sub_version} =   Replace String Using Regexp  	${ver}  -    .
	\    Should Be Equal     ${sub_version}     ${x['FW_version']}     msg=Mismatch in Firmware version of sub-ordinate module
	\    Log To Console    \n Checking stacking domain role status
	\    ${rc}   ${stdout} =   Run And Return Rc And Output    snmpget -v3 -l authPriv -u ${encICMPasswd['${x['Enclosure']}_${x['Bay_No']}']['User']} -A ${encICMPasswd['${x['Enclosure']}_${x['Bay_No']}']['Password']} -a SHA -x AES -X ${encICMPasswd['${x['Enclosure']}_${x['Bay_No']}']['Password']} udp6:[${encICMPasswd['${x['Enclosure']}_${x['Bay_No']}']['ipv6LinkLocal']}%${INTERFACE}]/161 ${STACKING_DOMAIN_STATUS_OOID}
	\    ${node}  Run Keyword If   ${rc} == 0     Get Regexp Matches    ${stdout}    .*(\\d)   1
	\    ...                ELSE    FAIL    msg=snmpget has non-zero return code (${rc}). Error: ${stdout}
	\    Run Keyword If   '${node[0]}' == '1'    Log To Console   \n Stacking domain role status using FS_RM_NODE_STATE is in ACTIVE node...
	\    ...     ELSE IF    '${node[0]}' == '2'     Log To Console   \n Stacking domain role status using FS_RM_NODE_STATE is in Subordinate node...
	\    ...     ELSE    FAIL    msg=Unexpected stacking domain role status using FS_RM_NODE_STATE: ${node[0]}
