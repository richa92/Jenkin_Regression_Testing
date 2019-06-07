*** Settings ***
Documentation     OVF1136: i3S - Lifecycle - OS Deployment included in Server Profile Template

Resource          resource.robot
Suite Setup        Login To Appliance And Verify Oneview Prerequisites    ${fusion_ip}    ${admin_credentials}
Suite Teardown     I3S Suite Teardown
Test Setup         OVF1136 Test Setup    ${profileTemplate}

***Variables***
${DEFAULT_USER}        administrator
${DEFAULT_PASSWORD}    admin123
${SSHUSER}             root
${SSHPASSWORD}         hpvse1
${TIMEOUT}             200

*** Test Cases ***

OVF1136_TC07 Verify whether SPT is created with NONE as a deployment plan
    [Documentation]    Verify whether SPT is created with NONE as a deployment plan
    [Tags]    TC07    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    ${spt} =    copy.deepcopy    ${tc07_spt}
    ${payload} =    Create Server Profile Template Payload    ${tc07_spt}
    ${resp}=    Fusion Api Create Server Profile Template    ${payload}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    Should Be True    ${blnStatus}    msg=Failed to create profile '${spt['name']}'

OVF1136_TC09 Verify compliance alert on SP page (created from SPT) when DP is changed from valid DP to None
    [Documentation]     Verify that the compliance alert  appears on SP page (created from SPT) when DP is changed from valid DP to None
    [Tags]    TC09    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc09_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc09_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile template '${tc09_spt['name']}'
    #Create SP from SPT
    ${tc09_sp} =    copy.deepcopy    ${sp_from_spt}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc09_sp}
    #Edit valid DP to None
    ${spbody}=    Get Server Profile    ${tc09_sp['name']}
    Set To Dictionary    ${spbody}    osDeploymentSettings    ${null}
    Set To Dictionary    ${spbody}    iscsiInitiatorName    ${null}
    ${boot_mode} =    Create Dictionary    manageMode=${false}
    Set To Dictionary    ${spbody}    bootMode    ${boot_mode}
    Set To Dictionary    ${spbody}    boot    ${null}
    ${connection_settings}=    Get From Dictionary    ${spbody}    connectionSettings
    ${connections} =    Get From Dictionary    ${connection_settings}    connections
    ${count}=  Get Length    ${connections}
    :FOR    ${conn_index}    IN Range    0    ${count}
    \    Remove From Dictionary    ${connections[${conn_index}]}    boot
    \    ${ipv4} =    Get From Dictionary    ${connections[${conn_index}]}    ipv4
    \    Set ipv4 Connection attributes to None    ${ipv4}
    ${resp} =    Fusion API Edit Server Profile    ${spbody}    ${spbody['uri']}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    #Verify compliance alert
    ${alert}=    Verify Compliance Alert    ${tc09_sp}

OVF1136_TC10 Verify compliance alert appears on SP page when DP is changed from None to valid DP
    [Documentation]    Verify that compliance alert  appears on SP page (created from SPT) when DP is changed from None to valid DP
    [Tags]    TC10    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc10_spt} =    copy.deepcopy    ${spt_10}
    ${blnCreateSPT} =    Create I3S SPT    ${tc10_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc10_spt['name']}'
    Sleep    20
    # Create server profile with SPT having DP None to SP having valid DP
    ${tc10_sp} =    copy.deepcopy    ${sp_edit10}
    Delete Server Profile    ${tc10_sp['name']}
    ${blnCreateProf}=    Create I3S Server Profile    ${tc10_sp}
    Should Be True    ${blnCreateProf}    \nFailed to create profile ${tc10_sp['name']}
    Sleep    30
    #Verify compliance alert
    ${alert}=    Verify Compliance Alert    ${tc10_sp}
    # Deploy operation
    Perform deploy operation    ${tc10_sp}

OVF1136_TC11 Verify compliance alert appears on SP page when existing DP in SP is changed
    [Documentation]    Verify that the compliance alert appears on SP page when existing deployment plan in SP is changed
    [Tags]    TC11    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc11_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc11_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc11_spt['name']}'
    #Create SP from SPT
    ${tc11_sp} =    copy.deepcopy    ${sp_from_spt}
    Delete Server Profile    ${tc11_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc11_sp}
    #Edit SP with DP
    ${osdp_uri} =    Get OSDP URI    ${osdps[1]['name']}
    ${tc11_sp} =    Get Server Profile    ${tc11_sp['name']}
    Set To Dictionary    ${tc11_sp['osDeploymentSettings']}    osDeploymentPlanUri=${osdp_uri}
    ${sp_uri} =    Get from dictionary    ${tc11_sp}    uri
    ${resp}=    Fusion API Edit Server Profile    ${tc11_sp}    ${sp_uri}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    Should Be True    ${blnStatus}    Failed to update SP DP
    #Verify compliance alert
     ${alert}=    Verify Compliance Alert    ${tc11_sp}

