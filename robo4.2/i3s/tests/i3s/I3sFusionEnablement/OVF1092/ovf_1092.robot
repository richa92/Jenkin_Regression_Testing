*** Settings ***
Documentation     OVF1092: OSS Management
Resource          resource.robot
Suite Setup       Login To Appliance And Verify Oneview Prerequisites    ${fusion_ip}    ${admin_credentials}
Suite Teardown    I3S Suite Teardown
Test Setup        I3S Test Setup

*** Test Cases ***
OVF1092_TC01
    [Documentation]    Verify Deployment Image is created when Server Profile is assigned to server hardware
    [Tags]    TC01    MAT

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    Failed to create profile '${sp_body['name']}'

    Log    \nValidating Os Volume after creating server profile
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

OVF1092_TC02
    [Documentation]    Verify No Deployment Image is created with unassigned  Server Profile
    [Tags]    TC02    MAT

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create un-assigned server profile
    Set To Dictionary    ${sp_body}    serverHardwareUri=${None}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    Failed to create profile '${sp_body['name']}'

    Log    \nVerifying whether OS Volume is assigned to server profile '${sp_body['name']}'
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should be equal as strings    '${os_vol}'    'None'    msg=Volume is not created

OVF1092_TC03
    [Documentation]    Verify Deployment Image is deleted when Server Profile is deleted(normal delete)
    [Tags]    TC03    MAT

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Should Be True    ${blnCreateProf}    Failed to create profile '${sp_body['name']}'

    Log    \nValidating Os Volume after creating server profile
    ${osVolUri} =    Get Server Profile OS Volume URI    ${sp_body['name']}
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    ${prof} =    Get Profile From OS Volume    ${os_vol}
    Should Be Equal    ${sp_body['name']}    ${prof}    Os Volume ${os_vol} associted to profile ${sp_body['name']} is not present in I3S

    Delete Server Profile    ${sp_body['name']}    ${False}
    ${resp1}=    Get Resource by URI    ${osVolUri}
    Should Be Equal As Integers    ${resp1['status_code']}    404    Failed to delete profile OS volume after deleting profile

OVF1092_TC04
    [Documentation]    Verify Deployment Image is deleted when Server Profile is deleted(force delete)
    [Tags]    TC04    MAT

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}    ${True}

    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'    Fail  Failed to create profile '${sp_body['name']}'

    Log    \nVerifying whether OS Volume is assigend to profile '${sp_body['name']}'
    ${osVolUri} =    Get Server Profile OS Volume URI    ${sp_body['name']}
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    Delete Server Profile    ${sp_body['name']}
    ${resp1}=    Get Resource by URI    ${osVolUri}
    Run Keyword If    '${resp1['status_code']}' == '404'    Log    \nOS volume is deleted after deleting SP '${sp_body['name']}'    console=True
    ...    ELSE    Fail    Failed to delete profile OS volume after deleting profile

OVF1092_TC10
    [Documentation]    Verify Deployment image is deleted when Deployment Plan is removed from Server Profile
    [Tags]    TC10    EXTENDED-MAT

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}    ${True}

    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'    Fail  Failed to create profile '${sp_body['name']}'

    Log    \nVerifying whether OS Volume is assigned to server profile '${sp_body['name']}'
    ${osVolUri} =    Get Server Profile OS Volume URI    ${sp_body['name']}
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

    ${blnChangeOsdp}=    Change Server Profile OSDP To None    ${sp_body['name']}
    Run Keyword If     ${blnChangeOsdp}!=True    Fail    Failed to delete osdp from profile
    ${resp1}=    Get Resource by URI    ${osVolUri}
    Run Keyword If    '${resp1['status_code']}' == '404'    Log    \nOS volume is deleted after deleting SP '${sp_body['name']}'    console=True
    ...    ELSE    Fail    Failed to delete profile OS volume after deleting profile

OVF1092_TC11
    [Documentation]    Verify Deployment Image is deleted and recreated
    ...    when Deployment Plan and/or Deployment attributes are modified
    [Tags]    TC11    EXTENDED-MAT

    ${sp_body} =    copy.deepcopy    ${serverprofiles}
    Delete Server Profile    ${sp_body['name']}    ${True}

    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    Log    \nVerifying whether OS Volume is assigned to server profile '${sp_body['name']}'
    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp2With1Nic_StaticAndDhcpNic
    # Remove From Dictionary    ${sp_body}    serverHardwareUri
    ${blnEditPorf}=    Edit I3S Server Profile    ${sp_body}
    Run Keyword If  '${blnEditPorf}'!='True'    Fail    Failed to update server profile '${sp_body['name']}'

    Log    \nVerifying whether OS Volume recreated server profile '${sp_body['name']}'
    ${os_vol1}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol1}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'
    Should not be equal as strings    '${os_vol}'    '${os_vol1}'    msg=OS volume not recreated
