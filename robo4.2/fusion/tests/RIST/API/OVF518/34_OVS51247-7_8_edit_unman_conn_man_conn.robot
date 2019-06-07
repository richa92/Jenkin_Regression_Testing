*** Settings ***
Documentation   Positive tests: Edit unassigned SP with man and unman conn, remove unmanaged connections.

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
TS0 Create the Profiles
    [Tags]   TS0
    ${resp} = 	Add Server Profiles from variable	${OVS51247_add_unassigned_w_unman_w_both_T7_8}
	Wait For Task2  ${resp}     timeout=2400    interval=2

TS1 Edit the Profiles
    [Tags]    TS1
    ${resp} =  Edit Server Profiles from variable    ${OVS51247_edit_unassigned_w_unman_w_both_T7_8}
    log    ${resp}    console=true
	Wait For Task2  ${resp}  timeout=2400  interval=2
	:FOR    ${profile}    IN    @{OVS51247_edit_unassigned_w_unman_w_both_T7_8}
	\    Verify Server Profile  ${profile}

*** Keywords ***
Initialize the Variables and Log In
    [Documentation]  Set the log level to TRACE, log the variables and login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

