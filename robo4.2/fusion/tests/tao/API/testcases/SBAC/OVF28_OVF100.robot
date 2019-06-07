*** Settings ***
Documentation	SBAC tests for I3S SBAC
Library			FusionLibrary
Library			RoboGalaxyLibrary
Library			OperatingSystem
Library			BuiltIn
Library			Collections
Library			XML
Library			String
Library			json
Library			Process

Resource						../../../../../Resources/api/fusion_api_resource.txt
Resource						../../../../clrm/support_files/clrm_common.txt
Variables 		    			../../data_variable_files/OVF28_OVF100_SBAC_data_variables.py
Resource						../../../../i3s/Resources/api/common.robot
Resource						../../Resources/resources.txt
Suite Setup                     Setup environment

*** Variables ***

${appliance_ip}		15.212.173.150


*** Test Cases ***

OVF28_OVF100_TC01
    [Documentation]    Tao SBAC Operation
    Create scopes to test OSBP SBAC    ${OVF28_OVF100_TC01}

OVF28_OVF100_TC02
    [Documentation]    Tao SBAC Operation
    Create scopes to test OSBP SBAC    ${OVF28_OVF100_TC02}

OVF28_OVF100_TC03
    [Documentation]    Tao SBAC Operation
    Create scopes to test OSBP SBAC    ${OVF28_OVF100_TC03}

OVF28_OVF100_TC04
    [Documentation]    Tao SBAC Operation
    Create scopes to test OSBP SBAC    ${OVF28_OVF100_TC04}

OVF28_OVF100_TC05
    [Documentation]    Tao SBAC Operation
    Create scopes to test OSBP SBAC    ${OVF28_OVF100_TC05}

OVF28_OVF100_TC06
    Create scopes to test OSBP SBAC    ${OVF28_OVF100_TC06}
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    ${uri}=    Get Scope URI By Name    ${OVF28_OVF100_TC06_01[0]['permissions'][0]['scopeUri']}
    Run keyword if    '${uri}'!='None'    Set to dictionary    ${OVF28_OVF100_TC06_01[0]['permissions'][0]}    scopeUri    ${uri}
    Add Users from variable    ${OVF28_OVF100_TC06_01}
    Fusion Api Logout Appliance

OVF28_OVF100_TC07
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Add Users from variable		${OVF28_OVF100_TC07_02}
	:FOR	${scope}	in    @{OVF28_OVF100_TC07_01}
	\	${resp} =   Fusion Api Create Scope     ${scope}
	\	Run Keyword If  '${resp['status_code']}' != '202'   Fail	${resp}    ELSE  log to console  \n-${scope['name']} : Scope Created successfully!
    Fusion Api Logout Appliance

OVF28_OVF100_TC08
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
	:FOR	${scope}	in    @{OVF28_OVF100_TC08_01}
	\	${resp} =   Fusion Api Create Scope     ${scope}
	\	Run Keyword If  '${resp['status_code']}' != '202'   Fail	${resp}    ELSE  log to console  \n-${scope['name']} : Scope Created successfully!
	Add Users from variable		${OVF28_OVF100_TC08_02}
	:FOR    ${sc}    in    @{OVF28_OVF100_TC08_03}
	\    Update Users    ${sc} 
    Fusion Api Logout Appliance

OVF28_OVF100_TC09
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    ${resp} =   Fusion Api Create Scope     ${OVF28_OVF100_TC09_01[0]}
    Run Keyword If  '${resp['status_code']}' != '202'   Fail	${resp}    ELSE  log to console  \n-${OVF28_OVF100_TC09_01[0]['name']} : Scope Created successfully!
    Add Users from variable		${OVF28_OVF100_TC09_02}
    Update Users    ${OVF28_OVF100_TC09_03}
    Fusion Api Logout Appliance

OVF28_OVF100_TC10
    Create scopes and server profiles    ${OVF28_OVF100_TC10_01}    ${OVF28_OVF100_TC10_02}    ${OVF28_OVF100_TC10_03}    ${OVF28_OVF100_TC10_04}    ${OVF28_OVF100_TC10_05}

