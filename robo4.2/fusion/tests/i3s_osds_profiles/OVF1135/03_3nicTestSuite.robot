*** Settings ***
Documentation      i3S  - Lifecycle - OS Deployment supports IP pools for NIC settings
Resource           resource.robot

Suite Setup        Login To Appliance And Verify Oneview Prerequisites    ${fusion_ip}    ${admin_credentials}
Suite Teardown     I3S Suite Teardown
Test Setup         I3S Test Setup

*** Test Cases ***
OVTC53115
    [Documentation]    Verify the SP creation for 3-nic configuration is successful and ips are assigned properly when  configured nics as follows:
    ...    1. AUTO for connection having subnet for nic-1
    ...    2. User-specified for connection having subnet for nic-2 and
    ...    3. DHCP for connection having subnet for nic-3
    [Tags]    3-nic    OVF1135_TC42

    ${sp_body} =    copy.deepcopy    ${sp_tc42}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith3Nic_Nic1StaticAndDhcpNic2StaticNic3Dhcp
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

OVTC53116
    [Documentation]    Verify the SP creation for 3-nic configuration is successful and ips are assigned properly when configured nics as follows:
    ...    1. AUTO for connection having subnet for nic-1
    ...    2. NONE as a connection for nic-2 and
    ...    3. Network configuration is disabled for nic-3
    [Tags]    3-nic    OVF1135_TC43

    ${sp_body} =    copy.deepcopy    ${sp_tc43}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith3Nic_Nic1StaticDHCPNic2StaticDhcpDisableNWConfigNic3DisableNWConfig
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

OVTC53091
    [Documentation]    Verify the SP creation for 3-nic configuration is successful
    ...    when selected NONE as connection for 3-nics
    [Tags]    3-nic    OVF1135_TC44

    ${sp_body} =    copy.deepcopy    ${sp_tc44}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith3Nic_Nic1StaticAndDisableNWConfigNic2DhcpAndDisableNWConfigNic3DisableNWConfig
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

OVTC53117
    [Documentation]    Verify the SP creation for 3-nic configuration is successful and ips are assigned properly when  configured nics as follows:
    ...    1. User-specified for connection having subnet but no ip pools for nic-1
    ...    2. AUTO for connection having subnet for nic-2 and
    ...    3. AUTO for connection having subnet for nic-3
    [Tags]    3-nic    OVF1135_TC45

    ${sp_body} =    copy.deepcopy    ${sp_tc45}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith3Nic_Nic1StaticNic2StaticNic3Static
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

OVTC53118
    [Documentation]    Verify the SP creation fails for 3-nic configuration  when  configured nics as follows:
    ...    1. User-specified for connection not having subnet for nic-1 and provide manual ip outside subnet.
    ...    2. AUTO for connection having subnet for nic-2 and
    ...    3. user-specified for connection having subnet for nic-3 and provided ip address from outside subnet.
    [Tags]    3-nic    OVF1135_TC46

    ${sp_body} =    copy.deepcopy    ${sp_tc46}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith3Nic_Nic1StaticNic2StaticNic3Static
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

OVTC53095
    [Documentation]    Verify the SP creation fails for dual-nic configuration when configured the nics as follows:
    ...    AUTO for tagged connection-1(from Netset-2) having subnet to nic-1,
    ...    User-specified for untagged connection-2(from Netset-1) having subnet to nic-2.
    [Tags]    3-nic    OVF1135_TC50

    ${sp_body} =    copy.deepcopy    ${sp_tc50}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith3Nic_Nic1StaticNic2StaticNic3Static
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nCreating Server Profile '${sp_body['name']}' failed as expected    console=True
    ...    ELSE IF  '${blnCreateProf}'!='False'  Fail  \nServer profile '${sp_body['name']}' created successfully which is not expected

OVTC53120
    [Documentation]    Verify the SP is created successfully for dual-nic configuration showing all the vlan id properly and all the mgmt ips are assigned properly
    ...    when configured the nics as follows:
    ...    AUTO for untagged connection (from Netset-2) having subnet to nic-1,
    ...    AUTO for another untagged connection (from Netset-1) having subnet to nic-2.
    [Tags]    3-nic    OVF1135_TC51

    ${sp_body} =    copy.deepcopy    ${sp_tc51}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith3Nic_Nic1StaticNic2StaticNic3Static
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
