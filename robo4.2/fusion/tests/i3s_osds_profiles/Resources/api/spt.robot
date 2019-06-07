*** Settings ***
Library            FusionLibrary

*** Keywords ***
Create I3S SPT
    [Documentation]    Create I3S SPT (includes Os Deployment Settings)
    [Arguments]    ${profileTemplate}    ${status_code}=202
    ${spt}=  Deep Copy  ${profileTemplate}
    Log    \nCreating Server Profile Template: ${spt['name']}    console=yes
    ${spt_body}=    Create Server Profile Template Payload    ${spt}
    ${resp}=    Fusion Api Create Server Profile Template    ${spt_body}
    ${blnStatus}=    Capture Task Status    ${resp}    120
    [Return]    ${blnStatus}

Create I3S SP from I3S SPT
    [Documentation]    Create SP from SPT with wait task
    [Arguments]    ${sp_payload}
    ${pay_load}=    Create I3S Server Profile POST Payload from SPT    ${sp_payload}
    ${resp}=    Fusion API Create Server Profile    ${pay_load}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    [Return]    ${blnStatus}

Edit I3S SPT
    [Documentation]    Edit Server Profile Template
    [Arguments]    ${profile_template}    ${api}=${None}
    ${name} =    Get from Dictionary    ${profile_template}  name
    Log    \nEditing Server Profile Template ${name}    console=True
    ${payload} =  Create Server Profile Template Payload  ${profile_template}
    ${profile_template_dto} =    Get Resource  SPT:${name}
    ${profile_template_etag} =    Get From Dictionary    ${profile_template_dto}    eTag
    ${profile_template_uri} =  Get From Dictionary    ${profile_template_dto}  uri
    Set to dictionary    ${payload}    eTag    ${profile_template_etag}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${payload}    uri=${profile_template_uri}  api=${api}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    [Return]    ${blnStatus}

Update DeploymentSettings Payload
    [Documentation]    update SPT deployment settings payload
    [Arguments]    ${payload}    ${deploymentSettings}
    remove from dictionary    ${payload['osDeploymentSettings']}    osCustomAttributes
    :FOR    ${os_ca}    IN    @{deploymentSettings['osCustomAttributes']}
    \    ${ca_name} =  Get From Dictionary  ${os_ca}  name
    \    ${regex_match} =  Evaluate  re.search(r'networkuri', '${ca_name}', re.I)    re
    \    Run Keyword If  '${regex_match}' == 'None'  continue For Loop
    \    ${mgmt_nic}=  Get From Dictionary  ${os_ca}  value
    \    @{words}=     Split String  ${mgmt_nic}    :
    \    ${net}=  Get From List  ${words}  1
    \    ${nwuri}=  Get Ethernet URI  ${net}
    \    Log   \n${mgmt_nic} Network URI ${nwuri}
    \    Set to Dictionary  ${os_ca}  value=${nwuri}
    Set To Dictionary    ${payload}    osDeploymentSettings=${deploymentSettings}
    ${osdp_uri}=    Run Keyword If    '${payload['osDeploymentSettings']['osDeploymentPlanUri']}' != 'None'    Get OSDP URI    ${payload['osDeploymentSettings']['osDeploymentPlanUri']}
    Set to Dictionary    ${payload['osDeploymentSettings']}    osDeploymentPlanUri=${osdp_uri}
    [Return]    ${payload}

Create I3S Server Profile POST Payload from SPT
    [Documentation]    Create I3S Server Profile POST payload when SPT is defined.
    [Arguments]        ${profile}    ${api}=${None}
    ${payload} =  copy dictionary  ${profile}
    ${spt} =  Get From Dictionary  ${payload}  serverProfileTemplateUri
    ${spt_uri} =  Common URI Lookup by name  ${spt}
    # get the new payload based on the SPT
    ${new_payload} =  Fusion Api Get Server Profile Template New Profile  ${spt_uri}  api=${api}
    # remove the status_code and headers in the response
    remove from dictionary  ${new_payload}  status_code
    remove from dictionary  ${new_payload}  headers
    # set profile name in the payload
    Set to Dictionary   ${new_payload}  name  ${payload['name']}
    # set serverHardwareUri in the payload
    ${status}  ${return} =  Run Keyword and Ignore Error  Get From Dictionary  ${payload}  serverHardwareUri
    ${sh} =  set variable if  '${status}'=='PASS'  ${return}  error
    ${sh} =  run keyword if  '${sh}'!= '${None}'  replace string using regexp  ${sh}  SH:  ${EMPTY}
    ${sh_uri} =  run keyword if  '${status}'=='PASS' and '${sh}'!='' and '${sh}'!= '${None}'  Get Server Hardware URI  ${sh}
    run keyword if  '${status}'=='PASS'  Set to Dictionary   ${new_payload}  serverHardwareUri  ${sh_uri}
    ${default_type} =    Get Server Profile Type
    ${status}    ${return}    Run Keyword and Ignore Error    Get From Dictionary    ${payload}    type
    ${type} =    Set Variable If    '${status}'=='PASS'    ${return}    ${default_type}
    Set to Dictionary    ${payload}    type    ${type}
    [return]  ${new_payload}

