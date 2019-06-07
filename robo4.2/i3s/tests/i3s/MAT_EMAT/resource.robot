*** Settings ***
Documentation     Feature Test: Fusion i3S Integration
#Resource          ../../../../../Fusion/tests/tbird_hal/resources/defaults.txt
#Resource          ../../../../../Fusion/tests/tbird_hal/resources/fusion_api.txt
Resource          /robo4.2/fusion/Resources/api/fusion_api_resource.txt
#Resource         ../ ../../../../Fusion/tests/cim/api/Resource/CIM_Backup_Restore_Keyword.txt
#Resource          ../../Resources/api/resource.robot
#Resource          /robo4.2/i3s/tests/i3s/setup-bringup-keywords.txt

Library           Collections
Library           json
Library           DateTime
Library           OperatingSystem
Library           BuiltIn
Library           FusionLibrary
Library           i3SLibrary
Library           SSHLibrary
Library           String
# Library           robot.api.logger
#Library           Selenium2Library
Library           RoboGalaxyLibrary
# Library           Dialogs


*** Variables ***

${X-API-VERSION}              800
${VAL_DELETE}       <Response [204]>
${POTASH}           Virtual Connect SE 40Gb F8 Module for Synergy
${CHLORIDE10}       Synergy 10Gb Interconnect Link Module
${CHLORIDE20}       Synergy 20Gb Interconnect Link Module
#${X-API-VERSION}             '300'
${GI_SLEEP}         600
${AB_SLEEP}         180
${FUSION_TIMEOUT}             600
${SERVER_SSH_USERNAME}        root
${SERVER_SSH_PASSWORD}        imageMgmt123
${FUSION_SSH_USERNAME}        root             # Fusion SSH Username
${FUSION_SSH_PASSWORD}        hpvse1        # Fusion SSH Password
${FUSION_PROMPT}              \#               # Fusion Appliance Prompt

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
   Login to Appliance via SSH    ${ip}%${interface}
   ${output} =    Execute Command    cd /mnt/usb;echo $?
   Should Contain   ${output}    0
   [Return]    ${output}

Get files list in ddimage zip
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

Check signature of files in ddimage
    [Arguments]    ${gz_files_count}    ${gz_files}
    :FOR    ${Z}    IN RANGE    0    ${gz_files_count}
    \    ${file_name} =    Get From List    ${gz_files}    ${Z}
    \    ${output} =    Execute Command    cd /ci/etc/usb-reimage/;gpg --import hpPublicKey2048_key1.pub
    \    ${output} =    Execute Command    cd /mnt/usb;gpg --check-sigs B1275EA3
    \    ${output} =    Execute Command    cd /mnt/usb;ls
    \    ${output} =    Execute Command    cd /mnt/usb;gpg --verify ${file_name}.sig ${file_name};echo $?
    \    Should Contain    ${output}    0

Appliance is unreachable
    [Documentation]    Waits for an appliance to become unreachable
    [Arguments]     ${appliance}    ${timeout}=1 min    ${interval}=5 s
    Wait Until Keyword Succeeds     ${timeout}    ${interval}    Unix ping6 unreachable check     ${appliance}
    Set Log Level    TRACE
    Run keyword 	resource.Unix ping6 unreachable check  ${appliance}	
	
Unix ping6 unreachable check
	[Arguments]    ${host}
	${output}=  Run   ping6 -c 5 ${host}%${interface}
	Should Contain 	  ${output}   Destination unreachable
	[Return]   ${output}
	

Trigger on 2 node withoutcluster
    ${IP} =    Get From List   ${ov_appliances}    1
	Login to Appliance via SSH    ${IP}%${interface}
    ${output} =   Execute Command    /sbin/hponcfg -f /ci/etc/usb-reimage/ilo_ribcl_developer_usb_reimage.xml
	Sleep	30s
	Log    ${output}    console=True
	Log to console    ilo_ribcl_developer_usb_reimage.xml script is running...
    Should Contain    ${output}    Script succeeded	
	Log to console 		Going for Reboot
	${output2} =		Start Command		reboot --force --force now
	Log    ${output2}    console=True
	Sleep  180s
	
    ${IP} =    Get From List    ${ov_appliances}    0
	Login to Appliance via SSH    ${IP}%${interface}
    ${output} =   Execute Command    /sbin/hponcfg -f /ci/etc/usb-reimage/ilo_ribcl_developer_usb_reimage.xml
	Sleep	30s
    Log    ${output}    console=True
	Log to console    ilo_ribcl_developer_usb_reimage.xml script is running...
    Should Contain    ${output}    Script succeeded
	Log to console		Going For Reboot
	${output2} =		Start Command		reboot --force --force now
	Log    ${output2}    console=True
	

