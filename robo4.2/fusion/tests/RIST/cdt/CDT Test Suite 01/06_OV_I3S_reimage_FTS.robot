*** Settings ***
Library             RoboGalaxyLibrary
Library             i3SLibrary
Resource            ../resource.txt
Resource            ../resource_i3s_clrm.robot
Documentation       Deploy I3S, perform FTS on I3S and OV
Suite Setup         Set log level    TRACE

# Setup\Teardown for ALL test cases
Test Setup      Test Setup
Test Teardown   Test Teardown

*** Test Cases ***
Download required images
    [Documentation]     Downloads the required images
    ${gifiles}    Download artifact bundle files    ${GI_LIST}
    ${aafiles}    Download artifact bundle files    ${artifact_bundle_locations}
    Set Suite Variable    ${aafiles}    ${aafiles}

CREATE SUBNET
    [Documentation]    CREATE SUBNET
    :FOR    ${subnet}   in    @{subnets}
    \   ${resp} =    Fusion Api Create Ipv4 Subnet    body=${subnet}
    \   Run keyword and continue on failure    should be equal as integers    ${resp['status_code']}    200

CREATE RANGE
    [Documentation]    CREATE RANGE
    :FOR    ${range}    in    @{ranges}
    \   ${subnet_uri} =    Get Subnet uri    ${range['networkId']}
    \   Set to dictionary    ${range}    subnetUri=${subnet_uri}
    \   Remove From Dictionary    ${range}    networkId
    \   ${resp}=    Fusion Api Create Ipv4 Range    ${range}
    \   Run keyword and continue on failure    should be equal as integers    ${resp['status_code']}    200

CREATE NETWORKS AND ASSOCIATE SUBNET HAVING RANGE
    [Documentation]    CREATE NETWORKs AND ASSOCIATE SUBNET HAVING RANGE
    :FOR    ${network}    in    @{networks}
    \   ${networkId} =    Get From Dictionary    ${network}    networkId
    \   Remove From Dictionary    ${network}    networkId
    \   ${subnet_uri} =    Run Keyword If    '${networkId}' is not '${null}'    Get Subnet uri    ${networkId}
    \   Set to dictionary    ${network}    subnetUri=${subnet_uri}
    \   ${resp} =    Fusion Api Create Ethernet Network    body=${network}
    \   Run keyword and continue on failure    should be equal as integers    ${resp['status_code']}    202

Create Ethernet Networks
    [Documentation]             Create Ethernet Networks based on data definition
    [Tags]                      Networking
    ${ethernet_networks} =      Get Variable Value                      ${ethernet_networks}
    Run Keyword If              ${ethernet_networks} is not ${null}     Add Ethernet Networks from variable async
    ...                         ${ethernet_networks}

Add SAN Managers
    [Documentation]             Add SAN Managers to OneView
    [Tags]                      Storage
    Add San Managers Async      ${san_managers}

Add the Storage System to OV
    [Documentation]     Add the Storage System to OV
    [Tags]              Storage    Storage_System
    ${resplist} =       Add Storage Systems Async       ${storage_systems}
    Wait for task2      ${resplist}                     timeout=60      interval=10
    ${resp} =           Fusion Api Get Storage System   param=?filter="'name'=='${storage_systems[0]['name']}'"
    Run Keyword If      ${resp['count']}==0             FAIL            Addition of ${storage_systems[0]['name']} failed

Edit StoreServ Storage Sytem to be managed in OV
    [Documentation]     Edit StoreServ Storage Sytem to manage in OV
    [Tags]              Storage    Storage_System  StoreServ
    ${storage_system}    Get Data from Array by name    ${storage_systems}  ${STORESERV_NAME}
    ${store_serv}=      Create List    ${storage_system}
    ${resplist} =       Edit Storage Systems Async      ${store_serv}
    Wait for task2      ${resplist}                     timeout=180     interval=10
    ${resp} =           Fusion Api Get Storage System   param=?filter="'name'=='${store_serv[0]['name']}'"
    Run Keyword If      ${resp['count']}==0             FAIL            Addition of ${store_serv[0]['name']} failed
    Run keyword if      '${resp['members'][0]['status']}'!='OK' or '${resp['members'][0]['state']}'!='Managed'      FAIL
    ...                 Failed to manage StoreServ storage system

