*** Settings ***
Library            FusionLibrary

*** Keywords ***
Create I3S Server Profile
    [Documentation]    Create I3S Profile (includes Os Deployment Settings)
    [Arguments]    ${serverprofile}    ${status_code}=202
    ${sp}=  copy.deepcopy  ${serverprofile}
    Log    \nCreating Server Profile: ${sp['name']}    console=yes
    Run Keyword If    '${sp['serverHardwareUri']}' != 'None'    Power Off Profile Server    ${sp['serverHardwareUri']}
    ${sp_body}=    Create Server Profile POST Payload    ${sp}
    ${resp}=    Fusion API Create Server Profile    ${sp_body}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    [Return]    ${blnStatus}

Create I3S unassigned Server Profile
    [Documentation]    Create I3S Unassigned Profile (includes Os Deployment Settings)
    [Arguments]    ${serverprofile}
    ${sp1}=  copy.deepcopy  ${serverprofile}
    Log    \nCreating unassign Server Profile: ${sp1['name']}    console=yes
    Remove From Dictionary    ${sp1}    serverHardwareUri
    Remove From Dictionary    ${sp1}    enclosureUri
    Log    \nCreating Server Profile: ${sp1['name']}    console=yes
    ${sp_body}=    Create Server Profile POST Payload    ${sp1}
    ${response}=    Fusion API Create Server Profile    ${sp_body}
    ${blnStatus}=    Capture Task Status    ${response}    1200
    [Return]    ${blnStatus}

Unassign I3S Server Profile
    [Documentation]    Edit profile and Unassign
    [Arguments]        ${serverprofile}    ${param}=?ignoreServerHealth=true  ${headers}=${None}    ${api}=${None}
    Log    \nUnassigning Server Profile: ${serverprofile}    console=yes
    ${sp_resp} =    Get Server Profile    ${serverprofile}
    Remove from Dictionary    ${sp_resp}    serverHardwareUri    enclosureUri    enclosureBay
    ${resp} =  Fusion Api Edit Server Profile  body=${sp_resp}  uri=${sp_resp['uri']}  param=?ignoreServerHealth=true  api=${api}  headers=${headers}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    [Return]    ${blnStatus}

Edit I3S Server Profile
    [Documentation]    Edit I3S Server Profile
    [Arguments]    ${serverprofile}    ${param}=?ignoreServerHealth=true  ${headers}=${None}    ${api}=${None}
    ${sp3}=  copy.deepcopy  ${serverprofile}
    Log    \nEditing Server Profile: ${sp3['name']}    console=yes
    ${sp_name} =     Get from Dictionary    ${sp3}    name
    ${payload} =  Create Server Profile Put Payload    ${sp3}

    # append profile type dynamically
    ${default_type} =    Get Server Profile Type
    ${status}    ${return}    Run Keyword and Ignore Error    Get From Dictionary    ${payload}    type
    ${type} =    Set Variable If    '${status}'=='PASS'    ${return}    ${default_type}
    Set to Dictionary    ${payload}    type    ${type}

    ${profile_dto} =     Get Resource  SP:${sp_name}
    ${profile_etag} =     Get From Dictionary        ${profile_dto}    eTag
    ${profile_uri} =  Get From Dictionary        ${profile_dto}    uri
    Set to dictionary    ${payload}    eTag    ${profile_etag}
    ${resp} =  Fusion Api Edit Server Profile  body=${payload}  uri=${profile_uri}  param=${param}  api=${api}  headers=${headers}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    [Return]    ${blnStatus}

Append SPT Uri to Profile Payload
    [Documentation]    Append SPT Uri to Profile Payload
    [Arguments]    ${payload}
    ${status}  ${return} =  Run Keyword and Ignore Error  Get From Dictionary  ${payload}  serverProfileTemplateUri
    ${spt} =  set variable if  '${status}'=='PASS'  ${return}  error
    ${spt_uri} =  run keyword if  '${status}'=='PASS' and '${spt}'!=''   Common URI Lookup by name  ${spt}
    run keyword if  '${status}'=='PASS' and '${spt}'!=''  Set to Dictionary    ${payload}    serverProfileTemplateUri    ${spt_uri}
    [Return]    ${payload}

