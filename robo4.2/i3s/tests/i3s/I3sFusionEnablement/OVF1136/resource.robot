*** Settings ***
Library           json
Library           copy
Resource          ${fusion_api_resource}
Resource          ../Resources/api/resource.robot
Variables         ./ovf_1136_me_data.py
Variables         ./environment_data.py
Variables         ../../../testdata/i3s_QA_testdata.py

*** Variables ***
${fusion_api_resource}    ../fusion/Resources/api/fusion_api_resource.txt
${X-API-VERSION}    1000
#Since compliance control json is newly added in 4.2 and it takes only the api version as 1000. We have made entire OVF1136 to run with x-api version as 1000 for SP and SPT
${blnVerifyPreReqs}    False
@{allResourcesCommonList}    ethernets    egs    servers    osdps
${profileTemplate}    OVF1136_SPT

*** Keywords ***

Ping IP
    [Arguments]    ${host}
    ${resp}  ${ping_output} =  Run And Return Rc And Output  ping -n 4 ${host}
    Return From Keyword If    ${resp} == 0  ${true}
    [Return]

Create Serverprofile Template from Serverprofile
    [Documentation]    create server profie template from server profile
    [Arguments]    ${response}
    Set log level  TRACE
    ${NAME} =    Get From Dictionary    ${response}    name
    Log To Console    \n\nServer Profile to be updated is: ${NAME}
    ${SP_json} =    Fusion API Get Server Profiles    param=?filter='name'=='${NAME}'
    ${SP_members_list} =    Get from Dictionary    ${SP_json}    members
    ${SP_members_dict} =    Convert to Dictionary    @{SP_members_list}
    # Get the SP uri, to be used next in update call
    ${SP_uri} =    Get from Dictionary    ${SP_members_dict}    uri
    Log To Console    \n\nURI of the SP is: ${SP_uri}
    ${SPT_Request_body} =    Fusion API Get Server Profiles    uri=${SP_uri}    param=/new-profile-template
    ${SPT_members_dict} =    Convert to Dictionary    ${SPT_Request_body}
    # Get the value of name  from the SPT_from_SP json
    ${SP_name} =    Get from Dictionary    ${sp_from_spt}    name
    Set to Dictionary    ${SPT_members_dict}    name    ${SP_name}
    # Get call with new-profile-template returns all members in a dictionary , it does not have members field separately
    # SPT_members_dict contains dict members with status_code and headers which is not
    # required for the SPT create, hence removing the same
    Remove From Dictionary    ${SPT_members_dict}    status_code
    Remove From Dictionary    ${SPT_members_dict}    headers
    ${Response} =    Fusion API Create Server Profile Template    ${SPT_members_dict}
    Should Be Equal as Strings    ${Response['status_code']}          202             msg=Failed to initiate Create SPT
    # Wait for task to complete
    ${Retry Interval}    Convert To Number     60
    ${Retries}           Convert To Integer    5
    ${Response} =    Fusion API Wait For Task To Complete    ${Response['headers']['Location']}    sleep_time=${Retry Interval}    retries=${Retries}
    # Check for errors
    ${Errors}=    Get From Dictionary    ${Response}    taskErrors
    ${Errors_count} =    Get Length    ${Errors}
    Run Keyword If    ${Errors_count} == 0    Log to console    \nSuccessfully created server profile template from server profile
    ...    ELSE    Fail    msg=Errors encountered while creating Server Profile Template from server profile...\n${Errors}

Copy Server profile
    [Documentation]    Copy server profile to different server hardware with SPT and OSDP
    [Arguments]    ${profile}    ${server}    ${spcopy}
    ${sp_resp}=    Get Server Profile    ${profile}
    Power Off Profile Server    ${server['serverHardwareUri']}
    ${shUri} =    Get Server Hardware URI    ${server['serverHardwareUri']}
    Set To Dictionary    ${sp_resp}    serverHardwareUri=${shUri}
    ${SP_name} =    Get from Dictionary    ${spcopy}    name
    Set to Dictionary    ${sp_resp}    name=${SP_name}
    Remove From Dictionary    ${sp_resp}    enclosureBay    enclosureUri    templateCompliance    serialNumber    serialNumberType    uuid
    #osDeploymentSettings
    ${status}  ${return} =  Run Keyword and Ignore Error    Get From Dictionary    ${spcopy}    osDeploymentSettings
    ${osDeploymentSettings} =  set variable if  '${status}'=='PASS'  ${return}  error
    ${osDeploymentSettings} =   run keyword if  '${status}'=='PASS' and ${osDeploymentSettings}!=${None}    Set OS Deployment settings    ${osDeploymentSettings}
    ${sp_resp} =    Run keyword if  '${status}'=='PASS' and ${osDeploymentSettings}!=${None}    Set to Dictionary   ${sp_resp}  osDeploymentSettings    ${osDeploymentSettings}
    # change port ID to Auto
    ${connection_settings}=    Get From Dictionary    ${sp_resp}    connectionSettings
    ${connections} =    Get From Dictionary    ${connection_settings}    connections
    ${count}=  Get Length    ${connections}
    :FOR    ${conn_index}    IN Range    0    ${count}
    \    Set To Dictionary    ${connections[${conn_index}]}    mac=${None}
    ${resp}=    Fusion API Create Server Profile    ${sp_resp}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    [Return]    ${blnStatus}

