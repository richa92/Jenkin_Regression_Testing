*** Settings ***
Documentation        Logical Interconnect Firmware Update and warm boot CRUD test for QXCR1001539489 and QXCR1001539769.
...                  There are two Hafnium FW upgrade scenarios that could result interconnect modules doing warm reboot instead of cold rebooting. First, upgrading FW from version X to version X (user wants to reinstall the same FW version for some reason). Second, user upgrades FW from 1.0.2-901 to 1.0.2-1005 and other compatible FW update will result into warm reboot. In both of these scenarios once modules come up after warm reboot, any changes made to Fibre Channel configuration from OneView will fail. The only recovery from this state is to login to Potash module as "root" and run come CLI commands. We don't advertise the root login to customers and it requires special instructions so that one is not a suitable recovery.
...
...                  Some setup requirements:
...                      1. A spare Potash FC uplink cable connection. This will be used in the create new Potash FC uplink set test.
...                      2. A spare server profile with FCoE connection that we can use to create new server profile as part of the tests. You can mark out that server profile in your setup data variable file so you can do that in your ./data_variables.py of this test. You will have to use serialNumberType: UserDefined and set serialNumber, uuid (wwpn and wwnn if applicable) in your ./data_variables.py.
...                      3. Another server profile in your data variable file with FCoE connection that can be deleted and recreated as part of the test to be done here. This means you'll have to modify your setup data variable file so that server profile will have a UserDefined attribute values instead of Virtual ranges.
...                      4. SSH client config must be set in TCS and OneView so it won't timeout after ~15m idle.
...                      5. SSH server in OneView must be set so it won't timeout after ~15m.
...                      6. root access to Potash (Break DUS and re-establish).
...                  This script will basically perform the following:
...                  1. Optional: Upload SPP FW Bundle.
...                  2. Use the uploaded SPP FW Bundle to update Potash interconnects FW.
...                  3. Create new Potash FC uplink set (FCoE).
...                  4. Edit existing side a uplink set - remove a port, add a port.
...                  5. Edit existing side b uplink set - remove a port, add a port.
...                  6. Delete side a uplink set and recreate that uplink set.
...                  7. Delete side b uplink set and recreate that uplink set.
...                  8. Delete FC profile connection, recreate that connection.
...                  9. Update FC profile connection.
...                  10. Enable/disable FC uplink ports on side a and side b.
...                  11. Create new Ethernet/FCOE Uplink Set.
...                  12. Create new Server Profile.
...                  13. Check for End2End traffic.
...                  14. Enable/disable uplink ports (Ethernet/FCOE).
...                  15. Negative test case to attempt toggling the stacking ports using REST API.
...                  16. Break the DUS and establish again: stacking port down/up.
...                  17. Add/remove uplink ports to/from uplink set (Ethernet/FCOE).
...                  18. Delete and create Ethernet/FCoE uplink set.
...                  19. Delete and create Server Profile.
...                  Required Arguments:
...                      -vSPP_BUNDLE_NAME:<SPP name>. The name of the SPP bundle.
...                      -V /root/ci-fit/config_files/potash_warm_reboot_data_variable.py
...                  Optional Arguments (PING_HAFILE is optional but highly recommended):
...                      -vPING_HAFILE:<path to your new profile HA file>
...                      -vSPP_BUNDLE_DIR:<path to your SPP>. If this is not specified, the script will use the existing/uploaded one provided in the required argument -vSPP_BUNDLE_NAME:<SPP name>.
...                       -v HA_FILE:/path/to/your/tcs/HA_file.conf
...                       To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                       To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                       To test for Nitro (if not specified it will try to find what you have in OneView), use -vHAFNIUM_MODEL:'Virtual Connect SE 100Gb F32 Module for Synergy'
...                       REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>
...                  Example workflow (Upload ./SPPGen10Snap1.2017_0425.124.iso and update):
...                      time pybot -T -d /tmp/logs/Potash-Warm-Reboot/ -LTRACE -vSPP_BUNDLE_DIR:./ -vSPP_BUNDLE_NAME:SPPGen10Snap1.2017_0425.124.iso -V /root/ci-fit/config_files/potash_warm_reboot_data_variable.py Potash-Warm-Reboot.robot
...                  Example workflow (Use an uploaded SPP Bundle Service Pack for ProLiant):
...                      time pybot -T -d /tmp/logs/Potash-Warm-Reboot/ -LTRACE -vSPP_BUNDLE_NAME:SPPGen10Snap1.2017_0425.124 -V /root/ci-fit/config_files/potash_warm_reboot_data_variable.py Potash-Warm-Reboot.robot

