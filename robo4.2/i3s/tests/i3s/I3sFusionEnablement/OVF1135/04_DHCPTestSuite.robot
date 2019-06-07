*** Settings ***
Documentation      i3S  - Lifecycle - OS Deployment supports IP pools for NIC settings
Resource           resource.robot

Suite Setup        Login To Appliance And Verify Oneview Prerequisites    ${fusion_ip}    ${admin_credentials}
Suite Teardown     I3S Suite Teardown
Test Setup         I3S Test Setup

*** Test Cases ***

#DHCP Test Cases

#Ping functionality lines are commented as private networks are used in the test cases for connection which cannot be reachable from i3S appliance.

OVF1135_TC14 Verify that all the values are obtained from DHCP server when enabled DHCP for a connection associated with SUBNET
    [Documentation]    Verify that all the values are obtained from DHCP server when enabled DHCP for a connection associated with SUBNET
    [Tags]    Dhcp-1-nic    TC14    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc09}
    #${sp_tc09} is used as a generic json. Hence the deployment plan is being set with the same custom attributes in the below line.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    # Create Server Profile with DHCP option
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

OVF1135_TC18 Verify that all the values are obtained from DHCP server when enabled DHCP for a connection NOT associated with SUBNET
    [Documentation]  Verify that all the values are obtained
    ...    from DHCP server when enabled DHCP for a connection NOT associated with SUBNET
    [Tags]    Dhcp-1-nic    TC18    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc12}
    #${sp_tc12} is used as a generic json. Hence the deployment plan is being set with the same custom attributes in the below line.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_DhcpNic
    Delete Server Profile    ${sp_body['name']}

    # check that user should not provide ipaddress, netmask, gateway, dns1, dns2 attributes in SP body
    ${attributes} =    Create List    ipaddress    netmask    gateway    dns1    dns2
    ${attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_body}    ${attributes}
    should contain x times    ${attrib_values}    None    5    msg=Custom attributes should not be provided in SP body

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

OVF1135_TC26 Verify the DHCP option appears for a connection NOT associated with SUBNET when enabled both STATIC & DHCP in NIC settings of build plan
    [Documentation]    Verify the DHCP option appears for a connection NOT associated with SUBNET
    ...    when enabled both STATIC & DHCP in NIC settings of build plan.
    [Tags]    Dhcp-1-nic    TC26    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc17}
    #${sp_tc017} is used as a generic json. Hence the deployment plan is being set with the same custom attributes in the below line.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    # Create Server Profile with DHCP option
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

