*** Settings ***
Documentation		IO.6 - IO stress test with scripted failing paths - 24 hours
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
	
	${body_new} =   Build LIG body      ${lig_hill_new}    
	${resp} = 	Fusion Api Edit Lig    ${body_new}    ${uri}
	${task} =	Wait For Task 	${resp} 	120s	2s
	Log to console and logfile    LIG edited successfully
	Log to console and logfile    Test Step-1 completed successfully


2.Create Uplink sets and Server profiles

	Add Server Profiles from variable   ${server_profiles_gen8}
	Log to console and logfile    Test Step-1A completed successfully

3. Power on the server 
	Power on server    ${server_profiles_gen8[0]['serverHardwareUri']}
	sleep	${Poweron_Server_Sleeptime}
	Log to console and logfile    Server ${server_profiles_gen8[0]['serverHardwareUri']} is powered on Successfully
	sleep	200sec

4. Get the interconnect and Start Traffic and parallely execute disable and enable uplink ports

	${out}=		fusion_api_get_interconnect
	${fc_uri}=	set variable	${empty}
	
	${enc_details}=	fusion_api_get_enclosures
	Log to Console	${enc_details['members'][0]['name']}
	${interconnect_name}=	catenate	${enc_details['members'][0]['name']}, interconnect ${fc_bay_num}	
	:FOR	${ele}	in	@{out['members']}
	\	${fc_uri}=		Set variable if	'${ele['name']}' == '${interconnect_name}'	${ele['uri']}
	\	Run Keyword If	'${ele['name']}' == '${interconnect_name}'	Exit For Loop
	
	${out1}=		fusion_api_get_interconnect	${fc_uri}
	${output}=		execute_IO_and_disable_enable_ports		${linux_details}	${oa_details}	${module_file_path}		${diskspd_cmd_disable_ports}	${windows_server_cred}	${fc_uri}	${out1}	${portno_for_statistics}
	
	Log to console and logfile		"The IO Traffic Details are \n"	INFO
	Log to console and logfile	${output}	INFO
	
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
