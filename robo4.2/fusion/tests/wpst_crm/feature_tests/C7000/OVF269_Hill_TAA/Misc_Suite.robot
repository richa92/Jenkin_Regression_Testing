*** Settings ***
#OVF269- Validating TAA Hill Module
Documentation     Verify MISC scenario in HILL module 
Library			Sdumpfunctions
Library			OperatingSystem
Library			FusionLibrary
Library			RoboGalaxyLibrary
Variables		data_variables.py
Resource        resource.txt
Resource		../../../resources/resource.txt

Suite Setup    Cleanup For Suite
Suite Teardown    Cleanup For Suite

***variables***
${LEuri} 	 /rest/logical-enclosures/
${file}		${CURDIR}/support_dump/ci_dfrm_supportdump.sdmp
${decyrpt_file}		${CURDIR}/support_dump/Decrypted/ci_dfrm_decrypted_supportdump.sdmp
${dump_file_path}		${CURDIR}/support_dump
${decryptor_path}		Decryptor
${content_path}    ${CURDIR}/support_dump/oneview/support-dump-temp/cidb.out
${content_path2}    ${CURDIR}/support_dump/oneview/support-dump-temp/cidb.out

*** Test Cases ***
###Pre-Conditions - Create LIG, EG, and import enclosure###
1 Create SessionID through API
	Set Log Level    TRACE
    ${Login_response} =    Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	Run keyword unless	${Login_response[0]['status_code']}== 200	Fail	"Unable to Login"
	Precheck for IC in OA
	Log to console and logfile    Test Step-1 completed successfully
	
2 Create LIG,EG and Import Enclosure
	${body} =   Build LIG body      ${lig_hill}
	${resp_lig} = 	Fusion Api Create LIG	${body}
	Run keyword unless	${resp_lig['status_code']}== 202	Fail	"Unable to Create LIG"
	${task} =	Wait For Task 	${resp_lig} 	120s	2s
	Log to console and logfile    LIG created successfully
	#${uri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri
	#Log to console and logfile    ${uri}

	${Enc_Grp_Resp} =    Add Enclosure Group from variable		${enc_group_hill}
	Log to console and logfile    ${Enc_Grp_Resp}
	Run keyword unless	${Enc_Grp_Resp['status_code']}== 201	Fail	"Unable to Create Enclosure Group"
	Log to console and logfile    \n\nEG created succesfully
	
	${Enc_Resp} =    Add Enclosures from variable     ${encs}
	Log to console and logfile    ${Enc_Resp}
	#Run keyword unless	${Enc_Resp['status_code']}== 202	Fail	"Unable to Create Ethernet network"
	Log to console and logfile    \n\nEnclosure imported succesfully
###Pre-Conditions steps over###

###Proceeding with MISC Suite ####
  
1 Downloading and validating encrypted support dump from LE page
	[Documentation] 	Create an encrypted support dump, decrypt it, extract and validate for the existence of files  
	
	Create Directory 	 ${dump_file_path}
	${LEResp}=    Fusion Api Get Resource			uri=${LEuri}
	logger		LE response : ${LEResp}		DEBUG
	Run Keyword If		'${LEResp['count']}' == '0'		Pass With Warnings		msg=Since LE is not available support dump is not created and test case is skipped 
	${LE_id} =	Get from dictionary		${LEResp['members'][0]}	uri
	${LE_id} =	Split String From Right		${LE_id}	/	1
	logger		Le id is : ${LE_id[-1]}		 
	${payload} = 	Build support dump payload		Mydump		${true}
	${resp}		Fusion Api Get Logical Enclosure Support Dump		${payload}		${LE_id[-1]}		
	Logger		LE support dump response : ${resp}		DEBUG
	${task_resp} =	Wait Until Keyword Succeeds		10 min	10 sec		Validate the response		${resp}		
	${uri}=     Get From Dictionary		${task_resp['associatedResource']}		resourceUri
	Logger		The downloadable dump file ${uri}
	Empty Directory 	${dump_file_path}
	${resp}=    Fusion Api Download Support Dump    uri=${uri}          localfile=${file}	
	decrypt_and_extract_the_dump_file		${dump_file_path}		${decryptor_path}
	validating_le_dump_files		${dump_file_path}	

