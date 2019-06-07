*** Settings ***
#OVF269- Validating TAA Hill Module
Documentation		Backup and restore scenario for Hill Module
Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary
Variables		data_variables.py
Resource        resource.txt
Resource		../../../resources/resource.txt

Suite Setup    Cleanup For Suite
Suite Teardown    Cleanup For Suite

*** Test Cases ***

###Pre-Conditions - Create LIG, EG, Networks and import enclosure###
1 Create SessionID through API
	Set Log Level    TRACE
    ${Login_response} =	Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	Run keyword unless	${Login_response[0]['status_code']}== 200    Fail    "Unable to Login"
	Precheck for IC in OA
	Log to console and logfile    Test Step-1 completed successfully

2 Create Networks, LIG, EG and import enclosure through API
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
	
	#${body_new} =   Build LIG body      ${lig_hill_new}    
	#${resp} = 	Fusion Api Edit Lig    ${body_new}    ${uri}
	#${task} =	Wait For Task 	${resp} 	180s	2s
	#Log to console and logfile    LIG edited successfully
	Log to console and logfile    Test Step-2 completed successfully
	
	Add Server Profiles from variable   ${server_profiles_gen8}
	Log to console and logfile    Test Step-1A completed successfully

1B Perform Backup Operation
	${Response}		Fusion Api Create Backup
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Create Backup"
	Sleep	200sec
	
	${Response}		Fusion Api Get Backup
	Run keyword unless	${Response['status_code']}== 200	Fail	"Unable to Get the latest backup"
	Log to console and logfile    Test Step-1B completed successfully
	
	
1C Restore from Backup operation
	Restore From Backup
	Log to console and logfile    Test Step-1C completed successfully
	
1D Validate the Created uplink set and server profile is present
	Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	Log to console and logfile    logged in succesfully
	
	#Server boot check
	Power on server    ${Server_name}
	Log to console and logfile    server boot checked succesfully
	
	#Validating the existence of already created server profiles
	${resp}=	fusion api get server profiles	param=?filter="'name'=='${server_profiles_gen8[0]['name']}'"
	Run keyword unless	${resp['count']}== 1	Fail	"Unable to verify the server Profile is present in the appliance
	
	#Validating the existence of already created uplink set
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets['us_eth']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets['us_fc1']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	
	#Validate the LIG is present
	${resp} 	Fusion Api Get LIG 		param=?filter="'name'=='${lig_hill['name']}'"
	Run keyword unless	${resp['count']}== 1	Fail	"Unable to verify the LIG present in the appliance"
	Power off server    ${Server_name}
	Log to console and logfile    Test Step-1D completed successfully
###Test Objective acheived successfully for BACKUP-1 test case###
	
###Proceeding with BACKUP-3 test case###
#The purpose of this test is to verify that changes to the LIG/LI will be backed out on restore.
3A Create additional uplink set and server profile after backup
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	${us} = 		Copy Dictionary	${uplink_sets['us_fc_new']}
	${body} = 		Build US body 	${us}	${li_uri}
	${resp} = 		Fusion Api Create Uplink Set	body=${body}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	Log to console and logfile    Uplink set created successfully
	
	Add Server Profiles from variable   ${server_profiles_gen8_bay1}
	Log to console and logfile    Test Step-3A completed successfully
	
3B Restore from Backup operation
	Restore From Backup
	Log to console and logfile    Test Step-3B completed successfully
	
