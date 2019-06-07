*** Settings ***
Documentation		Monitor-Fping-Log  -  Regular check on fping log(s) for loss. Create /root/.stop_script if fping loss is found to stop robustness scripts from running.
...                     Example: pybot -T -d /tmp/logs/Monitor-Fping-Log -LTRACE -V /root/ci-fit/config_files/eaglexx_robustness_data_variables.py -vCYCLES:1 Monitor-Fping-Log.robot

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
${CYCLES}                       540000
${END_OF_CYLE_WAIT}             10s
${STOP_SCRIPT}                  /root/.stop_script
${tbirdEnv}                     None

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Check Fping Log
    Variable File Should Be Passed
    :FOR   ${x}  IN RANGE   1   ${CYCLES}+1
    \   Log   \n Cycle: ${x} of ${CYCLES}   console=${True}
    \   ${returnStatus}  ${returnMsg} =   Run Keyword And Ignore Error   OperatingSystem.File Should Exist   ${STOP_SCRIPT}
    \   Run Keyword If   "${returnStatus}" == "PASS"   Log   \n ${STOP_SCRIPT} found, exiting...   console=${True}
    \   Exit For Loop If   "${returnStatus}" == "PASS"
    \   Fping Should Have No Loss
#    \   Check For ISS Crash   iface=eth4
    \   Sleep And Log Reason To Console   ${END_OF_CYLE_WAIT}   reason=Sleeping ${END_OF_CYLE_WAIT} before re-checking fping logs.