Variables           ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Library             Collections
Library             ../../resources/robustness-helper.py


*** Variables ***
${CYCLES}                       10
${FUSION_IP}                    ${APPLIANCE_IP}
${GOLDEN_FILE}                  None
${EMAIL_FROM}                   ${EMAIL_TO}
${SPP_BUNDLE_DIR}               None
${SPP_BUNDLE_NAME}              None
${SPP_BUNDLE_PATH}              ${SPP_BUNDLE_DIR}/${SPP_BUNDLE_NAME}
${CHECK_ETH_SUMMARY}            True
${SERVER_BONDING_CHECKS}        None
${DISABLE_BONDING_MULTI_TEST}   False
${HA_FILE}                      None
${UPDATE_LFCCACHE}              False
${HAFNIUM_MODEL}                ${Null}
${tbirdEnv}                     None
${FORCE_PROFILE_APPLY}          all
${STOP_SCRIPT}                  /root/.stop_script
${TCS_HAFNIUM_SSH_INTERFACE}    eth0
${REMOTE_CHECKS_TAG}            -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}       &{EMPTY}
@{REMOTE_RUN_CHECKS}            @{EMPTY}
@{AllResourcesList}             ethNets  fcNets  fcoeNets  ic  ictype  networkset  uplinkset  lig  li  encGrp  encs  servers  profiles  users
# Some ignored attributes with associated Quix
# linkPortIsolated: QXCR1001496453
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  portStatusReason  linkPortIsolated  mgmtPortState  mpFirmwareVersion  interconnectIP  ethernetSettings  stackingDomainId  lagId  personalityChecksum  remotePortDescription  remoteSystemDescription  deviceUri_ADD_romVersion  interconnectUri_ADD_interconnectIP  installState


*** Test Cases ***
Login Appliance And Set Test
    [Tags]   LOGIN
    Variable File Should Be Passed
    Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Check For New Profile HA File
    Run Keyword If   "${PING_HAFILE}" == "${null}"   Log   msg=PING_HAFILE is optional but highly recommended. Please consider using -vPING_HAFILE:<path to your HA file>.   WARN

Check For SPP Bundle Argument
    Run Keyword If   "${SPP_BUNDLE_NAME}" == "${null}"   Fail   msg=SPP_BUNDLE_NAME is a required argument. Please provide it using -vSPP_BUNDLE_NAME:<SPP Name>.

Check For ICM Names Variable
    ${icmLocStat}   ${icmLocRetval} =   Run Keyword And Ignore Error   Variable Should Exist   ${ICM_NAMES}
    Variable Should Exist   ${ICM_NAMES}   ICM_NAMES is a required variable for this test. Please make sure it is set in the data_variables.py file and try again.

Check For Target LI Variable
    ${targetLiStat}   ${targetLiRetval} =   Run Keyword And Ignore Error   Variable Should Exist   ${TARGET_LI}
    Variable Should Exist   ${TARGET_LI}   TARGET_LI is a required variable for this test. Please make sure it is set in the data_variables.py file and try again.

Robustness Potash Warm Reboot
    ${icmLocStat}   ${icmLocRetval} =   Run Keyword And Ignore Error   Variable Should Exist   ${ICM_NAMES}
    ${targetLiStat}   ${targetLiRetval} =   Run Keyword And Ignore Error   Variable Should Exist   ${TARGET_LI}
    Check Suite Requirements
    Log Variables
    Check Common Resource Attributes
    Run Optional Data Compare   ${GOLDEN_FILE}   preFWUpdate.json
    Cycle
    Run Optional Data Compare   ${GOLDEN_FILE}   postFWUpdate.json

Send Email Notification
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.


*** Keywords ***
Cycle
    [Documentation]   Run a robustness Potash Warm Reboot to test warm reboot.
    Check Filtered Common Resource Attributes
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    ${bundleUri} =   Load SPP FW Bundle   wait_task_timeout=${SPP_UPLOAD_WAIT_TIMEOUT}   wait_task_interval=${SPP_UPLOAD_WAIT_INTERVAL}
    ${ORIG_CREATE_UPLINK_SETS_FC} =   WPST Deep Copy   ${CREATE_UPLINK_SETS_FC}
    :FOR   ${x}   IN RANGE   1   ${CYCLES}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n Cycle: ${x} of ${CYCLES}   console=${True}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   Run Robustness Potash Warm Reboot Test   ${bundleUri}
    \   Check Filtered Common Resource Attributes
    \   ${CREATE_UPLINK_SETS_FC} =   WPST Deep Copy   ${ORIG_CREATE_UPLINK_SETS_FC}
    \   Set Suite Variable   ${CREATE_UPLINK_SETS_FC}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}