3C Validate the newly added uplink set and server profile is gone
	Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	
	#Validating the newly created server profiles
	${resp}=	fusion api get server profiles	param=?filter="'name'=='${server_profiles_gen8_bay1[0]['name']}'"
	Run keyword unless	${resp['count']}== 0	Fail	"Unable to verify the newly created server Profile is  absent in the appliance"
	
	#Validating the newly created uplink set
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets['us_fc_new']['name']}'"
	Run keyword unless	${Response['count']}== 0	Fail	"Unable to verify the newly created uplink set is  absent in the appliance"
	
	#Validating the LI/LIG consistency status
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	${resp}=	Fusion Api Get Li	
	Log to console and logfile    ${resp}
	Should Be Equal As Strings	${resp['members'][0]['consistencyStatus']}    ${Expected_Consistency_Status}
	Log to console and logfile    LI/LIG are consistent.
	
	#Validating the existence of already created server profiles
	${resp}=	fusion api get server profiles	param=?filter="'name'=='${server_profiles_gen8[0]['name']}'"
	Run keyword unless	${resp['count']}== 1	Fail	"Unable to verify the server Profile is present in the appliance
	
	#Validating the existence of already created uplink set
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets['us_fc1']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	Log to console and logfile    Test Step-3C completed successfully

###Test Objective acheived successfully for BACKUP-3 test case###
	
