*** Settings ***
Documentation     I3S and CLRM resource keywords
Resource          ../../../Resources/api/fusion_api_resource.txt


Library           Collections
Library           json
Library           DateTime
Library           OperatingSystem
Library           BuiltIn
Library           FusionLibrary
Library           i3SLibrary
Library           SSHLibrary
Library           String
Library           RoboGalaxyLibrary


*** Variables ***

${X-API-VERSION}              1000
${FUSION_PROMPT}              \#

*** Keywords ***
Login to Appliance via SSH
    [Documentation]    Connect to Appliance CIM Bash via SSH
    ...                Example:\n| Login to Appliance Via SSH | 10.0.12.106 | Administrator | hpvse123 |
    [Arguments]    ${ip}    ${USERNAME}=${FUSION_SSH_USERNAME}
    ...            ${PASSWORD}=${FUSION_SSH_PASSWORD}
    ...            ${TIMEOUT}=${FUSION_PROMPT}    ${ALIAS}=APP_SSH
    ${Id}=    Open Connection    ${ip}    alias=${ALIAS}
    ${output}=    Login    ${USERNAME}    ${PASSWORD}
    [Return]    ${Id}

Is usb mounted on appliance
   [Arguments]      ${ip}
   Set Log Level  TRACE
   Login to Appliance via SSH    ${ip}
   ${output} =    Execute Command    cd /mnt/usb;echo $?
   Should Contain   ${output}    0
   [Return]    ${output}

Extract Build Name
    [Documentation]    Extracts the image name from the provided URL Seperated with /
    [Arguments]    ${URL}
    @{words} =    Split String    ${URL}    /
    ${buildName} =    Get From List    ${words}    -1
    Log    ${buildName}    console=True
    [return]    ${buildName}

Appliance is unreachable
    [Documentation]    Waits for an appliance to become unreachable
    [Arguments]     ${appliance}    ${timeout}=1 min    ${interval}=5 s
    Wait Until Keyword Succeeds     ${timeout}    ${interval}    Windows ping unreachable check     ${appliance}
    Set Log Level    TRACE
    Run keyword if    os.name == "nt"    Windows ping unreachable check    ${appliance}

Windows ping unreachable check
    [Arguments]     ${host}
    ${output}=    Run    ping -n 4 ${host}
    Should Contain    ${output}    unreachable
    [Return]    ${output}

Get Subnet uri
    [Documentation]    Get Subnet uri
    [Arguments]    ${network_id}
    ${resp} =    fusion api get ipv4 subnet
    ${subnet_list} =    Get From Dictionary    ${resp}    members
    ${subnet_count} =    Get Length    ${subnet_list}
    :FOR    ${index}    IN RANGE    0    ${subnet_count}
    \    ${subnet} =    Get From List    ${subnet_list}    ${index}
    \    Exit For Loop If    '${subnet['networkId']}' == '${network_id}'
    ${uri} =    Get From Dictionary    ${subnet}    uri
    [Return]    ${uri}

Get Goldenimage URI
    [Documentation]    Get Goldenimage URI
    [Arguments]    ${goldenImage}
    ${resp} =     i3s Get Goldenimage    param=?filter="'name'=='${goldenImage}'"
    Run keyword if    ${resp['members']}==[]    FAIL    No golden image found
    ${giUri} =     Get From Dictionary    ${resp['members'][0]}    uri
    [Return]    ${giUri}

CREATE BUILD PLAN PAYLOAD
    [Arguments]    ${buildplan_create}
    ${bp_body} =    Copy Dictionary  ${buildplan_create}
    #planscript URI
    ${ps_body} =    Get from Dictionary    ${bp_body}    buildStep
    ${mx} =    Get Length    ${ps_body}
    Log    ${mx}
    :FOR    ${NUM}    IN RANGE    0    ${mx}
    \    ${psuri} =    Get From Dictionary    ${ps_body[${NUM}]}    planScriptUri
    \    ${uri} =    GET PLANSCRIPT URI    ${psuri}
    \    Set to Dictionary    ${ps_body[${NUM}]}    planScriptUri    ${uri}
    \    Log to console    ${uri}
    [Return]    ${bp_body}

GET PLANSCRIPT URI
    [Arguments]    ${psuri}
    ${resp} =    I3S GET PLANSCRIPT    param=?filter="'name'=='${psuri}'"
    Run keyword if    ${resp['members']}==[]    FAIL    No planscript found
    ${uri} =    Get From Dictionary    ${resp['members'][0]}    uri
    [Return]    ${uri}

Create Deploymentplan Payload
    [Arguments]    ${deploymentplan_create}
    ${dp_body} =    Copy Dictionary    ${deploymentplan_create}

    #Buildplan URI
    ${bp_name} =    Get from Dictionary    ${dp_body}    oeBuildPlanURI
    Log      \nBP Name is:\t ${bp_name}
    ${bp_uri} =    Run Keyword If  '${bp_name}' is not ''    Get Buildplan URI    ${bp_name}
    Log      \nBP URI is:\t ${bp_uri}
    Set to Dictionary    ${dp_body}    oeBuildPlanURI    ${bp_uri}

    #Goldenimage URI
    ${gi_name} =    Get from Dictionary    ${dp_body}    goldenImageURI
    Log    \nGI Name is:\t ${gi_name}
    ${gi_uri} =    Run Keyword If  '${gi_name}' is not ''    Get Goldenimage URI    ${gi_name}
    Log    \nGI URI is:\t ${gi_uri}
    Set to Dictionary    ${dp_body}    goldenImageURI    ${gi_uri}
    [Return]    ${dp_body}

Get Buildplan URI
    [Arguments]    ${bpuri}
    ${resp} =   i3s Get Buildplan    param=?filter="'name'=='${bpuri}'"
    Run keyword if    ${resp['members']}==[]    FAIL    No buildplan found
    ${uri} =    Get From Dictionary    ${resp['members'][0]}   uri
    [Return]    ${uri}

Get ArtifactBundle Uri
    [Arguments]    ${Name}
    ${resp} =    i3s Api Get Artifact Bundle    param=?filter="'name'=='${Name}'"
    Run keyword if    ${resp['members']}==[]    FAIL    No artifact bundle found
    ${uri} =    Get From Dictionary    ${resp['members'][0]}    uri
    [Return]    ${uri}