Trigger on 2 node withcluster
     ${IP} =    Get From List   ${ov_appliances}    1
	Login to Appliance via SSH    ${IP}%${interface}
    ${output} =   Execute Command    /sbin/hponcfg -f /ci/etc/usb-reimage/ilo_ribcl_developer_usb_reimage.xml
	Sleep	30s
	Log    ${output}    console=True
	Log to console    ilo_ribcl_developer_usb_reimage.xml script is running...
    Should Contain    ${output}    Script succeeded	
	Login to console	Going for reboot
	${output2} =		Start Command		reboot --force --force now
	Log    ${output2}    console=True
	Sleep  180s
	
    ${IP} =    Get From List    ${ov_appliances}    0
	Login to Appliance via SSH    ${IP}%${interface}
    ${output} =		Execute Command    /sbin/hponcfg -f /ci/etc/usb-reimage/ilo_ribcl_developer_usb_reimage.xml
	Sleep	30s
    Log    ${output}    console=True
	Log to console    ilo_ribcl_developer_usb_reimage.xml script is running...
    Should Contain    ${output}    Script succeeded	
	Log to console	Going For Reboot
	${output2} =		Start Command		reboot --force --force now
	Log    ${output2}    console=True
	
	
Trigger on 1 node
	${IP} =    Get From List    ${ov_appliances}	0
    Login to Appliance via SSH    ${IP}%${interface}
    ${output} =   Execute Command    /sbin/hponcfg -f /ci/etc/usb-reimage/ilo_ribcl_developer_usb_reimage.xml
	Sleep	30s
    Log    ${output}    console=True
	Log to console    ilo_ribcl_developer_usb_reimage.xml script is running...
    Should Contain    ${output}    Script succeeded	
	Log to console	Going For Reboot
	${output2} =		Start Command		reboot --force --force now
	Log    ${output2}    console=True
	
	
Wait for appliance webapps to startup
    [Arguments]     ${ip}
    Set Log Level  TRACE
    Login to Appliance via SSH  ${ip}%${interface}
    ${output} =   Execute Command  /ci/bin/wait-for-cic
    Should Contain  ${output}    done
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

Wait For GI Complete
    [Arguments]    ${Response}    ${NAME}
    ${Retry Interval}    Convert To Number    30
    ${Retries}    Convert To Integer    30
    ${Resp} =    i3s API Wait For Task To Complete    ${Response['headers']['location']}    sleep_time=${Retry Interval}    retries=${Retries}
    # Check for errors
    ${Errors} =    Get From Dictionary    ${Resp}    taskErrors
    ${Errors} =    Get Length    ${Errors}
    Run Keyword If    ${Errors} != 0    Log    Errors encountered while creating GI    level=WARN
    Should Be Equal As Integers    ${Errors}    0    msg=Could not create Golden Image !!
    Run Keyword If    ${Errors} == 0    Log  No errors    console=True
    ${Response} =    i3s Api Get Golden Image    param=?filter="'name'=='${NAME}'"
    Run Keyword If    '${Response['members'][0]['status']}' != 'OK'
         ...    Log    i3S API Add Golden Image failed,imageStatus not Active    console=True
    Run Keyword If    '${Response['members'][0]['status']}' == 'OK'
      ...       Log    i3S API Add Golden Image successful,imageStatus is Active
    ${gv_image_uri} =    Get GoldenImage Uri    ${NAME}
    Sleep    ${GI_SLEEP}
    # Form param to get golden volume Uri
    ${GV_Response} =    i3s Api Get Golden Volume    param=?filter="'imageuri'='${gv_image_uri}'"
    ${length} =    Get Length    ${GV_Response['members']}
    Run Keyword If    ${length} == 1    GV Create Success    ${GV_Response}    ${NAME}
    ...         ELSE    Should Be Equal as Strings    ${length}    1    msg=Failed to create GoldenImage for ${NAME}

