*** Settings ***
Documentation
...     Description : Create LJBODs, Create/edit Profiles with existing&new LJBODs, Create/edit Profile Templates with existing&new LJBODs,
...     Rally: OVF900, OVS11170
...     Test dependencies - DUAL SAS IC LI
...     HW requirements :
...         Server Hardware Type(s):
...                 SY 680 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA
...                 SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA
...                 SY 480 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA
...                 SY 660 Gen10:1:HPE Smart Array P416ie-m SR G10:3:Synergy 3820C 10/20Gb CNA:4:HPE Smart Array P416ie-m SR G10
...         Interconnects
...                 Potash/Chloride fabric
...                 2 SAS ICs
...         Local Storage: BigBird
...         Uplinks/Connections - Net100, Net300
...         SAN Managers: N/A
...         Shared Keywords modified - Create Server Profile POST Payload from SPT
...                Added Delete Logical JBOD, Delete all Logical JBODs

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

Suite Setup         Setup
Suite Teardown      Clean Up     ${profiles}

*** Variables ***
#${APPLIANCE_IP}         ${FUSION_IP}
#${DATA_FILE}        ./Dcs_Data.py
#&{admin_credentials}         userName=${FUSION_ADMIN_LOGIN}         password=${FUSION_ADMIN_PASSWORD}

*** Test Cases ***
Create SAS LJBODs
    [Tags]    OVF900-OVS11170-ljb
    Add Logical JBODs Async     ${ljbs}
    Wait Until Keyword Succeeds    6 min    5s    Check Resource Attribute     SASLJBOD:${gen9_ljb1}  state  Configured
    Wait Until Keyword Succeeds    6 min    5s    Check Resource Attribute     SASLJBOD:${gen10_ljb1}  state  Configured
    Wait Until Keyword Succeeds    6 min    5s    Check Resource Attribute     SASLJBOD:${gen9_ljb2}  state  Configured
    Wait Until Keyword Succeeds    6 min    5s    Check Resource Attribute     SASLJBOD:${gen10_ljb2}  state  Configured
    Reapply SAS Logical Interconnect Configuration By Name and Verify     ${SASLI}

create profiles
    [Tags]    OVF900-OVS11170-sp
    Create Server Profiles

Edit profiles
    [Tags]    OVF900-OVS11170-esp
    Edit Server Profiles

Cleanup Profiles and LJBODs
    [Tags]    OVF900-OVS11170-clean
    Clean Up     ${profiles}

create Profile Templates
    [Tags]    OVF900-OVS11170-spt
    Create Server Profile Templates
    Add Logical JBODs Async     ${spt_ljbs}
    Wait Until Keyword Succeeds    6 min    5s    Check Resource Attribute     SASLJBOD:${spt_gen9_ljb}  state  Configured
    Wait Until Keyword Succeeds    6 min    5s    Check Resource Attribute     SASLJBOD:${spt_gen10_ljb}  state  Configured
    Reapply SAS Logical Interconnect Configuration By Name and Verify     ${SASLI}

create Profiles from Templates
    [Tags]    OVF900-OVS11170-sp-from-spt
    Create Server Profiles from Templates

Delete LJBOD when it is attached to SP
    [Tags]    OVF900-OVS11170-delete-ljb
    Run Negative Task     ${del_ljb_task}

Cleanup Profiles from templates and LJBODs
    [Tags]    OVF900-OVS11170-clean2
    Clean Up     ${profiles_from_templates}
    Delete all Logical JBODs

*** Keywords ***
Delete SAS LJBODs
    [Documentation]  delete LJBODs
    Delete Logical JBODs Async     ${ljbs}

Setup
    [Documentation]  Setup
    Set Log Level  TRACE
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Power off Servers in Profiles    ${profiles}
    ${resp} =    Remove Server Profiles from variable    ${profiles}
    Wait For Task2    ${resp}	   timeout=2400	interval=15
    Power off Servers in Profiles    ${profiles_from_templates}
    ${resp} =    Remove Server Profiles from variable    ${profiles_from_templates}
    Wait For Task2    ${resp}	   timeout=2400	interval=15
    Delete all Logical JBODs
    Reapply SAS Logical Interconnect Configuration By Name and Verify       ${SASLI}
    ${sptlist} =    Remove All Server Profile Templates
    Wait For Task2    ${sptlist}    timeout=600    interval=5

Create Server Profiles
    [Documentation]  Create Server Profiles
    :FOR	${profile}	IN	@{profiles}
	\    ${resp} =    Add Server Profile    ${profile}
    \    Wait For Task2	${resp}    timeout=4800    interval=20

Edit Server Profiles
    [Documentation]   Edit profiles
    :FOR	${profile}	IN	@{edit_profiles}
	\		${resp} = 	Edit Server Profile	${profile}
	\       Wait For Task2	${resp}    timeout=2400    interval=20

Create Server Profile Templates
    [Documentation]   Create Server Profile Templates
     :FOR	${spt}	IN	@{profile_templates}
	 \		${resp} = 	Add Server Profile Template   ${spt}
	 \      Wait For Task2	${resp}	   timeout=60	interval=5

Create Server Profiles from Templates
    [Documentation]  Create Server Profiles from Templates
    :FOR	${profile}	IN	@{profiles_from_templates}
	\    ${resp} =    Add Server Profile    ${profile}
    \    Wait For Task2	${resp}    timeout=4800    interval=20

Clean Up
    [Documentation]  cleanup
    [Arguments]  ${profiles}
    Power off Servers in Profiles    ${profiles}
    ${resp} =    Remove Server Profiles from variable    ${profiles}
    Wait For Task2	${resp}	   timeout=4200	interval=5
    Delete SAS LJBODs
    Reapply SAS Logical Interconnect Configuration By Name and Verify       ${SASLI}
    ${sptlist} =    Remove All Server Profile Templates
    Wait For Task2    ${sptlist}    timeout=600    interval=5

