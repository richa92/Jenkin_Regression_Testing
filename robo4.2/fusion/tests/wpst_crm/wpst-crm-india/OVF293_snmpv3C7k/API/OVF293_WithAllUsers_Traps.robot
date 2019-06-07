*** Settings ** *
Documentation        Feature Test:  OVF293 SNMPv3
...                  This set of test cases is to verify the feature SNMPv3 related testing
...
Variables           data_variables.py
Resource            ../../../../resource/fusion_api_all_resource_files.txt
Library             Collections
Library             json
Library             OperatingSystem
Library             Selenium2Library
Library             FusionLibrary
Library             BuiltIn

*** Variables ** *
${SSH_PASS}                     hpvse1
${DataFile}                     ./OVAData.xml
${APPLIANCE_IP}                192.168.146.34
${inform}                       False
${li}                            SGH411DFYA-LIG_New1
${MIB_down}             IF-MIB::linkDown
${MIB_up}               IF-MIB::linkUp
${ICM_IP}         192.168.147.1
${ICM_1}                        SGH411DFYA, interconnect 1
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

OVF293_API_TC_00 Preconditions-Create LIG,EG,Import Enclosure
    Log to console and logfile    \nPreconditions
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    ${users} =    Get Variable Value    ${users}
    Run Keyword If    ${users} is not ${null}    Add Users from variable                ${users}
    ${ethernet_networks} =    Get Variable Value    ${ethernet_networks1}
    Run Keyword If    ${ethernet_networks1} is not ${null}    Add Ethernet Networks from variable    ${ethernet_networks1}
    ${fc_network} =    Get Variable Value    ${fc_network}
    Run Keyword If    ${fc_network} is not ${null}    Add FC Networks from variable    ${fc_network}
    # LIG with Ethernet Modules
    ${resp} =    Create LIG      ${LIG_new}
    Log to console and logfile    \n\nLIG Created Successfully:${resp}
    ${lig_edit}    Get LIG member    ${LIG1}
    ${lig_uri}    Get Variable Value    ${lig_edit['uri']}
    Set Global Variable    ${LIG_URI}    ${lig_uri}
    ${lig_snmp}    Edit LIG body for SNMP    ${LIG1}    ${add_snmp_users_six_combinations['snmpUsers']}    ${add_snmp_users_six_combinations['trapDestinations']}
    Set To Dictionary    ${lig_edit}    eTag=
    Set To Dictionary    ${lig_edit}    snmpConfiguration=${lig_snmp}
    ${resp}    fusion_api_edit_lig    body=${lig_edit}    uri=${LIG_URI}
    Run Keyword If  '${resp['status_code']}' == '202'    Log to console  \nStatus Code: ${resp['status_code']} \nSuccessfully!! Edited the LIG for snmpV3 single user with auth & priv protocols and trap details\n
    ...    ELSE    FAIL
    ${task} =    Wait For Task     ${resp}     180 s    10 s
    ${valDict} =     Create Dictionary    status_code=${200}
    ...                                 taskState=Completed
    Validate Response    ${task}    ${valDict}
    # LIG with Hill FC Module
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    ${resp} =    Create LIG      ${LIG_FC}
    Log to console and logfile    \n\nLIG with FC Created Successfully:${resp}
    ${lig_edit}    Get LIG member    ${LIG2}
    ${lig_uri}    Get Variable Value    ${lig_edit['uri']}
    Set Global Variable    ${LIG_URI_1}    ${lig_uri}
    ${lig_snmp}    Edit LIG body for SNMP    ${LIG2}    ${add_lig_fc['snmpUsers']}    ${add_lig_fc['trapDestinations']}
    Set To Dictionary    ${lig_edit}    eTag=
    Set To Dictionary    ${lig_edit}    snmpConfiguration=${lig_snmp}
    ${resp}    fusion_api_edit_lig    body=${lig_edit}    uri=${LIG_URI_1}
    Run Keyword If  '${resp['status_code']}' == '202'    Log to console  \nStatus Code: ${resp['status_code']} \nSuccessfully!! Edited the LIG for snmpV3 single user with auth & priv protocols and trap details\n
    ...    ELSE    FAIL
    ${task} =    Wait For Task     ${resp}     180 s    10 s
    ${valDict} =     Create Dictionary    status_code=${200}
    ...                                 taskState=Completed
    Validate Response    ${task}    ${valDict}
    ${status}=    Add Enclosure Group from variable    ${enc_group}
    Log to console and logfile    \nResp:${status}
    Add Enclosures from variable   ${encs}
    #Poweroff server and Create Serverprofile
    Power off ALL servers
    ${profiles} =    Copy List     ${server_profiles}
    Add Server Profiles from variable    ${profiles}
    Power on server      SGH411DFYA, bay 6
    Log to console and logfile      Waiting 10 minutes for server to boot...
    Sleep   10min