OVF1136_TC12 Verify compliance alert appears on SP page when changed the boot order of SP
    [Documentation]    Verify whether the compliance alert appears on SP page when tried to change the boot order of SP
    [Tags]    TC12    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc12_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc12_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc12_spt['name']}'
    #Create SP from SPT
    ${tc12_sp} =    copy.deepcopy    ${sp_from_spt}
    Delete Server Profile    ${tc12_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc12_sp}
    #Edit SP with boot order change
    Log    \nChange boot order to PXE    console=True
    ${spbody}=    Get Server Profile    ${tc12_sp['name']}
    ${sp_uri}=    Get from dictionary    ${spbody}    uri
    ${boot}=    Get from dictionary    ${spbody}    boot
    ${boot_order}=    Get from Dictionary    ${boot}    order
    Set List value    ${boot_order}    0    PXE
    ${response}=    Fusion API Edit Server Profile    ${spbody}    ${sp_uri}
    Wait For Task2    ${response}    timeout=2400    interval=20
    #verify compliance alert
    ${alert}=    Verify Compliance Alert    ${tc12_sp}

OVF1136_TC13 Verify compliance alert appears on SP page when changed the BIOS settings of SP
    [Documentation]    Verify whether the compliance alert appears on SP page when tried to change the BIOS settings of SP
    [Tags]    TC13    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc13_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc13_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc13_spt['name']}'
    #Create SP from SPT
    ${tc13_sp} =    copy.deepcopy    ${sp_from_spt}
    Delete Server Profile    ${tc13_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc13_sp}
    #Edit SP with BIOS setting.
    ${blnEditProf} =    Edit I3S Server Profile    ${sp_edit13}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${sp_edit13['name']}' with bios ENABLED
    #verify NO compliance alert
    ${sp_complaince} =    Get Server Profile    ${tc13_sp['name']}
    Run Keyword If    '${sp_complaince['templateCompliance']}' != 'NonCompliant'    Log to console    \nSuccessfully created server profile.. No compliance preview message..\n
    ...    ELSE    Fail    msg=Successfully created server profile but with no compliance preview messages
    # Deploy operation
    #Perform deploy operation    ${sp_edit13}

OVF1136_TC15 Verify we can add new connections to SP other than those present in SPT
    [Documentation]    Verify whether we can add new connections to server profile other than those present in SPT
    [Tags]    TC15    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    OVF1136 Test Setup    ${profileTemplate}
    ${tc15_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc15_spt}
    Should Be True    ${blnCreateSPT}    msg=Failed to create profile '${tc15_spt['name']}'
    #Create SP from SPT
    ${tc15_sp} =    copy.deepcopy    ${sp_from_spt}
    Delete Server Profile    ${tc15_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc15_sp}
    Should Be True    ${blnCreateSPFromSPT}    msg=Failed to create profile '${tc15_sp['name']}'
    #Adding new connection to SP
    Log    \nAdding new connection to profile    console=True
    ${spbody}=    Get Server Profile    ${tc15_sp['name']}
    ${sp_uri}=    Get from dictionary    ${spbody}    uri
    ${connectionSettings}=    Get from dictionary    ${spbody}    connectionSettings
    ${connections}=    Get from dictionary    ${connectionSettings}    connections
    ${networkUri}=    replace string using regexp    ${new_profile_connection['networkUri']}    ETH:    ${EMPTY}
    ${networkUri}=    Get Ethernet URI    ${networkUri}
    Set To Dictionary    ${new_profile_connection}    networkUri    ${networkUri}
    Append To List    ${connections}    ${new_profile_connection}
    ${response}=    Fusion API Edit Server Profile    ${spbody}    ${sp_uri}
    Wait For Task2    ${response}    timeout=2400    interval=20
    # Deploy operation
    Perform deploy operation    ${tc15_sp}

OVF1136_TC16 Verify compliance alert appears on SP page when added new connections to SP
    [Documentation]    Verify that compliance alert appears on SP page when added new connections to server profile
    [Tags]    TC16    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc16_spt} =    copy.deepcopy    ${spt_16}
    ${blnCreateSPT} =    Create I3S SPT    ${tc16_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc16_spt['name']}'
    #Create SP from SPT
    ${tc16_sp} =    copy.deepcopy    ${sp16_from_spt16}
    Delete Server Profile    ${tc16_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc16_sp}
    #Adding new connection to SP
    ${spbody}=    Get Server Profile    ${tc16_sp['name']}
    ${sp_uri}=    Get from dictionary    ${spbody}    uri
    ${connectionSettings}=    Get from dictionary    ${spbody}    connectionSettings
    ${connections}=    Get from dictionary    ${connectionSettings}    connections
    ${networkUri}=    replace string using regexp    ${new_profile_connection['networkUri']}    ETH:    ${EMPTY}
    ${networkUri}=    Get Ethernet URI    ${networkUri}
    Set To Dictionary    ${new_profile_connection}    networkUri    ${networkUri}
    Append To List    ${connections}    ${new_profile_connection}
    ${response}=    Fusion API Edit Server Profile    ${spbody}    ${sp_uri}
    Wait For Task2    ${response}    timeout=2400    interval=20
    #verify compliance alert
    ${alert}=    Verify Compliance Alert    ${tc16_sp}
    # Deploy operation
    Perform deploy operation    ${tc16_sp}

