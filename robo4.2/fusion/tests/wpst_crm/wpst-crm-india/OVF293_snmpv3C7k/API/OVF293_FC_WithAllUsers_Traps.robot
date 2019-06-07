*** Settings ** *
Documentation        Feature Test:  OVF293 SNMPv3
...                  This set of test cases is to verify the feature SNMPv3 related testing
...
Variables           data_variables.py
Resource            ../../../resources/resource.txt
Library             Collections
Library             json
Library             OperatingSystem
Library             Selenium2Library
Library             FusionLibrary
Library             BuiltIn

*** Variables ** *
${SSH_PASS}                     hpvse1
${DataFile}                     ./OVAData.xml
${APPLIANCE_IP}                192.168.148.25
${inform}                       False
${li}                            SGH411DFYA-LIG_FC
${MIB_down}             IF-MIB::linkDown
${MIB_up}               IF-MIB::linkUp
${ICM_IP}         192.168.146.59
${ICM_1}                        SGH411DFYA, interconnect 5
${OA_HOST}            192.168.144.133
${OA_USER}            Administrator
${OA_PASS}                Admin
${BAY}                1
${State_Power_Off}             Maintenance
${State_Configured}             Configured
${snmp_utils_ip}                192.168.148.49
${snmp_utils_userid}            root
${snmp_utils_password}          hpvse1
${OID_MIB}                       .1.3.6.1.6.3.15.1.2.2.1.5

*** Test Cases ***

OVF292_API_TC_00 Preconditions-Appliance Login

    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

OVF293_API_TC_155_1 User MIB Validation for AuthProto
   Execute snmpbulkwalk Command and validate for Authentication Protocols                                ${user_proto_priv_lig_fc}                     192.168.146.59                       .1.3.6.1.6.3.15.1.2.2.1.5

OVF293_API_TC_155_2 Retrieve User Name and PrivProto from MIB output and validate
   Execute snmpbulkwalk Command and validate for Privacy Protocols                                 ${user_proto_priv_lig_fc}                      192.168.146.59                      .1.3.6.1.6.3.15.1.2.2.1.8

OVF293_API_TC_156 Edit LIG with Adding one more User
    ${lig_edit}    Get LIG member    ${LIG2}
    ${lig_uri}    Get Variable Value    ${lig_edit['uri']}
    Set Global Variable    ${LIG_URI}    ${lig_uri}
    ${lig_snmp}    Edit LIG body for SNMP    ${LIG1}    ${add_lig_fc['snmpUsers']}    ${add_lig_fc['trapDestinations']}    ${add_lig_fc['v3Enabled']}
    Set To Dictionary    ${lig_edit}    eTag=
    Set To Dictionary    ${lig_edit}    snmpConfiguration=${lig_snmp}
    ${resp}    fusion_api_edit_lig    body=${lig_edit}    uri=${LIG_URI}
    Run Keyword If  '${resp['status_code']}' == '202'    Log to console  \nStatus Code: ${resp['status_code']} \nSuccessfully!! Edited the LIG for snmpV3 single user with auth & priv protocols and trap details\n
    ...    ELSE    FAIL
    ${task} =    Wait For Task     ${resp}     180 s    10 s
    ${valDict} =     Create Dictionary    status_code=${200}
    ...                                 taskState=Completed
    Validate Response    ${task}    ${valDict}
    Perform an Update From Group    ${li}    120 min        1 min

OVF293_API_TC_156_1 User MIB Validation for AuthProto
   Execute snmpbulkwalk Command and validate for Authentication Protocols                                ${user_proto_priv_lig}                     192.168.146.59                       .1.3.6.1.6.3.15.1.2.2.1.5

OVF293_API_TC_156_2 Retrieve User Name and PrivProto from MIB output and validate
   Execute snmpbulkwalk Command and validate for Privacy Protocols                                 ${user_proto_priv_lig}                      192.168.146.59                      .1.3.6.1.6.3.15.1.2.2.1.8

OVF292_API_80 Edit LI with all users and Validate Traps

    #Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Edit LI    ${li}    ${edit_li_exiting_snmp_users_auth_and_authpriv['snmpConfiguration']}
    ${li_Create_user} =    Get SNMPUSers from Data    ${edit_li_exiting_snmp_users_auth_and_authpriv['snmpConfiguration']}
    Verify SNMP Users Edit LI   ${li}    ${li_Create_user}

OVF292_API_80_1 User MIB Validation for AuthProto LI
   Execute snmpbulkwalk Command and validate for Authentication Protocols                                ${user_proto_priv_li}                     192.168.146.59                       .1.3.6.1.6.3.15.1.2.2.1.5

OVF292_API_80_2 Retrieve User Name and PrivProto from MIB output and validate LI
   Execute snmpbulkwalk Command and validate for Privacy Protocols                                 ${user_proto_priv_li}                     192.168.146.59                      .1.3.6.1.6.3.15.1.2.2.1.8


OVF292_API_80_3 Kill existing snmptrapd demon
    Kill snmptrapd demon

OVF292_API_80_4 Initiate trapd
      Open Connection               192.168.148.49
      Login                   root        hpvse1
      Sleep  2
      Set Client Configuration            timeout=16 seconds
      Write       resize
      ${output}=              Start Command                             snmptrapd -f -C -c /etc/snmp/snmptrapd.conf -Le -L f /etc/messages
      Close All Connections

OVF292_API_206_1 Uplink Ports Disable
    Uplink Ports Edit           ${downlink_disable}         ${ICM_1}
    sleep   60s
    Log to Console  \nUplink port edit completed

