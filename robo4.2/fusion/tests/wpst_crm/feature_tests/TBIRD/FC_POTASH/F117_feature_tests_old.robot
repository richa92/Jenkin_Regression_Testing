*** Settings ***
Documentation    FC DirectAttach on Potash User Story
...
...              - LE - 2 frame, HA, IBS3, CL20
...
...              - 1 Enet uplinkset on Aside: IC3:Q2:1 (4x8Gb FC/4x10Gb Enet Universal)
...              - 2 DA uplinksets on Aside
...                   - US-DA1: DA1. 2 uplinks, IC3:Q4:3 (4x8Gb FC/4x10Gb Enet, Universal) and IC3:Q5:1 (1x8Gb)
...                   - US-DA2: DA2, 1 uplinkport, IC3:Q4:4
...              - 1 DA uplinkset on Bside
...                   - US-DA3: DA3, 1 uplinkport, IC6:Q4:4 (4x8Gb FC/4x10Gb Enet, Universal)
...
...              - IC3:Q4:3 and IC3:Q5:1 are connected to 3par-A partner ports
...              - IC3:Q4:4 and IC6:Q4:4 are connected to 3par-B partner ports
...
...              - 4 servers: 1 Enet Connection, 2 FC DA connections
...                   - enc1, server1:  Linux,    DA1 and DA3 connections
...                   - enc2, server7:  Windows,  DA1 and DA3 connections
...                   - enc1, server10: Linux,    DA2 and DA3 connections
...                   - enc2, server4:  Windows,  DA2 and DA3 connections
...
...              - Minimum 2 servers going through each uplinkset locally or through CL20 port for storage access
...
...              - Test with Happy path, disable/enable uplinks/downlinks, uplink speed change
...              - Power off/on potashes (Aside and Bside)
...              - Remove/insert potashes (Aside and Bside)
...
...              - Server storage path verification are through server downlink connectionMap of IC nameServers
...

#Variables        ./data_common.py
#Variables        ./data_ha.py

Resource         ../../../../resource/fusion_api_all_resource_files.txt
Resource         ../FVT/fvt-keywords.txt
Resource         ../FVT/Resources/fvt_resource.txt
Resource         ./F117_keywords.txt

Library          FusionLibrary
Library          ../FVT/fvt_api.py

*** Variables ***
${LI_URI}	   None
${LE_URI}	   None
${ENC_URI}	   None
${LIG_URI}	   None
${POTASH3_URI}    None
${POTASH6_URI}    None
	
*** Test Cases ***
OVF243 Set up Login User
    [Tags]  Login    setup

	Set Log Level	TRACE
	Fusion Api Login Appliance	${appliance_ip}    ${data_common.admin_credentials}

    # get the OV version
    ${resp} =    Fusion Api Get Appliance Version
    Set Suite Metadata     OneView Version      ${resp['softwareVersion']}    top=True
	
OVF243 Set up Create Ethernet Networks
    [Tags]  Enet     setup
	Create Ethernet Networks    ${data_common.ethernet_networks}

OVF243 Set up Create FabricAttach and DirectAttach Networks
    [Tags]  FC    setup
	Create FC Networks    ${data_common.fc_networks}

OVF243 Negative LIG FC DA Uplinkset
    [Tags]  LigUSNegative
    [Documentation]    The following are tested: limitations for FC DA uplinkset defined on LIG
    ...                CRM_INVALID_UPLINK_SET_PORT
    ...                    case - IRF split port
    ...                    case - IRF unsplit port
    ...                CRM_LOGICAL_UPLINK_TEMPLATE_FIBRE_CHANNEL_PORTS_DO_NOT_ALL_BELONG_TO_SAME_SWITCH
    ...                CRM_LOGICAL_UPLINK_CAN_ONLY_CONTAIN_MAX_ONE_FC_NETWORK
    ...                CRM_INVALID_UPLINK_SET_PORT_FC
    ...                    case - Q1 to Q6 Unsplit port not allowed


    Log to console and logfile    ${\n}FC DA uplinkset on LIG negative test
    :FOR    ${ligtest}    IN    @{err_ligs}
    \	${resp} =    Add LIG from variable    ${ligtest['ligBody']}
    \	${task} =    Wait For Task    ${resp}    120s    2s
    \	Verify ErrorCode in taskError  ${task['taskErrors']}    ${ligtest['errorCode']}

OVF243 Set up Create Logical Interconnect Groups
    [Tags]  Lig    setup
	${resp} =	Add LIG from variable	${ligs['${LIG}']}
    #Should Be Equal As Integers    ${resp['status_code']}    ${202}

    ${task} =    Wait For Task    ${resp}    3min    10s
    Should Be Equal As Strings    ${task['taskState']}    Completed

OVF243 Set up Create Enclosure Group
    [Tags]  EG     setup
	${resp} =	Add Enclosure Group from variable    ${enc_group['${EG}']}
	${resp}	Fvt Api Get Enclosure Group By Name    ${EG}
	Should Be Equal As Strings	${resp['status']}	OK
	Should Be Equal As Strings	${resp['name']}    ${EG}