OVF1136_TC17 Verify compliance alert appears on SP page when deleted a connection on SP page
    [Documentation]    Verify that compliance alert appears on SP page when deleted a connection on server profile page
    [Tags]    TC17    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #create SPT
    ${tc17_spt} =    copy.deepcopy    ${spt_17}
    ${blnCreateSPT} =    Create I3S SPT    ${tc17_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc17_spt['name']}'
    #Craete SP from SPT
    ${tc17_sp} =    copy.deepcopy    ${sp17_from_tc17_spt}
    Delete Server Profile    ${tc17_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc17_sp}
    #Delete connection from SP
    ${spbody}=    Get Server Profile    ${tc17_sp['name']}
    ${sp_uri}=    Get from dictionary    ${spbody}    uri
    ${connections}=    Get from dictionary    ${spbody['connectionSettings']}    connections
    Log    ${connections}
    ${connections_length}=    Get length    ${connections}
    :For    ${index}   IN RANGE    0    ${connections_length}
    \    Run Keyword If    '${connections[${index}]['name']}' == 'Blade_boot_mgmt_2'    Remove from List    ${connections}    ${index}
    Log    ${spbody}
    ${response}=    Fusion API Edit Server Profile    ${spbody}    ${sp_uri}
    Wait For Task2    ${response}    timeout=2400    interval=20
    #verify compliance alert
    ${alert}=    Verify Compliance Alert    ${tc17_sp}
    # Deploy operation
    Perform deploy operation    ${tc17_sp}

OVF1136_TC18 Verify compliance alert appears on SP page change bandwidth of existing connection on SP page
    [Documentation]    Verify that compliance alert appears on SP page when changed the bandwidth of existing connection on server profile page
    [Tags]    TC18    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc18_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc18_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc18_spt['name']}'
    #Create SP from SPT
    ${tc18_sp} =    copy.deepcopy    ${sp_from_spt}
    Delete Server Profile    ${tc18_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc18_sp}
    #Edit server profile and change the connection bandwidth
    Log    \nEdit server profile and change the connection bandwidth to 3500    console=True
    ${spbody}=    Get Server Profile    ${tc18_sp['name']}
    ${sp_uri}=    Get from dictionary    ${spbody}    uri
    ${connectionSettings}=    Get from dictionary    ${spbody}    connectionSettings
    ${connections}=    Get from dictionary    ${connectionSettings}    connections
    Set to dictionary    ${connections[0]}    requestedMbps    3500
    ${response}=    Fusion API Edit Server Profile    ${spbody}    ${sp_uri}
    Wait For Task2    ${response}    timeout=2400    interval=20
    #verify compliance alert
    ${sp_complaince} =    Get Server Profile    ${tc18_sp['name']}
    ${compliance} =    Get SP_Compliancepreview    ${tc18_sp['name']}
    ${msg} =    Get From Dictionary    ${compliance}    manualUpdates
    ${msg_1} =    Get From List    ${msg}    0
    ${compl_preview_count}=    Get Length    ${msg_1}
    Run Keyword If    '${compl_preview_count}' != '0' and '${sp_complaince['templateCompliance']}' == 'NonCompliant'    Log to console    \nSuccessfully created server profile.. compliance preview message ${msg_1} displayed successfully..\n
    ...    ELSE    Fail    msg=Successfully created server profile but without any compliance preview messages
    # Deploy operation
    Perform deploy operation    ${tc18_sp}