Run Robustness Potash Warm Reboot Test
    [Documentation]   Update ICM FW through LI, and perform CRUD operation.
    [Arguments]   ${bundleUri}
    Update Potash ICMs FW   ${bundleUri}
    Update Link Failure Count Cache
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    Create New Potash FC Network And Uplink Set
    Edit Uplink Sets To Remove And Add A Port
    Delete And Recreate FC Uplink Sets
    Delete And Recreate FC Profile Connection
    Update FC Profile Connection
    Enable Disable FC Uplink Ports
    Create New Ethernet FCoE Uplink Set
    Create New Server Profile
    Enable Disable FCoE Uplink Ports
    Attempt Toggling Stacking Ports Using REST API
    Break The DUS And Re-establish
    Add Remove Uplink Ports From Uplink Set
    Delete And Recreate Ethernet FCoE Uplink Set
    Delete And Recreate Server Profile
    Sleep And Log Reason To Console   ${END_OF_CYCLE_WAIT}   reason=Sleeping for ${END_OF_CYCLE_WAIT} to let things settle after end of a cycle.
    Bonding Interfaces Should Be In Expected States   ${Null}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${Null}   tags=${REMOTE_CHECKS_TAG}
    End Of Cycle Cleanup

Create New Potash FC Network And Uplink Set
    [Documentation]   Create new Potash FC network and uplink set (faceplate).
    Create New Network And Uplink Set   ${CREATE_FC_NETWORKS}   ${CREATE_UPLINK_SETS_FC}   ${ICM_NAMES}   message=Creating FC networks and FC uplink sets.   wait_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_interval=${CREATE_US_WAIT_INTERVAL}

Edit Uplink Sets To Remove And Add A Port
    [Documentation]   Edit existing side a/b uplink sets: remove a port, add a port.
    Edit Uplink Set   ${UPLINK_SETS_FC_NOPORT_SIDEA}   ${ICM_NAMES}   Editing existing side a uplink set - remove a port   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811_LESS1FC}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Edit Uplink Set   ${UPLINK_SETS_FC_RESTOREPORT_SIDEA}   ${ICM_NAMES}   Editing existing side a uplink set - re-add a port   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${EDIT_UPLINK_SETS_SLEEP}   reason=Sleeping for ${EDIT_UPLINK_SETS_SLEEP} to let things settle after edit uplink sets: re-add port.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Edit Uplink Set   ${UPLINK_SETS_FC_NOPORT_SIDEB}   ${ICM_NAMES}   Editing existing side b uplink set - remove a port   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811_LESS1FC}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Edit Uplink Set   ${UPLINK_SETS_FC_RESTOREPORT_SIDEB}   ${ICM_NAMES}   Editing existing side b uplink set - re-add a port   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${EDIT_UPLINK_SETS_SLEEP}   reason=Sleeping for ${EDIT_UPLINK_SETS_SLEEP} to let things settle after edit uplink sets: re-add port.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    # NOTE: For some reason I am seeing timing issue here for MPIO recovery. So, adding some 30s sleep...
    Check For Multipath   ${CHECK_MULTIPATH_NO13811}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}