OVF292_API_206_2 Validate Trap received
     Validate Trap received          ${MIB_down}            ${ICM_IP}

OVF292_API_206_3 Uplink Ports Enable
    Uplink Ports Edit           ${downlink_enable}          ${ICM_1}

OVF292_API_206_4 Validate Trap received
    Validate Trap received       ${MIB_up}          ${ICM_IP}

OVF292_API_206_5 Power_Offinterconnect and verify the Recalculated Ip being updated
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    OA CLI POWEROFF    ${OA_HOST}    ${OA_USER}    ${OA_PASS}   INTERCONNECT    ${BAY}
    Log to Console  Waiting for interconnect removal  to complete
    Wait Until Keyword Succeeds    600 s    10 s    Verify Interconnect State    ${ICM_1}    ${State_Power_Off}

OVF292_API_206_6 Power_On interconnect and verify the Recalculated Ip being updated
    OA CLI POWERON    ${OA_HOST}    ${OA_USER}    ${OA_PASS}   INTERCONNECT    ${BAY}
    Log to Console  Waiting for interconnect claim process to complete
    Wait Until Keyword Succeeds    600 s    10 s    Verify Interconnect State    ${ICM_1}    ${State_Configured}
    Sleep    10 minutes 30 seconds

OVF292_API_206_7 Validate ColdTrap received
    Open Connection               192.168.148.49
    Login                   root        hpvse1
    Sleep  2
    Set Client Configuration            timeout=16 seconds
    Write       resize
    ${trapoutput}=                Write       cd /etc
    ${trapoutput}=                Read until         etc]#
    ${getfile}=             SSHLibrary.Get File                 //etc//messages               C:\\
    ${trap_coldstart}=                  OperatingSystem.Grep File                 C:\\messages                  SNMPv2-MIB::coldStart
    Log to Console          ${trap_coldstart}
    ${trap_coldstart}=                  Should contain                ${trap_coldstart}             SNMPv2-MIB::coldStart

OVF292_API_206_8 Kill snmptrapd demon
    Kill snmptrapd demon

OVF292_API_206_9 Edit LI with all users and Validate Traps-User2

    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Edit LI    ${li}    ${edit_li_User2['snmpConfiguration']}

OVF292_API_206_10 Kill existing snmptrapd demon
    Kill snmptrapd demon

OVF292_API_206_11 Initiate trapd
     Initiate trapd

OVF292_API_206_12 Uplink Ports Disable
    Uplink Ports Edit           ${downlink_disable}         ${ICM_1}
    sleep   60s
    Log to Console  \nUplink port edit completed

OVF292_API_206_13 Validate Trap received
     Validate Trap received          ${MIB_down}            ${ICM_IP}

OVF292_API_206_14 Uplink Ports Enable
    Uplink Ports Edit           ${downlink_enable}          ${ICM_1}
    sleep   30s
    Log to Console  \nUplink port edit completed

OVF292_API_206_15 Validate Trap received
    Validate Trap received       ${MIB_up}          ${ICM_IP}

OVF292_API_206_16 Kill snmptrapd demon
    Kill snmptrapd demon

OVF292_API_206_17 Edit LI with all users and Validate Traps-With User3
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Edit LI    ${li}    ${edit_li_User3['snmpConfiguration']}

OVF292_API_206_18 Kill existing snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_203_1 Initiate trapd
     Initiate trapd

OVF293_API_TC_203 Uplink Ports Disable
    Uplink Ports Edit           ${downlink_disable}         ${ICM_1}
    sleep   60s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_203_2 Validate Trap received
      Validate Trap received         ${MIB_down}            ${ICM_IP}

OVF293_API_TC_204 Uplink Ports Enable
    Uplink Ports Edit           ${downlink_enable}          ${ICM_1}
    sleep   30s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_204_1 Validate Trap received
    Validate Trap received       ${MIB_up}          ${ICM_IP}

OVF293_API_TC_204_2 Kill snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_204_5 Edit LI with all users and Validate Traps-With User4

    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Edit LI    ${li}    ${edit_li_User4['snmpConfiguration']}


OVF293_API_TC_204_6 Kill existing snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_204_7 Initiate trapd
     Initiate trapd

OVF293_API_TC_204_8 Uplink Ports Disable
    Uplink Ports Edit           ${downlink_disable}         ${ICM_1}
    sleep   60s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_204_9 Validate Trap received
      Validate Trap received         ${MIB_down}            ${ICM_IP}

OVF293_API_TC_204_10 Uplink Ports Enable
    Uplink Ports Edit           ${downlink_enable}          ${ICM_1}
    sleep   30s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_204_11 Validate Trap received
    Validate Trap received       ${MIB_up}          ${ICM_IP}

OVF293_API_TC_204_12 Kill snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_209_1 Edit LI with all users and Validate Traps-With User5

    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Edit LI    ${li}    ${edit_li_User5['snmpConfiguration']}


OVF293_API_TC_209_2 Kill existing snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_209_3 Initiate trapd
     Initiate trapd

OVF293_API_TC_209_4 Uplink Ports Disable
    Uplink Ports Edit           ${downlink_disable}         ${ICM_1}
    sleep   60s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_209_5 Validate Trap received
      Validate Trap received         ${MIB_down}            ${ICM_IP}

OVF293_API_TC_209_6 Uplink Ports Enable
    Uplink Ports Edit           ${downlink_enable}          ${ICM_1}
    sleep   30s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_209_7 Validate Trap received
    Validate Trap received       ${MIB_up}          ${ICM_IP}

OVF293_API_TC_209_8 Kill snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_209_9 Edit LI with all users and Validate Traps-With User6
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Edit LI    ${li}    ${edit_li_User6['snmpConfiguration']}


