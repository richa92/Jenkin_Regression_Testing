*** Settings ***
Documentation		Check-Server  -  Check server(s) for MeatGrinder error in the latest log, read-only filesystem, multipath, ping, Hafnium ISS Crash, fping loss, all Hafnium ports are linked, and servers bonding interfaces based on a defined checks (default is permanent hw addr, speed, and status).
...                     NOTE: Make sure you have IP-to-path_counts mapping (see example in data_variables.py).
...                     Example: pybot -T -d /tmp/logs/Check-Server.robot -LTRACE -V /root/ci-fit/config_files/eaglexx_robustness_data_variables.py -vCYCLES:1 Check-Server.robot
...                     Some of the optional arguments:
...                        To override data file appliance IP, use -vAPPLIANCE_IP:<OneView IP>
...                        To override data file email address for end of execution, use -vEMAIL_FROM:<valid.email@hpe.com>
...                        To override the default cycle of 1, use -vCYCLE:<number of cycles>
...                        To override end of cycle wait time, use -vEND_OF_CYLE_WAIT:<time in RF format, example 20s>
...                        To disable check ethernet summary, use -vCHECK_ETH_SUMMARY:False
...                        To enable server bonding interfaces based on specific check_bonds.py parameter, use -vSERVER_BONDING_CHECKS:<valid check_bonds.py arguments, this can also be set in data file>
...                        To disable bonding interface multi-test (NOT RECOMMENDED), use -vDISABLE_BONDING_MULTI_TEST:True
...                        To set your HA_FILE, use -vHA_FILE:<path to your HA file>
...                        To specify an offline Hafnium interconnect, use -vPOTASH_URI:</rest/interconnects/{id}>
...                        To initialize or sync up Link Failure Count Cache to that of the server, use -vUPDATE_LFCCACHE:Tru
...                        To indicate that the script was run from a remote caller (multi-TCS setup), use -vREMOTE_RUN:True
...                        To ignore bonding attributes during multi-test, set your IGNORE_BOND_ATTRIBUTES in the data file (examples provided in sysnergy_data_variables_template.py)
...                        To increment link failure count based on offline Hafnium interconnect, use -vINCREMENT_LFCCACHE:True
...                        To test for Nitro (if not specified it will try to find what you have in OneView), use -vHAFNIUM_MODEL:'Virtual Connect SE 100Gb F32 Module for Synergy'
...                        REMOTE_CHECKS_TAG is the variable use to define what checks will be ran in the remote TCS (Default: -i PING -i BONDING_MULTI_TEST). To override it, use -vREMOTE_CHECKS_TAG:<tags or "" to run all>
...    You can also use custom variables for customized checks. Below are examples on how you modify the script to pass a custom variable from your data file:
...    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO4}
...    Check For Multipath   ${CHECK_MULTIPATH_NO4}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
...    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO4}
...    common.Run Sequential Ping   ha_file=${PING_HAFILE_NO4}
...    Server Interfaces Should Be Up
...    Check For MeatGrinder Error   ${CHECK_MEATGRINDER_NO13811_4}
...    Check For Server In Read Only Filesystem   ${CHECK_READONLY_NO13811_4}
...    Check For Multipath   ${CHECK_MULTIPATH_NO13811_4}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
...    common.Run Sequential Ping   ha_file=${PING_HAFILE_NO13811_4}



Variables           ../resources/data_variables.py
Resource            ../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../resources/common.robot
Library             ../resources/robustness-helper.py
Library		    Collections
Library             OperatingSystem

*** Variables ***
${FUSION_IP}                    ${APPLIANCE_IP}
${EMAIL_FROM}                   ${EMAIL_TO}
${CYCLES}                       1
${END_OF_CYLE_WAIT}             15s
${STOP_SCRIPT}                   /tmp/.stop_script
${CHECK_ETH_SUMMARY}            True
${SERVER_BONDING_CHECKS}        None
${DISABLE_BONDING_MULTI_TEST}   False
${HA_FILE}                      None
${POTASH_URI}                   ${Null}
${UPDATE_LFCCACHE}              False
${tbirdEnv}                     None
${REMOTE_RUN}                   False
${HAFNIUM_MODEL}                ${Null}
${TCS_HAFNIUM_SSH_INTERFACE}    eth0
${INCREMENT_LFCCACHE}           ${False}
${REMOTE_CHECKS_TAG}            -i PING -i BONDING_MULTI_TEST
&{IGNORE_BOND_ATTRIBUTES}       &{EMPTY}

*** Test Cases ***
Login Appliance And Set Test
    [Tags]   BASIC   LOGIN   UPDATE_LFCCACHE   CYCLIC   RESOURCE   MULTIPATH   BONDING_MULTI_TEST   BONDING   ISS   HAFNIUM_LINKS   MULTI_TCS
    Authenticate And Set Login

