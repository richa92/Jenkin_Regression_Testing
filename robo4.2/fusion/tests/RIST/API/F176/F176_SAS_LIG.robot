*** Settings ***
Documentation                   F176 Synergy SASLIG and SASLI
...                               -  Add SideA SASLIG, Edit EG, Update LE from Group
...                               -  Verify SAS IC
...                               -  Edit SASLIG to Redundant and Update SASLI from Group
...                               -  Verify SAS IC
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${CURDIR}\\${DATA_FILE}

Suite Setup         F176 Synergy Setup
Suite Teardown      Teardown

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

${DATA_FILE}         Regression_Data.py

*** Test Cases ***
F176 Synergy Add SideA SASLIG to EG and Update LE from Group
	# Create SASLIG with Natasha in bay1
    Add SAS LIG from list  ${sasligs}
    # Edit EG and add SASLIG to it
    Edit Enclosure Group from list  ${edit_egs}
    # Get the Alert on non-comliance
    Wait Until Keyword Succeeds  60s  5s  Get Alert By Param  param=?filter=description like 'The logical enclosure is inconsistent with its enclosure group*'
    # Update LE from Group
    Update Logical Enclosure from Group from list  ${les}  timeout=3200  interval=10
    # Get the Alert on comliance
    Wait Until Keyword Succeeds  60s  5s  Get Alert By Param  param=?filter=description like 'The logical enclosure is consistent with its enclosure group*'

F176 Synergy Verify SAS IC after Add SideA SASLIG
    # Verify Natasha in bay1 is now configured
    Verify Sas Interconnects from list  ${sasics_bay1}  state=Configured
    # Verify Natasha in bay4 is still Monitored
    Verify Sas Interconnects from list  ${sasics_bay4}  state=Monitored

F176 Synergy Edit SASLIG to Redundant and Update SASLI from Group
    # Edit the SASLIG to redundant in bay1 and bay4
    Edit SAS LIG from list  ${edit_sasligs}
    # Get SASLI with OK/Warning status
    ${resp} =  fusion api get sas li  param=?filter="'status'='OK' OR 'status'='Warning'"
    # Return from the test If no SASLI with OK/Warning status returned
    ${count} =    Get From Dictionary    ${resp}    count
    Run Keyword If  ${count}==0  Fail  Edit SAS LIG and Update SAS LI
    # Update SASLI from group
    ${saslis} =  get from dictionary  ${resp}  members
	Update SAS LI from Group from list  ${saslis}	timeout=1800	interval=10

F176 Synergy Verify SAS IC after Edit SASLIG to Redundant
	# Verify Natasha in both bays are Configured
	Verify SAS Interconnects from list  ${sasics}  state=Configured

*** Keywords ***
F176 Synergy Setup
    Set Log Level	TRACE
    ${feature} =  set variable  F176
    log  ${feature} Suite Setup: Start check preconditions  console=True

	Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
	# Remove specific alerts
	Remove All Alerts  param=?filter=description like 'The logical enclosure is inconsistent with its enclosure group*'
	Remove All Alerts  param=?filter=description like 'The logical enclosure is consistent with its enclosure group*'
	# Verify the enclosures and interconnects state
	Verify Interconnects from list  ${ics}  state=Configured
    Verify Enclosures from list  ${enclosures}  state=Configured
    # Verify Natasha are Monitored
	Verify SAS Interconnects from list  ${sasics}  state=Monitored

	log  ${feature} Suite Setup: Finish check preconditions  console=True

Teardown
    Fusion Api Logout Appliance