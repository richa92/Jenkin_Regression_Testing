*** Settings ***
Documentation		Appliance-Backup-Restore.robot  -  Below is the algorithm of this test suite:
...                                                      1. Optional: Get appliance config and compare it to golden JSON file
...                                                      2. Create appliance backup
...                                                      3. Download the backup
...                                                      4. Edit OneView resource configuration: Rename the top of the list EG to _renamed
...                                                      5. Upload and restore backup
...                                                      6. Perform some basic checks on enclosures, interconnects, and logical interconnects
...                                                      7. Optional: Check on server's MeatGrinder error from latest log, read-only FS, and/or multipath
...                                                      8. Optional: Run sequential ping
...                                                      9. Loop step 2 thru 8 in each cycle until ${CYCLES} complete
...                                                      10. Optional: Get appliance config and compare it to golden JSON file
...                     Example:
...                             time pybot -T -d /tmp/logs/Appliance-Backup-Restore -LTRACE -V <your test data variable file> Appliance-Backup-Restore.robot
...                     Required arguments:
...                         -V /root/ci-fit/config_files/eaglexx_test_data_variables.py
...                         -v HA_FILE:/path/to/your/tcs/HA_file.conf
...                     Optional arguments:
...                         To trigger detailed resource checking, supply -vGOLDEN_FILE:<backup restore golden json> (Run test Generate-Resource-Json.robot to create golden file)
...                         To change the sender's name, use -vEMAIL_FROM:<email address>
...                         To override the default number of cycles, use -vCYCLES:<number of cycles>
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>

Variables           ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Library             Collections
Library             ../../resources/robustness-helper.py

*** Variables ***
${FUSION_IP}                    ${APPLIANCE_IP}
${CYCLES}                       10
${GOLDEN_FILE}                  None
${EMAIL_FROM}                   ${EMAIL_TO}
${EG}                           None
${dataFilesDir}                 dataFiles
${backupFile}                   ${dataFilesDir}/backup-restore-test.bkp
${CHECK_ETH_SUMMARY}            False
${SERVER_BONDING_CHECKS}        None
${DISABLE_BONDING_MULTI_TEST}   True
${HA_FILE}                      None
${UPDATE_LFCCACHE}              False
${tbirdEnv}                     None
${STOP_SCRIPT}                  /root/.stop_script
${REMOTE_CHECKS_TAG}            -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}       &{EMPTY}
@{REMOTE_RUN_CHECKS}            @{EMPTY}
@{AllResourcesList}             ethNets  fcNets  fcoeNets  ic  ictype  networkset  uplinkset  lig  li  encGrp  encs  servers  profiles  users
# Some ignored attributes with associated Quix
# linkPortIsolated: QXCR1001496453
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  linkPortIsolated  mgmtPortState  interconnectIP  settingId  optionId  loginsCount  address  deviceUri_ADD_romVersion

*** Test Cases ***
Login Appliance And Set Test
   Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Robustness Appliance Backup Restore
    Run Keyword If   "${APPLIANCE_IP}" == "${Null}"   Fail   msg=APPLIANCE_IP was not specified in the command or set in data variable file.
    Run Keyword If   "${SERVER_BONDING_CHECKS}" != "${Null}" and '${SERVER_HAFILE}' == '${Null}'   Fail   msg=SERVER_BONDING_CHECKS was enabled but SERVER_HAFILE is not set. Please set the SERVER_HAFILE in your pybot command or data variable file.
    Run Keyword If   "${DISABLE_BONDING_MULTI_TEST}" == "${False}" and '${HA_FILE}' == '${Null}' or '${SERVER_HAFILE}' == '${Null}'   Fail   msg=DISABLE_BONDING_MULTI_TEST is False but HA_FILE or SERVER_HAFILE is not set. Please set the HA_FILE and SERVER_HAFILE in your pybot command or data variable file.
    Run Keyword If   "${HA_FILE}" != "${Null}"   OperatingSystem.File Should Exist   ${HA_FILE}
    # There is an open issue in RF than when fixed can give us flexibilty of changing data variable file on the fly.
    # https://github.com/robotframework/robotframework/issues/2101
    # ${data_variable_files} =   Variable File Should Be Passed
    # Set Suite Variable   ${data_variable_files}   ${data_variable_files}
    Variable File Should Be Passed
    Run Keyword If   "${EG}" == "${null}"   Pick One EG And Use It
    Log Variables
    Check Common Resource Attributes
    Run Optional Data Compare   ${GOLDEN_FILE}   preBackup.json
    Run Robustness Backup And Restore   ${CYCLES}
    Run Optional Data Compare   ${GOLDEN_FILE}   postBackup.json

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.