OVF293_API_TC_209_10 Kill existing snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_209_11 Initiate trapd
     Initiate trapd

OVF293_API_TC_209_12 Uplink Ports Disable
    Uplink Ports Edit           ${downlink_disable}         ${ICM_1}
    sleep   60s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_209_13 Validate Trap received
      Validate Trap received         ${MIB_down}            ${ICM_IP}

OVF293_API_TC_209_14 Uplink Ports Enable
    Uplink Ports Edit           ${downlink_enable}          ${ICM_1}
    sleep   30s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_209_15 Validate Trap received
    Validate Trap received       ${MIB_up}          ${ICM_IP}

OVF293_API_TC_209_16 Kill snmptrapd demon
    Kill snmptrapd demon

*** Keywords ***
Edit LIG body for SNMP
    [Documentation]    Edit LIG for SNMPv3
    [Arguments]    ${LIG1}    ${snmpusers}    ${trapdestination}    ${v3Enabled}
    ${lig_get}    Fusion Api Get Lig    param=?filter=name=${LIG1}
    ${lig_snmp}    Get Variable Value    ${lig_get['members'][0]['snmpConfiguration']}
    Set To Dictionary    ${lig_snmp}    v3Enabled=${v3Enabled}
    Set To Dictionary    ${lig_snmp}    snmpUsers=${snmpusers}
    Set To Dictionary    ${lig_snmp}    trapDestinations=${trapdestination}
    [Return]    ${lig_snmp}

Validate Trap received
      [Documentation]    Trap Validations with MIB and ICM
      [Arguments]     ${MIB}        ${ICM_IP}
      Open Connection               192.168.148.49
      Login                   root        hpvse1
      Sleep  2
      Set Client Configuration            timeout=16 seconds
      Write       resize
      ${trapoutput}=                Write       cd /etc
      ${trapoutput}=                Read until         etc]#
      ${trapoutput2}=               Write              tail -n 3 messages
      ${trapoutput1}=               Read until         etc]#
      Log to Console                ${trapoutput1}
      ${string}=              Should contain                ${trapoutput1}                ${MIB}
      ${string}=              Should contain                ${trapoutput1}                ${ICM_IP}

Uplink Ports Edit
    [Documentation]    Editing Uplinkport with disabling
    [Arguments]      ${downlink_disable}        ${ICM}
    Fusion Api Login Appliance      ${APPLIANCE_IP}     ${admin_credentials}
    ${ic}=    Get IC    ${ICM}
    ${uri}=    Get From IC    ${ic}   uri
    Log             ${uri}
    ${port_id}=         Get PortId from Ports           ${downlink_disable}
    ${body}=            Build Ports Edit Body           ${port_id}          ${downlink_disable}
    Log         ${body}
    ${resp}=        fusion_api_edit_interconnect_ports          ${body}         ${uri}
    ${task} =       Wait For Task   ${resp}     30s
    ${valDict} =    Create Dictionary   status_code=${200}
    ...                                 taskState=Completed
    Validate Response   ${task}    ${valDict}
    sleep   60s
    Log to Console  \nUplink port edit completed

Initiate trapd
      [Documentation]    Initiating Trap
      Open Connection               192.168.148.49
      Login                   root        hpvse1
      Sleep  2
      Set Client Configuration            timeout=16 seconds
      Write       resize
      ${output}=              Start Command                             snmptrapd -f -C -c /etc/snmp/snmptrapd.conf -Le -L f /etc/messages
      Close All Connections

Kill snmptrapd demon
    [Documentation]    Stop the snmp trap daemon
    Open Connection               192.168.148.49
    Login                   root        hpvse1
    ${output}=                Execute Command                           ps -e | grep snmptrapd
    ${status}=                Run Keyword If                '${output}'!=''               Kill Process Id         ${output}
    ...                             ELSE              Log to Console                'Trapd daemon not running'

Kill Process Id
    [Documentation]    Killing Process ID
    [Arguments]     ${output}
    ${pid1}=                        Split String            ${output}
    ${pid}=                   Get from List           ${pid1}           0
    Log to Console                          snmptrapd pid is '${pid}'
    ${output}=                Execute Command                           kill ${pid}
    Sleep           10 seconds
    ${output1}=               Execute Command                           ps -e | grep snmptrapd
    Log to Console                        ${output1}
    Run Keyword and Continue on Failure    Should Be Equal  '${output1}'        ''    snmptrapd demon not killed
    Close All Connections


Old Kill snmptrapd demon
    [Documentation]    Killing Process ID
    Open Connection               192.168.148.49
    Login                   root        hpvse1
    ${output}=              Execute Command                           ps -e | grep snmptrapd
    ${pid1}=                      Split String            ${output}
    ${pid}=                       Get from List           ${pid1}           0
    Log to Console                        snmptrapd pid is '${pid}'
    ${output}=              Execute Command                           kill ${pid}
    ${output1}=             Execute Command                           ps -e | grep snmptrapd
    Log to Console                        ${output1}
    Run Keyword and Continue on Failure    Should Be Equal  '${output1}'        ''    snmptrapd demon not killed
    Close All Connections