OVF243 Create Logical Enclosure and Verify LI LE and uplinks status and speed
    [Documentation]   Create 2 FRAME ME HA IBS3 LE with DA Uplinksets defined on each side
    [Tags]  LE    setup
	#Pass Execution	Skip Create Logical Enclosure
	Run Keyword and Ignore Error    Write To ciDebug Log
    Add Logical Enclosure from variable    ${les['${LE}']}

    Log to Console     ${\n}Wait for all uplinks to reach final status
    Sleep    ${data_common.UPLINK_STATUS_WAIT}

    Log to Console     ${\n}Verify LE and LI status OK and Consistent
	${resp} =   Fvt Api Get Logical Enclosure By Name    ${LE}
	Run Keyword If    ${resp} != None    Set Suite Variable    ${LE_URI}    ${resp['uri']}
	Should Be Equal As Strings    ${resp['name']}    ${LE}
	Should Be Equal As Strings    ${resp['status']}    OK
	Should Be Equal As Strings    ${resp['state']}    Consistent

    Log to Console     ${\n}Verify All uplinksets status OK
    :FOR    ${us}    IN    @{ALL_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LI}    ${us}    OK

	${resp} =    Fvt Api Get Logical Interconnect By Name    ${LI}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${LI_URI}    ${resp['uri']}
    Should Be Equal As Strings	${resp['consistencyStatus']}	CONSISTENT
    Should Be Equal As Strings    ${resp['status']}    OK

    # Get the Potash information: name, uri,
    Log to Console     ${\n}Verify Both Potashes in Configured state
	${resp} =    Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    Should Be Equal As Strings    ${resp['state']}    Configured

    ${resp} =    Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}
    Should Be Equal As Strings    ${resp['state']}    Configured

    Log to Console     ${\n}Verify Aside and Bside DA Uplinks portStatus and operationalSpeed
    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Verify Port    ${POTASH3_URI}    ${uplink}    status=OK    portStatus=Linked    opSpeed=Speed_8G

    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Verify Port    ${POTASH6_URI}    ${uplink}    status=OK    portStatus=Linked    opSpeed=Speed_8G

    Log to Console     ${\n}Verify Aside and Bside FA Uplinks portStatus and operationalSpeed
    :FOR    ${uplink}    IN    @{IC3_FA_UPLINKS}
    \    Verify Port    ${POTASH3_URI}    ${uplink}    status=OK    portStatus=Linked    opSpeed=Speed_8G
    :FOR    ${uplink}    IN    @{IC6_FA_UPLINKS}
    \    Verify Port    ${POTASH6_URI}    ${uplink}    status=OK    portStatus=Linked    opSpeed=Speed_8G


OVF243 Verify all DA uplinkports connected 3par portWWN
    [Tags]   IC    setup    DAUplinks

    Log to Console     ${\n}Verify DA uplinkports connected 3par portWWN

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    Verify Happy Uplinks DA ports


OVF243 LI DA Uplinksets Negative Tests
    [Tags]  LiUSNegative
    [Documentation]    The following are tested: limitations for FC DA uplinkset on LI
    ...                CRM_PORT_CONFIG_INFO_LOCATION_IS_NOT_FC_UPLINK_CAPABLE
    ...                    case - Q1 to Q6 Unsplit port not allowed
    ...                    case - IRF split port
    ...                    case - IRF unsplit port
    ...                CRM_PORTS_IN_DIFFERENT_SWITCH
    ...                CRM_LOGICAL_UPLINK_CAN_ONLY_CONTAIN_MAX_ONE_FC_NETWORK
    ...                CRM_PORT_ALREADY_ASSIGNED
    ...                CRM_PORT_NUMBER_UNKNOWN_FORMAT
    ...                    case - Invalid port

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${LI_URI}' == 'None'     Fvt Api Get Logical Interconnect By Name    ${LI}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${LI_URI}    ${resp['uri']}


    :FOR    ${li_us}    IN    @{err_li_us_list}
    \    ${us} =     Copy Dictionary    ${li_us['usBody']}
    \    ${body} =    Build US body    ${us}    ${LI_URI}
    \    ${resp} =    Fusion Api Create Uplink Set    body=${body}
    \    Should Be Equal As Integers    ${resp['status_code']}    ${400}
    \    Should Be Equal As Strings    ${resp['errorCode']}    ${li_us['errorCode']}

OVF243 Create 4 Server Profiles Each With 2 DirectAttach Connections, Verify Profile status
    [Tags]  SP    Happy

    #Pass Execution    Skip create 4 server profiles
    Power off all servers
    Add Server Profiles from variable    ${server_profiles}    10m   20s

    # Verify Server Profile status is OK
    Verify Server Profiles Status    ${server_profile_names}    OK

OVF243 Power On Servers, Verify Servers Connections through Connection Map from Interconnect nameServers
    [Tags]  ServerEnd2End    Happy

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}

    # power on servers
    Run Keyword for List    ${servers}    Power on Server
    Log to Console    ${\n}Waiting ${data_common.SERVER_BOOT_WAIT} minutes for servers to boot and come up
    Sleep    ${data_common.SERVER_BOOT_WAIT}

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Servers DA Connections


OVF243 Change DA uplink speed Case 1, Update LI uplinkset uplink speed from Auto to 4Gb, Verifications
    [Tags]  UplinkSpeedChange1    speedChange

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${LI_URI}' == 'None'     Fvt Api Get Logical Interconnect By Name    ${LI}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${LI_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    Log to Console    ${\n}Edit LI uplinkset US-DA1 uplinks from Auto to 4Gb
    ${us} =    Copy Dictionary    ${li_uplinksets['US_DA1_4Gb']}
    ${body} =    Build US body    ${us}    ${LI_URI}
    ${us_resp} =    fvt-keywords.Get Uplink Set By Name    ${LI}    ${li_uplinksets['US_DA1_4Gb']['name']}
    ${us_uri} =    Get From Dictionary    ${us_resp}    uri

    ${resp} =    Fusion Api Edit Uplink Set    body=${body}    uri=${us_uri}
    ${task} =    Wait For Task    ${resp}    5min    15s
    Should Be Equal As Strings    ${task['taskState']}    Completed

    Log to Console    ${\n}Wait ${data_common.UPLINK_SPEED_WAIT} for speed change reflected in OV
    Sleep    ${data_common.UPLINK_SPEED_WAIT}

    Log to Console     ${\n}Verify uplink portStatus and updated operational speed
    Verify Port    ${POTASH3_URI}    Q4:3    status=OK    portStatus=Linked    opSpeed=Speed_4G
    Verify Port    ${POTASH3_URI}    Q5:1    status=OK    portStatus=Linked    opSpeed=Speed_4G

    Log to Console    ${\n}Verify server profiles status going through US_DA1 are not affected
    @{sp_set2} =    Create List    ${ENC1_SP1_NAME}    ${ENC2_SP7_NAME}
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${sp_set2}    OK

    Log to Console    ${\n}Verify servers Aside connections thorugh US-DA1 through connection map
    ${nameservers_ic3} =    Get IC NameServers    ${POTASH3_URI}
    Should Not Be Empty    ${nameservers_ic3}

    ${s1_s7_conn_map} =    Create List     ${IC3_Q43_DA_WWN}    ${IC3_Q51_DA_WWN}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER1_ENC1_DL}     ${s1_s7_conn_map}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER7_ENC1_DL}     ${s1_s7_conn_map}

