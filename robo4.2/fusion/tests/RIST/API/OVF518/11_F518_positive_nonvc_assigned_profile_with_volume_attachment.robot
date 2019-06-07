*** Settings ***
Documentation   Positive tests: Create a profile with a non-VC volume attachment and
...             apply to a server.

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
    Power off All Servers  control=PressAndHold
    ${resp} = 	Add Server Profile	${nonvc_valid_assigned_profile_with_volume_attachments}
    log    ${resp}    console=true
	Wait For Task2  ${resp}     timeout=2400    interval=10

*** Keywords ***
Initialize the Variables and Log In
    [Documentation]  Set the log level to TRACE, log the variables and login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