Update Link Failure Count Cache
    [Tags]   UPDATE_LFCCACHE
    Run Keyword If   ${UPDATE_LFCCACHE} is ${True}   Update Link Failure Count Cache

Cyclic Check Servers And Interconnects
    [Tags]   BASIC   CYCLIC
    Pass Execution If   ${CYCLES} <= ${1}   Skipping cyclic check servers and interconnects. Use -vCYCLES:2 (or more) to perform this test.
    Check Suite Requirements
    :FOR   ${x}  IN RANGE   1   ${CYCLES}
    \   Log   \n Cycle: ${x} of ${CYCLES}   console=${True}
    \   Exit Test When Flag File Exists   flag_file=${STOP_SCRIPT}
    \   Check Common Resource Attributes
    \   Check For MeatGrinder Error
    \   Check For Multipath   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    \   Check For Server In Read Only Filesystem
    \   common.Run Sequential Ping
    # Links and bonding interface checks
    \   Bonding Interfaces Should Be In Expected States   ${POTASH_URI}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}   update_link_failure_count=${INCREMENT_LFCCACHE}
    \   Fping Should Have No Loss
    \   Run Keyword If   ${REMOTE_RUN} == ${False}   Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    \   Run Keyword If   ${REMOTE_RUN} == ${False}   All Etherchannel Summary Ports Should Be Linked   iface=${TCS_HAFNIUM_SSH_INTERFACE}
    \   Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}
    \   ${REMOTE_RUN_CHECKS} =   Get Variable Value   ${REMOTE_RUN_CHECKS}   @{EMPTY}
    \   Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${POTASH_URI}   upd_lfccache=${UPDATE_LFCCACHE}   tags=${REMOTE_CHECKS_TAG}

Check Common Resource Attributes From Data File
    [Tags]   BASIC   RESOURCE
    Check Suite Requirements
    Exit Test When Flag File Exists
    Check Common Resource Attributes

Check For MeatGrinder Error On Servers Listed in Data File
    [Tags]   MEATGRINDER
    Exit Test When Flag File Exists
    Check For MeatGrinder Error

Check For Multipath On Servers Listed in Data File
    [Tags]   BASIC   MULTIPATH
    Exit Test When Flag File Exists
    Check For Multipath   hafnium_icm_model=${HAFNIUM_MODEL}   iface=${TCS_HAFNIUM_SSH_INTERFACE}

Check For Server In Read-only FileSystem
    [Tags]   BASIC   READONLY
    Exit Test When Flag File Exists
    Check For Server In Read Only Filesystem

Run Sequential Ping
    [Tags]   BASIC   PING
    Check Suite Requirements
    Exit Test When Flag File Exists
    common.Run Sequential Ping

Run Multi-test on Bonding Interfaces
    [Tags]   BASIC   BONDING_MULTI_TEST
    Check Suite Requirements
    Exit Test When Flag File Exists
    Bonding Interfaces Should Be In Expected States   ${POTASH_URI}   ignoreAttributes=${IGNORE_BOND_ATTRIBUTES}   update_link_failure_count=${INCREMENT_LFCCACHE}

Check Fping for Loss
    [Tags]   FPING
    Exit Test When Flag File Exists
    Fping Should Have No Loss

Check For ISS Crash
    [Tags]   BASIC   ISS
    Exit Test When Flag File Exists
    Run Keyword If   ${REMOTE_RUN} == ${False}   Check For ISS Crash   iface=${TCS_HAFNIUM_SSH_INTERFACE}


Check For Unlinked Port in Hafnium
    [Tags]   BASIC   HAFNIUM_LINKS
    Check Suite Requirements
    Exit Test When Flag File Exists
    Run Keyword If   ${REMOTE_RUN} == ${False}   All Etherchannel Summary Ports Should Be Linked   iface=${TCS_HAFNIUM_SSH_INTERFACE}

Check For Server Bonding Interfaces
    [Tags]   BONDING_INTERFACES
    Check Suite Requirements
    Exit Test When Flag File Exists
    Check Server Bonding Interfaces   ${SERVER_BONDING_CHECKS}   ${SERVER_HAFILE}

Run Remote Check Server Script for Multi-TCS
    [Tags]   MULTI_TCS
    Check Suite Requirements
    Exit Test When Flag File Exists
    ${REMOTE_RUN_CHECKS} =   Get Variable Value   ${REMOTE_RUN_CHECKS}   @{EMPTY}
    Run Keyword If   ${REMOTE_RUN_CHECKS} != @{EMPTY}   Run Remote Check Servers Script   ${REMOTE_RUN_CHECKS}   offline_interconnect=${POTASH_URI}   upd_lfccache=${UPDATE_LFCCACHE}   tags=${REMOTE_CHECKS_TAG}

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    Pass Execution If   ${CYCLES} == ${1}  Email will not be sent for CYCLES of 1, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.
