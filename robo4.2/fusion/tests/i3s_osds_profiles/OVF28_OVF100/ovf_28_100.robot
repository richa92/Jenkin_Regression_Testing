*** Settings ***
Documentation     OVF1136: [os-deployment-plans] Category supports Scope and SBAC
...               [server-profiles] [os-deployment-plans] Association supports SBAC

Resource          resources.robot
Suite Setup       Setup Environment
Test Setup        Login To Appliance And Verify Oneview Prerequisites    ${appliance_ip}    ${admin_credentials}
# Test Teardown     OVF28_100 Test Teardown


*** Test Cases ***
OVTC53148
    [Documentation]    Tao SBAC Operation
    [Tags]    OVF28_OVF100_TC01
    Create scopes to test OSBP SBAC    ${OVF28_OVF100_TC01}

OVTC53149
    [Documentation]    Tao SBAC Operation
    [Tags]    OVF28_OVF100_TC02
    Create scopes to test OSBP SBAC    ${OVF28_OVF100_TC02}

OVTC53150
    [Documentation]    Tao SBAC Operation
    [Tags]    OVF28_OVF100_TC03

    Create scopes to test OSBP SBAC    ${OVF28_OVF100_TC03}

OVTC53151
    [Documentation]    Tao SBAC Operation
    [Tags]    OVF28_OVF100_TC04

    Create scopes to test OSBP SBAC    ${OVF28_OVF100_TC04}

OVTC53152
    [Documentation]    Tao SBAC Operation
    [Tags]    OVF28_OVF100_TC05

    Create scopes to test OSBP SBAC    ${OVF28_OVF100_TC05}

OVTC53153
    [Documentation]    Creating a user & associating one SCOPE
    [Tags]    OVF28_OVF100_TC06

    Create scopes to test OSBP SBAC    ${OVF28_OVF100_TC06}
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    ${uri}=    Get Scope URI By Name    ${OVF28_OVF100_TC06_01[0]['permissions'][0]['scopeUri']}
    Run keyword if    '${uri}'!='None'    Set to dictionary    ${OVF28_OVF100_TC06_01[0]['permissions'][0]}    scopeUri    ${uri}
    Add Users from variable    ${OVF28_OVF100_TC06_01}
    Fusion Api Logout Appliance

OVTC53154
    [Documentation]    Creating a user & associating multiple SCOPE
    [Tags]    OVF28_OVF100_TC07

    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Add Users from variable    ${OVF28_OVF100_TC07_02}
    :FOR    ${scope}    in    @{OVF28_OVF100_TC07_01}
    \    ${resp} =   Fusion Api Create Scope     ${scope}
    \    Run Keyword If  '${resp['status_code']}' != '202'   Fail    ${resp}    ELSE  log to console  \n-${scope['name']} : Scope Created successfully!
    Fusion Api Logout Appliance

OVTC53155
    [Documentation]    Creating a user & associating multiple SCOPE
    [Tags]    OVF28_OVF100_TC08

    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    :FOR    ${scope}    in    @{OVF28_OVF100_TC08_01}
    \    ${resp} =   Fusion Api Create Scope     ${scope}
    \    Run Keyword If  '${resp['status_code']}' != '202'   Fail    ${resp}    ELSE  log to console  \n-${scope['name']} : Scope Created successfully!
    Add Users from variable    ${OVF28_OVF100_TC08_02}
    :FOR    ${sc}    in    @{OVF28_OVF100_TC08_03}
    \    Update Users    ${sc}
    Fusion Api Logout Appliance

OVTC53156
    [Documentation]    Create a ready-only user and associate a scope
    [Tags]    OVF28_OVF100_TC09

    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    ${resp} =   Fusion Api Create Scope     ${OVF28_OVF100_TC09_01[0]}
    Run Keyword If  '${resp['status_code']}' != '202'   Fail	${resp}    ELSE  log to console  \n-${OVF28_OVF100_TC09_01[0]['name']} : Scope Created successfully!
    Add Users from variable    ${OVF28_OVF100_TC09_02}
    Update Users    ${OVF28_OVF100_TC09_03}
    Fusion Api Logout Appliance

OVTC53157
    [Documentation]    Check for Scope related info on server profile page
    [Tags]    OVF28_OVF100_TC10

    Create scopes and server profiles    ${OVF28_OVF100_TC10_01}    ${OVF28_OVF100_TC10_02}    ${OVF28_OVF100_TC10_03}    ${OVF28_OVF100_TC10_04}    ${OVF28_OVF100_TC10_05}

OVTC53158
    [Documentation]    Check for Scope related info on server profile page
    [Tags]    OVF28_OVF100_TC11

    Create scopes and server profiles    ${OVF28_OVF100_TC11_01}    ${OVF28_OVF100_TC11_02}    ${OVF28_OVF100_TC11_03}    ${OVF28_OVF100_TC11_04}    ${OVF28_OVF100_TC11_05}