OVF243 Change DA uplink speed Case 2, Update LI uplinkset uplink speed from 4Gb to 8Gb, Servers DA connection veriication
    [Tags]  UplinkSpeedChange2    speedChange

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${LI_URI}' == 'None'     Fvt Api Get Logical Interconnect By Name    ${LI}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${LI_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    Log to Console    ${\n}Edit LI uplinkset US-DA1 uplinks from 4Gb to 8Gb
    ${us} =    Copy Dictionary    ${li_uplinksets['US_DA1_8Gb']}
    ${body} =    Build US body    ${us}    ${LI_URI}
    ${us_resp} =    fvt-keywords.Get Uplink Set By Name    ${LI}    ${li_uplinksets['US_DA1_8Gb']['name']}
    ${us_uri} =    Get From Dictionary    ${us_resp}    uri

    ${resp} =    Fusion Api Edit Uplink Set    body=${body}    uri=${us_uri}
    ${task} =    Wait For Task    ${resp}    5min    15s
    Should Be Equal As Strings    ${task['taskState']}    Completed

    Log to Console    ${\n}Wait ${data_common.UPLINK_SPEED_WAIT} for speed change reflected in OV
    Sleep    ${data_common.UPLINK_SPEED_WAIT}

    Log to Console     ${\n}Verify updated uplink speed
    Verify Port    ${POTASH3_URI}    Q4:3    status=OK    portStatus=Linked    opSpeed=Speed_8G
    Verify Port    ${POTASH3_URI}    Q5:1    status=OK    portStatus=Linked    opSpeed=Speed_8G

    Log to Console    ${\n}Verify server profiles status going through US_DA1 are not affected
    @{sp_set2} =    Create List    ${ENC1_SP1_NAME}    ${ENC2_SP7_NAME}
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${sp_set2}    OK

    # Verify servers Aside connections through connection map
    ${nameservers_ic3} =    Get IC NameServers    ${POTASH3_URI}
    Should Not Be Empty    ${nameservers_ic3}

    ${s1_s7_conn_map} =    Create List     ${IC3_Q43_DA_WWN}    ${IC3_Q51_DA_WWN}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER1_ENC1_DL}     ${s1_s7_conn_map}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER7_ENC1_DL}     ${s1_s7_conn_map}

OVF243 Change uplink speed Case 3, LI UFG change uplink speed back to Auto, Servers DA connection veriication
    [Tags]  LIUFGSpeedChange    speedChange

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${LI_URI}' == 'None'     Fvt Api Get Logical Interconnect By Name    ${LI}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${LI_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    Log to Console    ${\n}Perform LI update from group to change uplink speed back to Auto
    ${resp} =    Fusion Api Update from group    ${LI_URI}
    Should Be Equal As Integers    ${resp['status_code']}    ${202}
    #took more than 10 minutes
    ${task} =    Wait For Task    ${resp}    15m    30s
    Should Be Equal As Strings    ${task['taskState']}    Completed

    Log to Console    ${\n}Wait ${data_common.UPLINK_SPEED_WAIT} for speed change reflected in OV
    Sleep    ${data_common.UPLINK_SPEED_WAIT}

    Log to Console    ${\n}Verify all uplink speed are expected
    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Verify Port    ${POTASH3_URI}    ${uplink}    status=OK    portStatus=Linked    opSpeed=Speed_8G

    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Verify Port    ${POTASH6_URI}    ${uplink}    status=OK    portStatus=Linked    opSpeed=Speed_8G

    #Verify server profiles status going through US_DA1 are not affected
    @{sp_set2} =    Create List    ${ENC1_SP1_NAME}    ${ENC2_SP7_NAME}
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${sp_set2}    OK

    #Verify server connections
    ${nameservers_ic3} =    Get IC NameServers    ${POTASH3_URI}
    Should Not Be Empty    ${nameservers_ic3}

    ${s1_s7_conn_map} =    Create List     ${IC3_Q43_DA_WWN}    ${IC3_Q51_DA_WWN}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER1_ENC1_DL}     ${s1_s7_conn_map}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER7_ENC1_DL}     ${s1_s7_conn_map}

