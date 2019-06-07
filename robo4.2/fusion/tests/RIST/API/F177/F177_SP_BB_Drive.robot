*** Settings ***
Documentation                   F177 Server profiles with BigBird Drive JBODs
...                               -  Add Base Resources networks
...                               -  Add Single Switch SAS LIG, Potash LIG, create EG, and LE
...                               -  Create Server profiles with JBODs, edit, move, unassign profiles and Negative tests
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

Suite Setup          Run Keywords     Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
...                  AND    Power off Servers in Profiles    ${server_profiles}
...                  AND    Delete Server Profiles from variable    ${server_profiles}

Suite Teardown       Run Keyword    Fusion Api Logout Appliance

*** Variables ***
${APPLIANCE_IP}		16.114.209.223
${DATA_FILE}        ./Regression_Data.py

*** Test Cases ***
F177 BasicTest
    Set Log Level  DEBUG
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

F177 Create Unassigned Server Profile with JBODs
    Create Unassigned Server Profile With JBODs

F177 Create Server Profile Templates With JBODs
    Create Server Profile Templates With JBODs

F177 Verify Server Profile Templates With JBODs
    Verify Server Profile Templates With JBODs

F177 Create Server Profiles With JBODs
    [Tags]    Performance    server_profiles-condition-jbods
    Create Server Profiles With JBODs

F177 Verify Server Profiles With JBODs
    Verify Server Profiles With JBODs

F177 Verify Sas Logical JBODs
    Verify Sas Logical JBODs

F177 Verify Sas Logical JBOD Attachments
    Verify Sas Logical JBOD Attachments

F177 Edit Server Profile Add JBOD
    [Tags]    Performance    server_profiles-condition-jbods
    Edit Server Profile Add JBOD

F177 Verify Sas Logical JBODs After Edit
    Verify Sas Logical JBODs After Edit

F177 Verify Sas Logical JBOD Attachments After Edit
    Verify Sas Logical JBOD Attachments After Edit

F177 Move Server Profile To Another Blade Within same Tbird
   Power off ALL servers
   Move Server Profile To Another Blade Within same Tbird

F177 Move Server Profile between two tbirds within same ring
    Move Server Profile between two tbirds within same ring

F177 Unassign Server Profile With JBODs
    Unassign Server Profile With JBODs

F177 Remove All Server Profiles
    Power off Servers in Profiles    ${server_profiles}
    ${resplist} =    Remove All Server Profiles Async    force=${True}
    Wait For Task2    ${resplist}    timeout=600    interval=5

F177 Verify JBODs Count
    Verify JBODs Count

#   Some of the negative tests data is commented because of quixes.

F177 Negative Tests Server Profiles
    Negative Tests Server Profiles

F177 Remove All Server Profiles2 and Templates
    Remove All Server Profiles
    ${sptlist} =    Remove All Server Profile Templates
    Wait For Task2    ${sptlist}    timeout=600    interval=5

*** Keywords ***
Add Base Resources
    [Documentation]   Keyword described
	Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
	# Remove All alerts
	Remove All Alerts
	# Create ethernet networks
	Add Ethernet Networks from variable	${ethernet_networks}
	# Verify Interconnects are Monitored and create LIG1
	Verify Interconnects from list  ${ics}  state=Monitored
	Add LIG from list  ${ligs}
	# Create SAS LIG with single switch in bay1
    Add SAS LIG from list  ${sasligs}
	# Create EG1 with both LIG1 and SAS LIG
    Add Enclosure Group from list  ${egs}
    # Create LE1 from EG1
    Add Logical Enclosure from list  ${les}
    # Verify IC are Configured
    Verify Interconnects from list  ${ics}  state=Configured
    # Verify Natasha SAS IC bay1 is now configured
    Verify Sas Interconnects from list  ${sasics_bay1}  state=Configured

Create Unassigned Server Profile With JBODs
    [Documentation]   Keyword described
     Power Off All Servers    control=PressAndHold
     ${resp} = 	Add Server Profile	${unassigned_server_profile}
     Wait For Task2	${resp}	   timeout=60	interval=5

Create Server Profile Templates With JBODs
    [Documentation]   Keyword described
     :FOR	${profile_template}	IN	@{profile_templates}
	 \		${resp} = 	Add Server Profile Template   ${profile_template}
	 \		log to console		${resp}
	 \      Wait For Task2	${resp}	   timeout=60	interval=5