OVTC53159
    [Documentation]    Create a Server profile with one scope
    [Tags]    OVF28_OVF100_TC12

    Create scopes and server profiles    ${OVF28_OVF100_TC12_01}    ${OVF28_OVF100_TC12_02}    ${OVF28_OVF100_TC12_03}    ${OVF28_OVF100_TC12_04}    ${OVF28_OVF100_TC12_05}    ${OVF28_OVF100_TC12_06}

OVTC53160
    [Documentation]    Create a Server profile with multiple scope
    [Tags]    OVF28_OVF100_TC13

    Create scopes and server profiles    ${OVF28_OVF100_TC13_01}    ${OVF28_OVF100_TC13_02}    ${OVF28_OVF100_TC13_03}    ${OVF28_OVF100_TC13_04}    ${OVF28_OVF100_TC13_05}    ${OVF28_OVF100_TC13_06}

OVTC53161
    [Documentation]    Delete a Server profile associated a scope
    [Tags]    OVF28_OVF100_TC14

    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC14_01}
    ${uri}=    Get Scope URI By Name    ${OVF28_OVF100_TC14_02[0]['permissions'][0]['scopeUri']}
    Run keyword if    '${uri}'!='None'    Set to dictionary    ${OVF28_OVF100_TC14_02[0]['permissions'][0]}    scopeUri    ${uri}
    Add Users from variable    ${OVF28_OVF100_TC14_02}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC14_03}
    Power off Server    ${OVF28_OVF100_TC14_04[0]['serverHardwareUri']}
    ${sc_uri}=    Get Scope URI By Name    ${OVF28_OVF100_TC14_02[0]['permissions'][0]['scopeUri']}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC14_04}
    Power off Server    ${OVF28_OVF100_TC14_04[0]['serverHardwareUri']}
    Deployment servers SBAC Delete SP and check existence    ${OVF28_OVF100_TC14_04}
    Fusion Api Logout Appliance

OVTC53162
    [Documentation]    Access server profile as a read-only scope user
    [Tags]    OVF28_OVF100_TC15

    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC15_01}
    :FOR    ${in}    in    @{OVF28_OVF100_TC15_02}
    \    ${uri}=    Get Scope URI By Name    ${in['permissions'][0]['scopeUri']}
    \    Run keyword if    '${uri}'!='None'    Set to dictionary    ${in['permissions'][0]}    scopeUri    ${uri}
    Add Users from variable    ${OVF28_OVF100_TC15_02}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC15_05}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC15_04}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC15_03}
    :FOR    ${s}    in    @{OVF28_OVF100_TC15_04}
    \    ${res}=    Remove Server Profile    ${s}
    \    Run keyword if    '${res['status_code']}'!='403' or '${res['status_code']}'=='202'    FAIL    Invalid delete by User with read only permission
    Fusion Api Logout Appliance

OVTC53163
    [Documentation]    Updating a Server profile with IA or server admin scope user
    [Tags]    OVF28_OVF100_TC16

    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC16_01}
    :FOR    ${server}    in    @{OVF28_OVF100_TC16_06[0]['addedResourceUris']}
    \    Power off Server    ${server}
    Build body and update scope    ${OVF28_OVF100_TC16_06[0]['name']}    ${OVF28_OVF100_TC16_06[0]['addedResourceUris']}    ${OVF28_OVF100_TC16_06[0]['removedResourceUris']}
    ${uri}=    Get Scope URI By Name    ${OVF28_OVF100_TC16_02[0]['permissions'][0]['scopeUri']}
    Run keyword if    '${uri}'!='None'    Set to dictionary    ${OVF28_OVF100_TC16_02[0]['permissions'][0]}    scopeUri    ${uri}
    Add Users from variable    ${OVF28_OVF100_TC16_02}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC16_03}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC16_04}
    ${resp}=    Edit Server Profiles from variable    ${OVF28_OVF100_TC16_05}
    ${task_resp}=    Run Keyword If	${resp[0]['status_code']}==202    Wait For Task    ${resp[0]}    3600s    20s
    Fusion Api Logout Appliance

OVTC53164
    [Documentation]    Updating a Server profile with IA or server admin scope user
    [Tags]    OVF28_OVF100_TC17

    Create scopes and server profiles    ${OVF28_OVF100_TC17_01}    ${OVF28_OVF100_TC17_02}    ${OVF28_OVF100_TC17_03}    ${OVF28_OVF100_TC17_04}    ${OVF28_OVF100_TC17_05}
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC17_04}
    ${resp}=    Edit Server Profiles from variable    ${OVF28_OVF100_TC17_06}
    ${task_resp}=    Run Keyword If    ${resp[0]['status_code']}==202    Wait For Task2    ${resp}    3600    20
    Fusion Api Logout Appliance