OVF28_OVF100_TC11
    Create scopes and server profiles    ${OVF28_OVF100_TC11_01}    ${OVF28_OVF100_TC11_02}    ${OVF28_OVF100_TC11_03}    ${OVF28_OVF100_TC11_04}    ${OVF28_OVF100_TC11_05}

OVF28_OVF100_TC12
    Create scopes and server profiles    ${OVF28_OVF100_TC12_01}    ${OVF28_OVF100_TC12_02}    ${OVF28_OVF100_TC12_03}    ${OVF28_OVF100_TC12_04}    ${OVF28_OVF100_TC12_05}    ${OVF28_OVF100_TC12_06}

OVF28_OVF100_TC13
    Create scopes and server profiles    ${OVF28_OVF100_TC13_01}    ${OVF28_OVF100_TC13_02}    ${OVF28_OVF100_TC13_03}    ${OVF28_OVF100_TC13_04}    ${OVF28_OVF100_TC13_05}    ${OVF28_OVF100_TC13_06}

OVF28_OVF100_TC14
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC14_01}
    ${uri}=    Get Scope URI By Name    ${OVF28_OVF100_TC14_02[0]['permissions'][0]['scopeUri']}
    Run keyword if    '${uri}'!='None'    Set to dictionary    ${OVF28_OVF100_TC14_02[0]['permissions'][0]}    scopeUri    ${uri}
    Add Users from variable		${OVF28_OVF100_TC14_02}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC14_03}
    Power off Server    ${OVF28_OVF100_TC14_04[0]['serverHardwareUri']}
    ${sc_uri}=    Get Scope URI By Name    ${OVF28_OVF100_TC14_02[0]['permissions'][0]['scopeUri']}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC14_04}
    Power off Server    ${OVF28_OVF100_TC14_04[0]['serverHardwareUri']}
    Deployment servers SBAC Delete SP and check existence    ${OVF28_OVF100_TC14_04}
    Fusion Api Logout Appliance

OVF28_OVF100_TC15
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC15_01}
    :FOR    ${in}    in    @{OVF28_OVF100_TC15_02}
    \    ${uri}=    Get Scope URI By Name    ${in['permissions'][0]['scopeUri']}
    \    Run keyword if    '${uri}'!='None'    Set to dictionary    ${in['permissions'][0]}    scopeUri    ${uri}
    Add Users from variable		${OVF28_OVF100_TC15_02}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC15_05}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC15_04}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC15_03}
    :FOR    ${s}    in    @{OVF28_OVF100_TC15_04}
    \    ${res}=    Remove Server Profile    ${s}
    \    Run keyword if    '${res['status_code']}'!='403' or '${res['status_code']}'=='202'    FAIL    Invalid delete by User with read only permission
    Fusion Api Logout Appliance

OVF28_OVF100_TC16
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC16_01}
    :FOR    ${server}    in    @{OVF28_OVF100_TC16_06[0]['addedResourceUris']}
    \    Power off Server    ${server}
    Build body and update scope    ${OVF28_OVF100_TC16_06[0]['name']}    ${OVF28_OVF100_TC16_06[0]['addedResourceUris']}
    ${uri}=    Get Scope URI By Name    ${OVF28_OVF100_TC16_02[0]['permissions'][0]['scopeUri']}
    Run keyword if    '${uri}'!='None'    Set to dictionary    ${OVF28_OVF100_TC16_02[0]['permissions'][0]}    scopeUri    ${uri}
    Add Users from variable		${OVF28_OVF100_TC16_02}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC16_03}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC16_04}
    ${resp}=    Edit Server Profiles from variable    ${OVF28_OVF100_TC16_05}
    ${task_resp}=	Run Keyword If	${resp[0]['status_code']}==202		Wait For Task	${resp[0]}	3600s	20s
    Fusion Api Logout Appliance

OVF28_OVF100_TC17
    Create scopes and server profiles    ${OVF28_OVF100_TC17_01}    ${OVF28_OVF100_TC17_02}    ${OVF28_OVF100_TC17_03}    ${OVF28_OVF100_TC17_04}    ${OVF28_OVF100_TC17_05}
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC17_04}
    ${resp}=    Edit Server Profiles from variable    ${OVF28_OVF100_TC17_06}
    ${task_resp}=	Run Keyword If	${resp[0]['status_code']}==202    Wait For Task2	${resp[0]}	3600	20
    Fusion Api Logout Appliance

