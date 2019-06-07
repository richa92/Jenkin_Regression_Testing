*** Settings ***
#OVF269- Validating TAA Hill Module
Documentation		F137 - SERVER.8 - Swapping the Uplinkport shouldnot disturb the SAN Connectivity
Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary
Variables		data_variables.py
Resource        resource.txt
Library			ServerOperations
Library			OAOperations
Library			c7000_login_redistribution
Resource		../../../resources/resource.txt

Suite Setup    Cleanup For Suite
Suite Teardown    Cleanup For Suite

*** Test Cases ***
###Pre-Conditions - Create LIG, EG, and import enclosure###
1 Create SessionID through API
	Set Log Level    TRACE
    ${Login_response} =    Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	Run keyword unless	${Login_response[0]['status_code']}== 200	Fail	"Unable to Login"
	Precheck for IC in OA
	Log to console and logfile    Test Step-1 completed successfully

2 Create Networks, LIG, EG and import enclosure through API
	${Response_enet}     fusion api create ethernet network		${enet_hill}
	Run keyword unless	${Response_enet['status_code']}== 202	Fail	"Unable to Create Ethernet network"
	${Response_fc1}     Add FC Networks from variable    ${fc1_hill}
	Run keyword unless	${Response_fc1['status_code']}== 202	Fail	"Unable to Create FC network"
	${Response_fc2}     Add FC Networks from variable    ${fc2_hill}
	Run keyword unless	${Response_fc2['status_code']}== 202	Fail	"Unable to Create FC network"
	Log to console and logfile    Networks created successfully
	
	${body} =   Build LIG body      ${lig_hill_edit1}
	${resp_lig} = 	Fusion Api Create LIG	${body}
	Run keyword unless	${resp_lig['status_code']}== 202	Fail	"Unable to Create LIG"
	${task} =	Wait For Task 	${resp_lig} 	120s	2s
	Log to console and logfile    LIG created successfully
	${uri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri
	Set Global Variable    ${lig_uri}    ${uri}
	Log to console and logfile    ${uri}
		
	${resp_eg} =    Add Enclosure Group from variable		${enc_group_hill}
	Run keyword unless	${resp_eg['status_code']}== 201	Fail	"Unable to Create EG"
	Log to console and logfile    EG created succesfully
	${resp_import} =    Add Enclosures from variable     ${encs}
	#Run keyword unless	${resp_import['status_code']}== 202	Fail	"Unable to import enclosure"
	Log to console and logfile    Enclosure imported succesfully
	
###Pre-Conditions steps over###
2 Create Uplink sets and Server profiles

	Add Server Profiles from variable   ${server_profiles_server7_bay1}
	Log to console and logfile    Test Step-1A completed successfully
	
	Add Server Profiles from variable   ${server_profiles_server7_bay10}
	Log to console and logfile    Test Step-1A completed successfully
	
3 Power on the servers
	Power on server    ${server_profiles_server7_bay1[0]['serverHardwareUri']}
	Power on server    ${server_profiles_server7_bay10[0]['serverHardwareUri']}
	sleep	${Poweron_Server_Sleeptime}
	
	Log to console and logfile    Server ${server_profiles_server7_bay1[0]['serverHardwareUri']} is powered on Successfully
	Log to console and logfile    Server ${server_profiles_server7_bay10[0]['serverHardwareUri']} is powered on Successfully
	sleep	100sec
	
4 Pass IO Traffic to check the connectivity with server1
	${output_1}	${msg_1}=		executes		${linux_details}	${oa_details_1}	${module_file_path}		${diskspd_cmd}	${windows_server_cred}
	Run keyword unless	'${msg_1}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output_1}

5 Pass IO Traffic to check the connectivity with server2	
	${output_2}	${msg_2}=		executes		${linux_details}	${oa_details_2}	${module_file_path}		${diskspd_cmd_1}	${windows_server_cred}
	Run keyword unless	'${msg_2}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output_2}
	
6 Edit LI to swap ports on different bays in the uplink set
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	Set Global Variable    ${LI_uri}    ${li_uri}
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets_server8['us_fc1']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	${us} = 		Copy Dictionary	${uplink_sets_server8['us_fc1']}
	${body} = 		Build US body 	${us}	${LI_uri}
	${resp} = 		Fusion Api Edit Uplink Set    body=${body}    uri=${Response['members'][0]['uri']}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets_server8['us_fc2']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	${us} = 		Copy Dictionary	${uplink_sets_server8['us_fc2']}
	${body} = 		Build US body 	${us}	${LI_uri}
	${resp} = 		Fusion Api Edit Uplink Set    body=${body}    uri=${Response['members'][0]['uri']}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	sleep	100sec
	
7 Pass IO Traffic to check the connectivity with server1
	${output_1}	${msg_1}=		executes		${linux_details}	${oa_details_1}	${module_file_path}		${diskspd_cmd}	${windows_server_cred}
	Run keyword unless	'${msg_1}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output_1}

8 Pass IO Traffic to check the connectivity with server2
	${output_2}	${msg_2}=		executes		${linux_details}	${oa_details_2}	${module_file_path}		${diskspd_cmd_1}	${windows_server_cred}
	Run keyword unless	'${msg_2}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output_2}
	Log to console and logfile    Test Case Server-7 completed successfully
	
9 Edit LI to add ports in the uplink set
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets_server8['us_fc3']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	${us} = 		Copy Dictionary	${uplink_sets_server8['us_fc3']}
	${body} = 		Build US body 	${us}	${LI_uri}
	${resp} = 		Fusion Api Edit Uplink Set    body=${body}    uri=${Response['members'][0]['uri']}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets_server8['us_fc4']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	${us} = 		Copy Dictionary	${uplink_sets_server8['us_fc4']}
	${body} = 		Build US body 	${us}	${LI_uri}
	${resp} = 		Fusion Api Edit Uplink Set    body=${body}    uri=${Response['members'][0]['uri']}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	sleep	100sec
	
10 Pass IO Traffic to check the connectivity with server1
	${output_1}	${msg_1}=		executes		${linux_details}	${oa_details_1}	${module_file_path}		${diskspd_cmd}	${windows_server_cred}
	Run keyword unless	'${msg_1}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output_1}

11 Pass IO Traffic to check the connectivity with server2
	${output_2}	${msg_2}=		executes		${linux_details}	${oa_details_2}	${module_file_path}		${diskspd_cmd_1}	${windows_server_cred}
	Run keyword unless	'${msg_2}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output_2}
	Log to console and logfile    Test Case Server-7 completed successfully
	
12 Edit LI to delete ports in the uplink set
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets_server8['us_fc5']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	${us} = 		Copy Dictionary	${uplink_sets_server8['us_fc5']}
	${body} = 		Build US body 	${us}	${LI_uri}
	${resp} = 		Fusion Api Edit Uplink Set    body=${body}    uri=${Response['members'][0]['uri']}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets_server8['us_fc6']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	${us} = 		Copy Dictionary	${uplink_sets_server8['us_fc6']}
	${body} = 		Build US body 	${us}	${LI_uri}
	${resp} = 		Fusion Api Edit Uplink Set    body=${body}    uri=${Response['members'][0]['uri']}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	sleep	100sec
	
13 Pass IO Traffic to check the connectivity with server1
	${output_1}	${msg_1}=		executes		${linux_details}	${oa_details_1}	${module_file_path}		${diskspd_cmd}	${windows_server_cred}
	Run keyword unless	'${msg_1}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output_1}

14 Pass IO Traffic to check the connectivity with server2
	${output_2}	${msg_2}=		executes		${linux_details}	${oa_details_2}	${module_file_path}		${diskspd_cmd_1}	${windows_server_cred}
	Run keyword unless	'${msg_2}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output_2}
	Log to console and logfile    Test Case Server-7 completed successfully
	
15 Edit LI to change port speeds in the uplink set
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets_server8['us_fc7']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	${us} = 		Copy Dictionary	${uplink_sets_server8['us_fc7']}
	${body} = 		Build US body 	${us}	${LI_uri}
	${resp} = 		Fusion Api Edit Uplink Set    body=${body}    uri=${Response['members'][0]['uri']}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets_server8['us_fc8']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	${us} = 		Copy Dictionary	${uplink_sets_server8['us_fc8']}
	${body} = 		Build US body 	${us}	${LI_uri}
	${resp} = 		Fusion Api Edit Uplink Set    body=${body}    uri=${Response['members'][0]['uri']}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	sleep	100sec
	
16 Pass IO Traffic to check the connectivity with server1
	${output_1}	${msg_1}=		executes		${linux_details}	${oa_details_1}	${module_file_path}		${diskspd_cmd}	${windows_server_cred}
	Run keyword unless	'${msg_1}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output_1}

17 Pass IO Traffic to check the connectivity with server2
	${output_2}	${msg_2}=		executes		${linux_details}	${oa_details_2}	${module_file_path}		${diskspd_cmd_1}	${windows_server_cred}
	Run keyword unless	'${msg_2}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output_2}
	Log to console and logfile    Test Case Server-7 completed successfully
	
18 Edit LI to change name of the uplink sets
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets_server8['us_fc7']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	${us} = 		Copy Dictionary	${uplink_sets_server8['us_fc9']}
	${body} = 		Build US body 	${us}	${LI_uri}
	${resp} = 		Fusion Api Edit Uplink Set    body=${body}    uri=${Response['members'][0]['uri']}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets_server8['us_fc8']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	${us} = 		Copy Dictionary	${uplink_sets_server8['us_fc10']}
	${body} = 		Build US body 	${us}	${LI_uri}
	${resp} = 		Fusion Api Edit Uplink Set    body=${body}    uri=${Response['members'][0]['uri']}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	sleep	100sec
	
19 Pass IO Traffic to check the connectivity with server1
	${output_1}	${msg_1}=		executes		${linux_details}	${oa_details_1}	${module_file_path}		${diskspd_cmd}	${windows_server_cred}
	Run keyword unless	'${msg_1}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output_1}

20 Pass IO Traffic to check the connectivity with server2
	${output_2}	${msg_2}=		executes		${linux_details}	${oa_details_2}	${module_file_path}		${diskspd_cmd_1}	${windows_server_cred}
	Run keyword unless	'${msg_2}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output_2}
	Log to console and logfile    Test Case Server-7 completed successfully

21 Edit LI to delete all the ports in the uplink set
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets_server8['us_fc15']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	${us} = 		Copy Dictionary	${uplink_sets_server8['us_fc15']}
	${body} = 		Build US body 	${us}	${LI_uri}
	${resp} = 		Fusion Api Edit Uplink Set    body=${body}    uri=${Response['members'][0]['uri']}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets_server8['us_fc16']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	${us} = 		Copy Dictionary	${uplink_sets_server8['us_fc16']}
	${body} = 		Build US body 	${us}	${LI_uri}
	${resp} = 		Fusion Api Edit Uplink Set    body=${body}    uri=${Response['members'][0]['uri']}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	sleep	100sec
	
22 Pass IO Traffic to check the connectivity with server1
	${output_1}	${msg_1}=		executes		${linux_details}	${oa_details_1}	${module_file_path}		${diskspd_cmd}	${windows_server_cred}
	Log to console and logfile    ${msg_1}
	Run keyword unless	'${msg_1}'== 'FAIL'    Fail    "Unable to verify the IO Traffic"
	Log to console and logfile    As expected there is no connectivity with the server

23 Pass IO Traffic to check the connectivity with server2
	${output_2}	${msg_2}=		executes		${linux_details}	${oa_details_2}	${module_file_path}		${diskspd_cmd_1}	${windows_server_cred}
	Log to console and logfile    ${msg_2}
	Run keyword unless	'${msg_2}'== 'FAIL'    Fail    "Unable to verify the IO Traffic"
	Log to console and logfile    As expected there is no connectivity with the server
	
###Proceeding with cleanup###	
24 Teardown
	Power off ALL servers
	${resp}=	fusion api delete server profile	${server_profiles_server7_bay1[0]['name']}
	${task} =	Wait For Task 	${resp} 	120s	10s
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete Server profile"
	
	${resp}=	fusion api delete server profile	${server_profiles_server7_bay10[0]['name']}
	${task} =	Wait For Task 	${resp} 	120s	10s
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete Server profile"
	
	${encs} = 	Fusion Api Get Enclosures
	${resp}		fusion API Remove Enclosure		uri=${encs['members'][0]['uri']}
	${task} =	Wait For Task1 	${resp}
	
	${resp}=	fusion api delete enclosure group		name=${enc_group_hill['name']}
	Run keyword unless	${resp['status_code']}== 204	Fail	"Unable to delete the Enclosure Group"
	
	${resp}=	fusion api delete lig		name=${lig_hill_new['name']}
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete the Enclosure Group"
	
	${Response}     fusion api delete ethernet network		${enet_hill['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to delete FC network"
	
	${Response}     fusion api delete fc network		${fc1_hill[0]['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	
	${Response}     fusion api delete fc network		${fc2_hill[0]['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"