*** Settings ***
Documentation   Positive tests: Create a profile with no connections.  Edit to add unmanaged connections

Library  	        BuiltIn
Library		        FusionLibrary
Library		        Collections
Library             json
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ./../global_variables.robot
Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Initialize the Variables and Log In
...                 AND     Set Suite Variable      ${WFT2_CONTINUE_ON_ERROR}   ${TRUE}

Suite Teardown      Run Keywords    Fusion Api Logout Appliance

*** Variables ***
${APPLIANCE_IP}     ${None}
${DATA_FILE}        ${None}

*** Test Cases ***
TS0 Create the Profile
    [Tags]   TS0
    ${resp} = 	Add Server Profile	${OVS51247_unassigned_T1}
	Wait For Task2  ${resp}     timeout=2400    interval=2

TS1 Edit the Profile
    [Tags]    TS1
    ${new_name} =    Set Variable    OVF518_OVS51247_unassigned_add_unman_conn
    ${resp} =  Edit Server Profile  ${OVS51247_edit_unassigned_T1}    newname=${new_name}
    log    ${resp}    console=true
	Wait For Task2  ${resp}  timeout=2400  interval=2
	Set To Dictionary    ${OVS51247_edit_unassigned_T1}    name    ${new_name}
    Verify Server Profile  ${OVS51247_edit_unassigned_T1}

*** Keywords ***
Initialize the Variables and Log In
    [Documentation]  Set the log level to TRACE, log the variables and login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

