*** Settings ***
Documentation                   F247 After Server profiles with BigBird Drive JBODs
...                               -  Add Base Resources networks
...                               -  Add Single Switch SAS LIG, Potash LIG, create EG, and LE
...                               -  Efuse Natasha
...                               -  Create Server profiles with JBODs
...                               -  Check with RIS calls on P542D mezz card storage
...                               -  Remove Base Resources

Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		                ${DATA_FILE}

Suite Setup                     Set Up
Suite Teardown                  Tear Down

*** Variables ***
${APPLIANCE_IP}		16.114.209.223
${DATA_FILE}        ./Regression_Data.py

*** Test Cases ***
Create Server Profiles With JBODs
    [Tags]    Performance    server_profiles-condition-jbods
    Create Server Profiles With JBODs

Verify SAS Storage with RIS
    Verify SAS Storage with RIS

Edit Server Profile Add JBODs
    [Tags]    Performance    server_profiles-condition-jbods
    Edit Server Profile Add JBOD

Verify SAS Storage with RIS After Zone Modify
   Verify SAS Storage with RIS After Zone Modify

EfuseReset SAS IC and Check Configured
    Delete All Alerts by Param  param=?filter=description like 'The interconnect in bay 1 has been removed.'
    Delete All Alerts by Param  param=?filter=description like 'An interconnect has been inserted in bay 1.'
    EfuseReset SAS IC and Check Configured

EfuseOn SAS IC and Check Alert
    Delete All Alerts by Param  param=?filter=description like 'The interconnect in bay 1 has been removed.'
    EfuseOn SAS IC and Check Alert

EfuseOff SAS IC and Check Alert
    Delete All Alerts by Param  param=?filter=description like 'An interconnect has been inserted in bay 1.'
    EfuseOff SAS IC and Check Alert

SAS IC Configured
    ${uri} = 	Get Sas Interconnect URI    ${ENC1SASICBAY1}
    Wait Until Keyword Succeeds    6 min    5s    IC reached state    ${uri}    Configured

*** Keywords ***
Set Up
    [Documentation]  Setup
    Set Log Level  DEBUG
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Power off Servers in Profiles    ${server_profiles}

#   Remove the profiles if they exist
    @{tasks} =    Create List
    :FOR	${server_profile}	IN	@{server_profiles}
    \    ${sp_uri} =    Common Uri Lookup By Name    SP:${server_profile['name']}
    \    ${status}    ${dontcare} =    Run Keyword and Ignore Error    Should End With    ${sp_uri}    _not_found
    \    Run Keyword If   '${status}'=='PASS'    Continue For Loop
    \    ${task}=    Remove Server Profile    ${server_profile}
    \    Append To List    ${tasks}    ${task}

    ${numTasks} =    Get Length    ${tasks}
    Run Keyword if    ${numTasks}>0    Wait For Task2    ${tasks}    timeout=4200    interval=15

Tear Down
    [Documentation]  Tear Down
    Power off Servers in Profiles    ${server_profiles}
    ${sasli_uri} =  Common URI lookup by name    SASLI:${SAS_LI_NAME}
    ${resp} =  Fusion API Reapply SAS LI Configuration  ${sasli_uri}
    Wait for Task2    ${resp}    timeout=180    interval=10

    ${resp} =    Remove Server Profiles from variable    ${server_profiles}
    Wait For Task2	${resp}	   timeout=4200	interval=5
    Fusion Api Logout Appliance

Create Server Profiles With JBODs
    [Documentation]  Create Server Profiles With JBODs
    Power off Servers in Profiles    ${server_profiles}
    @{responses} =    Create List
    :FOR	${server_profile}	IN	@{server_profiles}
	\		${resp} = 	Add Server Profile	${server_profile}
	\		log to console		${resp}
	\       Append To List    ${responses}    ${resp}

	Wait For Task2    ${responses}    timeout=4200    interval=15

