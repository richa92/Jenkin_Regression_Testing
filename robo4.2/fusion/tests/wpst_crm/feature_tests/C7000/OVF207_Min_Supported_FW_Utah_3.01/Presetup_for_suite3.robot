*** Settings ***

Documentation     Feature Test: OVF207: C7000: Pre-setup for suite3 test case

Library                   FusionLibrary
Library                   RoboGalaxyLibrary
Library                   Collections
Library                   BuiltIn
Library                   OperatingSystem
Library                   Process
Library                   ServerOperations
Library                   Dialogs
Variables                 data_variables.py	

Resource            ../../../../resource/fusion_api_all_resource_files.txt


#This script has to be executed in 3.00 app with VC version 3.08.
#Download the necessary spp bundles and bin files into respective folders.

*** Test Cases ***
1.Login to Appliance  ###
    Set Log Level    TRACE
	Log to Console		${APPLIANCE_IP_3_00}
	Set Global Variable    ${APPLIANCE_IP}    ${APPLIANCE_IP_3_00}
    ${Login_response} =   Fusion Api Login Appliance    ${APPLIANCE_IP_3_00}        ${admin_credentials}
    Run keyword unless	${Login_response[0]['status_code']}== 200   Fail    "Unable to Login"
	
2.Initial Clean Up 
    Power OFF ALL Servers
    Remove ALL Server Profiles
    Remove ALL Enclosures
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Remove ALL Ethernet Networks
    Remove ALL FC Networks
    Remove ALL Users