Wait For Appliance To Become Pingable
    [Documentation]    Waits for an appliance to become pingable
    [Arguments]     ${appliance}={IP}   ${timeout}=1 min    ${interval}=5 s
    Wait Until Keyword Succeeds     ${timeout}    ${interval}    resource_i3s_clrm.Appliance is pingable    ${appliance}

Appliance is pingable
    [Arguments]     ${appliance}
    Set Log Level   TRACE
    Run keyword if  os.name == "nt"    resource_i3s_clrm.Windows ping    ${appliance}
    ...         ELSE    Unix ping    ${appliance}

Windows ping
    [Arguments]     ${host}
    ${output}=    Run    ping -n 4 ${host}
    Should Contain    ${output}    Reply from ${host}
    [Return]    ${output}

Import Certificate to OV
    [Documentation]    Adds the Vcenter Certificate to OneView Appliance
    [Arguments]    ${vcenter_IP}    ${OV_IP}    ${OV_credentials}   ${alias_name}
    Fusion Api Login Appliance    ${OV_IP}    ${OV_credentials}
    ${response} =  Fusion Api Get Remote Certificate        ${vcenter_IP}
    Set To Dictionary    ${CERTIFICATE['certificateDetails'][0]}    base64Data    ${response['certificateDetails'][0]['base64Data']}
    ${headers}=     Fusion APi Get Headers
    set to Dictionary       ${headers}      forceSaveLeaf=True
    set to Dictionary       ${CERTIFICATE['certificateDetails'][0]}     aliasName=${alias_name}
    ${resp}=        Fusion Api Import Server Certificate   ${CERTIFICATE}       headers=${headers}
    ${task}=       Wait For Task   ${resp}         timeout=500s            interval=5s
    ${response} =  Fusion Api Get Server Certificate   ${alias_name}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha1Fingerprint']}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha256Fingerprint']}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha384Fingerprint']}

Download artifact bundle files
    [Documentation]    Download artifact bundle files
    [Arguments]    ${artifact_bundle_locations}
    ${aafiles}    Create list
    :FOR    ${artifact_bundle_location}    in    @{artifact_bundle_locations}
    \   Httpserver open connection       ${artifact_bundle_location}     ${None}    ${None}
    \   ${_}   ${file} =    Split Path    ${artifact_bundle_location}
    \   Create Folder If Not Exists    ${path}
    \   ${localfile} =   Set Variable    ${path}/${file}
    \   Http Directory Download File    ${artifact_bundle_location}   ${localfile}   ${THREADNUM}
    \   Append to list    ${aafiles}    ${localfile}
    \   Httpserver close Connection
    [Return]    ${aafiles}

Wait for appliance webapps to startup
    [Documentation]    Wait for appliance webapps to startup
    [Arguments]     ${ip}
    Set Log Level    TRACE
    Login to Appliance via SSH    ${ip}
    ${output} =    Execute Command    /ci/bin/wait-for-cic
    Should Contain  ${output}    done
    [Return]    ${output}

Remove All Hyperv Cluster Profiles
    [Documentation]    Queries the appliance for all Cluster Profiles and then removes them
    ...                Remove All Hyperv Cluster Profiles
    ...                Remove All Hyperv Cluster Profiles  force=${True}
    [Arguments]  ${force}=${False}
    Log      Removing Hypervisor Cluster Profiles    console=True
    # Set the force flag
    ${tasks}=  Create List
    ${param} =  set variable if  ${force}==${False}  ${Empty}  ?force=${True}
    ${profiles} =     Fusion Api Get Hypervisor Cluster Profile  param=?sort=name:ascending
    Run Keyword If    ${profiles['status_code']}!= 200 or ${profiles['count']}==0    Run Keywords    Run Keyword And Continue On Failure    FAIL    "Could not get hypervisor cluster profiles or there is no hypervisor cluster profiles configured    AND    Return From Keyword
    :FOR    ${profile}    IN    @{profiles['members']}
    \       Log      Removing ${profile['uri']}
    \        ${resp} =     Fusion Api Delete Hypervisor Cluster Profile    param=${param}   uri=${profile['uri']}   
    \       Append To List    ${tasks}  ${resp}

    # Verify if all Tasks are complete. Continue with next task Uri, if any task fails
    :FOR    ${task}    IN    @{tasks}
    \    Run Keyword And Continue on Failure  Wait For Task2  ${task}  timeout=3600  interval=60    BREAK_LOOP_IF=((?i)Error|Terminated|Interrupted)
    ${profiles} =           Fusion Api Get Hypervisor Cluster Profile
    ${count}=               Convert To String                   ${profiles['count']}
    Run Keyword If          '${count}'!='0'                     FAIL    Deleting all Server Profiles did not succeed    

Remove All Hypervisor Managers
    [Documentation]    Queries the appliance for all Hypervisor managers and then removes them
    ...                Remove Hypervisor Managers
    ...                Remove Hypervisor Managerss  force=${True}
    [Arguments]  ${force}=${False}
    Log      Remove Hypervisor Managers    console=True
    # Set the force flag
    ${tasks}=  Create List
    ${param} =  set variable if  ${force}==${False}  ${Empty}  ?force=${True}
    ${hms} =     Fusion Api Get Hypervisor Manager  param=?sort=name:ascending
    Run Keyword If    ${hms['status_code']}!= 200 or ${hms['count']}==0    Run Keywords    Run Keyword And Continue On Failure    FAIL    "Could not get hypervisor cluster profiles or there is no hypervisor cluster profiles configured    AND    Return From Keyword
    :FOR    ${hms}    IN    @{hms['members']}
    \       Log      Removing ${hms['uri']}
    \        ${resp} =     Fusion Api Delete Hypervisor Manager    param=${param}    uri=${hms['uri']}
    \       Append To List    ${tasks}  ${resp}

    # Verify if all Tasks are complete. Continue with next task Uri, if any task fails
    :FOR    ${task}    IN    @{tasks}
    \    Run Keyword And Continue on Failure  Wait For Task2  ${task}  timeout=600  interval=20
    ${hms} =           Fusion Api Get Hypervisor Manager
    ${count}=               Convert To String                   ${hms['count']}
    Run Keyword If          '${count}'!='0'                     FAIL    Deleting all Hypervisor Managers did not succeed
    
    