Edit Server Profile Add JBOD
    [Documentation]  Edit Server Profiles With JBODs
     ${resp} = 	Edit Server Profile     ${edit_profile_add_jbod}
     Wait For Task2	${resp}	   timeout=4200	interval=5

Verify Server Profiles With JBODs
    [Documentation]  Verify Server Profiles With JBODs
    Run Keyword If	${server_profiles} is not ${null}		Verify Resources For list	${server_profiles}

Verify Sas Logical JBODs
    [Documentation]  Verify Sas Logical JBODs
    Run Keyword If	${sas_logical_jbods} is not ${null}		Verify Resources For list	${sas_logical_jbods}

Verify Sas Logical JBOD Attachments
    [Documentation]  Verify Sas Logical JBOD Attachments
    Run Keyword If	${sas_logical_jbod_attachments} is not ${null}		Verify Resources For list	${sas_logical_jbod_attachments}

Verify SAS Storage with RIS
    [Documentation]  Verify SAS Storage with RIS
    Verify RIS Nodes for List  ${ris_nodes_create_ilo}

Verify SAS Storage with RIS After Zone Modify
    [Documentation]  Verify SAS Storage with RIS After Zone Modify
    Verify RIS Nodes for List  ${ris_nodes_after_edit_ilo}

EfuseReset SAS IC and Check Configured
    [Documentation]  EfuseReset SAS IC and Check Configured
    [Tags]  Efuse  Neg
	${uri} = 	Get Sas Interconnect URI     ${ENC1SASICBAY1}
    ${enc} =    Fetch from left     ${ENC1SASICBAY1}    ,
    ${bay} =    Fetch from right    ${ENC1SASICBAY1}    ${SPACE}
    Get EM IP    ${enc}
    Get EM Token    ${enc}
    Efuse ICM   EFuseReset     ${bay}
    Wait Until Keyword Succeeds    180s    10s    Get Alert By Param   param=?filter=description like 'The interconnect in bay 1 has been removed.'
    Wait Until Keyword Succeeds    240s    10s    Get Alert By Param   param=?filter=description like 'An interconnect has been inserted in bay 1.'
	Log    Waiting for ICM in Bay:${bay} to reach state:Configured
    Wait Until Keyword Succeeds     6 min   5s      IC reached state    ${uri}    Configured

EfuseOn SAS IC and Check Alert
    [Documentation]  EfuseOn SAS IC and Check Alert
    [Tags]  Efuse  Neg
	Run Keyword and Ignore Error    Write To ciDebug Log
	${uri} = 	Get Sas Interconnect URI     ${ENC1SASICBAY1}
    ${enc} =    Fetch from left     ${ENC1SASICBAY1}    ,
    ${bay} =    Fetch from right    ${ENC1SASICBAY1}    ${SPACE}
	Log    Waiting for ICM in Bay:${bay} to reach state:Configured
    Wait Until Keyword Succeeds     6 min   5s      IC reached state    ${uri}    Configured
    Run Keyword and Ignore Error    Write To ciDebug Log    [EFUSEON SAS IC]
    Get EM IP    ${enc}
    Get EM Token    ${enc}
    Efuse ICM   EFuseOn     ${bay}
	Wait Until Keyword Succeeds    180s    10s    Get Alert By Param   param=?filter=description like 'The interconnect in bay 1 has been removed.'

EfuseOff SAS IC and Check Alert
    [Documentation]  EfuseOff SAS IC and Check Alert
    [Tags]  Efuse  Neg
	Run Keyword and Ignore Error    Write To ciDebug Log
    ${enc} =    Fetch from left     ${ENC1SASICBAY1}    ,
    ${bay} =    Fetch from right    ${ENC1SASICBAY1}    ${SPACE}
    Run Keyword and Ignore Error    Write To ciDebug Log    [EFUSEOFF SAS IC]
    Get EM IP    ${enc}
    Get EM Token    ${enc}
    Efuse ICM   EFuseOff     ${bay}
    Wait Until Keyword Succeeds    240s    10s    Get Alert By Param   param=?filter=description like 'An interconnect has been inserted in bay 1.'
