*** Settings ***
Documentation                   F1222 Edit Server Profile Templates - SHT and EG
...                               -  Add Base Resources networks
...                               -  Add Single Switch SAS LIG, Potash LIG, create EG, and LE
...                               -  Create Server Profile Templates
...                               -  Edit Server Profile Templates - Change SHT, EG, BL to DL, SHT and EG, auth test, negative(wrong values)
...                               -  Remove Base Resources

Library				FusionLibrary
Library             RoboGalaxyLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library             XML
Library             String
Library  			Dialogs

Resource            ../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot

Variables 		    ${DATA_FILE}

Suite Setup         F1222 Setup
Suite Teardown      F1222 Teardown

*** Variables ***
${APPLIANCE_IP}		16.114.209.223
${DATA_FILE}        ./Regression_Data.py

*** Test Cases ***
Setup Server Profile Templates for edit
   ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${server_credentials}
	Create Server Profile Templates		@{profile_templates}
	Verify Server Profile Templates		${profile_templates}

Edit Server Profile Template SHT
	Edit Server Profile Templates		@{edit_sht_templates}
	Verify Server Profile Templates		${edit_sht_templates}

Edit Server Profile Template EG and SHT
	Edit Server Profile Templates		@{edit_eg_templates}
	Verify Server Profile Templates		${edit_eg_templates}

Edit Server Profile Template Network Admin Unauthorized access
	${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${network_credentials}
	${negative_server_profile_tasks} =	Get Variable Value	${negative_unauth_edit_template}
    Run Negative Tasks for List     ${negative_unauth_edit_template}
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${storage_credentials}
	${negative_server_profile_tasks} =	Get Variable Value	${negative_unauth_edit_template}
    Run Negative Tasks for List     ${negative_unauth_edit_template}

Edit Server Profile Template - Negative tests - Non-existing EG, SHT, Address cannot be changed
	${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${server_credentials}
	${resp} =    Add Server Profile    ${sp_from_spt}
    Wait for Task2    ${resp}    timeout=3600    interval=10
	${negative_server_profile_tasks} =	Get Variable Value	${negative_tests_eg_sht_addresses}
    Run Negative Tasks for List     ${negative_server_profile_tasks}

Get and Verify Server Profile Template Transformation DTO
   ${uri}=		Get Server Profile Template Transformation URI	@{transformation_eg_templates}
   Log to console	${uri}
   ${transformation_dto}=		Get Server Profile Template Transformation	${uri}
   Remove From Dictionary		${transformation_dto}		created		modified	status	state 	status_code	headers 	# These needs to be removed from payload
   Verify Server Profile Template Transformation DTO	@{verify_transformation_eg_templates}		${transformation_dto['serverProfileTemplate']}

Edit Server Profile Template with Transformation DTO
   ${uri}=		Get Server Profile Template Transformation URI	@{transformation_edit_eg_templates}
   Log to console	${uri}
   ${transformation_dto}=		Get Server Profile Template Transformation	${uri}
   ${profile_template_uri} =  Get From Dictionary		${transformation_dto['serverProfileTemplate']}  uri
   Remove From Dictionary		${transformation_dto}		created		modified	status	state 	status_code	headers 	# These needs to be removed from payload
   ${resp} = 	Fusion Api Edit Server Profile Template		body=${transformation_dto['serverProfileTemplate']}		uri=${profile_template_uri}
   Wait For Task2	${resp}	   timeout=60	interval=5
   Verify Server Profile Templates		${transformation_edit_eg_templates}


*** Keywords ***
F1222 Setup
    [Documentation]    Setup
    Set Log Level  TRACE
	Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
	Add Users from variable    ${users}
	#Add Ethernet Networks from variable	${ethernet_networks}
	Add LIG from list  ${ligs}
    Add SAS LIG from list  ${sasligs}
    Add Enclosure Group from list  ${egs}
    Fusion Api Logout Appliance

Create Server Profile Templates
     [Documentation]   Create Server Profile Templates
	 [Arguments]		@{profile_templates}																
     :FOR	${profile_template}	IN	@{profile_templates}
	 \		${resp} = 	Add Server Profile Template   ${profile_template}
	 \		log to console		${resp}
	 \      Wait For Task2	${resp}	   timeout=60	interval=5

Edit Server Profile Templates
    [Documentation]    Edit Server Profile Templates
	[Arguments]		@{profile_templates}																	
     :FOR	${edit_profile_template}	IN	@{profile_templates}
	 \		${resp} = 	Edit Server Profile Template   ${edit_profile_template}
	 \		log to console		${resp}
	 \      Wait For Task2	${resp}	   timeout=60	interval=5

Verify Server Profile Templates
    [Documentation]    Verify SErver Profile Templates
	[Arguments]		${profile_templates}
    Run Keyword If	${profile_templates} is not ${null}		Verify Resources For list	${profile_templates}

Negative Tests Server Profiles
    [Documentation]    Negative Tests Server Profiles
    Power Off All Servers
    ${negative_server_profile_tasks} =	Get Variable Value	${negative_server_profile_tasks}
    Run Negative Tasks for List     ${negative_server_profile_tasks}

F1222 Teardown
    [Documentation]    Teardown
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    Delete Resource    SP:F1222_from_template

    :FOR    ${spt}    in    @{profile_templates}
    \    Delete Resource    SPT:${spt['name']}

    Delete Resource    EG:EG2
    Delete Resource    EG:EG3

    Delete Resource    LIG:LIG2
    Delete Resource    LIG:LIG3

    Delete Resource    SASLIG:SASLIG2
    Delete Resource    SASLIG:SASLIG3

    Fusion Api Logout Appliance