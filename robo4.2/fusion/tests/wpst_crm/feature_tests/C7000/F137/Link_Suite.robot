*** Settings ***
Documentation		LINK.7 - Verify port statistics while passing IO traffic | | LINK.19 - Verify port statistics are cleared when port is reset
Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary
Variables		data_variables.py
Resource        resource.txt
Library			ServerOperations
Library			OAOperations


Suite Setup    Cleanup For Suite
Suite Teardown    Cleanup For Suite


*** Test Cases ***
1.Create Networks, LIG, EG and import enclosure through API
	${Response}     fusion api create ethernet network		${enet_hill}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Create Ethernet network"
	Add FC Networks from variable    ${fc1_hill}
	Add FC Networks from variable    ${fc2_hill}
	Log to console and logfile		Ethernet and FC Networks created successfully
	Sleep	30sec

	${body} =   Build LIG body      ${lig_hill_new}
	${resp_lig} = 	Fusion Api Create LIG	${body}
	${task} =	Wait For Task 	${resp_lig} 	120s	2s
	Log to console and logfile    LIG created successfully
	${uri} =    Get From Dictionary    ${task['associatedResource']}    resourceUri
	Log to console and logfile    ${uri}
		
	Add Enclosure Group from variable		${enc_group_hill}
	Log to console and logfile    EG created succesfully
	Add Enclosures from variable     ${encs}
	Log to console and logfile    Enclosure imported succesfully
	
	Log to console and logfile    Test Step-1 completed successfully


2.Create Uplink sets and Server profiles

	Add Server Profiles from variable   ${server_profiles_gen8}
	Log to console and logfile    Test Step-1A completed successfully

3. Power on the server 
	Power on server    ${server_profiles_gen8[0]['serverHardwareUri']}
	sleep	${Poweron_Server_Sleeptime}
	Log to console and logfile    Server ${server_profiles_gen8[0]['serverHardwareUri']} is powered on Successfully
	sleep	200sec

4. Get the interconnect and port statistics details
	
	${out}=		fusion_api_get_interconnect
	${fc_uri}=	set variable	${empty}
	${enc_details}=	fusion_api_get_enclosures
	Log to Console	${enc_details['members'][0]['name']}
	
	${interconnect_name}=	catenate	${enc_details['members'][0]['name']}, interconnect ${fc_bay_num}	
	Log to console		${interconnect_name}
	:FOR	${ele}	in	@{out['members']}
	\	${fc_uri}=		Set variable if	'${ele['name']}' == '${interconnect_name}'	${ele['uri']}
	\	Run Keyword If	'${ele['name']}' == '${interconnect_name}'	Exit For Loop
	Log to Console		"The interconnect URI is "	${\n}
	Log to console		${fc_uri}
		
	#${uri}=	catenate	${out['members'][${fc_bay_num}]['uri']}/statistics
	${uri}=	catenate	${fc_uri}/statistics
	Log to Console	${uri}
	
	${out1}=		fusion_api_get_interconnect	${uri}
	${t2}	${t3}=	vaildate_port_statistics	${portno_for_statistics[0]}	${out1}	
	Log to console and logfile 		"Before the Reset"	INFO
	Log to console and logfile		"bytesTX : "	INFO	
	Log to console and logfile		${t2}	INFO
	Log to console and logfile 		"bytesRX : "	INFO
	Log to console and logfile		${t3}	INFO
	
	${uri_2}=	catenate	${fc_uri}
	Log To Console		${uri_2}
	
	${clear}=	fusion_api_clear_interconnect_ports	None	${uri_2}
	Log To Console		${clear}
	sleep	35sec
		
	${out1}=		fusion_api_get_interconnect	${uri}
	${t2}	${t3}=	vaildate_port_statistics	${portno_for_statistics[0]}	${out1}
	should be true	${t2} < 15000
	should be true	${t3} < 15000
	Log to console and logfile  		"After the Reset"	INFO
	Log to console and logfile 		"bytesTX : "	INFO
	Log to console and logfile 		${t2}	INFO
	Log to console and logfile 		"bytesRX : "	INFO
	Log to console and logfile 		${t3}	INFO
	
	${output}	${msg}=		executes		${linux_details}	${oa_details}	${module_file_path}		${diskspd_cmd}	${windows_server_cred}
	Run keyword unless	'${msg}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output}
	sleep	120sec
	
	${out1}=		fusion_api_get_interconnect	${uri}
	${t2}	${t3}=	vaildate_port_statistics	${portno_for_statistics[0]}	${out1}
	Log to console and logfile 		"After passing the traffic the values are as followss"	INFO
	Log to console and logfile		"bytesTX : "	INFO
	Log to console and logfile		${t2}	INFO
	Log to console and logfile		"bytesRX : "	INFO
	Log to console and logfile		${t3}	INFO
	should be true	${t2} > 2000
	should be true	${t3} > 2000
	Log to console and logfile		"Successfully Verified the port Statistics!!!"	INFO
	
6. Power off all servers
	Power off ALL servers
	
7. Delete the Server profile
	${resp}=	fusion api delete server profile	${server_profiles_gen8[0]['name']}
	Log to Console		${resp}
	${task} =	Wait For Task 	${resp} 	120s	10s
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete Server profile"

8. Delete the Enclosure
	${encs} = 	Fusion Api Get Enclosures
	${resp}		fusion API Remove Enclosure		uri=${encs['members'][0]['uri']}
	${task} =	Wait For Task1 	${resp}
	
	${resp}=	fusion api delete enclosure group		name=${enc_group_hill['name']}
	Run keyword unless	${resp['status_code']}== 204	Fail	"Unable to delete the Enclosure Group"
	
	${resp}=	fusion api delete lig		name=${lig_hill_new['name']}
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete the Enclosure Group"
	
9. Delete the Networks
	${Response}     fusion api delete ethernet network		${enet_hill['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to delete FC network"
	
	${Response}     fusion api delete fc network		${fc1_hill[0]['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	
	${Response}     fusion api delete fc network		${fc2_hill[0]['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
