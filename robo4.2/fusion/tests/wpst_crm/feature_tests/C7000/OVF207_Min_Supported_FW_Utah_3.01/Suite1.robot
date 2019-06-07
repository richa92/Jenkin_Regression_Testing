*** Settings ***

Documentation     Feature Test: OVF207: C7000: Minimum Supported Version of Utah FW 3.01
...               OVTC556--OVF207_API_TC_Verify the LI and LE upgrade only available to privileged users only.
...               Assumptions : Currently installed FW is 3.08
...				  OVTC564 --OVF207_API_TC_verify Utah FW downgrade not allowed from 3.08 to prior to 3.01


Library                   FusionLibrary
Library                   RoboGalaxyLibrary
Library                   Collections
Library                   BuiltIn
Library                   OperatingSystem
Library                   Process
Variables                 data_variables.py	

Resource            ../../../../resource/fusion_api_all_resource_files.txt

*** Test Cases ***
Step-1.Login to Appliance  ###
    Set Log Level    TRACE
    Set Global Variable    ${APPLIANCE_IP}    ${APPLIANCE_IP_3_10}
    ${Login_response} =   Fusion Api Login Appliance    ${APPLIANCE_IP_3_10}        ${admin_credentials}
    Run keyword unless	${Login_response[0]['status_code']}== 200   Fail    "Unable to Login"
    Log to console and logfile    Logged in to the appliance

Step-2.Initial Clean Up 
    Power OFF ALL Servers
    Remove ALL Server Profiles
    Remove ALL Enclosures
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Remove ALL Ethernet Networks
    Remove ALL FC Networks
    Remove ALL Users

