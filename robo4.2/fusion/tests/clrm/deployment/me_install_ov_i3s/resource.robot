*** Settings ***
Library           json
Resource          ../../../../Resources/api/fusion_api_resource.txt
Resource          ../../../i3s_osds_profiles/Resources/api/resource.robot
Variables         ../../../i3s_osds_profiles/environment_data.py
Variables         ${data_file}

*** Variables ***
#${fusion_ip}
${VERIFY}           True
${giSleep}          450
#${fusion_api_resource}      ../../../../Resources/api/fusion_api_resource.txt
${VAL_DELETE}               <Response [204]>
${POTASH}                   Virtual Connect SE 40Gb F8 Module for Synergy
${CHLORIDE10}               Synergy 10Gb Interconnect Link Module
${CHLORIDE20}               Synergy 20Gb Interconnect Link Module
${GI_SLEEP}                 600
${AB_SLEEP}                 180
${X-API-VERSION}            1000
${FUSION_TIMEOUT}           600
${SERVER_SSH_USERNAME}      root
${SERVER_SSH_PASSWORD}      imageMgmt123
${FUSION_SSH_USERNAME}      root
${FUSION_SSH_PASSWORD}      hpvse1
${FUSION_PROMPT}            \#
${data_file}                config_data.py

*** Keywords ***
Login to Appliance via SSH
    [Documentation]    Connect to Appliance CIM Bash via SSH
    ...                Example:\n| Login to Appliance Via SSH | 10.0.12.106 | Administrator | hpvse123 |
    [Arguments]    ${ip}    ${USERNAME}=${FUSION_SSH_USERNAME}
    ...            ${PASSWORD}=${FUSION_SSH_PASSWORD}
    ...            ${TIMEOUT}=${FUSION_PROMPT}    ${ALIAS}=APP_SSH
    ${Id} =    Open Connection    ${ip}    alias=${ALIAS}
    ${output} =    Login    ${USERNAME}    ${PASSWORD}
    [Return]    ${Id}

Is usb mounted on appliance
    [Documentation]    Is usb mounted on appliance
    [Arguments]      ${ip}
    Set Log Level    TRACE
    Login to Appliance via SSH    ${ip}
    ${output} =    Execute Command    cd /mnt/usb;echo $?
    Should Contain   ${output}    0
    [Return]    ${output}

Get files list in ddimage zip
    [Documentation]    Get files list in ddimage zip
    [Arguments]    ${files_count_zip}    @{words}
    ${file_list} =    Create List
    Log    ${file_list}    console=True
    :FOR    ${Y}    IN RANGE    0    ${files_count_zip}
    \    ${file} =    Get From List    ${words}    ${Y}
    \    Append to List    ${file_list}    ${file}
    [Return]    ${file_list}

Extract Build Name
    [Documentation]    Extracts the image name from the provided URL Seperated with /
    [Arguments]    ${URL}
    @{words} =    Split String    ${URL}    /
    ${buildName} =    Get From List    ${words}    -1
    Log    ${buildName}    console=True
    [return]    ${buildName}

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

Create Build Plan Payload
    [Documentation]    Create OS Build plan Payload
    [Arguments]    ${buildplan}
    ${osbp} =    copy.deepcopy    ${buildplan}
    ${buildSteps} =    Get from Dictionary    ${osbp}    buildStep
    :For    ${buildStep}    IN    @{buildSteps}
    \    ${planScript} =    Get From Dictionary    ${buildStep}    planScriptUri
    \    ${planScriptUri} =    Get Plan Script URI    ${planscript}
    \    Set To Dictionary    ${buildStep}    planScriptUri=${planScriptUri}
    [Return]    ${osbp}

Get plan Script URI
    [Documentation]    Get Plan script URI
    [Arguments]    ${planscript}
    ${resp} =    I3S Get Planscript    param=?filter="'name'=='${planscript}'"
    ${uri} =    Get From Dictionary    ${resp['members'][0]}    uri
    [Return]    ${uri}

Create Deploymentplan Payload
    [Documentation]    Create Deploymentplan Payload
    [Arguments]    ${deploymentplan}
    ${dp_body} =    copy.deepcopy    ${deploymentplan}

    #Buildplan URI
    ${bp_name} =    Get from Dictionary    ${dp_body}    oeBuildPlanURI
    ${bp_uri} =    Run Keyword If    '${bp_name}' is not ''    Get Buildplan URI    ${bp_name}
    Set to Dictionary    ${dp_body}    oeBuildPlanURI    ${bp_uri}

    #Goldenimage URI
    ${gi_name} =    Get from Dictionary    ${dp_body}    goldenImageURI
    ${gi_uri} =    Run Keyword If    '${gi_name}' is not ''    Get Goldenimage URI    ${gi_name}
    Set to Dictionary    ${dp_body}    goldenImageURI    ${gi_uri}
    [Return]    ${dp_body}

