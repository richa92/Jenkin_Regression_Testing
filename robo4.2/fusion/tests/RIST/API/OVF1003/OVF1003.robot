*** Settings ***
Documentation                   OVF1003 ensure satizitze starts and finishes on drives before they are returned to available drives.

Library             FusionLibrary
Library             BuiltIn
Library             Collections
Library             json
Library             Dialogs
Resource            ../global_variables.robot
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Variables           ${DATA_FILE}



Suite Setup         Run Keywords    Initialize the Variables and Log In as Administrator
Suite Teardown      Run Keywords    Remove all Profiles and log out


*** Variables ***
${DATA_FILE}        ./Regression_Data.py
${APPLIANCE_IP}     16.114.209.223

*** Test Cases ***

OVF1003 TS0 - Power Off Servers in profiles
    Power Off Servers in Profiles  ${all_profiles}



OVF1003 TS1 - apply server profile templates
    ${resplist} =    Add Server Profile Templates from variable   ${server_profile_templates}
    Wait For Task2  ${resp_list}  timeout=600  interval=10



OVF1003 TS2 - add single drive profile and verify its creation
    ${resp_list} =  Add Server Profile   ${SP_1drive_compatible}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

    Verify Server Profile  	${Verify_SP_1drive_compatible}

OVF1003 TS2 - edit profile and add jbod with 2 drives and verify edit was successful
    ${resplist} =    Edit Server Profile   ${SP_AddDrive}
    Wait For Task2  ${resp_list}  timeout=600  interval=10

    Verify Server Profile  	${SP_AddDrive_Verify}

OVF1003 TS2 - remove serverprofile and wait for completeion or removal
    ${resplist} =    Remove Server Profile   ${SP_AddDrive}
    Wait For Task2  ${resp_list}  timeout=600  interval=10

OVF1003 TS2 - check the drives and ensure that correct drive show EraseInProgress
    wait until keyword succeeds   10 min   30 sec   Verify Drive Enclosures from list   ${verify_drive_enclosures_inProgressTs0}

OVF1003 TS2 - check the drives and ensure that correct drive show EraseCompleted
    wait until keyword succeeds   75 min   30 sec   Verify Drive Enclosures from list   ${verify_drive_enclosures_eraseCompletedTs0}



OVF1003 TS3 - add serverProfile from template that has 3 different jbods and verify the serverprofile was created properly
    ${resplist} =    Add Server Profile Templates from variable   ${SPT_manyDrives_compatible}
    Wait For Task2  ${resp_list}  timeout=600  interval=10

    ${resp_list} =  Add Server Profile   ${SP2_manyDrives_compatible}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

    Verify Server Profile  	${Verify_SP2_manyDrives_compatible}

    Verify Drive Enclosures from list   ${verify_de_before_removing_jbod}
OVF1003 TS3 - unassign the profile, verify unassignment and then re-assign
    ${resplist} =    Edit Server Profile   ${Edit_SP2_unassign}
    Wait For Task2  ${resp_list}  timeout=600  interval=10

    Verify Server Profile  	${Edit_SP2_unassign}

    Verify Drive Enclosures from list   ${verify_de_before_removing_jbod}

    ${resplist} =    Edit Server Profile   ${Edit_SP2_reassign}
    Wait For Task2  ${resp_list}  timeout=600  interval=10

    Verify Server Profile  	${Edit_SP2_reassign}

    Verify Drive Enclosures from list   ${verify_de_before_removing_jbod}

OVF1003 TS3 - edit the sp and remove jbod1 and ensure the erase process starts
    ${resplist} =    Edit Server Profile   ${edit_sp_remove_jbod1}
    Wait For Task2  ${resp_list}  timeout=600  interval=10

    Verify Server Profile  	${edit_sp_remove_jbod1}

    wait until keyword succeeds   20 min   30 sec   Verify Drive Enclosures from list   ${verify_de_after_remove_jbod1}

OVF1003 TS3 - remove the serverProfile and and wait until removal has finished
    ${resplist} =    Remove Server Profile   ${edit_sp_remove_jbod1}
    Wait For Task2  ${resp_list}  timeout=600  interval=10

OVF1003 TS3 - check the drives of the 3 jbods and ensure that correct drives show EraseInProgress
    wait until keyword succeeds   20 min   30 sec   Verify Drive Enclosures from list   ${verify_drive_enclosures_inProgressTs1}

OVF1003 TS3 - check the drives of the 3 jbods and ensure that correct drives show EraseCompleted
    wait until keyword succeeds   75 min   30 sec   Verify Drive Enclosures from list   ${verify_drive_enclosures_eraseCompletedTs1}



OVF1003 TS4 - edit a template and verify the changes have been made
    ${resplist} =    Edit Server Profile Template   ${edit_spt}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

    Verify Server Profile Templates   ${verify_server_profile_templates2}



*** Keywords ***
Initialize the Variables and Log In as Administrator
    [Documentation]  Set the log level to TRACE, initialize the variables and, login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}     ${admin_credentials}

Remove all Profiles and log out
    [Documentation]  Remove all SP's and, remove all SPT's
    ${resplist} =    Remove All Server Profiles Async
    Wait For Task2    ${resplist}    timeout=600    interval=5
    Remove All Server Profile Templates
    Fusion Api Logout Appliance