Power Off Profile Server
    [Documentation]  Power Off Profile Server
    [Arguments]      ${server}
    ${server}=    replace string using regexp    ${server}    SH:    ${EMPTY}
    ${powerstate}=    Get Server Power    ${server}
    Run Keyword if   '${powerstate}' == 'On'   Power off Server  ${server}
    ...    ELSE    Log    \nServer '{${server}}' is already powered off

Power On Profile Server
    [Documentation]  Power On Profile Server
    [Arguments]      ${server}
    ${server}=    replace string using regexp    ${server}    SH:    ${EMPTY}
    ${powerstate}=    Get Server Power    ${server}
    Run Keyword if   '${powerstate}' == 'Off'   Power on Server  ${server}
    ...    ELSE    Log    \nServer '{${server}}' is already powered on

Get Server Profile
    [Documentation]    Get Server Profile by Name
    [Arguments]    ${ServerProfileName}
    ${ServerProfileCollection}=    Fusion Api Get Server Profiles
    Return From Keyword If  ${ServerProfileCollection['count']}==0  /rest/server_profile_uri_${ServerProfileName}_not_found
    @{members}=    Get From Dictionary    ${ServerProfileCollection}    members

    :FOR    ${member}    IN    @{members}
    \    ${name}=     Get From Dictionary    ${member}          name
    \    Continue For Loop If    '${ServerProfileName}'!='${name}'
    \    Return From Keyword    ${member}
    [Return]

Delete Server Profile
    [Documentation]    Delete if profile you want delete
    ...    is already exist
    [Arguments]    ${sp_name}    ${param}=${True}
    ${profile_uri}=    Get Server Profile URI    ${sp_name}
    ${msg}=  Get Substring  ${profile_uri}  -10
    Return From Keyword If  '${msg}'=='_not_found'
    Log    \nDeleting Server Profile '${sp_name}'    console=True
    ${resp} =  Run Keyword If  '${profile_uri}'!='None'    Fusion Api Delete Server Profile    uri=${profile_uri}    param=?force=${param}
    ${task} =  Run Keyword If  '${profile_uri}'!='None'    Wait For Task    ${resp}    420s    10s
    ${profileFound} =  Check Resource Existing  SP:${sp_name}
    Run Keyword If    ${profileFound}=='FAIL'   Log    \n...profile ${sp_name} deleted successfully    console=True
    ...    ELSE IF    ${profileFound}=='PASS'    Fail    msg=Server Profile '${sp_name}' still exists

Get Server Profile Management IP
    [Documentation]  Get Server Profile Management IP
    [Arguments]  ${server_profile}
    ${sp_body}=  Get Server Profile    ${server_profile['name']}
    ${osCustomAttributes}=  Get From Dictionary  ${sp_body['osDeploymentSettings']}  osCustomAttributes
    :For  ${attribute}  IN  @{osCustomAttributes}
    \    Continue For Loop If  '${attribute['name']}'!='ManagementNIC.ipaddress'
    \    ${mngt_ip}=  Run KeyWord If  '${attribute['name']}'=='ManagementNIC.ipaddress'  Get From Dictionary  ${attribute}  value
    \    Exit For Loop If  '${attribute['name']}'=='ManagementNIC.ipaddress'
    Log  \nServer profile '${server_profile['name']}' management IP '${mngt_ip}'  console=True
    [Return]  ${mngt_ip}

Get OS Volume From Server Profile
    [Documentation]    Get OS Volume From Server Profile
    [Arguments]    ${spname}
    ${sp_body}=    Get Server Profile    ${spname}
    ${OSDS}=    Get from Dictionary    ${sp_body}    osDeploymentSettings
    ${osvol}=    Get from Dictionary    ${OSDS}    osVolumeUri
    Return From Keyword If    '${osvol}' == 'None'
    ${resp} =    Get Resource by URI    ${osvol}
    Log    \nVolume '${resp['osVolumeName']}' is attached to Server profile '${spname}'    console=True
    [Return]    ${resp['osVolumeName']}

