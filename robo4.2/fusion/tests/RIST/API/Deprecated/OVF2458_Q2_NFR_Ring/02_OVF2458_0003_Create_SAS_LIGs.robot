*** Settings ***
Documentation   Create SAS LIGs from the data in the variable file

Suite Setup       Fusion Api Login Appliance           ${APPLIANCE_IP}         ${admin_credentials}
Suite Teardown    Fusion Api Logout Appliance

Resource        ../../../../Resources/api/fusion_api_resource.txt

*** Test Cases ***
OVF2458 Create SAS LIGs
    [Documentation]    Create SAS LIGs
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log
   	${sas_ligs} =	   Get Variable Value	${sas_ligs}
	Run Keyword If     ${sas_ligs} is not ${null}	Run Keyword for Dict	${sas_ligs}   Add SAS LIG
    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

*** Keywords ***
Get Errors
    [Documentation]    Get Errors
    ${ERRORS} =        Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}