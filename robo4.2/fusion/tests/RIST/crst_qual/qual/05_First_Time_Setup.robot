*** Settings ***
Library                OperatingSystem
Documentation          First Time Setup
Resource               ../resource.txt

Variables              ../Common.py
Variables              ../${DATA_FILE}

Suite Setup            Get Set Metadata

*** Test Cases ***
Confirm Feature Toggles then Set If Command Provided
    [Documentation]    Confirms the feature toggles are correctly set.
    ...    If FEATURE_TOGGLES_COMMAND is defined then will execute that command if the toggles defined in
    ...    FEATURE_TOGGLES are not correct, otherwise will terminate with Fatal Error
    ...    If a toggle is incorrect through the loop, the loop will exit.  Not all toggles checked in that case.
    [Tags]    05    CONFIRM_FT

    ${feature_toggles} =    Get Variable Value    ${FEATURE_TOGGLES}
    Pass Execution If    ${feature_toggles}==${None}    No Feature toggles defined to verify.

    :FOR   ${ft}    IN    @{feature_toggles}
    \    ${toggles_correct} =    Set Variable    ${False}     # unless proven otherwise below
    \    ${state}    ${toggle} =    Split String    ${ft}    :
    \    ${actual_state} =    Execute SSH Command    grep ${toggle} /ci/etc/feature-toggles.xml | sed s/^.*enabled=\\"// | sed s/\\".*$//
    \    # get rid of prompt which was also returned
    \    ${actual_state}    @{x} =    Split String    ${actual_state}
    \    Log    s: ${state}-    console=${CONSOLE}
    \    Log    as: ${actual_state}-    console=${CONSOLE}
    \    Run Keyword If    '${state}'=='${actual_state}'    Log    ${toggle} is as expected: ${actual_state}    console=${CONSOLE}
    \    Run Keyword If    '${state}'!='${actual_state}'    Log    ${toggle} is NOT as expected (${state}): actual (${actual_state})    console=${CONSOLE}
    \    Exit For Loop If   '${state}'!='${actual_state}'
    \    ${toggles_correct} =    Set Variable    ${True}

    Log    Toggles Correct: ${toggles_correct}    console=${CONSOLE}
    Run Keyword If    '${toggles_correct}'=='${False}'    Toggle Feature Toggles

Confirm Appliance Ready
    [Documentation]    If we executed a feature toggle, must wait for appliance to be "OK"
    ...   If feature toggle not changed then appliance should already be "OK" so Wait won't be long
    [Tags]    05   APPLIANCE_OK
    Wait For Appliance To Be Ready			${APPLIANCE_IP}

First Time Setup
    [Documentation]    Configure First time setup for OneView Appliance
    [Tags]    05    FTS
    Set To Dictionary    ${APPLIANCE['applianceNetworks'][0]}    app1Ipv4Addr    ${APPLIANCE_IP}
    Set To Dictionary    ${APPLIANCE['applianceNetworks'][0]}    hostname    ${OV_HOSTNAME}
    Set To Dictionary    ${APPLIANCE['applianceNetworks'][0]}    domainName    ${DOMAIN}
    First Time Setup    ${DATA_FILE}    ${ADMIN_CREDENTIALS['password']}
    Wait For Appliance To Become Pingable    ${APPLIANCE_IP}

Confirm CFM Pingable
    [Documentation]    Confirms CFM can be Pinged.
    [Tags]    05    PING_CFM

    Confirm APPLIANCE_IP and build PLEXXI_CFM

    ${uname} =    Run    uname -a
    Log    uname: ${uname}    console=${CONSOLE}

    ${is_Linux} =    Get Count    ${uname}    Linux

    ${ping} =    Set Variable If    ${is_linux}>0    Unix ping    Windows ping
    Log    will use ${ping}    console=${CONSOLE}

    ${status}    ${output} =    Run Keyword and Ignore Error    ${ping}    ${PLEXXI_CFM}
    Run Keyword If    '${status}'=='FAIL'    Fatal Error    Unable to ping CFM. DNS correct? ${output}

