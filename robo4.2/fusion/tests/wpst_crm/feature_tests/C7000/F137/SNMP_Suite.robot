*** Settings ***
Documentation		 Verify SNMP scenario on Hill module.
Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary
Library			OperatingSystem
Library			String
Library			OACommand
Variables		data_variables.py
Resource        resource.txt

Suite Setup    Cleanup For Suite
Suite Teardown    Cleanup For Suite

*** Test Cases ***
###Pre-Conditions - Create LIG, EG, and import enclosure###
1.Create SessionID through API
	Set Log Level    TRACE
    ${Login_response} =    Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	Run keyword unless	${Login_response[0]['status_code']}== 200	Fail	"Unable to Login"
	Precheck for IC in OA
	Log to console and logfile    Test Step-1 completed successfully

2.Create Networks, LIG, EG and import enclosure through API
	${Response_enet}     fusion api create ethernet network		${enet_hill}
	Run keyword unless	${Response_enet['status_code']}== 202	Fail	"Unable to Create Ethernet network"
	${Response_fc1}     Add FC Networks from variable    ${fc1_hill}
	Run keyword unless	${Response_fc1['status_code']}== 202	Fail	"Unable to Create FC network"
	${Response_fc2}     Add FC Networks from variable    ${fc2_hill}
	Run keyword unless	${Response_fc2['status_code']}== 202	Fail	"Unable to Create FC network"
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
	
###Pre-Conditions steps over###

###Proceeding with NETWORK-2 test case###

#This test case is to verify SNMPv1 configuration on Hill module.
2A.Verifying the SNMP status is disabled in IC
	${IC_IP}=    SHOW INTERCONNECT    ${OA_HOST}    ${OA_USER}    ${OA_PASS}    ${BAY}
	Log to Console		\n${IC_IP}
	Set Global Variable    ${Hill_IP}    ${IC_IP}
	@{output}=	get_trap_from_interconnects	${Hill_IP}	${Hill_Bay_Username}	${Hill_Bay_Password}	${IC_Command}    ${SNMP_Match}
	Log to Console		\n${output}
	List Should Contain Value    ${output}    SNMPv1:Disabled
	Log to Console		\nVerified the SNMPv1 configuration is disabled.
	
2B.Editing the LIG to enable SNMP configuration on Hill module.
	${body_new} =   Build LIG body      ${lig_hill_new}    
	${resp_lig} = 	Fusion Api Edit Lig    ${body_new}    ${lig_uri}
	Run keyword unless	${resp_lig['status_code']}== 202	Fail	"Unable to Edit LIG"
	${task} =	Wait For Task 	${resp_lig} 	120s	2s
	Log to console and logfile    LIG edited successfully
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	Perform an LI Update From Group    ${li_uri}
	
2C.Verifying the SNMP status is enabled in IC
	@{output}=	get_trap_from_interconnects	${Hill_IP}	${Hill_Bay_Username}	${Hill_Bay_Password}	${IC_Command}    ${SNMP_Match}
	Log to Console		\n${output}
	List Should Contain Value    ${output}    SNMPv1:Enabled
	Log to Console		\nVerified the SNMPv1 configuration is enabled.
	Log to console and logfile    \nTest Case Network-2 completed successfully
	
###Proceeding with NETWORK-3 test case###

#This test case is to Verify adding SNMPv1 trap.
3A.Verify adding SNMPv1 trap.
	@{output}=	get_trap_from_interconnects	${Hill_IP}	${Hill_Bay_Username}	${Hill_Bay_Password}	${IC_Command}    ${IC_Match}
	Log to Console		\n${output}
	List Should Contain Value    ${output}    Trap recipient: ${SSH_SNMP_IP}
	Log to Console		\n${SSH_SNMP_IP} is found as the trap destination
	Log to console and logfile    \nTest Case Network-3 completed successfully
	
###Proceeding with NETWORK-4 test case###

#This test case is to Verify generating SNMPv1 trap.
4A.Clearing Old Trapsin SNMP client
	Open SNMP Client and Login    ${SSH_SNMP_IP}
	Clear Trap
	Log to console and logfile    \nTraps cleared
	OperatingSystem.Remove File    ${Trap_File_Name}
	Log to console and logfile    Test step-2 completed successfully
	