OVF1136_TC19 Verify compliance alert appears on SP page when added new connections on parent SPT
    [Documentation]    Verify that compliance alert appears on SP page when added new connections on parent SPT
    [Tags]    TC19    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc19_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc19_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc19_spt['name']}'
    #Create SP from SPT
    ${tc19_sp} =    copy.deepcopy    ${sp_from_spt}
    Delete Server Profile    ${tc19_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc19_sp}
    #Add new connection to SPT
    ${NAME} =    Get From Dictionary    ${tc19_spt}    name
    ${spbody} =    Fusion API Get Server Profile Templates    param=?filter='name'=='${NAME}'
    ${SPT_members_list} =    Get from Dictionary    ${spbody}    members
    ${SPT_members_dict} =    Convert to Dictionary    @{SPT_members_list}
    # Get the SPT uri, to be used next in update call
    ${SPT_uri} =    Get from Dictionary    ${SPT_members_dict}    uri
    ${connectionSettings}=    Get from dictionary    ${SPT_members_dict}    connectionSettings
    ${connections}=    Get from dictionary    ${connectionSettings}    connections
    ${networkUri}=    replace string using regexp    ${new_profiletemplate_connection['networkUri']}    ETH:    ${EMPTY}
    ${networkUri}=    Get Ethernet URI    ${networkUri}
    Set To Dictionary    ${new_profiletemplate_connection}    networkUri    ${networkUri}
    Append To List    ${connections}    ${new_profiletemplate_connection}
    ${Response}=    Fusion Api Edit Server Profile Template    ${SPT_members_dict}    ${SPT_uri}
    Wait For Task2    ${Response}    timeout=2400    interval=20
    #verify compliance alert
    ${alert}=    Verify Compliance Alert    ${tc19_sp}
    # Deploy operation
    Perform deploy operation    ${tc19_sp}

OVF1136_TC20 Verify compliance alert appears on SP page when deleted the existing connection on parent SPT
    [Documentation]    Verify that compliance alert appears on SP page when deleted the existing connection on parent SPT
    [Tags]    TC20    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc20_spt} =    copy.deepcopy    ${spt_17}
    Delete Server Profile Template    ${tc20_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc20_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc20_spt['name']}'
    #Create SP from SPT
    ${tc20_sp} =    copy.deepcopy    ${sp17_from_tc17_spt}
    Delete Server Profile    ${tc20_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc20_sp}
    #Delete connection from parent SPT
    ${NAME} =    Get From Dictionary    ${tc20_spt}    name
    ${spbody} =    Fusion API Get Server Profile Templates    param=?filter='name'=='${NAME}'
    ${SPT_members_list} =    Get from Dictionary    ${spbody}    members
    ${SPT_members_dict} =    Convert to Dictionary    @{SPT_members_list}
    # Get the SPT uri, to be used next in update call
    ${SPT_uri} =    Get from Dictionary    ${SPT_members_dict}    uri
    ${connectionSettings}=    Get from dictionary    ${SPT_members_dict}    connectionSettings
    ${connections}=    Get from dictionary    ${connectionSettings}    connections
    ${connections_length}=    Get length    ${connections}
    :For    ${index}   IN RANGE    0    ${connections_length}
    \    Run Keyword If    '${connections[${index}]['name']}' == 'Blade_boot_mgmt_2'    Remove from List    ${connections}    ${index}
    ${Response}=    Fusion Api Edit Server Profile Template    ${SPT_members_dict}    ${SPT_uri}
    Wait For Task2	${Response}    timeout=2400    interval=20
    #verify compliance alert
    ${alert}=    Verify Compliance Alert    ${tc20_sp}
    # Deploy operation
    Perform deploy operation    ${tc20_sp}

OVF1136_TC21 Verify compliance alert appears on SP page change the bandwidth of existing connection on parent SPT
    [Documentation]    Verify that compliance alert appears on SP page when changed the bandwidth of existing connection on parent SPT
    [Tags]    TC21    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc21_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc21_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc21_spt['name']}'
    #Create SP from SPT
    ${tc21_sp} =    copy.deepcopy    ${sp_from_spt}
    Delete Server Profile    ${tc21_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc21_sp}
    #Edit server profile template and change the connection bandwidth to 3500
    Log    \nEdit server profile template and change the connection bandwidth to 3500    console=True
    ${NAME} =    Get From Dictionary    ${tc21_spt}    name
    ${spbody} =    Fusion API Get Server Profile Templates    param=?filter='name'=='${NAME}'
    ${SPT_members_list} =    Get from Dictionary    ${spbody}    members
    ${SPT_members_dict} =    Convert to Dictionary    @{SPT_members_list}
    # Get the SPT uri, to be used next in update call
    ${SPT_uri} =    Get from Dictionary    ${SPT_members_dict}    uri
    ${connectionSettings}=    Get from dictionary    ${SPT_members_dict}    connectionSettings
    ${connections}=    Get from dictionary    ${connectionSettings}    connections
    Set to dictionary    ${connections[0]}    requestedMbps    3500
    ${Response}=    Fusion Api Edit Server Profile Template    ${SPT_members_dict}    ${SPT_uri}
    Wait For Task2    ${Response}    timeout=2400    interval=20
    #verify compliance alert
    ${sp_complaince} =    Get Server Profile    ${tc21_sp['name']}
    ${compliance} =    Get SP_Compliancepreview    ${tc21_sp['name']}
    ${msg} =    Get From Dictionary    ${compliance}    manualUpdates
    ${msg_1} =    Get From List    ${msg}    0
    ${compl_preview_count}=    Get Length    ${msg_1}
    Run Keyword If    '${compl_preview_count}' != '0' and '${sp_complaince['templateCompliance']}' == 'NonCompliant'    Log to console    \nSuccessfully created server profile.. compliance preview message ${msg_1} displayed successfully..\n
    ...    ELSE    Fail    msg=Successfully created server profile but without any compliance preview messages
    # Deploy operation
    Perform deploy operation    ${tc21_sp}