OVF243 Disable Uplinks Case 1, Affect Servers Aside Connection, Servers DA connection veriication through map
    [Tags]  DisableAUplink
    [Documentation]    Disable Aside US_DA1 uplinkport Q4:3 and and US_DA2 uplinkport Q4:4
    ...                US_DA1 has 2 uplinkports Q4:3 and Q5:1, disabling Q4:3 cause uplinkset to be Warning status.
    ...                No profile connection error, server1 and 10 are not affected
    ...                US_DA2 has 1 uplinkport Q4:4, disabling it would cause profile connection error.

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    Log to Console    ${\n}Disable US-DA1 uplink Q4:3 and US-DA2 uplink Q4:4
    ${disabled_uls} =    Create List    Q4:3    Q4:4

    ${body} =    Create List
    :FOR    ${ul}    IN    @{disabled_uls}
    \    ${resp} =     Get IC Port    ${POTASH3_URI}    ${ul}
    \    Set to Dictionary   ${resp}   enabled    ${false}
    \    Append to list    ${body}    ${resp}

	${resp} =    fusion api edit interconnect ports    uri=${POTASH3_URI}   body=${body}
	${task} =    Wait For Task 	${resp} 	5 min	20s
	Should Be Equal As Strings    ${task['taskState']}    Completed

    #wait for subport to change status before verifying profile status
    Log to Console    ${\n}Wait for uplink and downlink subport status change
    sleep    ${data_common.SUBPORT_STATUS_WAIT}

    Log to Console    ${\n}Verify uplink status, portStatus and disabled
    :FOR    ${ul}    IN    @{disabled_uls}
    \    Verify Port    ${POTASH3_URI}    ${ul}    status=Warning    portStatus=Unlinked    enabled=False

    Log to Console    ${\n}Verify affected uplinkset status
    Verify Uplinkset Status    ${LI}    US-DA1    Warning
    Verify Uplinkset Status    ${LI}    US-DA2    Critical


    Log to Console    ${\n}Verify server profiles status going through US_DA2 become Critical
    ${sp_set1} =    Create List    ${ENC1_SP10_NAME}    ${ENC2_SP4_NAME}
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${sp_set1}    Critical

    Log to Console    ${\n}Verify server profiles status going through US_DA1 are not affected
    @{sp_set2} =    Create List    ${ENC1_SP1_NAME}    ${ENC2_SP7_NAME}
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${sp_set2}    OK

	#Verification Potash3 connection map
    ${nameservers_ic3} =    Get IC NameServers    ${POTASH3_URI}
    Should Not Be Empty    ${nameservers_ic3}

    Log to Console      ${\n}Verify disabled uplink not in nameServers
    :FOR    ${ul}    IN    @{disabled_uls}
    \    Verify Port Not In nameServers    ${nameservers_ic3}    ${ul}

    # If the affected port trigger 3par failover to its partner port (active), any server with connection to
    # that active port will result with no loss of path due to failed over connection.
    # This is the expected behavior for 3Par partner ports, confirmed by developer who also verified
    # on C7K with the same expected behavior.

    # US-DA1 2 uplinks are 3par-A partner ports. disable IC4:3, faile over to 3Par-A its partner port
    # For s1 and s7 with connection through US-DA1 - its connectionMap on IC3 remain the same
    # US-DA2 uplink IC3:Q4:4, connected to 3Par-B port whose partner port connected to IC6:Q4:4
    # Disable this uplink causing s4 and s10 losing Aside path but gained at Bside through active port
    Log to Console    ${\n}Verify servers 4 and 10 Aside connectionMap should be empty
    ${s4_s10_conn_map} =    Create List     ${EMPTY}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER4_ENC1_DL}     ${s4_s10_conn_map}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER10_ENC1_DL}    ${s4_s10_conn_map}

    Log to Console    ${\n}Verify servers 1 and 7 Aside connectionMap should remain unchanged due to 3par partner
    ${s1_s7_conn_map} =    Create List     ${IC3_Q51_DA_WWN}    ${IC3_Q43_DA_WWN}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER1_ENC1_DL}     ${s1_s7_conn_map}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER7_ENC1_DL}     ${s1_s7_conn_map}

    ${nameservers_ic6} =    Get IC NameServers    ${POTASH6_URI}
    Should Not Be Empty    ${nameservers_ic6}

    Log to Console    ${\n}Verify all servers have addtional path in Bside
    ${conn_map} =    Create List     ${IC6_Q44_DA_WWN}    ${IC3_Q44_DA_WWN}
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Verify Server DA Connection    ${nameservers_ic6}    ${dl}     ${conn_map}

OVF243 Enable back Uplinks Case 1, Aside Connection Restoration, Verify servers connection thru Connection Map
    [Tags]  EnableAUplink

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    Log to Console    ${\n}Enable back Aside US_DA1 uplinkport Q4:3 and US_DA2 uplinkport Q4:4

    ${disabled_uls} =    Create List    Q4:3    Q4:4

    ${body} =    Create List
    :FOR    ${ul}    IN    @{disabled_uls}
    \    ${resp} =     Get IC Port    ${POTASH3_URI}    ${ul}
    \    Set to Dictionary   ${resp}   enabled    ${true}
    \    Append to list    ${body}    ${resp}

    ${resp} =    fusion api edit interconnect ports    uri=${POTASH3_URI}   body=${body}
    ${task} =    Wait For Task 	${resp} 	5 min	20s
    Should Be Equal As Strings    ${task['taskState']}   Completed

    #wait for subport to change status before verifying profile status are back to OK
    Log to Console    ${\n}Wait for uplink and downlink subport status change
    sleep    ${data_common.SUBPORT_STATUS_WAIT}

    Log to Console    ${\n}Verify uplink status, portStatus and enabled
    :FOR    ${ul}    IN    @{disabled_uls}
    \    Verify Port    ${POTASH3_URI}    ${ul}    status=OK    portStatus=Linked    enabled=True

    Log to Console    ${\n}Verify affected uplinksets back to OK
    Verify Uplinkset Status    ${LI}    US-DA1    OK
    Verify Uplinkset Status    ${LI}    US-DA2    OK

    Log to Console      ${\n}Verify Server Profiles status back to OK
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    OK

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Servers DA Connections

OVF243 Disable Uplinks Case 2, Affect Server Bside Connection, Verify servers connection thru Connection Map
    [Tags]  DisableBUplink

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    ${disabled_ul} =    Set Variable    Q4:4

    Log to Console      ${\n}Disable Bside US_DA3 uplinkport ${disabled_ul}
    ${resp} =     Get IC Port    ${POTASH6_URI}    ${disabled_ul}
    Set to Dictionary   ${resp}   enabled    ${false}
    ${body} =    Create List
    Append to list    ${body}    ${resp}

	${resp} =    fusion api edit interconnect ports    uri=${POTASH6_URI}   body=${body}
	${task} =    Wait For Task 	${resp} 	5 min	20s
	Should Be Equal As Strings    ${task['taskState']}    Completed

	#wait for subport to change status that affect profile connection
    Log to Console    ${\n}Wait for uplink and downlink subport status change
    sleep    ${data_common.SUBPORT_STATUS_WAIT}

    Log to Console    ${\n}Verify uplink status portStatus and disabled
    Verify Port    ${POTASH6_URI}    ${disabled_ul}    status=Warning    portStatus=Unlinked    enabled=False

    Log to Console    ${\n}Verify affected uplinkset Critical
    Verify Uplinkset Status    ${LI}    US-DA3    Critical

    #Verify all 4 server profiles status become Critical
    Log to Console      ${\n}Verify Server Profiles status Critical
    Verify Server Profiles status    ${server_profile_names}    Critical

	${nameservers_ic6} =    Get IC NameServers    ${POTASH6_URI}
	Should Not Be Empty    ${nameservers_ic6}

    Log to Console      ${\n}Verify disabled uplink ${disabled_ul} not in nameServers
    Verify Port Not In nameServers    ${nameservers_ic6}    ${disabled_ul}

    Log to Console     ${\n}Verify servers DA connection on Bside, expect no connections
    # Expect all servers Bside downlink connectionMap is ['']
    ${conn_map} =    Create List    ${EMPTY}
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Verify Server DA Connection    ${nameservers_ic6}    ${dl}    ${conn_map}

    ${nameservers_ic3} =    Get IC NameServers    ${POTASH3_URI}
    Should Not Be Empty    ${nameservers_ic3}

    Log to Console     ${\n}Verify servers 4 and 10 Aside connectionMap has failed over connection
    ${s4_s10_conn_map} =    Create List    ${IC3_Q44_DA_WWN}    ${IC6_Q44_DA_WWN}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER4_ENC1_DL}      ${s4_s10_conn_map}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER10_ENC1_DL}     ${s4_s10_conn_map}

    # server 1 and server7 has no connection through the active port, no failed over connection
    Log to Console    ${\n}Verify servers 1 and 7 Aside remained as is
    ${s1_s7_conn_map} =    Create List    ${IC3_Q51_DA_WWN}      ${IC3_Q43_DA_WWN}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER1_ENC1_DL}     ${s1_s7_conn_map}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER7_ENC1_DL}     ${s1_s7_conn_map}


