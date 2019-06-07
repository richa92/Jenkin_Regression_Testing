*** Settings ***
Documentation   Create Server Profiles from Server Profile Templates from the data in the variable file

Suite Setup       Fusion Api Login Appliance           ${APPLIANCE_IP}         ${admin_credentials}
Suite Teardown    Fusion Api Logout Appliance

Resource        ../../../../Resources/api/fusion_api_resource.txt

*** Test Cases ***
OVF2458 Remove All Custom Address Ranges
    [Documentation]     Remove any existing Custom Address ranges.
    [Setup]             Run Keyword and Ignore Error    Write To ciDebug Log
	${pools} =  Create List		/rest/id-pools/vmac	/rest/id-pools/vwwn	/rest/id-pools/vsn
    Run Keyword for List	${pools}	Remove Custom Range
    [Teardown]    Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

OVF2458 Create Custom Address Ranges
    [Documentation]     Disable Generated Address Ranges and Create Custom Address ranges.
    [Setup]             Run Keyword and Ignore Error    Write To ciDebug Log
	${ranges} =	Get Variable Value	${ranges}
	${pools} =  Run Keyword If	${ranges} is not ${null}	Create List		/rest/id-pools/vmac	/rest/id-pools/vwwn	/rest/id-pools/vsn
    Run Keyword If	${ranges} is not ${null}                Run Keyword for List	${pools}	Disable ALL Generated ID Ranges
	Run Keyword If	${ranges} is not ${null}				Add Ranges From variable	${ranges}
	[Teardown]    Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

OVF2458 Create Server Profiles from Server Profile Templates
    [Documentation]     Create Server Profiles from Server Profile Templates
    [Setup]             Run Keyword and Ignore Error    Write To ciDebug Log
	${sp_from_spts} =	Get Variable Value	${sp_from_spts}
	${items} =          Get Dictionary Items    ${sp_from_spts}
	:FOR	${key}   ${value}	IN 	@{items}
	\	Run Keyword		Create SP from SPT    ${key}   ${value}
    [Teardown]    Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

*** Keywords ***
Create SP from SPT
    [Documentation]     Creates a new server profile named <spname> from SPT named <sptname>
    [Arguments]         ${spname}   ${sptname}    ${timeout}=10m   ${interval}=20s
    ${spt_uri} =        Common URI lookup by name     SPT:${sptname}
    ${resp} =           Fusion Api Get Server Profile Template New Profile  ${spt_uri}
    remove from dictionary  ${resp}  status_code   headers
	set to dictionary       ${resp}  name   ${spname}
	${resp} =           fusion api create server profile    body=${resp}
	${task} =	        Wait For Task 	${resp}   ${timeout}   ${interval}
    Should Match Regexp   ${task['taskState']}	 ((?i)Warning|Completed)
    [Return]   ${resp}

Get Errors
    [Documentation]    Get Errors
    ${ERRORS} =         Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}