Get Buildplan URI
    [Documentation]    Get Buildplan URI
    [Arguments]    ${buildPlan}
    ${resp} =     i3s Get Buildplan    param=?filter="'name'=='${buildPlan}'"
    ${bpUri} =    Get From Dictionary    ${resp['members'][0]}    uri
    [Return]    ${bpUri}

Get Goldenimage URI
    [Documentation]    Get Goldenimage URI
    [Arguments]    ${goldenImage}
    ${resp} =     i3s Get Goldenimage    param=?filter="'name'=='${goldenImage}'"
    ${giUri} =    Run Keyword If    ${resp['count']}!=0    Get From Dictionary    ${resp['members'][0]}    uri
    ...    ELSE    Get From Dictionary    ${resp}    uri
    [Return]    ${giUri}

Wait For GI Complete
    [Documentation]    Wait for task to complete
    [Arguments]    ${response}    ${name}
    ${retry_interval}    Convert To Number    30
    ${retries}    Convert To Integer    30
    ${resp} =    i3s API Wait For Task To Complete    ${response['headers']['location']}    sleep_time=${retry_interval}    retries=${retries}

    # Check for errors
    ${errors} =    Get From Dictionary    ${resp}    taskErrors
    ${errCount} =    Get Length    ${errors}
    Run Keyword If    ${errCount} != 0
    ...    Log    Errors encountered while creating GI    level=WARN
    Should Be Equal As Integers    ${errCount}    0    msg=Could not create Golden Image !!
    Run Keyword If    ${errCount} == 0  Log    No errors
    ${response} =    i3s Api Get Golden Image    param=?filter="'name'=='${name}'"
    Run Keyword If    '${response['members'][0]['status']}' != 'OK'    Log    i3S API Add Golden Image failed,imageStatus not Active    console=True
    ${gv_image_uri} =    Get GoldenImage Uri    ${name}
    Sleep    ${giSleep}

    # Form param to get golden volume Uri
    ${gv_response} =    i3s Api Get Golden Volume    param=?filter="'imageuri'='${gv_image_uri}'"
    ${length} =    Get Length    ${gv_response['members']}
    Run Keyword If    ${length} == 1    GV Create Success    ${gv_response}    ${name}
    ...    ELSE
    ...    Should Be Equal as Strings    ${length}    1    msg=Failed to create GoldenImage for ${name}

GV Create Success
    [Documentation]    GV Create Success
    [Arguments]    ${gv_response}    ${name}
    Log To Console    Check GV status
    Run Keyword If    '${gv_response['members'][0]['status']}' == 'OK'
    ...    Log    GV_created_successfully for ${name}
    ...    ELSE
    ...    Log    GV created but status yet to get updated to OK

Get ArtifactBundle Uri
    [Documentation]    Get ArtifactBundle Uri
    [Arguments]    ${nName}
    ${resp} =    i3s Api Get Artifact Bundle    param=?filter="'name'=='${nName}'"
    ${uri} =    Run Keyword If    ${resp['count']}!=0    Get From Dictionary    ${resp['members'][0]}    uri
    ...    ELSE    Get From Dictionary    ${resp}    uri
    [Return]    ${uri}

Create Fusion IPv4 SubnetV4
    [Documentation]    Creates Fusion Subnet and returns the URI on success
    ...                This keyword requires a dictonary containing network information
    ...                { 'networkId': '', 'subnetmask': '', 'gateway': '', 'dnsServers': [], 'domain': ''}
    [Arguments]    ${subnet}

    &{data} =    Create Dictionary
    ...         type=Subnet
    ...         networkId=${subnet['networkId']}
    ...         subnetmask=${subnet['subnetmask']}
    ...         gateway=${subnet['gateway']}
    ...         dnsServers=@{subnet['dnsServers']}
    ...         domain=${subnet['domain']}

    ${resp} =    Fusion Api Create IPv4 Subnet    ${data}
    Should Be Equal As Integers    ${resp['status_code']}    200
    [Return]    ${resp['uri']}

Create Fusion IPv4 Pools
    [Documentation]    Creates Fusion IPv4 Address and Identifiers
    ...                This keyword requires the subnet URI and a dictionary containing
    ...                a list of ranges in the form {'name': '', 'startAddress': '', 'endAddress': ''}
    ...                The subnetURi should also be passed along for association
    [Arguments]    ${uri}    @{pools}

    :FOR    ${pool}    IN    @{pools}
    \    &{data} =    Create Dictionary
    \    ...         type=Range
    \    ...         name=${pool['name']}
    \    ...         startAddress=${pool['startAddress']}
    \    ...         endAddress=${pool['endAddress']}
    \    ...         subnetUri=${uri}
    \    ${resp} =    Fusion Api Create IPv4 Range    ${data}
    \    Should Be Equal As Integers    ${resp['status_code']}    200