OVF243 Enable back Uplinks Case 2, Bside Connection Restoration, Verify servers connection thru Connection Map
    [Tags]  EnableBUplink

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    ${disabled_ul} =    Set Variable    Q4:4
    Log to Console      ${\n}Enable back Bside US_DA3 uplinkport ${disabled_ul}
    ${resp} =     Get IC Port    ${POTASH6_URI}    ${disabled_ul}
    Set to Dictionary   ${resp}   enabled    ${true}
    ${body} =    Create List
    Append to list    ${body}    ${resp}

	${resp} =    fusion api edit interconnect ports    uri=${POTASH6_URI}   body=${body}
	${task} =    Wait For Task 	${resp} 	5 min	20s
	Should Be Equal As Strings    ${task['taskState']}    Completed

    #wait for subport to change status and affect profile connection
    Log to Console    ${\n}Wait for uplink and downlink subport status change
    sleep    ${data_common.SUBPORT_STATUS_WAIT}

    #Verify uplink status
    Log to Console      ${\n}Verify uplinkport status, portStatus and enabled
    Verify Port    ${POTASH6_URI}    ${disabled_ul}    status=OK    portStatus=Linked    enabled=True

    Log to Console    ${\n}Verify affected uplinkset back to OK
    Verify Uplinkset Status    ${LI}    US-DA3    OK

    #Verify server profiles status back to OK
    Log to Console      ${\n}Verify Server Profiles status back to OK
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Bside Uplinks DA ports

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Servers DA Connections

OVF243 Disable Downlinks Case 1, Affect Server Aside Connection, Verify servers connection thru Connection Map
    [Tags]  DisableDownlink

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    Log to Console      ${\n}Disable Aside downlinks for server10 and server4
    ${dl_list} =    Create List     ${SERVER10_ENC1_DL}    ${SERVER4_ENC1_DL}
    ${body} =    Create List
    :FOR    ${dl}    IN    @{dl_list}
    \    ${resp} =     Get IC Port    ${POTASH3_URI}    ${dl}
    \    Set to Dictionary   ${resp}   enabled    ${false}
    \    Append to list    ${body}    ${resp}

	${resp} =    fusion api edit interconnect ports    uri=${POTASH3_URI}   body=${body}
	${task} =    Wait For Task 	${resp} 	5 min	20s
	Should Be Equal As Strings    ${task['taskState']}    Completed

    Log to Console    ${\n}Wait for downlink status change before checking profile status
    sleep    ${data_common.SUBPORT_STATUS_WAIT}

    Log to Console    ${\n}Verify downlink status, portStatus and disabled
    :FOR    ${dl}    IN    @{dl_list}
    \    Verify Port    ${POTASH3_URI}    ${dl}    status=Critical    portStatus=Unlinked    enabled=False

    #Verify server profiles with the disabled downlink should be Critical
    Log to Console      ${\n}Verify Server Profiles status
    @{sp_set1} =    Create List    ${ENC1_SP10_NAME}    ${ENC2_SP4_NAME}
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${sp_set1}    Critical

    @{sp_set2} =    Create List    ${ENC1_SP1_NAME}    ${ENC2_SP7_NAME}
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${sp_set2}    OK

    Log to Console      ${\n}Verify disabled downlink should not be in nameServers
	${nameservers_ic3} =    Get IC NameServers    ${POTASH3_URI}
    Should Not Be Empty    ${nameservers_ic3}

	:FOR    ${dl}    IN    @{dl_list}
    \    Verify Port Not In nameServers    ${nameservers_ic3}    ${dl}

OVF243 Enable Back Downlinks Case 1, Aside Connection Restoration, Verify servers connection thru Connection Map
    [Tags]  EnableDownlink

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    ${dl_list} =    Create List     ${SERVER10_ENC1_DL}    ${SERVER4_ENC1_DL}
    ${body} =    Create List
    :FOR    ${dl}    IN    @{dl_list}
    \    ${resp} =     Get IC Port    ${POTASH3_URI}    ${dl}
    \    Set to Dictionary   ${resp}   enabled    ${true}
    \    Append to list    ${body}    ${resp}

    ${resp} =    fusion api edit interconnect ports    uri=${POTASH3_URI}   body=${body}
    ${task} =    Wait For Task 	${resp} 	5 min	20s
    Should Be Equal As Strings    ${task['taskState']}   Completed

    #wait for subport to change status before verifying profile status are back to OK
    Log to Console    ${\n}Wait for downlink status change before checking profile status
    sleep    ${data_common.SUBPORT_STATUS_WAIT}

    Log to Console    ${\n}Verify downlink status, portStatus and enabled
    :FOR    ${dl}    IN    @{dl_list}
    \    Verify Port    ${POTASH3_URI}    ${dl}    status=OK    portStatus=Linked    enabled=True

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Servers DA Connections

    #Verify server profiles status back to OK
    Log to Console      ${\n}Verify Server Profiles status back to OK
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    OK