Get Goldenimage URI
    [Documentation]    Get Goldenimage URI
    [Arguments]    ${goldenImage}
    ${resp} =     i3s Get Goldenimage    param=?filter="'name'=='${goldenImage}'"
    ${giUri} =     Get From Dictionary    ${resp['members'][0]}    uri
    [Return]    ${giUri}

GV Create Success
    [Documentation]    GV Create Success
    [Arguments]    ${GV_Response}    ${NAME}
    Log To Console    Check GV status
    Run Keyword If    '${GV_Response['members'][0]['status']}' == 'OK'
    ...    Log To Console    GV_created_successfully for ${NAME}
    ...    ELSE
    ...    Log to Console    GV created but status yet to get updated to OK

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
    ${uri} =    Get From Dictionary    ${resp['members'][0]}   uri
    [Return]    ${uri}

Create Artifact Bundle Payload
    [Arguments]    ${artifactbundle}
    ${ab_body} =    Copy Dictionary  ${artifactbundle}

    # GoldenImage URI
    ${Gstatus} =    run keyword and return status    Dictionary should contain key    ${ab_body}    goldenImages
    ${gi_body} =    Run keyword if    ${Gstatus} ==${True}    Get from Dictionary    ${ab_body}    goldenImages
    ${mx} =    Run keyword if    ${Gstatus} ==${True}    Get Length    ${gi_body}
    ${gisUri} =    Run keyword If    '${mx}'!='None'    Get Goldenimage Body    ${mx}    ${gi_body}

    # Planscript URI
    ${Pstatus} =    run keyword and return status    Dictionary should contain key    ${ab_body}    planScripts
    ${ps_body} =    Run keyword if    ${Pstatus} ==${True}    Get from Dictionary    ${ab_body}    planScripts
    ${mx} =    Run keyword if    ${Pstatus} ==${True}    Get Length    ${ps_body}
    ${psUri} =    Run keyword If    '${mx}'!='None'    Get Planscript Body    ${mx}    ${ps_body}

    # Buildplan URI
    ${Bstatus} =    run keyword and return status    Dictionary should contain key    ${ab_body}    buildPlans
    ${bp_body} =    Run keyword if    ${Bstatus} ==${True}    Get from Dictionary    ${ab_body}    buildPlans
    ${mx} =    Run keyword if    ${Bstatus} ==${True}    Get Length    ${bp_body}
    ${bpUri} =    Run keyword If    '${mx}'!='None'    Get Buildplan Body    ${mx}    ${bp_body}

    #Deploymentplan URI
    ${Dstatus} =    run keyword and return status    Dictionary should contain key    ${ab_body}    deploymentPlans
    ${dp_body} =    Run keyword if    ${Dstatus} ==${True}    Get from Dictionary    ${ab_body}    deploymentPlans
    ${mx} =    Run keyword if    ${Dstatus} ==${True}    Get Length    ${dp_body}
    ${depUri} =    Run keyword If    '${mx}'!='None'    Get Deploymentplan Body    ${mx}    ${dp_body}
    [Return]    ${ab_body}

Get ArtifactBundle Uri
    [Arguments]    ${Name} 
    ${resp} =    i3s Api Get Artifact Bundle    param=?filter="'name'=='${NAME}'"
    ${uri} =    Get From Dictionary    ${resp['members'][0]}    uri
    [Return]    ${uri}

Get Goldenimage Body
    [Arguments]    ${mx}    ${gi_body}
    :FOR    ${IND}    IN RANGE    0    ${mx}
    \    ${giuri} =    Get From Dictionary    ${gi_body[${IND}]}    resourceUri
    \    ${uri} =    Get Goldenimage Uri    ${giuri}
    \    Set to Dictionary    ${gi_body[${IND}]}    resourceUri    ${uri}
    [Return]    ${gi_body}