Verify Server Profile Templates With JBODs
    [Documentation]   Keyword described
    Run Keyword If	${verify_profile_templates} is not ${null}		Verify Resources For list	${verify_profile_templates}

Create Server Profiles With JBODs
    [Documentation]   Keyword described
    @{responses} =    Create List
    :FOR	${server_profile}	IN	@{server_profiles}
	\		${resp} = 	Add Server Profile	${server_profile}
	\		log to console		${resp}
    \       Append To List    ${responses}    ${resp}
	Wait For Task2	${responses}    timeout=2400    interval=20

Verify Server Profiles With JBODs
    [Documentation]   Keyword described
    Run Keyword If	${verify_server_profiles} is not ${null}		Verify Resources For list	${verify_server_profiles}

Edit Server Profile Add JBOD
    [Documentation]   Keyword described
    ${resp} = 	Edit Server Profile     ${edit_profile_add_jbod}
    Wait For Task2	${resp}    timeout=2400    interval=20

Move Server Profile To Another Blade Within same Tbird
    [Documentation]   Keyword described
    ${move_server_profile} =	Get Variable Value	${move_server_profile_within_same_tbird}
    ${resp} =  	Edit Server Profile     ${move_server_profile}    newname=${move1_newName}
    Wait For Task2	${resp}    timeout=6000    interval=20

Move Server Profile between two tbirds within same ring
    [Documentation]   Keyword described
    Log 	Move Server Profile between two tbirds within same ring HAS BEEN COMMENTED OUT DUE TO LACK OF HW    WARN    console=True
#    ${move_server_profile} =	Get Variable Value	${move_server_profile_between_two_tbirds_within_same_ring}
#    ${resp} =  	Edit Server Profile     ${move_server_profile}    newname=${move2_newName}
#    Wait For Task2	${resp}    timeout=6000    interval=20

Unassign Server Profile With JBODs
    [Documentation]   Keyword described
    ${resp} = 	Edit Server Profile     ${unassign_existing_profile}
    Wait For Task2	${resp}    timeout=2400    interval=20

Verify Sas Logical JBODs
    [Documentation]   Keyword described
    Run Keyword If	${sas_logical_jbods} is not ${null}		Verify SasLJBODs Resources for List    ${sas_logical_jbods}

Verify Sas Logical JBOD Attachments
    [Documentation]   Keyword described
    Run Keyword If	${sas_logical_jbod_attachments} is not ${null}		Verify Resources For list	${sas_logical_jbod_attachments}

Verify Sas Logical JBODs After Edit
    [Documentation]   Keyword described
    Run Keyword If	${sas_logical_jbods_after_edit} is not ${null}		Verify SasLJBODs Resources For list    ${sas_logical_jbods_after_edit}

Verify Sas Logical JBOD Attachments After Edit
    [Documentation]   Keyword described
    Run Keyword If	${sas_logical_jbod_attachments_after_edit} is not ${null}		Verify Resources For list    ${sas_logical_jbod_attachments_after_edit}

Verify JBODs Count
    [Documentation]   Keyword described
	${resp} = 	Fusion Api Get Sas Logical Jbods
	Run Keyword If  ${resp['count']}!=0  FAIL   profile_delete_did_not_delete_jbods

Negative Tests Server Profiles
    [Documentation]   Keyword described
    Power Off All Servers    control=PressAndHold
    ${negative_server_profile_tasks} =	Get Variable Value	${negative_server_profile_tasks}
    Run Negative Tasks for List     ${negative_server_profile_tasks}

Verify SasLJBODs Resources for List
    [Documentation]  Verify a list DTOs with the expected ones
    ...              **kwargs are used to add key value pair to the expected DTO
    ...              Example:
    ...                Verify SasLJBODs Resouces for List  ${list}
    ...                Verify SasLJBODs Resources for List  ${list}  status=OK
    ...              Data Required:
    ...                List of expected Profile DTO
    [Arguments]  ${list}  ${api}=${None}  &{kwargs}
    Run Keyword for List with kwargs  ${list}  Verify SasLJBODs Resource  api=${api}  &{kwargs}

