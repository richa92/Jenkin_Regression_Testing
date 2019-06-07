*** Settings ***
Documentation    Initialize OneView with Plexxi
Library          FusionLibrary

Resource         ../resource.txt

Variables        ../Common.py
Variables        ../${DATA_FILE}

Suite Setup             QUAL Suite Setup    ${ADMIN_CREDENTIALS}
Suite Teardown          QUAL Suite Teardown

*** Test Cases ***
Plexxi Login
    [Documentation]    Ensure Logged Into Plexxi Test Cases in this Suite.  Needed for -i TAG support.
    [Tags]    25     PLEXXI_LOGIN    DISCOVER_FABRICS    SYNCED_HEALTHY    PLEXXI_INTEGRATION_SET
    ...    PLEXXI_ONEVIEW_CONFIG    CONFIRM_OV_INTEGRATION    ONEVIEW_CLAIM_FABRICS    CONFIRM_SWITCH_STATE
    ...    CONFIRM_SWITCH_CONFIG

    Plexxi Login

Discover Plexxi Fabrics
    [Documentation]    Discover Plexxi fabrics in Composable Fabric Manager
    [Tags]    25     DISCOVER_FABRICS
    ${plexxi_fabrics} =    Get Variable Value   ${PLEXXI_FABRICS}
    ${added_plexxi_fabrics} =     Plexxi Api Get Fabrics
    ${fabric_added} =    Set Variable    ${False}
    Log   See if ${FABRIC_NAME} is already added    console=${CONSOLE}
    :FOR    ${apf}    in    @{added_plexxi_fabrics['result']}
    \    Run Keyword If    '${apf["name"]}'=='${FABRIC_NAME}'    Log    Fabric "${FABRIC_NAME}" is already configured on ${PLEXXI_CFM}    level=WARN   console=${CONSOLE}
    \    ${fabric_added} =    Set Variable If    '${apf["name"]}'=='${FABRIC_NAME}'    ${True}    ${False}
    \    Exit For Loop If    '${apf["name"]}'=='${FABRIC_NAME}'

    Log   is_added: ${fabric_added}
    Run Keyword If   ${fabric_added}==${False}    Discover Plexxi Fabrics From Variable   ${plexxi_fabrics}

Perform Fit
    [Documentation]    Perform Fit on discovered fabric
    [Tags]    25    PERFORM_FIT
    ${resp} =    plexxi api get fabrics
    # In Qual, assuming only one fabric.
    Run Keyword If    ${resp['count']}!=1    For Qual expected one Fabric. Got ${resp['count']}
    ${fuuid} =   get from dictionary   ${resp['result'][0]}   uuid
    &{body} =    create dictionary    fabric_uuid=${fuuid}   description=Qual Perform Fit   name=Qual Fit

    Wait Until Keyword Succeeds    2 min    20 sec    CFM Perform Fit to COMPLETED    ${body}

Swiches Synced and Healthy
    [Documentation]    Confirms switches are Synced and Healthy else Fatal error
    [Tags]    25   SYNCED_HEALTHY
    ${status}    ${output} =    Run Keyword and Ignore Error
    ...    Wait Until Keyword Succeeds    5 min    10 sec    Switches Are Synced And Healthy

    Run Keyword If    '${status}'=='FAIL'    Fatal Error    Switches Not Synced and Healthy, abort test.

Enable Composable Cloud Integration Set
    [Documentation]    Enable composable cloud integration set in Composable Fabric Manager
    [Tags]    25     PLEXXI_INTEGRATION_SET
    ${integration_sets} =     Plexxi Api Get Integration Sets

    ${IS_configured} =    Set Variable    ${False}
    :FOR    ${is}    in    @{integration_sets['result']}
    \   ${IS_configured} =    Is Integration Set Selected    ${FABRIC_NAME}    ${is}
    \    Exit For Loop If    '${IS_configured}'=='${True}'

    Log   ${FABRIC_NAME} is_configured: ${IS_configured}
    ${resp} =    Run Keyword If    ${IS_configured}==${False}    Plexxi Api Enable Composable Cloud Integration Set
    Run Keyword If    ${resp['status_code']}==${BADREQUEST}    Fatal Error     Failed to add integration set ${resp["result"]}
    Run Keyword If    ${resp['status_code']}==${FORBIDDEN}    Log    ${FABRIC_NAME} is already added.    level=WARN    console=${CONSOLE}

