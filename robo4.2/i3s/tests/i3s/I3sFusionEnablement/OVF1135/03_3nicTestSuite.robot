*** Settings ***
Documentation      i3S  - Lifecycle - OS Deployment supports IP pools for NIC settings
Resource           resource.robot

Suite Setup        Login To Appliance And Verify Oneview Prerequisites    ${fusion_ip}    ${admin_credentials}
Test Setup         I3S Test Setup
Suite Teardown     I3S Suite Teardown

*** Test Cases ***

#Ping functionality lines are commented as private networks are used in the test cases for connection which cannot be reachable from i3S appliance.

OVF1135_TC83 SP creation successful with Auto option for Nic1, None option to Nic2 and Netork conn is Disabled option for Nic3
    [Documentation]    Verify the SP creation for 3-nic configuration is successful and ips are assigned properly when configured nics as follows:
    ...    1. AUTO for connection having subnet for nic-1
    ...    2. NONE as a connection for nic-2 and
    ...    3. Network configuration is disabled for nic-3
    [Tags]    3-nic    TC83

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

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_creating_sp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC84 SP creation successful with Auto option for all 3 nic's having subnet
    [Documentation]    Verify ips are assigned properly when configured nics as follows:
    ...    1. AUTO for connection having subnet for nic-1
    ...    2. AUTO for connection having subnet for nic-2
    ...    3. AUTO for connection having subnet for nic-3
    [Tags]    3-nic    TC84

    ${sp_body} =    copy.deepcopy    ${sp_tc84}
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

OVF1135_TC85 SP creation successful with User-specified option for Nic1 and Nic2 with no subnet user-specified option for 3 nic's having subnet
    [Documentation]    Verify ips are assigned properly when configured nics as follows:User-specified for connection not having subnet for nic-1,
    ...    User-specified for connection  with no subnet for nic-2 and,User-specified for connection having subnet for nic3
    [Tags]    3-nic    TC85

    ${sp_body} =    copy.deepcopy    ${sp_tc85}
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

OVF1135_TC86 Verify the SP creation for 3-nic configuration is successful when selected NONE as connection for 3-nics
    [Documentation]    Verify the SP creation for 3-nic configuration is successful
    ...    when selected NONE as connection for 3-nics
    [Tags]    3-nic    TC86

    ${sp_body} =    copy.deepcopy    ${sp_tc44}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith3Nic_Nic1StaticAndDisableNWConfigNic2DhcpAndDisableNWConfigNic3DisableNWConfig
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

OVF1135_TC87 SP creation for 3-nic configuration is successful with Nic1 having User-Specified option having subnet but no IP Pools, Auto option for Nic2 and Nic3
    [Documentation]    Verify the SP creation for 3-nic configuration is successful and ips are assigned properly when  configured nics as follows:
    ...    1. User-specified for connection having subnet but no ip pools for nic-1
    ...    2. AUTO for connection having subnet for nic-2 and
    ...    3. AUTO for connection having subnet for nic-3
    [Tags]    3-nic    TC87

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

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_creating_sp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC88 SP creation fails with Auto option for Nic1 having subnet but no free ip's in ip pool,Auto option for Nic2 having subnet and User-Specified for Nic3
    [Documentation]    Verify the SP creation fails for 3-nic configuration when configured nics as follows:
    ...    1. AUTO for connection having subnet but no free ips in ip pools for nic-1,
    ...    2. AUTO for connection having subnet for nic-2 and,
    ...    3. USER-specified for connection nic3
    [Tags]    3-nic    TC88

    ${sp_body} =    copy.deepcopy    ${sp_tc88}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith3Nic_Nic1StaticNic2StaticNic3Static
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nFailed to create profile '${sp_body['name']}'
    ...    ELSE IF  '${blnCreateProf}'!='False'  Fail  \nServer Profile '${sp_body['name']}' created successfully which is unexpected    console=True

OVF1135_TC89 SP creation fails with User-Specified option for connection not having subnet and provide manual ip outside subnet for Nic1 and Nic3, Auto option for Nic2 having subnet
    [Documentation]    Verify the SP creation fails for 3-nic configuration  when  configured nics as follows:
    ...    1. User-specified for connection not having subnet for nic-1 and provide manual ip outside subnet.
    ...    2. AUTO for connection having subnet for nic-2 and
    ...    3. User-specified for connection having subnet for nic-3 and provided ip address from outside subnet.
    [Tags]    3-nic    TC89

    ${sp_body} =    copy.deepcopy    ${sp_tc46}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith3Nic_Nic1StaticNic2StaticNic3Static
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

OVF1135_TC90 Verify the SP creation fails when selected the same connection having subnet for all the 3-nics
    [Documentation]    Verify the SP creation fails when selected the same connection having subnet for all the 3-nics
    [Tags]    3-nic    TC90

    ${sp_body} =    copy.deepcopy    ${sp_tc90}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith3Nic_Nic1StaticNic2StaticNic3Static
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='False'  Fail  \nFailed to create profile '${sp_body['name']}'