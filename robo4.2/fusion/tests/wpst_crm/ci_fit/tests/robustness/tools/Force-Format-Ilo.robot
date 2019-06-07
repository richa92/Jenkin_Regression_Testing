*** Settings ***
Documentation        Force format iLO NAND.
...                  The script will prompt you to accept the operation by entering 'yes' (excluding quote) to avoid accidental reset.
...                  Example:
...                          time pybot -d /tmp/logs/Force-Format-Ilo/ -LTRACE -V/root/ci-fit/config_files/tools/force-format-ilo.py Force-Format-Ilo.robot

Resource            ../../../../../wpst_crm/crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../../resource/fusion_api_all_resource_files.txt
Resource            ../resources/common.robot
Library             Collections
Library             ../resources/robustness-helper.py


*** Variables ***
${FUSION_IP}                    ${APPLIANCE_IP}
${EMAIL_FROM}                   ${EMAIL_TO}
${tbirdEnv}                     None

*** Test Cases ***
Prompt User To Continue
    Variable File Should Be Passed
    ${continue} =   Get Value From User On Console   This will force format iLO NAND of the following servers: \n${FORMAT_SERVER_NAMES}. \nContinue[yes|no] (Enter defaults to no)?${SPACE}
    Run Keyword If   '${continue}' != 'yes'   Fatal Error   msg=User chose not to continue. Script terminated...

Login Appliance And Set Test
    Authenticate And Set Login

Force Format iLO NAND
    # Build our own iLO host info dictionary
    ${iLOHostInfo} =   Get iLO IP Addresses
    Log To Console   Force formatting iLO NAND...
    :FOR   ${k}   IN   @{FORMAT_SERVER_NAMES}
    \   Log To Console   DEBUG: Force formatting ${k}...   no_newline=${True}
    \   ${output} =   Run   perl ../../../tools/tcs/locfg.pl -s ${iLOHostInfo['${k}']['mpIpAddresses'][0]} -f ../../../tools/tcs/Force_Format.xml -u Administrator -p hpvse123 -${iLOHostInfo['${k}']['mpModel']}
    \   Log To Console   [Done]
    \   Log To Console   DEBUG: format output ${output}

Send Email Notification
    ${EMAIL_TO} =   Get Variable Value   ${EMAIL_TO}
    Pass Execution If   '${EMAIL_TO}' == '${null}'  EMAIL_TO was set to None, no email notification will be sent.
    ${suitename} =   Fetch From Left   ${SUITE NAME}  --
    Send Email    ${EMAIL_FROM}   ${EMAIL_TO}   [Tools] ${suitename} complete   [Tools] ${suitename} on ${APPLIANCE_IP} complete, check your system and or RoboGalaxy log for the result.

