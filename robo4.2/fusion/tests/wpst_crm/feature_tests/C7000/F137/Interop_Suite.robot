*** Settings ***
Documentation		22014: INTEROP.14 Verify manual login redistribution
Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary
Variables		data_variables.py
Resource        resource.txt
Library			ServerOperations
Library			OAOperations
Library			c7000_login_redistribution

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
	
	Add Server Profiles from variable   ${server_profiles_gen8_enc1_bay1}
	Log to console and logfile    Test Step-1A completed successfully
	
3. Power on the servers
	Power on server    ${server_profiles_gen8[0]['serverHardwareUri']}
	Power on server    ${server_profiles_gen8_enc1_bay1[0]['serverHardwareUri']}
	sleep	${Poweron_Server_Sleeptime}
	
	Log to console and logfile    Server ${server_profiles_gen8[0]['serverHardwareUri']} is powered on Successfully
	Log to console and logfile    Server ${server_profiles_gen8_enc1_bay1[0]['serverHardwareUri']} is powered on Successfully
	sleep	200sec

4. Manual Login Redistribution

	${out}=		fusion_api_get_li
	Log to console and logfile		${out['members'][0]['uri']}
	
	Log to console and logfile		${bay_port_detail}
	${output_1}	${logins}=	verify_login_count	${APPLIANCE_IP}	${out['members'][0]['uri']}	${bay_port_detail}	${mlr_initial_output}
	Log to console and logfile		${output_1}
	Log to Console		Login count details after poweron servers
	Log to console and logfile		${logins}
	Run keyword unless	'${output_1}'== 'True'	Fail	"The login counts dsplayed are incorect and not expected"

	${interconnects}=	fusion_api_get_interconnect
	
	${ports_uri}=	get_port_uri	${interconnects}	${bay_port_detail}	
	
	:FOR	${ele}	in	@{interconnect_ports_to_disable}
	\	@{temp} =  Split String	${ports_uri[str(${ele})]}	/ports
	\	${output}=	fusion_api_get_interconnect_ports	${temp[0]}	${api_version}	${temp[-1]}
	\	${payload}=		build_edit_interconnect_payload		${output}	${edit_interconnect_port_payload_keys}		false
	\	${status}=	edit interconnect	${APPLIANCE_IP}	${ports_uri[str(${ele})]}	${payload}	
	
	sleep	120sec
	${output_2}	${logins}=	verify_login_count	${APPLIANCE_IP}	${out['members'][0]['uri']}	${bay_port_detail}	${mlr_final_output}
	Log to console and logfile		${output_2}
	Log to Console		Login count details after disabling the interconnect ports
	Log to console and logfile		${logins}
	
	Run keyword unless	'${output_2}'== 'True'	Fail	"The login counts dsplayed are incorect and not expected"
	
	:FOR	${ele}	in	@{interconnect_ports_to_disable}
	\	@{temp} =  Split String	${ports_uri[str(${ele})]}	/ports
	\	${output}=	fusion_api_get_interconnect_ports	${temp[0]}	${api_version}	${temp[-1]}
	\	${payload}=		build_edit_interconnect_payload		${output}	${edit_interconnect_port_payload_keys}		true
	\	${status}=	edit interconnect	${APPLIANCE_IP}	${ports_uri[str(${ele})]}	${payload}	
	
	sleep	120sec
	
	${uplinkset}=	fusion_api_get_uplink_set
	
	${us_name}=	create list
	Append to list	${us_name}	${lig_uplink_sets['UplinkSet_2']['name']}	${lig_uplink_sets['UplinkSet_3']['name']}
	Log to console and logfile		${us_name}
		
	${return_data}=		manual_login_redistribution	${APPLIANCE_IP}	${out['members'][0]['uri']}	${uplinkset}	${us_name}
	sleep	30sec
	#${return_data}=		manual_login_redistribution	${APPLIANCE_IP}	${out['members'][0]['uri']}	${uplinkset}	${us_name}
	Log to console and logfile	${return_data}
	
	sleep	90sec
	
	${output_3}	${logins}=	verify_login_count	${APPLIANCE_IP}	${out['members'][0]['uri']}	${bay_port_detail}	${mlr_initial_output}
	Log to Console		${output_3}
	Log to Console		Login count details after Manual Login Redistribution
	Log to Console		${logins}
	Run keyword unless	'${output_3}'== 'True'	Fail	"The login counts dsplayed are incorect and not expected"	

	
6. Power off all servers
	Power off ALL servers
	
7. Delete the Server profile
	${resp}=	fusion api delete server profile	${server_profiles_gen8[0]['name']}
	Log to Console		${resp}
	${task} =	Wait For Task 	${resp} 	120s	10s
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete Server profile"
	
	${resp}=	fusion api delete server profile	${server_profiles_gen8_enc1_bay1[0]['name']}
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