3.Create LIG, EG and import enclosure 
    ${fc_networks} =    Get Variable Value    ${fcNet_utah}
    Run Keyword If   ${fc_networks} is not ${null}    Add FC Networks from variable    ${fc_networks}
	${Response}     fusion api create ethernet network		${enet_hill}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Create Ethernet network"
    ${body} =   Build LIG body      ${lig_utah_111}
    ${resp_lig} =    Fusion Api Create LIG    ${body}
    ${task} =    Wait For Task    ${resp_lig}    120s    2s
    Log to console and logfile    LIG created successfully
    ${uri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri
    Log to console and logfile    ${uri}

    ${enc_groups} =  Get Variable Value   ${enc_group_utah_111}
    Run Keyword If   ${enc_groups} is not ${null}   Add Enclosure Group from variable    ${enc_groups}
    Log to console and logfile    EG created succesfully
    ${EG_uri}=    Get Enclosure Group URI    ${EG1}
    Set To Dictionary    ${enc_body1}    enclosureGroupUri    ${EG_uri}
    ${resp_enc}=    Fusion Api Add Enclosure    ${enc_body1}
    Run keyword unless    ${resp_enc['status_code']}== 202    Fail    ${resp_enc['message']}
    ${task} =   Wait For Task    ${resp_enc}    15min   1min
    Log to console and logfile  \n\nImported the enc Successfully !!

#verify Utah FW with two step downgrade is successful.
4.Validate UTAH interconnect firmware version is 3.08
    #Pause Execution 
    :FOR    ${IC}    IN    @{INTERCONNECTS_UTAH}
    \   ${resp} =    Fusion Api Get Interconnect    param=?filter="'name' = '${IC}'"
    \   ${firmwareVersion} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion 
    \   Log to console and logfile    ${firmwareVersion}
    \   Run keyword If    ${firmwareVersion} != ${fc_firmwareVersion_latest}   Fail    "Firmware version mismatch"
	\   ...    ELSE     Log to console and logfile    \nFirmware Version is validated as ${fc_firmwareVersion_latest} for ${IC}
    
5.Uploading the FW bundle of Utah module version of 3.01 and 1.11
    Remove Environment Variable     https_proxy    http_proxy
    Log to console and logfile    \nUploading spp bundle with version 3.01"
    ${resp} =     Fusion Api Upload Firmware Bundle      localfile=${CURDIR}/SPP/${SPP_bundle_301}
    Log to Console    Uploadsppdetails ${resp}
    Log to Console and logfile    \n ${SPP_bundle_301}SPP bundle is successfully uploaded

    Log to console and logfile    \nUploading spp bundle with version 1.11"
    ${resp} =     Fusion Api Upload Firmware Bundle      localfile=${CURDIR}/SPP/${SPP_bundle_111}
    Log to Console    Uploadsppdetails ${resp}
    Log to Console and logfile    \n ${SPP_bundle_111}SPP bundle is successfully uploaded

6.Downgrading the firmware through LI page to 3.01
    Log to console and logfile     \nDowngrading firmware through LI page
    ${li_uri} =    Get LI URI   ${LI}
    Set to dictionary     ${liupdate_body}     sppUri    ${fw_uri_301}
    ${response}=    Fusion Api Li Upgrade Firmware    ${liupdate_body}    ${li_uri}
    Log to console    \n The response is:${response}
    Run Keyword If  ${response['status_code']} !=202    fail    msg=\nLI Firmware update Failed. \n ErrorCode:${response['errorCode']}\nMessage:${response['message']}
    ${task} =     Wait For Task        ${response}   60min    2min
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200   fail    msg=\nLI Firmware update Failed. \n ErrorCode:${task['taskErrors'][0][errorCode]}\n :Message ${task['taskErrors'][0][errorCode]}
    ...         ELSE    Log to console and logfile  \n\nLI FW Upgrade completed successfully by the Administrator user !!

7.Validate UTAH interconnect firmware version after downgrade is 3.01 and is configured
    :FOR    ${IC}    IN    @{INTERCONNECTS_UTAH}
    \   ${resp} =    Fusion Api Get Interconnect    param=?filter="'name' = '${IC}'"
    \   ${firmwareVersion} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion
    \   ${state}=    Get From Dictionary   ${resp['members'][0]}   state
    \   Log to console and logfile    ${firmwareVersion}
    \   Run keyword If    ${firmwareVersion} != ${fc_firmwareVersion_301}   Fail    "Firmware version mismatch"
    \   ...    ELSE     Log to console and logfile    \nFirmware Version is validated as ${fc_firmwareVersion_301} for ${IC}
    \   Run Keyword If    '${state}'!='Configured'    Fail    msg=\nThe IC ${IC} is not in configured state after downgrade
    \   ...      ELSE      Log to console and logfile    \nThe IC ${IC} is in configured state after downgrade

8.Downgrading to 1.11 from LE page
    ${resp} =    Fusion Api Get Logical Enclosure
    ${uri} =    Get From Dictionary    ${resp['members'][0]}    uri
    ${etag}=    Get From Dictionary    ${resp['members'][0]}    eTag
    ${headers} =   Get From Dictionary     ${resp}  headers
    Set To Dictionary    ${headers}    If-Match    ${etag}
    Set to dictionary     ${leupdate_body[0]['value']}    firmwareBaselineUri    ${fw_uri_111}
    ${response}=    Fusion Api Le Firmware Update    ${leupdate_body}    ${uri}    headers=${headers}

    Log to console	\n The response is:${response}
    Run Keyword If  ${response['status_code']} !=202    fail    msg=\nLE Firmware update Failed. \n ErrorCode:${response['errorCode']}\nMessage:${response['message']}
    ${task} =     Wait For Task        ${response}   60min    1min
    Run Keyword If  '${task['taskState']}' !='Completed' or ${task['status_code']} !=200   fail    msg=\nLE Firmware update Failed. \n ErrorCode:${task['taskErrors'][0][errorCode]}\n :Message ${task['taskErrors'][0][errorCode]}
    ...         ELSE    Log to console and logfile  \n\nLE FW Upgrade completed successfully !!

9.Validate UTAH interconnect firmware version after downgrade is 1.11 and is configured
    :FOR    ${IC}    IN    @{INTERCONNECTS_UTAH}
    \   ${resp} =    Fusion Api Get Interconnect    param=?filter="'name' = '${IC}'"
    \   ${firmwareVersion} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion
    \   ${state}=    Get From Dictionary   ${resp['members'][0]}   state
    \   Log to console and logfile    ${firmwareVersion}
    \   Run keyword If    ${firmwareVersion} != ${fc_firmwareVersion_old}   Fail    "Firmware version mismatch"
    \   ...    ELSE     Log to console and logfile    \nFirmware Version is validated as ${fc_firmwareVersion_old} for ${IC}
    \   Run Keyword If    '${state}'!='Configured'    Fail    msg=\nThe IC ${IC} is not in configured state after downgrade
    \   ...      ELSE      Log to console and logfile    \nThe IC ${IC} is in configured state after downgrade
	
Final Clean Up 
    Power OFF ALL Servers
    Remove ALL Server Profiles
    Remove ALL Enclosures
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Remove ALL Ethernet Networks
    Remove ALL FC Networks
    Remove ALL Users
	
*** Keywords ***
Log to console and logfile
	[Arguments]	${data}     ${level}=INFO
	Log	${data}     ${level}
	Log to console	${data}
	
Validate Response
    [Documentation]	Validates data in a response body against expected values
    ...	Example:
    ...	${rc} = 		Convert to Integer	400
	...	${valDict} = 	Create Dictionary	status_code=${rc}
	...										errorCode=CRM_DUPLICATE_NETWORK_NAME
	...	Validate Response	${respDict}	${valDict}
	[Arguments]    ${resp}	${validation}
	Set Log Level	TRACE	
	${response} = 	Copy Dictionary	${resp}	
	@{vkeys} =	Get Dictionary Keys	${validation}
	${rkeys} =	Get Dictionary Keys	${response}
	@{keys} =	Remove all the keys in response that are not in validation	${vkeys}	${rkeys}
	:FOR	${x}	IN	@{keys}
	\	Remove From Dictionary	${response}	${x}
	Dictionaries Should Be Equal	${validation}	${response}	msg=Response does not match validation dictionary	values=True
	
Remove all the keys in response that are not in validation
	[Arguments]	${vkeys}	${rkeys}
	:FOR	${x}	IN	@{vkeys}
	\	Remove Values From List	${rkeys}	${x}
	[Return]	${rkeys}