Delete And Recreate FC Uplink Sets
    [Documentation]   Delete side a/b uplink sets then recreate them.
    Delete Uplink Set   ${FC_UPLINK_SET_SIDEA}   ${ICM_NAMES}   Deleting existing side a uplink set - ${FC_UPLINK_SET_SIDEA}   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811_LESS1FC}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Recreate Uplink Set   ${UPLINK_SETS_FC_RESTOREPORT_SIDEA}   ${ICM_NAMES}   Recreating deleted side a uplink set - ${FC_UPLINK_SET_SIDEA}   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${EDIT_UPLINK_SETS_SLEEP}   reason=Sleeping for ${EDIT_UPLINK_SETS_SLEEP} to let things settle after recreating uplink sets: ${FC_UPLINK_SET_SIDEA}.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    # NOTE: For some reason I am seeing timing issue here for MPIO recovery. So, adding some 30s sleep...
    Check For Multipath   ${CHECK_MULTIPATH_NO13811}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Delete Uplink Set   ${FC_UPLINK_SET_SIDEB}   ${ICM_NAMES}   Deleting existing side b uplink set - ${FC_UPLINK_SET_SIDEB}   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811_LESS1FC}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Recreate Uplink Set   ${UPLINK_SETS_FC_RESTOREPORT_SIDEB}   ${ICM_NAMES}   Recreating deleted side b uplink set - ${FC_UPLINK_SET_SIDEB}   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${EDIT_UPLINK_SETS_SLEEP}   reason=Sleeping for ${EDIT_UPLINK_SETS_SLEEP} to let things settle after recreating uplink sets: ${FC_UPLINK_SET_SIDEB}.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}

Delete And Recreate FC Profile Connection
    [Documentation]   Delete FC profile connection, recreate that connection.
    # Added negative test case by attempting to delete primary boot connection
    Delete Profile Connection With Primary Boot   ${PROFILE_TO_EDIT}   ${CONNECTION_ID_EDIT_NEGATIVE}   Deleting connection id ${CONNECTION_ID_EDIT_NEGATIVE} from ${PROFILE_TO_EDIT}.   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    ${deletedConnectionBody} =   Delete Profile Connection   ${PROFILE_TO_EDIT}   ${CONNECTION_ID_EDIT}   Deleting connection id ${CONNECTION_ID_EDIT} from ${PROFILE_TO_EDIT}.   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${POST_DELETE_PROFILE_CONNECTION_SLEEP}   reason=Sleeping for ${POST_DELETE_PROFILE_CONNECTION_SLEEP} to let things settle after delete profile connection: ${CONNECTION_ID_EDIT}.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811_LESS1BAY2}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    #NOTE: Replace Virtual to UserDefined
    Set To Dictionary   ${deletedConnectionBody}   macType=UserDefined
    Set To Dictionary   ${deletedConnectionBody}   wwpnType=UserDefined
    Log To Console   ${deletedConnectionBody}
    Create Profile Connection   ${PROFILE_TO_EDIT}   ${deletedConnectionBody}   Recreating deleted connection id ${CONNECTION_ID_EDIT} in ${PROFILE_TO_EDIT}.   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}   forceProfileApply=${FORCE_PROFILE_APPLY}
    Sleep And Log Reason To Console   ${POST_DELETE_PROFILE_CONNECTION_SLEEP}   reason=Sleeping for ${POST_DELETE_PROFILE_CONNECTION_SLEEP} to let things settle after recreate profile connection: ${CONNECTION_ID_EDIT}.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}

Update FC Profile Connection
    [Documentation]   Update FC profile connection.
    Update Profile Connection   ${PROFILE_TO_UPDATE}  ${CONNECTION_ID_UPDATE}   name   3_updated   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}   forceProfileApply=${FORCE_PROFILE_APPLY}
    Sleep And Log Reason To Console   ${POST_DELETE_PROFILE_CONNECTION_SLEEP}   reason=Sleeping for ${POST_DELETE_PROFILE_CONNECTION_SLEEP} to let things settle after update profile connection: ${CONNECTION_ID_UPDATE}.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}

