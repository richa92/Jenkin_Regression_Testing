*** Settings ***
Documentation   Create LIGs from the data in the variable file

Suite Setup       Fusion Api Login Appliance           ${APPLIANCE_IP}         ${admin_credentials}
Suite Teardown    Fusion Api Logout Appliance

Resource        ../../../../Resources/api/fusion_api_resource.txt

*** Test Cases ***
OVF2458 Create LIGs
    [Documentation]    Create LIGs
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log

    #   If executed via __init__.robot, will be logged in thus don't login again.
    ${active} =    Run Keyword and Return Status    Fusion Api Get Active User
    Run Keyword if    '${active}'=='False'    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

   	${ligs} =	       Get Variable Value	${ligs}
	Run Keyword If     ${ligs} is not ${null}	Run Keyword for Dict	    ${ligs}       Add LIG from variable
    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

*** Keywords ***
Get Errors
    [Documentation]    Get Errors
    ${ERRORS} =        Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}
    [Return]           ${ERRORS}