*** Settings ***
Documentation    Automatic Zoning In Oneview
...
Variables        data_variables.py
Library        Collections
Library        FusionLibrary
Library        RoboGalaxyLibrary
Library        ServerOperations
Library        SSHLibrary
Library        OperatingSystem
Library        Process
Resource        ../../../../../Resources/api/fusion_api_resource.txt

*** Variables ***
${domain}    NO DOMAIN
${volume_count}    2
${module_file_path1}      ${CURDIR}\\PerformIO.py
${module_file_path2}      ${CURDIR}\\FetchIO.py
${module_file_path}      ${CURDIR}\\GetDisks.py

*** Test Cases ***
Set up Login User
    [Documentation]    Login To OneView
    [Tags]  Login    setup
    Set Log Level    TRACE

    Fusion Api Login Appliance    ${appliance_ip}    ${admin_credentials}

Initial OV cleanup
    [Documentation]    Performs a initial cleanup
    [Tags]  cleanup    setup
    Set Log Level    TRACE

    Initial Cleanup

Create Fc netowrks
    [Documentation]    Creating the FC networks through rest calls
    [Tags]  Network    setup
    Set Log Level    TRACE

    ${FC_uris}  Create List
    Set To Dictionary  ${Fc_body}  fabricType  FabricAttach
    :FOR  ${x}  IN RANGE  1  3
    \  Set To Dictionary  ${Fc_body}  name  FC_${x}
    \  ${resp}  Fusion Api Create Fc Network  ${Fc_body}
    \  Run keyword unless  ${resp['status_code']}== 202  Fail  ${resp['message']}
    \  ${uri}  Get From Dictionary  ${resp['associatedResource']}  resourceUri
    \  Append To List  ${FC_uris}  ${uri}
    Set Global Variable  ${FC_uris}  ${FC_uris}

Creating LIG
    [Documentation]    Creating the LIG,EG,LEthrough rest calls
    [Tags]  LIG    setup
    Set Log Level    TRACE

    Log to console and logfile  Creating LIG
    ${Keys}  Get Dictionary Keys  ${Enc_bay_type}
    ${Keys_length}  Get Length  ${Keys}
    ${Values}  Get Dictionary Values  ${Enc_bay_type}
    ${Values_length}  Get Length  ${Values}
    ${LIG_name_list}  Create List
    ${LIG_uri_list}  Create List
    ${Current_position}  Set Variable  0

    # Fetching permittedInterconnectTypeUri

    ${ictype_resp}  Fusion Api Get Interconnect Types  param=?filter="'name'=='${IC_model_name}'"
    ${permittedInterconnectTypeUri}  Set Variable  ${ictype_resp['members'][0]['uri']}
    Set To Dictionary  ${icmap_Redundant['interconnectMapEntryTemplates'][0]}  permittedInterconnectTypeUri  ${permittedInterconnectTypeUri}
    Set To Dictionary  ${icmap_Redundant['interconnectMapEntryTemplates'][1]}  permittedInterconnectTypeUri  ${permittedInterconnectTypeUri}
    Set To Dictionary  ${icmap_NonRedundantASide['interconnectMapEntryTemplates'][0]}  permittedInterconnectTypeUri  ${permittedInterconnectTypeUri}
    Set To Dictionary  ${icmap_NonRedundantBSide['interconnectMapEntryTemplates'][0]}  permittedInterconnectTypeUri  ${permittedInterconnectTypeUri}

    # set values in interconnectMapTemplate
    :FOR  ${x}  IN RANGE  0  ${Keys_length}
    \  Set To Dictionary  ${icmap_Redundant['interconnectMapEntryTemplates'][0]['logicalLocation']['locationEntries'][0]}  relativeValue  ${IC_bay_set}
    \  Run keyword if  '${Values[${x}]}' == 'Redundant'  Set To Dictionary  ${LIG_body}  interconnectMapTemplate  ${icmap_Redundant}
    \  Run keyword if  '${Values[${x}]}' == 'NonRedundantASide'  Set To Dictionary  ${LIG_body}  interconnectMapTemplate  ${icmap_NonRedundantASide}
    \  Run keyword if  '${Values[${x}]}' == 'NonRedundantBSide'  Set To Dictionary  ${LIG_body}  interconnectMapTemplate  ${icmap_NonRedundantBSide}
    \  Set To Dictionary  ${LIG_body}  redundancyType  ${Values[${x}]}
    \  Set To Dictionary  ${LIG_body}  name  LIG_${Keys[${x}]}_${Values[${x}]}

    # Creating LIG
    \  ${resp_lig}  Fusion Api Create LIG  ${LIG_body}
    \  Run keyword unless  ${resp_lig['status_code']} == 202  Fail  ${resp_lig['message']}
    \  ${task}  Wait For Task  ${resp_lig}  120s  2s
    \  ${resource}  Get From Dictionary  ${task['associatedResource']}  resourceName
    \  Append To List  ${LIG_name_list}  ${resource}
    \  ${resource_uri}  Get From Dictionary  ${task['associatedResource']}  resourceUri
    \  Append To List  ${LIG_uri_list}  ${resource_uri}
    \  Log to console and logfile  ${resource} created successfully

    # Set values for interconnectBayMappings
    \  ${Current_position}  Run keyword if  '${Values[${x}]}' == 'Redundant'  Steps for Redundant bay type  ${Current_position}  ${resource_uri}  ELSE  Set Variable  ${Current_position}
    \  Log to console and logfile  Current_position is ${Current_position}
    \  ${Current_position}  Run keyword if  '${Values[${x}]}' == 'NonRedundantASide'  Steps for NonRedundantASide bay type  ${Current_position}  ${resource_uri}  ELSE  Set Variable  ${Current_position}
    \  Log to console and logfile  Current_position is ${Current_position}
    \  ${Current_position}  Run keyword if  '${Values[${x}]}' == 'NonRedundantBSide'  Steps for NonRedundantBSide bay type  ${Current_position}  ${resource_uri}  ELSE  Set Variable  ${Current_position}
    \  Log to console and logfile  Current_position is ${Current_position}
    ${Current_position}  Evaluate  ${Current_position}-1
    :FOR  ${y}  IN RANGE  9  ${Current_position}  -1
    \  Remove from List  ${interconnectBayMappings}  ${y}

    Set Global Variable  ${LIG_name_list}  ${LIG_name_list}
    Set Global Variable  ${LIG_uri_list}  ${LIG_uri_list}