Get Planscript Body
    [Arguments]    ${mx}    ${ps_body}
    :FOR    ${IND}    IN RANGE    0    ${mx}
    \    ${psuri} =    Get From Dictionary    ${ps_body[${IND}]}    resourceUri
    \    ${uri} =    Get Planscript Uri    ${psuri}
    \    Set to Dictionary    ${ps_body[${IND}]}    resourceUri    ${uri}
    [Return]    ${ps_body}

Get Buildplan Body
    [Arguments]    ${mx}    ${bp_body}
    :FOR    ${IND}    IN RANGE    0    ${mx}
    \    ${bpuri} =    Get From Dictionary    ${bp_body[${IND}]}    resourceUri
    \    Log    ${bpuri}    console=True
    \    ${uri} =    Get Buildplan Uri    ${bpuri}
    \    Set to Dictionary    ${bp_body[${IND}]}    resourceUri    ${uri}
    [Return]    ${bp_body}

Get Deploymentplan Body
    [Arguments]    ${mx}    ${dp_body}
    :FOR    ${IND}    IN RANGE    0    ${mx}
    \    ${dpuri} =    Get From Dictionary    ${dp_body[${IND}]}    resourceUri
    \    Log to console    ${dpuri}
    \    ${uri} =    Get Deploymentplan Uri    ${dpuri}
    \    Set to Dictionary    ${dp_body[${IND}]}    resourceUri    ${uri}
    [Return]    ${dp_body}

Get Deploymentplan Uri
    [Arguments]    ${dpuri}
    ${resp} =   i3s Get Deploymentplan     param=?filter="'name'=='${dpuri}'"
    ${uri} =    Get From Dictionary    ${resp['members'][0]}   uri 
    [Return]    ${uri}
	
Wait For Appliance Reachability
	[Documentation]    Waits for an appliance reachability
	[Arguments]     ${appliance}={IP}   ${timeout}=1 min    ${interval}=5 s
	Wait Until Keyword Succeeds     ${timeout}    ${interval}    resource.Appliance reachability    ${appliance}
	
Appliance reachability
	[Arguments]     ${appliance}
	Set Log Level   TRACE
	Run keyword		resource.Unix ping4    ${appliance}
	
Unix ping4
	[Arguments]    ${host}
	${output}=  Run   ping -c 5 ${host}
	Should Contain 	  ${output}   64 bytes from ${host}
	[Return]   ${output}	
	
Wait For Appliance To Become Pingable
    [Documentation]    Waits for an appliance to become pingable
    [Arguments]     ${appliance}={IP}   ${timeout}=1 min    ${interval}=5 s
    Wait Until Keyword Succeeds     ${timeout}    ${interval}    resource.Appliance is pingable    ${appliance}


Appliance is pingable
    [Arguments]     ${appliance}
    Set Log Level   TRACE
    Run keyword		resource.Unix ping6    ${appliance}
       

Unix ping6
	[Arguments]    ${host}
	${output}=  Run   ping6 -c 5 ${host}%${interface}
	Should Contain 	  ${output}   64 bytes from ${host}
	[Return]   ${output}

Get Interconnect Type URI
    [Documentation]    Get Interconnect type URI for the named interconnect
    [Arguments]     ${ic}
    ${resp} =   Fusion Api Get Interconnect Types       param=?filter="'name'=='${ic}'"
    ${uri} =    Get From Dictionary     ${resp['members'][0]}   uri
    [Return]    ${uri}
	
	
Get OS Volume From Server Profile
    [Documentation]    Get OS Volume From Server Profile
    [Arguments]    ${spname}
    ${sp_body}=    Get Server Profile   ${spname}
    ${OSDS}=    Get from Dictionary    ${sp_body}    osDeploymentSettings
    ${osvol}=    Get from Dictionary    ${OSDS}    osVolumeUri
    Return From Keyword If    '${osvol}' == 'None'
    ${resp} =    Get Resource by URI    ${osvol}
    Log    \nOS Volume '${resp['osVolumeName']}' is attached to Server profile '${spname}'    console=True
    [Return]    ${resp['osVolumeName']}
	
	