Retrieve username and AuthProto from MIB output
    [Documentation]    Retrieving  MIB output for Authproto
    [Arguments]     ${output}
    #${lines}=    Split to Lines                ${output}
    #${lines1}=    Convert To List    ${lines}
    ${UserProto_list}=              Create List
    :For     ${line}  IN  @{output}
    \       ${words}=               Split String            ${line}                 =
    \       ${word_username}=             Get from List        ${words}       0
    \       ${word_uname}=                      Split String            ${word_username}                  .
    \       ${user_name1}=                      Get from List           ${word_uname}            -1
    \       ${user_name}=                       Remove String           ${user_name1}            " 
    \       ${user_name}=           Strip String            ${user_name}
    \       ${word_proto}=                Get from List        ${words}       1
    \       ${word_proto1}=               Split String            ${word_proto}           ::
    \       ${word_protocol}=             Get from List           ${word_proto1}          1
    \       ${auth_protocol}=             Set Variable If
    \       ...                                                   '${word_protocol}'=='usmHMACSHAAuthProtocol'                      SHA1
    \       ...                                                   '${word_protocol}'=='usmHMACMD5AuthProtocol'                      MD5
    \       ...                                                   '${word_protocol}'=='usmNoAuthProtocol'                     None
    \       ${user_proto} =         Create Dictionary   user=${user_name}
    \       ...                             auth=${auth_protocol}
    \       Append to List                ${UserProto_list}             ${user_proto}
    [Return]                  ${UserProto_list}


Create UserProto Data
      [Documentation]    Create Userproto Data
      [Arguments]     ${user_proto_priv}
      ${user_proto}                 Create List
      ${l} =  Get Length            ${user_proto_priv}
      :FOR    ${x}    IN RANGE    0   ${l}
      \           ${user_name}=                 Get from Dictionary           ${user_proto_priv[${x}]}            user
      \           ${auth_protocol}=             Get from Dictionary           ${user_proto_priv[${x}]}            auth
      \           ${user_auth_proto} =   Create Dictionary   user=${user_name}
      \           ...                             auth=${auth_protocol}
      \       Append to List                ${user_proto}                 ${user_auth_proto}
      [Return]                        ${user_proto}

Create UserPriv Data
      [Documentation]    Create for UserPriv Data
      [Arguments]     ${user_proto_priv}
      ${user_priv}                  Create List
      ${l} =  Get Length            ${user_proto_priv}
      :FOR    ${x}    IN RANGE    0   ${l}
      \           ${user_name}=                 Get from Dictionary           ${user_proto_priv[${x}]}            user
      \           ${priv_protocol}=             Get from Dictionary           ${user_proto_priv[${x}]}            priv
      \           ${user_priv_proto} =   Create Dictionary   user=${user_name}
      \           ...                             priv=${priv_protocol}
      \       Append to List                ${user_priv}                  ${user_priv_proto}
      [Return]                        ${user_priv}


Validate UserName and AuthProtoMIB output
    [Documentation]    Validate UserName and AuthProtoMIB output
    [Arguments]     ${expected_UserAuthProto}               ${actual_UserAuthProto}
    Log to console          \nBefore sort is '${actual_UserAuthProto}'
    Sort List       ${actual_UserAuthProto}
    Log to console          \n After sort is '${actual_UserAuthProto}'
    ${expected_UserAuthProto}=          Create UserProto Data       ${expected_UserAuthProto}
    ${expected_UserAuthProto}=          Convert to List             ${expected_UserAuthProto}
    Sort List       ${expected_UserAuthProto}
    Log to console          \nExpected UserAuthProto is '${expected_UserAuthProto}'
    Log to console          \nActual UserAuthProto is '${actual_UserAuthProto}'
    ${status}=      Run Keyword And Return Status           Lists Should Be Equal           ${expected_UserAuthProto}           ${actual_UserAuthProto}
    [Return]        ${status}

Retrieve username and PrivProto from MIB output
    [Documentation]    Retrieve username and PrivProto from MIB output
    [Arguments]     ${output}
    #${lines}=    Split to Lines                ${output}
    #${lines1}=     Convert to List               ${lines}
    #${user_list}=            Create List
    ${UserPriv_list}=         Create List
      :For     ${line}  IN  @{output}
    \       ${words}=               Split String            ${line}                 =
    \       ${word_username}=             Get from List        ${words}       0
    \       ${word_uname}=                      Split String            ${word_username}                  .
    \       ${user_name1}=                      Get from List           ${word_uname}            -1
    \       ${user_name}=                       Remove String           ${user_name1}            " 
    \       ${user_name}=           Strip String            ${user_name}
    \       ${word_priv}=                 Get from List        ${words}       1
    \       ${word_priv1}=                Split String            ${word_priv}            ::
    \       ${word_privilege}=                  Get from List           ${word_priv1}            1
    \       ${priv_protocol}=             Set Variable If
    \       ...                                                   '${word_privilege}'=='usmDESPrivProtocol'                   DES
    \       ...                                                   '${word_privilege}'=='usmNoPrivProtocol'                          None
    \       ...                                                   '${word_privilege}'=='snmpPrivProtocols.4'                              AES-128
    \       ${priv_protocol} =      Create Dictionary   user=${user_name}
    \       ...                             priv=${priv_protocol}
    \       Append to List                ${UserPriv_list}              ${priv_protocol}
    [Return]                  ${UserPriv_list}



Validate UserName and AuthPrivMIB output
    [Documentation]    Validate UserName and AuthPrivMIB output
    [Arguments]     ${expected_UserPrivProto}               ${actual_UserPrivProto}
    Log to console          \nBefore sort is '${actual_UserPrivProto}'
    Sort List       ${actual_UserPrivProto}
    Log to console          \nActual UserPrivProto1 is '${actual_UserPrivProto}'
    ${expected_UserPrivProto}=          Create UserPriv Data        ${expected_UserPrivProto}
    ${expected_UserPrivProto}=          Convert to List             ${expected_UserPrivProto}
    Sort List       ${expected_UserPrivProto}
    Log to console          \nExpected UserPrivProto is '${expected_UserPrivProto}'
    Log to console          \nActual UserAuthProto is '${actual_UserPrivProto}'

    ${status}=      Run Keyword And Return Status           Lists Should Be Equal           ${expected_UserPrivProto}           ${actual_UserPrivProto}
    [Return]        ${status}