Enable Disable FC Uplink Ports
    [Documentation]   Enable/disable FC uplink ports on side a and side b.
    Toggle Uplink Ports And Check For Error   ${ICM_NAMES[0]}   ${FC_UPLINK_PORT_SIDEA}   ${DISABLE_FC_UPLINK_SIDEA}   wait_task_timeout=${TOGGLE_UPLINK_WAIT_TIMEOUT}   wait_task_interval=${TOGGLE_UPLINK_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${TOGGLE_UPLINK_PORT_SLEEP}   reason=Sleeping for ${TOGGLE_UPLINK_PORT_SLEEP} to let things settle after toggling uplink ports.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811_LESS1FC}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Toggle Uplink Ports And Check For Error   ${ICM_NAMES[0]}   ${FC_UPLINK_PORT_SIDEA}   ${ENABLE_FC_UPLINK_SIDEA}   wait_task_timeout=${TOGGLE_UPLINK_WAIT_TIMEOUT}   wait_task_interval=${TOGGLE_UPLINK_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${TOGGLE_UPLINK_PORT_SLEEP}   reason=Sleeping for ${TOGGLE_UPLINK_PORT_SLEEP} to let things settle after toggling uplink ports.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Toggle Uplink Ports And Check For Error   ${ICM_NAMES[1]}   ${FC_UPLINK_PORT_SIDEB}   ${DISABLE_FC_UPLINK_SIDEB}   wait_task_timeout=${TOGGLE_UPLINK_WAIT_TIMEOUT}   wait_task_interval=${TOGGLE_UPLINK_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${TOGGLE_UPLINK_PORT_SLEEP}   reason=Sleeping for ${TOGGLE_UPLINK_PORT_SLEEP} to let things settle after toggling uplink ports.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811_LESS1FC}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Toggle Uplink Ports And Check For Error   ${ICM_NAMES[1]}   ${FC_UPLINK_PORT_SIDEB}   ${ENABLE_FC_UPLINK_SIDEB}   wait_task_timeout=${TOGGLE_UPLINK_WAIT_TIMEOUT}   wait_task_interval=${TOGGLE_UPLINK_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${TOGGLE_UPLINK_PORT_SLEEP}   reason=Sleeping for ${TOGGLE_UPLINK_PORT_SLEEP} to let things settle after toggling uplink ports.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE_NO13811}
    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811}
    Check For Multipath   ${CHECK_MULTIPATH_NO13811}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}

Create New Ethernet FCoE Uplink Set
    [Documentation]   Create new Ethernet/FCoE UplinkSet.
    Create New Uplink Set   ${UPLINK_SETS_FCOE_RESTOREPORT_SIDEA}   ${ICM_NAMES}   message=Creating new side a FCoE uplink sets from data variable file.   wait_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_interval=${CREATE_US_WAIT_INTERVAL}
    Create New Uplink Set   ${UPLINK_SETS_FCOE_RESTOREPORT_SIDEB}   ${ICM_NAMES}   message=Creating new side b FCoE uplink sets from data variable file.   wait_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_interval=${CREATE_US_WAIT_INTERVAL}

Create New Server Profile
    [Documentation]   Create new Server Profile
    Create New Server Profile And Assign Server Hardware   ${SERVER_PROFILES_NOHW}   ${SERVER_PROFILE_TO_BAY_MAP}   forceProfileApply=${FORCE_PROFILE_APPLY}
    Power On All Servers
    #NOTE: I noticed that eagle-11 bay 2 blade is slow at the start and may fail during ping.
    Sleep And Log Reason To Console   ${POST_DELETE_PROFILE_CONNECTION_SLEEP}   reason=Sleeping for ${POST_DELETE_PROFILE_CONNECTION_SLEEP} to let things settle after powering on new profiles assigned.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE}
    Check For Multipath   ${CHECK_MULTIPATH}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}

Enable Disable FCoE Uplink Ports
    [Documentation]   Enable/disable Ethernet FCoE Uplink Ports.
    Toggle Uplink Ports And Check For Error   ${ICM_NAMES[0]}   ${FCOE_UPLINK_PORT_SIDEA}   ${DISABLE_FCOE_UPLINK_SIDEA}   wait_task_timeout=${TOGGLE_UPLINK_WAIT_TIMEOUT}   wait_task_interval=${TOGGLE_UPLINK_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${TOGGLE_UPLINK_PORT_SLEEP}   reason=Sleeping for ${TOGGLE_UPLINK_PORT_SLEEP} to let things settle after toggling uplink ports.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE}
    Check For Multipath   ${CHECK_MULTIPATH_LESS1FCOE}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Toggle Uplink Ports And Check For Error   ${ICM_NAMES[0]}   ${FCOE_UPLINK_PORT_SIDEA}   ${ENABLE_FCOE_UPLINK_SIDEA}   wait_task_timeout=${TOGGLE_UPLINK_WAIT_TIMEOUT}   wait_task_interval=${TOGGLE_UPLINK_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${TOGGLE_UPLINK_PORT_SLEEP}   reason=Sleeping for ${TOGGLE_UPLINK_PORT_SLEEP} to let things settle after toggling uplink ports.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE}
    Check For Multipath   ${CHECK_MULTIPATH}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Toggle Uplink Ports And Check For Error   ${ICM_NAMES[1]}   ${FCOE_UPLINK_PORT_SIDEB}   ${DISABLE_FCOE_UPLINK_SIDEB}   wait_task_timeout=${TOGGLE_UPLINK_WAIT_TIMEOUT}   wait_task_interval=${TOGGLE_UPLINK_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${TOGGLE_UPLINK_PORT_SLEEP}   reason=Sleeping for ${TOGGLE_UPLINK_PORT_SLEEP} to let things settle after toggling uplink ports.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE}
    Check For Multipath   ${CHECK_MULTIPATH_LESS1FCOE}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Toggle Uplink Ports And Check For Error   ${ICM_NAMES[1]}   ${FCOE_UPLINK_PORT_SIDEB}   ${ENABLE_FCOE_UPLINK_SIDEB}   wait_task_timeout=${TOGGLE_UPLINK_WAIT_TIMEOUT}   wait_task_interval=${TOGGLE_UPLINK_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${TOGGLE_UPLINK_PORT_SLEEP}   reason=Sleeping for ${TOGGLE_UPLINK_PORT_SLEEP} to let things settle after toggling uplink ports.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE}
    Check For Multipath   ${CHECK_MULTIPATH}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}