OVF243 Power Off Aside Potash Affecting Aside connections, Verify servers Bside connection thru Connection Map
    [Tags]  PowerOffAside    PowerAside    Power

    # power off IC3, triggered US-DA2 3par port fail over to partner port where US-DA3 is connected.
    # All servers have connection through that port, result in failed over path on Bside
    # Server1 and 7 has connection through US-DA1 with both uplinks on IC3, will lose Aside connection
    # Result: all servers will lose Aside connection, and have 2 connections on bside

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    Log to Console    ${\n}Power off Aside Potash and wait for Maintenance state
    Power IC and Wait    ${POTASH3_URI}    Off

    Log to Console    ${\n}Wait for downlink status change before checking profile status
    sleep    ${data_common.SUBPORT_STATUS_WAIT}

    Log to Console     ${\n}Verify Aside DA Uplinks Unlinked Critical
    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Verify Port    ${POTASH3_URI}    ${uplink}    status=Critical    portStatus=Unlinked

    Log to Console     ${\n}Verify Aside downlinks Unlinked Critical
    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${POTASH3_URI}    ${dl}    status=Critical    portStatus=Unlinked

    Log to Console     ${\n}Verify Bside Interconnect is Configured
    Verify Interconnect    ${POTASH6}    state=Configured

    Log to Console     ${\n}Verify Bside DA Uplinks portStatus and operationalSpeed not impacted
    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Verify Port    ${POTASH6_URI}    ${uplink}    status=OK    portStatus=Linked

    Log to Console     ${\n}Verify Aside uplinksets Critical
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LI}    ${us}    Critical

    Log to Console     ${\n}Verify Bside uplinksets OK, not impacted
    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LI}    ${us}    OK

	${nameservers_ic6} =    Get IC NameServers    ${POTASH6_URI}
	Should Not Be Empty    ${nameservers_ic6}

    Log to Console     ${\n}Verify servers DA connection on Bside has failed over connection
    ${conn_map} =    Create List    ${IC6_Q44_DA_WWN}    ${IC3_Q44_DA_WWN}
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Verify Server DA Connection    ${nameservers_ic6}    ${dl}    ${conn_map}

    #there is bug that SP does not turn Critical, move as last verification
    Log to Console      ${\n}Verify Profile status Critical
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    Critical


OVF243 Power On Aside Potash Restoring Aside connections, Verify servers connection thru Connection Map
    [Tags]  PowerOnAside    PowerAside    Power

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    Log to Console     ${\n}Power back on Aside Potash and wait for Configured state
    Power IC and Wait    ${POTASH3_URI}    On

    Log to Console     ${\n}Wait for connection deployment before checking profile status
    sleep    ${data_common.CONN_DEPLOY_WAIT}

    Log to Console     ${\n}Verify Bside Interconnect remain Configured
    Verify Interconnect    ${POTASH6}    state=Configured

    Log to Console     ${\n}Verify DA Uplinks status and portStatus
    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Verify Port    ${POTASH3_URI}    ${uplink}    status=OK    portStatus=Linked
    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Verify Port    ${POTASH6_URI}    ${uplink}    status=OK    portStatus=Linked

    Log to Console     ${\n}Verify Aside downlinks back to Linked  OK
    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${POTASH3_URI}    ${dl}    status=OK    portStatus=Linked

    Log to Console     ${\n}Verify All uplinksets OK
    :FOR    ${us}    IN    @{ALL_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LI}    ${us}    OK

    Log to Console     ${\n}Verify servers Profile status OK
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Uplinks DA ports

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Servers DA Connections

OVF243 Power Off Bside Potash Affecting Bside connections, Verify servers Aside connection thru Connection Map
    [Tags]  PowerOffBside    PowerBside    Power

    # Power off IC6 result in US-DA3 connected 3par-B port to fail over to its partner port which
    # is connected through US_DA2 uplink (active).
    # Server4 and server10 will lose Bside path and gain failed over path on Aside
    # Server1 and server7 does not have connection through US_DA2, so will not have failed over path on
    # Aside. It will lose Bside path and not gain on Aside. Its path through USA-DA1 is not affected

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    Log to Console    ${\n}Power off Bside Potash and wait for Maintenance state
    Power IC and Wait    ${POTASH6_URI}    Off

    Log to Console    ${\n}Wait for downlink status change before checking profile status
    sleep    ${data_common.SUBPORT_STATUS_WAIT}

    Log to Console     ${\n}Verify Bside DA Uplinks Unlinked Critical
    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Verify Port    ${POTASH6_URI}    ${uplink}    status=Critical    portStatus=Unlinked

    Log to Console     ${\n}Verify Bside downlinks Unlinked Critical
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${POTASH6_URI}    ${dl}    status=Critical    portStatus=Unlinked

    Log to Console     ${\n}Verify Aside Interconnect remains Configured
    Verify Interconnect    ${POTASH3}    state=Configured

    Log to Console     ${\n}Verify Aside DA Uplinks status and portStatus not impacted
    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Verify Port    ${POTASH3_URI}    ${uplink}    status=OK    portStatus=Linked

    Log to Console     ${\n}Verify Bside uplinksets Critical
    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LI}    ${us}    Critical

    Log to Console     ${\n}Verify Aside uplinksets OK, not impacted
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LI}    ${us}    OK

	${nameservers_ic3} =    Get IC NameServers    ${POTASH3_URI}
	Should Not Be Empty    ${nameservers_ic3}

    Log to Console     ${\n}Verify servers 4 and 10 Aside connectionMap has failed over connection
    ${s4_s10_conn_map} =    Create List    ${IC3_Q44_DA_WWN}    ${IC6_Q44_DA_WWN}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER4_ENC1_DL}      ${s4_s10_conn_map}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER10_ENC1_DL}     ${s4_s10_conn_map}

    Log to Console    ${\n}Verify servers 1 and 7 Aside connectionMap remain as is
    ${s1_s7_conn_map} =    Create List    ${IC3_Q51_DA_WWN}    ${IC3_Q43_DA_WWN}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER1_ENC1_DL}     ${s1_s7_conn_map}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER7_ENC1_DL}     ${s1_s7_conn_map}

    # there is bug that SP does not turn Critical, do verification last
    Log to Console      ${\n}Verify Profile status after Powering off Bside Potash
    Verify Server Profiles status    ${server_profile_names}    Critical


