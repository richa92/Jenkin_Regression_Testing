*** Settings ***
#OVF269- Validating TAA Hill Module
Documentation		 TEST SUITE - LIG
Library		json
Library		collections
Library 	BuiltIn
Library		String
Library		FusionLibrary
Variables	data_variables.py
Library		OperatingSystem
Library		String
Resource		../../../resources/resource.txt

Resource		resource.txt

*** Test Cases ***

1 Log-in to the appliance
	Set Log Level    TRACE
    ${Login_response} =		Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}	
	Run keyword unless	${Login_response[0]['status_code']}== 200    Fail    "Unable to Login"
	Precheck for IC in OA
	Log to console and logfile		\n\nSTEP-1 completed Successfully!!!
	
###Inital Cleanup###
2 Initial Cleanup
    Remove ALL Enclosures
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Remove ALL Ethernet Networks
    Remove ALL FC Networks
    
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

	${Enc_Grp_Resp} =    Add Enclosure Group from variable		${enc_group_hill}
	Run keyword unless	${Enc_Grp_Resp['status_code']}== 201	Fail	"Unable to Create Enclosure Group"
	Log to console and logfile    \n\nEG created succesfully
	
	${Enc_Resp} =    Add Enclosures from variable     ${encs}
	#Run keyword unless	${Enc_Resp['status_code']}== 202	Fail	"Unable to Create Ethernet network"
	Log to console and logfile    \n\nEnclosure imported succesfully
	
5 Validating the Interconnect State
	Validate IC State    ${IC_Configured}

#####LIG-3 : Edit LI, delete Hill module and uplink sets.  Verify changes in module.  Verify IC status.  LIG and LI should be inconsistent###

#### LIG-3 : Step-1 Delete Uplink Set ###

6-a Delete Uplink sets from LI and check for Consistency State
	${resp} = 	Fusion Api Get Uplink Set
	Run keyword unless	${resp['status_code']}== 200	Fail	"Unable to get Uplinkset Details"
	${mem_resp} =	Get From Dictionary		${resp}		members
	${len} = 	Get Length	${mem_resp}
	:FOR	${x}	IN RANGE	0	${len}
	\	${us_name} =	Get From Dictionary		${mem_resp[${x}]}	name
	\	${resp} = 	Fusion Api Delete Uplink Set	${us_name}
	\	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to get Uplinkset Details"
	
6-b Check for Inconsistency alert message in LI
	Get LI LIG Consistency    ${Inconsistency_Status}

6-c Update from Group	
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	Perform an LI Update From Group    ${li_uri}
	Log to console and logfile    \n\nUpdate from Group is done Successfully
	
6-d Check for Consistency alert message in LI
	Get LI LIG Consistency    ${Consistency_Status}

###LIG-3 : Step-2 - Delete Hill Module and check for IC State###

7 Remove Hill by editing LIG
	${resp} =	Fusion Api Get Lig
	${lig_uri} =	Get From Dictionary		${resp['members'][0]}	uri    
	${body} =   Build LIG body      ${lig_hill_edit}
	${resp} =	Fusion Api Edit Lig		${body}		${lig_uri}	
	${task} =	Wait For Task 	${resp} 	120s	2s
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to Edit LIG"
	Log to console and logfile    Hill removed by editing LIG Successfully

8 Verifying the presence of HILL in LIG
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
	\	Log to console and logfile	\n\nIC_Details... ${IC_Details}
	\	Run Keyword If    '${IC_Details['name']}' != '${Module_name}'	Continue For Loop	
	\	Append To List    ${ICtype_Names}    ${IC_Details['name']}
	${len} = 	Get Length    ${ICtype_Names}
	Run Keyword If      ${len} != 0       fail    "Hill Module is Present in LIG"
   ...         ELSE    Log to console and logfile   \nHill Module is not Present in LIG

9 Verify the LI consistency with LIG
   Get LI LIG Consistency    ${Inconsistency_Status}
   
