*** Settings ***
Documentation                   F175 Synergy Natasha Discovery and Management
...                               -  Verify Enclosure
...                               -  Verify SAS IC
...                               -  Turn UID On/Off, Power Off/On, Soft/Hard reset on the SAS IC
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${CURDIR}\\${DATA_FILE}

Suite Teardown      F175 Synergy Teardown

*** Variables ***
${APPLIANCE_IP}		'DCS APPLIANCE IP'

${DATA_FILE}         dcs_variables.py

*** Test Cases ***
F175 Synergy Login the Users
    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Run Keyword If	${users} is not ${null}    Add Users from variable  ${users}
	Login all users  ${users}

F175 Synergy Verify the Enclosure
	Verify enclosures from list  ${enclosures}  state=Monitored
	
F175 Synergy Power on all Server hardware
	Power on ALL servers

F175 Synergy Power on all SAS IC
    Power On Sas Interconnects from list  ${sasics}
    
F175 Synergy Refresh all server hardware
    @{responses} =    Create List
    :FOR    ${server}    IN    @{hardware_list}
    \        Log to console    Refreshing server ${server}
    \        ${resp} =    Refresh Server Hardware    ${server}
    \        Append To List    ${responses}    ${resp}

    Set Suite Variable    ${tasks}    ${responses}

F175 Synergy Verify the SAS Interconnects
	Verify Sas Interconnects from list  ${sasics}  state=Monitored

F175 Synergy SAS Interconnects Verify UID operations
	Run keyword as user  Serveradmin  Turn Sas Interconnects UID On from list  ${sasics}
	Verify Sas Interconnects from list  ${verify_sasics_no_port_state}  uidState=On
	Turn Sas Interconnects UID Off from list  ${sasics}
	Verify Sas Interconnects from list  ${verify_sasics_no_port_state}  uidState=Off
	
F175 Synergy SAS Interconnects Verify Power operations
    [Tags]    Performance    sas_interconnects-condition-power
	Power Off Sas Interconnects from list  ${sasics}
	Verify Sas Interconnects from list  ${verify_sasics_no_port_state}  powerState=Off
	Run keyword as user  Serveradmin  Power On Sas Interconnects from list  ${sasics}
	Verify Sas Interconnects from list  ${verify_sasics_no_port_state}  powerState=On

F175 Synergy SAS Interconnects Verify Reset operations
    [Tags]    Performance    sas_interconnects-condition-reset
    Soft Reset Sas Interconnects from list  ${sasics}
	Run keyword as user  Serveradmin  Hard Reset Sas Interconnects from list  ${sasics}

*** Keywords ***
F175 Synergy Teardown
    Wait For Task2    ${tasks}    timeout=300    interval=10
	Fusion Api Logout Appliance
