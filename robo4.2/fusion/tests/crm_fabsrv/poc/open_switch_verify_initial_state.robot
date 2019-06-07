*** Settings ***
Suite Setup    OpenSwitch Suite Setup
Suite Teardown    OpenSwitch Suite Teardown
Library    RequestsLibrary
Library    Collections
Variables    ../resource/open_switch_variables.py
Resource    ../resource/open_switch_keywords.robot

*** Test Cases ***
Management VLAN Only
    ${header}=    Format Header
    ${resp}=    Get Request    ${SESSION_ALIAS}   ${VLANS_URL}    headers=${header}
    HTTP Response Should Be 200    ${resp.status_code}
    ${configured_vlans}=    Parse Response For VLANs    ${resp}
    ${vlan_count}=    Get Length    ${configured_vlans}
    Should Be Equal As Integers     ${vlan_count}    ${EXP_INITIAL_VLAN_COUNT}    msg=Incorrect vlan count ${vlan_count} - expected ${EXP_INITIAL_VLAN_COUNT}    values=False
    Should Be Equal As Strings    @{configured_vlans}[0]    ${DEFAULT_VLAN_URL}    msg=Incorrect url for management vlan - @{configured_vlans}[0] - expected - ${DEFAULT_VLAN_URL}   values=False

No Active Ports
    ${header}=    Format Header
    ${params}=    Create Dictionary    depth=1    link_state=up
    ${resp}=    Get Request    ${SESSION_ALIAS}    ${INTERFACES_URL}    headers=${header}    params=${params}
    HTTP Response Should Be 200    ${resp.status_code}
    ${active_count}=    Get Count    ${resp.content}    link_state
    Should Be Equal As Integers    ${active_count}    ${EXP_INITIAL_PORT_COUNT}    msg=Incorrect active port count - ${active_count} - expected - ${EXP_INITIAL_PORT_COUNT}    values=False

*** Keywords ***
OpenSwitch Suite Setup
    # See if we can do a SSH and a reboot
    Reboot via SSH    ${TOR_SWITCH_IP}
    Create session    ${SESSION_ALIAS}    https://${TOR_SWITCH_IP}
    ${headers}    Create Dictionary    Content-Type=application/x-www-form-urlencoded
    ${params}=    Create Dictionary    username=${NETOP_USER}    password=${NETOP_USER}
    ${resp}=    Post Request    ${SESSION_ALIAS}    /login    headers=${headers}    params=${params}
    HTTP Response Should Be 200   ${resp.status_code}
    ${token}=    Parse Response For Login Token    ${resp}
    Set Suite Variable    ${LOGIN_TOKEN}    ${token}

OpenSwitch Suite Teardown
    Delete All Sessions

Format Header
    ${cookie_token}=    Catenate  SEPARATOR=    user=    ${LOGIN_TOKEN}
    ${headers}    Create Dictionary    Accept-Type=application/json    Cookie=${cookie_token}
    [Return]    ${headers}

HTTP Response Should Be 200
    [Arguments]    ${response_code}
    Should Be Equal As Strings    ${response_code}    200    msg=Incorrect HTTP response - received ${response_code} but expected 200    values=False