Execute snmpbulkwalk Command and validate for Authentication Protocols
      [Documentation]    Execute snmpbulkwalk Command and validate for Authentication Protocols
      [Arguments]     ${user_proto_priv}        ${ICM_IP}    ${OID}
      Log to console          \nDatas are ${OID}
      Open Connection               ${snmp_utils_ip}
      Login                   ${snmp_utils_userid}          ${snmp_utils_password}
      ${l} =  Get Length            ${user_proto_priv}
      Log to console          \nLength is ${l}
      :FOR    ${x}    IN RANGE    0   ${l}
      \           ${user_name}=                 Get from Dictionary           ${user_proto_priv[${x}]}            user
      \           ${auth_protocol}=             Get from Dictionary           ${user_proto_priv[${x}]}            auth
      \           ${auth_protocol}=             Get Substring           ${auth_protocol}            0                 3
      \           ${priv_protocol}=             Get from Dictionary           ${user_proto_priv[${x}]}            priv
      \           ${priv_protocol2}=                  Get Substring           ${priv_protocol}        0                 3
      \           ${priv_protocol}=             Set Variable if
      \           ...                                 '${priv_protocol}'=='None'                None
      \           ...                                 '${priv_protocol}'!='None'                ${priv_protocol2}

      \           ${auth_password}=             Get from Dictionary           ${user_proto_priv[${x}]}            auth_pass
      \           ${priv_password}=             Get from Dictionary           ${user_proto_priv[${x}]}            priv_pass
      \           ${sec_level}=                 Set Variable if
      \           ...                                 '${priv_protocol}'=='None'                authNoPriv
      \           ...                                 '${priv_protocol}'!='None'                authPriv
      \           Log to Console                Performing MIB walk for '${user_name}' with SecurityLevel '${sec_level}' AuthProtocol '${auth_protocol}' PrivacyProtocol '${priv_protocol}'
      \           ${command}=             Set Variable if
      \           ...                           '${priv_protocol}'=='None'                snmpbulkwalk -v 3 -u ${user_name} -a ${auth_protocol} -A ${auth_password} -t 30 -l ${sec_level} -c public ${ICM_IP} ${OID}
      \           ...                           '${priv_protocol}'!='None'                snmpbulkwalk -v 3 -u ${user_name} -a ${auth_protocol} -A ${auth_password} -x ${priv_protocol} -X ${priv_password} -t 30 -l ${sec_level} -c public ${ICM_IP} ${OID}

      \           Log to Console          \nExecuting Command        ${command}
      \           ${output1}=              Execute Command                           ${command}
      \           Log to Console    \nOutput is :${output1}
      \           ${output}=            filter_default_users                ${output1}
    \       ${user_AuthProto}=            Retrieve username and AuthProto from MIB output                              ${output}
    \       Log to Console    \nuser_Auth_Proto is :${user_AuthProto}
    \       ${Status}=              Validate UserName and AuthProtoMIB output       ${user_proto_priv}                  ${user_AuthProto}
    \       Log to Console                      ${status}
      \           Run Keyword And Continue On Failure   Should Be Equal   '${Status}'   'True'   ${Status}
    #Close All Snmp Connections
    Close All Connections

Execute snmpbulkwalk Command and validate for Privacy Protocols
      [Documentation]    Execute snmpbulkwalk Command and validate for Privacy Protocols
      [Arguments]     ${user_proto_priv}        ${ICM_IP}         ${OID}
      Open Connection               ${snmp_utils_ip}
      Login                   ${snmp_utils_userid}          ${snmp_utils_password}
      ${l} =  Get Length            ${user_proto_priv}
      :FOR    ${x}    IN RANGE    0   ${l}
      \           ${user_name}=                 Get from Dictionary           ${user_proto_priv[${x}]}            user
      \           ${auth_protocol}=             Get from Dictionary           ${user_proto_priv[${x}]}            auth
      \           ${auth_protocol}=             Get Substring           ${auth_protocol}            0                 3
      \           ${priv_protocol}=             Get from Dictionary           ${user_proto_priv[${x}]}            priv
      \           ${priv_protocol2}=                  Get Substring           ${priv_protocol}        0                 3
      \           ${priv_protocol}=             Set Variable if
      \           ...                                 '${priv_protocol}'=='None'                None
      \           ...                                 '${priv_protocol}'!='None'                ${priv_protocol2}

      \           ${auth_password}=             Get from Dictionary           ${user_proto_priv[${x}]}            auth_pass
      \           ${priv_password}=             Get from Dictionary           ${user_proto_priv[${x}]}            priv_pass
      \           ${sec_level}=                 Set Variable if
      \           ...                                 '${priv_protocol}'=='None'                authNoPriv
      \           ...                                 '${priv_protocol}'!='None'                authPriv
      \           Log to Console                Performing Privacy protocol MIB walk for '${user_name}' with SecurityLevel '${sec_level}' AuthProtocol '${auth_protocol}' PrivacyProtocol '${priv_protocol}'
      \           ${command}=             Set Variable if
      \           ...                           '${priv_protocol}'=='None'                snmpbulkwalk -v 3 -u ${user_name} -a ${auth_protocol} -A ${auth_password} -t 30 -l ${sec_level} -c public ${ICM_IP} ${OID}
      \           ...                           '${priv_protocol}'!='None'                snmpbulkwalk -v 3 -u ${user_name} -a ${auth_protocol} -A ${auth_password} -x ${priv_protocol} -X ${priv_password} -t 30 -l ${sec_level} -c public ${ICM_IP} ${OID}
      \           Log to Console          Executing Command                   ${command}
      \           ${output1}=              Execute Command                           ${command}
      \           Log to Console    \nOutput is :${output1}
      \           ${output}=            filter_default_users                ${output1}
    \       ${user_Priv_Proto}=           Retrieve username and PrivProto from MIB output                              ${output}
    \       Log to Console                         ${user_proto_priv}
    \       ${Status}=              Validate UserName and AuthPrivMIB output        ${user_proto_priv}                  ${user_Priv_Proto}
    \       Log to Console                      ${status}
      \           Run Keyword And Continue On Failure   Should Be Equal   '${Status}'   'True'   ${Status}
    #Close All Snmp Connections
    Close All Connections
    Close All Connections


