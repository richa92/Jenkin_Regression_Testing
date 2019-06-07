*** Settings ***
Documentation		Verify network suite for Hill module
Library			json
Library			FusionLibrary
Library			RoboGalaxyLibrary
Library			OperatingSystem
Library			String
Variables		data_variables.py
Resource        resource.txt
 
 
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

 	
2.Create LIG, EG and import enclosure through API
	
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
####Configure DNS hostname on the Hill module####
#### Due to the Quix QXCR1001486841, We are not able to verify the hostname being displayed in the REST o/p. So we have verified by returning the serial number from REST O/P####
4. To check the hostname and modify it

	${host_oa} =    GET HOSTNAME FROM OA    ${OA_HOST}    ${OA_USER}    ${OA_PASS}    ${BAY}    ${INTERCONNECT_USER}    ${INTERCONNECT_PASS}
	@{host_rest} =    GET SERIAL AND PART NUMBER FROM REST    ${ENC1}, interconnect ${BAY}
	Run Keyword If    '${host_rest[2]}' == 'none'      Should Match Regexp     ${host_oa}    ${host_rest[0]}        ELSE    Run Keyword If    '${host_rest}' != 'none'      Should Be Equal As Strings    ${host_oa}    ${host_rest[2]}
	${modified_host} =    CHANGE HOSTNAME FROM OA    ${OA_HOST}    ${OA_USER}    ${OA_PASS}    ${BAY}    ${INTERCONNECT_USER}    ${INTERCONNECT_PASS}    ${hostname_manual}
	Run Keyword If    '${modified_host}' == '${hostname_manual}'    Log to Console and logfile    Hostname is same     ELSE    FAIL    Log to Console    Host name is different
	${modified_host1} =    CHANGE HOSTNAME FROM OA    ${OA_HOST}    ${OA_USER}    ${OA_PASS}    ${BAY}    ${INTERCONNECT_USER}    ${INTERCONNECT_PASS}    ${host_oa}
	Run Keyword If    '${modified_host1}' == '${host_oa}'    Log to Console and logfile    Hostname is reverted back     ELSE    FAIL    Log to Console    Host name is different

####Verify DHCP assigned IPv6 address####
####Verify assigning IPv6 address manually####
5. To verify ebipav6 address

	${len} = 	Get Length	${bay_no}
	:FOR    ${x}	IN RANGE    0    ${len}
	\   DISABLE EBIPAV6    ${OA_HOST}    ${OA_USER}    ${OA_PASS}    ${bay_no[${x}]}
	\	${ip_return_1} =    SHOW INTERCONNECT EBIPAV6    ${OA_HOST}    ${OA_USER}    ${OA_PASS}    ${bay_no[${x}]}
	\   ${ip_return_2} =    Get interconnect ip    ${ENC1}, interconnect ${bay_no[${x}]}    IPV6
	\	@{verify_ip} =    Split String    ${ip_return_1}    /
	\	${IP_APP_NO_EBIPA_1} =    Run Keyword If    '${verify_ip[0]}' == '${ip_return_2}'    Set Variable    ${ip_return_1}
	\	@{ip_to_change} =    Split String    ${ip_return_1}    :
	\   Set List Value    ${ip_to_change}    0    fd11
	\	${my_ip}=    Catenate    SEPARATOR=:    @{ip_to_change}
	\	SET EBIPAV6    ${OA_HOST}    ${OA_USER}    ${OA_PASS}    ${bay_no[${x}]}    ${my_ip}
	\	ENABLE EBIPAV6    ${OA_HOST}    ${OA_USER}    ${OA_PASS}    ${bay_no[${x}]}
	\	${ip_return_3} =    SHOW INTERCONNECT EBIPAV6    ${OA_HOST}    ${OA_USER}    ${OA_PASS}    ${bay_no[${x}]}
	\   ${ip_return_4} =    Get interconnect ip    ${ENC1}, interconnect ${bay_no[${x}]}    IPV6
	\	@{verify_ip_with_ebipa} =    Split String    ${ip_return_3}    /
	\	${IP_APP_WITH_EBIPA} =    Run Keyword If    '${verify_ip_with_ebipa[0]}' == '${ip_return_4}'    Set Variable    ${ip_return_3}
	\	Run Keyword If    '${my_ip}' == '${IP_APP_WITH_EBIPA}'    Log to Console and logfile    Able to set the EBIPAV6 address manually    ELSE    Log to Console    Not Changed
	\   DISABLE EBIPAV6    ${OA_HOST}    ${OA_USER}    ${OA_PASS}    ${bay_no[${x}]}
	\	${ip_return_5} =    SHOW INTERCONNECT EBIPAV6    ${OA_HOST}    ${OA_USER}    ${OA_PASS}    ${bay_no[${x}]}
	\   ${ip_return_6} =    Get interconnect ip    ${ENC1}, interconnect ${bay_no[${x}]}    IPV6
	\	@{verify_ip_no_ebipa} =    Split String    ${ip_return_5}    /
	\	${IP_APP_NO_EBIPA_2} =    Run Keyword If    '${verify_ip_no_ebipa[0]}' == '${ip_return_6}'    Set Variable    ${ip_return_5}
	\	Run Keyword If    '${IP_APP_NO_EBIPA_1}' == '${IP_APP_NO_EBIPA_2}'    Log to Console and logfile    Able to revert back the EBIPAV6 address to DHCP    ELSE    FAIL
	
