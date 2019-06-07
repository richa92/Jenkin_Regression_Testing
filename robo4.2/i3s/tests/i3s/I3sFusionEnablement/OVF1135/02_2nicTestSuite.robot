*** Settings ***
Documentation     i3S  - Lifecycle - OS Deployment supports IP pools for NIC settings
Resource          resource.robot

Suite Setup        Login To Appliance And Verify Oneview Prerequisites    ${fusion_ip}    ${admin_credentials}
Test Setup         I3S Test Setup
Suite Teardown     I3S Suite Teardown

*** Test Cases ***

#Ping functionality lines are commented as private networks are used in the test cases for connection which cannot be reachable from i3S appliance.

OVF1135_TC65 Automatic IP assignment for 2-Nic configuration with Auto option for both the Nic's
    [Documentation]    Verify the mgmt ip's are picked automatically by both the nics in dual nic configuration
    ...    when selected AUTO option for both the nics on server profile page.
    [Tags]    2-nic    TC65

    ${sp_body} =    copy.deepcopy    ${sp_tc32}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticNic2StaticAndDhcp
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should not be similar.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_creating_sp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC66 IP assignment for 2-Nic configuration with Auto option for Nic1 and User-Specified for Nic2
    [Documentation]    Verify whether the mgmt ips are assigned properly for dual nic configuration & SP creation is successful
    ...    when selected AUTO for nic-1 and User-specified for nic-2.
    [Tags]    2-nic    TC66

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

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_creating_sp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC68 IP assignment for 2-Nic configuration with Auto option for Nic1 and None for Nic2 with no IP
    [Documentation]    Verify ip is assigned automatically when selected AUTO to nic-1 and NONE as nic connection-2
    [Tags]    2-nic    TC68

    ${sp_body} =    copy.deepcopy    ${sp_tc68}
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_creating_sp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC69 IP assignment for 2-Nic configuration with User-Specified option for both the Nic's
    [Documentation]    Verify whether the mgmt ips provided by user are assigned properly for dual nic configuration &
    ...    SP creation is successful when selected User-specified option for both the nics.
    [Tags]    2-nic    TC69

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

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_creating_sp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC73 Verify SP creation is successful when selected NONE as nic connection for both the nics
    [Documentation]    Verify SP creation is successful when selected NONE as nic connection for both the nics
    [Tags]    2-nic    TC73

    ${sp_body} =    copy.deepcopy    ${sp_tc37}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticAndDhcpNic2DisableNWConfig
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nServer Profile '${sp_body['name']}' failed as per expected    console=True
    ...    ELSE IF  '${blnCreateProf}'!='False'  Fail  \Server profile '${sp_body['name']}' created successfully which is not expected

OVF1135_TC74 Verify SP creation fails with validation error when selected NONE as nic connection for both the nics
    [Documentation]    Verify SP creation fails with validation error when selected NONE as nic connection1 and disabled nic connection for Nic2
    [Tags]    2-nic    TC74

    ${sp_body} =    copy.deepcopy    ${sp_tc74_master}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticAndDhcpNic2DisableNWConfig
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nServer Profile '${sp_body['name']}' failed as per expected    console=True
    ...    ELSE IF  '${blnCreateProf}'!='False'  Fail  \Server profile '${sp_body['name']}' created successfully which is not expected

OVF1135_TC77 User-Specified option enabled for connection not having subnet to Nic1 and NONE as Nic2
    [Documentation]    Verify that the user prompted to fill ip values when selected User-specified for
    ...    connection not having subnet to nic-1, NONE as nic connection-2
    [Tags]    2-nic    TC77

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

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_creating_sp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC78 SP creation successful with Auto option to Nic1 and User-Specified for Nic2
    [Documentation]    Verify whether the mgmt ips are assigned properly for dual nic configuration & SP creation is successful
    ...    when selected AUTO to connection having subnet for nic-1 and User-specified to the connection not having subnet for nic-2.
    [Tags]    2-nic    TC78

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

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_creating_sp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC79 SP creation successful with User-Specified option to Nic1 and User-Specified for Nic2
    [Documentation]    Verify whether ips & other ip values are assigned, when selected User-specified to connection having subnet for nic-1
    ...    and User-specified to the connection not having subnet
    [Tags]    2-nic    TC79

    ${sp_body} =    copy.deepcopy    ${sp_tc79_master}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticNic2StaticAndDhcp
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_creating_sp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC80 SP creation fails with dual nic configuration with same connection having subnet for both the nics
    [Documentation]    Verify that SP fails to create with validation error for dual nic configuration
    ...    when selected the same connection having subnet for both the nics.
    [Tags]    2-nic    TC80    dpWith2Nic_Nic1StaticNic2StaticAndDhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc40}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticNic2StaticAndDhcp
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nFailed to create profile '${sp_body['name']}' as per expected   level=WARN
    ...    ELSE IF  '${blnCreateProf}'=='True'  Fail  \nServer Profile '${sp_body['name']}' created successfully which is unexpected

OVF1135_TC81 SP creation fails with dual nic configuration with same connection not having subnet for both the nics
    [Documentation]    Verify that SP fails to create with validation error for dual nic configuration
    ...    when selected the same connection not having subnet for both the nics.
    [Tags]    2-nic    TC81    dpWith2Nic_Nic1StaticAndDhcpNic2Static

    ${sp_body} =    copy.deepcopy    ${sp_tc41}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticAndDhcpNic2Static
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nFailed to create profile '${sp_body['name']}' as per expected   level=WARN
    ...    ELSE IF  '${blnCreateProf}'=='True'  Fail  \nServer Profile '${sp_body['name']}' created successfully which is unexpected

OVF1135_TC94 Verify the SP creation fails with AUTO for tagged connection-1(from Netset-2) having subnet to nic-1, User-specified for untagged connection-2(from Netset-1) having subnet to nic-2
    [Documentation]    Verify the SP creation fails for dual-nic configuration when configured the nics as follows:
    ...    AUTO for tagged connection-1(from Netset-2) having subnet to nic-1,
    ...    User-specified for untagged connection-2(from Netset-1) having subnet to nic-2.
    [Tags]    2-nic    TC94

    ${sp_body} =    copy.deepcopy    ${sp_tc94}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticAndDhcpNic2Static
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nCreating Server Profile '${sp_body['name']}' failed as expected    console=True
    ...    ELSE IF  '${blnCreateProf}'!='False'  Fail  \nServer profile '${sp_body['name']}' created successfully which is not expected

OVF1135_TC95 Verify ips are assigned when AUTO for tagged connection (from Netset) having subnet to nic-1, AUTO for untagged connection (from Netset) having subnet to nic-2
    [Documentation]    Verify ips are assigned when configured the nics as follows:
    ...    AUTO for tagged connection (from Netset) having subnet to nic-1,
    ...    AUTO for untagged connection (from Netset) having subnet to nic-2
    [Tags]    2-nic    TC95

    ${sp_body} =    copy.deepcopy    ${sp_tc95}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticAndDhcpNic2Static
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nCreating Server Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC97 Verify the SP is updated, new ip is assigned with actual vlan id assigned when replaced the network connection with tagged network in netset in single NIC configuration
    [Documentation]    Verify the SP is updated, new ip is assigned with actual vlan id assigned when replaced the
    ...    network connection with tagged network in netset in single NIC configuration
    [Tags]    2-nic    TC97

    ${sp_body} =    copy.deepcopy    ${sp_tc51}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticAndDhcpNic2Static
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_creating_sp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10