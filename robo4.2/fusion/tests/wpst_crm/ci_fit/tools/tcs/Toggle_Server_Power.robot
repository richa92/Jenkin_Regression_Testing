*** Settings ***
Documentation        Power off/on every server in the configuration
...                  This script will use the HA file to attempt a power off using ssh.  Then a momentary press.  Then it will use press and hold.
...                  Example:
...                          time pybot -d /tmp/logs/Toggle_Server_Power/ -LTRACE -v APPLIANCE_IP:15.186.9.10 -v ENC_NAME:CN7544044K -v POWER:On -v FORCE:True HA_FILE:HA_ipaddr.conf Toggle_Server_Power.robot
...                   REQUIRED: POWER --> On or Off
...                             HA_FILE:/path/to/your/ha_file.conf
...                   OPTIONAL: ENC_NAME --> Will toggle the power states on the given enclosure, instead of all servers in the ME.
...                             FORCE --> If FORCE:True, the script will do a hold and press on all servers
...                             POWER_CONTROL --> To override the default PressAndHold power control used for -vFORCE:True

Variables           ../../tests/robustness/resources/data_variables.py
Resource            ../../../crm_austin/resources/keywords_ovcli.txt
Resource            ../../../../resource/fusion_api_all_resource_files.txt
Resource            ../../tests/robustness/resources/common.robot
Library            ../../tests/robustness/resources/robustness-helper.py
Library             Collections

*** Variables ***
${FUSION_IP}                    ${APPLIANCE_IP}
${POWER}                        None
${ENC_NAME}                     None
${HA_FILE}                      None
${PROCEED_WITH_PRESS_AND_HOLD}  None
${FORCE}                        None
${POWER_CONTROL}                PressAndHold

*** Test Cases ***
Login Appliance And Set Test
    Authenticate And Set Login

Toggle Power State
    ${Enclosures} =   Run Keyword If   "${ENC_NAME}" != "${null}"   fusion api get enclosures   param=?filter="name=='${ENC_NAME}'"
        ...       ELSE   fusion api get enclosures   param=?sort=name:ascending
    :FOR   ${enc}   IN   @{Enclosures['members']}
    \   Traverse Device Bays    ${enc['deviceBays']}

*** Keywords ***
Traverse Device Bays
    [Documentation]   traverse device bays
    [Arguments]   ${devices}
    ${POWER} =   Convert To Uppercase   ${POWER}
    Log To Console   \n
    :FOR   ${device}   IN   @{devices}
    \   ${uri} =   Get From Dictionary   ${device}   deviceUri
    \   ${bay} =   Get From Dictionary   ${device}   bayNumber
    \   ${server} =   Fusion Api Get Server Hardware   uri=${uri}
    \   ${present} =   Get From Dictionary   ${device}   devicePresence
    \   Run Keyword If   '${present}' == 'Absent' or '${present}' == 'Subsumed'   Log To Console   Device in bay number ${bay} is Absent or Subsumed (Full Height).
    \   Continue For Loop If   '${present}' == 'Absent' or '${present}' == 'Subsumed'
    \   ${powerState} =   Get From Dictionary   ${server}   powerState
    \   ${powerState} =   Convert To Uppercase   ${powerState}
    \   ${FORCE} =   Convert To Uppercase   ${FORCE}
    \   Continue For Loop If   '${POWER}' == '${powerState}'
    \   Run Keyword If   '${POWER}' != '${powerState}' and '${POWER}' == 'OFF' and '${FORCE}' == 'TRUE'   common.Power Off All Servers In Parallel   powerControl=${POWER_CONTROL}
    \   ...    ELSE IF   '${POWER}' != '${powerState}' and '${POWER}' == 'OFF' and '${FORCE}' != 'TRUE'   common.Get IP And Power Off Server Via Ssh As Possible   ${server}
    \   ...    ELSE IF   '${POWER}' != '${powerState}' and '${POWER}' == 'ON'    common.Power On Server Uri    ${uri}
