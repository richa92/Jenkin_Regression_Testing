*** Settings ***
Documentation		Appliance-Reboot.robot  -  Perform appliance reboot using REST API and check that resources are in expected states.
...                     Example:
...                              time pybot -T -d /tmp/logs/Appliance-Reboot.robot -LTRACE -V /root/ci-fit/config_files/eaglexx_test_data_variables.py Appliance-Reboot.robot
...                     Required argument:
...                         -V /root/ci-fit/config_files/eaglexx_test_data_variables.py
...                         -v HA_FILE:/path/to/your/tcs/HA_file.conf
...                     Optional arguments:
...                         To trigger detailed resource checking, supply -vGOLDEN_FILE:<golden json> (Run test Generate-Resource-Json.robot to create golden file)
...                         To change the sender's name, use -vEMAIL_FROM:<email address>
...                         To override the default number of cycles, use -vCYCLES:<number of cycles>
...                         To update link failure count cache, use -vUPDATE_LFCCACHE:True
...                         To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                         REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>

Variables           ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Library		    Collections
Library             ../../resources/robustness-helper.py

*** Variables ***
${CYCLES}                       18
${FUSION_IP}                    ${APPLIANCE_IP}
${GOLDEN_FILE}                  None
${EMAIL_FROM}                   ${EMAIL_TO}
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
@{ignoreList}                   uuid  virtualUuid  installedStateTimestamp  romVersion  uidState  refreshState  roles  ipAddressType  ipAddress  remoteSupportSettings  assetTag  enclosureUris_ADD_refreshState  deviceUri_ADD_refreshState  portTypeExtended  hpSmartUpdateToolStatus  connectorType  settingId  optionId  address  logins  portId  remoteSystemName  deviceUri_ADD_romVersion  migrationState

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Robustness Appliance Reboot
    Run Keyword If   "${APPLIANCE_IP}" == "${Null}"   Fail   msg=APPLIANCE_IP was not specified in the command or set in data variable file.
    Run Keyword If   "${SERVER_BONDING_CHECKS}" != "${Null}" and '${SERVER_HAFILE}' == '${Null}'   Fail   msg=SERVER_BONDING_CHECKS was enabled but SERVER_HAFILE is not set. Please set the SERVER_HAFILE in your pybot command or data variable file.
    Run Keyword If   "${DISABLE_BONDING_MULTI_TEST}" == "${False}" and '${HA_FILE}' == '${Null}' or '${SERVER_HAFILE}' == '${Null}'   Fail   msg=DISABLE_BONDING_MULTI_TEST is False but HA_FILE or SERVER_HAFILE is not set. Please set the HA_FILE and SERVER_HAFILE in your pybot command or data variable file.
    Run Keyword If   "${HA_FILE}" != "${Null}"   OperatingSystem.File Should Exist   ${HA_FILE}
    Variable File Should Be Passed
    Log Variables
    Check Common Resource Attributes
    Run Optional Data Compare   ${GOLDEN_FILE}   appliance.json
    Run Robustness Appliance Reboot    ${CYCLES}
    Run Optional Data Compare   ${GOLDEN_FILE}   appliance.json

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.

