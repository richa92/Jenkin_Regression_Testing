*** Settings ***
Library            Collections
Library            json
Library            OperatingSystem
Library            FusionLibrary
Library            i3SLibrary

*** Keywords ***
I3S Suite Setup
    [Documentation]    Login to I3s Using Onview Authtoken
    [Arguments]        ${ip}=${fusion_ip}    ${credentials}=${admin_credentials}
    Set Log Level    TRACE
    ${authtoken} =     Login to Fusion Via REST    ${ip}    ${credentials}
    ${i3s_details} =     Fusion Api Get i3sCluster IP
    ${i3s_ip} =    Get From Dictionary    ${i3s_details['members'][0]}    primaryIPV4
    Log    \nI3s IP: ${i3s_ip}    console=True
    I3S API LOGIN APPLIANCE    ${i3s_ip}    ${authtoken}

Login to Fusion Via REST
    [Documentation]    Connects to the Appliance and creates a session using the Username and Password.
    ...                Example:\n| Login to Fusion Via REST | 15.212.171.212 | Administrator | admin123 |
    [Arguments]        ${fusion_ip}    ${credentials}
    ${resp}    ${sessionId} =    Fusion Api Login Appliance    ${fusion_ip}    ${credentials}
    Run Keyword If   ${resp['status_code']} is not 400    Log    \nSuccessfully logged into Appliance
    Run Keyword If   ${resp['status_code']} is 400    Fatal Error    Failed to Login to Appliance
    ${Response}=    Fusion Api Get Appliance Version
    Set Suite Metadata     OneView Version    ${Response['softwareVersion']} : ${Response['date']}    top=True
    [Return]    ${sessionId}

I3S Suite Teardown
    [Documentation]    Logout from Oneview
    Fusion Api Logout Appliance

I3S Test Setup
    [Documentation]    Power off server hardware and delete server profile
    [Tags]    Test-Setup
    ${server_prof} =    Get Server Hardware Profile    ${servers [0]['serverHardwareUri']}
    Run Keyword If    '${server_prof}'!='${null}'    Log    \nServer profile '${server_prof}' is assigned to server '${servers [0]['serverHardwareUri']}'
    Return From Keyword If    '${server_prof}'=='${null}'
    Power Off Profile Server    ${servers [0]['serverHardwareUri']}
    Delete Server Profile    ${server_prof}

Get Server Hardware Profile
    [Documentation]    Querys the appliance for server hardware and returns the server profile for particular server bay
    [Arguments]    ${server}
    ${server} =    replace string using regexp    ${server}    SH:    ${EMPTY}
    ${resp} =     Fusion Api Get Server Hardware    param=?filter="'name'=='${server}'"
    Return From Keyword If  ${resp['count']}==0  /rest/server_hardware_uri_${server}_not_found
    ${sp_uri} =    Get From Dictionary    ${resp['members'][0]}    serverProfileUri
    ${sp_resp} =    Run Keyword If    '${sp_uri}' != 'None'    Get Resource by URI    ${sp_uri}
    ...    ELSE    Return From Keyword    ${None}
    ${sp} =    Get From Dictionary    ${sp_resp}    name
    Log    Server profile '${sp}' is assigned to server '${server}'    console=True
    [Return]    ${sp}

Windows ping unreachable check
    [Documentation]    Windows ping unreachable check
    [Arguments]    ${host}
    ${Output}=    Run    ping -n 4 ${host}
    Should Contain    ${Output}    unreachable

Capture Task Status
    [Documentation]    Returns task Status
    [Arguments]      ${resp}    ${timeout}=1200    ${interval}=5    ${status_code}=202
    ${status}=    Run Keyword And Return Status    should be equal as integers    ${resp['status_code']}    ${status_code}
    ${task_resp}=    Run Keyword If    '${status}'=='True'    Wait For Task    ${resp}    timeout=${timeout}    interval=${interval}
    ${task_status}=  Run Keyword If    '${status}'=='True'    Run Keyword And Return Status    should be equal    ${task_resp['taskState']}    Completed
    Run Keyword If    '${task_status}'=='False'    Log    \n${task_resp['taskErrors'][0]['message']}    level=WARN
    [Return]    ${task_status}

Login To Appliance And Verify Oneview Prerequisites
    [Documentation]    Login to appliance and verify whether applaince meets Prerequisites
    [Arguments]     ${fusion_ip}    ${admin_credentials}

    I3S Suite Setup    ${fusion_ip}    ${admin_credentials}
    ${blnVerify} =    Verify Oneview Prerequisites
    Run Keyword If    ${blnVerify}!=True    Fail    One or more prerequisites not added to appliance
    I3S Test Setup

