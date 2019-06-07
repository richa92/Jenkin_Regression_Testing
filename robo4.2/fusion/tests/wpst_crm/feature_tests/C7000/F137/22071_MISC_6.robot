*** Settings ***
Documentation		MISC.6 - Upgrade OV 2.0 to OV 3.0 with Hill modules installed.  After upgrade, verify Hill modules are in configured state
Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary
Variables		data_variables.py
Resource        resource.txt
Library			ServerOperations
Library			OAOperations


Suite Setup		Login to OneView via REST
Suite Teardown	Logout OneView via REST


*** Test Cases ***
###Pre-Conditions - Create LIG, EG, Networks and import enclosure###
1. Log-in to the appliance
	Set Log Level    TRACE
    ${Login_response} =		Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}	
	Run keyword unless	${Login_response[0]['status_code']}== 200    Fail    "Unable to Login"
	Log to console and logfile		\n\nLogged In Successfully!!!
	
####Initial Clean-Up#####
2. Initial Cleanup
    Remove ALL Enclosures
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Remove ALL Ethernet Networks
    Remove ALL FC Networks
		
4. Create LIG,EG and Import Enclosure
	${body} =   Build LIG body      ${lig_hill_edit}
	${resp_lig} = 	Fusion Api Create LIG	${body}
	Run keyword unless	${resp_lig['status_code']}== 202	Fail	"Unable to Create LIG"
	${task} =	Wait For Task 	${resp_lig} 	120s	2s
	Log to console and logfile    LIG created successfully

	${Enc_Grp_Resp} =    Add Enclosure Group from variable		${enc_group_V200}
	Run keyword unless	${Enc_Grp_Resp['status_code']}== 200	Fail	"Unable to Create Enclosure Group"
	Log to console and logfile    \n\nEG created succesfully
	
	${Enc_Resp} =    Add Enclosures from variable     ${encs}
	Run keyword unless	${Enc_Resp['status_code']}== 202	Fail	"Unable to Create Ethernet network"
	Log to console and logfile    \n\nEnclosure imported succesfully

5. Validating the Interconnect State
	Validate IC State    ${IC_Inventory}
	
###Pre-Conditions steps over###
	
6. Uploading the BIN File
	${upload_resp} =    Fusion Api Upload Appliance Firmware    ${localfile}
	Run keyword unless	${upload_resp['status_code']}== 200	Fail	"Unable to Upload Bin File"
	
7. Upgrade Appliance
	${upgrade_resp} =    Fusion Api Upgrade Appliance Firmware    ${localfile}
	Run keyword unless	${upgrade_resp['status_code']}== 202	Fail	"Unable to Upgrade Appliance"
	sleep   ${Upload_Sleep_Time}
	
8. Validate upgrade
	${upgrade_resp_1} =    Fusion Api Get Appliance Firmware Upgrade Status
	Log to console and logfile    \n\nupgrade_resp_1..${upgrade_resp_1}
	${version_dict} =    Get From Dictionary	${upgrade_resp_1}    version
	${string} =    Fetch From Left    ${version_dict}    ,
	Log to console and logfile    \n\nstring...${string}
	Run keyword unless	'${string}' == '${version_Check}'	Fail	"Appliance did not get upgraded to the version ${version_Check}"
	Log to console and logfile    \n\nAppliance got upgraded to the version ${version_Check} 
	
9. Validating the Interconnect State
	Validate IC State    ${IC_Configured}
	
###Proceeding with cleanup###
TEARDOWN
    Remove ALL Enclosures
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Log to console and logfile    \n\nTest Suite Upgrade Appliance with hill module completed successfully
	