Get Server Profile OS Volume URI
    [Documentation]    Get OS Volume From Server Profile
    [Arguments]    ${spname}
    ${sp_body}=    Get Server Profile   ${spname}
    ${OSDS}=    Get from Dictionary    ${sp_body}    osDeploymentSettings
    ${osVolumeUri}=    Get from Dictionary    ${OSDS}    osVolumeUri
    [Return]    ${osVolumeUri}
	

	
Create GI Capture Payload
	[Arguments]		${creategoldenimage}	
	${gic_body} =  Copy Dictionary  ${creategoldenimage}	
	#Buildplan URI	
	${bp_name} =	Get from Dictionary	 ${gic_body}	buildPlanUri
	${bp_uri} =	Run Keyword If  '${bp_name}' is not ''		Get Buildplan URI		${bp_name}
	Set to Dictionary	${gic_body}  buildPlanUri	${bp_uri}	
	#OSvolume URI
	${sp_name} =	Get from Dictionary	${gic_body}	osVolumeURI
	${osvolume_uri} =	Run Keyword If  '${sp_name}' is not ''		Get OSvolume URI		${sp_name}
	#${response} = 	i3s Get Statelessserver	param=?filter="'name'=='${sp_name}'"
	#${osvolume_uri} = 	Get From Dictionary		${response['members'][0]}	oeVolume
	Set to Dictionary	${gic_body}  osVolumeURI	${osvolume_uri}	
	[Return]	${gic_body}
	
Get OSvolume Uri
	[Arguments]		${osvolumename}
	${resp} = 	i3s Get Statelessserver  param=?filter="'name'=='${osvolumename}'"	
	${uri} = 	Run Keyword if  ${resp['count']} != 0   
	 ...    Get From Dictionary		${resp['members'][0]}	oeVolume
	 ...    ELSE 
	 ...    Set Variable    ${InvalidOSvolumeUri}
	[Return]	${uri}
	
Wait For GIC Complete
    # Wait for task to complete
    [Arguments]    ${Response}    ${NAME}
    Log to Console and Logfile    ${Response}
	${Retry Interval}    Convert To Number    30
	${Retries}    Convert To Integer    30
	${Resp}=    i3s API Wait For Task To Complete	${Response['headers']['location']}    sleep_time=${Retry Interval}    retries=${Retries}
	
	# Check for errors
	${Errors}=    Get From Dictionary    ${Resp}    taskErrors
	${Errors}=    Get Length    ${Errors}
	Run Keyword If    ${Errors} != 0
		...    Log    Errors encountered while creating GI    level=WARN
	Should Be Equal As Integers    ${Errors}    0    msg=Could not create Golden Image !!
    Run Keyword If    ${Errors} == 0  Log to console  No errors
        ${Response}=    i3s Api Get Golden Image    param=?filter="'name'=='${NAME}'"
        Run Keyword If    '${Response['members'][0]['status']}' != 'OK'
            ...    Log to console    i3S API Add Golden Image failed,imageStatus not Active
        Run Keyword If	'${Response['members'][0]['status']}' == 'OK'
            ...    Log To Console    i3S API Add Golden Image successful,imageStatus is Active
        ${gv_image_uri}=    Get GoldenImage Uri    ${NAME}
        Sleep    ${GI_SLEEP}
        #Form param to get golden volume Uri
        ${GV_Response}=    i3s Api Get Golden Volume    param=?filter="'imageuri'='${gv_image_uri}'"
        ${length}=    Get Length    ${GV_Response['members']}
        Run Keyword If    ${length} == 1    GV Create Success    ${GV_Response}    ${NAME}
        ...    ELSE
	    ...    Should Be Equal as Strings    ${length}    1    msg=Failed to create GoldenImage for ${NAME}
		
Change Deployment Plan IN Server Profile body
    [Arguments]    ${SP_body}    ${Index}
    ${payload} =    Copy Dictionary    ${SP_body}
    ${DP} =    Get From Dictionary    ${OSDP[${Index}]}    name
    Set to Dictionary    ${payload['osDeploymentSettings']}    osDeploymentPlanUri=${DP}
    [Return]    ${payload}
	
	