Configure Storage Pools in OV
    [Documentation]     Configure Storage Pools in OV
    [Tags]              Storage
    ${resplist} =       Edit Storage Pools Async    ${storage_pools}
    Wait for task2      ${resplist}                 timeout=120     interval=10
    Verify Storage Pool is Managed                  ${storage_pools}

Import Existing Storage Volumes
    [Tags]              Storage         EXISTING_VOLUMES
    [Documentation]     Import existing Storage Volumes from 3par
    ${resplist} =       Add Existing Storage Volumes Async      ${existing_volumes}
    Wait for task2      ${resplist}     timeout=120             interval=10
    
Create FCoE Networks
    [Documentation]         Create FCoE Networks based on data definition
    [Tags]                  Networking
    ${fcoe_networks} =      Get Variable Value                  ${fcoe_networks}
    Run Keyword If          ${fcoe_networks} is not ${null}     Add FCoE Networks from variable     ${fcoe_networks}

Create FC Networks
    [Documentation]     Create FC Networks based on data definition
    [Tags]              Networking
    ${fc_networks} =    Get Variable Value              ${fc_networks}
    Run Keyword If      ${fc_networks} is not ${null}   Add FC Networks from variable   ${fc_networks}

Create Network Sets
    [Documentation]     Create Network Sets based on data definition
    [Tags]              Networking
    ${network_sets} =   Get Variable Value                  ${network_sets}
    Run Keyword If      ${network_sets} is not ${null}      Add Network Sets from variable      ${network_sets}

Create OS Deployment Server
    [Documentation]    Create OS Deployment Server
    ${osds_body} =    Create Deployment Server Payload    ${osdeploymentserver}    I3S
    ${response} =    Fusion Api Create OS DeploymentServer    ${osds_body}
    Wait For task2    ${response}    timeout=1200    interval=60

Create LIGs
    [Documentation]     Create LIGs
    [Tags]              Networking
    ${sas_ligs} =       Get Variable Value              ${sas_ligs}
    ${sas_resplist}=    Run Keyword If      ${sas_ligs} is not ${null}      Run Keyword for Dict    ${sas_ligs}     Add SAS LIG
    ${ligs} =           Get Variable Value          ${ligs}
    ${lig_resplist}=    Run Keyword If      ${ligs} is not ${null}      Run Keyword for Dict    ${ligs}     Add LIG from variable async
    ${resplist}=    Combine Lists    ${sas_resplist}    ${lig_resplist}
    Wait for task2      ${resplist}                     timeout=20m      interval=10

Create EGs
    [Documentation]     Create EGs
    [Tags]              Networking
    ${enc_group_dict} =    Evaluate    copy.deepcopy(${enc_groups})    modules=copy
    ${resplist}=           Run Keyword for Dict    ${enc_group_dict}
    ...                 Add Enclosure Group from variable
    Wait for task2      ${resplist}                     timeout=5m      interval=10

Create LEs
    [Documentation]     Create LEs
    [Tags]              Networking                     Create_LE               Performance
    ...                 logical_enclosure-condition-single
    ${les} =            Get Variable Value              ${les}
    Create Logical Enclosures    ${les}
    Wait For Resources To Reach Desired State    False
    ${task}    Get Task By Param    param=?filter="'name'='Create' AND associatedResource.resourceName='${les[0]['name']}'"&sort=created:descending&count=1
    ${alt}    Get Active Alert List    ${task['created']}
    ${len}    Get length    ${alt}
    Run keyword and continue on failure    Run keyword if    ${len}!=0    FAIL    Critical/Active alerts exist.
    Check uplink sets and uplink ports

Get i3s Appliance Cluster IP and Login
    [Documentation]    Get i3s Appliance Cluster IP and Login
    ${resp} =    Fusion Api Get i3sCluster IP
    ${i3S_ip} =    Get From Dictionary    ${resp['members'][0]}    primaryIPV4
    ${response}    ${SessionId} =    Fusion Api Login Appliance    ${FUSION_IP}    ${admin_credentials}
    I3S API LOGIN APPLIANCE    ${i3S_ip}    ${SessionId}