OVF293_API_TC_05 Verify LIG USers
    ${lig_name} =           Get Variable Value  ${LIG1}
    ${lig_snmp_users} =           Get Variable Value  ${add_snmp_users_six_combinations['snmpUsers']}
    Log to console and logfile    \n\nResp Content Is: ${lig_snmp_users}
    ${len1} =     Get Length    ${lig_snmp_users}
    ${lig_Create_user}=    Create List
    :FOR    ${x}    IN RANGE    0    ${len1}
    \    ${users1} =     Get From Dictionary    ${lig_snmp_users}    ${x}
    \    ${list_user_1}=    Get From Dictionary    ${users1}    snmpV3UserName
    \    Append To List    ${lig_Create_user}    ${list_user_1}
    Log to console and logfile    \n\nResp Content Is: ${lig_Create_user}
    Verify SNMP Users     ${lig_name}    ${lig_Create_user}
    Log to console and logfile    \nUsers are verified successfully Security Level Authentication with MD5

OVF293_API_TC_156 User MIB Validation for AuthProto
   Execute snmpbulkwalk Command and validate for Authentication Protocols                                ${user_proto_priv_lig}                     192.168.147.1                       .1.3.6.1.6.3.15.1.2.2.1.5

OVF293_API_TC_157 Retrieve User Name and PrivProto from MIB output and validate
   Execute snmpbulkwalk Command and validate for Privacy Protocols                                 ${user_proto_priv_lig}                     192.168.147.1                       .1.3.6.1.6.3.15.1.2.2.1.8

OVF293_API_TC_36 Edit LI with all users and Validate Traps

    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Edit LI    ${li}    ${edit_li_exiting_snmp_users_auth_and_authpriv['snmpConfiguration']}
    #${task} =   Wait For Task   ${resp}     300s    2s
    #Run Keyword If  '${resp['status_code']}' != '202'   Fail    ELSE    Log to Console  \n-LI  Edited successfully
    Wait Until Keyword Succeeds    600 s    10 s    Verify Interconnect State    ${ICM_1}    ${State_Configured}
    ${li_Create_user} =    Get SNMPUSers from Data    ${edit_li_exiting_snmp_users_auth_and_authpriv['snmpConfiguration']}
    Verify SNMP Users Edit LI   ${li}    ${li_Create_user}

OVF293_API_TC_36_156 User MIB Validation for AuthProto LI
   Execute snmpbulkwalk Command and validate for Authentication Protocols                                ${user_proto_priv_li}                     192.168.147.1                       .1.3.6.1.6.3.15.1.2.2.1.5

OVF293_API_TC_36_157 Retrieve User Name and PrivProto from MIB output and validate LI
   Execute snmpbulkwalk Command and validate for Privacy Protocols                                 ${user_proto_priv_li}                     192.168.147.1                       .1.3.6.1.6.3.15.1.2.2.1.8

OVF293_API_TC_173_01 Kill existing snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_173_02 Initiate trapd
      Open Connection               192.168.148.49
      Login                   root        hpvse1
      Sleep  2
      Set Client Configuration            timeout=16 seconds
      Write       resize
      ${output}=              Start Command                             snmptrapd -f -C -c /etc/snmp/snmptrapd.conf -Le -L f /etc/messages
      Close All Connections

OVF293_API_TC_173_03 Uplink Ports Disable
    Uplink Ports Edit           ${downlink_disable}         ${ICM_1}
    sleep   60s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_173_04 Validate Trap received
     Validate Trap received          ${MIB_down}            ${ICM_IP}

OVF293_API_TC_178_05 Uplink Ports Enable
    Uplink Ports Edit           ${downlink_enable}          ${ICM_1}

OVF293_API_TC_178_06 Validate Trap received
    Validate Trap received       ${MIB_up}          ${ICM_IP}

OVF293_API_TC_146 Power_Off_on interconnect and verify the Recalculated Ip being updated
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    OA CLI POWEROFF    ${OA_HOST}    ${OA_USER}    ${OA_PASS}   INTERCONNECT    ${BAY}
    Log to Console  Waiting for interconnect removal  to complete
    Wait Until Keyword Succeeds    600 s    10 s    Verify Interconnect State    ${ICM_1}    ${State_Power_Off}

    #Power_On interconnect and verify the Recalculated Ip being updated
    OA CLI POWERON    ${OA_HOST}    ${OA_USER}    ${OA_PASS}   INTERCONNECT    ${BAY}
    Log to Console  Waiting for interconnect claim process to complete
    Wait Until Keyword Succeeds    600 s    10 s    Verify Interconnect State    ${ICM_1}    ${State_Configured}
    Sleep    10 minutes 30 seconds

    #Validate ColdTrap received
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

    #Kill snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_173 Edit LI with all users and Validate Traps-User2

    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Edit LI    ${li}    ${edit_li_User2['snmpConfiguration']}

