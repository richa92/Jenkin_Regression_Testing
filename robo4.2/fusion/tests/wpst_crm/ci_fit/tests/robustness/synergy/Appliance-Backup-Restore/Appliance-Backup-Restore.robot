*** Settings ***
Documentation		Appliance-Backup-Restore.robot  -  Below is the algorithm of this test suite:
...                                                      1. Optional: Get appliance config and compare it to golden JSON file
...                                                      2. Create appliance backup
...                                                      3. Download the backup
...                                                      4. Edit OneView resource configuration: Rename the top of the list EG to _renamed
...                                                      5. Perform LI Factory reset
...                                                      6. Upload and restore backup
...                                                      7. Perform some basic checks on enclosures, interconnects, and logical interconnects
...                                                      8. Optional: Check on server's MeatGrinder error from latest log, read-only FS, and/or multipath
...                                                      9. Optional: Run sequential ping
...                                                      10. Loop step 2 thru 8 in each cycle until ${CYCLES} complete
...                                                      11. Optional: Get appliance config and compare it to golden JSON file
...                     Example workflow: Run the test then send email
...                             pybot -T -d /tmp/logs/Appliance-Backup-Restore/ -LTRACE -V /root/ci-fit/config_files/eaglexx_robustness_data_variables.py Appliance-Backup-Restore.robot
...                     Required argument:
...                         -V /root/ci-fit/config_files/eaglexx_robustness_data_variables.py
...                         -v HA_FILE:/path/to/your/tcs/HA_file.conf
...                     Optional arguments:
...                         To trigger detailed resource checking, supply -vGOLDEN_FILE:<backup restore golden json> (Run test Generate-Resource-Json.robot to create golden file.)
...                         To change the sender's name, use -vEMAIL_FROM:<email address>
...                         To override the default number of cycles, use -vCYCLES:<number of cycles>
...                         To disable checking of etherchannel summary, use -vCHECK_ETH_SUMMARY:False
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                         To test for Nitro (if not specified it will try to find what you have in OneView), use -vHAFNIUM_MODEL:'Virtual Connect SE 100Gb F32 Module for Synergy'
...                         To specify sleep time to let the li factory reset complete , use -v LI_FACTORY_RESET_SLEEP_TIME:10m
...                         To specify the wait timeout and wait interval for ICMs to reach its configured state, use -v ICM_STATE_WAIT_TIMEOUT:120m and -v ICM_STATE_WAIT_INTERVAL:2s
...                         To specify the wait timeout and wait interval for LI factory reset, use -v LI_FACTORY_RESET_TIMEOUT:30m and -v LI_FACTORY_RESET_INTERVAL:2s
...                         To specify LI factory reset value, use -v LI_FACTORY_RESET_VALUE:ReapplyConfiguration
...                         REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>


Variables           ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Library             Collections
Library             ../../resources/robustness-helper.py

*** Variables ***
${APPLIANCE_IP}                    None
${FUSION_IP}                       ${APPLIANCE_IP}
${CYCLES}                          25
${GOLDEN_FILE}                     None
${EMAIL_FROM}                      ${EMAIL_TO}
${EG}                              None
${dataFilesDir}                    dataFiles
${backupFile}                      ${dataFilesDir}/backup-restore-test.bkp
${CHECK_ETH_SUMMARY}               True
${SERVER_BONDING_CHECKS}           None
${DISABLE_BONDING_MULTI_TEST}      False
${HA_FILE}                         None
${UPDATE_LFCCACHE}                 False
${HAFNIUM_MODEL}                   ${Null}
${ICM_STATE_WAIT_TIMEOUT}          200m
${ICM_STATE_WAIT_INTERVAL}         2s
${LI_FACTORY_RESET_VALUE}          ReapplyConfiguration
${LI_FACTORY_RESET_TIMEOUT}        30m
${LI_FACTORY_RESET_INTERVAL}       2s
${tbirdEnv}                        None
${STOP_SCRIPT}                     /root/.stop_script
${REMOTE_CHECKS_TAG}               -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}          &{EMPTY}
@{REMOTE_RUN_CHECKS}               @{EMPTY}
@{AllResourcesList}                ethNets  fcNets  fcoeNets  ic  ictype  networkset  uplinkset  lig  li  encGrp  encs  servers  profiles  users
# Some ignored attributes with associated Quix
# linkPortIsolated: QXCR1001496453
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  linkPortIsolated  remotePortDescription  remoteSystemDescription  deviceUri_ADD_romVersion  interconnects_ADD_ports_15_portTypeExtended  interconnects_ADD_ports_15_connectorType  interconnectUri_ADD_ports_15_portTypeExtended  interconnectUri_ADD_ports_15_connectorType

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Robustness Appliance Backup Restore
    Check Suite Requirements
    Run Keyword If   "${EG}" == "${null}"   Pick One EG And Use It
    Log Variables
    Check Common Resource Attributes
    Run Optional Data Compare   ${GOLDEN_FILE}   preBackup.json
    Run Robustness Backup And Restore   ${CYCLES}   factoryResetValue=${LI_FACTORY_RESET_VALUE}   factoryReset_timeout=${LI_FACTORY_RESET_TIMEOUT}    factoryReset_interval=${LI_FACTORY_RESET_INTERVAL}
    Run Optional Data Compare   ${GOLDEN_FILE}   postRestore.json

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.
