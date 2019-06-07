*** Settings ***
Documentation   Positive edit test: Test various profile configuration changes using PUT

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
    [Documentation]  Create the initial profile that will be used for the edit tests
    ${resp} =  Add Server Profile	${profile_with_nonvc_connection}
    log    ${resp}    console=true
	Wait For Task2  ${resp}  timeout=2400  interval=2

TS1 Edit the Profile
    [Documentation]  Test edits by adding an Ethernet connection
    ${resp} =  Edit Server Profile  ${profile_with_nonvc_connection_edit_add_connection}
    log    ${resp}    console=true
	Wait For Task2  ${resp}  timeout=2400  interval=2
    Verify Server Profile  ${profile_with_nonvc_connection_edit_add_connection_validator}

TS2 Edit the Profile
    [Documentation]  Test edits by changing params on the non-VC connection
    ${resp} =  Edit Server Profile  ${profile_with_nonvc_connection_edit_change_connection_params}
    log    ${resp}    console=true
	Wait For Task2  ${resp}  timeout=2400  interval=2
	Verify Server Profile  ${profile_with_nonvc_connection_edit_change_connection_params_validator}

TS3 Edit the Profile
    [Documentation]  Test edits by deleting the connections
    ${resp} =  Edit Server Profile  ${profile_with_nonvc_connection_delete_connections}
    log    ${resp}    console=true
	Wait For Task2  ${resp}  timeout=2400  interval=2
	Verify Server Profile  ${profile_with_nonvc_connection_delete_connections_validator}

TS4 Edit the Profile
    [Documentation]  Test edits by adding a volume, VC and non-VC connections, and storage paths to both connections
    ${resp} =  Edit Server Profile  ${profile_with_nonvc_connection_edit_add_volume_with_storage_paths}
    log    ${resp}    console=true
	Wait For Task2  ${resp}  timeout=2400  interval=2
	Verify Server Profile  ${profile_with_nonvc_connection_edit_add_volume_with_storage_paths_validator}

TS5 Edit the Profile
    [Documentation]  Test edits by deleting the non-VC connection and checking the storage paths
    ${resp} =  Edit Server Profile  ${profile_with_nonvc_connection_edit_delete_nonvc_connection}
    log    ${resp}    console=true
	Wait For Task2  ${resp}  timeout=2400  interval=2
	Verify Server Profile  ${profile_with_nonvc_connection_edit_delete_nonvc_connection_validator}

TS6 Delete the Profile
    ${resp} =  Remove Server Profile  ${profile_with_nonvc_connection_to_delete}
    log    ${resp}    console=true
	Wait For Task2  ${resp}  timeout=2400  interval=2

*** Keywords ***
Initialize the Variables and Log In
    [Documentation]  Set the log level to TRACE, log the variables and login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