OVF293_API_TC_173_05 Kill existing snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_173_06 Initiate trapd
     Initiate trapd

OVF293_API_TC_173_07 Uplink Ports Disable
    Uplink Ports Edit           ${downlink_disable}         ${ICM_1}
    sleep   60s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_173_08 Validate Trap received
     Validate Trap received          ${MIB_down}            ${ICM_IP}

OVF293_API_TC_174 Uplink Ports Enable
    Uplink Ports Edit           ${downlink_enable}          ${ICM_1}
    sleep   30s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_174_01 Validate Trap received
    Validate Trap received       ${MIB_up}          ${ICM_IP}

OVF293_API_TC_174_02 Kill snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_177 Edit LI with all users and Validate Traps-With User3
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Edit LI    ${li}    ${edit_li_User3['snmpConfiguration']}

OVF293_API_TC_177_01 Kill existing snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_177_02 Initiate trapd
     Initiate trapd

OVF293_API_TC_177_03 Uplink Ports Disable
    Uplink Ports Edit           ${downlink_disable}         ${ICM_1}
    sleep   60s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_177_04 Validate Trap received
      Validate Trap received         ${MIB_down}            ${ICM_IP}

OVF293_API_TC_178 Uplink Ports Enable
    Uplink Ports Edit           ${downlink_enable}          ${ICM_1}
    sleep   30s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_178_01 Validate Trap received
    Validate Trap received       ${MIB_up}          ${ICM_IP}

OVF293_API_TC_178_02 Kill snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_178_03 Edit LI with all users and Validate Traps-With User4

    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Edit LI    ${li}    ${edit_li_User4['snmpConfiguration']}


OVF293_API_TC_178_04 Kill existing snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_178_05 Initiate trapd
     Initiate trapd

OVF293_API_TC_178_06 Uplink Ports Disable
    Uplink Ports Edit           ${downlink_disable}         ${ICM_1}
    sleep   60s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_178_07 Validate Trap received
      Validate Trap received         ${MIB_down}            ${ICM_IP}

OVF293_API_TC_178_08 Uplink Ports Enable
    Uplink Ports Edit           ${downlink_enable}          ${ICM_1}
    sleep   30s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_178_09 Validate Trap received
    Validate Trap received       ${MIB_up}          ${ICM_IP}

OVF293_API_TC_178_10 Kill snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_178_11 Edit LI with all users and Validate Traps-With User5

    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Edit LI    ${li}    ${edit_li_User5['snmpConfiguration']}

OVF293_API_TC_178_12 Kill existing snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_178_13 Initiate trapd
     Initiate trapd

OVF293_API_TC_178_14 Uplink Ports Disable
    Uplink Ports Edit           ${downlink_disable}         ${ICM_1}
    sleep   60s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_178_15 Validate Trap received
      Validate Trap received         ${MIB_down}            ${ICM_IP}

OVF293_API_TC_178_16 Uplink Ports Enable
    Uplink Ports Edit           ${downlink_enable}          ${ICM_1}
    sleep   30s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_178_17 Validate Trap received
    Validate Trap received       ${MIB_up}          ${ICM_IP}

OVF293_API_TC_178_18 Kill snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_178_19 Edit LI with all users and Validate Traps-With User6
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Edit LI    ${li}    ${edit_li_User6['snmpConfiguration']}

OVF293_API_TC_178_20 Kill existing snmptrapd demon
    Kill snmptrapd demon

OVF293_API_TC_178_21 Initiate trapd
     Initiate trapd

OVF293_API_TC_178_22 Uplink Ports Disable
    Uplink Ports Edit           ${downlink_disable}         ${ICM_1}
    sleep   60s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_178_23 Validate Trap received
      Validate Trap received         ${MIB_down}            ${ICM_IP}

OVF293_API_TC_178_24 Uplink Ports Enable
    Uplink Ports Edit           ${downlink_enable}          ${ICM_1}
    sleep   30s
    Log to Console  \nUplink port edit completed

OVF293_API_TC_178_25 Validate Trap received
    Validate Trap received       ${MIB_up}          ${ICM_IP}

OVF293_API_TC_178_26 Kill snmptrapd demon
    Kill snmptrapd demon