Verify Oneview Prerequisites
    [Documentation]    Verifies the existence of prerequisites
    [Arguments]    ${resourcesList}=@{allResourcesCommonList}

    :FOR    ${resourceName}    IN    @{resourcesList}
    \    ${blnVerifyPreReqs} =    Run Keyword If    '${resourceName}' == 'ethernets'    Get Ethernet Networks Passed in Variable File
    \       ...                          ELSE IF    '${resourceName}' == 'egs'    Get Enclosure Groups Passed in Variable File
    \       ...                          ELSE IF    '${resourceName}' == 'servers'    Get Servers Passed in Variable File
    \       ...                          ELSE IF    '${resourceName}' == 'osdps'    Get OS deployment Plans Passed in Variable File
    \    Return From Keyword If    ${blnVerifyPreReqs}!=True    One or more '${resourceName}' are not exist in appliance
    [Return]    ${blnVerifyPreReqs}

Get Ethernet Networks Passed in Variable File
    [Documentation]    Returns false If any of ehternets passed in variable file
    ...    is not present in applaince

    :FOR    ${net}    IN    @{networks}
    \    ${resp} =   Get Resource    ETH:${networks['${net}']}
    \    Run Keyword If    ${resp['status_code']}==404     Log    ... Network ${networks['${net}']} doesn't exists\n    console=True
    \    Return From Keyword If    ${resp['status_code']}==404
    [Return]    True

Get Enclosure Groups Passed in Variable File
    [Documentation]    Returns false If any of Enclosure Groups passed in variable file
    ...    is not present in applaince

    :For    ${eg}    IN    @{egs}
    \    ${resp} =   Get Resource    EG:${eg['enclosureGroupUri']}
    \    Run Keyword If    ${resp['status_code']}==404     Log    ...Enclosure Group ${eg['enclosureGroupUri']} doesn't exists\n    console=True
    \    Return From Keyword If    ${resp['status_code']}==404
    [Return]    True

Get Servers Passed in Variable File
    [Documentation]    Returns false If any of Servers passed in variable file
    ...    is not present in applaince

        :For    ${server}    IN    @{servers}
    \    ${resp} =   Get Resource    SH:${server['serverHardwareUri']}
    \    Run Keyword If    ${resp['status_code']}==404     Log    ...Server ${server['serverHardwareUri']} doesn't exists\n    console=True
    \    Return From Keyword If    ${resp['status_code']}==404
    [Return]    True

Get OS deployment Plans Passed in Variable File
    [Documentation]    Returns false If any of OS DPs passed in variable file
    ...    is not present in applaince

    :For    ${dp}    IN    @{osdps}
    \    ${resp} =    i3s Api Get Deploymentplan    param=?filter="'name'=='${dp['name']}'"
    \    Run Keyword If    ${resp['count']} == 0     Log    ...OS Deployment Plan ${dp['name']} doesn't exists\n    console=True
    \    Return From Keyword If    ${resp['count']} == 0
    [Return]    True

Get Profile From OS Volume
    [Documentation]    Gets profile associated with Os volume
    [Arguments]    ${osVolume}

    ${resp} =    i3s Api Get OS Volume    param=?filter="'name'=='${osVolume}'"
    Return From Keyword if    ${resp['count']} == 0
    ${volResp} =    i3s Api Get OS Volume    uri=${resp['members'][0]['uri']}
    ${volProf} =    Get From Dictionary    ${volResp['dependentArtifacts'][0]}    name
    Log    \nVolume '${osVolume}' is used by profile '${volProf}'
    [return]    ${volProf}

Login to Appliance via SSH
    [Documentation]    Connect to Appliance CIM Bash via SSH
    ...    Example:\n| Login to Appliance Via SSH | 10.0.12.106 | Administrator | hpvse123 |
    [Arguments]    ${IP}    ${USERNAME}=${APP_SSH_USERNAME}
    ...    ${PASSWORD}=${APP_SSH_PASSWORD}
    ...    ${TIMEOUT}=${APP_TIMEOUT}    ${ALIAS}=APP_SSH
    ${Id} =    Open Connection    ${IP}    alias=${ALIAS}
    ${Output} =    Login    ${USERNAME}    ${PASSWORD}
    [Return]    ${Id}
