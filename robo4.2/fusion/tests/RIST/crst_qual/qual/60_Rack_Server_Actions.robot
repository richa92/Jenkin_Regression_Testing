*** Settings ***
Documentation    Execute Rack Servers (DL) Actions
Resource                ../resource.txt

Variables                       ../Common.py
Variables                       ../${DATA_FILE}

Suite Setup                     QUAL Suite Setup    ${ADMIN_CREDENTIALS}
Suite Teardown                  QUAL Suite Teardown

*** Test Cases ***
Refresh Rack Servers
    [Documentation]    Refresh All Servers defined in ${CONFIRM_SERVER_PROFILES_ONE}
    [Tags]    TEST    60    REFRESH_DL

    Wait For ALL Servers Complete Refresh

    Log      Refreshing Servers in Profiles    console=${CONSOLE}
    ${resp} =    Refresh Servers in Profiles    ${CONFIRM_SERVER_PROFILES_ONE}
    Wait For Task2    ${resp}

Reset Rack Servers iLO
    [Documentation]    Resets All Server ilOs defined in ${DL_SERVER_FQDN}
    [Tags]    TEST    60    RESET_DL_ILO

    Log      Reset Server iLO in Profiles    console=${CONSOLE}
    :FOR    ${fqdn}    IN    @{DL_SERVER_FQDN}
    \    ${sh} =    Set Variable    SH:${fqdn}
    \    ${resp} =    Reset Server Hardware iLO    ${sh}
    \    Should Be Equal As Integers    ${resp['status_code']}    ${BADREQUEST}    Reset iLO not allowed on DL
    \    Should Be Equal As Strings     ${resp['message']}    ProLiant DL360 Gen10 is not support for resetting management processor.

Servers Should Be
    [Documentation]    Confirms Servers are still in the expected status
    [Tags]    TEST    60    DL_STATUS
    Verify Resources for List    ${EXPECTED_RACK_SERVERS}    status=${DL_ADD_STATUS}

Get Critical IML Events
    [Tags]    TEST    60    GET_CRITICAL_IML
    :FOR    ${server}    IN    @{DL_SERVER_FQDN}
    \    ${uri} =    Run Keyword     Common URI lookup by name    SH:${server}
    \    ${serverExists} =    Run Keyword And Return Status    Should Not Contain    ${uri}    ${server}_not_found
    \    Run Keyword If    ${serverExists}==${False}    Log   ${server} not found    level=ERROR    console=True
    \    Continue For Loop If    ${serverExists}==${False}
    \    ${token} =       Get Trusted Token        ${APPLIANCE_IP}
    \    ${iSERVER} =     Get iLO ipv6     ${token}   ${uri}
    \    ${iUSER} =       set variable     _HPOneViewAdmin
    \    ${iPASSWORD} =   Get _HPOneViewAdmin iLO credentials   ${token}   ${uri}
    \    ${ribcl} =       OperatingSystem.Get file   ..\\..\\..\\Tools\\cpqlocfg\\actions\\Get_IML.xml
    \    ${postProcess} =    set variable    2>/dev/null | sed -n -e '/<EVENT_LOG DESCRIPTION="Integrated Management Log">/,/<\\/EVENT_LOG>/ p'
    \    ${response} =      Execute RIBCL xml     ${iUSER}    ${iPASSWORD}   ${iSERVER}   ${ribcl}    ${postProcess}
    \
    \    ${xml} =  Parse XML  ${response}
    \    ${events} =  Get Elements  ${xml}  EVENT
    \    Get Critical Severity and Description   ${server}    ${events}


*** Keywords ***
Get Critical Severity and Description
    [Documentation]    Logs as ERROR IML events that are Critical
    [Arguments]    ${host}    ${events}
    :FOR    ${event}    in    @{events}
    \    ${severity} =    XML.Get Element Attribute    ${event}    SEVERITY
    \    ${description} =    XML.Get Element Attribute   ${event}    DESCRIPTION
    \    Run Keyword If    '${severity}'=='Critical'    Log   IML Alert @ ${host} -> ${severity}:${description}    level=ERROR    console=True
