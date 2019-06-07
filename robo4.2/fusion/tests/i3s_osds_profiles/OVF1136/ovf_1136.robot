*** Settings ***
Documentation     OVF1136: i3S - Lifecycle - OS Deployment included in Server Profile Template

Resource          resource.robot
Suite Setup        Login To Appliance And Verify Oneview Prerequisites    ${fusion_ip}    ${admin_credentials}
Suite Teardown     I3S Suite Teardown
Test Setup         OVF1136 Test Setup    ${profileTemplate}

*** Test Cases ***
OVTC53128
    [Documentation]    Verify whether SPT is created with NONE as a deployment plan
    [Tags]    OVF1136_TC03
    OVF1136 Test Setup    ${profileTemplate}
    ${spt} =    copy.deepcopy    ${tc03_spt}

    ${payload} =    Create Server Profile Template Payload    ${tc03_spt}
    ${resp}=    Fusion Api Create Server Profile Template    ${payload}
    ${blnStatus}=    Capture Task Status    ${resp}    1200
    Should Be True    ${blnStatus}    msg=Failed to create profile '${spt['name']}'

OVTC53134
    [Documentation]    Verify whether we can add new connections to server profile other than those present in SPT
    [Tags]    OVF1136_TC09
    OVF1136 Test Setup    ${profileTemplate}
    ${tc09_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc09_spt}
    Should Be True    ${blnCreateSPT}    msg=Failed to create profile '${tc09_spt['name']}'

    ${tc09_sp} =    copy.deepcopy    ${sp_from_spt}
    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${tc09_sp}
    Should Be True    ${blnCreateSPFromSPT}    msg=Failed to create profile '${tc09_sp['name']}'

    Log    \nAdding new connection to profile    console=True
    ${spbody}=    Get Server Profile    ${tc09_sp['name']}
    ${sp_uri}=    Get from dictionary    ${spbody}    uri
    ${connectionSettings}=    Get from dictionary    ${spbody}    connectionSettings
    ${connections}=    Get from dictionary    ${connectionSettings}    connections
    ${networkUri}=    replace string using regexp    ${new_profile_connection['networkUri']}    ETH:    ${EMPTY}
    ${networkUri}=    Get Ethernet URI    ${networkUri}
    Set To Dictionary    ${new_profile_connection}    networkUri    ${networkUri}
    Append To List    ${connections}    ${new_profile_connection}
    ${response}=    Fusion API Edit Server Profile    ${spbody}    ${sp_uri}
    Wait For Task2    ${response}    timeout=2400    interval=20

OVTC53141
    [Documentation]    Verify SPT creation is successful with blank custom attribute values
    [Tags]    OVF1136_TC16
    OVF1136 Test Setup    ${profileTemplate}
    ${tc16_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc16_spt}
    Should Be True    ${blnCreateSPT}    msg=Failed to create profile '${tc16_spt['name']}'

OVTC53142
    [Documentation]    Verify whether the deployment connections can be deleted when deployment plan is present on SPT
    [Tags]    OVF1136_TC17
    OVF1136 Test Setup    ${profileTemplate}
    ${tc17_spt} =    copy.deepcopy    ${spt}
    ${blnCreateSPT} =    Create I3S SPT    ${tc17_spt}
    Should Be True    ${blnCreateSPT}    msg=Failed to Create Server profile '${tc17_spt['name']}'

    ${blnEditSPT} =    Edit I3S SPT    ${tc17_edit_spt}
    Should Not Be True    ${blnEditSPT}    msg= deployment connections deleted successfully when deployment plan is present on SPT