Verify SasLJBODs Resource
    [Documentation]  Verify SasLJBODs Resource
    ...              **kwargs are used to add key value pair to the expected DTO
    ...              Example:
    ...                Verify SasLJBODs Resource  ${expected_dto}
    ...                Verify SasLJBODs Resource  ${expected_dto}  Status=OK
    ...              Data Required:
    ...                Expected Resource DTO
    [Arguments]  ${expected_dto}  ${api}=${None}  &{kwargs}
    ${status}  ${name} =  Run Keyword and Ignore Error  Get From Dictionary  ${expected_dto}  name
    Return from keyword if    '${status}'=='FAIL'    ${expected_dto} doesn't contain the key $name
    ${status}  ${type} =  Run Keyword and Ignore Error  Get From Dictionary  ${expected_dto}  type
    Return from keyword if    '${status}'=='FAIL'    ${expected_dto} doesn't contain the key $type
    Log    ${\n}Verifying ${type} ${name}    console=true
    ${sas_ljbods_uri}  ${ljbod_name}=   Get Sas Logical Jbods URI And Name    ${name}
    Log    sas ljbods uri : ${sas_ljbods_uri}
    Log    sas ljbods name : ${ljbod_name}
    ${dto} =  Get Resource  ${type}:${name}  api=${api}
    ${new_expected_dto} =  Add Key Value to DTO  ${expected_dto}  &{kwargs}
    Set To Dictionary  ${new_expected_dto}    name=${ljbod_name}
    Set To Dictionary  ${new_expected_dto}    uri=${sas_ljbods_uri}
    ${validate_status} =  Run Keyword And Continue on Failure   Fusion api validate response follow  ${new_expected_dto}  ${dto}  wordy=${True}
    Run Keyword If  '${validate_status}'=='None' or '${validate_status}'=='False'   Run Keyword And Continue On Failure   Fail   Verify ${type} ${name} failed
    Run Keyword If  '${validate_status}'=='True'    Log    Verify ${type} ${name} succeeded    console=true

Get Sas Logical Jbods URI And Name
	[Documentation]	Get Sas Logical Jbods URI And Name using regex
	[Arguments]		${SASLJBOD}
	${resp} = 	Fusion Api Get Sas Logical Jbods 		param=?filter="'name' regex '^${SASLJBOD}'"
	Return From Keyword If  ${resp['count']}==0  /rest/sas_logical_jbod_uri_${SASLJBOD}_not_found
	${uri} = 	Get From Dictionary		${resp['members'][0]}	uri
	${name} = 	Get From Dictionary		${resp['members'][0]}	name
	[Return]	${uri}    ${name}

Get sasLogicalJBOD names
    [Documentation]    Processes a list of sasLogicalJBODs, getting the names for each
    [Arguments]        ${sasLogicalJBODs}
    ${JBODs} =  Create List
    :FOR    ${sasLogicalJBOD}    IN    @{sasLogicalJBODs}
    \   ${name} =  Get from Dictionary   ${sasLogicalJBOD}   name
    \   ${status}  ${return} =  Run Keyword and Ignore Error  Get from Dictionary   ${sasLogicalJBOD}   sasLogicalJBODUri
    \   ${sasLogicalJBODUri}     ${name} =      Run keyword if  '${status}'=='PASS' and "${return}"!="${None}"  Get Sas Logical Jbods URI And Name    ${name}
    \   Run keyword if  '${status}'=='PASS' and "${return}"!="${None}"  Set to Dictionary   ${sasLogicalJBOD}   name   ${name}
    \   append to list   ${JBODs}   ${sasLogicalJBOD}
    Log    ${JBODs}
    [Return]   ${JBODs}

Delete Server Profiles from variable
    [Documentation]    Processes a list of profiles and delete the profiles
    [Arguments]    ${server_profiles}
    ${tasks}=    Remove Server Profiles from variable    ${server_profiles}
    :FOR    ${task}    IN    @{tasks}
    \    Run Keyword And Continue on Failure  Wait For Task2  ${task}  timeout=240  interval=5

Set SASLogicalJBOD name
    [Documentation]    Processes a list of profiles, and set SASLogicalJBOD name
    [Arguments]    ${server_profiles}
    ${status}  ${return} =  Run Keyword and Ignore Error  Get From Dictionary    ${server_profiles['localStorage']}    sasLogicalJBODs
    ${sasLogicalJBODs} =     set variable if  '${status}'=='PASS'  ${return}
    ${sasLogicalJBODs} =     Run Keyword If  '${status}'=='PASS'    Get sasLogicalJBOD names   ${sasLogicalJBODs}
    Run Keyword If  '${status}'=='PASS'  Set to Dictionary   ${server_profiles['localStorage']}  sasLogicalJBODs  ${sasLogicalJBODs}
    [Return]   ${server_profiles}