Perform Post HCP Creation Validations
    [Documentation]    Validates the state and status of hypervisor cluster profiles
    ...                and Hypervisor Host profiles assoicated with cluster profiles
    [Arguments]    ${profileNames}    ${hyperv_cluster_profiles}

    Run Keyword for List    ${profileNames}     Cluster Profile State And Status Should Be OK
    ${hostProfiles} =    Get Host Profile Names    ${hyperv_cluster_profiles}
    Log    \n\n host profile names: ${hostProfiles}\n\n    console=True
    Run Keyword for List    ${hostProfiles}     Cluster Profile State And Status Should Be OK    False


Get Host Profile Names
     [Documentation]    Generates the hypervisor Host profile names from hostprefix and 
     ...                addHostRequests fields of cluster profiles by combining the 
     ...                hostprefix with index number. For e.g. if there are 3 host entries
     ...                in the addHostRequests field and hostprefix is hcp, then it will generate
     ...                hcp1, hcp2, hcp3 as host profile names and returns it
    [Arguments]    ${profiles}

    ${hostlist} =    Create List
    ${namelist} =    Create List

    :FOR    ${profile}    IN    @{profiles}
    \    ${prefix} =    Get Variable Value    ${profile['hypervisorHostProfileTemplate']['hostprefix']}
    \    ${hostlist} =    Get Variable Value    ${profile['addHostRequests']}    ${NULL}
    \    ${count} =    Run Keyword If    ${hostlist} != ${NULL}    Get Length    ${hostlist}
    \    ...                     ELSE    Set Variable    ${0}
    \    ${tmp} =    Evaluate    ['${prefix}'+ str(idx) for idx in range(1,${count}+1)]
    \    ${namelist} =    Combine Lists    ${namelist}    ${tmp}

    [Return]    ${namelist}


Assign Sht To Server Profile Template
    [Documentation]    Since there are multiple server hardware types in our setup and each
    ...                types value changes after every hardware discovery, it becomes essential 
    ...                to find the sht dynamically. This keyword try to matches the adapters 
    ...                section of the server hardware types with the one defined in the data file
    ...                if there is a match, it assigns that type to server profile template
    [Arguments]    ${hypervisor_spts}

    :FOR    ${spt_entry}    IN    @{hypervisor_spts}
    \    ${dataFileUriVar} =    Get Variable Value    ${spt_entry['serverHardwareTypeUri']}
    \    ${keys} =    Get Dictionary Keys    ${dataFileUriVar}
    \    ${model} =    Get Variable Value    ${keys[0]}
    \    ${resp} =    Fusion Api Get Server Hardware Types    param=?filter="model='${model}'"
    \    Run Keyword if  ${resp['status_code']} != 200    FAIL    Unable to get server hardware types
    \    ${sht} =    Get Server Hardware Type    ${dataFileUriVar['${model}']}    ${resp['members']}
    \    Log    \n\nsht is ${sht}\n\n    console=True
    \    Run Keyword If    '${sht}' != 'None'    Set To Dictionary    ${spt_entry}   serverHardwareTypeUri    SHT:${sht}
    \    ...     ELSE     Run Keyword And COntinue On Failure    FAIL    Unable to get the server hardware type for ${spt_entry['name']}

Get Server Hardware Type
    [Documentation]    Helper keyword for Assign Sht To Server Profile Template
    [Arguments]    ${sht_details}    ${response}

    :FOR    ${entry}    IN    @{response}
    \    ${ret_val} =    Compare And Find Match    ${sht_details['adapters']}       ${entry['adapters']} 
    \    Run Keyword If    '${ret_val}' == 'True'    Return From Keyword    ${entry['name']} 

Compare And Find Match 
    [Documentation]    Iterate through each adpater entry in the data file and finds a matching
    ...                entry in the server hardware types of OV
    [Arguments]    ${data_adapters}    ${ov_adapters}

    :FOR    ${ent}    IN    @{data_adapters}
    \    ${ret} =    Find Matching Adapter    ${ent}    ${ov_adapters}
    \    Run Keyword If    '${ret}' == 'False'    Return From Keyword    False

    [Return]    True

Find Matching Adapter
    [Documentation]    Iterate through each adpater entry from OV and finds a matching
    ...                entry in the data file
    [Arguments]    ${data_adapter_entry}    ${ov_adapters}

    :FOR    ${ov_entry}    IN    @{ov_adapters}
    \    ${status} =    Run Keyword And Return Status    Dictionary Should Contain Sub Dictionary    ${ov_entry}    ${data_adapter_entry}
    \    Run Keyword If    '${status}' == 'True'    Return From Keyword    True

    [Return]    False

Add Cluster Profiles
    [Documentation]    Creates hypervisor cluster profiles defined in the data file if it does not exist in OV
    ...                Returns the profile name list and profile list that are actually process by this keyword
    [Arguments]    ${cluster_profiles}    ${status_code}=202

    ${status_code}=   Set Variable    202
    ${toAdd} =    Create List
    ${resplist} =    Create List    
    ${proflist} =    Create List
    ${profnamelist} =    Create List

    :FOR    ${profile}    IN    @{cluster_profiles}
    \    ${status} =  Run Keyword And Return Status    Check Resource Existing  HCP:${profile['name']}
    \    Run Keyword If    '${status}'=='False'  Append To List   ${toAdd}  ${profile}
    \    Run Keyword If    '${status}'=='True'   Log   Hypervisor Cluster Profile ${profile['name']} already exist   WARN
    ${len} =   get length  ${toAdd}
    Return from keyword if  '${len}'=='0'

   :FOR    ${profile}    IN    @{toAdd}
    \    ${payload} =    Create Hyperv Cluster Profile Payload    ${profile}
    \    ${resp} = 	Fusion Api Create Hypervisor Cluster Profile 	${payload}
    \    Run Keyword If    ${resp['status_code']}== ${status_code}    Run Keywords    append to list    ${resplist}    ${resp}    AND    Append To List    ${profnamelist}    ${profile["name"]}    AND    Append To List    ${proflist}    ${profile}
    \    ...          ELSE    Run Keywords    Run Keyword And Continue On Failure    Fail    Failed to create Cluster Profile ${profile["name"]}    AND    Continue For Loop 
    ${responses} =    Get Length    ${resplist}
    Run Keyword If      ${responses} > 0
    ...                 Run Keyword for List     ${resplist}    Wait For Task2      
    ...                 timeout=7500    interval=60    BREAK_LOOP_IF=((?i)Error|Terminated|Interrupted)

    [Return]    ${profnamelist}    ${proflist}    