Efuse blade by profile
    [Arguments]     ${profile}    ${action}
    ${profile}=  copy dictionary     ${serverprofile_3enc}
    ${server} =  set variable  ${profile['serverHardwareUri']}
    ${server} =  replace string using regexp  ${server}  SH:  ${EMPTY}
    ${words} =  set variable  ${server.split(',')}
    ${enclosure} =  set variable  ${words[0]}
    ${bay} =  set variable  ${words[1]}
    ${bay} =  set variable  ${bay.strip()}
    ${bay} =  set variable  ${bay[-1]}
    Get EM IP
    Get EM Token    ${enclosure}
    EFuse Blade   ${action}     ${bay}
	
	
Profile In Critical Status
    [Arguments]    ${profile}
    Set Log Level    TRACE
	${profile} =   Fusion Api Get Server Profiles     ${profile['uri']}
    ${status} =  Get From Dictionary  ${profile}  status
    Log to console and logfile    \t Server Profile: [${profile['name']}] is: ${status}
    Should Match    ${status}    Critical

Profile In OK Status
    [Arguments]    ${profile}
    Set Log Level    TRACE
	${profile} =   Fusion Api Get Server Profiles     ${profile['uri']}
    ${status} =  Get From Dictionary  ${profile}  status
    Log to console and logfile    \t Server Profile: [${profile['name']}] is: ${status}
    Should Match    ${status}    OK

Profile In Updating State
    [Arguments]    ${profile}
    Set Log Level    TRACE
	${profile} =   Fusion Api Get Server Profiles     ${profile['uri']}
    ${state} =  Get From Dictionary  ${profile}  state
    Log to console and logfile    \t Server Profile: [${profile['name']}] is: ${state}
    Should Match    ${state}    Updating
	
Wait For Appliance State To Be UPGRADE
    [Documentation]   Wait For Appliance State To Be UPGRADE
    [Arguments]       ${timeout}=20 min    ${interval}=30 s
    Wait Until Keyword Succeeds    ${timeout}    ${interval}        Appliance State Should Be UPGRADE

Wait For Appliance State To Be OK
    [Documentation]  Wait For Appliance State To Be OK
    [Arguments]      ${timeout}=20 min    ${interval}=30 s
    Wait Until Keyword Succeeds    ${timeout}    ${interval}        Appliance State Should Be OK

Appliance State Should Be UPGRADE
    [Documentation]  Appliance State Should Be UPGRADE
    ${state} =    Fusion Api Get Resource    /controller-state.json
    Log      -Appliance state: ${state['state']}  console=True
    Should Match Regexp        ${state['state']}    ((?i)UPGRADE)

Appliance State Should Be OK
    [Documentation]  Appliance State Should Be OK
    ${state} =    Fusion Api Get Resource    /controller-state.json
    Log      -Appliance state: ${state['state']}  console=True
    Should Match Regexp    ${state['state']}    ((?i)OK)
	
Import Certificate to OV
    [Documentation]    Adds the TAO Certificates from TAO to OneView Appliance
    [Arguments]    ${TAO_IP}    ${OV_IP}    ${OV_credentials}	${alias_name}
    Fusion Api Login Appliance    ${OV_IP}    ${OV_credentials}
    ${response} =  Fusion Api Get Remote Certificate        ${TAO_IP}
    Set To Dictionary    ${CERTIFICATE['certificateDetails'][0]}    base64Data    ${response['certificateDetails'][0]['base64Data']}
	${headers}=		Fusion APi Get Headers
	set to Dictionary		${headers}		forceSaveLeaf=True
	set to Dictionary		${CERTIFICATE['certificateDetails'][0]}		aliasName=${alias_name}
    ${resp}=        Fusion Api Import Server Certificate   ${CERTIFICATE}		headers=${headers}
    ${task}=       Wait For Task   ${resp}         timeout=500s            interval=5s
    ${response} =  Fusion Api Get Server Certificate   ${alias_name}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha1Fingerprint']}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha256Fingerprint']}
    Should Not Be Empty  ${response['certificateDetails'][0]['sha384Fingerprint']}

