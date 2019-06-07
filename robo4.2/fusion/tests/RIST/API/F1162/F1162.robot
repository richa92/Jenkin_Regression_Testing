*** Settings ***
Documentation       F1162 - SPT supports iSCSI

Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Resource            ../global_variables.robot

Variables 		                ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}     'DCS APPLIANCE IP'

${DATA_FILE}         Regression_Data.py

*** Test Cases ***
Initialize the Variables and Log In
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Create Server Profile Template
    ${resp} =    Add Server Profile Templates from variable  ${create_profile_templates}
    Wait For Task2    ${resp}    timeout=10    interval=1

    Verify Server Profile Templates  ${create_profile_templates}
    Power off Servers in Profiles  ${sp}
    ${resp_list}=  Add Server Profiles from variable  ${sp}
    Wait For Task2  ${resp_list}  timeout=1500  interval=10

    :FOR  ${profile}  IN  @{sp}
    \   Verify Server Profile  ${profile}

    Verify Server Profile Compliance    ${sp_pre_compliance}

    ${resp} =  Edit Server Profile    ${sp_Enable_Chap}
    Wait For Task2    ${resp}    timeout=300    interval=10

    Verify Server Profile Compliance    ${sp_post_compliance}

Edit Server Profile Template
    Edit Server Profile Template  ${spt_1_edit[0]}
    Verify Server Profile Templates  ${spt_1_edit}

Create the Negative Profile Templates
    Run Negative Tasks for List  ${negative_spt_tasks}

Clean Up
    ${resp} =  Remove Server Profile  @{sp}[0]
    Wait for Task2  ${resp}  timeout=300
    ${resplist} =  Remove Server Profile Templates from variable  ${create_profile_templates}
    Wait for Task2  ${resplist}  timeout=30  interval=10
    Fusion Api Logout Appliance