Creating EG
    [Documentation]    Creating the LIG,EG,LEthrough rest calls
    [Tags]  EG    setup
    Set Log Level    TRACE

    Log to console and logfile  Creating EG
    Set To Dictionary  ${EG_body}  name  EG_enc_${enclosureCount}
    ${eg_resp}  Fusion Api Create Enclosure Group  ${EG_body}
    Run keyword unless  ${eg_resp['status_code']} == 201  Fail  ${eg_resp['message']}
    Set Global Variable  ${EG_uri}  ${eg_resp['uri']}
    Set Global Variable  ${EG_name}  ${eg_resp['name']}
    Log to console and logfile  EG created successfully

Creating LE
    [Documentation]    Creating the LIG,EG,LEthrough rest calls
    [Tags]  LE    setup
    Set Log Level    TRACE

    ${ENC1_uri}  Create List
    Log to console and logfile  Creating LE
    Set To Dictionary  ${les[0]}  enclosureGroupUri  ${EG_uri}
    :FOR  ${x}  IN RANGE  0  ${enclosureCount}
    \  ${enc_resp}  Fusion Api Get Enclosures  param=?filter="'name'=='${Enclosure_Name[${x}]}'"
    \  Set Global Variable  ${ENC_${x}_uri}  ${enc_resp['members'][0]['uri']}
    \  Log to console and logfile  The enclosure uri is ${ENC_${x}_uri}
    \  Append To List  ${les[0]['enclosureUris']}  ${ENC_${x}_uri}
    ${le_resp}  Fusion Api Create Logical Enclosure  ${les[0]}
    ${task}  Wait For Task  ${le_resp}  900s  30s

Creating Uplinkset
    [Documentation]    Creating the LIG,EG,LEthrough rest calls
    [Tags]   Uplinkset    setup
    Set Log Level    TRACE

    ${len}    Get Length    ${US_details}
    :FOR    ${x}    IN RANGE    0    ${len}
    \    Create uls in LIG   ${LIG_uri_list[0]}    ${FC_uris[${x}]}    ${US_details[${x}]['name']}
    \    ...    ${desiredSpeeds[${x}]}    ${US_details[${x}]['bay']}    ${US_details[${x}]['rel_ports']}

    LI update from Group  ${les[0]['name']}  ${LIG_name_list[0]}-1
    Sleep  60s

