*** Settings ***
Documentation        Use existing SPPs and rpms to create Custom Firmware Bundles, then remove them.
...
...                  All non-iso files will be treated as a hotfix and will be added to the custom SPP
...                  This script shares the same data variable file with the issu robustness test
...                  Example workflow:
...                      time pybot -T -d /tmp/logs/Custom-SPP-Create-Remove/ -LTRACE -vSPP_BUNDLE_NAME:SPPGen10Snap3_2018_0327_32 -V /root/ci-fit/config_files/robustness/eagle63-issu.py Custom-SPP-Create-Remove.robot
...                  The SPP_BUNDLE_NAME is the name of the SPP iso that has been uploaded to OV and is being used as the baseline to create the custom bundle.

Variables           ../../resources/data_variables.py
Resource            ../../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../resources/common.robot
Library		    Collections
Library             ../../resources/robustness-helper.py

*** Variables ***
${CYCLES}                       10
${FUSION_IP}                    ${APPLIANCE_IP}
${EMAIL_FROM}                   ${EMAIL_TO}
${SPP_BUNDLE_NAME}              None
${CUSTOM_SPP_BUNDLE_NAME}       RGCUSTOMBUNDLE
${STOP_SCRIPT}                  /root/.stop_script
${baselineUri}                  None

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Check For SPP Bundle Argument
    Run Keyword If   "${SPP_BUNDLE_NAME}" == "${null}"   Fail   msg=SPP_BUNDLE_NAME is a required arguments. Please provide it using -vSPP_BUNDLE_NAME:<SPP Name>.

Assign Variables
    ${customUri} =   Catenate   SEPARATOR=   /rest/firmware-drivers/   ${CUSTOM_SPP_BUNDLE_NAME}
    Cycle   ${customUri}

Send Email Notification
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Robustness] ${suitename} complete   [Robustness] ${suitename} complete, check your RoboGalaxy log for the result.


*** Keywords ***
Cycle
    [Documentation]   Starts cycling tests.
    [Arguments]    ${customUri}
    :FOR   ${x}   IN RANGE   1   ${CYCLES}+1
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Return From Keyword If   "${returnStatus}" == "PASS"
    \   Log   \n Cycle: ${x} of ${CYCLES}   console=${True}
    \   Run Keyword and Ignore Error    fusion_api_appliance_logging.Write To ciDebug Log    ${SUITE_NAME}: Cycle: ${x} of ${cycles}
    \   Create Custom Firmware Bundle   ${SPP_BUNDLE_NAME}   ${SPP_UPLOAD_WAIT_TIMEOUT}   ${SPP_UPLOAD_WAIT_INTERVAL}
    \   Remove Custom Firmware Bundle   ${customUri}
    \   Sleep And Log Reason To Console   ${END_OF_CYCLE_WAIT}   reason=Sleeping ${END_OF_CYCLE_WAIT} at the end of the cycle.
