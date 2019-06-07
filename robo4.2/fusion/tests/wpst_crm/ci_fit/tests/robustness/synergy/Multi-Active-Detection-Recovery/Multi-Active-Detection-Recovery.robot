*** Settings ***
Documentation        MultiActive Detection feature (MAD)
...                  This test case induces stacking link failures to cause multiple Master interconnects in an LI domain. MAD detection and recovery will be verified on CI-FIT configuration with traffic flowing (ping and/or fping, MeatGrinder, IOMeter, etc). No network outage should occur unless traffic flows over stacking links. See ALM for more details...
...                  IMPORTANT NOTE: This test requires root access to your Potash interconnects.
...                        To test for Nitro (if not specified it will try to find what you have in OneView), use -vHAFNIUM_MODEL:'Virtual Connect SE 100Gb F32 Module for Synergy'
...                        REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>
...
...                  Example syntax:
...                      time pybot -T -d /tmp/logs/MAD/ -LTRACE -V/root/ci-fit/config_files/eaglexx_robustness_data_variables.py Multi-Active-Detection-Recovery.robot

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
${STOP_SCRIPT}                  /root/.stop_script
${CHECK_ETH_SUMMARY}            True
${SERVER_BONDING_CHECKS}        None
${DISABLE_BONDING_MULTI_TEST}   False
${HA_FILE}                      None
${UPDATE_LFCCACHE}              False
${HAFNIUM_MODEL}                ${Null}
${tbirdEnv}                     None
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
    Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Robustness MultiActive Detection And Recovery
    Check Suite Requirements
    Log Variables
    Check Common Resource Attributes
    Check For MeatGrinder Error
    Check For Multipath   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Check For Server In Read Only Filesystem
    common.Run Sequential Ping
    Run Optional Data Compare   ${GOLDEN_FILE}   preMAD.json
    Run Robustness MultiActive Detection And Recovery    ${CYCLES}   ${TARGET_ENC}   ${TARGET_ICM}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    Run Optional Data Compare   ${GOLDEN_FILE}   postMAD.json

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.