Login to 3PAR And Verify If Service Enabled
    [Documentation]    Verifying if services are enabled in 3PAR
    [Tags]   ServiceCheck
    Set Log Level    TRACE
    :FOR    ${command}    IN    @{Service_command}
    \    ${Service_Dict}    Verifying the status of the services    ${Storage_System_Cred}    ${command}
    \    Run Keyword If    '${Service_Dict['Service']}' != 'Enabled'    OR    '${Service_Dict['State']}' != 'Active'    Fail    ELSE    Log to Console
    \    ...    Service is Enabled and Active

Adding San Manager
    [Documentation]     Adding BNA To OneView
    [Tags]   SanManager
    Set Log Level    TRACE

    ${Response}    Add San Manager    ${san_manager_details}
    ${task} =     Wait For Task        ${Response}   60sec
    Run Keyword If  '${task['taskState']}' !='Completed'  or  ${task['status_code']} !=200   fail    msg=\nUnable to Add San Manager with Error Message ${task['taskErrors'][0][errorCode]}
    ...         ELSE    Log to console and logfile  \n\Successfully Added the SAN Manager !!
    ${Resp}    fusion_api_get_san_manager
    ${san_manager_uri}  Get From Dictionary     ${Resp['members'][0]}    uri
    Set Global Variable    ${san_manager_uri}

Connecting Storage System
    [Documentation]    Connects a Storage system in OneView
    [Tags]  StorageSystem
    Set Log Level    TRACE

    ${Response} =   Fusion Api Create Storage System    body=${Storage_System_Cred}
    ${task} =     Wait For Task        ${Response}   60sec
    ${Storage_System_uri}    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    msg=\nUnable to connect storage system with Error Message ${task['taskErrors'][0]['errorCode']}
    ...         ELSE    Set Variable    ${task['associatedResource']['resourceUri']}
    Set Global Variable    ${Storage_System_uri}
    ${Response}    Fusion Api Get Storage System    uri=${Storage_System_uri}
    Log to Console    \nresp is${Response}
    Run Keyword If    '${Response['state']}' !='Connected'    Fail
    ...         ELSE    Log to Console    \nSuccessfully Verified the Storage System state as Connected.

Changing Storage System To Managed State and Managing Storage Pools
    [Documentation]    Manage Storage System and Pools
    [Tags]  StorageSystem
    Set Log Level    TRACE

    ${Storage_Pool_Name}    Manage Storage System And Storage Pools    ${Storage_System_uri}
    ${Response}    Fusion Api Get Storage System    uri=${Storage_System_uri}
    Log to Console    \nresp is${Response}
    Run Keyword If    '${Response['state']}' !='Managed'    Fail
    ...         ELSE    Log to Console    \nSuccessfully Verified the Storage System state as managed.
    Set Global Variable    ${Storage_Pool_Name}

Verify If Pools are Managed
    [Documentation]    Verify If Pools are Managed
    [Tags]  VerifyStoragePool
    Set Log Level    TRACE

    ${Response}    Fusion Api Get Storage Pools    param=?query=name eq '${Storage_Pool_Name}'
    ${Storage_Pool_Uri}    Get From Dictionary    ${Response['members'][0]}    uri
    Set Global Variable    ${Storage_Pool_Uri}
    Run Keyword If    '${Response['members'][0]['isManaged']}' !='True'    Fail
    ...         ELSE    Log to Console    \nSuccessfully Verified the Storage Pool state as managed

Adding Associated SAN to the network
    [Documentation]    Edit Network to add associated SAN
    [Tags]  SanNetwork
    Set Log Level    TRACE

    ${san_resp}    fusion_api_get_managed_san
    ${SAN_URI}   Get From Dictionary    ${san_resp['members'][0]}    uri
    ${uplink_set_resp}    fusion_api_get_uplink_set
    ${len_network_uri}   Get From Dictionary    ${uplink_set_resp}    count
    :FOR    ${x}    IN RANGE    ${len_network_uri}
    \    continue for loop if    '${uplink_set_resp['members'][${x}]['networkType']}' == 'Ethernet'
    \    ${network_uri}    Get From Dictionary      ${uplink_set_resp['members'][${x}]}     fcNetworkUris
    \    Log to Console and logfile    ${network_uri}
    \    ${fc_resp}    fusion_api_get_fc_networks    uri=${network_uri[0]}
    \    Remove From Dictionary    ${fc_resp}    status_code    headers
    \    Set to Dictionary    ${fc_resp}    managedSanUri    ${SAN_URI}
    \    ${edit_resp}    fusion_api_edit_fc_network    ${fc_resp}    ${network_uri[0]}
    \    Run keyword If   ${edit_resp['status_code']} != 202    Fail    ${edit_resp['message']}
    \    ...    ELSE    Log to Console    \nSuccessfully Edited the Network with Associated SAN.
    Sleep    10s
    ####################  Verifying SAN state changed from Discovered to Managed   ###################
    ${san_resp1}    fusion_api_get_managed_san
    Run Keyword If    '${san_resp1['members'][0]['state']}' != 'Managed'    Fail
    ...    ELSE    Log to Console and logfile    SAN is in Managed state.

