*** Settings ***
Documentation   Create EGs from the data in the variable file

Suite Setup       Fusion Api Login Appliance           ${APPLIANCE_IP}         ${admin_credentials}
Suite Teardown    Fusion Api Logout Appliance

Resource        ../../../../Resources/api/fusion_api_resource.txt

*** Test Cases ***
OVF2458 Create EGs
    [Documentation]    Create EGs
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log
	${enc_groups} =    Get Variable Value	${enc_groups}
	Run Keyword If     ${enc_groups} is not ${null}	Run Keyword for Dict	${enc_groups}	Add Enclosure Group from variable
    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

*** Keywords ***
Get Errors
    [Documentation]    Get Errors
    ${ERRORS} =        Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}