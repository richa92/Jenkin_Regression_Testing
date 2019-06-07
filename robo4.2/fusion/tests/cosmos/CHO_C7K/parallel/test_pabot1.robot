*** Settings ***
Library                         pabot.PabotLib
Resource                        cho_resource_new.txt
Suite Setup                     Login And Load Test Data	Administrator
Suite Teardown                  Logout Appliance
 
*** Test Cases ***
Status Poll
	[Documentation]         Exit Test Case if any failure
	${server_hardware}=		Get From Dictionary		${server_profile_E1bay3}		serverHardwareUri
	${hardwareStatus}=	Get Server Hardware State	${server_hardware}
	${profileName}=		Get From Dictionary		${server_profile_E1bay3}		name
	${profileUri}=	Get Server Profile URI	${profileName}
	Run Keyword If	'${profileUri}'!='/rest/server_profile_uri_${profileName}_not_found' or '${hardwareStatus}'=='Critical'		Fail	Status Poll Failed
 
Create Server Profile
	[Tags]    SETUP 		SP
	[Documentation]		Create Server Profile on C7K Server 
	Set Log Level	TRACE
	Power Off Server if On		${server_profile_E1bay3}             	
	${profileStatus}	${response}=  Run Keyword And Ignore Error		Add Server Profile  ${server_profile_E1bay3}        
	${taskStatus}=		Run Keyword And Return Status	Wait For Task2	${response}   timeout=1200    interval=30
	Run Keyword If		'${taskStatus}'=='False'  	Fail  Create server Profile E1bay3 failed 
	${verifyStatus}=	Run Keyword And Return Status	Verify Resource  ${expected_server_profile_E1bay3}
	Run Keyword If		'${verifyStatus}'=='False'  Fail  Verify server profile on E1bay3 failed

Add Server to Altair using ILO
	[Documentation]	Add Servers to Altair using ILO
	${Servers} =    Get Data By Property		${TestData.Servers}		ServerNo		1    	
	${status}	${jobUri}=	Altair API Add Server    ${Servers[0].ilousername}    ${Servers[0].ilopassword}    ${Servers[0].iloip} 	
	${jobStatus}	${jobState}=	Wait For Task And Verify	${jobUri}	1200
	Run Keyword If	'${jobStatus}'!='ok' and '${jobState}'!='STATUS_SUCCESS'	Fail	Failed to Add Server to Altair using ILO. ILO IP - ${Servers[0].iloip}
	Fail  Failed to Add Server to Altair using ILO. ILO IP - ${Servers[0].iloip}

Install OS
	[Documentation]	Install OSBP
	Set Log Level	TRACE
	${Servers} =    Get Data By Property		${TestData.Servers}		ServerNo		1
	${Server_URI}=	Altair API Get Server Uri Using Location	${Servers[0].enclosure}    ${Servers[0].bay}
	${OSBP_URI}=	Altair API Get Os Buildplan Uri    ${Servers[0].OSBP}
	${status}	${jobUri}=    Altair API Run Os Buildplan    ${Server_URI}    ${OSBP_URI}
	${jobState}=	Altair API Wait For Task	${jobUri}	1200
	Pass Execution If		${jobState['status']}=='ok' and ${jobState['state']}=='STATUS_SUCCESS'		OSBP completed successfully
	Fail	Failed to complete OSBP

# Ping Server Open SSH Connection And Verify Disk
# 	[Documentation]	Ping the server, open the SSH connection and check number of disks present
# 	${Servers} =    Get Data By Property		${TestData.Servers}		ServerNo		1
# 	${ipv4addr}=	Get Server Management IP using Serial Number	${server_profile_E1bay2}	${Servers[0].enclosure}		${Servers[0].bay}
#  		
# 	${RC}	${output} =	Run and return RC and Output	ping -n 4 ${ipv4addr}
# 	${gotTask}     ${response} =  Run Keyword and Ignore Error 	Should be equal		${RC}	${0}	\n${output}
# 	#Run keyword if		'${gotTask}'=='FAIL'	Pause Execution    message=Failed to Ping the Server with IP - ${ipv4addr} . Press OK to continue
# 	Run keyword if		'${gotTask}'=='FAIL'	Fail		Server with IP- ${ipv4addr} is unreachable . Output is ${response}
# 	...					ELSE					Log To Console	Server with IP- ${ipv4addr} is pingable
#  	
# 	${status}	${resp}=	Run Keyword And Ignore Error	Open Connection    ${ipv4addr}
# 	#Run Keyword If	'${status}'=='FAIL'		Pause Execution    message=Failed to Open SSH Connection for server in Enclosure ${Servers[0].enclosure} and bay ${Servers[0].bay}. Press OK to continue
# 	Run Keyword If	'${status}'=='FAIL'		Fail	Failed to Open SSH Connection for server in Enclosure ${Servers[0].enclosure} and bay ${Servers[0].bay}
#  	
#     ${newstatus}	${resp}=	Run Keyword And Ignore Error	Login    ${USERNAME}    ${PASSWORD}
#     #Run Keyword If	'${newstatus}'=='FAIL'		Pause Execution    message=Failed to do SSH Login for server in Enclosure ${Servers[0].enclosure} and bay ${Servers[0].bay}. Press OK to continue
# 	Run Keyword If	'${newstatus}'=='FAIL'		Fail	Failed to do SSH Login for server in Enclosure ${Servers[0].enclosure} and bay ${Servers[0].bay}
#      
#     ${stdout}=	Execute Command     fdisk -l | grep /dev/sd
#     ${stdout2}=	Execute Command     df -h | grep /dev/sd
#     Log to console and logfile		\n${stdout}
#     Log to console and logfile		\n${stdout2}
#     ${gotTask}     ${taskState} =  Run Keyword and Ignore Error  Should Contain  ${stdout}  /dev/sd
#     Run Keyword If   '${gotTask}'== 'FAIL'  Fail  Failed to get /dev/sd in output
#     Close All Connections 
#  
# 	Pause Execution   		message=Check Disk Before Edit Profile
 