Add OneView Configuration To Plexxi CFM
    [Documentation]    Add OneView configuration to Plexxi CFM
    [Tags]    25     PLEXXI_ONEVIEW_CONFIG
    ${plexxi_OV_configuration} =    Plexxi Api Get Oneview Configuration

    ${OV_pack_added} =    Set Variable    ${False}
    :For    ${pOVc}    in    @{plexxi_OV_configuration['result']}
    \    Run Keyword If    '${pOVc["host"]}'=='${APPLIANCE_IP}'    Log    Fabric "${APPLIANCE_IP}" is already configured on Plexxi    level=WARN
    \    ${OV_pack_added} =    Set Variable If    '${pOVc["host"]}'=='${APPLIANCE_IP}'    ${True}    ${False}
    \    Exit For Loop If    '${pOVc["host"]}'=='${APPLIANCE_IP}'

    Pass Execution If    ${OV_pack_added}    Log   OV_added: ${OV_pack_added}

    Set To Dictionary     ${ONEVIEW_CONFIG}    host    $APPLIANCE_IP
    ${resp} =    Run Keyword If    ${OV_pack_added}==${False}    Add OneView Configuration To Plexxi Connect From Variable   ${ONEVIEW_CONFIG}
    Should Be Equal As Integers    ${resp['status_code']}    ${OK}
    Should Be Equal As Integers    ${resp['count']}    1

Confirm HPEOneView Integration
    [Documentation]    OneView added, now confirm via Plexxi CFM API
    [Tags]    25   CONFIRM_OV_INTEGRATION
    ${integrations} =    Plexxi Api Get OneView Configuration

    Should Be Equal As Integers    ${integrations['count']}    1
    Should Be Equal    ${integrations['result'][0]['name']}    ${ONEVIEW_CONFIG['name']}
    Should Be Equal    ${integrations['result'][0]['host']}    ${APPLIANCE_IP}
    Should Be Equal    ${integrations['result'][0]['connection_state']}    connected

Initiate Fabric Claim Process
    [Documentation]    Initiate the claim process in fabrics which will transition to fabrics from Adding to Configured
    [Tags]    25     ONEVIEW_CLAIM_FABRICS

    ${fabric_uri} =    Wait Until Keyword Succeeds    5 min    20 sec    Get Fabric Uri By Name    ${FABRIC_NAME}

    ${fabric} =     Get Resource by URI    ${fabric_uri}
    Log    ${FABRIC_NAME} is currently ${fabric['state']} and is ${fabric['status']}    console=${CONSOLE}

    Run Keyword If    '${fabric["state"]}'=='Configured'    Log    ${fabric['name']} is already configured in OneView    level=WARN
    Run Keyword If    '${fabric["state"]}'!='Configured'    Claim The Fabric    ${FABRIC_NAME}    ${FABRIC_ADD_BODY}    ${fabric_uri}

Confirm Switch Name ChassisID and Ports
    [Documentation]    Confirm the Switch Ports are Linked/Enabled, etc as expected
    [Tags]    25    CONFIRM_OV_SWITCH_Ports

    Run Keyword If    ${PAUSE_TO_REVIEW_OV_SWITCHES}==${True}    Pause Execution    Switches Look Ok on ${CFM}

    Wait Until Switches Reached State    ${PLEXXI_SWITCH_CHASSISIDS}    ${PLEXXI_SWITCH_NAMES}
    ${switches} =   Fusion Api Get Switch

    Run Keyword If    ${PAUSE_TO_REVIEW_OV_SWITCHES}==${True}    Pause Execution    Switches Look Ok on ${APPLIANCE_IP}

    ${confirm_switches} =    Get Variable Value   ${CONFIRM_SWITCHES}
    Run Keyword If  ${confirm_switches} is ${null}    Run Keywords
    ...    Log    CONFIRM_SWITCHES is not defined, unable to confirm switch values in ${TEST NAME}.    level=WARN    console=${CONSOLE}
    ...    AND    Pass Execution    Passing though not executed due to missing CONFIRM_SWITCHES

    Wait Until Keyword Succeeds    3 min    30 sec    Ports Are As Expected    ${CONFIRM_SWITCHES}

*** Keywords ***
Ports Are As Expected
    [Documentation]    Validates all of the switch ports are as expected.
    [Arguments]    ${switches}

    # Refresh the fabric as the ports take time to stabilize
    Refresh Fabric    ${FABRIC_NAME}

    :FOR    ${switch}    IN    @{switches}
    \    ${this_switch} =    Get Resource    SW:${switch["name"]}
    \    ${status} =    Fusion Api Validate Response Follow    ${switch}    ${this_switch}    wordy=True
    \    Should Be True    ${status}

Claim The Fabric
    [Documentation]    Claims Fabric in OneView.  Assumes fabric is not already configured else keyword will fail
    [Arguments]    ${fabric_name}    ${fabric_adding}    ${uri}

    ${resp} =    Fusion Api Generic Patch    body=${fabric_adding}    uri=${uri}
    Wait For Task2    ${resp}    timeout=200    interval=10
    # Check that fabric and switches are in configured state
    Wait Until Fabric Reached State    ${fabric_name}    Configured


Is Integration Set Selected
   [Documentation]    Checks to see if the OneView (Composable Rack) Integraion Set is selected
   [Arguments]     ${fabric_name}    ${is}
    Run Keyword If    '${is["name"]}'=='${fabric_name}' and '${is["is_selected"]}'=='${True}'    Run Keywords
    ...    Log    Integration Set "${fabric_name}" is already selected on Plexxi    level=WARN
    ...    AND    Return From Keyword    ${True}

    [Return]    ${False}