Get Volume Template Uri
    [Documentation]    Fetches the Root Volume Template Uri
    [Tags]  SanVolume    VolumeTemplate
    Set Log Level    TRACE

    ${Temp_Resp}    Fusion Api Get Storage Volumes Template
    ${len}    Get Length    ${Temp_Resp['members']}
    :FOR    ${x}    IN RANGE    0    ${len}
    \    Log to Console    \nx is ${x}
    \    Run Keyword If  '${Temp_Resp['members'][${x}]['isRoot']}' == 'True'    Run Keywords
    \    ...    Set Global Variable    ${volume_template_uri}    ${Temp_Resp['members'][${x}]['uri']}    AND      Exit For Loop
    Log to Console    \nVolume template uri is ${volume_template_uri}

Create Volume in OneView
    [Documentation]    Creates a Volume In OneView
    [Tags]  SanVolume    CreateVolume
    Set Log Level    TRACE
    ${Volume_Name}    Create List

    ${Storage_Volume_uri}    Create Storage Volume    ${Storage_volume_data}    ${Storage_Pool_Uri}    ${volume_template_uri}    ${volume_count}    ${Volume_size}
    Set Global Variable    ${Storage_Volume_uri}
    : FOR    ${x}    IN RANGE    0    ${volume_count}
    \    ${Resp}    Fusion Api Get Storage Volumes    uri=${Storage_Volume_uri[${x}]}
    \    Run Keyword If    '${Resp['status']}' != 'OK'  or  ${Resp['provisionedCapacity']} != ${Volume_size[${x}]}    Fail    msg=\nVolume is not created as expected
    \    ...    ELSE    Run Keywords    Append To List    ${Volume_Name}    ${Resp['name']}    AND
    \    ...    Log to Console    \nSuccessfully created the volume with expected size
    Set Global Variable    ${Volume_Name}

Verify The Existence of Volume in 3PAR
    [Documentation]    Verify if created voumne is reflected in 3PAR
    [Tags]  SanVolume    VerifyVolume
    Set Log Level    TRACE

    ${len}    Get Length    ${Volume_Name}
    : FOR    ${x}    IN RANGE    0    ${len}
    \    Verify Presence Of Volume In 3PAR    ${Volume_Name[${x}]}    ${Storage_System_Cred}

Creating Profile with SAN Storage
    [Documentation]    Creating Server profile with SAN Storage
    [Tags]  ServerProfile
    Set Log Level    TRACE

    ${Host_Name_List}    Create List
    :FOR   ${SP}   IN   @{server_profiles}
    \    Set to Dictionary    ${SP[0]['sanStorage']['volumeAttachments'][0]}    volumeUri     ${Storage_Volume_uri[0]}
    \    Set to Dictionary    ${SP[0]['sanStorage']['volumeAttachments'][0]}    volumeStoragePoolUri    ${Storage_Pool_Uri}
    \    Set to Dictionary    ${SP[0]}    enclosureGroupUri    EG:${EG_name}
    \    Log to Console    \nsp is ${SP}
    \    Add Server Profiles from variable     ${SP}
    \    Power on server    ${SP[0]['serverHardwareUri']}
    \    ${host_name}    Get From Dictionary      ${SP[0]}     name
    \    Log to Console and logfile    ${host_name}
    \    Append To List    ${Host_Name_List}    ${host_name}
    Set Global Variable    ${Host_Name_List}
    Sleep    600s

Verify The Existence of Host in 3PAR
    [Documentation]    Verify The Existence of Host in 3PAR
    [Tags]  VerifyHost
    Set Log Level    TRACE
    ${len_host}    Get Length    ${Host_Name_List}
    : FOR    ${x}    IN RANGE    0    ${len_host}
    \    Verifying Presence Of Host In 3PAR    ${Host_Name_List[${x}]}    ${Storage_System_Cred}

