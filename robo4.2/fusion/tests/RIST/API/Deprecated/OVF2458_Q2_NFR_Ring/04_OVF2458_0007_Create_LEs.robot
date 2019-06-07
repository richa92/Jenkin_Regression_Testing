*** Settings ***
Documentation   Create LEs from the data in the variable file

Suite Setup       Fusion Api Login Appliance           ${APPLIANCE_IP}         ${admin_credentials}
Suite Teardown    Fusion Api Logout Appliance

Resource        ../../../../Resources/api/fusion_api_resource.txt

*** Test Cases ***
OVF2458 Create LEs
    [Documentation]    Create LEs
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log
    [Tags]    Performance    logical_enclosures-condition-3encl
	${les} =	       Get Variable Value	${les}
    ${task} =          Add Logical Enclosure from variable     ${les['${LE1}']}
    ${resp} =  	       Fusion Api Get Logical Enclosure 	param=?filter="'name'=='${LE1}'"
	${resp} =          Get From List   ${resp['members']}	0
    Should Be Equal As Strings	${resp['status']}	OK
    Should Be Equal As Strings	${resp['state']}	Consistent
    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

*** Keywords ***
Get Errors
    [Documentation]    Get Errors
    ${ERRORS} =        Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}