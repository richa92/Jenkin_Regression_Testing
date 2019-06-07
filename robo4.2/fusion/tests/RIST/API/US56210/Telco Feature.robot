*** Settings ***
Documentation       Telco settings on LE and EG
Suite Setup         Run Keywords    Set Log Level	TRACE
...          AND                Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
...          AND                Add Base Resources
#Suite Teardown      Run Keywords    Set Log Level	TRACE
#...          AND                Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
#...          AND                Delete Base Storage Resources
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Resource            ../global_variables.robot
Variables 		    ${CURDIR}\\${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}		16.114.209.223

${DATA_FILE}         Regression_Data.py
${SSH_PASS}          hpvse1
${FUSION_IP}         ${APPLIANCE_IP}

*** Test Cases ***
TS0 Login the Appliance
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Create Remote EG and LE
    Add Enclosure Group from list    ${REMOTE_EG}
    Add Logical Enclosure from lists    ${REMOTE_LE}
    Verify Logical Enclosure from list    ${REMOTE_LE}

Create EG with different Ambient Temp Mode
    Add Enclosure Group from list    ${Telco_EGs}
    Verify Enclosure Group from list    ${Telco_EGs}

Create LE with with ASHRAE A3
    Add Logical Enclosure from lists    ${les_ASHRAE_A3}
    Verify Logical Enclosure from list    ${verify_les_ASHRAE_A3}

Power on server and verify ambient temp after Create LE
    Power on server    ${ENC1SHBAY3}
    Wait for Server to reach POST state  ${ENC1SHBAY3}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=10m  interval=20s
    Verify RIS nodes for list  ${ris_node_enc1bay3}

Power off sever bay after create LE
    Power off server    ${ENC1SHBAY3}

Power on a server in Enclosure before Edit LE
    Power on server    ${ENC2SHBAY1}
    Wait for Server to reach POST state  ${ENC2SHBAY1}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=10m  interval=20s

Edit LE with different ASHRAE A4 while server power is power on
    Edit Logical Enclosure    ${EDIT_LE_EG_A4}    api=400    errorMessage=CONFIGURE_AMBIENT_TEMP_MODE_POWERON_WARNING   PASS=Warning 
    #Get Alert By Param   param=?filter=description like 'The ambient temperature mode of server hardware*'

Verify Power on server Ambient temp has not changed
    Verify RIS nodes for list  ${ris_node_enc2bay1_A3}

Power on a server and verify Ambient after Edit LE
    Power on server    ${ENC3SHBAY1}
    Wait for Server to reach POST state  ${ENC3SHBAY1}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST     timeout=10m  interval=20s
    Verify RIS nodes for list  ${ris_node_enc3bay1}

Power off servers in Enclosure
    Power off server    ${ENC2SHBAY1}
    Power off server    ${ENC3SHBAY1}

Reapply LE config and verify ambient temp
    Reapply Logical Enclosure Configuration    ${EDIT_LE_EG_A4}
    Verify Logical Enclosure from list   ${VERIFY_EDIT_LE_EG_A4}

Power on a server and verify Ambient after Reapply config
    Power on server    ${ENC2SHBAY1}
    Wait for Server to reach POST state  ${ENC2SHBAY1}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=10m  interval=20s
    Verify RIS nodes for list  ${ris_node_enc2bay1_A4}

Power off server after Reapply config
    Power off server    ${ENC2SHBAY1}

Edit the EG with different Telco
    Edit Enclosure Group    ${EDIT_EG_Telco}    api=400
    Verify Enclosure Group    ${EDIT_EG_Telco}

Remove server via Efuse
    Efuse blade by server name    ${ENC1SHBAY5}    EFuseOn
    check blade removed via GET Task    ${ENC1SHBAY5}

Update from Group on LE and Verify Ambient temp
    Update Logical Enclosure from Group    ${EDIT_LE_TELCO}
    Verify Logical Enclosure from list   ${VERIFY_EDIT_LE_TELCO}

Reinsert server via Efuse
    Efuse blade by server name    ${ENC1SHBAY5}    EFuseOff
    check blade added via GET Task    ${ENC1SHBAY5}

Power on a server and verify Ambient after Update from Group
    Power on server    ${ENC1SHBAY5}
    Wait for Server to reach POST state  ${ENC1SHBAY5}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=10m  interval=20s
    Verify RIS nodes for list  ${ris_node_enc1bay5_Telco}

Power off server bay after Update from group
    Power off server    ${ENC1SHBAY5}
    
Edit EG with to ASHRAE_A4 using API 300-- Negative
    Edit Enclosure Group    ${EDIT_EG_ASHRAE_A4}    api=300
    Verify Enclosure Group    ${EDIT_EG_Telco}

Edit LE with to ASHRAE_A3 using API 300 -- Negative
    Edit Logical Enclosure    ${EDIT_LE_A3}    api=300
    Verify Logical Enclosure from list     ${VERIFY_EDIT_LE_TELCO}

*** Keywords ***

check blade removed via GET Task
    [Arguments]  ${blade_name}
	Log to console and logfile  	\t Waiting for Blade to be removed
	${task}=    Wait Until Keyword Succeeds   5 min    1 sec    Get Task By Param     param=?filter="taskState='Running'"&filter="name='Remove'"&filter="associatedResource.resourceName='${blade_name}'"
	${task_uri} =    Get From Dictionary    ${task}    uri
	Log to console and logfile    ${task_uri}
	Wait for task2    ${task}    10 min

check blade added via GET Task
    [Arguments]  ${blade_name}
	Log to console and logfile  	\t Waiting for Blade to be added
	${task}=    Wait Until Keyword Succeeds   5 min    10 sec    Get Task By Param     param=?filter="taskState='Running'"&filter="name='Add'"&filter="associatedResource.resourceName='${blade_name}'"
	${task_uri} =    Get From Dictionary    ${task}    uri
	Log to console and logfile    ${task_uri}
	Wait for task2    ${task}    10 min

Add Base Resources
    Add FC Networks from variable    ${fc_networks}
    Add Ethernet Networks from variable    ${ethernet_networks}
    Add LIG from list    ${ligs}

Efuse blade by server name
    [Arguments]     ${server}    ${action}
    ${words} =  set variable  ${server.split(',')}
    ${enclosure} =  set variable  ${words[0]}
    ${bay} =  set variable  ${words[1]}
    ${bay} =  set variable  ${bay.strip()}
    ${bay} =  set variable  ${bay[-1]}
    Get EM IP
    Get EM Token    ${enclosure}
    EFuse Blade   ${action}     ${bay}
