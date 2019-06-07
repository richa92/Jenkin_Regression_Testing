*** Settings ***
Documentation		Verify Config scenario in HILL module
Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary
Library			OperatingSystem
Library			String
Library			ServerOperations
Variables		data_variables.py
Resource        resource.txt

Suite Setup    Cleanup For Suite
Suite Teardown    Cleanup For Suite

*** Test Cases ***
###Pre-Conditions - Create LIG, EG, and import enclosure###
1.Create SessionID through API
	Set Log Level    TRACE
    ${Login_response} =    Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	Run keyword unless	${Login_response[0]['status_code']}== 200	Fail	"Unable to Login"
	Precheck for IC in OA
	Log to console and logfile    Test Step-1 completed successfully

2.Create Networks, LIG, EG and import enclosure through API
	${Response_enet}     fusion api create ethernet network		${enet_hill}
	Run keyword unless	${Response_enet['status_code']}== 202	Fail	"Unable to Create Ethernet network"
	:For	${FC}	IN	@{fcNet_hill}
	\	${resp} =	Fusion Api Create Fc Network		${FC}
	\	Run Keyword If  '${resp['status_code']}' != '202'	Fail    
	\	...			ELSE	Log to console	\n"FC Network : ${FC['name']} created successfully"
	Log to console and logfile    Networks created successfully
	
	${body} =   Build LIG body      ${lig_hill_config}
	${resp_lig} = 	Fusion Api Create LIG	${body}
	Run keyword unless	${resp_lig['status_code']}== 202	Fail	"Unable to Create LIG"
	${task} =	Wait For Task 	${resp_lig} 	120s	2s
	Log to console and logfile    LIG created successfully
	${uri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri
	Set Global Variable    ${lig_uri}    ${uri}
		
	${resp_eg} =    Add Enclosure Group from variable		${enc_group_hill}
	Run keyword unless	${resp_eg['status_code']}== 201	Fail	"Unable to Create EG"
	Log to console and logfile    EG created succesfully
	${resp_import} =    Add Enclosures from variable     ${encs}
	Run keyword unless	${resp_import['status_code']}== 202	Fail	"Unable to import enclosure"
	Log to console and logfile    Enclosure imported succesfully
	
###Pre-Conditions steps over###

###Proceeding with Config-3 ####
3A.Restart the OV appliance
	${del_resp} =    Fusion Api Delete Alert
	Run keyword unless	${del_resp['status_code']}== 202	Fail	"Unable to Delete Alerts"
	${resp} =	Fusion Api Appliance Shutdown	${restart_mode}
	Run Keyword If  '${resp['status_code']}' != '202'  Fail    ELSE  log to console   \n-Task is in progress\n
	Wait For Restarting OV Appliance
	Log to console and logfile    Test Step-3A completed successfully
	
3B.Login to appliance after restart
	${Login_response} =    Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	Run keyword unless	${Login_response[0]['status_code']}== 200	Fail	"Unable to Login"
	Log to console and logfile    Test Step-3B completed successfully
	
3C.Navigate to li and verify the uplinks
	${resp} =	Fusion Api Get Uplink Set		param=?filter="'name' == '${uplink_sets['us_fc1']['name']}'"
	Run Keyword If  '${resp['count']}' != '1'  Fail    ELSE  log to console   \n-Uplink set verified succesfully\n
	${resp} =	Fusion Api Get Uplink Set		param=?filter="'name' == '${uplink_sets['us_fc2']['name']}'"
	Run Keyword If  '${resp['count']}' != '1'  Fail    ELSE  log to console   \n-Uplink set verified succesfully\n
	${resp} =	Fusion Api Get Uplink Set		param=?filter="'name' == '${uplink_sets['us_fc3']['name']}'"
	Run Keyword If  '${resp['count']}' != '1'  Fail    ELSE  log to console   \n-Uplink set verified succesfully\n
	${resp} =	Fusion Api Get Uplink Set		param=?filter="'name' == '${uplink_sets['us_fc4']['name']}'"
	Run Keyword If  '${resp['count']}' != '1'  Fail    ELSE  log to console   \n-Uplink set verified succesfully\n
	Log to console and logfile    Test Step-3C completed successfully
	
3D.Verifying the interconnects are in configured state
	Validate IC State    ${IC_Configured}
	Log to console and logfile    Test Case Config-3 completed successfully
	
###Proceeding with Config-1 ####
Step1-Power off all the servers
	Power off ALL servers
	Log to console and logfile    Proceeding with Config-1 Test Case
	
Step2-Profile Creation with user defined range and power on the server
	${SP_resp}=    Add Server Profiles from variable   ${server_profiles_edit1}
	Run keyword unless	${SP_resp['status_code']}== 202	Fail	"Unable to Create Server Profile"
	Log to console and logfile    ${server_profiles_edit1[0]['serverHardwareUri']}
	${resp_Power}=    Power on server    ${server_profiles_edit1[0]['serverHardwareUri']}
	Run keyword unless	${resp_Power['status_code']}== 202	Fail	"Unable to power on server"
	Sleep    ${Poweron_Server_Sleeptime}
	Log to console and logfile    Test Step-2 completed successfully

Step3-Getting the mac, wwn, sn, uuid from server and validating	
	${resp}=    get_server_mac_wwn_uuid    ${linux_details}    ${oa_details}    ${module_file_path}    ${windows_server_cred} 
	Log to console and logfile    ${resp}
	Dictionary Should Contain Value    ${resp}    ${Serial_number_UD}
	Dictionary Should Contain Value    ${resp}    ${UUID_UD}
	Log to console and logfile    ${resp['mac']}
	List Should Contain Value    ${resp['mac']}    ${MAC_address_UD}
	Log to console and logfile    ${resp['wwn']}
	List Should Contain Value    ${resp['wwn']}    ${WWPN_UD}
	Log to console and logfile    Test Step-3 completed successfully
	
Step4-Power off the server and delete profile
	${resp_Power}=    Power off server    ${server_profiles_edit1[0]['serverHardwareUri']}
	Run keyword unless	${resp_Power['status_code']}== 202	Fail	"Unable to power off server"
	${resp}=	fusion api delete server profile	${server_profiles_edit1[0]['name']}
	${task} =	Wait For Task 	${resp} 	120s	10s
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete Server profile"
	Log to console and logfile    Test Step-4 completed successfully
	
Step5-Editing the V-pools range
	Disable The Auto Generated Mac,Wwn,Sn Ranges
	${resp_mac} =    Fusion Api Create Vmac Range    ${Vmac_body} 
	Log to console and logfile    ${resp_mac}
	Run keyword unless	${resp_mac['status_code']}== 200	Fail	"Unable to edit Vmac range"
	${resp_wwn} =    Fusion Api Create Vwwn Range    ${Vwwn_body} 
	Log to console and logfile    ${resp_wwn}
	Run keyword unless	${resp_wwn['status_code']}== 200	Fail	"Unable to edit Vwwn range"
	${resp_sn} =     Fusion Api Create Vsn Range    ${Vsn_body} 
	Log to console and logfile    ${resp_sn}
	Run keyword unless	${resp_sn['status_code']}== 200    Fail    "Unable to edit Vsn range"
	Log to console and logfile    Test Step-5 completed successfully
	
Step6-Profile Creation with Virtual range and power on the server
	${SP_resp}=    Add Server Profiles from variable   ${server_profiles_edit2}
	Run keyword unless	${SP_resp['status_code']}== 202	Fail	"Unable to Create Server Profile"
	Log to console and logfile    ${server_profiles_edit2[0]['serverHardwareUri']}
	${resp_Power}=    Power on server    ${server_profiles_edit2[0]['serverHardwareUri']}
	Run keyword unless	${resp_Power['status_code']}== 202	Fail	"Unable to power on server"
	Sleep    ${Poweron_Server_Sleeptime}
	Log to console and logfile    Test Step-6 completed successfully

Step7-Getting the mac, wwn, sn from server and validating	
	${resp}=    get_server_mac_wwn_uuid    ${linux_details}    ${oa_details}    ${module_file_path}    ${windows_server_cred} 
	Log to console and logfile    ${resp}
	Dictionary Should Contain Value    ${resp}    ${startAddress_sn}
	Log to console and logfile    ${resp['mac']}
	List Should Contain Value    ${resp['mac']}    ${startAddress_mac}
	Log to console and logfile    ${resp['wwn']}
	List Should Contain Value    ${resp['wwn']}    ${startAddress_check}
	Log to console and logfile    Test Step-7 completed successfully
	
Step8-Power off the server and delete profile
	${resp_Power}=    Power off server    ${server_profiles_edit2[0]['serverHardwareUri']}
	Run keyword unless	${resp_Power['status_code']}== 202	Fail	"Unable to power off server"
	${resp}=	fusion api delete server profile	${server_profiles_edit2[0]['name']}
	${task} =	Wait For Task 	${resp} 	120s	10s
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete Server profile"
	Log to console and logfile    Test Step-8 completed successfully
	
Step9-Profile Creation with Physical range and power on the server
	${SP_resp}=    Add Server Profiles from variable   ${server_profiles_edit3}
	Run keyword unless	${SP_resp['status_code']}== 202	Fail	"Unable to Create Server Profile"
	Log to console and logfile    ${server_profiles_edit3[0]['serverHardwareUri']}
	${resp_Power}=    Power on server    ${server_profiles_edit3[0]['serverHardwareUri']}
	Run keyword unless	${resp_Power['status_code']}== 202	Fail	"Unable to power on server"
	Sleep    ${Poweron_Server_Sleeptime}
	Log to console and logfile    Test Step-9 completed successfully

Step10-Getting the mac, wwn, sn from server and validating	
	${resp}=    get_server_mac_wwn_uuid    ${linux_details}    ${oa_details}    ${module_file_path}    ${windows_server_cred} 
	Log to console and logfile    ${resp}
	Dictionary Should Not Contain Value    ${resp}    ${startAddress_sn}
	Log to console and logfile    ${resp['mac']}
	List Should Not Contain Value    ${resp['mac']}    ${startAddress_mac}
	Log to console and logfile    ${resp['wwn']}
	List Should Not Contain Value    ${resp['wwn']}    ${startAddress_check}
	Log to console and logfile    Test Step-10 completed successfully
	
Step11-Power off the server and delete profile
	${resp_Power}=    Power off server    ${server_profiles_edit3[0]['serverHardwareUri']}
	Run keyword unless	${resp_Power['status_code']}== 202	Fail	"Unable to power off server"
	${resp}=	fusion api delete server profile	${server_profiles_edit3[0]['name']}
	${task} =	Wait For Task 	${resp} 	120s	10s
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete Server profile"
	Log to console and logfile    Test Case Config-1 completed successfully
	
###Proceeding with Config-7 ####	
7A. Edit LIG and LI and then Clear Alert Message
	${body_new} =   Build LIG body      ${lig_hill}    
	${resp_lig} = 	Fusion Api Edit Lig    ${body_new}    ${lig_uri}
	Run keyword unless	${resp_lig['status_code']}== 202	Fail	"Unable to Edit LIG"
	${task} =	Wait For Task 	${resp_lig} 	120s	2s
	Log to console and logfile    LIG edited successfully
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	Perform an LI Update From Group    ${li_uri}
	${del_resp} =    Fusion Api Delete Alert
	Log to console and logfile    \n\n${del_resp}
	
7B. Validating the Interconnect State
	${resp} =	Get IC State
	#Log to console and logfile    \n\n${resp}
	${len} = 	Get Length	${resp}
	:FOR	${x}	IN RANGE	0	${len}
	\	Run Keyword If    '${resp[${x}]}' == 'Configured'    Log to console    \nThe state of IC(HILL Module) is Configured    ELSE    Log to console    \n\nThe state of IC(HILL Module) is not Configured
	
7C. Create UplinkSet 
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	${us} = 		Copy Dictionary	${uplink_sets['us_eth']}
	${body} = 		Build US body 	${us}	${li_uri}
	${resp} = 		Fusion Api Create Uplink Set	body=${body}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
		
	${us} = 		Copy Dictionary	${uplink_sets['us_fc']}
	${body} = 		Build US body 	${us}	${li_uri}
	${resp} = 		Fusion Api Create Uplink Set	body=${body}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	
7D. Check for Alert Message in OV
	${resp} = 	Fusion Api Get Li
	#Log to console and logfile	${resp}
	${li_state} =	Get From Dictionary		${resp['members'][0]}	consistencyStatus  
	Log to console and logfile		${li_state}
	Run Keyword If    '${li_state}' == '${Expected_Consistency_Status}'    Log to console    \n\nThe LI is ${li_state} with LIG    ELSE    Log to console    \n\nThe LI is not ${li_state} with LIG

7E. Change the uplink port being used by the uplink set  	
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	${us} = 		Copy Dictionary	${uplink_sets_edit['us_fc']}
	${body} = 		Build US body 	${us}	${li_uri}
	${resp} =    Fusion Api Get Uplink Set    param=?filter="'name'=='${US_Check}'"
	${uri} =    Get From Dictionary		${resp['members'][0]}	uri
    ${resp} = 		Fusion Api Edit Uplink Set	body=${body}	uri=${uri}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	
7F. Check for Alert Message in OV after editing Uplinkset
	${resp} =    Fusion Api Get Alerts
	${mem_resp} =	Get From Dictionary		${resp}		members
	${len} = 	Get Length	${mem_resp}
	${Alert_msg} =	Create List
	:FOR	${x}	IN RANGE	0	${len}
	\	${desc_alert} =		Get From Dictionary		${mem_resp[${x}]}		description
	\	Run Keyword If    '${desc_alert}' != '${Alert_Message_Delete_Port}'	Continue For Loop	
	\	Append To List    ${Alert_msg}    ${desc_alert}
	${len} = 	Get Length    ${Alert_msg}
	Run Keyword If      ${len} != 0      Log to console and logfile   \n${Alert_Message_Delete_Port} is observed
    ...         ELSE    Log to console and logfile   \nNo Critical Alert Message Observed

7G. Deleting UplinkSet
	${resp} =	Fusion Api Delete Uplink Set	${uplink_sets['us_eth']['name']}
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to Delete UplinkSet"
	Log to console and logfile  \n\nUplinkSet deleted succesfully !!
	${resp} =	Fusion Api Delete Uplink Set	${uplink_sets['us_fc']['name']}
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to Delete UplinkSet"
	Log to console and logfile  \n\nUplinkSet deleted succesfully !!

7H. Validating the Presence of deleted Uplinkset
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets['us_eth']['name']}'"
	Run keyword unless	${Response['count']}== 0	Fail	"Unable to verify the newly created uplink set is  absent in the appliance"
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${US_Check}'"
	Run keyword unless	${Response['count']}== 0	Fail	"Unable to verify the presence of uplink set in OV"
	Log to console and logfile    Test Case Config-7 completed successfully
	
###Proceeding with cleanup###
TEARDOWN
	${encs} = 	Fusion Api Get Enclosures
	${resp}		fusion API Remove Enclosure		uri=${encs['members'][0]['uri']}
	${task} =	Wait For Task1 	${resp}	
	${resp}=	fusion api delete enclosure group		name=${enc_group_hill['name']}
	Run keyword unless	${resp['status_code']}== 204	Fail	"Unable to delete the Enclosure Group"
	
	${resp}=	fusion api delete lig		name=${lig_hill['name']}
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete the LIG"
	
	${Response}     fusion api delete ethernet network		${enet_hill['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to delete FC network"
	
	${Response}     fusion api delete fc network		${fcNet_hill[0]['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	
	${Response}     fusion api delete fc network		${fcNet_hill[1]['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	
	${Response}     fusion api delete fc network		${fcNet_hill[2]['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	
	${Response}     fusion api delete fc network		${fcNet_hill[3]['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	Log to console and logfile    Test Suite CONFIG for hill module completed successfully