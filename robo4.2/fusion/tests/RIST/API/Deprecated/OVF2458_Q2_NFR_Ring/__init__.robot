*** Settings ***
Documentation		OVF2458 Q2 NFR Mini-scale
...   Q2 NFR Mini-Scale Test Suite
...   Usage:
...   robot -V data_variables_ftc.py -v APPLIANCE_IP:16.114.208.62 ../OVF2458_Q2_mini_scale/

Resource        ../../../../Resources/api/fusion_api_resource.txt

Suite Setup    Test Specific setup
#Suite Setup    Run FTS and test-specific setup
#Suite Teardown		Teardown

# Setup\Teardown for ALL test cases
Test Setup     Run Keyword and Ignore Error    Write To ciDebug Log
Test Teardown  Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors


*** Variables ***
${VM}
${SSH_USER}                     root
${SSH_PASS}                     Wpst@hpvse123#!
${FUSION_IP}					${APPLIANCE_IP}

*** Test Cases ***
Empty Test Case
    Log    Empty Test Case so __init__.robot can be ran stand alone.
    No Operation

*** Keywords ***
Get Errors
    [Documentation]    Retrieves errors from the ciDebugLog
    ${ERRORS}=   Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}

Run FTS and test-specific setup
    [Documentation]    Run FTS and test-specific setup
	Set Log Level	TRACE
    FTS
    Test Specific Setup

FTS
    [Documentation]    First time setup steps
    [Tags]  FTS
	Set Log Level	 TRACE
    Run Keyword and Ignore Error    Write To ciDebug Log    FTS
	log variables
	First Time Setup    DATAFILE=${null}   password=${admin_credentials['password']}    interfaces=bond0
    [Teardown]     Run Keyword If    '${KEYWORD_STATUS}' == 'FAIL'   Get Errors


Test Specific Setup
    [Documentation]    Perform setup of all necessary resources for all additional tests
    [Tags]    TSS    Setup
	Set Log Level	TRACE
    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
	Run Keyword and Ignore Error    Write To ciDebug Log    TEST-SPECIFIC SETUP
	log    [TEST-SPECIFIC SETUP]   console=True
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

	${resp} =    Configure Appliance Time and Locale    ${Time_and_Locale}
	Wait for task2  ${resp}  timeout=60  interval=10

	${users} =	Get Variable Value	${users}
	Run Keyword If	${users} is not ${null}	Add Users from variable				${users}

    # STrm Resources
    Add San Managers Async  ${san_managers}

	${resplist} =  Add Storage Systems Async  ${storage_systems}
	Wait for task2  ${resplist}  timeout=60  interval=10

    ${resplist} =  Edit Storage Systems Async  ${storage_systems}
    Wait for task2  ${resplist}  timeout=180  interval=10

	${resplist} =  Edit Storage Pools Async  ${storage_pools}
	Wait for task2  ${resplist}  timeout=120  interval=10
    # End STrm Resources

	${ethernet_networks} =	Get Variable Value	${ethernet_networks}
	Run Keyword If	${ethernet_networks} is not ${null}     Add Ethernet Networks from variable   ${ethernet_networks}

	${fcoe_networks} =	Get Variable Value	${fcoe_networks}
	Run Keyword If	${fcoe_networks} is not ${null}	        Add FCoE Networks from variable		  ${fcoe_networks}

	${network_sets} =	Get Variable Value	${network_sets}
	Run Keyword If	${network_sets} is not ${null}          Add Network Sets from variable		  ${network_sets}

	${fc_networks} =	Get Variable Value	${fc_networks}
	Run Keyword If	${fc_networks} is not ${null}           Add FC Networks from variable		  ${fc_networks}

	${racks} =	Get Variable Value	${racks}
	Run Keyword If	${racks} is not ${null}                 Add Racks from variable		          ${racks}

#    Add Existing Storage Volumes to OV
    ${resplist} =  Add Existing Storage Volumes Async  ${existing_volumes}
    Wait for Task2  ${resplist}  timeout=30  interval=10

    [Teardown]     Run Keyword If    '${KEYWORD_STATUS}' == 'FAIL'   Get Errors

Teardown
    [Documentation]    Remove all resources from the appliance
	Set Log Level	TRACE
    Run Keyword and Ignore Error    Write To ciDebug Log    TEARDOWN
	Log    [TEARDOWN]    console=True
	Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
	Power off ALL Servers
	Remove All Server Profiles
	Remove All Server Templates
	Remove ALL LS
	Remove ALL LSGs
	Remove All Logical Enclosures
	Remove ALL Enclosure Groups
	Remove ALL LIGs
	Remove All SAS LIGs
	Remove ALL Ethernet Networks
	Remove ALL FC Networks
	Remove ALL FCoE Networks
	Remove ALL Network Sets
	Remove ALL Users
    [Teardown]     Run Keyword If    '${KEYWORD_STATUS}' == 'FAIL'   Get Errors
