*** Settings ***
Documentation   Create Server Profile Templates from the data in the variable file

Suite Setup       Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
Suite Teardown    Fusion Api Logout Appliance

Resource        ../../../../Resources/api/fusion_api_resource.txt

*** Test Cases ***
OVF2458 Create SPTs 480_1 and 660_1 RAID 1 4/8 drives respectively
    [Documentation]    Create Server Profile Templates
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log
	${spts} =	       Get Variable Value	${spts}
	${resplist} =      Run Keyword If	${spts} is not ${null}   Run Keyword for Dict    ${spts}   Add Server Profile Template
	${resp} =          Run Keyword for List   ${resplist}   Wait for Task
    [Teardown]         Run Keyword If    '${TEST_STATUS}'=='FAIL'   Get Errors

*** Keywords ***
Get Errors
    [Documentation]    Get Errors
    ${ERRORS} =        Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}