Collect SupportDump on Failure
    [Documentation]     Collect Support Dump on failure of the test case
    Run Keyword If Test Failed      Collect Support Dump    	${File_location}\\CLRM_MAT_SupportDump.sdmp

Collect Support Dump
    [Documentation]		Collect logs from the OV Appliance and places it support dump loc
    [Arguments]     ${File_location}
	${sd_body}=    Create Dictionary                   encrypt=${false}    errorCode=CI
    ${sd_resp}=    Fusion Api Create Support Dump      ${sd_body}
	Return From Keyword If		${sd_resp} is None or ${sd_resp['status_code']} !=200
    ${uri}=     Get From Dictionary                 ${sd_resp}             uri
    ${resp}=    Fusion Api Download Support Dump    uri=${uri}          localfile=${File_location}
	
	
Get Temporary IP for OV Login
    [Arguments]        ${os}  ${ipv6}  ${iface}  ${ipv4}  ${nmask}  ${gway_ipv4}
    Log to Console  Get Temporary IP for OV Login
    Log to Console  ${os}, ${ipv6}, ${iface}, ${ipv4}, ${nmask}, ${gway_ipv4}
    Run Keyword If  '${os}' == '1'  Get Temporary IP for OV Login Worker  ${ipv6}  ${iface}  ${ipv4}  ${nmask}  ${gway_ipv4}
    ${result} =  Run Keyword If  '${os}' == '1'  Set Variable  ${ipv4}  ELSE  Set Variable  ${ipv6}
    [return]    ${result}

Get Temporary IP for OV Login Worker
    [Arguments]        ${ipv6}  ${iface}  ${ipv4}  ${nmask}  ${gway_ipv4}
    Log to Console  Login Worker says ${ipv6}, ${iface}, ${ipv4}, ${nmask}, ${gway_ipv4}
    Login to Appliance via SSH		${ipv6}%${iface}
	Log to console	Logged onto appliance
    Execute command		ifconfig eth0 ${ipv4} netmask ${nmask} up
    Execute command		route add default gw ${gway_ipv4} eth0


Remove Temporary IP for OV Login
    [Arguments]        ${os}  ${ipv4}  ${ipv6}  ${iface}
    Run Keyword If  '${os}' == '1'   Remove Temporary IP for OV Login Worker  ${ipv4}  ${ipv6}  ${iface}

Remove Temporary IP for OV Login Worker
    [Documentation]    
    [Arguments]        ${ipv4}  ${ipv6}  ${iface}
    Log to Console  Remove IP Worker says ${ipv4} ${ipv6} ${iface}
    Login to Appliance via SSH  ${ipv6}%${interface}
    Execute command  ip addr del ${ipv4} dev eth0


Get OV Session
    [Documentation]     This would have worked better if we figured out how to regex the IP
    [Arguments]    ${credentials}  ${ov_ip}  ${iptype}=4
    Run Keyword If  '${iptype}' == '6'   Get OV Session WorkerSix   ${credentials}  ${ov_ip}
    Run Keyword If  '${iptype}' == '4'   Get OV Session WorkerFour   ${credentials}  ${ov_ip}

Get OV Session WorkerSix
    [Documentation]     This will NOT WORK FROM A LINUX VM
    [Arguments]    ${admin_credentials}  ${ov_ip}
    ${Response}    ${SessionId} =    Fusion Api Login Appliance    [${ov_ip}]    ${admin_credentials}    300
    Run Keyword If  ${Response['status_code']} != 200  Fail  msg="Unable to get a session to OV via ${ov_ip}"

Get OV Session WorkerFour
    [Arguments]    ${admin_credentials}  ${ov_ip}
    Log to Console   Get OV Session WorkerFour says		${ov_ip}
    ${Response}    ${SessionId} =    Fusion Api Login Appliance    ${ov_ip}    ${admin_credentials}    300
    Run Keyword If  ${Response['status_code']} != 200  Fail  msg="Unable to get a session to OV via ${ov_ip}"
    Run Keyword If  ${Response['status_code']} == 200  Log to Console  Got a Fusion Login session to ${ov_ip}
	