OVTC53165
    [Documentation]    Updating a Server profile with IA or server admin scope user
    [Tags]    OVF28_OVF100_TC18

    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC18_01}
    Populate scope Uri for user payload    ${OVF28_OVF100_TC18_02}
    Add Users from variable    ${OVF28_OVF100_TC18_02}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC18_03}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC18_04}
    ${resp}=    Edit Server Profiles from variable    ${OVF28_OVF100_TC18_05}
    ${task_resp}=    Run Keyword If    ${resp[0]['status_code']}==202    Wait For Task    ${resp[0]}    3600s    20s
    Update User    ${OVF28_OVF100_TC18_06}
    ${resp}=    Edit Server Profiles from variable    ${OVF28_OVF100_TC18_05}
    ${task_resp}=    Run Keyword If	${resp[0]['status_code']}==202    Wait For Task    ${resp[0]}    3600s    20s
    Fusion Api Logout Appliance

OVTC53166
    [Documentation]    Try to delete a scope while associated to a user
    [Tags]    OVF28_OVF100_TC19

    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC19_01}
    Populate scope Uri for user payload    ${OVF28_OVF100_TC19_02}
    Add Users from variable    ${OVF28_OVF100_TC19_02}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    ${r}=    Run keyword and ignore error    Remove Scope By Name    ${OVF28_OVF100_TC19_01[0]['name']}
    Run keyword if    '${r[0]}'=='PASS'    FAIL
    Fusion Api Logout Appliance

OVTC53167
    [Documentation]    Update a user with multiple scope to single scope
    [Tags]    OVF28_OVF100_TC20

    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC20_01}
    Populate scope Uri for user payload    ${OVF28_OVF100_TC20_02}
    Add Users from variable    ${OVF28_OVF100_TC20_02}
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

OVTC53168
    [Documentation]    Delete scope & check the scope association with server profile
    [Tags]    OVF28_OVF100_TC21

    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC21_01}
    Populate scope Uri for user payload    ${OVF28_OVF100_TC21_02}
    Add Users from variable    ${OVF28_OVF100_TC21_02}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC21_04}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC21_03}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    ${r} =     Fusion Api Get User    param=${OVF28_OVF100_TC21_04['userName']}
    Fusion Api Remove User    uri=${r['uri']}
    :FOR    ${i}    in    @{OVF28_OVF100_TC21_01}
    \    Remove Scope By Name    ${i['name']}
    ${sp_uri}=    Get Server Profile URI    ${OVF28_OVF100_TC21_03[0]['name']}
    Validate Resource Not Assign To Any Scope    ${sp_uri}
    Fusion Api Logout Appliance

OVTC53169
    [Documentation]    Create scope as a scope administrator
    [Tags]    OVF28_OVF100_TC22

    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Add Users from variable    ${OVF28_OVF100_TC22_01}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance    ${appliance_ip}    ${OVF28_OVF100_TC22_02}
    :FOR    ${in}    in    @{OVF28_OVF100_TC22_03}
    \    ${res}=    Populate resources in scope body    ${in}
    \    ${resp} =   Fusion Api Create Scope     ${res}
    \    Run Keyword If  '${resp['status_code']}' != '202'   Fail	${resp}    ELSE  log to console  \n-${in['name']} : Scope Created successfully!
    Fusion Api Logout Appliance

OVTC53170
    [Documentation]    Multiple users having access to common scope
    [Tags]    OVF28_OVF100_TC23

    Fusion Api Login Appliance  ${appliance_ip}     ${admin_credentials}
    Deployment servers SBAC Create scope    ${OVF28_OVF100_TC23_01}
    Populate scope Uri for user payload    ${OVF28_OVF100_TC23_02}
    Add Users from variable    ${OVF28_OVF100_TC23_02}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC23_06}
    Deployment servers SBAC Add SP and check existence    ${OVF28_OVF100_TC23_07}
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC23_04}
    Remove Server Profile    ${OVF28_OVF100_TC23_07[0]}
    sleep    20 seconds
    Fusion Api Logout Appliance
    Fusion Api Login Appliance  ${appliance_ip}     ${OVF28_OVF100_TC23_05}
    ${resp}=    Edit Server Profiles from variable    ${OVF28_OVF100_TC23_08}
    ${task_resp}=    Run Keyword If	${resp[0]['status_code']}==202    Wait For Task    ${resp[0]}    3600s    20s
    Fusion Api Logout Appliance

OVTC54192
    [Documentation]    OVF28_OVF100 teardown
    Remove All Users
    Remove All Scopes