Get Server Profile OS Volume URI
    [Documentation]    Get OS Volume From Server Profile
    [Arguments]    ${spname}
    ${sp_body}=    Get Server Profile    ${spname}
    ${OSDS}=    Get from Dictionary    ${sp_body}    osDeploymentSettings
    ${osVolumeUri}=    Get from Dictionary    ${OSDS}    osVolumeUri
    [Return]    ${osVolumeUri}

Change Server Profile OSDP To None
    [Documentation]    Edit server profile and Change OS Delployment plan to None
    [Arguments]    ${serverprofile}

    Log    \nChanging profile '${serverprofile}' OSDP to None    console=True

    ${spbody} =    Get Server Profile    ${serverprofile}
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
    [Return]    ${blnStatus}

Change Server Profile OSDP
    [Documentation]    Edit server profile and Change OS Delployment plan to None
    [Arguments]    ${serverprofile}    ${osdp}=${None}

    Log    \nChanging profile '${serverprofiles['name']}' OSDP to ${osdp}    console=True
    ${osdp_Uri} =   Run Keyword If    '${osdp}' != 'None'    Get OSDP URI    ${osdp}
    ...    ELSE    Set Variable    ${osdp}

    ${spbody} =    Get Server Profile    ${serverprofile}
    Set To Dictionary    ${spbody['osDeploymentSettings']}    osDeploymentPlanUri=${osdp_Uri}
    ${resp} =    Fusion API Edit Server Profile    ${spbody}    ${spbody['uri']}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    [Return]    ${blnStatus}

Delete iscsi connection From SP
    [Documentation]    Edit server profile and Delete iscsi connection From SP
    [Arguments]    ${serverprofile}

    Log    \nDeleting iscsi connection from '${serverprofile}'    console=True
    ${spbody} =    Get Server Profile    ${serverprofiles['name']}

    Set To Dictionary    ${spbody}    osDeploymentSettings    ${null}
    Set To Dictionary    ${spbody}    iscsiInitiatorName    ${null}
    ${connection_settings}=    Get From Dictionary    ${spbody}    connectionSettings
    ${connections} =    Get From Dictionary    ${connection_settings}    connections
    ${count}=  Get Length    ${connections}
    :FOR    ${conn_index}    IN Range    0    ${count}
    \    Set ipv4 Connection attributes to None    ${connections[${conn_index}]['ipv4']}
    \    Set Boot attributes to None    ${connections[${conn_index}]['boot']}
    ${resp} =    Fusion API Edit Server Profile    ${spbody}    ${spbody['uri']}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    [Return]    ${blnStatus}

Set ipv4 Connection attributes to None
    [Documentation]    Set ipv4 attributes of connection to None
    [Arguments]    ${ipv4}
    ${type}    Evaluate    type(${ipv4})
    Return From Keyword If    "${type}"!="<type 'dict'>"
    ${ipv4_attrib} =    Get Dictionary Keys    ${ipv4}
    :FOR    ${attrib}    IN    @{ipv4_attrib}
    \    Set To Dictionary    ${ipv4}    ${attrib}    ${null}

Set Boot attributes to None
    [Documentation]    Set Boot attributes to None
    [Arguments]    ${boot_attributes}

    ${attributes} =    Get Dictionary Keys    ${boot_attributes}
    :For    ${attribute}    IN    @{attributes}
    \    Run Keyword If    "${attribute}"!="iscsi"    Set To Dictionary    ${boot_attributes}    ${attribute}=${None}
    \    ...    ELSE    Set iscsi Connection attributes to None    ${boot_attributes['${attribute}']}

Set iscsi Connection attributes to None
    [Documentation]    Set iscsi Connection attributes to None
    [Arguments]    ${iscsi_attributes}

    ${attributes} =    Get Dictionary Keys    ${iscsi_attributes}
    :For    ${iscsi_attribute}    IN    @{attributes}
    \    Set To Dictionary    ${iscsi_attributes}    ${iscsi_attribute}=${None}