Step-3.Create LIG, EG and import enclosure ###
    ${fc_networks} =    Get Variable Value    ${fcNet_utah}
    Run Keyword If   ${fc_networks} is not ${null}    Add FC Networks from variable    ${fc_networks}
    ${body} =   Build LIG body      ${lig_utah}
    ${resp_lig} =    Fusion Api Create LIG    ${body}
    ${task} =    Wait For Task    ${resp_lig}    120s    2s
    Log to console and logfile    LIG created successfully
    ${uri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri
    Log to console and logfile    ${uri}

    ${resp_eg}=    Add Enclosure Group from variable   ${enc_group_utah}
    #Run keyword unless	${resp_eg['status_code']}== 201	Fail	"Unable to Create EG"
    Log to console and logfile    EG created succesfully
    ${EG_uri}=    Get Enclosure Group URI    ${EG1}
    Log to console and logfile    EG created successfully
    Set To Dictionary    ${enc_body1}    enclosureGroupUri    ${EG_uri}
    ${resp_enc}=    Fusion Api Add Enclosure    ${enc_body1}
    Run keyword unless	${resp_enc['status_code']}== 202    Fail    ${resp_enc['message']}
    ${task} =   Wait For Task    ${resp_enc}    20min  1min
    Log to console and logfile  \n\nImported the enc Successfully !!
	
OVTC556-Step1.Uploading the FW bundle of Utah module version of 3.01 and 3.08####
    Remove Environment Variable     https_proxy    http_proxy
    Log to console and logfile    \nUploading spp bundle with version 3.01"
    ${resp} =     Fusion Api Upload Firmware Bundle      localfile=${CURDIR}/SPP/${SPP_bundle_301}
    Log to Console    Uploadsppdetails ${resp}
    Log to Console and logfile    \n ${SPP_bundle_301}SPP bundle is successfully uploaded

    Log to console and logfile    \nUploading spp bundle with version 3.08"
    ${resp} =     Fusion Api Upload Firmware Bundle      localfile=${CURDIR}/SPP/${SPP_bundle_308}
    Log to Console    Uploadsppdetails ${resp}
    Log to Console and logfile    \n ${SPP_bundle_308}SPP bundle is successfully uploaded

OVTC556-Step2.Validate UTAH interconnect firmware version is 3.08 ###
    :FOR    ${IC}    IN    @{INTERCONNECTS_UTAH}
    \   ${resp} =    Fusion Api Get Interconnect    param=?filter="'name' = '${IC}'"
    \   ${firmwareVersion} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion 
    \   Log to console and logfile    ${firmwareVersion}
    \   Run keyword If    ${firmwareVersion} != ${fc_firmwareVersion_latest}   Fail    "Firmware version mismatch"
	\   ...    ELSE     Log to console and logfile    \nFirmware Version is validated as ${fc_firmwareVersion_latest} for ${IC}

OVTC556-Step3.Downgrading the firmware through LI page to 3.01 by the Administrator ####
    Log to console and logfile     \nDowngrading firmware through LI page
    ${li_uri} =    Get LI URI   ${LI}
    Set to dictionary     ${liupdate_body}     sppUri    ${fw_uri_301}
    ${response}=    Fusion Api Li Upgrade Firmware    ${liupdate_body}    ${li_uri}
    Log to console    \n The response is:${response}
    Run Keyword If  ${response['status_code']} !=202    fail    msg=\nLI Firmware update Failed. \n ErrorCode:${response['errorCode']}\nMessage:${response['message']}
    ${task} =     Wait For Task        ${response}   60min    2min
    Run Keyword If  '${task['taskState']}' !='Completed'  or  ${task['status_code']} !=200   fail    msg=\nLI Firmware update Failed. \n ErrorCode:${task['taskErrors'][0][errorCode]}\n :Message ${task['taskErrors'][0][errorCode]}
    ...         ELSE    Log to console and logfile  \n\nLI FW Upgrade completed successfully by the Administrator user !!

OVTC556-Step4.Validate UTAH interconnect firmware version after downgrade is 3.01###
    :FOR    ${IC}    IN    @{INTERCONNECTS_UTAH}
    \   ${resp} =    Fusion Api Get Interconnect    param=?filter="'name' = '${IC}'"
    \   ${firmwareVersion} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion 
    \   Log to console and logfile    ${firmwareVersion}
    \   Run keyword If    ${firmwareVersion} != ${fc_firmwareVersion_301}   Fail    "Firmware version mismatch"
    \   ...    ELSE     Log to console and logfile    \nFirmware Version is validated as ${fc_firmwareVersion_301} for ${IC}

OVTC556-Step5.Creating the network user and logging in to do the upgrade ####
    ${user_name}=    Get From Dictionary   ${network_user}   userName
    ${pw}=      Get From Dictionary   ${network_user}   password
    ${credentials}=    Create Dictionary
    Set To Dictionary     ${credentials}   userName=${user_name}   password=${pw}
    ${resp} =   Fusion Api Add User     body=${network_user}
    Run Keyword If  ${resp['status_code']} !=200    fail    msg=${user_name} creation failed
    ...         ELSE    Log to console and logfile  \n ${user_name} created succesfully !!
    Fusion Api Login Appliance    ${APPLIANCE_IP_3_10}    ${credentials}

    Set to dictionary     ${liupdate_body}     sppUri    ${fw_uri_308}
    ${li_uri} =    Get LI URI   ${LI}
    ${response}=    Fusion Api Li Upgrade Firmware    ${liupdate_body}    ${li_uri}
    Log to console    \n The response is:${response}
    Run Keyword If  ${response['status_code']} !=202    fail    msg=\nLI Firmware update Failed. \n #ErrorCode:${response['errorCode']}\nMessage:${response['message']}
    ${task} =     Wait For Task        ${response}   60min    2min
    Run Keyword If  '${task['taskState']}' !='Completed'  or  ${task['status_code']} !=200   fail    msg=\nLI Firmware update Failed for network User. \n ErrorCode:${task['taskErrors'][0][errorCode]}\n :Message ${task['taskErrors'][0][errorCode]}
    ...         ELSE    Log to console and logfile  \n\nLI FW Upgrade completed successfully by the Network User !!

OVTC556-Step6. Validate UTAH interconnect firmware version is 3.08###
    :FOR    ${IC}    IN    @{INTERCONNECTS_UTAH}
    \   ${resp} =    Fusion Api Get Interconnect    param=?filter="'name' = '${IC}'"
    \   ${firmwareVersion} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion 
    \   Log to console and logfile    ${firmwareVersion}
    \   Run keyword If    ${firmwareVersion} != ${fc_firmwareVersion_latest}   Fail    "Firmware version mismatch"
	\   ...    ELSE     Log to console and logfile    \nFirmware Version is validated as ${fc_firmwareVersion_latest} for ${IC}

OVTC556-Step7. Creating other users and trying to do the update the FW ####
     Fusion Api Login Appliance    ${APPLIANCE_IP_3_10}    ${admin_credentials}
    :FOR   ${user}   IN   @{users}
    \    ${user_name}=    Get From Dictionary   ${user}   userName
    \    ${pw}=      Get From Dictionary   ${user}   password
    \    ${credentials}=    Create Dictionary
    \    Set To Dictionary     ${credentials}   userName=${user_name}   password=${pw}
    \    ${resp} =   Fusion Api Add User     body=${user}
    \    Run Keyword If  ${resp['status_code']} !=200    fail    msg=${user_name} creation failed
    \    ...         ELSE    Log to console and logfile  \n ${user_name} created succesfully !!
    \    Fusion Api Login Appliance    ${APPLIANCE_IP_3_10}    ${credentials}
    \    Log to console and logfile     \nDowngrading firmware through LI page
    \   ${li_uri} =    Get LI URI   ${LI}
    \   Set to dictionary     ${liupdate_body}     sppUri    ${fw_uri_301}
    \   ${response}=    Fusion Api Li Upgrade Firmware    ${liupdate_body}    ${li_uri}
    \    Log to console    \n The response is:${response}
    \    Validate Response      ${response}      ${valDict_user}
    \    Log to console and logfile    \n Verified that the FW update is not possible by the ${user_name}
	\    Fusion Api Login Appliance    ${APPLIANCE_IP_3_10}    ${admin_credentials}
	
#OVTC564 --OVF207_API_TC_verify Utah FW downgrade not allowed from 3.08 to prior to 3.01	
OVTC564-Step1.Validate UTAH interconnect firmware version is 3.08 ###
    :FOR    ${IC}    IN    @{INTERCONNECTS_UTAH}
    \   ${resp} =    Fusion Api Get Interconnect    param=?filter="'name' = '${IC}'"
    \   ${firmwareVersion} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion 
    \   Log to console and logfile    ${firmwareVersion}
    \   Run keyword If    ${firmwareVersion} != ${fc_firmwareVersion_latest}   Fail    "Firmware version mismatch"
	\   ...    ELSE     Log to console and logfile    \nFirmware Version is validated as ${fc_firmwareVersion_latest} for ${IC}

OVTC564-Step2.Uploading the bundle for the 3.00 version
    Remove Environment Variable     https_proxy    http_proxy
    Log to console and logfile    \nUploading spp bundle with version 3.00"
    ${resp} =     Fusion Api Upload Firmware Bundle      localfile=${CURDIR}/SPP/${SPP_bundle_300}
    Log to Console    Uploadsppdetails ${resp}
    Log to Console and logfile    \n ${SPP_bundle_300}SPP bundle is successfully uploaded

OVTC564-Step3.Downgrading to 3.00 version
    Log to console and logfile     \nDowngrading firmware through LI page
    ${li_uri} =    Get LI URI   ${LI}
    Set to dictionary     ${liupdate_body}     sppUri    ${fw_uri_300}
    ${response}=    Fusion Api Li Upgrade Firmware    ${liupdate_body}    ${li_uri}
    Log to console    \n The response is:${response}
    Run Keyword If  ${response['status_code']} !=202    fail    msg=\nLI Firmware update Failed. \n ErrorCode:${response['errorCode']}\nMessage:${response['message']}
    ${task} =     Wait For Task        ${response}   10min    30s
    ${ValDict}=      create Dictionary     taskStatus=Staging failed for the LI ${LI}
    ...                                    taskState=Warning
    Validate Response     ${task}   ${ValDict}
    Validate Response Regex    ${task['taskErrors'][0]}     ${ValDict_1}
    Log to console and logfile    \n Verified that direct downgrade from 3.08 to version less than 3.01 is not allowed
	
	
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