Clear DL IML Logs
    [Documentation]    Clear the IML logs.  After test is done we will then know the new entries are due to the test run
    [Tags]    TEST    05    CLEAR_IML
    ${resp}=   Fusion Api Login Appliance  ${APPLIANCE_IP}     ${ADMIN_CREDENTIALS}

    :FOR    ${server}    IN    @{DL_SERVER_IPs}
    \    ${ribcl} =       OperatingSystem.Get file   ..\\..\\..\\Tools\\cpqlocfg\\actions\\Clear_IML.xml
    \    ${response} =      Execute RIBCL xml     ${ILO_CREDENTIALS['username']}    ${ILO_CREDENTIALS['password']}   ${server}   ${ribcl}

    Fusion Api Logout Appliance

*** Keywords ***
Get Set Metadata
    [Documentation]    Get Set Metadata which includes OV, CFM and NOS versions

    # CFM version
    plexxi api login    ${CFM}    &{CFM_CREDENTIAlS}
    Set Suite Metadata    CFM Host  ${cfm}    top=True
    ${cfm} =    plexxi api get versions
    Set Suite Metadata    CFM Version  ${cfm['result']['software']}    top=True

    # Ring, just extract from ${DATA_FILE}
    ${ring} =    Replace String    ${DATA_FILE}    -cfm.py    ${EMPTY}
    Set Suite Metadata    Ring    ${ring}    top=True

    # NOS
    ${swCred} =    Get From Dictionary    ${PLEXXI_SWITCHES_CREDENTIALS}    1
    Open Connection   ${swCred['hostname']}
    ${login} =    Login   ${swCred['username']}   ${swCred['password']}   delay=1.5s
    ${nos} =    Get Lines Matching Regexp    ${login}    HPE Composable Fabric Switch    partial_match=true
    Set Suite Metadata    NOS   ${nos}    top=True

    Set Suite Metadata    OneView IP    ${APPLIANCE_IP}    top=True
    Set Suite Metadata    Data File    ${DATA_FILE}    top=True

    Close All Connections

Toggle Feature Toggles
    [Documentation]     IF FEATURE_TOGGLES_COMMAND is defined, execut that command.  Otherwise Fatal Erro
    ${feature_toggles_command} =    Get Variable Value    ${FEATURE_TOGGLES_COMMAND}

    Run Keyword If    '${feature_toggles_command}' is '${null}'    Fatal Error    Feature Toggles not correct and no feature toggle command specified.

    Log    Will execute ${feature_toggles_command} on ${APPLIANCE_IP}

#    Since we are rebooting, the prompt "#" will not be returned.  Use the message last word as the prmompt
#    Output:
#    Enabled: OVF6484_Composable_Rack_Plexxi_Switch_3eq
#    Disabled: OVF6385_Composable_Rack_Plexxi_Switch_3ex
#    Feature toggles have changed since last reboot. A reboot is required to apply these feature toggles.
#    A factory reset will be performed on reboot due to changes made to one or more feature toggles that specify apply-with="FACTORY_RESET".
#    The system will reboot in 15 seconds... Press Ctrl-C to abort.

    # couldn't use Execute SSH Command as that keyword executes a Logout which aports the reboot.
    Login to Fusion via SSH
    SSHLibrary.Write    ${feature_toggles_command}
    ${Output}=          Read until      abort.
    Log    SSH output: ${output}    console=${CONSOLE}

    Wait Until Keyword Succeeds    40 min    30 sec    Appliance Is Performing Factory Reset

Appliance Is Performing Factory Reset
    [Documentation]    Confirms Appliance is in "FACTORY_RESET" state
    ${state} = 	Fusion Api Get Resource		${APPLIANCE_IP}/controller-state.json
	Log 	-Appliance state: ${state['state']}    console=${CONSOLE}
	Should Match Regexp	   ${state['state']}    FACTORY_RESET
