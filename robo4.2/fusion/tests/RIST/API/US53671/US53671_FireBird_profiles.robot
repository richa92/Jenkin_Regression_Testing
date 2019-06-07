*** Settings ***
Documentation                   US53671 Firebird Server profiles connections, Local storage and BB storage
...                               -  Add Base Resources networks
...                               -  Add SAS LIG, Potash LIG, create EG, and LE
...                               -  Create Firebird Server profiles connections, Local storage and BB storage, edit, move
...                               -  Remove Base Resources

Library				FusionLibrary
Library             RoboGalaxyLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library             XML
Library             String
Library  			Dialogs

Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${DATA_FILE}

#Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
#Resource            ../global_variables.robot
#Variables 		    ${CURDIR}\\${DATA_FILE}

Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}		16.114.209.223
${DATA_FILE}        ./Regression_Data.py

*** Test Cases ***
TC 1 Create Firebird SPT
    Create Firebird Server Profile Template

TC2 Create Firebird SP
    [Tags]    Performance    server_profiles-condition-jbods
    Create FireBird Server Profiles

TC3 Verify SAS lJBODS
    Verify Sas Logical JBODs

TC4 Verify SAS lJBOD Attachments
    Verify Sas Logical JBOD Attachments

TC5 Edit Firebird SP
    [Tags]    Performance    server_profiles-condition-jbods
    Edit Firebird Server Profile

TC6 Verify SAS lJBOD After Edit
    Verify Sas Logical JBODs After Edit

TC7 Verify SAS lJBOD Attachments After Edit
    Verify Sas Logical JBOD Attachments After Edit

TC8 Create and Move Firebird Profile to 2nd Enclosure
#    Power off Servers in Profiles       ${firebird_server_profiles}
    ${resp} =    Remove All Server Profiles Async
    Wait For Task2    ${resp}	   timeout=2400	interval=15
    Create FireBird Server Profile
    Move Server Profile To 2nd Enclosure

*** Keywords ***
Setup
    [Documentation]  Setup
    Set Log Level  DEBUG
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    ${resp} =    Remove All Server Profiles Async
    Wait For Task2    ${resp}	   timeout=2400	interval=15

Clean Up
    [Documentation]  Clean Up
    Power off Servers in Profiles    ${firebird_server_profiles}
    ${resp} =    Remove All Server Profiles Async
    Wait For Task2    ${resp}	   timeout=2400	interval=15
    Remove All Server Profile Templates
    Fusion Api Logout Appliance

Create Firebird Server Profile Template
    [Documentation]  Create Firebird Server Profile Template
    @{responses} =    Create List
    :FOR	${profile_template}	IN	@{firebird_server_profile_templates}
	\      ${resp} = 	Add Server Profile Template	${profile_template}
	\      log to console		${resp}
	\      Append To List    ${responses}    ${resp}

	Wait For Task2	${responses}	   timeout=60	interval=5

Create FireBird Server Profiles
    [Documentation]  Create FireBird Server Profiles
    @{responses} =    Create List
    :FOR	${server_profile}	IN	@{firebird_server_profiles}
	\      ${resp} = 	Add Server Profile	${server_profile}
	\      log to console		${resp}
	\      Append To List    ${responses}    ${resp}

	Wait For Task2    ${responses}    timeout=2400	interval=15
	Sleep     15s    # don't like this but last tests failed due to an operation still going on the SP, yet Task was Completed.  ???
#    Power on Servers in Profiles  ${firebird_server_profiles}

Verify Sas Logical JBODs
    [Documentation]  Verify Sas Logical JBODs
    Run Keyword If	${sas_logical_jbods} is not ${null}		Verify Resources For list	${sas_logical_jbods}

Verify Sas Logical JBOD Attachments
    [Documentation]  Verify Sas Logical JBOD Attachments
    Run Keyword If	${sas_logical_jbod_attachments} is not ${null}		Verify Resources For list	${sas_logical_jbod_attachments}

Edit Firebird Server Profile
    [Documentation]  Edit Firebird Server Profile
     Power off Servers in Profiles  ${firebird_server_profiles}
	 ${resp} = 	Edit Server Profile	${edit_profile_add_jbod}
	 log to console		${resp}
	 Wait For Task2	${resp}	   timeout=2400	interval=15

Verify Sas Logical JBODs After Edit
    [Documentation]  Verify Sas Logical JBODs After Edit
    Run Keyword If	${sas_logical_jbods_after_edit} is not ${null}		Verify Resources For list	${sas_logical_jbods_after_edit}

Verify Sas Logical JBOD Attachments After Edit
    [Documentation]  Verify Sas Logical JBOD Attachments After Edit
    Run Keyword If	${sas_logical_jbod_attachments_after_edit} is not ${null}		Verify Resources For list	${sas_logical_jbod_attachments_after_edit}

Create FireBird Server Profile
    [Documentation]  Create FireBird Server Profile
	 ${resp} = 	Add Server Profile	${server_profile}
	 log to console		${resp}
	 Wait For Task2	${resp}	   timeout=2400	interval=15

Move Server Profile To 2nd Enclosure
    [Documentation]  Move Server Profile To 2nd Enclosure
    ${resp} = 	Edit Server Profile     ${move_server_profile_to_enc2}
    Wait For Task2	${resp}	   timeout=2400	interval=15