OVF28_OVF100_TC18
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC18_01}
    Populate scope Uri for user payload    ${OVF28_OVF100_TC18_02}
    Add Users from variable		${OVF28_OVF100_TC18_02}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC18_03}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC18_04}
    ${resp}=    Edit Server Profiles from variable    ${OVF28_OVF100_TC18_05}
    ${task_resp}=	Run Keyword If	${resp[0]['status_code']}==202		Wait For Task	${resp[0]}	3600s	20s
    Run Keyword If	${resp[0]['status_code']}==202    FAIL
    Update User    ${OVF28_OVF100_TC18_06}
    ${resp}=    Edit Server Profiles from variable    ${OVF28_OVF100_TC18_05}
    ${task_resp}=	Run Keyword If	${resp[0]['status_code']}==202		Wait For Task	${resp[0]}	3600s	20s
    Fusion Api Logout Appliance

OVF28_OVF100_TC19
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC19_01}
    Populate scope Uri for user payload    ${OVF28_OVF100_TC19_02}
    Add Users from variable		${OVF28_OVF100_TC19_02}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    ${r}=    Run keyword and ignore error    Remove Scope By Name    ${OVF28_OVF100_TC19_01[0]['name']}
    Run keyword if    '${r[0]}'=='PASS'    FAIL
    Fusion Api Logout Appliance

OVF28_OVF100_TC20
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC20_01}
    Populate scope Uri for user payload    ${OVF28_OVF100_TC20_02}
    Add Users from variable		${OVF28_OVF100_TC20_02}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance    ${appliance_ip}     ${OVF28_OVF100_TC20_05}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC20_03}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    :FOR    ${sc}    in    @{OVF28_OVF100_TC20_04}
	\    Update Users    ${sc}
	Fusion Api Logout Appliance
	Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC20_05}
    ${s_uri}=    Get Scope URI By Name    ${OVF28_OVF100_TC20_01[1]['name']}
    ${sp_uri}=    Get Server Profile URI    ${OVF28_OVF100_TC20_03[0]['name']}
    Validate Resource Assign To Scope    ${s_uri}    ${sp_uri}
    Fusion Api Logout Appliance

OVF28_OVF100_TC21
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC21_01}
    Populate scope Uri for user payload    ${OVF28_OVF100_TC21_02}
    Add Users from variable		${OVF28_OVF100_TC21_02}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC21_04}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC21_03}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    ${r} = 	Fusion Api Get User    param=${OVF28_OVF100_TC21_04['userName']}
    Fusion Api Remove User		uri=${r['uri']}
    :FOR    ${i}    in    @{OVF28_OVF100_TC21_01}
    \    Remove Scope By Name    ${i['name']}
    ${sp_uri}=    Get Server Profile URI    ${OVF28_OVF100_TC21_03[0]['name']}
    Validate Resource Not Assign To Any Scope    ${sp_uri}
    Fusion Api Logout Appliance

OVF28_OVF100_TC22
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Add Users from variable		${OVF28_OVF100_TC22_01}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance 		${appliance_ip}		${OVF28_OVF100_TC22_02}
    :FOR	${in}	in    @{OVF28_OVF100_TC22_03}
    \    ${res}=    Populate resources in scope body    ${in}
    \    ${resp} =   Fusion Api Create Scope     ${res}
    \    Run Keyword If  '${resp['status_code']}' != '202'   Fail	${resp}    ELSE  log to console  \n-${in['name']} : Scope Created successfully!
    Fusion Api Logout Appliance

OVF28_OVF100_TC23
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC23_01}
    Populate scope Uri for user payload    ${OVF28_OVF100_TC23_02}
    Add Users from variable		${OVF28_OVF100_TC23_02}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC23_06}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC23_07}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC23_04}
    Remove Server Profile    ${OVF28_OVF100_TC23_07[0]}
    sleep    20 seconds
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC23_05}
    ${resp}=    Edit Server Profiles from variable    ${OVF28_OVF100_TC23_08}
    ${task_resp}=	Run Keyword If	${resp[0]['status_code']}==202		Wait For Task	${resp[0]}	3600s	20s
    Fusion Api Logout Appliance
