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
Suite Teardown      Clean Up

*** Variables ***
#${APPLIANCE_IP}         ${FUSION_IP}
#${DATA_FILE}        ./Dcs_Data.py
#&{admin_credentials}         userName=${FUSION_ADMIN_LOGIN}         password=${FUSION_ADMIN_PASSWORD}

*** Test Cases ***
Create Scopes SAS LJBODs and Scope users
    [Tags]    OVF900-OVS34006-ljb
    Log     \nCreating Scopes Gen9 Gen10, respective ljbods, and scope users    console=yes
    ${responses} =    Create Scopes    ${scopes}
    :FOR    ${resp}    IN    @{responses}
    \       Should Be Equal    '${resp["status_code"]}'   '202'    msg= Failed to create scope!
    Add Logical JBODs Async     ${scope_ljbs}
    Wait Until Keyword Succeeds    6 min    5s    Check Resource Attribute     SASLJBOD:${gen9_scope_ljb1}  state  Configured
    Wait Until Keyword Succeeds    6 min    5s    Check Resource Attribute     SASLJBOD:${gen10_scope_ljb1}  state  Configured
    Wait Until Keyword Succeeds    6 min    5s    Check Resource Attribute     SASLJBOD:${gen9_scope_ljb2}  state  Configured
    Wait Until Keyword Succeeds    6 min    5s    Check Resource Attribute     SASLJBOD:${gen10_scope_ljb2}  state  Configured
    Reapply SAS Logical Interconnect Configuration By Name and Verify     ${SASLI}
    Add Users from variable			${scope_users}

Gen9 scope user ljbod Profile Template Profile operations
    [Tags]    OVF900-OVS34006-gen9
    Log     \n As Gen9 scope user creating ljbod, spt, profile from spt    console=yes
    Fusion Api Logout Appliance
    ${gen9_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${gen9_scope_credentials}
    Power off Server  SH:${ENC1SHBAY7}
    Add Logical JBOD     ${spt_gen9_scope_ljb_def}
    Wait Until Keyword Succeeds    6 min    5s    Check Resource Attribute     SASLJBOD:${spt_gen9_scope_ljb}  state  Configured
    Add Server Profile Template     ${gen9_profile_template}
    ${resp} =    Add Server Profile    ${gen9_profile_from_template}
    Wait For Task2	${resp}    timeout=4800    interval=20
    ${resp} =  Remove Server Profile  ${gen9_profile_from_template}
    Wait For Task2	${resp}    timeout=4800    interval=20
    Fusion Api Logout Appliance
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}


Gen10 scope user ljbod Profile Template Profile operations
    [Tags]    OVF900-OVS34006-gen10
    Fusion Api Logout Appliance
    Log     \n As Gen10 scope user creating ljbod, spt, profile from spt   console=yes
    ${gen10_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${gen10_scope_credentials}
    Power off Server  SH:${ENC1SHBAY6}
    Add Logical JBOD     ${spt_gen10_scope_ljb_def}
    Wait Until Keyword Succeeds    6 min    5s    Check Resource Attribute     SASLJBOD:${spt_gen10_scope_ljb}  state  Configured
    Add Server Profile Template     ${gen10_profile_template}
    ${resp} =    Add Server Profile    ${gen10_profile_from_template}
    Wait For Task2	${resp}    timeout=4800    interval=20
    Fusion Api Logout Appliance
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

Gen10 profile Delete ljbod change its scope Try adding it again
    [Tags]    OVF900-OVS34006-OVTC40992
    Fusion Api Logout Appliance
    ${gen10_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${gen10_scope_credentials}
    Log     \n As Gen10 scope user edit profile delete ljbod    console=yes
    ${resp} = 	Edit Server Profile	${gen10_profile_1st_edit}
	Wait For Task2	${resp}    timeout=4800    interval=20
	Fusion Api Logout Appliance
	${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
	Log     \n As admin delete gen10 ljb from gen10 scope    console=yes
	${ljb_uri} =     Get Sas Logical Jbod URI    ${spt_gen10_scope_ljb}
	${uri_list}=  create list   ${ljb_uri}
	${resp} =     Edit Scope    name=${gen10_scope_name}    removeresources=${uri_list}
	Log     \n As admin add gen10 ljb to gen9 scope    console=yes
    Edit Scope    name=${gen9_scope_name}    addresources=${uri_list}
    Log     \n log back in as gen10 scope user edit profile and add different scope ljbod    console=yes
    Fusion Api Logout Appliance
    ${gen10_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${gen10_scope_credentials}
    ${negative_server_profile_task} =	Get Variable Value	${negative_server_profile_task}
    Run Negative Task     ${negative_server_profile_task}
 	Fusion Api Logout Appliance
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}

*** Keywords ***
Setup
    [Documentation]  Setup
    Set Log Level  TRACE
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Power off Server  SH:${ENC1SHBAY6}
    Power off Server  SH:${ENC1SHBAY7}

Clean Up
    [Documentation]  cleanup
    Fusion Api Logout Appliance
    ${admin_session} =    Fusion Api Login Appliance 		${APPLIANCE_IP}		${admin_credentials}
    Power off Server  SH:${ENC1SHBAY6}
    Power off Server  SH:${ENC1SHBAY7}
    ${resp} =  Remove Server Profile  ${gen10_profile_from_template}
    Wait For Task2	${resp}    timeout=4800    interval=20
    ${resp} =  Remove Server Profile Template    ${gen10_profile_from_template}
    ${resp} =  Remove Server Profile Template    ${gen9_profile_from_template}
    Delete all Logical JBODs
    Remove All Users
    Remove All Scopes