Edit Server Profile
	[Tags]    SETUP 		SP
	[Documentation]		Edit Server Profile
	Set Log Level	TRACE
	Power Off Server if On		${server_profile_E1bay3}	${False}   	
	${profileStatus}	${response}=  Run Keyword And Ignore Error		Edit Server Profile  ${edit_server_profile_E1bay3}     	
	${taskStatus}=		Run Keyword And Return Status	Wait For Task2	${response}   timeout=1200    interval=30
	Run Keyword If		'${taskStatus}'=='False'  	Fail  Edit server Profile E1bay3 failed 
	${verifyStatus}=	Run Keyword And Return Status	Verify Resource  ${expected_edit_server_profile_E1bay3}
	Run Keyword If		'${verifyStatus}'=='False'  Fail  Edit server profile verification on E1bay3 failed
#  
# Power On And Boot
# 	[Documentation]		Power On Server And wait for it to complete boot 
#     Set Log Level	TRACE
#     ${server_hardware}=		Get From Dictionary		${server_profile_E1bay2}		serverHardwareUri 
#     ${server_hardware}=		replace string using regexp  ${server_hardware}  SH:  ${EMPTY}
#       
#     ${server_powerstate}=	Get Server Power	${server_hardware}
#     Pass Execution If	'${server_powerstate}'=='On'		Server is Powered On	
#           
#     ${powerStatus}=		Run Keyword And Return Status	Power on Server	${server_hardware}
#     #Run Keyword If		'${powerStatus}'=='False'	Pause Execution    message=Failed to power on the server - ${server_hardware}. Press OK to continue
# 	Run Keyword If		'${powerStatus}'=='False'	Fail 	Failed to power on the server- ${server_hardware}
#   	
# 	Wait for Server to reach POST State		${server_hardware}
 
 
# Ping And Open SSH Connection
# 	[Documentation]		Open SSH Connection for the given Server/VM using IP and credentials
# 	${Servers} =    Get Data By Property		${TestData.Servers}		ServerNo		2
# 	${ipv4addr}=	Get Server Management IP using Serial Number	${server_profile_E1bay2}	${Servers[0].enclosure}		${Servers[0].bay}
#  		
# 	${index} =    Set Variable    ${0}
# 	${Range} =    Set Variable    ${30}
# 	:FOR	${index}	IN RANGE	${Range}
# 	\	${RC}	${output} =	Run and return RC and Output	ping -n 4 ${ipv4addr}
# 	\	${gotTask}     ${response} =  Run Keyword and Ignore Error 	Should be equal		${RC}	${0}	\n${output}
# 	\	Exit For Loop If		'${gotTask}'=='PASS'	
# 	\	${index}= 	Set Variable	${index+1}
# 	\	Sleep    20
# 	#Run keyword if		'${gotTask}'=='FAIL'	Pause Execution    message=Failed to Ping the Server with IP - ${ipv4addr} . Press OK to continue
# 	Run keyword if		'${gotTask}'=='FAIL'	Fail		Server with IP- ${ipv4addr} is unreachable . Output is ${response}
# 	...					ELSE					Log To Console	Server with IP- ${ipv4addr} is pingable
# 	Sleep    120
#      
#     ${status}	${resp}=	Run Keyword And Ignore Error	Open Connection    ${ipv4addr}
# 	#Run Keyword If	'${status}'=='FAIL'		Pause Execution    message=Failed to Open SSH Connection for server in Enclosure ${Servers[0].enclosure} and bay ${Servers[0].bay}. Press OK to continue
# 	Run Keyword If	'${status}'=='FAIL'		Fail	Failed to Open SSH Connection for server in Enclosure ${Servers[0].enclosure} and bay ${Servers[0].bay}
#  	
#     ${newstatus}	${resp}=	Run Keyword And Ignore Error	Login    ${USERNAME}    ${PASSWORD}
#     #Run Keyword If	'${newstatus}'=='FAIL'		Pause Execution    message=Failed to do SSH Login for server in Enclosure ${Servers[0].enclosure} and bay ${Servers[0].bay}. Press OK to continue
# 	Run Keyword If	'${newstatus}'=='FAIL'		Fail	Failed to do SSH Login for server in Enclosure ${Servers[0].enclosure} and bay ${Servers[0].bay}
#      
#     ${stdout}=	Execute Command     fdisk -l
#     ${stdout2}=	Execute Command     df -h | grep /dev/sd
#     Log to console and logfile	 ${stdout}
#     Log to console and logfile	 ${stdout2}
#     ${gotTask}     ${taskState} =  Run Keyword and Ignore Error  Should Contain  ${stdout}  /dev/sd
#     Run Keyword If   '${gotTask}'== 'FAIL'  Fail  Failed to get /dev/sd in output
# 	Close All Connections
#  
# 	Pause Execution   		message=Check Disk After Edit Profile