Get OS Attribute Values from Profile Response
    [Documentation]    Get Attribute Value From server profile
    [Arguments]    ${sp_body}    ${attributes}
    ${payload} =    copy.deepcopy    ${sp_body}
    ${osds} =     Get From Dictionary    ${payload}    osDeploymentSettings
    ${os_ca} =    Run Keyword If    ${osds} != None    Get From Dictionary    ${osds}    osCustomAttributes
    ...    ELSE  Create List
    ${attrib_value} =    Create List
    :FOR    ${attrib}    IN    @{attributes}
    \    ${ca_val} =    Get Attribute Value From OSCA    ${os_ca}    ${attrib}
    \    Append To List    ${attrib_value}    ${ca_val}
    [Return]    ${attrib_value}

Get Attribute Value From OSCA
    [Documentation]    Get Attribute Value From OSCA
    [Arguments]    ${osca}    ${attrib}
    :FOR    ${ca}    IN    @{osca}
    \    ${ca_name} =    Get From Dictionary    ${ca}    name
    \    ${regex_match} =    Evaluate    re.search(r'${attrib}', '${ca_name}', re.I)    re
    \    ${ca_value} =    Run Keyword If    '${regex_match}' != 'None'    Return From Keyword    ${ca['value']}
    [Return]    None

Ping Profile Management IP
    [Documentation]    Ping Profile Management IP
    [Arguments]    ${ip}    ${retries}=40    ${sleep}=30
    Log    \nPinging host '${ip}'    console=True
    :FOR    ${trial}    IN RANGE    0    ${retries}
    \    ${resp}  ${ping_output} =  Run And Return Rc And Output  ping -n 4 ${ip}
    \    Exit For Loop If    ${resp} == 0
    \    Sleep    ${sleep}
    Run Keyword If    ${resp} == 0  Log  \nIP '${ip}' is reachable  console=True
    ...    ELSE    Fail    msg=IP is not reachable.

Swap Server profile to different Server
    [Documentation]    Move server profile to different server hardware
    [Arguments]    ${profile}    ${server}

    ${sp_resp}=    Get Server Profile    ${profile}

    Power Off Profile Server    ${server['serverHardwareUri']}
    ${shUri} =    Get Server Hardware URI    ${server['serverHardwareUri']}
    Set To Dictionary    ${sp_resp}    serverHardwareUri=${shUri}
    ${shTypeUri} =    Get Server Hardware Type URI    ${server['serverHardwareTypeUri']}
    Set To Dictionary    ${sp_resp}    serverHardwareTypeUri=${shTypeUri}
    Remove From Dictionary    ${sp_resp}    enclosureBay
    Remove From Dictionary    ${sp_resp}    enclosureUri

    # change port ID to Auto
    ${connection_settings}=    Get From Dictionary    ${sp_resp}    connectionSettings
    ${connections} =    Get From Dictionary    ${connection_settings}    connections
    ${count}=  Get Length    ${connections}
    :FOR    ${conn_index}    IN Range    0    ${count}
    \    Run Keyword If    ${connections[${conn_index}]['ipv4']} == ${None}    Set To Dictionary    ${connections[${conn_index}]}    portId=Auto

    ${resp}=    Fusion API Edit Server Profile    ${sp_resp}    ${sp_resp['uri']}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    [Return]    ${blnStatus}

Get SP_Compliancepreview
    [Arguments]    ${SP_name}
    Log to console    Inside compliance check
    ${resp} =    Fusion API Get Server Profiles    param=?filter="name='${SP_name}'"
    ${SP_uri} =    Get From Dictionary    ${resp['members'][0]}    uuid
    Run Keyword If    ${resp['count']} != 0    Log    ${resp['count']} Server Profile[s] are present with name ${SP_name}
    ...    ELSE    Fail    msg=ERROR: No Server Profiles are present with name ${SP_name}
    ${resp_cp} =    Fusion API Get Server Profiles    param=/${SP_uri}/compliance-preview
    [Return]    ${resp_cp}
    