Add Artifact Bundle
    [Documentation]    Add Artifact Bundle
    :FOR    ${aafile}   in    @{aafiles}
    \   ${response} =    i3s Api Add Artifact Bundle    ${aafile}
    \   Should Be Equal as Strings    ${response['status_code']}    202    msg=Failed to add Artifact Bundle.
    \   ${Retry Interval}    Convert To Number     60
    \   ${Retries}           Convert To Integer    3
    \   ${resp}=    i3s API Wait For Task To Complete   ${response['headers']['Location']}      sleep_time=${Retry Interval}    retries=${Retries}
    \   ${errors}=    Get From Dictionary    ${resp}    taskErrors
    \   ${errCount}=    Get Length    ${errors}
    \   Should be True    ${errCount} == 0    msg=Errors encountered while adding Artifact Bundle

Extract Artifact Bundle
    [Documentation]    Extract Artifact Bundle
    :FOR    ${artifactbundle_extract}   in    @{artifactbundle_extracts}
    \   ${name} =    Get From Dictionary    ${artifactbundle_extract}    name
    \   Log    \Extract Artifact Bundle ${name}.    console=True
    \   ${ab_uri} =    Get ArtifactBundle Uri    ${name}
    \   ${response} =    i3s Api Extract Artifact Bundle    ${ab_uri}
    \   Should Be Equal as Strings    ${response['status_code']}    202    msg=Failed to extract Artifact Bundle.
    \   ${Retry Interval}    Convert To Number     60
    \   ${Retries}           Convert To Integer    3
    \   ${resp}=    i3s API Wait For Task To Complete   ${response['headers']['Location']}      sleep_time=${Retry Interval}    retries=${Retries}
    \   ${errors}=    Get From Dictionary    ${resp}    taskErrors
    \   ${errCount}=    Get Length    ${errors}
    \   Should be True    ${errCount} == 0    msg=Errors encountered while adding Artifact Bundle

Add Golden Image
    [Documentation]    Add Golden Image
    ${len}    Get length    ${goldenimage}
    :FOR    ${index}    IN RANGE    0    ${len}
    \   ${name} =    Get From Dictionary    ${goldenimage[${index}]}    name
    \   ${desc} =    Get From Dictionary    ${goldenimage[${index}]}    description
    \   ${_}   ${file} =    Split Path    ${goldenimage[${index}]['location']}
    \   Move file   ${path}/${file}    ${path}/${filename}
    \   ${local_file} =    Get From Dictionary    ${goldenimage[${index}]}    file
    \   ${response} =    i3s Api Add Golden Image    ${local_file}    param=?name=${name}&description=${desc}
    \   ${Retry Interval}    Convert To Number    30
    \   ${Retries}    Convert To Integer    30
    \   ${Resp} =    i3s API Wait For Task To Complete    ${response['headers']['location']}    sleep_time=${Retry Interval}    retries=${Retries}
    \   Move file   ${path}/${filename}    ${path}/${file}
    Remove directory    ${path}    ${True}

Create Plan Script
    [Documentation]    Create Plan Script
    ${response} =    I3s Api Create Plan Scripts    ${planscript}
    Should Be Equal as Strings    ${response['status_code']}    201    msg=Failed to Create PS

Create OSBuildplan
    [Documentation]    Create OSBuildplan
    ${bp_body} =    CREATE BUILD PLAN PAYLOAD    ${buildplan}
    ${response} =    i3S_api_create_buildplan    ${bp_body}
    Should Be Equal as Strings    ${response['status_code']}    201    msg=Failed to Create Build Plan with Type Deploy

Create OEDeploymentplan
    [Documentation]    Create OEDeploymentplan
    :FOR    ${dp}   in    @{deploymentplan}
    \   ${dp_body} =    Create Deploymentplan Payload    ${dp}
    \   ${response} =    i3s Api Create Deploymentplan    ${dp_body}
    \   Should Be Equal as Strings    ${response['status_code']}    201    msg=Failed to Create DeploymentPlan