OVF1136_TC28 Verify no compliance alert appears on SP page when assigned some value to the blank CA value
    [Documentation]    Verify that no compliance alert appears on SP page when assigned some value to the blank custom attribute value
    [Tags]    TC28    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT with blank custom attribute value
    ${tc28_spt} =    copy.deepcopy    ${spt_28}
    ${blnCreateSPT} =    Create I3S SPT    ${tc28_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc28_spt['name']}'
    # Create server profile and assign CA values
    ${tc28_sp} =    copy.deepcopy    ${serverprofiles_tc28}
    Delete Server Profile    ${tc28_sp['name']}
    ${blnCreateProf}=    Create I3S Server Profile    ${tc28_sp}
    Should Be True    ${blnCreateProf}    \nFailed to create profile ${tc28_sp['name']}
    Sleep    20
    #verify no compliance alert
    ${sp_complaince} =    Get Server Profile    ${tc28_sp['name']}
    Run Keyword If    '${sp_complaince['templateCompliance']}' != 'NonCompliant'    Log to console    \nSuccessfully created server profile.. No compliance preview message..\n
    ...    ELSE    Fail    msg=Successfully created server profile but with no compliance preview messages
    # Deploy operation
    Perform deploy operation    ${tc28_sp}

OVF1136_TC29 Verify no compliance alert appears on the SP page when tried to over ride the existing CA values
    [Documentation]    Verify that no compliance alert appears on the SP page when tried to over ride the existing custom attribute values
    [Tags]    TC29    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc29_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc29_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc29_spt['name']}'
    # Create server profile with new CA values
    ${tc29_sp} =    copy.deepcopy    ${serverprofiles_tc29}
    Delete Server Profile    ${tc29_sp['name']}
    ${blnCreateProf}=    Create I3S Server Profile    ${tc29_sp}
    Should Be True    ${blnCreateProf}    \nFailed to create profile ${tc29_sp['name']}
    Sleep    20
    #verify no compliance alert
    ${sp_complaince} =    Get Server Profile    ${tc29_sp['name']}
    Run Keyword If    '${sp_complaince['templateCompliance']}' != 'NonCompliant'    Log to console    \nSuccessfully created server profile.. No compliance preview message..\n
    ...    ELSE    Fail    msg=Successfully created server profile but with no compliance preview messages
    # Deploy operation
    Perform deploy operation    ${tc29_sp}

OVF1136_TC30 Verify SPT creation is successful with blank CA values
    [Documentation]    Verify SPT creation is successful with blank custom attribute values
    [Tags]    TC30    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    OVF1136 Test Setup    ${profileTemplate}
    ${tc30_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc30_spt}
    Should Be True    ${blnCreateSPT}    msg=Failed to create profile '${tc30_spt['name']}'

OVF1136_TC31 Verify the deployment connections can be deleted when DP is present on SPT
    [Documentation]    Verify whether the deployment connections can be deleted when deployment plan is present on SPT
    [Tags]    TC31    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    ${tc31_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc31_spt}
    Should Be True    ${blnCreateSPT}    msg=Failed to Create Server profile '${tc31_spt['name']}'
    ${blnEditSPT} =    Edit I3S SPT    ${tc31_edit_spt}
    Should Be True    ${blnEditSPT}    msg= deployment connections deleted successfully when deployment plan is present on SPT

OVF1136_TC43 Verify the right enclosure/enc-bay and profile value is updated in SP when we had chosen the token in SPT
    [Documentation]    Verify the right enclosure/enclosure bay and profile value is updated in SP when we had chosen the enclosure/enclosure bay and profile token in SPT
    [Tags]    TC43    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${blnCreateSPT} =    Create I3S SPT    ${tc43_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc43_spt['name']}'
    #Create SP from SPT
    ${tc43_sp} =    copy.deepcopy    ${sp43_from_spt}
    Delete Server Profile    ${tc43_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc43_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc43_sp['name']}'
    #To verify Token name
    ${sp_response} =    Get Server Profile    ${sp43_from_spt['name']}
    ${osds} =     Get From Dictionary    ${sp_response}    osDeploymentSettings
    ${os_ca} =    Run Keyword If    ${osds} != None    Get From Dictionary    ${osds}    osCustomAttributes
    ${token}=    Get Attribute Value From OSCA    ${os_ca}    DomainName
    Log    \ntoken value is: ${token}    console=true
    Should Be Equal    ${token}    ${token_names['name']}    msg=Failed to match with the Enclosure,EnclosureBay and profile names
    # Deploy operation
    Perform deploy operation    ${tc43_sp}