Verification of LUN and Passing IO Traffic
    [Documentation]    Verification of LUN and Passing IO Traffic
    [Tags]  LUN_IO_Traffic
    Set Log Level    TRACE

    :FOR   ${SP}   IN   @{server_profiles}
    \    ${bay}    ${bay_no}    Should Match Regexp    ${SP[0]['serverHardwareUri']}    bay\\s+(\\d+)
    \    Log to Console     ${bay_no}
    \    ${iloip} =     Get Server iLO IP    ${bay_no}
    \    Set To Dictionary    ${ilo_details}    ilo_ip   ${iloip}
    \    LUN Count and IO Traffic     ${iloip}    ${linux_details}    ${ilo_details}    ${server_details}    ${module_file_path}
    \    Remove From Dictionary    ${ilo_details}    ilo_ip   ${iloip}

Cleanup OV
    [Documentation]    Cleans up OV
    [Tags]  teardown
    Set Log Level    TRACE

    Clean OV    ${Storage_Volume_uri}    ${Volume_Name}    ${Storage_System_uri}    ${san_manager_uri}    ${Host_Name_List}

*** Keywords ***

Steps for Redundant bay type
    [Documentation]    These steps are going to set icmap templates if the respective bay position is in Redundant bay type
    [Arguments]    ${Current_position_scope}  ${resource_uri}
    Set Log Level    TRACE

    Set To Dictionary  ${interconnectBayMappings[${Current_position_scope}]}  logicalInterconnectGroupUri  ${resource_uri}
    ${Current_position_scope}  Evaluate  ${Current_position_scope}+1
    Set To Dictionary  ${interconnectBayMappings[${Current_position_scope}]}  logicalInterconnectGroupUri  ${resource_uri}
    ${Current_position_scope}  Evaluate  ${Current_position_scope}+1
    [Return]  ${Current_position_scope}

Steps for NonRedundantASide bay type
    [Documentation]    These steps are going to set icmap templates if the respective bay position is in NonRedundantASide bay type
    [Arguments]  ${Current_position_scope}  ${resource_uri}
    Set Log Level    TRACE

    Set To Dictionary  ${interconnectBayMappings[${Current_position_scope}]}  logicalInterconnectGroupUri  ${resource_uri}
    ${Current_position_scope}  Evaluate  ${Current_position_scope}+1
    [Return]  ${Current_position_scope}

Steps for NonRedundantBSide bay type
    [Documentation]    These steps are going to set icmap templates if the respective bay position is in NonRedundantBSide bay type
    [Arguments]  ${Current_position_scope}  ${resource_uri}
    Set Log Level    TRACE

    Set To Dictionary  ${interconnectBayMappings[${Current_position_scope}]}  logicalInterconnectGroupUri  ${resource_uri}
    ${Current_position_scope}  Evaluate  ${Current_position_scope}+1
    [Return]  ${Current_position_scope}

Create uls in LIG
    [Documentation]    Creating Uplinkset with network in LIG through rest calls
    [Arguments]    ${LIG_uri}    ${FC_uri}    ${uls_name}    ${desiredSpeed}    ${IC_bay_set}    ${ports}
    Set Log Level    TRACE

    ${port_list}  Create List
    ${resp}  fusion_api_get_lig  uri=${LIG_uri}
    Log to console and logfile  ${resp}
    #Set To Dictionary  ${lig_uls_body1}  fcMode  ${fcMode}
    Set To Dictionary  ${lig_uls_body1}  name  ${uls_name}
    Append To List  ${lig_uls_body1['networkUris']}  ${FC_uri}
    ${ports_length}  Get Length  ${ports}
    :FOR  ${x}  IN RANGE  0  ${ports_length}
    \  Set To Dictionary  ${logicalPortConfigInfos[${x}]}  desiredSpeed  ${desiredSpeed}
    \  Set To Dictionary  ${logicalPortConfigInfos[${x}]['logicalLocation']['locationEntries'][0]}  relativeValue  ${IC_bay_set}
    \  ${tmp_list}  Create List
    \  ${tmp_var}  Copy Dictionary  ${logicalPortConfigInfos[${x}]}
    \  Set To Dictionary  ${tmp_var['logicalLocation']['locationEntries'][1]}  relativeValue  ${ports[${x}]}
    \  Append To List  ${port_list}  ${tmp_var}
    Log to console and logfile  ${port_list}
    Set To Dictionary  ${lig_uls_body1}  logicalPortConfigInfos  ${port_list}
    Log to console and logfile  ${lig_uls_body1}
    Remove From Dictionary   ${resp}   headers    status_code
    Append to List  ${resp['uplinkSets']}  ${lig_uls_body1}
    ${resp1}  Fusion Api Edit Lig  ${resp}  ${LIG_uri_list[0]}
    ${task}  Wait For Task  ${resp1}  60s  2s
    Remove From List  ${lig_uls_body1['networkUris']}  0