*** Keywords ***
Create LIG
    [Documentation]    Suite Setup Tasks
    [Arguments]        ${body1}
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    ${body}    Build LIG body    ${body1}
    Log to console and logfile    \n-Creating LIG ${body}
    ${resp}    Fusion Api Create LIG    ${body}
    ${task} =   Wait For Task   ${resp}    60s  2s
    [Return]    ${resp}

Get LIG member
    [Documentation]    Get LIG member
    [Arguments]    ${LIG1}
    ${lig_get}    Fusion Api Get Lig    param=?filter=name=${LIG1}
    ${lig_edit}    Get Variable Value    ${lig_get['members'][0]}
    [Return]    ${lig_edit}


Edit LIG body for SNMP
    [Documentation]    Edit LIG for SNMPv3
    [Arguments]    ${LIG1}    ${snmpusers}    ${trapdestination}
    ${lig_get}    Fusion Api Get Lig    param=?filter=name=${LIG1}
    ${lig_snmp}    Get Variable Value    ${lig_get['members'][0]['snmpConfiguration']}
    Set To Dictionary    ${lig_snmp}    v3Enabled=true
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
    ${output}=                Execute Command                           kill -9 ${pid}
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
    ${lines}=    Split to Lines                ${output}
    ${lines1}=    Convert To List    ${lines}
    ${UserProto_list}=              Create List
      :For     ${line}  IN  @{lines1}
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
    ...                             auth=${auth_protocol}
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
      ...                             auth=${auth_protocol}
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
      ...                             priv=${priv_protocol}
      \       Append to List                ${user_priv}                  ${user_priv_proto}
      [Return]                        ${user_priv}

Validate UserName and AuthProtoMIB output
    [Documentation]    Validate UserName and AuthProtoMIB output
    [Arguments]     ${expected_UserAuthProto}               ${actual_UserAuthProto}

    Sort List       ${actual_UserAuthProto}
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
    ${lines}=    Split to Lines                ${output}
    ${lines1}=     Convert to List               ${lines}
    #${user_list}=            Create List
    ${UserPriv_list}=         Create List
      :For     ${line}  IN  @{lines1}
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
    ...                             priv=${priv_protocol}
    \       Append to List                ${UserPriv_list}              ${priv_protocol}
    [Return]                  ${UserPriv_list}

Validate UserName and AuthPrivMIB output
    [Documentation]    Validate UserName and AuthPrivMIB output
    [Arguments]     ${expected_UserPrivProto}               ${actual_UserPrivProto}
    Sort List       ${actual_UserPrivProto}
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
      \           Log to Console          Executing Command                   ${command}
      \           ${output}=              Execute Command                           ${command}
    \       ${user_AuthProto}=            Retrieve username and AuthProto from MIB output                              ${output}
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
      \           ${output}=              Execute Command                           ${command}
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
    [Documentation]    Performing edit LI
    [Arguments]        ${li}        ${li_body}
    ${li_uri} =     Get LI URI   ${li}
    log to console    LI URI is ${li_uri}
    ${resp} =    Fusion Api Get Li    ${li_uri}
    log to console  Editing Li with snmp ${resp}
    ${respl} =    Fusion Api Update snmp configuration    body=${li_body}    uri=${li_uri}
    log to console  Editing Li with snmp ${respl}
    #${task} =  Wait For Task   ${respl}    300s    2s
    #Run Keyword If '${respl['status_code']}' != '202'   Fail    ELSE    Log to Console  \n-LI  Edited successfully
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
    [Documentation]    Verify SNMP Users Edit LI
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

Verify SNMP Users
    [Documentation]    Verifying SNMP Users
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

Set Variable keyword
    [Documentation]   Set Variable Keyword
    ${status}=        Set Variable    True
    [Return]          ${status}

Add Enclosure Group from variable
    [Documentation]    Adds an Enclosure Group to an appliance from a variable which contains  a list of dicts with the entire payload
    [Arguments]     ${enc_group}
    Log to console and logfile      Adding ENCLOSURE GROUP ${enc_group['name']}
    ${l} =  Get Length  ${enc_group['interconnectBayMappings']}
    :FOR    ${x}    IN RANGE    0   ${l}
    \   ${liguri} =     Get From Dictionary    ${enc_group['interconnectBayMappings'][${x}]}   logicalInterconnectGroupUri
    \   Continue For Loop If    '${liguri}' == 'None'
    \   ${liguri} =     Common URI Lookup by name    ${liguri}
    \   Set to dictionary   ${enc_group['interconnectBayMappings'][${x}]}   logicalInterconnectGroupUri     ${liguri}
    ${resp} =   Fusion Api Create Enclosure Group   ${enc_group}
    [Return]    ${resp}
