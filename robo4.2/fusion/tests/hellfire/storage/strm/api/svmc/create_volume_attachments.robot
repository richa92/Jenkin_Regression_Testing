*** Settings ***
Documentation    This test is using the fusion/hellfire client. It createa all resources
...              needed by the server profile. It then creates the server profile with
...              volume attachments using SVMC. IT DOES USE SVMC.
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Library             OperatingSystem
Library             String
Library             XML
Resource            ${CURDIR}\\..\\..\\..\\..\\..\\..\\Resources\\api\\fusion_api_resource.txt
Resource			${CURDIR}\\..\\..\\..\\..\\..\\..\\Resources\\api\\hellfire_api_resource.txt

Variables 		    ${CURDIR}\\..\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		16.71.130.119
${api}              400

${DATA_FILE}         Regression_Data.py


*** Test Cases ***
Initialize the Variables
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance 		${APPLIANCE_IP}  ${admin_credentials}
    
Add LIG Base Resources
	[Tags]    SETUP		LIG
    [Documentation]		Add LIG to hellfire Oneview VM
    Add LIG from list	${ligs}
	
Add Enclosure Group Base Resources
	[Tags]    SETUP		Encl Group
    [Documentation]		Add Encl grp to hellfire Oneview VM	
	Add Enclosure Group from list	${enc_groups}
	
Add Enclosure Base Resources
	[Tags]    SETUP		Enclosure
    [Documentation]		Add Encl to hellfire Oneview VM	
	Add Enclosures from variable	${enclosures}

Create server profile with attachments
    [Tags]    SETUP		Server Profile
    [Documentation]		Add Server Profile with volume attachments to hellfire Oneview VM	
	${payload} =  Create Server Profile POST Payload   ${profile1_create}
	${blnCreateProf} =	Fusion API Create Server Profile     ${payload}  api=${api}
	wait for task2  ${blnCreateProf}  timeout=300  interval=10
	