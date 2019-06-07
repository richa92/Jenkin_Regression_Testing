*** Settings ***

Documentation        Feature Test: OVF207: C7000: Minimum Supported Version of Utah FW 3.01
...                  OVTC570-OVF207_API_TC_Verify importing the enclosure with Utah FW version prior to 3.01
...					 OVTC571--OVF207_API_TC_Verify the firmware upgrade from version prior to 3.01 to 3.08

Library                   FusionLibrary
Library                   RoboGalaxyLibrary
Library                   Collections
Library                   OperatingSystem
Library                   Process
Variables                 data_variables.py	

Resource            ../../../../resource/fusion_api_all_resource_files.txt

#Trigger the pres-setup suite before executing this

*** Test Cases ***
OVTC570.Step-1.Login to Appliance and initial clean up
    Set Log Level    TRACE
    Set Global Variable    ${APPLIANCE_IP}    ${APPLIANCE_IP_3_10}
    ${Login_response} =   Fusion Api Login Appliance    ${APPLIANCE_IP_3_10}        ${admin_credentials}
    Run keyword unless	${Login_response[0]['status_code']}== 200	Fail	"Unable to Login"
    Log to console and logfile    Test Step-1 completed successfully
    Power OFF ALL Servers
    Remove ALL Server Profiles
    Remove ALL Enclosures
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Remove ALL Ethernet Networks
    Remove ALL FC Networks
    Remove ALL Users
    
OVTC570.Step-2.Uploading the 1.11 fw bundle.
    Remove Environment Variable     https_proxy    http_proxy
    Log to console and logfile    \nUploading spp bundle with version 1.11"
    ${resp} =     Fusion Api Upload Firmware Bundle      localfile=${CURDIR}/SPP/${SPP_bundle_111}
    Log to Console    Uploadsppdetails ${resp}
    Log to Console and logfile    \n ${SPP_bundle_111}SPP bundle is successfully uploaded

OVTC570.Step-3.Create LIG, EG and import enclosure with Utah FW version as 1.11
    ${fc_networks} =    Get Variable Value    ${fcNet_utah}
    Run Keyword If   ${fc_networks} is not ${null}    Add FC Networks from variable    ${fc_networks}
    ${body} =   Build LIG body      ${lig_utah_111_310}
    ${resp_lig} =    Fusion Api Create LIG    ${body}
    ${task} =    Wait For Task    ${resp_lig}    120s    2s
    Log to console and logfile    LIG created successfully

    ${enc_groups} =  Get Variable Value   ${enc_group_utah_111_310}
    Run Keyword If   ${enc_groups} is not ${null}   Add Enclosure Group from variable    ${enc_groups}
    Log to console and logfile    EG created succesfully
    ${EG_uri}=    Get Enclosure Group URI    ${EG1}
    Set To Dictionary    ${encs_fwupdate}    enclosureGroupUri    ${EG_uri}
    ${resp_enc}=    Fusion Api Add Enclosure    ${encs_fwupdate}
    Run keyword unless    ${resp_enc['status_code']}== 202    Fail    ${resp_enc['message']}
    ${task} =   Wait For Task    ${resp_enc}    100min   1min
    Log to console and logfile  \n\nImported the enc Successfully !!

OVTC570.Step-4.Validate interconnect firmware version
    :FOR    ${IC}    IN    @{INTERCONNECTS_UTAH}
    \   ${resp} =    Fusion Api Get Interconnect    param=?filter="'name' = '${IC}'"
    \   ${firmwareVersion} =  Get From Dictionary  ${resp['members'][0]}    firmwareVersion
    \   ${state}=     Get From Dictionary     ${resp['members'][0]}   state 
    \   Run keyword If    '${firmwareVersion}' != '${fc_firmwareVersion_old}'    Fail    msg="Firmware version mismatch"
    \   ...    ELSE     Log to console and logfile    \nFirmware Version is validated as ${fc_firmwareVersion_old} for ${IC}
    \   Run Keyword If    '${state}' != 'Unmanaged'    fail      msg="The IC module ${IC} is not showing unmanaged state" 
    \    ...     ELSE   Log to console and logfile    \n The IC module ${IC} is in unmanaged state

#OVTC571--OVF207_API_TC_Verify the firmware upgrade from version prior to 3.01 to 3.08	
OVTC571.Step-1.Uploading the 3.08 fw bundle.
    Remove Environment Variable     https_proxy    http_proxy
    Log to console and logfile    \nUploading spp bundle with version 3.08"
    ${resp} =     Fusion Api Upload Firmware Bundle      localfile=${CURDIR}/SPP/${SPP_bundle_308}
    Log to Console    Uploadsppdetails ${resp}
    Log to Console and logfile    \n ${SPP_bundle_308}SPP bundle is successfully uploaded
    
OVTC571.Step-2.Direct Upgrading the firmware through LI page to 3.08 
    Log to console and logfile     \nDowngrading firmware through LI page
    ${li_uri} =    Get LI URI   ${LI}
    Set to dictionary     ${liupdate_body}     sppUri    ${fw_uri_308}
    ${response}=    Fusion Api Li Upgrade Firmware    ${liupdate_body}    ${li_uri}
    Log to console    \n The response is:${response}
    Run Keyword If  ${response['status_code']} !=202    fail    msg=\nLI Firmware update Failed. \n ErrorCode:${response['errorCode']}\nMessage:${response['message']}
    ${task} =     Wait For Task        ${response}   60min    30s
    ${message}=      Get From Dictionary   ${task['taskErrors'][0]}    message
    ${msg1}=    Split String From Right    ${message}     ,
    ${pw}=   Remove String Using Regexp    ${msg1[-1].strip()}    '${SPACE}
    Run Keyword If   '${pw}' != '${ValDict_msg}'    Fail     msg="The expected error msg is not displayed"
    Validate Response   ${task['taskErrors'][0]}     ${ValDict_Action}
    Log to console and logfile   \nThe expected error messages are correctly displayed for attempting the direct upgrade from 1.11 to 3.08

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
	