OVF1135_TC47 Verify whether mgmt ip is released and new ip is assigned when changed DP1 having DHCP option to DP2 having DHCP option
    [Documentation]    Verify whether mgmt ip is released and new ip is assigned
    ...    when changed the deployment plan from DP1 having DHCP option to DP2 having DHCP option.
    [Tags]    Dhcp-1-nic    TC117    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc66}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_before_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_before_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    # Edit profile and change OSDP
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp2With1Nic_StaticAndDhcpNic
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DO    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_dp}!=${mngt_ip_after_changing_dp}    Log    \nProfile management IP changed after changing DP    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC52 Verify whether the mgmt ip of SP is released and new ip is assigned by DHCP server when Nic option changed from auto to dhcp
    [Documentation]    Verify whether the mgmt ip of SP is released and new ip is assigned by DHCP server when Nic option changed from auto to dhcp
    [Tags]    Dhcp-1-nic    TC52    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_before_changing_nic[0]}    None    msg=Mgmt ip address should be assigned.
    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_before_changing_nic[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    ${sp_body} =    copy.deepcopy    ${sp_tc09}

    # Edit profile and change OSDP
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_nic[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_nic}!=${mngt_ip_after_changing_nic}    Log    \nProfile management IP changed after changing the connection type    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_nic[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC56 Verify whether ip is assigned to SP when changed connection from NONE to NIC connection of type DHCP
    [Documentation]    Verify whether ip is assigned to SP when changed connection from NONE to NIC connection of type DHCP
    [Tags]    Dhcp-1-nic    TC56    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc19}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_DisabledNWConfig
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Be Equal as Strings    ${mngt_ip_before_changing_nic[0]}    None    msg=Mgmt ip address should be assigned.
    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_before_changing_nic[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    ${sp_body} =    copy.deepcopy    ${sp_tc09}

    # Edit profile and change OSDP
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_nic[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_nic}!=${mngt_ip_after_changing_nic}    Log    \nProfile management IP changed after changing the connection type    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_nic[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC58 Verify whether ip is released, ip is assigned to SP from ip pool when changed the NIC connection from DHCP to AUTO
    [Documentation]    Verify whether ip is released, ip is assigned to SP from ip pool when changed the NIC connection from DHCP to AUTO
    [Tags]    Dhcp-1-nic    TC58    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc09}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Be Equal as Strings    ${mngt_ip_before_changing_nic[0]}    None    msg=Mgmt ip address should be assigned.
    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_before_changing_nic[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic

    # Edit profile and change OSDP
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_nic[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_nic}!=${mngt_ip_after_changing_nic}    Log    \nProfile management IP changed after changing the connection type    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_nic[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC59 Verify whether ip is released, ip is assigned to SP when changed the NIC connection from DHCP to User-specified
    [Documentation]    Verify whether ip is released, ip is assigned to SP when changed the NIC connection from DHCP to User-specified
    [Tags]    Dhcp-1-nic    TC59    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc09}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Be Equal as Strings    ${mngt_ip_before_changing_nic[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_before_changing_nic[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic

    # Edit profile and change OSDP
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_nic[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_nic}!=${mngt_ip_after_changing_nic}    Log    \nProfile management IP changed after changing the connection type    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_nic[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC60 Verify whether ip is released, no ip is assigned to SP when changed the DHCP NIC connection to NONE
    [Documentation]    Verify whether ip is released, no ip is assigned to SP when changed the DHCP NIC connection to NONE
    [Tags]    Dhcp-1-nic    TC60    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc09}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_before_changing_nic[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_before_changing_nic[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    ${sp_body} =    copy.deepcopy    ${sp_tc19}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_DisabledNWConfig
    Delete Server Profile    ${sp_body['name']}

    # Edit profile and change OSDP
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Be Equal as Strings    ${mngt_ip_after_changing_nic[0]}    None    msg=Mgmt ip address should not be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_nic}!=${mngt_ip_after_changing_nic}    Log    \nProfile management IP changed after changing the connection type    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_nic[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC62 Verify whether ip of SP is released and new ip is assigned to SP, when changed the NIC connection type from User-specified to DHCP
    [Documentation]    Verify whether ip of SP is released and new ip is assigned to SP, when changed the NIC connection type from User-specified to DHCP
    [Tags]    Dhcp-1-nic    TC62    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_before_changing_nic[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_before_changing_nic[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    ${sp_body} =    copy.deepcopy    ${sp_tc09}
    Delete Server Profile    ${sp_body['name']}

    # Edit profile and change OSDP
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_nic[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_nic}!=${mngt_ip_after_changing_nic}    Log    \nProfile management IP changed after changing the connection type    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_nic[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC67 IP assignment for 2-Nic configuration with Auto option for Nic1 and DHCP for Nic2
    [Documentation]    Verify whether mgmt ips are assigned properly for dual nic configuration & SP creation is successful
    ...    when selected AUTO for nic-1 and DHCP for nic-2.
    [Tags]    Dhcp-2-nic    TC67    Dhcp

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

OVF1135_TC70 IP assignment for 2-Nic configuration with User-Specified option for Nic1 and DHCP for Nic2
    [Documentation]    Verify ips are assigned for dual nic configuration, when selected User-specified for nic-1 and DHCP for nic-2
    [Tags]    Dhcp-2-nic    TC70    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc70_master}
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

OVF1135_TC71 IP assignment for 2-Nic configuration with DHCP option for both the NIC's
    [Documentation]    Verify whether mgmt ips are assigned by DHCP server
    ...    for both the nics in dual nic configuration & SP creation is successful.
    [Tags]    Dhcp-2-nic    TC71    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc36}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticAndDhcpNic2Dhcp
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

OVF1135_TC72 IP assignment for 2-Nic configuration with DHCP option for Nic1 and NONE for Nic2
    [Documentation]    Verify ip is assigned by DHCP server when selected DHCP to nic-1 and NONE as nic connection-2
    [Tags]    Dhcp-2-nic    TC72    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc72_master}
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

OVF1135_TC75 Verify whether mgmt ip is released and new ip is assigned when changed DP1 having DHCP option to DP2 having USER-SPECIFIED option
    [Documentation]    Verify whether mgmt ip is released and new ip is assigned when changed the deployment plan from
    ...    DP1 having DHCP option to DP2 having USER-SPECIFIED option
    [Tags]    Dhcp-1-nic    TC116    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc09}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_DhcpNic
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_before_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_before_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic

    # Edit profile and change OSDP
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_dp}!=${mngt_ip_after_changing_dp}    Log    \nProfile management IP changed after changing the connection type    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC76 SP creation with Nic1 User-Specified and Nic2 with DHCP, both not having subnets
    [Documentation]    Verify the SP creates for dual nic configuration when selected user-specified for connection not having subnet for nic-1
    ...    & DHCP for connection not having subnet for nic-2
    [Tags]    Dhcp-2-nic    TC76    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc76_master}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith2Nic_Nic1StaticNic2StaticAndDhcp
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

OVF1135_TC82 SP creation successful with Auto option for Nic1, User-Specified option to Nic2 and DHCP option for Nic3
    [Documentation]    Verify the SP creation for 3-nic configuration is successful and ips are assigned properly when  configured nics as follows:
    ...    1. AUTO for connection having subnet for nic-1
    ...    2. User-specified for connection having subnet for nic-2 and
    ...    3. DHCP for connection having subnet for nic-3
    [Tags]    Dhcp-3-nic    TC82    Dhcp

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

OVF1135_TC106 Verify whether mgmt ip is released and new ip is assigned when changed the deployment plan
    [Documentation]    Verify whether mgmt ip is released and new ip is assigned when changed the deployment plan
    ...    from DP1 having DHCP option to DP2 having AUTO option
    [Tags]    Dhcp-1-nic    TC115    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc09}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_DhcpNic
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_before_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_before_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic

    # Edit profile and change OSDP
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_dp}!=${mngt_ip_after_changing_dp}    Log    \nProfile management IP changed after changing the connection type    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC111 Verify whether mgmt ip is released and new ip is assigned when changed the deployment plan from DP1 having AUTO option to DP2 having DHCP option
    [Documentation]    Verify whether mgmt ip is released and new ip is assigned when changed the deployment plan from DP1 having AUTO option to DP2 having DHCP option
    [Tags]    Dhcp-1-nic    TC111    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_before_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_before_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    ${sp_body1} =    copy.deepcopy    ${sp_tc09}
    Set To Dictionary    ${sp_body1['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_DhcpNic
    #Delete Server Profile    ${sp_body1['name']}

    # Edit profile and change OSDP
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body1}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body1['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body1['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body1['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_dp}!=${mngt_ip_after_changing_dp}    Log    \nProfile management IP changed after changing the connection type    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body1['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_dp[0]}
    Power Off Profile Server    ${sp_body1['serverHardwareUri']}
    Sleep    10

OVF1135_TC113 Verify whether user provided mgmt ip is released and new ip from pool is assigned when changed
    [Documentation]    Verify whether user provided mgmt ip is released and new ip from pool is assigned when changed
    ...    the deployment plan from DP1 having USER-SPECIFIED option to DP2 having DHCP option
    [Tags]    Dhcp-1-nic    TC114    Dhcp

    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_before_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_before_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    ${sp_body} =    copy.deepcopy    ${sp_tc09}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_DhcpNic
   #Delete Server Profile    ${sp_body['name']}

    # Edit profile and change OSDP
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_dp}!=${mngt_ip_after_changing_dp}    Log    \nProfile management IP changed after changing the connection type    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10