Create Fusion Ethernet Network V4
    [Documentation]    Creates Fusion Ethernet network version 4
    ...    This keyword requires the subnet URI and a dictionary containing
    [Arguments]    ${net}    ${subnetUri}=None

    ${smartLink} =       Pop From Dictionary    ${net}    smartLink                 default=${False}
    ${pvtNet} =          Pop From Dictionary    ${net}    privateNetwork            default=${False}
    ${netType} =         Pop From Dictionary    ${net}    ethernetNetworkType       default=Tagged
    ${conTmpltName} =    Pop From Dictionary    ${net}    connectionTemplateName    default=${None}

    # Retrieve the connectionTemplateUri
    ${con_tmpl_uri} =    Set Variable If    ${conTmpltName}
    ...                 Get Network Connection Template Uri    ${conTmpltName}
    ...                 ${null}

    &{data} =    Create Dictionary
    ...         type=ethernet-networkV4
    ...         vlanId=${net['vlanId']}
    ...         purpose=${net['purpose']}
    ...         name=${net['name']}
    ...         smartLink=${smartLink}
    ...         privateNetwork=${pvtNet}
    ...         ethernetNetworkType=${netType}
    ...         connectionTemplateUri=${con_tmpl_uri}
    ...         subnetUri=${subnetUri}

    ${resp} =    Fusion Api Create Ethernet Network    ${data}
    Should Be Equal As Integers    ${resp['status_code']}    202

Get Network Connection Template Uri
    [Documentation]    The URIs are retrieved for the provided connection template name
    ...                Optional - name of the network connection template
    [Arguments]        ${tmpl_name}=None
    [Tags]             DEMO

    ${r} =    Run Keyword If    ${tmpl_name}
    ...                        Fusion Api Get Connection Templates    param=?filter="'name'=='${tmpl_name}'"
    ...      ELSE              Fusion Api Get Default Connection Template

    ${uri} =    Set Variable If    ${r['status_code']} == 200
    ...        ${r['uri']}    ${null}
    [Return]    ${uri}

Wait For Appliance To Become Pingable
    [Documentation]    Waits for an appliance to become pingable
    [Arguments]     ${appliance}={IP}   ${timeout}=1 min    ${interval}=5 s
    Wait Until Keyword Succeeds     ${timeout}    ${interval}    resource.Appliance is pingable    ${appliance}

Appliance is pingable
    [Documentation]    Appliance is pingable
    [Arguments]     ${appliance}
    Set Log Level   TRACE
    Run keyword if  os.name == "nt"    resource.Windows ping    ${appliance}
    ...         ELSE    Unix ping    ${appliance}

Windows ping
    [Documentation]    Windows ping
    [Arguments]     ${host}
    ${output} =    Run    ping -n 4 ${host}
    Should Contain    ${output}    Reply from ${host}
    [Return]    ${output}

Appliance is unreachable
    [Documentation]    Waits for an appliance to become unreachable
    [Arguments]    ${appliance}    ${timeout}=1 min    ${interval}=5 s
    Wait Until Keyword Succeeds    ${timeout}    ${interval}    Windows ping unreachable check    ${appliance}
    Set Log Level    TRACE
    Run keyword if    os.name == "nt"    Windows ping unreachable check    ${appliance}

Trigger on 2 node withcluster
    [Documentation]    Trigger on 2 node withcluster
    ${IP} =     Get From List   ${ov_appliances}    0
    ${command} =    Set Variable    /ci/etc/usb-reimage/developer_usb_reimage_two_node.sh -R
    OV Reimage    ${IP}    ${command}

Trigger on 2 node withoutcluster
    [Documentation]    Trigger on 2 node withoutcluster
    ${IP} =     Get From List   ${ov_appliances}    0
    ${command} =    Set Variable    /ci/etc/usb-reimage/developer_usb_reimage_two_node.sh -R
    OV Reimage    ${IP}    ${command}
    ${IP} =     Get From List   ${ov_appliances}    1
    ${command} =    Set Variable    /ci/etc/usb-reimage/developer_usb_reimage_two_node.sh -R
    OVReimage    ${IP}    ${command}

Trigger on 1 node
    [Documentation]    Trigger on 1 node
    ${IP} =     Get From List   ${ov_appliances}    0
    ${command} =    Set Variable    /ci/etc/usb-reimage/developer_usb_reimage.sh -R
    OV Reimage    ${IP}    ${command}

OV Reimage
    [Documentation]    OV Reimage
    [Arguments]    ${IP}    ${command}
    Login to Appliance via SSH    ${IP}
    Log    ${command}    console=True
    SSHLibrary.Write    ${command}
    SSHLibrary.Write    ${command}
    Log    developer_usb_reimage.sh script is running...    console=True
    ${output} =    Wait Until Keyword Succeeds    20 minutes    2 minutes
    ...    Read Until    Gaius reimage process takes 75 minutes.
    Log    ${output}
