*** Settings ***
#OVF269- Validating TAA Hill Module
Documentation		 SERVER.2 - Create Server Profile with connections to a Hill, remove Hill module and observe OV message.
Library		json
Library		collections
Library 	BuiltIn
Library		String
Library		FusionLibrary
Variables	data_variables.py
Library		OperatingSystem
Library		String

Resource		resource.txt
Resource		../../../resources/resource.txt

Suite Setup    Cleanup For Suite
Suite Teardown    Cleanup For Suite

*** Test Cases ***

1 Log-in to the appliance
	Set Log Level    TRACE
    ${Login_response} =		Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}	
	Run keyword unless	${Login_response[0]['status_code']}== 200    Fail    "Unable to Login"
	Precheck for IC in OA
	Log to console and logfile		\n\nStep-1 Completed Successfully
	

3 Create Networks
	${Response}     fusion api create ethernet network		${enet_hill}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Create Ethernet network"
	Add FC Networks from variable    ${fc1_hill}
	Add FC Networks from variable    ${fc2_hill}
	Log to console and logfile		Ethernet and FC Networks created successfully
	Sleep	30sec
	
4 Create LIG,EG and Import Enclosure
	${body} =   Build LIG body      ${lig_hill_new}
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
	
5 Create Server Profile
	${Server_resp} =    Add Server Profiles from variable   ${server_profiles_gen8_enc1_bay1}
	#Run keyword unless	${Server_resp['status_code']}== 202	Fail	"Unable to Create Server Profile"
	Log to console and logfile    \n\nServer Profile Created Successfully
	
6 Validating the Interconnect State
	Validate IC State    ${IC_Configured}
	
7 Clear Alert Message
	${del_resp} =    Fusion Api Delete Alert
	Run keyword unless	${del_resp['status_code']}== 202	Fail	"Unable to Clear Alert Message"
	Log to console and logfile    \n\nAlert Message cleared Successfully
		
8 Remove Hill Module
	${resp} =	Fusion Api Get Lig
	${lig_uri} =	Get From Dictionary		${resp['members'][0]}	uri    
	${body} =   Build LIG body      ${lig_hill_edit}
	${resp} =	Fusion Api Edit Lig		${body}		${lig_uri}	
	${task} =	Wait For Task 	${resp} 	120s	2s
	Log to console and logfile    Hill removed by editing LIG Successfully

9 Verifying the presence of HILL in LIG
	${resp} =	Fusion Api Get Lig
	${icMapEntry} =     Get From Dictionary     ${resp['members'][0]['interconnectMapTemplate']}	interconnectMapEntryTemplates
	${mapEntrylist} =    Create List
	${len} = 	Get Length    ${icMapEntry}
	:FOR	${x}	IN RANGE	0	${len}
    \   ${mapEntry} =     Get From List   ${icMapEntry}    ${x}
	\   Append to list      ${mapEntrylist}  ${mapEntry['permittedInterconnectTypeUri']}

	${ICtype_Names} =	Create List
	:FOR	${y}	IN    @{mapEntrylist}
	\	${string} =    Fetch From Right    ${y}    /
	\	${param} =	Catenate	SEPARATOR=	/	${string}
	\	${IC_Details} =    Fusion Api Get Interconnect Types    param=${param}
#	\	${IC_Details} =    Fusion Api Get Interconnect Types    uri=${y}
	\	Run Keyword If    '${IC_Details['name']}' != '${Module_name}'	Continue For Loop	
	\	Append To List    ${ICtype_Names}    ${IC_Details['name']}
	${len} = 	Get Length    ${ICtype_Names}
	Run Keyword If      ${len} != 0       fail    "Hill Module is Present in LIG"
    ...         ELSE    Log to console and logfile   \nHill Module is not Present in LIG

10 Update from Group	
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	Perform an LI Update From Group    ${li_uri}
	Log to console and logfile    \n\nUpdate from Group is done Successfully
	
11 Validating the Interconnect State
	Validate IC State    ${IC_Inventory}
	
12 Checking for the alert message in OV	
	${resp} =    Fusion Api Get Alerts
	${mem_resp} =	Get From Dictionary		${resp}		members
	${len} = 	Get Length	${mem_resp}
	${Alert_msg} =	Create List
	:FOR	${x}	IN RANGE	0	${len}
	\	${desc_alert} =		Get From Dictionary		${mem_resp[${x}]}		description
	\	Run Keyword If    '${desc_alert}' != '${Alert_Message_Server_Profile}'	Continue For Loop	
	\	Append To List    ${Alert_msg}    ${desc_alert}
	${len} = 	Get Length    ${Alert_msg}
	Run keyword unless	${len}!= 0    Fail    "No Critical Alert Message Observed"
	Log to console and logfile   \n${Alert_Message_Server_Profile} is observed	
	
###Proceeding with cleanup###
TEARDOWN
	Power off ALL Servers
	Remove All Server Profiles
    Remove ALL Enclosures
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Remove ALL Ethernet Networks
    Remove ALL FC Networks
    Log to console and logfile    Test Suite LIG for hill module completed successfully