Break The DUS And Re-establish
    [Documentation]   Break the DUS and establish again: Stacking port up/down 
    Break DUS And Establish Again   ${ENC_NAME}   ${ICM_NAMES[0]}   ${ICM_NAMES}   wait_configured_timeout=${STACKING_LINK_WAIT_TIMEOUT}   wait_configured_interval=${STACKING_LINK_WAIT_INTERVAL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}

Add Remove Uplink Ports From Uplink Set
    [Documentation]   Add/Remove uplink ports to/from uplink set (Ethernet/FCoE).
    Edit Uplink Set   ${UPLINK_SETS_FCOE_NOPORT_SIDEA}   ${ICM_NAMES}   Editing existing side a uplink set - remove a port   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE}
    Check For Multipath   ${CHECK_MULTIPATH_LESS1FCOE}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Edit Uplink Set   ${UPLINK_SETS_FCOE_RESTOREPORT_SIDEA}   ${ICM_NAMES}   Editing existing side a uplink set - re-add a port   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${TOGGLE_UPLINK_PORT_SLEEP}   reason=Sleeping for ${TOGGLE_UPLINK_PORT_SLEEP} to let things settle after re-adding a port.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE}
    Check For Multipath   ${CHECK_MULTIPATH}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Edit Uplink Set   ${UPLINK_SETS_FCOE_NOPORT_SIDEB}   ${ICM_NAMES}   Editing existing side b uplink set - remove a port   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE}
    Check For Multipath   ${CHECK_MULTIPATH_LESS1FCOE}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Edit Uplink Set   ${UPLINK_SETS_FCOE_RESTOREPORT_SIDEB}   ${ICM_NAMES}   Editing existing side b uplink set - re-add a port   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${TOGGLE_UPLINK_PORT_SLEEP}   reason=Sleeping for ${TOGGLE_UPLINK_PORT_SLEEP} to let things settle after re-adding a port.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE}
    Check For Multipath   ${CHECK_MULTIPATH}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}

Delete And Recreate Ethernet FCoE Uplink Set
    [Documentation]   Delete and create Ethernet/FCoE UplinkSet.
    Delete Uplink Set   ${FCOE_UPLINK_SET_SIDEA}   ${ICM_NAMES}   Deleting existing side a uplink set - ${FCOE_UPLINK_SET_SIDEA}   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE}
    Check For Multipath   ${CHECK_MULTIPATH_LESS1FCOE}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Recreate Uplink Set   ${UPLINK_SETS_FCOE_RESTOREPORT_SIDEA}   ${ICM_NAMES}   Recreating deleted side a uplink set - ${FCOE_UPLINK_SET_SIDEA}   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${EDIT_UPLINK_SETS_SLEEP}   reason=Sleeping for ${EDIT_UPLINK_SETS_SLEEP} to let things settle after recreating uplink sets: ${FCOE_UPLINK_SET_SIDEA}.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE}
    Check For Multipath   ${CHECK_MULTIPATH}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Delete Uplink Set   ${FCOE_UPLINK_SET_SIDEB}   ${ICM_NAMES}   Deleting existing side b uplink set - ${FCOE_UPLINK_SET_SIDEB}   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE}
    Check For Multipath   ${CHECK_MULTIPATH_LESS1FCOE}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Recreate Uplink Set   ${UPLINK_SETS_FCOE_RESTOREPORT_SIDEB}   ${ICM_NAMES}   Recreating deleted side b uplink set - ${FCOE_UPLINK_SET_SIDEB}   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    Sleep And Log Reason To Console   ${EDIT_UPLINK_SETS_SLEEP}   reason=Sleeping for ${EDIT_UPLINK_SETS_SLEEP} to let things settle after recreating uplink sets: ${FCOE_UPLINK_SET_SIDEB}.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE}
    Check For Multipath   ${CHECK_MULTIPATH}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}