OVF243 Power On Bside Potash Restoring Bside connections, Verify servers connection thru Connection Map
    [Tags]  PowerOnBside    PowerBside    Power

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}

    Log to Console     ${\n}Power back on Bside Potash and wait for Configured state
    Power IC and Wait    ${POTASH6_URI}    On

    Log to Console     ${\n}Wait for connection deployment before checking profile status
    sleep    ${data_common.CONN_DEPLOY_WAIT}

    Log to Console     ${\n}Verify Aside and Bside DA Uplinks status and portStatus
    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Verify Port    ${POTASH3_URI}    ${uplink}    status=OK    portStatus=Linked
    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Verify Port    ${POTASH6_URI}    ${uplink}    status=OK    portStatus=Linked

    Log to Console     ${\n}Verify Aside Interconnect remains Configured
    Verify Interconnect    ${POTASH3}    state=Configured

    Log to Console     ${\n}Verify Bside downlinks Linked  OK
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${POTASH6_URI}    ${dl}    status=OK    portStatus=Linked

    Log to Console     ${\n}Verify All uplinksets OK
    :FOR    ${us}    IN    @{ALL_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LI}    ${us}    OK

    Log to Console     ${\n}Verify servers Profile status back to OK
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Uplinks DA ports

    #Verify Servers DA connections on both Aside and Bside through connection map
    Verify Happy Servers DA Connections

OVF243 Efuse Remove Aside Potash Affecting Aside connections, Verify servers Bside connection thru Connection Map
    [Tags]  RemoveAsidePotash    efuse    efuseA

    # remove IC3, triggered US-DA2 3par port fail over to partner port where US-DA3 is connected.
    # All servers have connection through that active port. Will have failed over path in Bside
    # Server1 and 7 has connection through US-DA1 with both uplinks on IC3, will lose Aside connection
    # So all servers will lose Aside connection, and have 2 connections on bside

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    Log to Console    ${\n}Remove Aside potash and wait for Absent state
    Efuse IC and Wait    ${POTASH3}    EFuseOn

    Log to Console    ${\n}Wait for HA sync and nameServers info stabilization for Efuse case
    sleep    ${data_common.CONN_DEPLOY_WAIT}
    #sleep    ${REMOVE_IC_NS_WAIT}

    Log to Console     ${\n}Verify Bside Interconnect remains Configured
    Verify Interconnect    ${POTASH6}    state=Configured

    Log to Console     ${\n}Verify DA Bside Uplinks status and portStatus not impacted
    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Verify Port    ${POTASH6_URI}    ${uplink}    status=OK    portStatus=Linked

    Log to Console     ${\n}Verify Aside uplinksets Critical
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LI}    ${us}    Critical

    Log to Console     ${\n}Verify Bside uplinksets OK, not impacted
    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LI}    ${us}    OK

	${nameservers_ic6} =    Get IC NameServers    ${POTASH6_URI}
	Should Not Be Empty    ${nameservers_ic6}

    Log to Console     ${\n}Verify servers DA connection on Bside has failed over connection
    ${conn_map} =    Create List    ${IC6_Q44_DA_WWN}    ${IC3_Q44_DA_WWN}
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Verify Server DA Connection    ${nameservers_ic6}    ${dl}    ${conn_map}

    Log to Console      ${\n}Verify Profile status Critical
    Verify Server Profiles status    ${server_profile_names}    Critical


OVF243 Efuse Insert Aside Potash Restoring Aside connections, Verify servers connection thru Connection Map
    [Tags]  InsertAsidePotash    efuse    efuseA

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    Log to Console    ${\n}Insert back Aside potash and wait for Configured state
    Efuse IC and Wait    ${POTASH3}    EFuseOff

    Log to Console     ${\n}Wait for connection deployment before checking profile status
    sleep    ${data_common.CONN_DEPLOY_WAIT}

    Log to Console     ${\n}Verify Bside Interconnect remains Configured
    Verify Interconnect    ${POTASH6}    state=Configured

    Log to Console     ${\n}Verify both sides DA Uplinks status and portStatus
    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Verify Port    ${POTASH3_URI}    ${uplink}    status=OK    portStatus=Linked

    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Verify Port    ${POTASH6_URI}    ${uplink}    status=OK    portStatus=Linked

    Log to Console     ${\n}Verify Aside downlinks Linked OK
    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${POTASH3_URI}    ${dl}    status=OK    portStatus=Linked

    Log to Console     ${\n}Verify All uplinksets OK
    :FOR    ${us}    IN    @{ALL_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LI}    ${us}    OK

    Log to Console     ${\n}Verify Servers Profile status
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Uplinks DA ports
    Verify Happy Servers DA Connections

OVF243 Efuse Remove Bside Potash Affecting Bside connections, Verify servers Aside connection thru Connection Map
    [Tags]  RemoveBsidePotash    efuse    efuseB

    # Remove IC6 result in US-DA3 connected 3par-B port to fail over to its partner port which
    # is connected through US_DA2 uplink (active).
    # server4 and server10 will lost Bside path and gain failed over path on Aside through US_DA2
    # server1 and server7 does not have connection through US_DA2, so will not have failed over path on
    # Aside. It will lose Bside path and not gaied on Aside. Its path through USA-DA1 is not affected

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    Log to Console    ${\n}Remove Bside potash and wait for Absent state
    Efuse IC and Wait    ${POTASH6}    EFuseOn

    Log to Console    ${\n}Wait for HA sync and nameServers info stabilization for Efuse case
    sleep    ${data_common.CONN_DEPLOY_WAIT}
    #sleep    ${REMOVE_IC_NS_WAIT}

    Log to Console     ${\n}Verify Aside Interconnect remains Configured
    Verify Interconnect    ${POTASH3}    state=Configured

    Log to Console     ${\n}Verify Aside DA Uplinks status and portStatus not impacted
    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Verify Port    ${POTASH3_URI}    ${uplink}    status=OK    portStatus=Linked

    Log to Console     ${\n}Verify Aside downlinks Linked OK not impacted
    :FOR    ${dl}    IN    @{ASIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${POTASH3_URI}    ${dl}    status=OK    portStatus=Linked

    Log to Console     ${\n}Verify Bside uplinksets Critical
    :FOR    ${us}    IN    @{BSIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LI}    ${us}    Critical

    Log to Console     ${\n}Verify Aside uplinksets OK, not impacted
    :FOR    ${us}    IN    @{ASIDE_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LI}    ${us}    OK

    #Verify server profiles status become Critical
    Log to Console      ${\n}Verify Profile status Critical
    Verify Server Profiles status    ${server_profile_names}    Critical

	${nameservers_ic3} =    Get IC NameServers    ${POTASH3_URI}
	Should Not Be Empty    ${nameservers_ic3}

    Log to Console     ${\n}Verify servers 4 and 10 Aside connectionMap has failed over connection
    ${s4_s10_conn_map} =    Create List    ${IC3_Q44_DA_WWN}    ${IC6_Q44_DA_WWN}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER4_ENC1_DL}      ${s4_s10_conn_map}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER10_ENC1_DL}     ${s4_s10_conn_map}

    Log to Console    ${\n}Verify servers 1 and 7 Aside remain as is
    ${s1_s7_conn_map} =    Create List    ${IC3_Q51_DA_WWN}    ${IC3_Q43_DA_WWN}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER1_ENC1_DL}     ${s1_s7_conn_map}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER7_ENC1_DL}     ${s1_s7_conn_map}