Verify Interconnect State
    [Documentation]    Verify Interconnect State
    [Arguments]        ${ICM_1}        ${POWER_STATE}
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    ${ic} =        Get IC        ${ICM_1}
    ${State} =    Get From IC        ${ic}    state
    Log to console and logfile        \tICM state is ${ICM_1}:${State}
    Should Be Equal As Strings    ${State}    ${POWER_STATE}

Edit LI
    [Documentation]    Editing LI
    [Arguments]        ${li}        ${li_body}
    ${li_uri} =     Get LI URI   ${li}
    log to console    LI URI is ${li_uri}
    ${resp} =    Fusion Api Get Li    ${li_uri}
    log to console  Editing Li with snmp ${resp}
    ${respl} =    Fusion Api Update snmp configuration    body=${li_body}    uri=${li_uri}
    log to console  Editing Li with snmp ${respl}
    [Return]    ${respl}


Get SNMPUSers from Data
    [Documentation]    Get SNMPUSers from Data from LI Body
    [Arguments]    ${li_body}
    ${li_snmp_configuration} =           Get Variable Value  ${li_body}
    ${li_snmp_users} =           Get Variable Value  ${li_snmp_configuration['snmpUsers']}
    ${len1} =     Get Length    ${li_snmp_users}
    ${li_Create_user}=    Create List
    :FOR    ${x}    IN RANGE    0    ${len1}
    \    ${users1} =     Get From Dictionary    ${li_snmp_users}    ${x}
    \    ${list_user_1}=    Get From Dictionary    ${users1}    snmpV3UserName
    \    Append To List    ${li_Create_user}    ${list_user_1}
    Log to console and logfile    \n\nUsers are: ${li_Create_user}
    [Return]   ${li_Create_user}


Verify SNMP Users Edit LI
    [Documentation]    Verifying SNMP Users Edit LI
    [Arguments]        ${li}        ${data_users}
    Log to console and logfile    Validating Logical Interconnects for SNMP Users
    ${li_uri} =     Get LI URI   ${li}
    ${resp_li} =    Fusion Api Get Li    ${li_uri}
    ${snmp_config} =     Get From Dictionary        ${resp_li}    snmpConfiguration
    ${snmp_users} =     Get From Dictionary       ${snmp_config}    snmpUsers
    ${len} =     Get Length    ${snmp_users}
    ${Create_user}=    Create List

    :FOR    ${x}    IN RANGE    0    ${len}
    \    ${users} =     Get From Dictionary    ${snmp_users}    ${x}
    \    ${list_user}=    Get From Dictionary    ${users}    snmpV3UserName
    \    Append To List    ${Create_user}    ${list_user}
    \    ${users} =     Get From Dictionary    ${snmp_users}    ${x}

    #User Names
    ${len}    Get Length    ${data_users}
    :For    ${x}    In Range    0    ${len}
    \    List Should Contain Value    ${Create_user}    ${data_users[${x}]}

Get Trap Destinations Engine ID LIG
    [Documentation]    Get Trap Destinations Engine ID LIG
    [Arguments]    ${lig}
    ${lig_uri} =     Get LIG URI   ${lig}
    ${resp_lig} =    Fusion Api Get Lig    ${lig_uri}
    ${trap_dest_dict}=    Get From Dictionary    ${resp_lig['snmpConfiguration']}    trapDestinations
    ${len1} =     Get Length    ${trap_dest_dict}
    ${engine_id_list}=    Create List
    :FOR    ${x}    IN RANGE    0    ${len1}
    \    ${Engine_ID_Details}=    Get From Dictionary    ${trap_dest_dict[0]}    engineId
    \    Append To List    ${engine_id_list}    ${Engine_ID_Details}
    Log to console and logfile    \n\nEngine IDs are: ${engine_id_list}
    [Return]    ${engine_id_list}

Get Trap Destinations Port Details LIG
    [Documentation]    Get Trap Destinations Port Details LIG
    [Arguments]    ${lig}
    ${lig_uri} =     Get LIG URI   ${lig}
    log to console    LI URI is ${lig_uri}
    ${resp_lig} =    Fusion Api Get Lig    ${lig_uri}
    ${lig_trap_dest_dict}=    Get From Dictionary    ${resp_lig['snmpConfiguration']}    trapDestinations
    ${len1} =     Get Length    ${lig_trap_dest_dict}
    ${lig_port_number}=    Create List
    :FOR    ${x}    IN RANGE    0    ${len1}
    \    ${port_number}=    Get From Dictionary    ${lig_trap_dest_dict[0]}    port
    \    Append To List    ${lig_port_number}    ${port_number}
    Log to console and logfile    \n\nPort is: ${lig_port_number}
    [Return]   ${lig_port_number}