####Verify DHCP assigned IPv4 address####
####Verify assigning IPv4 address manually####
6. DHCP to Enclosure
    
	${l} = 	Get Length	${bay_no}
	:FOR	${x}	IN RANGE	0	${l}		
	
    \	${IP1}      Set Variable    ${manual_IP[${x}]}
	
    \	${one_group}=	SHOW INTERCONNECT     ${OA_HOST}    ${OA_USER}                         ${OA_PASS}    ${bay_no[${x}]}
	\	Log to console and logfile		\n ${one_group}
		
    \	SET EBIPA     ${OA_HOST}    ${OA_USER}                         ${OA_PASS}   ${IP1}  ${bay_no[${x}]}
	
	\	${one_group1}=	SHOW INTERCONNECT     ${OA_HOST}    ${OA_USER}                         ${OA_PASS}    ${bay_no[${x}]}
	\	Log to console and logfile		one_group1 ${one_group1}
	\	Should Match Regexp	${one_group1}	${IP1}
	
	\	Fusion Api Login Appliance	${APPLIANCE_IP}		${admin_credentials}
	\	${interconnectIP} =	Get interconnect ip		${ENC1}, interconnect ${bay_no[${x}]}   IPV4
	\	Log to console and logfile    interconnectIP ${interconnectIP}
	\	Should Match Regexp	${interconnectIP}	${IP1}
	
    \	DISABLE EBIPA     ${OA_HOST}    ${OA_USER}                         ${OA_PASS}	${bay_no[${x}]}
	
	\	${one_group3}=	SHOW INTERCONNECT     ${OA_HOST}    ${OA_USER}                         ${OA_PASS}    ${bay_no[${x}]}
	\	Log to console and logfile		${one_group3}
    \	Should Match Regexp	${one_group3}	${one_group}
	
	\	Fusion Api Login Appliance	${APPLIANCE_IP}		${admin_credentials}
	\	${interconnectIP2} =	Get interconnect ip		${ENC1}, interconnect ${bay_no[${x}]}   IPV4
	\	Log to console and logfile    interconnectIP ${interconnectIP2}
	\	Should Match Regexp	${interconnectIP2}	${one_group}
    \   Sleep 		${poweron_sleep_time}secs
	
7. Teardown (a) Cleanup

	${Login_response} =	Fusion Api Login Appliance    ${APPLIANCE_IP}        ${admin_credentials}
	${encs} = 	Fusion Api Get Enclosures
	${resp}		fusion API Remove Enclosure		uri=${encs['members'][0]['uri']}
	${task} =	Wait For Task1 	${resp}
	
	${resp}=	fusion api delete enclosure group		name=${enc_group_hill['name']}
	Run keyword unless	${resp['status_code']}== 204	Fail	"Unable to delete the Enclosure Group"
	
	${resp}=	fusion api delete lig		name=${lig_hill_new['name']}
	Run keyword unless	${resp['status_code']}== 202	Fail	"Unable to delete the Enclosure Group"