###Proceeding with BACKUP-5 test case###
#The purpose of this test is to confirm that backing up the OneView appliance and restoring it will reverse anything that's been deleted.
5A Deleting FC Networks, Server profiles and Uplink set before restore operation
	
	Log to console and logfile  \n\n****Deleting Server Profile****
	${resp}=	fusion api delete server profile	${server_profiles_gen8[0]['name']}
	${task} =	Wait For Task 	${resp} 	120s	10s
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete Server profile"
	Log to console and logfile  \n\nServer Profile deleted succesfully !!
	
	Log to console and logfile  \n\n****Deleting UplinkSet****
	${resp} =	Fusion Api Delete Uplink Set	${uplink_sets['us_fc1']['name']}
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to Delete UplinkSet"
	Log to console and logfile  \n\nUplinkSet deleted succesfully !!
	
	Log to console and logfile  \n\n****Deleting FCNetwork****
	${Response}     fusion api delete fc network		${fc1_hill[0]['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
    Log to console and logfile  \n\nFC Network deleted succesfully !!
	Log to console and logfile    Test Step-5A completed successfully

5B Restore from Backup operation
	Restore From Backup
	Log to console and logfile    Test Step-5B completed successfully

5C Validate the Created uplink set and server profile is present
	Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	
	#Validating the existence of deleted server profiles after restore
	${resp}=	fusion api get server profiles	param=?filter="'name'=='${server_profiles_gen8[0]['name']}'"
	Run keyword unless	${resp['count']}== 1	Fail	"Unable to verify the server Profile is present in the appliance
	Log to console and logfile    Server profile is present.Verified Successfully
	
	#Validating the existence of deleted uplink set after restore
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets['us_fc1']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	Log to console and logfile    Uplink set is present.Verified Successfully
	
	${Response}		Fusion Api Get FC Networks		param=?filter="'name'=='${fc1_hill[0]['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the FC network is  present in the appliance"
	Log to console and logfile    FC Networks are present.Verified Successfully
	
	Log to console and logfile    Test Step-5C completed successfully
###Test Objective acheived successfully for BACKUP-5 test case###
	
###Proceeding with BACKUP-6 test case###
#The purpose of this test is to verify that CRX1001440175 is no longer an issue.
6A Verify user is able to create networks, uplink sets and server profiles
	
	#Verify User can create FC Network	
	Add FC Networks from variable    ${fc3_hill}
	Log to console and logfile    User can create FC network
	
	#Verify User can create uplink sets
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	${us} = 		Copy Dictionary	${uplink_sets['us_fc_mk']}
	Log to console and logfile    ${us}
	${body} = 		Build US body 	${us}	${li_uri}
	${resp} = 		Fusion Api Create Uplink Set	body=${body}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
	Log to console and logfile    Uplink set created successfully
	
	#Verify User can create Server Profiles
	Add Server Profiles from variable   ${server_profiles_gen8_bay1}
	Log to console and logfile    User can create server profile
	
	Log to console and logfile    Test Step-6A completed successfully
###Test Objective acheived successfully for BACKUP-6 test case###

###Proceeding with BACKUP-4 test case###
#The purpose of this test is to confirm that the OneView appliance factory defaults came be backed out with a restore.  
4A Create Backup
	${Response}		Fusion Api Create Backup
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Create Backup"
	Sleep	180sec
	
4B Download Backup
	[Tags]	download
	[Documentation]	Downloads the current backup from OneView 
	${Response}		Fusion Api Get Backup
	Log To Console		${Response}
	Run keyword unless	${Response['status_code']}== 200	Fail	"Unable to Get the latest backup"
	Log To Console		${Response['members'][0]['id']}
	set global variable	${Backup_file_name}	${Response['members'][0]['id']}
	Log to Console	${Backup_file_name}	${\n}
	Download Backup
  
4C Reset OV Appliance to Factory Defaults
	Log to console and logfile  \n\n****Reset OV Appliance to Factory Defaults****
	${resp} =	Fusion Api Appliance Factory Reset	${Mode}
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to do Factory Reset"
	Log to console	\nFactory Reset In-Progress.
	Sleep	${factory_reset_sleep_time}
	Log to console	\nFactory Reset Done Successfully.
	Sleep	200Sec
	${Response}    Fusion Api Save Eula    ${appliance_IP}    yes
	Pass Execution If    ${Response['status_code']}==200    Saved EULA Status
	Sleep	120Sec
	
4D Change the password
	${Creds}    Create Dictionary    newPassword=${admin_credentials['password']}
	...                              oldPassword=${admin_default_paswd}
	...                              userName=${admin_credentials['userName']}
	Log To Console		"Going to change the password"
	${Response}    Fusion Api Change Administrator Password    ${appliance_IP}    ${Creds}
	Log to Console		${Response}
	Pass Execution If	${Response['status_code']}==200	Assigned Administrator password	${admin_credentials['password']}
	Fatal Error    Fatal Error Assigning Administrator Password
	sleep	100Sec
	Log To Console		${\n}	"Done change the password"

4E Log in to Oneview
	Log To Console		"Log in to Oneview"	${\n}
	Login to OneView via REST
	sleep	120Sec
	
4F Upload Backup
	[Tags]	upload
	[Documentation]	Uploads a backup file to OneView
	Log To Console	${Backup_file_name}	${\n}
	Log To Console	${BACKUPFILE_DIR}${Backup_file_name}
	sleep	360sec
	Upload Backup		${BACKUPFILE_DIR}${Backup_file_name}
	sleep	300sec

4G Get the created Backup and start the restore operation
	Restore From Backup
	Log to console and logfile		"Exited from the for loop"

4H Log in to Oneview
	Login to OneView via REST
	
4I Validation
	#Validating the existence of already created server profiles
	${resp}=	fusion api get server profiles	param=?filter="'name'=='${server_profiles_gen8_bay1[0]['name']}'"
	Run keyword unless	${resp['count']}== 1	Fail	"Unable to verify the server Profile is present in the appliance
	
	#Validating the existence of already created uplink set
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets['us_eth']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	
	${Response}		Fusion Api Get Uplink Set	param=?filter="'name'=='${uplink_sets['us_fc1']['name']}'"
	Run keyword unless	${Response['count']}== 1	Fail	"Unable to verify the uplink set is  present in the appliance"
	
	#Validate the LIG is present
	${resp} 	Fusion Api Get LIG 		param=?filter="'name'=='${lig_hill_new['name']}'"
	Run keyword unless	${resp['count']}== 1	Fail	"Unable to verify the LIG present in the appliance"
	Log to console and logfile    Test Step-6D completed successfully

###Proceeding with cleanup###
8 Teardown (a) Cleanup
	Power off ALL servers
	${resp}=	fusion api delete server profile	${server_profiles_gen8_bay1[0]['name']}
	${task} =	Wait For Task 	${resp} 	120s	10s
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete Server profile"
	
	${resp}=	fusion api delete server profile	${server_profiles_gen8[0]['name']}
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
	
	${Response}     fusion api delete fc network		${fc3_hill[0]['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	Log to console and logfile    Test case Backup & Restore check for hill module completed successfully