Get Trap Destinations Trap Type LIG
    [Documentation]    Get Trap Destinations Trap Type LIG
    [Arguments]    ${lig}
    ${lig_uri} =     Get LIG URI   ${lig}
    log to console    LI URI is ${lig_uri}
    ${resp_lig} =    Fusion Api Get Lig    ${lig_uri}
    ${lig_snmp_config}=    Get From Dictionary    ${resp_lig}    snmpConfiguration
    ${lig_trap_dest_dict}=    Get From Dictionary    ${lig_snmp_config}    trapDestinations
    ${len1} =     Get Length    ${lig_trap_dest_dict}
    ${lig_trap_type_list}=    Create List
    :FOR    ${x}    IN RANGE    0    ${len1}
    \    ${trap_type}=    Get From Dictionary    ${lig_trap_dest_dict[0]}    inform
    \    Append To List    ${lig_trap_type_list}    ${trap_type}
    Log to console and logfile    \n\nTrap Type is: ${lig_trap_type_list}
    [Return]   ${lig_trap_type_list}

Get LIG SNMP Users From Data
    [Documentation]    Get LIG SNMP Users From Data
    [Arguments]        ${lig_body}
    ${lig_snmp_config} =           Get Variable Value  ${lig_body['snmpConfiguration']}
    ${lig_snmp_trapdestinations} =           Get Variable Value  ${lig_snmp_config['trapDestinations']}
    ${len} =     Get Length    ${lig_snmp_trapdestinations}
    Log to console and logfile    Length..${len}
    ${USer_name}=    Create List
    :FOR    ${x}    IN RANGE    0    ${len}
    \    ${users} =     Get From Dictionary    ${lig_snmp_trapdestinations}    ${x}
    \    ${list_user}=    Get From Dictionary    ${users}    userName
    \    Append To List    ${USer_name}    ${list_user}
    Log to console and logfile    \Types are :${lig_snmp_trapdestinations}
    Log to console and logfile    \Users are :${USer_name}
    [Return]    ${USer_name}

Get LIG SNMP TrapDestinations From Data
    [Documentation]    Get LIG SNMP TrapDestinations From Data
    [Arguments]        ${lig_body}
    ${lig_snmp_config} =           Get Variable Value  ${lig_body['snmpConfiguration']}
    ${lig_snmp_trapdestinations} =           Get Variable Value  ${lig_snmp_config['trapDestinations']}
    ${len} =     Get Length    ${lig_snmp_trapdestinations}
    Log to console and logfile    Length..${len}
    ${Trap_Destination_Ip}=    Create List
    :FOR    ${x}    IN RANGE    0    ${len}
    \    ${users} =     Get From Dictionary    ${lig_snmp_trapdestinations}    ${x}
    \    ${list_user}=    Get From Dictionary    ${users}    trapDestination
    \    Append To List    ${Trap_Destination_Ip}    ${list_user}
    Log to console and logfile    \Types are :${lig_snmp_trapdestinations}
    Log to console and logfile    \Trap are :${Trap_Destination_Ip}
    [Return]    ${Trap_Destination_Ip}

Verify SNMP Trap Destination Edit LIG
    [Documentation]    Verify SNMP Trap Destination Edit LIG
    [Arguments]        ${lig}        ${data_users}    ${trap_destinations}
    Log to console and logfile    Validating Interconnects for SNMP
    log to console  Verify LIG with snmp in LIG ${lig}
    ${lig_uri} =    Get LIG URI    ${lig}
    log to console  Verify LIG with snmp in LIG ${lig_uri}
    ${Resp_Lig} =     fusion_api_get_lig    ${lig_uri}
    log to console  Verify LIG with snmp in LIG ${Resp_Lig}

    # Trap Details
    ${snmp_config} =     Get From Dictionary        ${Resp_Lig}    snmpConfiguration
    Log to console and logfile    LIG SNMP Config..${snmp_config}
    ${snmp_trap_details} =     Get From Dictionary       ${snmp_config}    trapDestinations
    Log to console and logfile    SNMP TRap Destinations...${snmp_trap_details}
    ${len} =     Get Length    ${snmp_trap_details}
    Log to console and logfile    Length..${len}
    ${trap_dest}=    Create List
    ${trap_dest_ips}=    Create List
    ${trap_dest_user}=    Create List
    ${inform}=    Create List
    :FOR    ${x}    IN RANGE    0    ${len}
    \    ${traps} =     Get From Dictionary    ${snmp_trap_details}    ${x}
    \    ${list_trap}=    Get From Dictionary    ${traps}    trapDestination
    \    Append To List    ${trap_dest}    ${list_trap}
    \    ${list_trap_users}=    Get From Dictionary    ${traps}    userName
    \    Append To List    ${trap_dest_user}    ${list_trap_users}
    ${len}    Get Length    ${data_users}
    :For    ${x}    In Range    0    ${len}
    \    List Should Contain Value    ${trap_dest_user}    ${data_users[${x}]}
    ${len}    Get Length    ${trap_destinations}
    :For    ${x}    In Range    0    ${len}
    \    List Should Contain Value    ${trap_dest}    ${trap_destinations[${x}]}
    \    log to console Verify LIG with snmp in LIG  traps and Users

Edit LIG
    [Documentation]    Editing LIG
    [Arguments]        ${lig_body}    ${lig}
    ${body} =    Build LIG body      ${lig_body}
    ${lig_uri} =    Get LIG URI    ${lig}
    Log to console and logfile    \n\nUri Is: ${lig_uri}
    ${resp1} =    Fusion Api Edit LIG    body=${body}    uri=${lig_uri}
    Log to console and logfile    \n\nOutput Is: ${resp1}
    [Return]    ${resp1}

