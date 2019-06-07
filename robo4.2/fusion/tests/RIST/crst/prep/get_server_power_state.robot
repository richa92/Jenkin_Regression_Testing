*** Settings ***
Documentation        Log to console every server's power state
...                  Example:
...                          time pybot -d /tmp/logs/Display_Server_Power_Status/ -LTRACE -v APPLIANCE_IP:15.186.9.10 -v INVERT:True -v POWER:On get_server_power_state.robot
...                   OPTIONAL: POWER --> Will only display servers that are in the state mentioned.
...                                       ex: on, off, resetting, powering off, etc
...                   OPTIONAL: INVERT --> Will display the power states that are NOT in the POWER variable.
...                                        ex: INVERT:True POWER:on will display all servers that do NOT have the powerState of "on"

Resource        ../../../../Resources/api/fusion_api_resource.txt

Test Setup      Test Setup
Test Teardown   Test Teardown

*** Variables ***
${APPLIANCE_IP}                 None
${POWER}                        None
${INVERT}                       False
&{OV_CRED}                      userName=Administrator   password=hpvse123

*** Test Cases ***
Get Server Power State
    ${POWER} =   Convert To Uppercase   ${POWER}
    Log To Console   \n
    ${server} =   Fusion Api Get Server Hardware
    :FOR   ${device}   IN   @{server['members']}
    \   ${powerState} =   Get From Dictionary   ${device}   powerState
    \   ${powerState} =   Convert To Uppercase   ${powerState}
    \   Run Keyword If   '${POWER}' == 'NONE'   Log To Console   '${device['name']}','${powerState}'
    \   ...    ELSE IF   '${POWER}' == '${powerState}' and ${INVERT} == False   Log To Console   '${device['name']}','${powerState}'
    \   ...    ELSE IF   '${POWER}' != '${powerState}' and ${INVERT} == True   Log To Console   '${device['name']}','${powerState}'

*** Keywords ***
Test Setup
    [Documentation]   Pre-conditions for ALL test cases
    ${r}   ${s} =   Fusion Api Login Appliance  ${APPLIANCE_IP}  ${OV_CRED}
    Run Keyword If   ${r['status_code']} is not ${200}   Fail   Unable to login to OneView.

Test Teardown
    [Documentation]   Post-conditions for ALL test cases
    Fusion Api Logout Appliance