Update SP From SPT
    [Documentation]    Update server profile from server profile template
    [Arguments]    ${profile_name}    ${op}=replace    ${path}=/templateCompliance    ${value}=Compliant    ${api}=${None}
    ${uri} =  Common URI lookup by name  SP:${profile_name}
    ${dict} =  Create Dictionary  op=${op}  path=${path}  value=${value}
    ${payload} =  Create List  ${dict}
    Log    \...Updating Sp from SPT
    ${resp} =  Fusion Api Patch Server Profile  body=${payload}  uri=${uri}  api=${api}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    [Return]    ${blnStatus}

Get Server Profile Template
    [Documentation]    Get Server Profile Template by Name
    [Arguments]    ${spt_name}
    ${sptCollection} =    Fusion Api Get Server Profile Templates
    Return From Keyword If  ${sptCollection['count']}==0  /rest/server_profile_template_uri_${spt_name}_not_found
    @{members}=    Get From Dictionary    ${sptCollection}    members

    :FOR    ${member}    IN    @{members}
    \    ${name}=     Get From Dictionary    ${member}    name
    \    Continue For Loop If    '${spt_name}'!='${name}'
    \    Return From Keyword    ${member}
    [Return]

Get Default custom Attributes From DP
    [Documentation]    Get Default custom Attributes Hostname, Domainname and SSH
    ...    From Deployment Plan
    ...    resource : 'SP:Profile'
    [Arguments]    ${resource}
    @{words}=     Split String  ${resource}    :
    ${type}=  Get From List  ${words}  0
    ${resource_name} =     Get From List    ${words}    1
    ${resp} =    Run Keyword If    '${type}'=='SP'    Get Server Profile    ${resource_name}
    ...    ELSE IF    '${type}'=='SPT'    Get Server Profile Template    ${resource_name}

    ${ca_dict} =    Create Dictionary
    ${cas} =     Get From Dictionary    ${resp['osDeploymentSettings']}    osCustomAttributes
    :For    ${ca}    IN    @{cas}
    \    Run Keyword If    '${ca['name']}'=='Hostname'    Set To Dictionary    ${ca_dict}    ${ca['name']}=${ca['value']}
    \    Run Keyword If    '${ca['name']}'=='DomainName'    Set To Dictionary    ${ca_dict}    ${ca['name']}=${ca['value']}
    \    Run Keyword If    '${ca['name']}'=='SSH'    Set To Dictionary    ${ca_dict}    ${ca['name']}=${ca['value']}
    \    Run Keyword If    '${ca['name']}'=='Password'    Set To Dictionary    ${ca_dict}    ${ca['name']}=${ca['value']}
    \    Run Keyword If    '${ca['name']}'=='UserName'    Set To Dictionary    ${ca_dict}    ${ca['name']}=${ca['value']}
    [Return]    ${ca_dict}

Remove SPT And Server Profiles by SPT
    [Documentation]  Look-up to see if the SPT in a profile DTO already has a profile applied and, if so, remove it.
    [Arguments]    ${spt}

    ${spt_uri} =    Get Server Profile Template URI    ${spt}
    Return From Keyword If  '${spt_uri}'== '/rest/server_profile_template_uri_${spt}_not_found'
    ${sp_resp} =    Fusion Api Get Server Profiles    param=?filter="'serverProfileTemplateUri'=='${spt_uri}'"
    Run Keyword If    ${sp_resp['count']}!=0    Delete Server Profile    ${sp_resp['members'][0]['name']}

    ${resp_delete_spt} =   Fusion Api Delete Server Profile Template    uri=${spt_uri}
    Wait For Task2    ${resp_delete_spt}

Remove SPT By Name
    [Documentation]  Remove Server Profile Template By name
    [Arguments]    ${spt}

    ${spt_uri} =    Get Server Profile Template URI    ${spt}
    Return From Keyword If  '${spt_uri}'== '/rest/server_profile_template_uri_${spt}_not_found'
    ${resp_delete_spt} =   Fusion Api Delete Server Profile Template    uri=${spt_uri}
    Wait For Task2    ${resp_delete_spt}
