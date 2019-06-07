*** Settings ***
Documentation		IO.4 - Verify OneView VM restart with IO traffic
Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary
Variables		data_variables.py
Resource        resource.txt
Library		ServerOperations

Suite Setup    Cleanup For Suite
Suite Teardown    Cleanup For Suite

*** Test cases ***
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

4. Pass IO Traffic
	${output}	${msg}=		executes		${linux_details}	${oa_details}	${module_file_path}		${diskspd_cmd}	${windows_server_cred}
	Run keyword unless	'${msg}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output}
	
5. Restart the Appliance
	${out}	Fusion API Appliance shutdown		REBOOT
	Log to Console	${out}

6. Pass IO Traffic to check the disturbance while restarting
	${output}	${msg}=		executes		${linux_details}	${oa_details}	${module_file_path}		${diskspd_cmd_1}	${windows_server_cred}
	Run keyword unless	'${msg}'== 'PASS'	Fail	"Unable to verify the IO Traffic"
	Log To Console		"The IO Traffic Details are as follows: \n"
	Log to Console		${output}

7. Log into the Appliance and verify the settings
	Login to OneView via REST

8.Validate the Ethernet Networks are present

	${Response}		Fusion Api Get Ethernet Networks	param=?filter="'name'=='${enet_hill['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the Ethernet network is  present in the appliance"

9. Validate the FC Networks are present
	${Response}		Fusion Api Get FC Networks		param=?filter="'name'=='${fc1_hill[0]['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the FC network is  present in the appliance"
	${Response}		Fusion Api Get FC Networks		param=?filter="'name'=='${fc2_hill[0]['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the FC network is  present in the appliance"
	
10. Validate the LIG is present
	${resp} 	Fusion Api Get LIG 		param=?filter="'name'=='${lig_hill_new['name']}'"
	Run keyword unless	${resp['count']}== 1	Fail	"Unable to verify the LIG present in the appliance"
	
11. Validate the Server Profile is present
	${resp}=	fusion api get server profiles	param=?filter="'name'=='${server_profiles_gen8[0]['name']}'"
	Run keyword unless	${resp['count']}== 1	Fail	"Unable to verify the server Profile is  present in the appliance"

Teardown

	Power off ALL servers
	
	${resp}=	fusion api delete server profile	${server_profiles_gen8[0]['name']}
	Log to Console		${resp}
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
