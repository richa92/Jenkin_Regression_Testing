*** Settings ***
Documentation     i3S  - Lifecycle - OS Deployment supports IP pools for NIC settings
Resource          resource.robot

Suite Setup        Login To Appliance And Verify Oneview Prerequisites    ${fusion_ip}    ${admin_credentials}
Suite Teardown     I3S Suite Teardown
Test Setup         I3S Test Setup

*** Test Cases ***
OVTC53081
    [Documentation]    Verify the mgmt ip's are picked automatically by both the nics in dual nic configuration
    ...    when selected AUTO option for both the nics on server profile page.
    [Tags]    2-nic    OVF1135_TC32

    ${sp_body} =    copy.deepcopy    ${sp_tc32}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticNic2StaticAndDhcp
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

OVTC53082
    [Documentation]    Verify whether the mgmt ips are assigned properly for dual nic configuration & SP creation is successful
    ...    when selected AUTO for nic-1 and User-specified for nic-2.
    [Tags]    2-nic    OVF1135_TC33

    ${sp_body} =    copy.deepcopy    ${sp_tc33}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticNic2StaticAndDhcp
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

OVTC53083
    [Documentation]    Verify whether mgmt ips are assigned properly for dual nic configuration & SP creation is successful
    ...    when selected AUTO for nic-1 and DHCP for nic-2.
    [Tags]    2-nic    OVF1135_TC34

    ${sp_body} =    copy.deepcopy    ${sp_tc34}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticNic2StaticAndDhcp
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

OVTC53084
    [Documentation]    Verify whether the mgmt ips provided by user are assigned properly for dual nic configuration &
    ...    SP creation is successful when selected User-specified option for both the nics.
    [Tags]    2-nic    OVF1135_TC35

    ${sp_body} =    copy.deepcopy    ${sp_tc35}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticAndDhcpNic2Static
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

OVTC53085
    [Documentation]    Verify whether mgmt ips are assigned by DHCP server
    ...    for both the nics in dual nic configuration & SP creation is successful.
    [Tags]    2-nic    OVF1135_TC36

    ${sp_body} =    copy.deepcopy    ${sp_tc36}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticAndDhcpNic2Dhcp
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

OVTC53086
    [Documentation]    Verify whether the SP creation fails with validation error when selected NONE as nic connection for both the nics
    ...    when NOT disabled network configuration for nic-1 in OSBP and disabled network configuration for nic-2 in OSBP
    [Tags]    2-nic    OVF1135_TC37

    ${sp_body} =    copy.deepcopy    ${sp_tc37}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticAndDhcpNic2DisableNWConfig
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nServer Profile '${sp_body['name']}' failed as per expected    console=True
    ...    ELSE IF  '${blnCreateProf}'!='False'  Fail  \Server profile '${sp_body['name']}' created successfully which is not expected

OVTC53087
    [Documentation]    Verify that the user should provide all ip values when selected User-specified
    ...    for connection not having subnet to nic-1 and NONE as nic connection-2 should be accepted
    ...    without any error when disabled network configuration for nic-2 in OSBP.
    [Tags]    2-nic    OVF1135_TC38

    ${sp_body} =    copy.deepcopy    ${sp_tc38}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticNic2DhcpAndDisabledNWConfig
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

OVTC53088
    [Documentation]    Verify whether the mgmt ips are assigned properly for dual nic configuration & SP creation is successful
    ...    when selected AUTO to connection having subnet for nic-1 and User-specified to the connection not having subnet for nic-2.
    [Tags]    2-nic    OVF1135_TC39

    ${sp_body} =    copy.deepcopy    ${sp_tc39}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticNic2StaticAndDhcp
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

OVTC53089
    [Documentation]    Verify that SP fails to create with validation error for dual nic configuration
    ...    when selected the same connection having subnet for both the nics.
    [Tags]    2-nic    OVF1135_TC40

    ${sp_body} =    copy.deepcopy    ${sp_tc40}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticNic2StaticAndDhcp
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nFailed to create profile '${sp_body['name']}' as per expected   level=WARN
    ...    ELSE IF  '${blnCreateProf}'=='True'  Fail  \nServer Profile '${sp_body['name']}' created successfully which is unexpected

OVTC53090
    [Documentation]    Verify that SP fails to create with validation error for dual nic configuration
    ...    when selected the same connection not having subnet for both the nics.
    [Tags]    2-nic    OVF1135_TC41

    ${sp_body} =    copy.deepcopy    ${sp_tc41}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticAndDhcpNic2Static
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nFailed to create profile '${sp_body['name']}' as per expected   level=WARN
    ...    ELSE IF  '${blnCreateProf}'=='True'  Fail  \nServer Profile '${sp_body['name']}' created successfully which is unexpected