Cluster Profile State And Status Should Be OK
    [Documentation]    Ensure that the cluster profile or host profile state, status and compliance state is proper
    ...                This keyword is called after cluster profile (host profile)) creation as post validation checks
    [Arguments]    ${pname}    ${cp}=True    ${status_code}=200
    
   
    ${resp}= 	Run Keyword If    '${cp}' == 'True'    Fusion Api Get Hypervisor Cluster Profile		param=?filter="'name'=='${pname}'
    ...       ELSE   Fusion Api Get Hypervisor Host Profile    param=?filter="'name'=='${pname}'
                          
    Run Keyword If    ${resp['status_code']}!= ${status_code} or ${resp['count']}==0     FAIL    Could not fetch cluster profile with name ${pname}
    
    Run Keyword If    ${resp['status_code']}== ${status_code} and ${resp['count']}==1    Run Keyword And Continue On Failure    Should be equal     ${resp['members'][0]['complianceState']}      Consistent

    Run Keyword If    ${resp['status_code']}== ${status_code} and ${resp['count']}==1    Run Keyword And Continue On Failure    Should be equal     ${resp['members'][0]['state']}      Active

    Run Keyword If    ${resp['status_code']}== ${status_code} and ${resp['count']}==1    Run Keyword And Continue On Failure    Should be equal     ${resp['members'][0]['status']}      OK