Verify SNMP Users
    [Documentation]    Verify SNMP Users
    [Arguments]        ${lig}        ${data_users}
    Log to console and logfile    Validating Interconnects for SNMP
    ${lig_uri} =    Get LIG URI    ${lig}
    ${Resp_Lig} =     fusion_api_get_lig    ${lig_uri}

    #For Single & Multiple users
    ${snmp_config} =     Get From Dictionary        ${Resp_Lig}    snmpConfiguration
    Log to console and logfile    SNMP Config..${snmp_config}
    ${snmp_users} =     Get From Dictionary       ${snmp_config}    snmpUsers
    Log to console and logfile    SNMP Users...${snmp_users}
    ${len} =     Get Length    ${snmp_users}
    Log to console and logfile    Length..${len}
    ${Create_user}=    Create List
    :FOR    ${x}    IN RANGE    0    ${len}
    \    ${users} =     Get From Dictionary    ${snmp_users}    ${x}
    \    ${list_user}=    Get From Dictionary    ${users}    snmpV3UserName
    \    Append To List    ${Create_user}    ${list_user}

    ${len}    Get Length    ${data_users}
    :For    ${x}    In Range    0    ${len}
    \    List Should Contain Value    ${Create_user}    ${data_users[${x}]}

    #\    List Should Contain Value    ${Create_user}    ${data_users}
    #Log to console and logfile    list of SNMP User Name List..${Create_user}
    #List Should Contain Value    ${Create_user}    ${data_users}
    Log to console and logfile    SNMP Users are successfully Verified

Get IC
    [Documentation]    Get Interconnect Details
    [Arguments]        ${ICM_NAME}
    ${resp} =   fusion api get interconnect
    Log        ${resp}
    ${ics} =     Get From Dictionary     ${resp}    members
    ${l} =     Get Length    ${ics}
    :FOR    ${x}    IN RANGE    0    ${l}
    \   ${ic} =     Get From List   ${ics}    ${x}
    \     Exit For Loop If     '${ic['name']}' == '${ICM_NAME}'
    [Return]    ${ic}
    Log        ${ic}

Get PortId from Ports
    [Documentation]   Getting Port ID from Ports
    [Arguments]     ${port_edit}
    #Port number Eg: d2
    ${ic} =     Get IC          ${port_edit['interconnectName']}
    ${uri} =     Get From IC    ${ic}   uri
    Log             ${uri}
    ${interconnect} =           fusion_api_get_interconnect           uri=${uri}
    ${ports} =  Get From Dictionary     ${interconnect}     ports
    ${port_number} =           Get Variable Value  ${port_edit['portName']}
    Log         ${ports}
    ${l} =  Get Length  ${ports}
    Log     ${l}
    :FOR    ${x}    IN RANGE    0   ${l}
    \   ${port_list} =   Get From List   ${ports}    ${x}
    \   Log         ${port_list}
    \   ${portName} =   Get From Dictionary     ${port_list}        portName
    \   Run Keyword If  '${portName}' != '${port_number}'       Continue For Loop
    \   ${port_id} =    Get From Dictionary     ${port_list}        portId

    [Return]    ${port_id}
    Log         ${port_id}


Build Ports Edit Body
    [Documentation]   Building ports for Edit LI
    [Arguments]     ${port_id}          ${port_edit}
    ${interconnectName} =           Get Variable Value  ${port_edit['interconnectName']}
    ${enabled} =           Get Variable Value  ${port_edit['enabled']}
    ${portName} =           Get Variable Value  ${port_edit['portName']}
    ${type} =           Get Variable Value  ${port_edit['type']}
    ${edit_body} =  Create Dictionary   interconnectName=${interconnectName}
    ...                             enabled=${enabled}
    ...                             portName=${portName}
    ...                             portId=${port_id}
    ...                             type=${type}
    ${edit_body} =   Create list     ${edit_body}
    [Return]    ${edit_body}
    Log         ${edit_body}


Set Variable keyword
    [Documentation]    Set Variables
    ${status}=        Set Variable    True
    [Return]          ${status}

Add Enclosure Group from variable
    [Documentation]    Adds an Enclosure Group to an appliance from a variable which contains  a list of dicts with the entire payload
    [Arguments]     ${enc_group}
    Log to console and logfile      Adding ENCLOSURE GROUP ${enc_group['name']}
    ${l} =  Get Length  ${enc_group['interconnectBayMappings']}
    :FOR    ${x}    IN RANGE    0   ${l}
    \   ${liguri} =     Get From Dictionary ${enc_group['interconnectBayMappings'][${x}]}   logicalInterconnectGroupUri
    \   Continue For Loop If    '${liguri}' == 'None'
    \   ${liguri} =     Common URI Lookup by name    ${liguri}
    \   Set to dictionary   ${enc_group['interconnectBayMappings'][${x}]}   logicalInterconnectGroupUri     ${liguri}
    ${resp} =   Fusion Api Create Enclosure Group   ${enc_group}
    [Return]    ${resp}


Perform an Update From Group
    [Documentation]    Performing Update From Group
    [Arguments]        ${li}=${li}    ${timeout}=5 min     ${interval}=15s
    ${li_uri} =    Get LI URI    ${li}
    ${resp} =         Fusion Api Update from group    ${li_uri}
    ${task} =        Wait For Task     ${resp}     ${timeout}        ${interval}
    ${valDict} =     Create Dictionary    status_code=${200}
    ...                                 taskState=Completed
    Validate Response    ${task}    ${valDict}
