*** Settings ***
Suite Setup    Auto Server Suite Setup
Suite Teardown    Auto Server Suite Teardown
Library    RequestsLibrary
Library    robot.libraries.String
Library    Collections
Library    FusionLibrary
Library    SSHLibrary
Library    HttpLibrary.HTTP
Variables    ../resource/one_view_variables.py
Variables    ../resource/open_switch_variables.py
Variables    poc_variables.py
Resource    ../resource/open_switch_keywords.robot

*** Variables ***
${rest_token}=    unset

*** Test Cases ***
Automated POC
    [Documentation]    Long single test case to see if all operations for POC can be automated
    #  1.  Start the ILo discovery daemon
    Start Ilo Discovery If Not Running

    #  2.  reboot the switch
    Reboot Via SSH    ${TOR_SWITCH_IP}

    #  3.  Set up the networks
    Create Network If Not Exist    ${BLUE_VLAN_NAME}
    Create Network If Not Exist    ${PURPLE_VLAN_NAME}

    #  4.  Ensure we have 4 ILo servers discovered
    Wait Until Keyword Succeeds    2 min    5 sec    Verify Server Hardware Count In OneView    4

    #  5.  Add in the Tor template
    Create Tor Template

    #  6.  Assign the Tor template to the switch
    Assign Tor Template

    #  7.  Verify ping connectivity
    Wait Until Keyword Succeeds    3 min    5 sec    Should Have VLANS
    Wait Until Keyword Succeeds    2 min    5 sec    Should Ping Video Servers

*** Keywords ***
Auto Server Suite Setup
    ${Response}    ${SessionId}    Fusion API Login Appliance     ${ONE_VIEW_IP}    ${ADMIN_CREDENTIALS}
    Set Suite Variable    ${rest_token}    ${SessionId}

Auto Server Suite Teardown
    Fusion Api Logout Appliance

Start Ilo Discovery If Not Running
    Set Default Configuration   prompt=${FUSION_PROMPT}    timeout=${FUSION_TIMEOUT}
    Open Connection    ${ONE_VIEW_IP}    alias=vctor_ssh
    Login    ${SSH_USER}    ${SSH_PASSWORD}
    SSHLibrary.Write    service ilo-discovery status
    ${result}=    Read until    ${FUSION_PROMPT}
    Close Connection
    ${status_line}=    robot.libraries.String.Get Line    ${result}    0
    ${status}=    robot.libraries.String.Fetch From Right    ${status_line}    :
    Run Keyword If    '${status}' != 'running'    Start Ilo Daemon

Start Ilo Daemon
    Set Default Configuration   prompt=${FUSION_PROMPT}    timeout=${FUSION_TIMEOUT}
    Open Connection    ${ONE_VIEW_IP}    alias=vctor_ssh
    Login    ${SSH_USER}    ${SSH_PASSWORD}
    SSHLibrary.Write    service ilo-discovery start
    Read until    ${FUSION_PROMPT}
    SSHLibrary.Write    service ilo-discovery status
    ${Output}=    Read until    ${FUSION_PROMPT}
    Close Connection
    ${status_line}=    robot.libraries.String.Get Line    ${Output}    0
    ${status}=    robot.libraries.String.Fetch From Right    ${status_line}    :
    Should Be Equal As Strings    running    ${status}    msg=Unable to start ilo-discovery daemon - found to be ${status}    values=False

Create Network If Not Exist
    [Arguments]    ${vlan_name}
    ${response}=    Fusion Api Get Ethernet Networks    param=?filter="'name'=='${vlan_name}'"
    Return From Keyword If    ${response['count']}==1
    ${network}=    Set Variable If    '${vlan_name}' == '${BLUE_VLAN_NAME}'    ${BLUE_NETWORK_DETAILS}    ${PURPLE_NETWORK_DETAILS}
    ${response}=    Fusion Api Create Ethernet Network  ${network}
    Should Be Equal as Strings    ${response['status_code']}    202    msg=Failed to Create Network ${vlan_name}.

Get Network Id
    [Arguments]    ${network_name}
    ${response}=    Fusion Api Get Ethernet Networks    param=?filter="'name'=='${network_name}'"
    Should Be Equal As Integers    ${response['count']}    1    msg=Incorrect number ${response['count']} networks with name ${network_name}    values=False
    ${network_identification}=    robot.libraries.String.Fetch From Right    ${response['members'][0]['uri']}    /
    [Return]    ${network_identification}

Verify Server Hardware Count In OneView
    [Arguments]    ${expected_server_count}
    ${resp}=    Fusion Api Get Server Hardware
    Should Be Equal As Integers   ${resp['count']}    ${expected_server_count}    msg=Incorrect server count, expected 4 but found ${resp['count']}    values=False

