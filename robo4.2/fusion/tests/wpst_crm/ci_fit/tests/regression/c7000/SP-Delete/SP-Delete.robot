*** Settings ***

Documentation       Server Profile Delete           -  Below is the algorithm of this test suite:
...                                                      1. Login to the Appliance
...                                                      2. Take the appliance backup and download before going to server profile delete
...                                                      3. Get the details of server profile and count
...                                                      4. Pick a random server profile to delete
...                                                      5. Before Delete, randomly Power off the server to delete and unassign the server hardware
...                                                      6. Wait for the completion of profile delete
...                                                      7. Loop step 4 through 6 in for specified number of profiles
...                                                      8. Verify the server profile delete operation with number of profiles deleted
...                                                      9. Restore the OV from Backup
...                     Example:
...                              pybot -d /tmp/logs/SP-Delete -LTRACE -V <your test data variable file> SP-Delete.robot
...                     Required arguments:
...                         -V /root/ci-fit/config_files/est_robustness_DVF.py
...						For the data variable file  template please refer the path,  tests/wpst_crm/ci_fit/tests/robustness/resources/c7000_robustness_data_variables_template.py
...                     Optional arguments:
...                         To trigger detailed resource checking, supply -vGOLDEN_FILE:<backup restore golden json> (Run test Generate-Resource-Json.robot to create golden file)
...                         To change the sender's name, use -vEMAIL_FROM:<email address>



Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../../robustness/resources/common.robot
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Library             Collections
Library             json
Library             FusionLibrary
Library             RoboGalaxyLibrary
Library             SSHLibrary


*** Variables ***

${FUSION_IP}                    ${APPLIANCE_IP}
${Profiles}                     2
${GOLDEN_FILE}                  None
${EMAIL_FROM}                   ${EMAIL_TO}
${ENC}                          None
${ONE_TIME_PASS}                None
${tbirdEnv}                     None
${dataFilesDir}                 dataFiles
${backupFile}                   ${dataFilesDir}/backup-restore-test.bkp
${SP_DELETE_WAIT_TIMEOUT}       5 min
${SP_DELETE_WAIT_INTERVAL}      1 min

*** Test Cases ***

Login Appliance And Set Test
   [Tags]    LOGIN
   Set Log Level    TRACE
   Authenticate And Set Login

VerIfy for alerts or warnings
   [Tags]    VERIfYALERTS
   Set Log Level    TRACE
   Check Common Resource Attributes

Create Backup of the appliance
   [Tags]    OV_BACKUP
   Set Log Level    TRACE
   Create Appliance Backup Download And Data Compare   wait_task_timeout=${CREATE_BACKUP_WAIT_TIMEOUT}   wait_task_interval=${CREATE_BACKUP_WAIT_INTERVAL}
   Log    \nAppliance Backup is taken successfully    console=${True}

SP Delete
   [Tags]    SPDelete
   ${SP_org} =    Fusion Api Get Server Profiles
   ${profile_count_org} =    Get From Dictionary    ${SP_org}    count
   Log    \nNumber of Server Profiles before Delete : ${profile_count_org}    console=${True}
   :FOR    ${INDEX}    IN RANGE    1    ${Profiles}+1
   \   ${SP} =    Fusion Api Get Server Profiles
   \   ${profile_count} =    Get From Dictionary    ${SP}    count
   \   ${random_profile_no} =    Evaluate    random.randint(0, ${profile_count}-1)    random
   \   ${random_profile_name} =    Get from Dictionary    ${SP['members'][${random_profile_no}]}    name
   \   ${random_profile_uri} =    Get from Dictionary    ${SP['members'][${random_profile_no}]}    uri
   \   ${random_hardware_uri} =    Get from Dictionary    ${SP['members'][${random_profile_no}]}    serverHardwareUri
   \   Log    \nSelected the profile ${random_profile_name} for Delete    console=${True} 
   \   Run Keyword If    '${random_hardware_uri}' != 'None'    common.Power Off Server Uri    ${random_hardware_uri}    powerControl=PressAndHold
   \   ${check} =    Evaluate    random.choice(['True','False'])    random
   \   ${profile} =    Create List    ${SP['members'][${random_profile_no}]}
   \   Run Keyword If    '${check}' == 'True' and '${random_hardware_uri}' != 'None'    common.Unassign Server Profiles    ${profile}
   \   SP Delete    ${random_profile_uri}    ${random_profile_name}
   ${SP_after_delete} =    Fusion Api Get Server Profiles
   ${profile_count_after_delete} =    Get From Dictionary    ${SP_after_delete}    count
   Log    \nNumber of Server Profiles after Delete : ${profile_count_after_delete}   console=${True}     
   Run Keyword If    ${profile_count_org}==${profile_count_after_delete}+${Profiles}    Log    \nVerified Successfully    console=${True}


Restore the appliance
  [Tags]   OV_RESTRE
  Set Log Level    TRACE
  ${EG} =      Pick One EG And Use It
  Upload Restore Backup And Perform Data Compare   upload_task_timeout=${UPLOAD_BACKUP_WAIT_TIMEOUT}   upload_task_interval=${UPLOAD_BACKUP_WAIT_INTERVAL}
  ...               restore_task_timeout=${RESTORE_BACKUP_WAIT_TIMEOUT}   restore_task_interval=${RESTORE_BACKUP_WAIT_INTERVAL}
  
Send Email Notification
    [Tags]    SEND_A_MAIL
    Set Log Level    TRACE
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.

*** Keywords ***

SP Delete
     [Documentation]    Delete the selected profile
     [Arguments]    ${profile_delete_uri}    ${random_profile_name}
     ${resp1} =    Fusion Api Delete Server Profile    uri=${profile_delete_uri}
     Should Be Equal as Strings    ${resp1['status_code']}    202    msg=Failed to initiate delete server profile ${random_profile_name}    
     ${task}    fusion_api_appliance_setup.Wait For Task    ${resp1}    ${SP_DELETE_WAIT_TIMEOUT}    ${SP_DELETE_WAIT_INTERVAL}
     Should Be Equal as Strings    ${task['status_code']}    200    msg=Failed to delete server profile ${random_profile_name}