Copy Server profile by changing osdp and removing connection
    [Documentation]    Copy server profiles to different server hardware with SPT and OSDP
    [Arguments]    ${profile}    ${server}    ${spcopy}
    ${sp_resp}=    Get Server Profile    ${profile}
    Power Off Profile Server    ${server['serverHardwareUri']}
    ${shUri} =    Get Server Hardware URI    ${server['serverHardwareUri']}
    Set To Dictionary    ${sp_resp}    serverHardwareUri=${shUri}
    ${SP_name} =    Get from Dictionary    ${spcopy}    name
    Set to Dictionary    ${sp_resp}    name=${SP_name}
    Remove From Dictionary    ${sp_resp}    enclosureBay    enclosureUri    templateCompliance    serialNumber    serialNumberType    uuid
    # change port ID to Auto
    ${connection_settings}=    Get From Dictionary    ${sp_resp}    connectionSettings
    ${connections} =    Get From Dictionary    ${connection_settings}    connections
    ${count}=  Get Length    ${connections}
    :FOR    ${conn_index}    IN Range    0    ${count}
    \    Set To Dictionary    ${connections[${conn_index}]}    mac=${None}
    ${resp}=    Fusion API Create Server Profile    ${sp_resp}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    Log    \n Remove connection to profile    console=True
    ${spbody}=    Get Server Profile    ${sp_resp['name']}
    ${sp_uri}=    Get from dictionary    ${spbody}    uri
    #osDeploymentSettings
    ${status}  ${return} =  Run Keyword and Ignore Error    Get From Dictionary    ${spcopy}    osDeploymentSettings
    ${osDeploymentSettings} =  set variable if  '${status}'=='PASS'  ${return}  error
    ${osDeploymentSettings} =   run keyword if  '${status}'=='PASS' and ${osDeploymentSettings}!=${None}    Set OS Deployment settings    ${osDeploymentSettings}
    ${spbody} =    Run keyword if  '${status}'=='PASS' and ${osDeploymentSettings}!=${None}    Set to Dictionary   ${spbody}  osDeploymentSettings    ${osDeploymentSettings}
    ${connections}=    Get from dictionary    ${spbody['connectionSettings']}    connections
    Log    ${connections}
    ${connections_length}=     Get length      ${connections}
    :For    ${index}   IN RANGE    0    ${connections_length}
    \    Run Keyword If    '${connections[${index}]['name']}' == 'Deployment Network D'    Remove from List    ${connections}    ${index}

    Log    ${spbody}
    ${response}=    Fusion API Edit Server Profile    ${spbody}    ${sp_uri}
    Wait For Task2    ${response}    timeout=2400    interval=20
    [Return]    ${blnStatus}

Verify Compliance Alert
    [Documentation]    Verify compliance alert when SP is inconsistent with SPT
    [Arguments]    ${profile}
    ${sp_complaince} =    Get Server Profile    ${profile['name']}
    ${compliance} =    Get SP_Compliancepreview    ${profile['name']}
    ${msg} =    Get From Dictionary    ${compliance}    automaticUpdates
    ${msg_1} =    Get From List    ${msg}    0
    ${compl_preview_count}=    Get Length    ${msg_1}
    Run Keyword If    '${compl_preview_count}' != '0' and '${sp_complaince['templateCompliance']}' == 'NonCompliant'    Log to console    \nSuccessfully created server profile.. compliance preview message ${msg_1} displayed successfully..\n
    ...    ELSE    Fail    msg=Successfully created server profile but without any compliance preview messages.

Delete Server Profile Template
    [Documentation]    To delete SPT
    [Arguments]    ${profile}
    ${NAME}=    Get From Dictionary    ${profile}    name
    Log To Console    \nDeleting Server Profile Template ${NAME}
    ${Response} =    Fusion API Delete Server Profile Template    ${NAME}
    Log to console    ${Response}

Perform deploy operation
    [Documentation]    To power on/off and verify ping function
    [Arguments]    ${serverprofile}
    Power On Profile Server    ${serverprofile['serverHardwareUri']}
    Log to console    ${serverprofile['serverHardwareUri']}
    #Get i3s Appliance Cluster IP and Login to i3s appliance
    ${resp} =    Fusion Api Get i3sCluster IP
    ${i3S_IP} =    Get From Dictionary    ${resp['members'][0]}    primaryIPV4
    Log to console    ${i3S_IP}
    Login to Appliance via SSH    ${i3S_IP}    ${SSHUSER}    ${SSHPASSWORD}    ${TIMEOUT}
    ${mgmt_ip} =    Get Server Profile Management IP    ${serverprofile}
    Ping Profile Management IP    ${mgmt_ip}
    Power Off Profile Server    ${serverprofile['serverHardwareUri']}
    Sleep    50