Create Tor Template
    ${header_stuff}=    Create Dictionary    auth=${rest_token}    content-type=application/json
    Create session    vctor    ${REST_BASE_URL}
    ${resp}=    Get Request    vctor    ${TOR_TEMPLATE_NAME}   headers=${header_stuff}
    Delete All Sessions
    Should Not Contain    '${resp.content}'    '${TOR_TEMPLATE_NAME}'    msg=Template with name ${TOR_TEMPLATE_NAME} already exists    values=False

    ${blue_network_id}=    Get Network Id    ${BLUE_VLAN_NAME}
    ${purple_network_id}=    Get Network Id    ${PURPLE_VLAN_NAME}

    Set To Dictionary    ${BLUE_NETWORK_IDENTIFIER}    network_id=${blue_network_id}
    Set To Dictionary    ${PURPLE_NETWORK_IDENTIFIER}    network_id=${purple_network_id}

    ${purple_network_list}=    Create List    ${PURPLE_NETWORK_IDENTIFIER}
    ${blue_network_list}=    Create List    ${BLUE_NETWORK_IDENTIFIER}
    ${both_network_list}=    Create List    ${BLUE_NETWORK_IDENTIFIER}    ${PURPLE_NETWORK_IDENTIFIER}

    # create the uplinks
    Set To Dictionary    ${UP_LINK}    networks=${both_network_list}
    ${up_list}=    Create List    ${UP_LINK}

    # create the downlinks
    Set To Dictionary    ${OLDIES}    networks=${purple_network_list}
    Set To Dictionary    ${COMEDY}    networks=${blue_network_list}
    Set To Dictionary    ${VIDEO_CLIENT}    networks=${both_network_list}
    ${downlink_list}=    Create List    ${OLDIES}    ${COMEDY}    ${VIDEO_CLIENT}

    Set To Dictionary    ${TOR_TEMPLATE}    uplinkSets=${up_list}    downlinkSets=${downlink_list}
    Log    ${TOR_TEMPLATE}
    ${json_data}=    Stringify Json    ${TOR_TEMPLATE}

    ${header_stuff}=    Create Dictionary    auth=${rest_token}    content-type=application/json
    Create session    vctor    ${REST_BASE_URL}
    ${resp}=    Post Request    vctor    ${TOR_TEMPLATE_URL}   headers=${header_stuff}    data=${json_data}
    Delete All Sessions

Assign Tor Template
    ${header_stuff}=    Create Dictionary    auth=${rest_token}    content-type=application/json
    Create session    vctor    ${REST_BASE_URL}

    Set To Dictionary    ${TOR_DETAILS}    torip=${TOR_SWITCH_IP}    servers=${EMPTY}
    Log    ${TOR_DETAILS}
    ${json_data}=    Stringify Json    ${TOR_DETAILS}
    Log    ${json_data}
    ${resp}=    Post Request    vctor    ${TOR_URL}    headers=${header_stuff}    data=${json_data}
    Log    ${resp}
    Delete All Sessions

Should Have VLANS
    Create session    vlanCheck    https://${TOR_SWITCH_IP}
    ${headers}    Create Dictionary    Content-Type=application/x-www-form-urlencoded
    ${params}=    Create Dictionary    username=${NETOP_USER}    password=${NETOP_USER}
    ${resp}=    Post Request    vlanCheck    /login    headers=${headers}    params=${params}

    Should Be Equal As Strings   ${resp.status_code}    200    msg=Failed Switch RESTful login
    ${token}=    Parse Response For Login Token    ${resp}

    ${cookie_token}=    Catenate  SEPARATOR=    user=    ${token}
    ${headers}    Create Dictionary    Accept-Type=application/json    Cookie=${cookie_token}
    ${resp}=    Get Request    vlanCheck   ${VLANS_URL}    headers=${headers}
    Should Be Equal As Strings   ${resp.status_code}    200    msg=Faied to read configured vlan data
    ${configured_vlans}=    Parse Response For VLANs    ${resp}
    ${vlan_count}=    Get Length    ${configured_vlans}
    Should Be Equal As Integers     ${vlan_count}    3    msg=Incorrect vlan count ${vlan_count} - expected 3    values=False
    Delete All Sessions

Should Ping Video Servers
    Set Default Configuration   prompt=${PING_VERIFY_PROMPT}    timeout=${SSH_TIMEOUT}
    Open Connection    ${VIDEO_CLIENT_ADDRESS}   alias=videoClient
    Login    ${PING_VERIFY_USER}    ${PING_VERIFY_PASSWORD}
    SSHLibrary.Write    ping -c 2 ${OLDIE_PING_ADDRESS}
    ${result_oldie}=    Read until    ${PING_VERIFY_PROMPT}
    SSHLibrary.Write    ping -c 2 ${COMEDY_PING_ADDRESS}
    ${result_comedy}=    Read until    ${PING_VERIFY_PROMPT}
    Close Connection

    ${count}=    robot.libraries.String.Get Line Count    ${result_oldie}
    Should Be Equal As Integers    ${count}    8    msg=Incorrect results from ping ${result_oldie}    values=False
    ${ping_line}=    robot.libraries.String.Get Line    ${result_oldie}    5
    Should Contain    ${ping_line}    2 packets transmitted, 2 received    msg=Ping Was Not Successful from video client to ${OLDIE_PING_ADDRESS}

    ${count}=    robot.libraries.String.Get Line Count    ${result_comedy}
    Should Be Equal As Integers    ${count}    8    msg=Incorrect results from ping ${result_comedy}    values=False
    ${ping_line}=    robot.libraries.String.Get Line    ${result_comedy}    5
    Should Contain    ${ping_line}    2 packets transmitted, 2 received    msg=Ping Was Not Successful from video client to ${COMEDY_PING_ADDRESS}