10 Update from Group
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	Perform an LI Update From Group    ${li_uri}
	
11 Verify the LI consistency with LIG
	Get LI LIG Consistency    ${Consistency_Status}
	
###LIG-6 :  Edit LIG, remove a Hill module from LIG.  From LI, update from group, verify status of removed module is Inventory###	

12 Verify Module Status
	Validate IC State    ${IC_Inventory}

#####Adding the HILL again#####

13 Edit LIG by adding the module
	${resp} =	Fusion Api Get Lig
	${lig_uri} =	Get From Dictionary		${resp['members'][0]}	uri    
	${body} =   Build LIG body      ${lig_hill}
	${resp} =	Fusion Api Edit Lig		${body}		${lig_uri}	
	${task} =	Wait For Task 	${resp} 	120s	2s
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to Edit LIG"
	Log to console and logfile    Hill added by editing LIG Successfully
	
14 Verifing the presence of HILL in LIG
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
	Run Keyword If      ${len} == 0       fail    "Hill Module is not Present in LIG"
    Log to console and logfile   \nHill Module is Present in LIG

15 Update from Group	
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	Perform an LI Update From Group    ${li_uri}
	Log to console and logfile    \n\nUpdate from Group is done Successfully

16 Validating the Interconnect State
	Validate IC State    ${IC_Configured}
	
###LIG-5 : Edit LI, edit uplink sets, network, port speeds.  Verify LI status is inconsistent with LIG.  update from group, verify changes in LI are removed.  Verify LI and LIG are consistent####

17 Edit LI by creating Uplink Set
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	${us} = 		Copy Dictionary	${uplink_sets['us_eth']}
	${body} = 		Build US body 	${us}	${li_uri}
	${resp} = 		Fusion Api Create Uplink Set	body=${body}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
		
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	${us} = 		Copy Dictionary	${uplink_sets['us_fc']}
	${body} = 		Build US body 	${us}	${li_uri}
	${resp} = 		Fusion Api Create Uplink Set	body=${body}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}

18 Verify the consistency state in LI
	Get LI LIG Consistency    ${Inconsistency_Status}
	
19 Edit UplinkSet - By edit Network
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	${us} = 		Copy Dictionary	${uplink_sets_edit1['us_fc']}
	${body} = 		Build US body 	${us}	${li_uri}
	${resp} =    Fusion Api Get Uplink Set    param=?filter="'name'=='${US_Check}'"
	${uri} =    Get From Dictionary		${resp['members'][0]}	uri
	${resp} = 		Fusion Api Edit Uplink Set	body=${body}	uri=${uri}
	${task} =       Wait For Task 	${resp} 	5 min	15s
	${valDict} = 	Create Dictionary	status_code=${200}
	...									taskState=Completed
	Validate Response	${task}	${valDict}
		
20 Verify the consistency state in LI
	Get LI LIG Consistency    ${Inconsistency_Status}

21 Update from Group	
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	Perform an LI Update From Group    ${li_uri}
	Log to console and logfile    \n\nUpdate from Group is done Successfully
	
22 Verifying the changes in LI is removed
	${UplinkSet_resp} = 	Fusion Api Get UplinkSet
	${UplinkSet_Count} =	Get From Dictionary    ${UplinkSet_resp}		count
	Run Keyword If	${UplinkSet_Count}!= 0	Fail	"The Changes made in LI is not removed"
	Log to console and logfile  \n\nThe Changes made in LI is removed
	
23 Verify the consistency state in LI
	Get LI LIG Consistency    ${Consistency_Status}
	
###Proceeding with cleanup###
TEARDOWN
    Remove ALL Enclosures
    Remove ALL Enclosure Groups
    Remove ALL LIGs
    Remove ALL Ethernet Networks
    Remove ALL FC Networks
    Log to console and logfile    Test Suite LIG for hill module completed successfully