OVF1136_TC44 Verify that CA does not accept only tokens for domainname
    [Documentation]    Verify that custom attribtes does not accept only tokens for domainname
    [Tags]    TC44    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${blnCreateSPT} =    Create I3S SPT    ${tc44_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create template '${tc44_spt['name']}'
    #Create SP
    ${tc44_sp} =    copy.deepcopy    ${sp44_from_spt}
    Delete Server Profile    ${tc44_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc44_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'=='True'    Fail    Failed to create profile '${tc44_sp['name']}'
    # Deploy operation
    Perform deploy operation    ${tc44_sp}

OVF1136_TC46 Deploy sp from spt having nic attribute, template is created from profile having nic ca
    [Documentation]    Deploy sp from spt having nic attribute, template is created from profile having nic ca
    [Tags]    TC46    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc46_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc46_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create template '${tc46_spt['name']}'
    #Create SP from SPT
    ${tc46_sp} =    copy.deepcopy    ${sp_from_spt}
    Delete Server Profile    ${tc46_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc46_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc46_sp['name']}'
    #Create SPT from SP
    ${sp_response} =    Get Server Profile    ${sp_from_spt['name']}
    Create Serverprofile Template from Serverprofile    ${sp_response}
    # Deploy operation
    Perform deploy operation    ${tc46_sp}

OVF1136_TC48 Verify compliance alert is displayed when SP is edited to add SPT with mismatched SHT
    [Documentation]    Verify compliance alert is displayed when existing SP is edited to add SPT with mismatched hardware type
    [Tags]    TC48    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT with one hardware type
    ${tc48_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc48_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc48_spt['name']}'
    #Create SP from SPT
    ${tc48_sp} =    copy.deepcopy    ${sp_from_spt}
    Delete Server Profile    ${tc48_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc48_sp}
    #Create SPT with another Hardware type
    ${tc48_spt1} =    copy.deepcopy    ${spt1_tc48}
    ${blnCreateSPT} =    Create I3S SPT    ${tc48_spt1}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc48_spt1['name']}'
    # Edit Sp and Change SPT
    ${blnEditProf} =    Edit I3S Server Profile    ${serverprofiles_edittc48}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${serverprofiles_edittc48['name']}' with different SPT
    #verify compliance alert
    ${sp_complaince} =    Get Server Profile    ${serverprofiles_edittc48['name']}
    ${compliance} =    Get SP_Compliancepreview    ${serverprofiles_edittc48['name']}
    ${msg} =    Get From Dictionary    ${compliance}    manualUpdates
    ${msg_1} =    Get From List    ${msg}    0
    ${compl_preview_count}=    Get Length    ${msg_1}
    Run Keyword If    '${compl_preview_count}' != '0' and '${sp_complaince['templateCompliance']}' == 'NonCompliant'    Log to console    \nSuccessfully created server profile.. compliance preview message ${msg_1} displayed successfully..\n
    ...    ELSE    Fail    msg=Successfully created server profile but without any compliance preview messages
    # Deploy operation
    Perform deploy operation    ${serverprofiles_edittc48}

OVF1136_TC50 Verify compliance alert is displayed for DP inconsistency only after SHT mismatch alert is displayed
    [Documentation]    Verify compliance alert is displayed for deployment plan inconsistency only after SHT mismatch alert is displayed
    [Tags]    TC50    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
     #Create SPT with one hardware type
    ${tc48_spt} =    copy.deepcopy    ${spt}
    Delete Server Profile Template    ${tc48_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc48_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc48_spt['name']}'
    #Create SP from SPT
    ${tc48_sp} =    copy.deepcopy    ${sp_from_spt}
    Delete Server Profile    ${tc48_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc48_sp}
    #Create SPT with another Hardware type
    ${tc48_spt1} =    copy.deepcopy    ${spt1_tc48}
    Delete Server Profile Template    ${tc48_spt1}
    ${blnCreateSPT} =    Create I3S SPT    ${tc48_spt1}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to Create Server profile template '${tc48_spt1['name']}'
    # Edit Sp and Change SPT
    ${blnEditProf} =    Edit I3S Server Profile    ${serverprofiles_edittc50}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${serverprofiles_edittc48['name']}' with different SPT
    #verify compliance alert
    ${sp_complaince} =    Get Server Profile    ${serverprofiles_edittc50['name']}
    ${compliance} =    Get SP_Compliancepreview    ${serverprofiles_edittc50['name']}
    ${msg} =    Get From Dictionary    ${compliance}    manualUpdates
    ${msg_1} =    Get From List    ${msg}    0
    ${compl_preview_count}=    Get Length    ${msg_1}
    Run Keyword If    '${compl_preview_count}' != '0' and '${sp_complaince['templateCompliance']}' == 'NonCompliant'    Log to console    \nSuccessfully created server profile.. compliance preview message ${msg_1} displayed successfully..\n
    ...    ELSE    Fail    msg=Successfully created server profile but without any compliance preview message
    #To verify compliance alert on deployment plan which will be seen only once above alert is cleared so editing
    ${blnEditProf} =    Edit I3S Server Profile    ${sp_secondedittc50}
    Run Keyword If    '${blnEditProf}'!='True'    Fail    Failed to update profile '${sp_secondedittc50['name']}' with different SPT
    #verify compliance alert
    ${alert}=    Verify Compliance Alert    ${sp_secondedittc50}
    # Deploy operation
    Perform deploy operation    ${sp_secondedittc50}

OVF1136_TC51 Deploy sp from spt having nic teaming deployment plan
    [Documentation]    Deploy sp from spt having nic teaming deployment plan
    [Tags]    TC51    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${blnCreateSPT} =    Create I3S SPT    ${tc51_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create template '${tc51_spt['name']}'
    #Create SP from SPT
    ${tc51_sp} =    copy.deepcopy    ${sp51_from_spt51}
    Delete Server Profile    ${tc51_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc51_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc51_sp['name']}'
    # Deploy operation
    Perform deploy operation    ${tc51_sp}

OVF1136_TC52 Create SPT having nic teaming deployment plan
    [Documentation]    Create SPT having nic teaming deployment plan
    [Tags]    TC52    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    ${tc52_sp} =    copy.deepcopy    ${tc51_spt}
    Delete Server Profile Template    ${tc52_sp}
    #Create SPT with nic
    ${blnCreateSPT} =    Create I3S SPT    ${tc52_sp}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create template '${tc51_spt['name']}'

OVF1136_TC53 Unassign dp from SP created from SPT, check in-use of dp
    [Documentation]    Unassign dp from SP created from SPT, check in-use of dp
    [Tags]    TC53    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc53_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc53_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile template '${tc53_spt['name']}'
    #Create SP from SPT
    ${tc53_sp} =    copy.deepcopy    ${sp_from_spt}
    Delete Server Profile    ${tc53_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc53_sp}
    #Edit SP by making DP None
    ${spbody}=    Get Server Profile    ${tc53_sp['name']}
    Set To Dictionary    ${spbody}    osDeploymentSettings    ${null}
    Set To Dictionary    ${spbody}    iscsiInitiatorName    ${null}
    ${boot_mode} =    Create Dictionary    manageMode=${false}
    Set To Dictionary    ${spbody}    bootMode    ${boot_mode}
    Set To Dictionary    ${spbody}    boot    ${null}
    ${connection_settings}=    Get From Dictionary    ${spbody}    connectionSettings
    ${connections} =    Get From Dictionary    ${connection_settings}    connections
    ${count}=  Get Length    ${connections}
    :FOR    ${conn_index}    IN Range    0    ${count}
    \    Remove From Dictionary    ${connections[${conn_index}]}    boot
    \    ${ipv4} =    Get From Dictionary    ${connections[${conn_index}]}    ipv4
    \    Set ipv4 Connection attributes to None    ${ipv4}
    ${resp} =    Fusion API Edit Server Profile    ${spbody}    ${spbody['uri']}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    #Get i3s Appliance Cluster IP and Login to i3s appliance
    ${resp} =    Fusion Api Get i3sCluster IP
    ${i3S_IP} =    Get From Dictionary    ${resp['members'][0]}    primaryIPV4
    Log to console    ${i3S_IP}
    # Login to i3s appliance
    ${admin_credentials} =    Create Dictionary    userName=${DEFAULT_USER}
    ...                                            password=${DEFAULT_PASSWORD}
    Set Suite Variable    ${admin_credentials}    ${admin_credentials}
    ${Response}    ${SessionId} =    Fusion Api Login Appliance    ${fusion_IP}    ${admin_credentials}
    I3S API LOGIN APPLIANCE    ${i3S_IP}    ${SessionId}
    #Delete Deploymentplan 1 to check in-use of DP
    ${NAME} =    Get From Dictionary    ${osdps[0]}    name
    Log To Console    \nDeleting Deploymentplan:\t ${NAME}
    ${Response} =    i3s Api Delete Deploymentplan    ${NAME}
    Should Be Equal As Strings    ${Response['status_code']}    412    msg=Failed to delete Deploymentplan

OVF1136_TC54 Copy SP created from SPT, edit dp from having no nic to dp having nic, add connections
    [Documentation]    Copy SP created from SPT, edit dp from dp having no nic constraints to dp having nic constraints, add connections
    [Tags]    TC54    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc54_spt} =    copy.deepcopy    ${tc54_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc54_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile template '${tc54_spt['name']}'
    #Create SP from SPT
    ${tc54_sp} =    copy.deepcopy    ${sp54_from_tc54_spt}
    Delete Server Profile    ${tc54_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc54_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc54_sp['name']}'
    #Add new connection to SP
    Log    \nAdding new connection to profile    console=True
    ${spbody}=    Get Server Profile    ${tc54_sp['name']}
    ${sp_uri}=    Get from dictionary    ${spbody}    uri
    ${connectionSettings}=    Get from dictionary    ${spbody}    connectionSettings
    ${connections}=    Get from dictionary    ${connectionSettings}    connections
    ${networkUri}=    replace string using regexp    ${new_profile_connection['networkUri']}    ETH:    ${EMPTY}
    ${networkUri}=    Get Ethernet URI    ${networkUri}
    Set To Dictionary    ${new_profile_connection}    networkUri    ${networkUri}
    Append To List    ${connections}    ${new_profile_connection}
    ${response}=    Fusion API Edit Server Profile    ${spbody}    ${sp_uri}
    Wait For Task2    ${response}    timeout=2400    interval=20
    #Copy server profile
    ${blnSwapProf} =    Copy Server profile    ${tc54_sp['name']}    ${servers[1]}    ${Serverprofile_copy[1]}
    Should Be True    ${blnSwapProf}    msg=Failed To Copy Server profile
    # Deploy operation
    Perform deploy operation    ${Serverprofile_copy[1]}

OVF1136_TC55 Copy SP created from SPT, edit dp having nic to dp having no nic, remove connections
    [Documentation]    Copy SP created from SPT, edit dp from dp having nic constraints to dp having no nic constraints, remove connections
    [Tags]    TC55    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc55_spt} =    copy.deepcopy    ${tc55_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc55_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile template '${tc55_spt['name']}'
    #Create SP from SPT
    ${tc55_sp} =    copy.deepcopy    ${sp55_from_tc55_spt}
    Delete Server Profile    ${tc55_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc55_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc55_sp['name']}'
    #Copy server profile
    Delete Server Profile    ${Serverprofile_copy[2]['name']}
    ${blnSwapProf} =    Copy Server profile by changing osdp and removing connection    ${tc55_sp['name']}    ${servers[1]}    ${Serverprofile_copy[2]}
    Should Be True    ${blnSwapProf}    msg=Failed To Copy Server profile
    # Deploy operation
    Perform deploy operation    ${Serverprofile_copy[2]}

OVF1136_TC56 Copy SP created from SPT change the ca values deploy
    [Documentation]    Copy SP created from SPT change the ca values deploy
    [Tags]    TC56    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc56_spt} =    copy.deepcopy    ${tc56_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc56_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile template '${tc56_spt['name']}'
    #Create SP from SPT
    ${tc56_sp} =    copy.deepcopy    ${sp56_from_tc56_spt}
    Delete Server Profile    ${tc56_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc56_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc56_sp['name']}'
    #Copy server profile
    Delete Server Profile    ${Serverprofile_copy[0]['name']}
    ${blnSwapProf} =    Copy Server profile    ${tc56_sp['name']}    ${servers[1]}    ${Serverprofile_copy[0]}
    Should Be True    ${blnSwapProf}    msg=Failed To Copy Server profile
    # Deploy operation
    Perform deploy operation    ${Serverprofile_copy[0]}

OVF1136_TC57 Edit SP from SPT none to SPT having blank CA's
    [Documentation]    Edit SP from SPT none to SPT having blank ca's
    [Tags]    TC57    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${blnCreateSPT} =    Create I3S SPT    ${spt_tc57}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create profile '${spt_tc57['name']}'
    #Create SP with SPT = None
    ${tc57_sp} =    copy.deepcopy    ${sp_tc57}
    Delete Server Profile    ${tc57_sp['name']}
    ${blnCreateSP} =    Create I3S Server Profile    ${tc57_sp}
    Run Keyword If    '${blnCreateSP}'!='True'    Fail    Failed to create profile '${tc57_sp['name']}'
    #Edit SP
    ${sp_new} =    Create I3S Server Profile POST Payload from SPT    ${sp_tc57_edit}
    ${blnEditSP} =    Edit I3S Server Profile    ${sp_tc57_edit}
    # Deploy operation
    Perform deploy operation    ${sp_tc57_edit}

OVF1136_TC45 Deploy sp from spt having nic attribute Create SP
    [Documentation]    Deploy sp from spt having nic attribute Create I3S Server Profile
    [Tags]    TC45    OVF1136
    OVF1136 Test Setup    ${profileTemplate}
    #Create SPT
    ${tc45_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc45_spt}
    Run Keyword If    '${blnCreateSPT}'!='True'    Fail    Failed to create template '${tc45_spt['name']}'
    #Create SP from SPT
    ${tc45_sp} =    copy.deepcopy    ${sp_from_spt}
    Delete Server Profile    ${tc45_sp['name']}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc45_sp}
    Run Keyword If    '${blnCreateSPFromSPT}'!='True'    Fail    Failed to create profile '${tc45_sp['name']}'
    # Deploy operation
    Perform deploy operation    ${tc45_sp}