4B.Restarting Interconnect, Disabling and enabling ports
	OA CLI Restart Interconnect    ${OA_HOST}    ${OA_USER}    ${OA_PASS}    ${BAY}
	Wait For Restarting Interconnect
	Log to console and logfile    \nInterconnect restarted
	
	${resp} = 	Fusion Api Get Interconnect  		param=?filter="'name' = '${interconnectname_2}'"
	${IC_uri} =    Get From Dictionary  ${resp['members'][0]}    uri 
	
	${Port_Id} =    Get From Dictionary  ${resp['members'][0]['ports'][0]}    portId
	Set to Dictionary	${Port_enable_body[0]}    portId	${Port_Id}
	Set to Dictionary	${Port_disable_body[0]}    portId	${Port_Id}
	
	${Port_Name} =    Get From Dictionary  ${resp['members'][0]['ports'][0]}    portName
	Set to Dictionary	${Port_enable_body[0]}    portName    ${Port_Name}
	Set to Dictionary	${Port_disable_body[0]}    portName    ${Port_Name}
	
	${Response}=    Fusion Api Edit Interconnect Ports    ${Port_disable_body}    ${IC_uri}
	Wait For Disabling Ports
	Log to console and logfile    \nPort disabled
	${Response}=    Fusion Api Edit Interconnect Ports    ${Port_enable_body}    ${IC_uri}
	Wait For Enabling Ports
	Log to console and logfile    \nPort enabled
	Log to console and logfile    Test Step-4B completed successfully
	
4C.Verifying traps in the SNMP client
	Get Remote files    ${SSH_SNMP_IP}    ${SNMP_UserName}    ${SNMP_Password}    ${QUERY}
	${contents}=    OperatingSystem.Get File    ${Trap_File_Name}
	${Lines_1}=    Get Lines Containing String    ${contents}    ${Port_status_trap_name}
	${Count_1}=    Get Line Count    ${Lines_1}
    Log to console and logfile    \n\nCount - ${Count_1}
    Run Keyword If    ${Count_1} > 0  log to console    ${Port_status_trap_name} is present    Else    Fail
	
	${Lines_2}=    Get Lines Containing String    ${contents}    ${IC_restart_trap_name}
	${Count_2}=    Get Line Count    ${Lines_2}
    Log to console and logfile    \n\nCount - ${Count_2}
    Run Keyword If    ${Count_1} > 0  log to console    ${IC_restart_trap_name} is present    Else    Fail
	Log to console and logfile    \nTest NETWORK-4 completed successfully
	
###Proceeding with NETWORK-9 test case###

#F137 - NETWORK.9 - Verify that the 6th SNMPv1 trap cannot be pushed to the module
9A.Editing LIG to add six trap destinations
	${body_new} =   Build LIG body      ${lig_hill_trap6}    
	${resp_lig} = 	Fusion Api Edit Lig    ${body_new}    ${lig_uri}
	Run keyword unless	${resp_lig['status_code']}== 202	Fail	"Unable to Edit LIG"
	${task} =	Wait For Task 	${resp_lig} 	120s	2s
	Log to console and logfile    LIG edited successfully
	${li_uri} = 	Get LI URI   ${LE}-${LIG1}
	Perform an LI Update From Group    ${li_uri}
	
9B.Verifying that the 6th SNMPv1 trap cannot be pushed to the module
	@{output}=	get_trap_from_interconnects	${Hill_IP}	${Hill_Bay_Username}	${Hill_Bay_Password}	${IC_Command}    ${IC_Match}
	Log to Console		\n${output}
	${Count}=    Set Variable    0
	Log to console and logfile		count is ${Count}
	:FOR	${index}    IN    @{Trap_Ips}
	\	${return}=    Run Keyword And Return Status    List Should Contain Value    ${output}    ${index}
	\	Run Keyword If    ${return} == False    Continue For Loop
	\	${Count}=    Evaluate	${Count}+1	
	Log to console and logfile		\n${Count}
	Run Keyword If    ${Count} == 5    Log to console and logfile    Verified 5 trap destinations are found	
	List Should Contain Value    ${output}    Trap recipient: 254.254.245.1
	Log to console and logfile    Verfied that the 6th SNMPv1 trap cannot be pushed to the module. 
	Log to console and logfile    \nTest NETWORK-9 completed successfully.
	
###Proceeding with cleanup###
TEARDOWN
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