OVF243 Efuse Insert Bside Potash Restoring Bside connections, Verify servers connection thru Connection Map
    [Tags]  InsertBsidePotash    efuse    efuseB

    # for Tag include without going through LE creation that was created already
    ${resp} =    Run Keyword If    '${POTASH3_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH3}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH3_URI}    ${resp['uri']}
    ${resp} =    Run Keyword If    '${POTASH6_URI}' == 'None'     Fvt Api Get Interconnect By Name    ${POTASH6}
    Run Keyword If    ${resp} != None    Set Suite Variable    ${POTASH6_URI}    ${resp['uri']}


    Log to Console    ${\n}Insert back Bside potash and wait for Configured state
    Efuse IC and Wait    ${POTASH6}    EFuseOff

    Log to Console     ${\n}Wait for connection deployment before checking profile status
    sleep    ${data_common.CONN_DEPLOY_WAIT}

    Log to Console     ${\n}Verify Aside Interconnect remains Configured
    Verify Interconnect    ${POTASH3}    state=Configured

    Log to Console     ${\n}Verify DA Uplinks portStatus and operationalSpeed
    :FOR    ${uplink}    IN    @{IC3_DA_UPLINKS}
    \    Verify Port    ${POTASH3_URI}    ${uplink}    status=OK    portStatus=Linked
    :FOR    ${uplink}    IN    @{IC6_DA_UPLINKS}
    \    Verify Port    ${POTASH6_URI}    ${uplink}    status=OK    portStatus=Linked

    Log to Console     ${\n}Verify Bside downlinks Linked OK
    :FOR    ${dl}    IN    @{BSIDE_SERVER_DOWNLINKS}
    \    Verify Port    ${POTASH6_URI}    ${dl}    status=OK    portStatus=Linked

    Log to Console     ${\n}Verify All uplinksets OK
    :FOR    ${us}    IN    @{ALL_UPLINK_SETS}
    \    Verify Uplinkset Status    ${LI}    ${us}    OK

    Log to Console      ${\n}Verify Profile status OK
    Run Keyword And Continue On Failure    Verify Server Profiles status    ${server_profile_names}    OK

    Verify Happy Uplinks DA ports

    Verify Happy Servers DA Connections

*** Keywords ***
Verify Happy Servers Aside DA Connections

    Log to Console    ${\n}Verify servers Aside DA connections through connection map
    ${nameservers_ic3} =    Get IC NameServers    ${POTASH3_URI}

    # In happy path, nameServers should not be Empty
    Should Not Be Empty    ${nameservers_ic3}

    ${s1_s7_conn_map} =    Create List     ${IC3_Q43_DA_WWN}    ${IC3_Q51_DA_WWN}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER1_ENC1_DL}     ${s1_s7_conn_map}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER7_ENC1_DL}     ${s1_s7_conn_map}

    ${s4_s10_conn_map} =    Create List     ${IC3_Q44_DA_WWN}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER4_ENC1_DL}     ${s4_s10_conn_map}
    Verify Server DA Connection    ${nameservers_ic3}    ${SERVER10_ENC1_DL}    ${s4_s10_conn_map}

Verify Happy Servers Bside DA Connections
    # Verify Servers Bside connections through connection map

    Log to Console    ${\n}Verify servers Bside DA connections through connection map

    ${nameservers_ic6} =    Get IC NameServers    ${POTASH6_URI}
    # In happy path, nameServers should not be Empty
    Should Not Be Empty    ${nameservers_ic6}

    ${conn_map} =    Create List     ${IC6_Q44_DA_WWN}
    Verify Server DA Connection    ${nameservers_ic6}    ${SERVER1_ENC2_DL}     ${conn_map}
    Verify Server DA Connection    ${nameservers_ic6}    ${SERVER7_ENC2_DL}     ${conn_map}
    Verify Server DA Connection    ${nameservers_ic6}    ${SERVER4_ENC2_DL}     ${conn_map}
    Verify Server DA Connection    ${nameservers_ic6}    ${SERVER10_ENC2_DL}    ${conn_map}

Verify Happy Servers DA Connections

    Log to Console    ${\n}Verify servers both Aside and Bside DA connections through connection map

    Verify Happy Servers Aside DA Connections
    Verify Happy Servers Bside DA Connections


Verify Happy Aside Uplinks DA ports

    Log to Console    ${\n}Verify Aside DA uplinkports connected to 3par port
    ${nameServers} =    Get IC NameServers    ${POTASH3_URI}
    Should Not Be Empty    ${nameServers}

    :FOR    ${uplink_da}    IN    @{IC3_UPLINKS_DA}
    \    Verify Uplink DA Port    ${nameServers}    ${uplink_da}


Verify Happy Bside Uplinks DA ports

    Log to Console    ${\n}Verify Bside DA uplinkports connected to 3par port

    ${nameServers} =    Get IC NameServers    ${POTASH6_URI}
    Should Not Be Empty    ${nameServers}

    :FOR    ${uplink_da}    IN    @{IC6_UPLINKS_DA}
    \    Verify Uplink DA Port    ${nameServers}    ${uplink_da}


Verify Happy Uplinks DA ports
    [Documentation]    Verify all DA uplinkports connected to its 3par port through nameServers

    Log to Console    ${\n}Verify all Aside and Bside DA uplinkports connected to 3par port

    Verify Happy Aside Uplinks DA ports
    Verify Happy Bside Uplinks DA ports