Delete And Recreate Server Profile
    [Documentation]   Delete and create Server Profile.
    Delete Server Profiles From Variable   ${DELETE_CREATE_PROFILE}   wait_timeout=${DELETE_PROFILES_WAIT_TIMEOUT}   wait_interval=${DELETE_PROFILES_WAIT_INTERVAL}
    Add Server Profiles From Variable   ${DELETE_CREATE_PROFILE}
    Power On Servers Assigned In Profile From Variable   ${DELETE_CREATE_PROFILE}
    Sleep And Log Reason To Console   ${POST_DELETE_PROFILE_CONNECTION_SLEEP}   reason=Sleeping for ${POST_DELETE_PROFILE_CONNECTION_SLEEP} to let things settle after powering on servers.
    common.Run Sequential Ping   target_ha_file=${PING_HAFILE}
    Check For Multipath   ${CHECK_MULTIPATH}   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem   ${CHECK_READONLY}
    Fping Should Have No Loss
    Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}

End Of Cycle Cleanup
    [Documentation]   Clean things up for another test cycle.
    Delete New Potash FC Network And Uplink Set   ${CREATE_FC_NETWORKS}
    Restore Updated Profile Connection
    Delete New Server Profile
    Delete Ethernet FCoE Uplink Sets

Delete New Potash FC Network And Uplink Set
    [Documentation]   Remove new potash fc network and uplink set.
    [Arguments]   ${fcNetworks}
    Delete Uplink Set   ${CREATE_FC_NETWORK_NAME_SIDEA}   ${ICM_NAMES}   Deleting existing side a uplink set - ${CREATE_FC_NETWORK_NAME_SIDEA}   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    Delete Uplink Set   ${CREATE_FC_NETWORK_NAME_SIDEB}   ${ICM_NAMES}   Deleting existing side a uplink set - ${CREATE_FC_NETWORK_NAME_SIDEB}   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    Delete FC Networks   ${fcNetworks}   wait_timeout=${DELETE_NETWORK_WAIT_TIMEOUT}   wait_interval=${DELETE_NETWORK_WAIT_INTERVAL}

Restore Updated Profile Connection
    [Documentation]   Restore the updated profile connection.
    Update Profile Connection   ${PROFILE_TO_UPDATE}  ${CONNECTION_ID_UPDATE}   name   3   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}   forceProfileApply=${FORCE_PROFILE_APPLY}

Delete Ethernet FCoE Uplink Sets
    [Documentation]   Remove the FCoE Uplink Sets.
    Delete Uplink Set   ${FCOE_UPLINK_SET_SIDEA}   ${ICM_NAMES}   Deleting existing side a uplink set - ${FCOE_UPLINK_SET_SIDEA}   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}
    Delete Uplink Set   ${FCOE_UPLINK_SET_SIDEB}   ${ICM_NAMES}   Deleting existing side a uplink set - ${FCOE_UPLINK_SET_SIDEB}   wait_task_timeout=${CREATE_US_WAIT_TIMEOUT}   wait_task_interval=${CREATE_US_WAIT_INTERVAL}

Delete New Server Profile
    [Documentation]   Remove the server profiles with FCoE connections script created for the this test.
    Delete Server Profiles From Variable   ${SERVER_PROFILES_NOHW}   wait_timeout=${DELETE_PROFILES_WAIT_TIMEOUT}   wait_interval=${DELETE_PROFILES_WAIT_INTERVAL}   wait_interval=${DELETE_PROFILES_WAIT_INTERVAL}

Check Filtered Common Resource Attributes
    [Documentation]   Similar to Check Common Resource Attributes except LI validation is filtered for tests that could end up with different status.
    Enclosure Should Be In Expected State
    Interconnect Should Be In Expected State
    #JMP: Known issue OVD2000 LI state is always Unknown
    Logical Interconnect Should Be In Expected State   filterByName=LE-LIG 1-1 
    Logical Interconnect Should Be In Expected State   filterByName=${TARGET_LI}