Manage Storage System And Storage Pools
    [Documentation]    Adds a Storage system in connected state
    [Arguments]     ${Storage_System_uri}
    Set Log Level    TRACE

    ${Get_Response}    Fusion Api Get Storage System    uri=${Storage_System_uri}
    Remove From Dictionary    ${Get_Response}    status_code    headers
    Set To Dictionary    ${Get_Response['deviceSpecificAttributes']}    managedDomain    ${domain}
    ${pool_value}    Remove From List    ${Get_Response['deviceSpecificAttributes']['discoveredPools']}    1
    ${Storage_Pool_Name}    Set Variable    ${pool_value['name']}
    Append To List    ${Get_Response['deviceSpecificAttributes']['managedPools']}    ${pool_value}
    ${Response}    Fusion Api Update Storage System    body=${Get_Response}    uri=${Storage_System_uri}
    ${task} =     Wait For Task        ${Response}   60sec
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    msg=\nUnable to update the storage system with Error Message ${task['taskErrors'][0]['errorCode']}
    ...         ELSE    Log to Console    \nSuccessfully updated the Storage System state.
    [Return]    ${Storage_Pool_Name}

Create Storage Volume
    [Documentation]    Adds a Storage system in connected state
    [Arguments]     ${Storage_volume_data}    ${Storage_Pool_Uri}    ${volume_template_uri}    ${volume_count}    ${Volume_size}
    Set Log Level    TRACE

    ${Storage_Volume_uri}    Create List
    : FOR    ${x}    IN RANGE    0    ${volume_count}
    \    ${count}    Evaluate   ${x}+1
    \    Log to console    \ncount is ${count}
    \    Set To Dictionary    ${Storage_volume_data['properties']}    name    storage_volume_${count}
    \    Set To Dictionary    ${Storage_volume_data['properties']}    storagePool    ${Storage_Pool_Uri}
    \    Set To Dictionary    ${Storage_volume_data['properties']}    snapshotPool    ${Storage_Pool_Uri}
    \    Set To Dictionary    ${Storage_volume_data['properties']}    size    ${Volume_size[${x}]}
    \    Set To Dictionary    ${Storage_volume_data}    templateUri    ${volume_template_uri}
    \    Log to Console    \ndata is ${Storage_volume_data}
    \    ${Resp}    Fusion Api Create Storage Volume    ${Storage_volume_data}
    \    ${task} =     Wait For Task        ${Resp}   90sec
    \    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    msg=\nUnable to create storage volume
    \    ...         ELSE    Append to List    ${Storage_Volume_uri}    ${task['associatedResource']['resourceUri']}
    [Return]    ${Storage_Volume_uri}


Verify Presence Of Volume In 3PAR
    [Documentation]    Verifying the created volume existence
    [Arguments]     ${Volume_Name}    ${Storage_System_Cred}    ${flag}=True
    Set Log Level    TRACE

    Open Connection     ${Storage_System_Cred['hostname']}    timeout=20s
    ${login}    Login    ${Storage_System_Cred['username']}     ${Storage_System_Cred['password']}
    Write     showvv
    Sleep    10sec
    ${stdout} =  Read
    Log to Console    \nout is ${stdout}
    Run Keyword If  '${flag}' == 'True'    Run Keywords    Should Contain    ${stdout}     ${Volume_Name}    AND    Log to Console    \nVoulme ${Volume_Name} is present in 3PAR
    ...    ELSE IF    '${flag}' == 'False'    Run Keywords    Should Not Contain    ${stdout}     ${Volume_Name}    AND    Log to Console    \nVoulme ${Volume_Name} is not present in 3PAR
    Close All Connections


