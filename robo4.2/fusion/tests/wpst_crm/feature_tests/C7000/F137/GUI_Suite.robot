*** Settings ***
Documentation		 GUI scenario for Hill module
Library		json
Library		collections
Library 	BuiltIn
Library		String
Library		FusionLibrary
Variables	data_variables.py
Library		OperatingSystem
Library		String

Resource		resource.txt

Suite Setup    Cleanup For Suite
Suite Teardown    Cleanup For Suite

*** Test Cases ***

###Pre-Conditions - Create LIG, EG, and import enclosure###
1.Create SessionID through API
	Set Log Level    TRACE
    ${Login_response} =    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
	Run keyword unless	${Login_response[0]['status_code']}== 200	Fail	"Unable to Login"
	Precheck for IC in OA
	Log to console and logfile    Test Step-1 completed successfully

2.Create Networks, LIG, EG and import enclosure through API
	${Response}     fusion api create ethernet network		${enet_hill}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Create Ethernet network"
	Add FC Networks from variable    ${fc1_hill}
	Add FC Networks from variable    ${fc2_hill}
	Log to console and logfile    Networks created successfully

	${body} =   Build LIG body      ${lig_hill}
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
	Run keyword unless	${resp_import['status_code']}== 202	Fail	"Unable to import enclosure"
	Log to console and logfile    Enclosure imported succesfully
	
3. Validating the Interconnect State
	Validate IC State    ${IC_Configured}
	
###Pre-Conditions steps over###
	
######## Verify Hill displays (see steps for details)######
4. To check the Serial and part number

	Fusion Api Login Appliance	${APPLIANCE_IP}		${admin_credentials}
	${l} = 	Get Length	${interconnect_no}
	:FOR	${x}	IN RANGE	0	${l}
	\	@{interconnect_OA} =     GET SERIAL AND PART NUMBER FROM OA    ${OA_HOST}    ${OA_USER}    ${OA_PASS}     ${interconnect_no[${x}]}
	\	@{interconnect_rest} =     GET SERIAL AND PART NUMBER FROM REST    ${ENC1}, interconnect ${interconnect_no[${x}]}
	\	Run Keyword If    '${interconnect_OA[0]}' == '${interconnect_rest[0]}'    Log to Console and logfile    Serial Number is same in OA and Appliance    ELSE    FAIL    Log to Console    Serial Number is different
	\	Run Keyword If    '${interconnect_OA[1]}' == '${interconnect_rest[1]}'    Log to Console and logfile    Part Number is same in OA and Appliance    ELSE    FAIL    Log to Console    Part Number is different

######## Verify that the Hill, HP VC 16Gb 24-Port FC Module displays correctly in OV (LI and LIG)######

5. Verify the presence of HILL in LI
	${resp} =	Fusion Api Get Li
	${members_resp} =     Get From Dictionary     ${resp}    members
	${interconnect_uris} =     Get From Dictionary     ${resp['members'][0]}	interconnects
	${len} =	Get Length	${interconnect_uris}
	${resp} =	Get IC State
	${len} = 	Get Length	${resp}
	:FOR	${x}	IN RANGE	0	${len}
	\	Run Keyword If    '${resp[${x}]}' == 'Configured'    Log to console    \nThe Presence of HILL Module in LI is verified    Fail    "\n\nThe Hill Module is not present in LI"	
	
	
6. Verify the presence of HILL in LIG
	${resp} =	Fusion Api Get Lig
	Log to console and logfile    \nresp..${resp}	
	${icMapEntry} =     Get From Dictionary     ${resp['members'][0]['interconnectMapTemplate']}	interconnectMapEntryTemplates
	${mapEntrylist} =    Create List
	${len} = 	Get Length    ${icMapEntry}
	Log to console and logfile    \len..${len}	
	:FOR	${x}	IN RANGE	0	${len}
    \   ${mapEntry} =     Get From List   ${icMapEntry}    ${x}
	\   Append to list      ${mapEntrylist}  ${mapEntry['permittedInterconnectTypeUri']}
	Log to console and logfile    \mapEntrylist..${mapEntrylist}
	${ICtype_Names} =	Create List
	Log to console and logfile    \nICtype_Names..${ICtype_Names}
	:FOR	${y}	IN    @{mapEntrylist}
	
	\	Log to console and logfile    \nURI..${y}
	\	${string} =    Fetch From Right    ${y}    /
	\	${param} =	Catenate	SEPARATOR=	/	${string}
	\	${IC_Details} =    Fusion Api Get Interconnect Types    param=${param}
	
	\	Log to console and logfile    \nIC_Details..${IC_Details}
	\	Run Keyword If    '${IC_Details['name']}' != '${Module_name}'	Continue For Loop	
	\	Append To List    ${ICtype_Names}    ${IC_Details['name']}
	Log to console and logfile    \n${ICtype_Names}	
	${len} = 	Get Length    ${ICtype_Names}
	Run Keyword If    ${len} != 0	Log to console    \nHill Module is Present in LIG	Fail    "Hill Module is not Present in LIG"
	
###Proceeding with cleanup###
7. TEARDOWN
	${encs} = 	Fusion Api Get Enclosures
	${resp}		fusion API Remove Enclosure		uri=${encs['members'][0]['uri']}
	${task} =	Wait For Task1 	${resp}	
	${resp}=	fusion api delete enclosure group		name=${enc_group_hill['name']}
	Run keyword unless	${resp['status_code']}== 204	Fail	"Unable to delete the Enclosure Group"
	
	${resp}=	fusion api delete lig		name=${lig_hill['name']}
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete the LIG"
	
	${Response}     fusion api delete ethernet network		${enet_hill['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to delete FC network"
	
	${Response}     fusion api delete fc network		${fc1_hill[0]['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	
	${Response}     fusion api delete fc network		${fc2_hill[0]['name']}
	Run keyword unless	${Response['status_code']}== 202	Fail	"Unable to Delete FC network"
	Log to console and logfile    Test Suite SNMP for hill module completed successfully