Move Server Profiles
	[Tags]    SETUP 		SP
	[Documentation]		Move Server Profile
	:FOR	${move_server_profiles}	in	@{move_server_profiles}
	\	Set Log Level	TRACE
	\	Power Off Server if On		${move_server_profiles}	${False}
	\	${profileStatus}	${response}=  Run Keyword And Ignore Error		Edit Server Profile  ${move_server_profiles}
	\	#Run Keyword If		'${profileStatus}'=='FAIL'		Pause Execution    message=Editing Server Profile E1bay2 failed. Press OK to continue
	\	${taskStatus}=		Run Keyword And Return Status	Wait For Task2	${response}   timeout=1200    interval=30
	\	#Run Keyword If		'${taskStatus}'=='False'		Pause Execution    message=Waiting for Task for move_server_profiles Failed. Press OK to continue
	\	Run Keyword If		'${taskStatus}'=='False'  	Fail  Switch between one Server HW to Other failed

# Erase Disk
# 	[Documentation]	Erase Hard Disk using Altair OSBP
# 	${Servers} =    Get Data By Property		${TestData.Servers}		ServerNo		2
# 	${jobStatus}	${jobState}=	Run OSBP	${server_profile_E1bay2}	${Servers[0].EraseOSBP}		${Servers[0].enclosure}		${Servers[0].bay}
# 	Pass Execution If		'${jobStatus}'=='ok' and '${jobState}'=='STATUS_SUCCESS'		Successfully Erased Disk on server in Enclosure - ${Servers[0].enclosure} and bay - ${Servers[0].bay}
# 	#Pause Execution   		message=Failed to Erase Disk on server in Enclosure - ${Servers[0].enclosure} and bay - ${Servers[0].bay} . Press OK to Continue
# 	Fail	Failed to Erase Disk on server in Enclosure - ${Servers[0].enclosure} and bay - ${Servers[0].bay}
 
 
Delete Altair Server
	[Documentation]	Deleting Server from Altair
	Set Log Level	TRACE
	${Servers} =    Get Data By Property		${TestData.Servers}		ServerNo		1
	${response}=	Delete Server From Altair	${server_profile_E1bay3}	${Servers[0].enclosure}		${Servers[0].bay}
	${keywordStatus}	${jobStatus}=		Run Keyword And Ignore Error	Get From Dictionary		${response}		status
	Run Keyword If 		'${keywordStatus}'=='PASS' and '${jobStatus}' in ['200','201','202','203','204']		Pass Execution		message=Successfully Deleted the Server in Enclosure - ${Servers[0].enclosure} and bay - ${Servers[0].bay} from Altair
	#Pause Execution   	message=Failed to Delete the server from Altair in Enclosure - ${Servers[0].enclosure} and bay - ${Servers[0].bay}. Press OK to Continue
	Fail	Failed to Delete the server from Altair in Enclosure - ${Servers[0].enclosure} and bay - ${Servers[0].bay}
   
   
Remove Server Profile
	[Tags]    SETUP 		SP
	[Documentation]		Remove Server Profile From C7K Server
	Set Log Level	TRACE
	Power Off Server if On		${server_profile_E1bay3}	${False} 
	${profileStatus}	${response}=  Run Keyword And Ignore Error		Remove Server Profile  ${edit_server_profile_E1bay3}
	#Run Keyword If		'${profileStatus}'=='FAIL'		Pause Execution    message=Removing Server Profile E1bay2 failed. Press OK to continue
	${taskStatus}=		Run Keyword And Return Status	Wait For Task2	${response}   timeout=1200    interval=30
	#Run Keyword If		'${taskStatus}'=='False'		Pause Execution    message=Waiting for Task for Remove Server Profile on E1bay2 Failed. Press OK to continue
	Run Keyword If		'${taskStatus}'=='False'  Fail  Remove server Profile E1bay3 failed 