Verifying the status of the services
    [Documentation]    Verifying the status of the services
    [Arguments]     ${Storage_System_Cred}   ${command}
    Set Log Level    TRACE

    ${Service_Dict}    Create Dictionary
    Open Connection    ${Storage_System_Cred['hostname']}
    Login    ${Storage_System_Cred['username']}     ${Storage_System_Cred['password']}
    Write    ${command}
    Sleep    5sec
    ${Output}=    Read
    ${Output1}    Convert To String    ${Output}
    ${str}    Replace String    ${Output1}    -    ${EMPTY}
    @{Lines}   Split To Lines    ${str}
    @{Key}    Split String    ${Lines[0]}
    @{Value}    Split String    ${Lines[1]}
    Set To Dictionary   ${Service_Dict}     ${Key[0]}    ${Value[0]}
    Set To Dictionary   ${Service_Dict}     ${Key[1]}    ${Value[1]}
    Log to console     ${Service_Dict}
    [Return]      ${Service_Dict}

Verifying Presence Of Host In 3PAR
    [Documentation]    Verifying the Presence of created Host in 3PAR
    [Arguments]     ${Host_Name_List}    ${Storage_System_Cred}    ${flag}=True
    Set Log Level    TRACE

    Open Connection    ${Storage_System_Cred['hostname']}
    Login    ${Storage_System_Cred['username']}     ${Storage_System_Cred['password']}
    Write    showhost
    Sleep    10sec
    ${output} =  Read
    Log to Console    ${output}
    Run Keyword If  '${flag}' == 'True'    Run Keywords    Should Contain    ${output}     ${Host_Name_List}    AND    Log to Console    \nHOST::${Host_Name_List} is present in 3PAR
    ...    ELSE IF    '${flag}' == 'False'    Run Keywords    Should Not Contain    ${output}     ${Host_Name_List}    AND    Log to Console    \nVoulme ${Host_Name_List} is not present in 3PAR
    Close All Connections

LI update from Group
    [Documentation]    Performing update from group in LI through rest call
    [Arguments]  ${LE}  ${LIG}
    Set Log Level    TRACE

    ${li_uri}  Get LI URI  ${LE}-${LIG}
    Set Global Variable  ${LI_uri}  ${li_uri}
    ${resp_update}  Fusion Api Update From Group  ${LI_uri}
    Run keyword unless  ${resp_update['status_code']}== 202  Fail  ${resp_update['message']}
    ${task}  Wait For Task  ${resp_update}  20min
    Sleep  60s
    Log to console and logfile  LI updated from group successfully.

LUN Count and IO Traffic
    [Documentation]    Verifying of LUN and Passing IO Traffic
    [Arguments]   ${iloip}   ${linux_details}    ${ilo_details}    ${server_details}    ${module_file_path}
    Set Log Level    TRACE

    ${disk_count}=    lun_discovery    ${linux_details}    ${ilo_details}    ${server_details}    ${module_file_path}
    ${len}    Get Length    ${disk_count}
    ${count}    Evaluate    ${len}-1
    Log to console and logfile    COUNT OF LUN : ${count}


    Log to Console and Logfile   \nStarting IO traffic\n
    ${cmd}   ${out_file}      ${msg}=   executes    ${linux_details}    ${ilo_details}  ${server_details}   ${module_file_path1}    "${diskspd_cmd_60s}"
    Log to Console and Logfile     outfile::: ${out_file}
    Run keyword unless   '${msg}'== 'PASS'   Fail   "Unable to Start the IO Traffic"    Log To Console   \nThe IO Traffic Details are as follows:\n
    Log to Console and Logfile   \nStarted IO traffic\nCommand--${cmd}\nOutputFile--${out_file}\n

    Sleep   60s

    Log to Console and Logfile   \nVerifying IO traffic\n
    ${cmd}    ${exeout}     ${msg}=     ioresults       ${linux_details}    ${ilo_details}  ${server_details}   ${module_file_path2}    "${out_file}"
    Log to Console and Logfile     exeout::: ${exeout}
    Run keyword unless  '${msg}'== 'PASS'   Fail    "Unable to Finish the IO Traffic"   Log To Console   \nThe IO Traffic Details are as follows:\n
    Log to Console and Logfile   \nIO traffic Success!!\nCommand--${cmd}\nOutput--${exeout}\n

Remove Storage Volume
    [Documentation]    Removing the Storage Volume
    [Arguments]    ${Storage_Volume_uri}
    Set Log Level    TRACE
    ${Resp}    Fusion Api Get Storage Volumes    uri=${Storage_Volume_uri}
    ${headers}  Get From Dictionary     ${Resp}    headers
    ${eTag}    Get From Dictionary     ${Resp}    eTag
    Set To Dictionary    ${headers}    If-Match=${eTag}
    ${Respone}    Fusion Api Delete Storage Volume    uri=${Storage_Volume_uri}    headers=${headers}
    ${task} =     Wait For Task        ${Respone}    30sec
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    msg=\nUnable to delete storage volume
    ...         ELSE    Log to Console    \n Successully deleted Storage Volume

