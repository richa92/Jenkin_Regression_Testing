*** Settings ***
Documentation   Positive edit test: Test profile configuration changes with template compliance

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
TS0 Create the Template
    [Documentation]  Create the template that will be used for the profile compliance tests
    ${resp} =  Add Server Profile Template  ${template_with_nonvc_connection}
    log to console  ${resp}
	Wait For Task2  ${resp}  timeout=2400  interval=2

TS1 Create a Profile from the Template
    ${resps} =    Add Server Profiles from variable    ${profile_from_template_with_nonvc_connection}
    Wait for Task2  ${resps}  timeout=2400  interval=2

TS2 Verify the Profile
    Verify Server Profile  ${profile_from_template_with_nonvc_connection_validator}

TS3 Edit the Profile
    [Documentation]  Test edits by changing the port ID
    ${resp} =  Edit Server Profile  ${profile_from_template_with_nonvc_connection_edit}
    log to console  ${resp}
	Wait For Task2  ${resp}  timeout=2400  interval=2

TS4 Verify the Compliance Messages
    [Documentation]  Verify the non-compliance messages
	Verify Server Profile Compliance  ${profile_from_template_with_nonvc_connection_edit_non_compliance}

TS5 Delete the Profile
    ${resp} =  Remove Server Profile  ${profile_from_template_with_nonvc_connection_to_delete}  True
    log to console  ${resp}
	Wait For Task2  ${resp}  timeout=2400  interval=2

TS6 Delete the Template
    ${resp} =  Remove Server Profile Template  ${template_with_nonvc_connection_to_delete}
    log to console  ${resp}
	Wait For Task2  ${resp}  timeout=2400  interval=2

*** Keywords ***
Initialize the Variables and Log In
    [Documentation]  Set the log level to TRACE, log the variables and login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