2 Validate the LE dump files
	${resp} = 	Fusion Api Get Interconnect    param=?filter="'name' = '${interconnectname_1}'"
	Log to console and logfile    ${resp['members'][0]['uri']}
	Set Global Variable    ${IC_uri}    ${resp['members'][0]['uri']}
	${contents} =    OperatingSystem.Get File    ${content_path}
	${Lines}=    Get Lines Containing String    ${contents}    ${IC_uri}
	#Log to console and logfile    ${Lines}
	${Count}=    Get Line Count    ${Lines}
	Log to console and logfile    ${Count}
	Run Keyword If    ${Count} > 0  log to console    Hill module is present in support dump    Else    fail
	Log to console and logfile    Test Case-1 completed successfully		


3 Downloading and validating decrypted support dump from Appliance settings page
	[Documentation] 	Create an appliance support dump, decrypt it, extract and validate for the existence of files  
	
	${dump_file_path} = 	Catenate	SEPARATOR=/		${dump_file_path}		Decrypted
	${decryptor_path} =		Set Variable 			#Making the path as null since encryption not required
	logger		\n Location of Dump files : ${dump_file_path}		
	Create Directory 	 ${dump_file_path}
	Empty Directory 	${dump_file_path}
	${resp}    Fusion Api Create Support Dump    ${sdmp_body}
	Log to console and logfile    ${resp}		
	Logger		Appliance support dump response : ${resp}		DEBUG
	${uri}=     Get From Dictionary		${resp}		uri
	Logger		The downloadable dump file ${uri}
	Empty Directory 	${dump_file_path}
	${resp}=    Fusion Api Download Support Dump    uri=${uri}          localfile=${decyrpt_file}	
	decrypt_and_extract_the_dump_file		${dump_file_path}		${decryptor_path}	

4 Validate the appliance dump files
	${contents} =    OperatingSystem.Get File    ${content_path2}
	${Lines}=    Get Lines Containing String    ${contents}    ${IC_uri}
	#Log to console and logfile    ${Lines}
	${Count}=    Get Line Count    ${Lines}
	Log to console and logfile    ${Count}
	Run Keyword If    ${Count} > 0  log to console    Hill module is present in support dump    Else    fail
	Log to console and logfile    Test Case-2 completed successfully
	
5 Cleanup
	${encs} = 	Fusion Api Get Enclosures
	${resp}		fusion API Remove Enclosure		uri=${encs['members'][0]['uri']}
	${task} =	Wait For Task1 	${resp}
	
	${resp}=	fusion api delete enclosure group		name=${enc_group_hill['name']}
	Run keyword unless	${resp['status_code']}== 204	Fail	"Unable to delete the Enclosure Group"
	
	${resp}=	fusion api delete lig		name=${lig_hill['name']}
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete the LIG"

#Test Case-3 : Importing enclosure in a monitored mode and verifying the presence of Interconnect moduless	
3A Import enclosure in Monitored mode
	${resp} =	Fusion Api Add Enclosure	${encs_m}
	Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-Task is in progress\n 
	${task} =	Wait For Task1	${resp} 	30min	20s
	Log to console and logfile	Task is completed and Enclosure imported successfully!!
	
3B Verifying the module is present in Interconnect page
    ${resp} = 	Fusion Api Get Interconnect  		param=?filter="'name' = '${interconnectname_1}'"
	${model_1} =  Get From Dictionary  ${resp['members'][0]}		model
	Log to console and logfile    ${model_1}
	Run keyword If	'${model_1}' != '${Module_name}'		Fail	
	...			ELSE	Log to console	\n Interconnect Module name found
	
	
	 ${resp} = 	Fusion Api Get Interconnect  		param=?filter="'name' = '${interconnectname_2}'"
	Log to console	\nhi is:${resp['members'][0]}	
	${model_2} =  Get From Dictionary  ${resp['members'][0]}		model
	Log to console and logfile    ${model_2}
	
	Run keyword If	'${model_2}' != '${Module_name}'		Fail	
	...			ELSE	Log to console	\n Interconnect Module name found
	Log to console and logfile    Test Case-3 completed successfully

3C Cleanup
	${encs} = 	Fusion Api Get Enclosures
	${resp}		fusion API Remove Enclosure		uri=${encs['members'][0]['uri']}
	${task} =	Wait For Task1 	${resp}