Create Hyperv Cluster Profile Payload
    [Documentation]    Creates the Hypervisor cluster profile payload based on the datafile entries 
    [Arguments]    ${cluster_template}    ${api}=${None}

    ${payload} =  copy dictionary  ${cluster_template}
    Log    \nCreating Hyperv Cluster Payload ${Payload}\n    console=True
    # SPT URI
    ${status}  ${return} =  Run Keyword and Ignore Error  Get Variable Value    ${payload['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    #${status}  ${return} =  Run Keyword and Ignore Error  Get From Dictionary        ${payload['hypervisorHostProfileTemplate']}    serverProfileTemplateUri'
    ${spt} =  set variable if  '${status}'=='PASS'  ${return}  error
    ${spt_uri} =  run keyword if  '${status}'=='PASS' and '${spt}'!=''   Common URI Lookup by name  ${spt}
    Run Keyword If  '${status}'=='PASS' and '${spt}'!=''    Set To Dictionary    ${payload['hypervisorHostProfileTemplate']}         serverProfileTemplateUri=${spt_uri}

    # hypervisorManagerUri    
    ${status}  ${return} =  Run Keyword and Ignore Error  Get From Dictionary  ${payload}    hypervisorManagerUri
    ${hm} =  set variable if  '${status}'=='PASS'  ${return}  error
    ${hm_uri} =  run keyword if  '${status}'=='PASS' and '${hm}'!=''   Common URI Lookup by name  ${hm}
    run keyword if  '${status}'=='PASS' and '${hm}'!=''  Set to Dictionary    ${payload}    hypervisorManagerUri    ${hm_uri}

    # sharedStorageVolumes    
    ${svol_status}=    Run keyword and return status    Dictionary should contain key    ${payload}    sharedStorageVolumes
    ${resp_vol}=    Run keyword if    ${svol_status}==True    update shared volume    ${payload['sharedStorageVolumes']}
    Run keyword if    ${svol_status}==True    Set to Dictionary    ${payload}    sharedStorageVolumes    ${resp_vol}

    # Add Host Request
    ${host_list}=    Create List
    ${addHostRequests}=    run keyword and return status    Dictionary should contain key    ${payload}	addHostRequests
    ${host_list}=    Run keyword if	${addHostRequests}==True    Create Add Host Request    ${payload}
    Run keyword if    ${addHostRequests}==True    Set to Dictionary    ${payload}    addHostRequests    ${host_list}

    [Return]    ${payload}
    
Create Add Host Request
    [Documentation]    Gets the server hardware URI for each addHostEntry defined in the cluster profile data
    [Arguments]    ${cp}

    ${hardware_lst} =    Create List

    :FOR    ${hw}    in    @{cp['addHostRequests']}
    \    ${dict} =    Create Dictionary
    \    ${uri}=    Run keyword and return status    Dictionary should contain key    ${hw}    serverHardwareUri
    \    ${hwUri}=	Run Keyword If    '${uri}' == 'True'    Get Server Hardware URI    ${hw['serverHardwareUri']}
    \   ...         ELSE    Return From Keyword    ${hardware_lst}
    \    Run Keyword if    '${hwUri}'!=''    Set to Dictionary    ${dict}    serverHardwareUri    ${hwUri}
    \    Run Keyword if	'${hwUri}'!=''    Append to List    ${hardware_lst}    ${dict}
    [Return]    ${hardware_lst}

Get Host List
    [Documentation]    Get list of servers defined in addHostRequests list of Cluster Profile DTO  
    [Arguments]    ${cp}

    ${host_list} =   Create List
    :FOR    ${host}    in    @{cp['addHostRequests']}
    \    ${uri}=    Run keyword and return status    Dictionary should contain key    ${host}    serverHardwareUri
    \    ${hwUri}=    Run Keyword If    '${uri}' == 'True'    Get Variable Value    ${host['serverHardwareUri']}
    \   Run Keyword If    '${hwUri}' != 'None'    Append To List    ${host_list}    ${hwUri}

    [Return]    ${host_list}
    
Remediation Between Edit SPT and HCP
    [Documentation]     Remediation check between Edit SPT and HCP
    [Arguments]     ${cp_name}
    ${Cluster_with_prereq}=    Get Cluster Profile By Name And With Consistent State    ${cp_name}
    Run keyword if    ${Cluster_with_prereq} == ${None}    FAIL    Could not find HyperVisor cluster profile with Consistency state.
    ${Cluster_uri}=     Get from Dictionary     ${Cluster_with_prereq}      uri
    ${net_uri}=     Get Ethernet URI     ${edit_network}
    ${spt_response}=    Fusion Api Get Server Profile Templates     uri=${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Remove from dictionary      ${spt_response}      headers    status_code
    ${Connections}=     Get From Dictionary     ${spt_response['connectionSettings']}     connections
    :For    ${connection}   in      @{Connections}
    \   Run keyword if      '${connection['boot']['priority']}' != 'NotBootable'    Continue for loop
    \   ${resp}=    Fusion Api Get Ethernet Networks      ${connection['networkUri']}
    \   Run keyword if      '${resp['category']}' != 'ethernet-networks'    Continue for loop
    \   ${edit_conn_variable}=    Set Variable If    '${resp['purpose']}' == 'General'    ${True}    ${False}
    \   Run keyword if      '${resp['purpose']}' == 'General'    run keywords
    \   ...     set to Dictionary      ${connection}      networkUri=${net_uri}     AND
    \   ...     Exit for loop
    Run keyword if      '${edit_conn_variable}' == '${False}'    Fail    Editing the Connection in SPT is failed
    ${spt_edit_response}=    Fusion Api Edit Server Profile Template     ${spt_response}     uri=${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Wait For Task2  ${spt_edit_response}  300  5
    Log    Waiting for the cluster to became Inconsistent,Wait time is for 5 min maximum
    ${hcp_state}=    Wait Until Keyword Succeeds    8 minutes    1 minutes      Cluster Profile State Should Not Be Consistent     ${Cluster_uri}    ClusterTemplateVSwitchError
    Run Keyword And Continue On Failure    Should be equal     ${hcp_state}      ClusterTemplateVSwitchError
    ${hcp_response_after_vswitch}=  Update Virtual Switch Layout    ${cluster_uri}
    Run Keyword And Continue On Failure    should be equal as integers     ${hcp_response_after_vswitch['status_code']}      202
    Wait For Task2    ${hcp_response_after_vswitch}    timeout=5m   interval=1m
    ${hcp_state}=    Cluster Profile State Should Not Be Consistent    ${Cluster_uri}    HostProfileInconsistent
    Run Keyword And Continue On Failure    Should be equal     ${hcp_state}      HostProfileInconsistent
    Check Host Profile State    ${Cluster_with_prereq}
    Check Server Profile State    ${Cluster_with_prereq}
    ${Hypervisor_count}=     Get Host Profile Count    ${Cluster_uri}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate Cluster Profile Inconsistent  ${Cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    BREAK_LOOP_IF=((?i)Error|Terminated|Interrupted)
    Sleep    60s
    Wait Until Keyword Succeeds    10 minutes    1 minutes      Cluster Profile State And Status Should Be OK    ${Cluster_with_prereq['name']}    True

Remediation Between Delete_conn SPT and HCP
    [Documentation]     Remediation check between Edit SPT and HCP
    [Arguments]     ${cp_name}
    ${Cluster_with_prereq}=    Get Cluster Profile By Name And With Consistent State    ${cp_name}
    Run keyword if    ${Cluster_with_prereq} == ${None}    FAIL    Could not find HyperVisor cluster profile with Consistency state.
    ${Cluster_uri}=     Get from Dictionary     ${Cluster_with_prereq}      uri
    ${spt_response}=    Fusion Api Get Server Profile Templates     uri=${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Remove from dictionary      ${spt_response}      headers    status_code
    ${Connections}=     Get From Dictionary     ${spt_response['connectionSettings']}     connections
    ${connections_length}=     Get length      ${Connections}
    :For    ${index}   IN RANGE    ${connections_length}
    \   Run keyword if      '${Connections[${index}]['boot']['priority']}' != 'NotBootable'    Continue for loop
    \   ${resp}=    Fusion Api Get Ethernet Networks      ${Connections[${index}]['networkUri']}
    \   Run keyword if      '${resp['category']}' != 'ethernet-networks'    Continue for loop
    \   ${del_conn_variable}=    Set Variable If    '${resp['purpose']}' == 'General'    ${True}    ${False}
    \   Run keyword if      '${resp['purpose']}' == 'General'    run keywords
    \   ...     Remove from list      ${Connections}    ${index}      AND
    \   ...     Exit for loop
    Run keyword if      '${del_conn_variable}' == '${False}'    Fail    Deleting the connection from SPT is failed
    ${spt_edit_response}=    Fusion Api Edit Server Profile Template     ${spt_response}     uri=${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Wait For Task2  ${spt_edit_response}  300  5
    Log    Waiting for the cluster to became Inconsistent,Wait time is for 5 min maximum
    ${hcp_state}=    Wait Until Keyword Succeeds    8 minutes    1 minutes      Cluster Profile State Should Not Be Consistent     ${Cluster_uri}    ClusterTemplateVSwitchError
    Run Keyword And Continue On Failure    Should be equal     ${hcp_state}      ClusterTemplateVSwitchError
    ${hcp_response_after_vswitch}=  Update Virtual Switch Layout    ${cluster_uri}
    Run Keyword And Continue On Failure    Should be equal as integers     ${hcp_response_after_vswitch['status_code']}      202
    Wait For Task2    ${hcp_response_after_vswitch}    timeout=5m   interval=1m
    ${hcp_state}=    Cluster Profile State Should Not Be Consistent    ${Cluster_uri}    HostProfileInconsistent
    Run Keyword And Continue On Failure    Should be equal     ${hcp_state}      HostProfileInconsistent
    Check Host Profile State    ${Cluster_with_prereq}
    Check Server Profile State    ${Cluster_with_prereq}
    ${Hypervisor_count}=     Get Host Profile Count    ${Cluster_uri}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate Cluster Profile Inconsistent  ${Cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    BREAK_LOOP_IF=((?i)Error|Terminated|Interrupted)
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Profile State And Status Should Be OK    ${Cluster_with_prereq['name']}    True

Remediation Between Add_conn SPT and HCP
    [Documentation]     Remediation check between Edit SPT and HCP
    [Arguments]     ${cp_name}
    ${Cluster_with_prereq}=    Get Cluster Profile By Name And With Consistent State    ${cp_name}
    Run keyword if    ${Cluster_with_prereq} == ${None}    FAIL    Could not find HyperVisor cluster profile with Consistency state.
    ${Cluster_uri}=     Get from Dictionary     ${Cluster_with_prereq}      uri
    ${net_uri}=     Get Ethernet URI     ${add_ethernet_networks}
    ${spt_response}=    Fusion Api Get Server Profile Templates     uri=${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Remove from dictionary      ${spt_response}      headers    status_code
    ${Connections}=     Get From Dictionary     ${spt_response['connectionSettings']}     connections
    ${connections_length}=     Get length      ${Connections}
    ${Additional_network}=     Create Dictionary     networkUri=${net_uri}
    Append to list      ${Connections}      ${Additional_network}
    ${spt_edit_response}=    Fusion Api Edit Server Profile Template     ${spt_response}     uri=${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Wait For Task2  ${spt_edit_response}  300  5
    Log    Waiting for the cluster to became Inconsistent,Wait time is for 5 min maximum
    ${hcp_state}=    Wait Until Keyword Succeeds    8 minutes    1 minutes      Cluster Profile State Should Not Be Consistent     ${Cluster_uri}    ClusterTemplateVSwitchError
    Run Keyword And Continue On Failure    Should be equal     ${hcp_state}      ClusterTemplateVSwitchError
    ${hcp_response_after_vswitch}=  Update Virtual Switch Layout    ${cluster_uri}
    Run Keyword And Continue On Failure    Should be equal as integers     ${hcp_response_after_vswitch['status_code']}      202
    Wait For Task2    ${hcp_response_after_vswitch}    timeout=5m   interval=1m
    ${hcp_state}=    Cluster Profile State Should Not Be Consistent    ${Cluster_uri}    HostProfileInconsistent
    Run Keyword And Continue On Failure    Should be equal     ${hcp_state}      HostProfileInconsistent
    Check Host Profile State    ${Cluster_with_prereq}
    Check Server Profile State    ${Cluster_with_prereq}
    ${Hypervisor_count}=     Get Host Profile Count    ${Cluster_uri}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate Cluster Profile Inconsistent  ${Cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    BREAK_LOOP_IF=((?i)Error|Terminated|Interrupted)
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Profile State And Status Should Be OK    ${Cluster_with_prereq['name']}    True

Remediation Between Edit SP and HCP
    [Documentation]     Remediation check between Edit SP and HCP
    [Arguments]     ${cp_name}
    ${Cluster_with_prereq}=    Get Cluster Profile By Name And With Consistent State    ${cp_name}
    Run keyword if    ${Cluster_with_prereq} == ${None}    FAIL    Could not find HyperVisor cluster profile with Consistency state.
    ${Cluster_uri}=     Get from Dictionary     ${Cluster_with_prereq}      uri
    ${Cluster_host_uri}=      Get From List       ${Cluster_with_prereq['hypervisorHostProfileUris']}    0
    ${host_response}=   Fusion Api Get Hypervisor Host profile      uri=${Cluster_host_uri}
    ${server_profile_uri}=      Get from Dictionary     ${host_response}      serverProfileUri
    ${server_profile_response}=     Fusion Api Get Server Profiles      uri=${server_profile_uri}
    ${Connections}=     Get From Dictionary     ${server_profile_response['connectionSettings']}     connections
    :For    ${connection}   in      @{Connections}
    \   Run keyword if      '${connection['boot']['priority']}' != 'NotBootable'    Continue for loop
    \   ${edit_spconn_variable}=    Set Variable If    '${connection['name']}' == 'VMGuest-A'    ${True}    ${False}
    \   Run keyword if      '${connection['name']}' == 'VMGuest-A'    run keywords
    \   ...     set to Dictionary      ${connection}      requestedMbps=5500     AND
    \   ...     Exit for loop
    Run keyword if      '${edit_spconn_variable}' == '${False}'    Fail    Editing the Connection in SP is failed
    Remove from dictionary      ${server_profile_response}      headers     status_code
    ${spt_edit_response}=    Fusion Api Edit Server Profile      body=${server_profile_response}     uri=${server_profile_response['uri']}
    Wait For Task2  ${spt_edit_response}  300  5
    ${hcp_state}=    Wait Until Keyword Succeeds    8 minutes    1 minutes      Cluster Profile State Should Not Be Consistent     ${Cluster_uri}    HostProfileInconsistent
    Run Keyword And Continue On Failure    Should be equal     ${hcp_state}      HostProfileInconsistent
    Check Host Profile State By Uri    ${Cluster_host_uri}
    CHeck Server Profile State By Uri    ${server_profile_uri}
    ${Hypervisor_count}=     Get Host Profile Count    ${Cluster_uri}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate Cluster Profile Inconsistent  ${Cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    BREAK_LOOP_IF=((?i)Error|Terminated|Interrupted)
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Profile State And Status Should Be OK    ${Cluster_with_prereq['name']}    True

Remediation Between Delete_conn SP and HCP
    [Documentation]     Remediation check between Delete NetworkSet in SP and HCP
    [Arguments]     ${cp_name}
    ${del_spconn_variable}=    Set Variable    ${False}
    ${Cluster_with_prereq}=    Get Cluster Profile By Name And With Consistent State    ${cp_name}
    Run keyword if    ${Cluster_with_prereq} == ${None}    FAIL    Could not find HyperVisor cluster profile with Consistency state.
    ${Cluster_uri}=     Get from Dictionary     ${Cluster_with_prereq}      uri
    ${Cluster_host_uri}=      Get From List       ${Cluster_with_prereq['hypervisorHostProfileUris']}    0
    ${host_response}=   Fusion Api Get Hypervisor Host profile      uri=${Cluster_host_uri}
    ${server_profile_uri}=      Get from Dictionary     ${host_response}      serverProfileUri
    ${server_profile_response}=     Fusion Api Get Server Profiles      uri=${server_profile_uri}
    Power Off Server By Uri     ${server_profile_response['serverHardwareUri']}
    ${Connections}=     Get From Dictionary     ${server_profile_response['connectionSettings']}     connections
    ${connections_length}=     Get length      ${Connections}
    :For    ${index}   IN RANGE    ${connections_length}
    \   Run keyword if      '${Connections[${index}]['boot']['priority']}' != 'NotBootable'    Continue for loop
    \   ${del_spconn_variable}=    Set Variable If    '${Connections[${index}]['name']}' == 'VMGuest-A'    ${True}    ${False}
    \   Run keyword if      '${Connections[${index}]['name']}' == 'VMGuest-A'    run keywords
    \   ...     Remove from list      ${Connections}    ${index}      AND
    \   ...     Exit for loop
    Run keyword if      '${del_spconn_variable}' == '${False}'    Fail    Deleting the connection from SPT is failed
    Remove from dictionary      ${server_profile_response}      headers     status_code
    ${spt_edit_response}=    Fusion Api Edit Server Profile      body=${server_profile_response}     uri=${server_profile_response['uri']}
    Wait For Task2  ${spt_edit_response}  300  5
    Run Keyword And Continue On Failure    Power On Server By Uri      ${server_profile_response['serverHardwareUri']}
    ${host_ip}=     Get Ip From Host Profile    ${Cluster_host_uri}
    Run Keyword And Continue On Failure    Wait For Server To Become Pingable  ${host_ip}  30 min    30 s
    ${hcp_state}=    Wait Until Keyword Succeeds    8 minutes    1 minutes      Cluster Profile State Should Not Be Consistent     ${Cluster_uri}    HostProfileInconsistent
    Run Keyword And Continue On Failure    Should be equal     ${hcp_state}      HostProfileInconsistent
    Check Host Profile State By Uri    ${Cluster_host_uri}
    CHeck Server Profile State By Uri    ${server_profile_uri}
    ${Hypervisor_count}=     Get Host Profile Count    ${Cluster_uri}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate Cluster Profile Inconsistent  ${Cluster_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    BREAK_LOOP_IF=((?i)Error|Terminated|Interrupted)
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Profile State And Status Should Be OK    ${Cluster_with_prereq['name']}    True

Remediation Between Add_Vol SPT and HCP
    [Documentation]     Remediation check between After adding SAN Volume in SPT and HCP
    [Arguments]     ${cp_name}
    ${Cluster_with_prereq}=    Get Cluster Profile By Name And With Consistent State    ${cp_name}
    Run keyword if    ${Cluster_with_prereq} == ${None}    FAIL    Could not find HyperVisor cluster profile with Consistency state.
    ${vol_uri} =       Get Storage Volume URI     ${add_vol}
    ${Cluster_uri}=     Get from Dictionary     ${Cluster_with_prereq}      uri
    ${spt_response}=    Fusion Api Get Server Profile Templates     uri=${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Remove from dictionary      ${spt_response}      headers    status_code
    ${volumeAttachments}=     Get From Dictionary     ${spt_response['sanStorage']}     volumeAttachments
    ${Additional_volume}=   Create Dictionary       volumeUri=${vol_uri}    lunType=Auto
    Append to list      ${volumeAttachments}    ${Additional_volume}
    ${spt_edit_response}=    Fusion Api Edit Server Profile Template     ${spt_response}     uri=${Cluster_with_prereq['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    Wait For Task2  ${spt_edit_response}  300  5
    ${hcp_state}=    Wait Until Keyword Succeeds    8 minutes    1 minutes      Cluster Profile State Should Not Be Consistent     ${Cluster_uri}    ClusterTemplateStorageVolError
    Run Keyword And Continue On Failure    Should be equal     ${hcp_state}      ClusterTemplateStorageVolError
    Check Host Profile State    ${Cluster_with_prereq}
    Check Server Profile State    ${Cluster_with_prereq}
    ${Hypervisor_count}=     Get Host Profile Count    ${Cluster_uri}
    ${time_out_for_task}=    Evaluate    ${Hypervisor_count} * 30
    ${remediate_response}=      Remediate Cluster Profile StorageInconsistent    ${cluster_uri}    ${vol_uri}
    should be equal as integers     ${remediate_response['status_code']}      202
    Wait For Task2    ${remediate_response}    timeout=${time_out_for_task}m    interval=1m    BREAK_LOOP_IF=((?i)Error|Terminated|Interrupted)
    Wait Until Keyword Succeeds    5 minutes    1 minutes      Cluster Profile State And Status Should Be OK    ${Cluster_with_prereq['name']}    True

Get Cluster Profile By Name And With Consistent State
    [Documentation]     Checks all the required prerequisites to do Remediate
    [Arguments]     ${cp_names}
    log    ${cp_names}
    Set Log Level    Trace
    :For    ${cluster}      In      @{cp_names}
    \     ${Cluster_with_prereq}=   Check Cluster Profile Consistency   ${cluster}
    \     Run Keyword If    ${Cluster_with_prereq} != ${None}    Exit For Loop
    [return]    ${Cluster_with_prereq}


Check Cluster Profile Consistency
    [Arguments]     ${cp_name}
    ${clusters} =       Create List
    ${Cluster_with_prereq} =   Set Variable    ${None}
    ${cp_details}   ${count}=    Get Cluster Profile    ${cp_name}
    Run Keyword If    '${count}' == '0'    Log    ${cp_name} Hypervisor Cluster Profile Is Not Found    
    return from keyword if    '${count}' == '0'
    return from keyword if    '${cp_details['complianceState']}' != 'Consistent'
    ${hostprofile_count}=     get length    '${cp_details['hypervisorHostProfileUris']}'
    return from keyword if    ${hostprofile_count} == 0
    ${cluster_with_consistency}=    set variable    ${cp_details}
    ${Status}=     Check Host Profile Ip Settings      ${cluster_with_consistency}
    return from keyword if    '${Status}'!='True'
    ${Cluster_with_prereq} =   Set Variable    ${cluster_with_consistency}
    [return]    ${Cluster_with_prereq}

Check Host Profile Ip Settings
    [Documentation]     Cheks if IP has set to the host for the cluster selected
    [Arguments]     ${cluster_with_consistency}
    ${host_profiles}=       Get from Dictionary    ${cluster_with_consistency}    hypervisorHostProfileUris
    :For    ${host_profile}     In      @{host_profiles}
    \     ${host_profile_detail}=     Get Host Profile by Uri     ${host_profile}
    \     return from keyword if    ${host_profile_detail['ipSettings']} == ${None}
    \     return from keyword if      '${host_profile_detail['ipSettings']['ip']}'=='${None}'
    \     return from keyword if    '${host_profile_detail['complianceState']}' !='Consistent'
    [return]    ${True}

Cluster Profile State Should Not Be Consistent
    [Documentation]     Returns HCP consistency state
    [Arguments]    ${cluster_uri}    ${cluster_state}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${hcp_state}=    Get from Dictionary    ${hcp_response}    complianceState
    Should be equal    ${hcp_response['complianceState']}    ${cluster_state}
    [return]    ${hcp_state}

Check Host Profile State
    [Documentation]     Returns Host Profile state
    [Arguments]    ${cluster_with_consistency}
    ${host_profiles}=       Get from Dictionary    ${cluster_with_consistency}    hypervisorHostProfileUris
    :For    ${host_profile}     In      @{host_profiles}
    \     ${host_profile_detail}=     Get Host Profile by Uri     ${host_profile}
    \     Run Keyword If    '${host_profile_detail['complianceState']}' != 'ServerProfileInconsistent'    Run Keywords
    \     ...     Run Keyword And Continue On Failure    Fail    Host Profile state is not in expected compliant state  AND
    \     ...     Continue for loop

Check Host Profile State By Uri
    [Documentation]     Check Host Profile state by Uri
    [Arguments]    ${host_profile}
    ${host_profile_detail}=     Get Host Profile by Uri     ${host_profile}
    Run Keyword And Continue On Failure    Should be equal    ${host_profile_detail['complianceState']}    ServerProfileInconsistent

Get Host Profile Count
    [Documentation]     Returns Host Profile Count
    [Arguments]    ${cluster_uri}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${host_profile_count}=       Get length    ${hcp_response['hypervisorHostProfileUris']}
    [return]    ${host_profile_count}

Check Server Profile State
    [Documentation]     Returns the compliance state of SP
    [Arguments]    ${cluster_with_consistency}
    ${host_profiles}=       Get from Dictionary    ${cluster_with_consistency}    hypervisorHostProfileUris
    :For    ${host_profile}     In      @{host_profiles}
    \     ${host_profile_detail}=     Get Host Profile by Uri     ${host_profile}
    \     ${ServerProfile_uri}=  Get from Dictionary    ${host_profile_detail}  serverProfileUri
    \     ${profile} =   Fusion Api Get Server Profiles     ${ServerProfile_uri}
    \     ${template_compliance} =  Get From Dictionary  ${profile}  templateCompliance
    \     Log    \t Server Profile: [${profile['name']}] is: ${template_compliance}
    \     Run Keyword If    '${template_compliance}' != 'NonCompliant'    Run Keywords
    \     ...     Run Keyword And Continue On Failure    Fail    Server Profile state is not compliant   AND
    \     ...     Continue for loop

Check Server Profile State By Uri
    [Documentation]     Returns the compliance state of SP
    [Arguments]    ${ServerProfile_uri}
    ${profile} =   Fusion Api Get Server Profiles     ${ServerProfile_uri}
    ${template_compliance} =  Get From Dictionary  ${profile}  templateCompliance
    Log    \t Server Profile: [${profile['name']}] is: ${template_compliance}
    Run Keyword And Continue On Failure    Should be equal    ${template_compliance}    NonCompliant

Remediate Cluster Profile Inconsistent
    [Documentation]     Remediates the cluster in Inconsistent state
    [Arguments]     ${cluster_uri}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    Remove from dictionary      ${hcp_response}      headers    status_code
    set to dictionary       ${hcp_response}      complianceState    Remediate
    ${remediate_response}=      Fusion Api Update Hypervisor Cluster Profile    body=${hcp_response}    uri=${hcp_response['uri']}
    [return]    ${remediate_response}

Update Virtual Switch Layout
    [Documentation]     Update virtual switch layout for the HCP provided
    [Arguments]     ${cluster_uri}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${vsl}=     Get Virtual Switch Layout       ${Cluster_uri}
    Remove from dictionary      ${hcp_response}      headers    status_code
    ${vsl_json}     json.loads      ${vsl['response_body']}
    set to dictionary       ${hcp_response['hypervisorHostProfileTemplate']}      virtualSwitches    ${vsl_json}
    ${hcp_response_after_vswitch}=      Fusion Api Update Hypervisor Cluster Profile    body=${hcp_response}    uri=${hcp_response['uri']}
    [return]    ${hcp_response_after_vswitch}

Remediate Cluster Profile StorageInconsistent
    [Documentation]    Remediate Cluster Profile StorageInconsistent
    [Arguments]     ${cluster_uri}    ${vol_uri}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    Remove from dictionary      ${hcp_response}      headers    status_code
    ${Additional_volume}=   Create Dictionary       storageVolumeUri=${vol_uri}   volumeFileSystemType=Unmanaged
    Append to list      ${hcp_response['sharedStorageVolumes']}   ${Additional_volume}
    set to dictionary       ${hcp_response}      complianceState    Remediate
    ${remediate_response}=      Fusion Api Update Hypervisor Cluster Profile    body=${hcp_response}    uri=${hcp_response['uri']}
    [return]    ${remediate_response}

Get Virtual Switch Layout
    [Documentation]     gets virtual switch layout for the HCP provided
    [Arguments]     ${cluster_uri}
    ${hcp_response}=    Fusion Api Get Hypervisor Cluster Profile       ${cluster_uri}
    ${payload}=     Create Dictionary
    set to dictionary       ${payload}      serverProfileTemplateUri=${hcp_response['hypervisorHostProfileTemplate']['serverProfileTemplateUri']}
    ...     hypervisorManagerUri=${hcp_response['hypervisorManagerUri']}    hypervisorClusterSettings=${hcp_response['hypervisorClusterSettings']}
    ...     virtualSwitchConfigPolicy=${hcp_response['hypervisorHostProfileTemplate']['virtualSwitchConfigPolicy']}
    Log     ${payload}   console=True
    ${VSL}=  Fusion Api Create Virtual Switch Layout    ${payload}
    Remove from dictionary      ${VSL}      headers     status_code
    [return]    ${VSL}

Wait For Server To Become Pingable
    [Documentation]    Check Host Is Pingable
    [Arguments]    ${host}  ${timeout}=1 min    ${interval}=5 s
    Login To VCENTRE Via SSH
    Wait Until Keyword Succeeds     ${timeout}    ${interval}    Host Is Pingable    ${host}
    Close Connection

Login To VCENTRE Via SSH
    [Documentation]             Connect to VCENTRE via SSH
    [Arguments]                 ${IP}=${Hypervisor_manager[0]['name']}      ${USERNAME}=${Hypervisor_manager[0]['username']}
    ...                         ${PASSWORD}=${Hypervisor_manager[0]['password']}
    ${Id}=                      Open Connection    ${IP}
    ${Output}=                  Login    ${USERNAME}    ${PASSWORD}

Host Is Pingable
    [Arguments]     ${host}
    ${result}=  Write       ping -c 4 ${host}
    ${output}=      Read        delay=5s
    Should Contain    ${output}    ttl=
    Log    ${output}    console=True

Get Ip From Host Profile
    [Documentation]     Gets the IP Address Configures in the Host profile
    [Arguments]     ${host_profile_uri}
    ${host_profile_detail}=     Get Host Profile by Uri     ${host_profile_uri}
    [return]        ${host_profile_detail['ipSettings']['ip']}
   