Remove Storage System
    [Documentation]    Removing the Storage System
    [Arguments]    ${Storage_System_uri}
    Set Log Level    TRACE

    ${Resp}    Fusion Api Get Storage Volumes    uri=${Storage_System_uri}
    ${headers}  Get From Dictionary     ${Resp}    headers
    ${eTag}    Get From Dictionary     ${Resp}    eTag
    Set To Dictionary    ${headers}    If-Match=${eTag}
    ${Respone}    Fusion Api Delete Storage System    uri=${Storage_System_uri}    headers=${headers}
    ${task} =     Wait For Task        ${Respone}    30sec
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200    fail    msg=\nUnable to delete storage System
    ...         ELSE    Log to Console    \n Successully deleted Storage System

Remove SAN Manager
    [Documentation]    Removing the SAN Manager
    [Arguments]    ${san_manager_uri}
    Set Log Level    TRACE

    ${Resp}    fusion_api_get_san_manager
    Log to Console    ${Resp}
    ${Respone}    fusion_api_remove_san_manager    uri=${san_manager_uri}
    ${task} =     Wait For Task        ${Respone}    30sec
    Run Keyword If  '${task['taskState']}' !='Completed'  or  ${task['status_code']} !=200    fail    msg=\nUnable to delete SAN manager
    ...         ELSE    Log to Console    \n Successully deleted San Manager

Get Server iLO IP
    [Documentation]    Keyword to retrieve iLO IP for server bay
    [Arguments]    ${bay_no}
    ${server_info}=    Get Server Info    ${bay_no}
    ${ilo_ip}=    Get Server iLO Address    ${server_info}
    [Return]    ${ilo_ip}


Get Server iLO Address
    [Documentation]    Keyword to retrieve iLO IP for server bay
    [Arguments]    ${server_bay_info}
    ${mpHostInfo}=    Get From Dictionary    ${server_bay_info}    mpHostInfo
    ${mpIpAddresses} =    Get From Dictionary    ${mpHostInfo}    mpIpAddresses
    ${l} =  Get Length  ${mpIpAddresses}
    :FOR    ${x}    IN RANGE    0   ${l}
    \    ${enc} =    Get From List    ${mpIpAddresses}    ${x}
    \    ${type}=    Get From Dictionary    ${enc}    type
    \    Run Keyword If    '${type}'!='DHCP'    Continue For Loop
    \    ${address}=    Get From Dictionary     ${enc}    address
    [Return]    ${address}

Clean OV
    [Documentation]    Tear-down - Cleans up OneView.
    [Arguments]   ${Storage_Volume_uri}    ${Volume_Name}    ${Storage_System_uri}    ${san_manager_uri}    ${Host_Name_List}
    Set Log Level    TRACE

    ${vol_len}    Get Length    ${Volume_Name}
    ${host_len}    Get Length    ${Host_Name_List}

    Power off ALL Servers
    Remove All Server Profiles

    Remove All Logical Enclosures
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Remove ALL FC Networks

    Log to Console    \nRemove Storage volume from OV and 3PAR
    : FOR    ${x}    IN RANGE    0    ${vol_len}
    \    Remove Storage Volume    ${Storage_Volume_uri[${x}]}
    \    Log to Console    \nVerify If Volume is deleted from 3PAR
    \    Verify Presence Of Volume In 3PAR    ${Volume_Name[${x}]}    ${Storage_System_Cred}    False

    Log to Console    \nRemove Host from OV and 3PAR
    : FOR    ${x}    IN RANGE    0    ${host_len}
    \    Log to Console    \nVerify If Host is deleted from 3PAR
    \    Verifying Presence Of Host In 3PAR   ${Host_Name_List[${x}]}    ${Storage_System_Cred}    False

    Log to Console    \nRemove Storage system from OneView
    Remove Storage System    ${Storage_System_uri}
    Remove SAN Manager    ${san_manager_uri}

Initial Cleanup
    [Documentation]    Initial Clean up.
    Set Log Level    TRACE

    Power off ALL Servers
    Remove All Server Profiles
    Remove All Logical Enclosures
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Remove ALL FC Networks