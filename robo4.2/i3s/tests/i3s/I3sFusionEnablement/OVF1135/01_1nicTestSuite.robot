*** Settings ***
Documentation     i3S  - Lifecycle - OS Deployment supports IP pools for NIC settings
Resource          resource.robot

Suite Setup        Login To Appliance And Verify Oneview Prerequisites    ${fusion_ip}    ${admin_credentials}
Test Setup         I3S Test Setup
Suite Teardown     I3S Suite Teardown

*** Test Cases ***

#Ping functionality lines are commented as private networks are used in the test cases for connection which cannot be reachable from i3S appliance.

OVF1135_TC04 Verify that only ipv4 address should be provided by user when enabled USER-SPECIFIED for a connection associated with SUBNET
    [Documentation]    Verify that only ipv4 address should be provided by user when enabled USER-SPECIFIED for a connection associated with SUBNET when enabled USER-SPECIFIED for a connection associated with SUBNET
    [Tags]    1-nic    TC04

    # Create Server Profile with User-Specified option
    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    #${sp_tc02} is used as a generic json. Hence the deployment plan is being set with the same custom attributes in the below line.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify profile body should have netmask, gateway, dns1, dns2 attributes
    Log    \nVerify profile body should have netmask, gateway, dns1, dns2 attributes    console=True
    ${resp_attributes} =    Create List    ipaddress    netmask    gateway    dns1    dns2
    ${resp_attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_response}    ${resp_attributes}
    list should not contain value    ${resp_attrib_values}    None    msg=All Custom attribute should be auto-filled after SP creation.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC05 Obtain NIC values automatically when enabled Auto option for a connection associated with Subnet
    [Documentation]    Verify that all the values should be obtained automatically
    ...    when enabled AUTO for a connection associated with SUBNET
    [Tags]    1-nic    TC05

    Set Log Level    TRACE
    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    #${sp_tc03} is used as a generic json. Hence the deployment plan is being set with the same custom attributes in the below line.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    #Checking subnet of management NIC connection
    ${attributes} =  Create List  networkuri
    ${mgmt_nic} =    Get OS Attribute Values from Profile Response  ${sp_body}  ${attributes}
    Log    \n${mgmt_nic}
    ${subnet_uri} =  Get Subnet Uri of network  ${mgmt_nic[0]}
    Should Not Be Equal as Strings  ${subnet_uri}  None  msg=Nic connection should have subnet.

    # Create Server Profile with Auto option
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify profile body should have netmask, gateway, dns1, dns2 attributes
    Log    \nVerify profile body should have netmask, gateway, dns1, dns2 attributes    console=True
    ${resp_attributes} =    Create List    ipaddress    netmask    gateway    dns1    dns2
    ${resp_attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_response}    ${resp_attributes}
    list should not contain value    ${resp_attrib_values}    None    msg=All Custom attribute should be auto-filled after SP creation.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC09 Obtain NIC values when enabled USER-SPECIFIED option for a connection NOT associated with Subnet
    [Documentation]  Verify that all the values like ipv4 address, netmask & gateway
    ...    should be provided by user when enabled USER-SPECIFIED for a connection NOT associated with SUBNET
    [Tags]    1-nic  TC09

    ${sp_body} =    copy.deepcopy    ${sp_tc06}
    #${sp_tc06} is used as a generic json. Hence the deployment plan is being set with the same custom attributes in the below line.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.

    Log    \nVerify profile body should have netmask, gateway, dns1, dns2 attributes  console=True
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${resp_attributes} =    Create List    ipaddress    netmask    gateway    dns1    dns2
    ${resp_attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_response}    ${resp_attributes}
    list should not contain value    ${resp_attrib_values}    None    msg=All Custom attribute should be auto-filled after SP creation.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC10 SP creation fails when only IP address is provided for User-Specified option with No subnet associated
    [Documentation]    Verify that Sp creation fails when only ip address is provided by user and
    ...    enabled User-specified for a connection NOT associated with SUBNET
    [Tags]    1-nic    TC10

    ${sp_body} =    copy.deepcopy    ${sp_tc06}
    #${sp_tc06} is used as a generic json. Hence the deployment plan is being set with the same custom attributes in the below line.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${sp_body} =    Remove Network attributes except Ipaddress for osCutomAttributes    ${sp_body}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='False'  Fail  \nServer profile '${sp_body['name']}' created successfully which is unexpected

OVF1135_TC22 Obtain NIC values automatically when enabled Auto option for a connection associated with Subnet
    [Documentation]    Verify that all the values like ipv4 address, netmask & gateway should be obtained automatically
    ...    when enabled AUTO for a connection associated with SUBNET
    [Tags]    1-nic    TC22

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    #${sp_tc03} is used as a generic json. Hence the deployment plan is being set with the same custom attributes in the below line.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    # Checking subnet of management NIC connection
    ${attributes} =    Create List    networkuri
    ${mgmt_nic} =    Get OS Attribute Values from Profile Response    ${sp_body}    ${attributes}
    ${subnet_uri} =    Get Subnet Uri of network    ${mgmt_nic[0]}
    Should Not Be Equal as Strings    ${subnet_uri}    None    msg=Nic connection should have subnet.

    Log    \nVerify profile creation request body does not have netmask, gateway, dns1, dns2 attributes  console=True
    ${attributes} =  Create List  netmask  gateway  dns1  dns2
    ${Attrib_values} =  Get OS Attribute Values from Profile Response  ${sp_body}  ${attributes}
    should contain x times  ${Attrib_values}  None  4  msg=Custom attributes other than ip address should not be provided in SP body

    # Create Server Profile with Auto option
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  Failed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.

    Log    \nVerify profile body should have netmask, gateway, dns1, dns2 attributes  console=True
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${resp_attributes} =    Create List    ipaddress    netmask    gateway    dns1    dns2
    ${resp_attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_response}    ${resp_attributes}
    list should not contain value    ${resp_attrib_values}    None    msg=All Custom attribute should be auto-filled after SP creation.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC23 Verify that mgmt ip should be retained when changed the server hardware having different SHT when selected AUTO option
    [Documentation]    Verify that mgmt ip should be retained when changed the server hardware having different SHT when selected AUTO option
    [Tags]   1-nic    TC122

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

    ${sp_body} =    copy.deepcopy    ${sp_tc122}
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_dp}==${mngt_ip_after_changing_dp}    Log    \nProfile management IP not changed after changing the DP    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC24 Verify that mgmt ip should be retained when changed the SHT and make server hardware unassigned when selected AUTO option
    [Documentation]    Verify that mgmt ip should be retained when changed the SHT and make server hardware unassigned when selected AUTO option
    [Tags]    1-nic    TC123

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

    ${sp_body} =    copy.deepcopy    ${sp_tc122}
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    ${blnUnassignProf}=    Unassign I3S Server Profile    ${sp_body['name']}
    Should Be True    ${blnUnassignProf}    Failed to unassign server profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_dp}==${mngt_ip_after_changing_dp}    Log    \nProfile management IP not changed after changing the DP    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP changed after changing DP

OVF1135_TC25 Verify the USER-SPECIFIED option appears for a connection NOT associated with SUBNET when enabled both STATIC & DHCP in build plan
    [Documentation]    Verify the USER-SPECIFIED option appears
    ...    for a connection NOT associated with SUBNET when enabled both STATIC & DHCP in build plan
    [Tags]    1-nic    TC25

    ${sp_body} =    copy.deepcopy    ${sp_tc18}
    #${sp_tc018} is used as a generic json. Hence the deployment plan is being set with the same custom attributes in the below line.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    Log  \nVerify profile creation request body does not have netmask, gateway, dns1, dns2 attributes  console=True
    ${attributes} =  Create List  netmask  gateway  dns1  dns2
    ${Attrib_values} =  Get OS Attribute Values from Profile Response  ${sp_body}  ${attributes}
    list should not contain value    ${Attrib_values}    None    msg=All CA should be provided in Sp body

    # Create Server Profile with User-Specified option
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    Log    \nVerify profile body should have netmask, gateway, dns1, dns2 attributes  console=True
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${resp_attributes} =    Create List    ipaddress    netmask    gateway    dns1    dns2
    ${resp_attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_response}    ${resp_attributes}
    list should not contain value    ${resp_attrib_values}    None    msg=All Custom attribute should be auto-filled after SP creation.

OVF1135_TC27 Verify that mgmt ip should not be released when changed the server hardware having same SHT when selected AUTO option
    [Documentation]    Verify that mgmt ip should not be released when changed the server hardware having same SHT when selected AUTO option
    [Tags]    1-nic    TC121

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic

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

    ${sp_body} =    copy.deepcopy    ${sp_tc121}
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_dp}==${mngt_ip_after_changing_dp}    Log    \nProfile management IP not changed after changing the DP    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC28 Verify that SP creation should fail when selected AUTO option and provided only dns1 and not provided dns2
    [Documentation]    Verify that SP creation should fail when selected AUTO option and provided only dns1 and not provided dns2
    [Tags]    1-nic    TC120

    ${sp_body} =    copy.deepcopy    ${sp_tc120_master}
    Delete Server Profile    ${sp_body['name']}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nDNS values are not specified hence failed to create server profile  '${sp_body['name']}'
    ...    ELSE IF  '${blnCreateProf}'!='False'  Fail  \nServer Profile '${sp_body['name']}' created successfully which is unexpected    console=True

OVF1135_TC29 SP creation fails when selected NONE as a connection when NOT DISABLED NETWORK CONFIGURATION in NIC settings of build plan
    [Documentation]    Verify the SP creation fails with a validation error
    ...    when selected NONE as a connection when NOT DISABLED NETWORK CONFIGURATION in NIC settings of build plan.
    [Tags]    1-nic    TC29

    ${sp_body} =    copy.deepcopy    ${sp_tc19}
    #${sp_tc19} is used as a generic json and had the NIC attribute disabled. Hence the deployment plan is being set with the same custom attributes but different values.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='False'  Fail  \nServer profile '${sp_body['name']}' created successfully which is unexpected

OVF1135_TC30 SP creation is successful when selected NONE as a connection when DISABLED NETWORK CONFIGURATION in NIC settings of build plan
    [Documentation]    Verify the SP creation is successful when selected NONE as a connection
    ...    when DISABLED NETWORK CONFIGURATION in NIC settings of build plan.
    [Tags]    1-nic    TC30

    ${sp_body} =    copy.deepcopy    ${sp_tc19}
    #${sp_tc19} is used as a generic json. Hence the deployment plan is being set with the same custom attributes but different values.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_DisabledNWConfig
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should not be assigned.

OVF1135_TC31 Verify that SP creation should fail when selected AUTO option and not provided both dns1 and dns2
    [Documentation]    Verify that SP creation should fail when selected AUTO option and not provided both dns1 and dns2
    [Tags]    1-nic    TC119

    ${sp_body} =    copy.deepcopy    ${sp_tc119_master}
    Delete Server Profile    ${sp_body['name']}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nDNS values are not specified hence failed to create server profile  '${sp_body['name']}'
    ...    ELSE IF  '${blnCreateProf}'!='False'  Fail  \nServer Profile '${sp_body['name']}' created successfully which is unexpected    console=True

OVF1135_TC32 Verify the mgmt ip is released if deployment plan is removed when SP created with AUTO connection
    [Documentation]    Verify the mgmt ip is released if
    ...    deployment plan is removed when SP created with AUTO connection.
    [Tags]    1-nic    TC32

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    #${sp_tc03} is used as a generic json. Hence the deployment plan is being set with the same custom attributes but different values.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${attributes} =    Create List    networkuri
    ${mgmt_nic} =    Get OS Attribute Values from Profile Response    ${sp_body}    ${attributes}
    ${subnet_uri} =    Get Subnet Uri of network    ${mgmt_nic[0]}
    Should Not Be Equal as Strings    ${subnet_uri}    None    msg=Nic connection should have subnet.
    ${free_ips_before_sp} =    Get Available IP Count In Subnet Of Network    ${mgmt_nic[0]}

    # Create Server profile with Auto Option
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  Failed to create profile '${sp_body['name']}'

    ${free_ips_after_sp} =    Get Available IP Count In Subnet Of Network    ${mgmt_nic[0]}
    Should Not Be Equal as Strings    ${free_ips_before_sp}    ${free_ips_after_sp}    msg=Mgmt ip picked from pool and so free ip count decreased

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip[0]}

    # Edit Sp and remove osdp
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${sp_get_response} =    Get Server Profile    ${sp_body['name']}
    ${sp_uri}=  Get From Dictionary   ${sp_get_response}   uri
    ${sp_json_body} =    Change OSDP To None In SP Json Body    ${sp_get_response}
    ${Response}=    Fusion API Edit Server Profile    ${sp_json_body}    ${sp_uri}
    ${Retry Interval}    Convert To Number     30
    ${Retries}           Convert To Integer    30
    ${Response}=    Fusion API Wait For Task To Complete    ${Response['uri']}    sleep_time=${Retry Interval}    retries=${Retries}
    # Check for errors
    ${Errors}=    Get From Dictionary    ${Response}    taskErrors
    ${Errors_count}=    Get Length    ${Errors}
    Run Keyword If    ${Errors_count} == 0    Log to console    Succesfully updated server profile..
    ...    ELSE    Fail    msg=Errors encountered while updating Server Profile...\n${Errors}

    # check free ips after osdp delete
    ${free_ips_after_osdp_delete} =    Get Available IP Count In Subnet Of Network    ${mgmt_nic[0]}
    Should Be Equal as Strings    ${free_ips_before_sp}    ${free_ips_after_osdp_delete}    msg=mgmt ip released back to pool and so free ip count increased

OVF1135_TC33 Verify the mgmt ip is released if SP with AUTO option is deleted
    [Documentation]    Verify the mgmt ip is released if SP with AUTO option is deleted.
    [Tags]    1-nic    TC33

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    #${sp_tc03} is used as a generic json. Hence the deployment plan is being set with the same custom attributes but different values.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    #Checking subnet of management NIC connection
    ${attributes} =    Create List    networkuri
    ${mgmt_nic} =    Get OS Attribute Values from Profile Response    ${sp_body}    ${attributes}
    ${subnet_uri} =    Get Subnet Uri of network    ${mgmt_nic[0]}
    Should Not Be Equal as Strings    ${subnet_uri}    None    msg=Nic connection should have subnet.
    ${free_ips_before_sp} =    Get Available IP Count In Subnet Of Network    ${mgmt_nic[0]}

    # Create Server Profile
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  Failed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip[0]}

    # check free ips after sp create
    ${free_ips_after_sp} =    Get Available IP Count In Subnet Of Network    ${mgmt_nic[0]}
    Should Not Be Equal as Strings    ${free_ips_before_sp}    ${free_ips_after_sp}    msg=Mgmt ip picked from pool and so free ip count decreased

    # Delete Server Profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Delete Server Profile    ${sp_body['name']}

    ${free_ips_after_sp_delete} =    Get Available IP Count In Subnet Of Network    ${Mgmt_nic[0]}
    Should Be Equal as Strings    ${free_ips_before_sp}    ${free_ips_after_sp_delete}    msg=mgmt ip released back to pool and so free ip count increased

OVF1135_TC34 Verify whether the mgmt ip is assigned when created an unassigned server profile with deployment plan
    [Documentation]    Verify whether the mgmt ip is assigned
    ...    when created an unassigned server profile with deployment plan
    [Tags]    1-nic    TC34

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    #${sp_tc03} is used as a generic json. Hence the deployment plan is being set with the same custom attributes but different values.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    #Checking subnet of management NIC connection
    ${attributes} =    Create List    networkuri
    ${mgmt_nic} =    Get OS Attribute Values from Profile Response    ${sp_body}    ${attributes}
    ${subnet_uri} =    Get Subnet Uri of network    ${mgmt_nic[0]}
    Should Not Be Equal as Strings    ${subnet_uri}    None    msg=Nic connection should have subnet.

    # Create Server Profile Payload NIC when we have NIC attributes as it has additional connection
    Log    \nCreate Server Profile... '${sp_body['name']}'    console=True
    ${blnCreateProf}=  Create I3S unassigned Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  Failed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should not be assigned.

OVF1135_TC35 Verify that mgmt ip is NOT assigned when created an unassigned server profile without deployment plan
    [Documentation]    Verify that mgmt ip is NOT assigned
    ...    when created an unassigned server profile without deployment plan
    [Tags]    1-nic    TC35

    # Create Server Profile Payload
    ${sp_body} =    copy.deepcopy    ${sp_tc25}
    Delete Server Profile    ${sp_body['name']}

    Log    \nCreate Server Profile... '${sp_body['name']}'    console=True
    ${response}=  Add Server Profile  ${sp_body}
    ${blnCreateProf}=    Capture Task Status    ${response}    1200
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  Failed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address '${mngt_ip[0]}' assigned to unassigned profile.

OVF1135_TC36 Verify the ip count is same when Server Profile is created and deleted with User-Specified option
    [Documentation]    Create a SP with USER-SPECIFIED option, Verify the ip count is same when Server Profile is created and deleted.
    [Tags]    1-nic    TC36

    # Create Server Profile with User-Specified option
    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    #${sp_tc02} is used as a generic json. Hence the deployment plan is being set with the same custom attributes but different values.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${attributes} =  Create List  networkuri
    ${mgmt_nic} =    Get OS Attribute Values from Profile Response  ${sp_body}  ${attributes}
    ${subnet_uri} =  Get Subnet Uri of network  ${mgmt_nic[0]}
    Should Not Be Equal as Strings  ${subnet_uri}  None  msg=Nic connection should have subnet.
    ${free_subnet_ips_before_sp} =    Get Available IP Count In Subnet Of Network    ${mgmt_nic[0]}

    # check user provides only ip address attribute in server profile request body
    ${attribute} =    Create List    ipaddress
    ${Attrib_value} =    Get OS Attribute Values from Profile Response    ${sp_body}    ${attribute}
    Should Not Be Equal as Strings    ${Attrib_value[0]}    None    msg=ip address should be provided in Sp body

    # Create Server Profile
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip[0]}

    ${free_subnet_ips_after_sp} =    Get Available IP Count In Subnet Of Network    ${mgmt_nic[0]}
    Should Be Equal as Strings    ${free_subnet_ips_before_sp}    ${free_subnet_ips_after_sp}    msg=Mgmt ip should not be picked from pool and so free ip count remains same

    Log    \nVerify profile body should have netmask, gateway, dns1, dns2 attributes  console=True
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${resp_attributes} =    Create List    ipaddress    netmask    gateway    dns1    dns2
    ${resp_attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_response}    ${resp_attributes}
    list should not contain value    ${resp_attrib_values}    None    msg=All Custom attribute should be auto-filled after SP creation.

    # Delete Server Profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Delete Server Profile    ${sp_body['name']}

    ${free_subnet_ips_after_sp_delete} =    Get Available IP Count In Subnet Of Network    ${mgmt_nic[0]}
    Should Be Equal as Strings    ${free_subnet_ips_after_sp}    ${free_subnet_ips_after_sp_delete}    msg=Mgmt ip should not be picked from pool and so free ip count remains same

OVF1135_TC37 Verify whether the manually assigned ip can be re-used after the deletion of SP
    [Documentation]    Verify whether the manually assigned ip can be re-used after the deletion of SP
    [Tags]    1-nic    TC37

    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    # Create Server Profile
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.

    Delete Server Profile    ${sp_body['name']}

    ${sp2_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp2_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp2_body['name']}

    # Create Server Profile
    ${blnCreateProf}=  Create I3S Server Profile  ${sp2_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp2_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp2_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip2} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip2[0]}    None    msg=Mgmt ip address should be assigned.

    Should Be Equal as Strings     ${mngt_ip}    ${mngt_ip2}    msg=Profile has the same IP assigned

OVF1135_TC42 Verify that only ipv4 address should be provided by user when enabled USER-SPECIFIED for a connection associated with SUBNET but no IP POOLS
    [Documentation]    Verify that only ipv4 address should be provided by user when enabled USER-SPECIFIED for a connection
    ...    associated with SUBNET but no IP POOLS
    [Tags]    1-nic    TC42

    ${sp_body} =    copy.deepcopy    ${sp_tc41_1nic}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.

OVF1135_TC43 Verify the server profile creation fails when created SP with AUTO enabled for mgmt connection having no free ip's left in ip pools.
    [Documentation]    Verify the server profile creation fails
    ...    when created SP with AUTO enabled for mgmt connection having no free ip's left in ip pools.
    [Tags]    1-nic    TC43

    ${sp_body} =    copy.deepcopy    ${sp_tc43_1_nic}
    #${sp_tc43_1_nic} is used as a generic json. Hence the deployment plan is being set with the same custom attributes but different values.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='False'  Fail  \nNo free IP left'${sp_body['name']}'

OVF1135_TC44 Verify that the ip's are allocated from multiple ip pools under one subnet when created SP with AUTO enabled for mgmt connection
    [Documentation]    Verify that the ip's are allocated from multiple ip pools under one subnet
    ...    when created SP with AUTO enabled for mgmt connection.
    [Tags]    1-nic    TC44

    ${sp_body} =    copy.deepcopy    ${sp_tc29}
    #${sp_tc29} is used as a generic json. Hence the deployment plan is being set with the same custom attributes but different values.
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${blnUnassignProf}=    Unassign I3S Server Profile    ${sp_body['name']}
    Run Keyword If  '${blnUnassignProf}'=='True'  Log  \n...Server Profile '${sp_body['name']}' unassigned successfully    console=True
    ...    ELSE IF  '${blnUnassignProf}'!='True'  Fail  Failed to unassign server profile '${sp_body['name']}'

    ${sp2_body} =    copy.deepcopy    ${sp_tc29}
    Set To Dictionary    ${sp2_body}    name=sp2
    ${blnCreateProf}=  Create I3S Server Profile  ${sp2_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp2_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp2_body['name']}'

    Delete Server Profile    ${sp_body['name']}
    Delete Server Profile    ${sp2_body['name']}

OVF1135_TC45 Verify that the IPv4 subnet cannot be deleted when it was asociated with a connection inuse by profile
    [Documentation]    Verify that the IPv4 subnet cannot be deleted when it was asociated with a connection inuse by profile
    [Tags]    1-nic    TC45

    ${sp_body} =    copy.deepcopy    ${sp_tc28}
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

    ${subnets}=    Get Subnet    192.169.79.0
    ${uri}=    Get from Subnet        ${subnets}       uri
    ${blnDeleteProf} =    fusion_api_delete_ipv4_subnet        uri=${uri}

    Run Keyword If  '${blnDeleteProf}'=='False'  Log  \nServer Profile '${sp_body['name']}' subnet is in-use by a profile    console=True
    ...    ELSE IF  '${blnDeleteProf}'!='False'  Fail    deleted profile '${sp_body['name']}' successfully

OVF1135_TC46 Verify whether mgmt ip duplication error appears when used the same static ip for two server profiles
    [Documentation]    Verify whether mgmt ip duplication error appears when used the same static ip for two server profiles
    [Tags]    1-nic    TC118

    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp1_body} =    copy.deepcopy    ${sp_tc118}
    Set To Dictionary    ${sp1_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp1_body['name']}

    #the below test case Pass as there can be same IP's assigned to two different servers,we need to ping IPv4 and ensure that ping fails
    ${blnCreateProf1}=  Create I3S Server Profile  ${sp1_body}
    Run Keyword If  '${blnCreateProf1}'=='True'  Log  \nServer Profile '${sp1_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf1}'!='True'  Fail  \nA server profile already has the same IP address '${sp1_body['name']}'
    Delete Server Profile    ${sp1_body['name']}

OVF1135_TC48 Verify whether the IPv4 address range cannot be deleted when the ip's are used by server profiles
    [Documentation]    Verify whether the IPv4 address range cannot be deleted when the ip's are used by server profiles
    [Tags]    1-nic    TC48

    ${sp_body} =    copy.deepcopy    ${sp_tc28}
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
    # Ping Profile Management IP    ${mngt_ip[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    ${subnets}=    Get Subnet    192.169.78.0
    ${uri}=    Get from Subnet        ${subnets}       uri
    ${resp} =    fusion api get ipv4 subnet    uri=${uri}
    ${rangeuri} =     Get From Dictionary     ${resp}    rangeUris
    ${blnDeleteProf} =    fusion api delete ipv4 range    uri=${rangeuri[0]}

    Run Keyword If  '${blnDeleteProf}'=='False'  Log  \nServer Profile '${sp_body['name']}' range is in-use by a profile    console=True
    ...    ELSE IF  '${blnDeleteProf}'!='False'  Fail    deleted profile '${sp_body['name']}' successfully

OVF1135_TC49 Verify whether the server profile creation fails when tried to create SP with user specified option and assign ip address within the range
    [Documentation]    Verify whether the server profile creation fails
    ...    when tried to create SP with user specified option and assign ip address within the range
    [Tags]    1-nic    TC49

    ${sp_body} =    copy.deepcopy    ${sp_tc30}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nServer Profile '${sp_body['name']}' failed as per expected    console=True
    ...    ELSE IF  '${blnCreateProf}'!='False'  Fail  \Server profile '${sp_body['name']}' created successfully which is not expected

OVF1135_TC50 Verify whether the server profile creation fails when tried to create SP with user specified option, ip outside subnet
    [Documentation]    Verify whether the server profile creation fails when tried to create SP with user specified option, ip outside subnet
    [Tags]    1-nic    TC50

    ${sp_body} =    copy.deepcopy    ${sp_tc50_master}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
#    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nServer Profile '${sp_body['name']}' failed as per expected    console=True
    ...    ELSE IF  '${blnCreateProf}'!='False'  Fail  \Server profile '${sp_body['name']}' created successfully which is not expected

OVF1135_TC51 Verify whether the mgmt ip of SP is released and new ip is assigned when changed the NIC connection of existing server profile configured with AUTO option
    [Documentation]    Verify whether the mgmt ip of SP is released and new ip is assigned
    ...    when changed the NIC connection of existing server profile configured with AUTO option.
    [Tags]    1-nic    TC51

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

    ${sp2_body} =    copy.deepcopy    ${sp_tc03}
    Set To Dictionary    ${sp2_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    ${sp2_body} =    Change Nic Connection from profile    ${sp2_body}    private_nw2
    ${blnupdateProf}=    Edit I3S Server Profile  ${sp2_body}
    Run Keyword If  '${blnupdateProf}'=='True'  Log  \n...Server Profile '${sp2_body['name']}' NIC Connection updated successfully    console=True
    ...    ELSE IF  '${blnupdateProf}'!='True'  Fail  Failed to update NIC Connection server profile '${sp2_body['name']}'

    ${sp_response2} =    Get Server Profile    ${sp_body['name']}
    ${mngt_ip_after_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response2}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_nic[0]}    None    msg=Mgmt ip address should be assigned.
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    ${mngt_ip_after_changing_nic[0]}    msg=Profile '${sp_body['name']}' management ip '${mngt_ip_after_creating_sp[0]}' not changed to different IP after changing NIC connection

OVF1135_TC53 Verify whether the ip of SP is released, new ip is assigned when changed the NIC connection type from AUTO to User-specified
    [Documentation]    Verify whether the ip of SP is released, new ip is assigned when changed the NIC connection type
    ...    from AUTO to User-specified
    [Tags]    1-nic    TC53

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
    # Ping Profile Management IP    ${mngt_ip[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    ${sp_body} =    Update Profile request body with free Ipaddress    ${sp_body}    192.169.75.125

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
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing Nic

OVF1135_TC54 Verify whether ip of SP is released, no IP is assigned to SP when changed the AUTO NIC connection to NONE
    [Documentation]    Verify whether ip of SP is released, no IP is assigned to SP when changed the AUTO NIC connection to NONE
    [Tags]    1-nic    TC54

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

    #sp_tc19 contains the DP with NIC attribute set to NONE
    ${sp_body} =    copy.deepcopy    ${sp_tc19}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_DisabledNWConfig

    # Edit profile and change OSDP
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Be Equal as Strings    ${mngt_ip_after_changing_nic[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_nic}!=${mngt_ip_after_changing_nic}    Log    \nProfile management IP changed after changing the connection type    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_nic[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC55 Verify whether ip is assigned to SP when changed connection from NONE to NIC type AUTO
    [Documentation]    Verify whether ip is assigned to SP when changed connection from NONE to NIC type AUTO
    [Tags]    1-nic    TC55

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
    Should Be Equal as Strings    ${mngt_ip_before_changing_nic[0]}    None    msg=Mgmt ip address should not be assigned.

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

OVF1135_TC57 Verify whether ip is assigned to SP when changed connection from NONE to NIC connection of type User-specified
    [Documentation]    Verify whether ip is assigned to SP when changed connection from NONE to NIC connection of type User-specified
    [Tags]    1-nic    TC57

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

    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    ${sp_body} =    Update Profile request body with free Ipaddress    ${sp_body}    192.169.75.124

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

OVF1135_TC61 Verify whether ip of SP is released and new ip is assigned to SP when changed the NIC connection type from User-specified to AUTO
    [Documentation]    Verify whether ip of SP is released and new ip is assigned to SP when changed the NIC connection type
    ...    from User-specified to AUTO
    [Tags]    1-nic    TC61

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

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    #${sp_body} =    Update Profile request body with free Ipaddress    ${sp_body}    192.169.75.124

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

OVF1135_TC63 Verify whether ip of SP is released and no ip is assigned to SP when changed the User-specified NIC connection to NONE
    [Documentation]    Verify whether ip of SP is released and no ip is assigned to SP when changed the User-specified NIC connection to NONE
    [Tags]    1-nic    TC63

    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    ${sp_body} =    Update Profile request body with free Ipaddress    ${sp_body}    192.169.75.124
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

    ${sp_body} =    copy.deepcopy    ${sp_tc19}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_DisabledNWConfig

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

OVF1135_TC64 Verify ip of SP is released and user provided ip is assigned when replaced the AUTO nic connection with a connection which don't have subnet
    [Documentation]    Verify ip of SP is released and user provided ip is assigned when replaced the AUTO nic connection with a connection which don't have subnet
    [Tags]    1-nic    TC64

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

    ${sp_body} =    copy.deepcopy    ${sp_tc06}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    # ${sp_body} =    Update Profile request body with free Ipaddress    ${sp_body}    192.169.79.124

    # Edit profile and change OSDP
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_nic} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_nic[0]}    None    msg=Mgmt ip address should not be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_nic}!=${mngt_ip_after_changing_nic}    Log    \nProfile management IP changed after changing from Auto to User-specified option    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

OVF1135_TC92 SP is created successfully and mgmt ip is assigned and actual vlan id should be displayed when selected a tagged network from Netset to mgmt Nic in server profile page.
    [Documentation]    Verify that SP is created successfully and mgmt ip is assigned and actual vlan id should be displayed
    ...    when selected a tagged network from Netset to mgmt Nic in server profile page.
    [Tags]    1-nic    TC92

    ${sp_body} =    copy.deepcopy    ${sp_tc48}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
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
    # Ping Profile Management IP    ${mngt_ip[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC93 Verify that SP is created successfully and mgmt ip is assigned and check the vlan id displayed as zero when selected a untagged network from Netset to mgmt Nic in server profile page.
    [Documentation]    Verify that SP is created successfully and mgmt ip is assigned and check the vlan id displayed as zero
    ...    when selected a untagged network from Netset to mgmt Nic in server profile page.
    [Tags]    1-nic    TC93

    ${sp_body} =    copy.deepcopy    ${sp_tc49}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
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
    # Ping Profile Management IP    ${mngt_ip[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC96 Verify that mgmt ip should be retained when changed the server hardware to unassigned of same SHT when selected AUTO option
    [Documentation]    Verify that mgmt ip should be retained when changed the server hardware to unassigned of same SHT when selected AUTO option
    [Tags]    1-nic    TC96

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
    Sleep    50

    ${sp_body} =    copy.deepcopy    ${sp_tc124}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    ${blnUnassignProf}=    Unassign I3S Server Profile    ${sp_body['name']}
    Should Be True    ${blnUnassignProf}    Failed to unassign server profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_dp}==${mngt_ip_after_changing_dp}    Log    \nProfile management IP not changed after changing the DP    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC98 Verify whether mgmt ip is released and new ip is assigned when selected another network in the Network set to nic connection.
    [Documentation]    Verify whether mgmt ip is released and new ip is assigned when selected another network in the Network set to nic connection.
    [Tags]    1-nic    TC98

    ${sp_body} =    copy.deepcopy    ${sp_tc52}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should be assigned.

    ${sp2_body} =    copy.deepcopy    ${sp_tc52}
    ${sp2_body} =    Change Nic Connection from profile    ${sp2_body}    private_nw2
    ${blnupdateProf}=    Edit I3S Server Profile  ${sp2_body}
    Run Keyword If  '${blnupdateProf}'=='True'  Log  \n...Server Profile '${sp2_body['name']}' NIC Connection updated successfully    console=True
    ...    ELSE IF  '${blnupdateProf}'!='True'  Fail  Failed to update NIC Connection server profile '${sp2_body['name']}'

    ${sp_response1} =    Get Server Profile    ${sp_body['name']}
    ${mngt_ip_after_changing_nic_conn} =   Get OS Attribute Values from Profile Response    ${sp_response1}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_nic_conn[0]}    None    msg=Mgmt ip address should be assigned.
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    ${mngt_ip_after_changing_nic_conn[0]}    msg=Profile management ip '${mngt_ip_after_creating_sp[0]}' not changed after changing NIC connection

OVF1135_TC99 Verify that SP is updated successfully and mgmt ip is assigned when updated the NIC connection from NONE to Netset.
    [Documentation]    Verify that SP is updated successfully and mgmt ip is assigned when updated the NIC connection from NONE to Netset.
    [Tags]    1-nic    TC99

    ${sp_body} =    copy.deepcopy    ${sp_tc54}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNicAndDisableNWConfig
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should not be assigned.

    ${sp2_body} =    copy.deepcopy    ${sp_tc54}
    Remove from Dictionary    ${sp2_body['osDeploymentSettings']}    osCustomAttributes
    Set To Dictionary    ${sp2_body['osDeploymentSettings']}    osCustomAttributes=${sp_tc54_edit['osCustomAttributes']}
    ${blnupdateProf}=    Edit I3S Server Profile  ${sp2_body}
    Run Keyword If  '${blnupdateProf}'=='True'  Log  \n...Server Profile '${sp2_body['name']}' NIC Connection updated successfully    console=True
    ...    ELSE IF  '${blnupdateProf}'!='True'  Fail  Failed to update NIC Connection server profile '${sp2_body['name']}'

    ${sp_response1} =    Get Server Profile    ${sp_body['name']}
    ${mngt_ip_after_changing_nic_conn} =   Get OS Attribute Values from Profile Response    ${sp_response1}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_nic_conn[0]}    None    msg=Mgmt ip address should be assigned.
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    ${mngt_ip_after_changing_nic_conn[0]}    msg=Profile management ip '${mngt_ip_after_creating_sp[0]}' not changed after changing NIC connection

OVF1135_TC100 Verify that SP is updated successfully and mgmt ip is assigned when updated the NIC connection from NONE to Netset.
    [Documentation]    Verify that SP is updated successfully and mgmt ip is assigned when updated the NIC connection from NONE to Netset.
    [Tags]    1-nic    TC100

    ${sp_body} =    copy.deepcopy    ${sp_tc55}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNicAndDisableNWConfig
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should not be assigned.

    ${sp2_body} =    copy.deepcopy    ${sp_tc55}
    Set To Dictionary    ${sp2_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNicAndDisableNWConfig
    Remove from Dictionary    ${sp2_body['osDeploymentSettings']}    osCustomAttributes
    Set To Dictionary    ${sp2_body['osDeploymentSettings']}    osCustomAttributes=${sp_tc55_edit['osCustomAttributes']}
    ${blnupdateProf}=    Edit I3S Server Profile  ${sp2_body}
    Run Keyword If  '${blnupdateProf}'=='True'  Log  \n...Server Profile '${sp2_body['name']}' NIC Connection updated successfully    console=True
    ...    ELSE IF  '${blnupdateProf}'!='True'  Fail  Failed to update NIC Connection server profile '${sp2_body['name']}'

    ${sp_response1} =    Get Server Profile    ${sp_body['name']}
    ${mngt_ip_after_changing_nic_conn} =   Get OS Attribute Values from Profile Response    ${sp_response1}    ${attributes}
    Should Be Equal as Strings    ${mngt_ip_after_changing_nic_conn[0]}    None    msg=Mgmt ip address should be assigned.

OVF1135_TC101 Verify that SP is updated successfully and new mgmt ip is assigned when updated the nic connection from tagged network in Netset to individual mgmt network
    [Documentation]    Verify that SP is updated successfully and new mgmt ip is assigned
    ...    when updated the nic connection from tagged network in Netset to individual mgmt network.
    [Tags]    1-nic    TC101

    ${sp_body} =    copy.deepcopy    ${sp_tc55}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNicAndDisableNWConfig
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should not be assigned.

    ${sp2_body} =    copy.deepcopy    ${sp_tc55}
    Set To Dictionary    ${sp2_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNicAndDisableNWConfig
    Remove from Dictionary    ${sp2_body['osDeploymentSettings']}    osCustomAttributes
    Set To Dictionary    ${sp2_body['osDeploymentSettings']}    osCustomAttributes=${sp_tc56_edit['osCustomAttributes']}

    Remove from Dictionary    ${sp2_body}    connectionSettings
    Set To Dictionary    ${sp2_body}    connectionSettings=${sp_tc56_edit['connectionSettings']}

    ${blnupdateProf}=    Edit I3S Server Profile  ${sp2_body}
    Run Keyword If  '${blnupdateProf}'=='True'  Log  \n...Server Profile '${sp2_body['name']}' NIC Connection updated successfully    console=True
    ...    ELSE IF  '${blnupdateProf}'!='True'  Fail  Failed to update NIC Connection server profile '${sp2_body['name']}'

    ${sp_response1} =    Get Server Profile    ${sp_body['name']}
    ${mngt_ip_after_changing_nic_conn} =   Get OS Attribute Values from Profile Response    ${sp_response1}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    ${mngt_ip_after_changing_nic_conn[0]}    msg=Profile management ip '${mngt_ip_after_creating_sp[0]}' not changed after changing NIC connection

OVF1135_TC102 Verify that SP is updated successfully and new mgmt ip is assigned when updated the nic connection from untagged network in Netset to individual mgmt network.
    [Documentation]    Verify that SP is updated successfully and new mgmt ip is assigned
    ...    when updated the nic connection from untagged network in Netset to individual mgmt network.
    [Tags]    1-nic    TC102

    ${sp_body} =    copy.deepcopy    ${sp_tc49}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNicAndDisableNWConfig
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should not be assigned.

    ${sp2_body} =    copy.deepcopy    ${sp_tc49}
    Set To Dictionary    ${sp2_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNicAndDisableNWConfig
    Remove from Dictionary    ${sp2_body['osDeploymentSettings']}    osCustomAttributes
    Set To Dictionary    ${sp2_body['osDeploymentSettings']}    osCustomAttributes=${sp_tc56_edit['osCustomAttributes']}

    Remove from Dictionary    ${sp2_body}    connectionSettings
    Set To Dictionary    ${sp2_body}    connectionSettings=${sp_tc56_edit['connectionSettings']}

    ${blnupdateProf}=    Edit I3S Server Profile  ${sp2_body}
    Run Keyword If  '${blnupdateProf}'=='True'  Log  \n...Server Profile '${sp2_body['name']}' NIC Connection updated successfully    console=True
    ...    ELSE IF  '${blnupdateProf}'!='True'  Fail  Failed to update NIC Connection server profile '${sp2_body['name']}'

    ${sp_response1} =    Get Server Profile    ${sp_body['name']}
    ${mngt_ip_after_changing_nic_conn} =   Get OS Attribute Values from Profile Response    ${sp_response1}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    ${mngt_ip_after_changing_nic_conn[0]}    msg=Profile management ip '${mngt_ip_after_creating_sp[0]}' not changed after changing NIC connection

OVF1135_TC103 Verify whether user provided mgmt ip is released and new ip is assigned
    [Documentation]    Verify whether user provided mgmt ip is released and new ip is assigned
    ...    when changed the deployment plan from DP1 having USER-SPECIFIED option to DP2 having USER-SPECIFIED option.
    [Tags]    1-nic    TC113

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
    ${mngt_ip_before_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_before_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_before_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp2With1Nic_StaticAndDhcpNic
    ${sp_body} =    Update Profile request body with free Ipaddress    ${sp_body}    192.169.75.124

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
    Run Keyword If    ${mngt_ip_before_changing_dp}!=${mngt_ip_after_changing_dp}    Log    \nProfile management IP changed after changing DP    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC106 Verify that SP will show an error for connections missing when deleted the Network set which is selected as mgmt NIC connection of SP
    [Documentation]    Verify that SP will show an error for connections missing when deleted the Network set which is selected as mgmt NIC connection of SP
    [Tags]    1-nic    TC106

    ${sp_body} =    copy.deepcopy    ${sp_tc106_master}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    Fusion Api Delete Network Set    network_set5
    ${sp_response} =    Get Server Profile    ${sp_body['name']}

    Remove from Dictionary    ${sp_body}    connectionSettings
    Set To Dictionary    ${sp_body}    connectionSettings=${sp_tc106_edit['connectionSettings']}

    #${osdp} =    Get From Dictionary    ${sp_body}    osDeploymentSettings
    Remove from Dictionary    ${sp_body}    osDeploymentSettings
    Set To Dictionary    ${sp_body}    osDeploymentSettings=${sp_tc106_edit['osDeploymentSettings']}

    Remove from Dictionary    ${sp_body}    connectionSettings
    Set To Dictionary    ${sp_body}    connectionSettings=${sp_tc106_edit['connectionSettings']}

    # ${sp2_body} =    copy.deepcopy    ${sp_tc106_edit}
    ${blnupdateProf}=    Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnupdateProf}'=='False'  Log  \n...Server Profile '${sp_body['name']}' NIC Connection not updated successfully    console=True
    ...    ELSE IF  '${blnupdateProf}'!='False'  Fail  Pass to update NIC Connection server profile '${sp2_body['name']}'

OVF1135_TC107 Verify the Vlan id of SP is updated when changed the tagged network as untagged in Netset
    [Documentation]    Verify the Vlan id of SP is updated when changed the tagged network as untagged in Netset
    [Tags]    1-nic    TC107

    ${sp_body} =    copy.deepcopy    ${sp_tc52}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should not be assigned.

    ${sp2_body} =    copy.deepcopy    ${sp_tc107_edit}
    ${blnupdateProf}=    Edit I3S Server Profile  ${sp2_body}
    Run Keyword If  '${blnupdateProf}'=='True'  Log  \n...Server Profile '${sp2_body['name']}' NIC Connection updated successfully    console=True
    ...    ELSE IF  '${blnupdateProf}'!='True'  Fail  Failed to update NIC Connection server profile '${sp2_body['name']}'

    ${sp_response1} =    Get Server Profile    ${sp_body['name']}
    ${mngt_ip_after_changing_nic_conn} =   Get OS Attribute Values from Profile Response    ${sp_response1}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    ${mngt_ip_after_changing_nic_conn[0]}    msg=Profile management ip '${mngt_ip_after_creating_sp[0]}' not changed after changing NIC connection

OVF1135_TC108 Verify that SP is updated successfully and all vlan ids are properly reflected on host when changed the NIC connection from one Netset to another Netset.
    [Documentation]    Verify that SP is updated successfully and all vlan ids are properly reflected on host
    ...    when changed the NIC connection from one Netset to another Netset.
    [Tags]    1-nic    TC108

    ${sp_body} =    copy.deepcopy    ${sp_tc52}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_creating_sp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    None    msg=Mgmt ip address should not be assigned.

    ${sp2_body} =    copy.deepcopy    ${sp_tc63_edit}
    ${blnupdateProf}=    Edit I3S Server Profile  ${sp2_body}
    Run Keyword If  '${blnupdateProf}'=='True'  Log  \n...Server Profile '${sp2_body['name']}' NIC Connection updated successfully    console=True
    ...    ELSE IF  '${blnupdateProf}'!='True'  Fail  Failed to update NIC Connection server profile '${sp2_body['name']}'

    ${sp_response1} =    Get Server Profile    ${sp_body['name']}
    ${mngt_ip_after_changing_nic_conn} =   Get OS Attribute Values from Profile Response    ${sp_response1}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    ${mngt_ip_after_changing_nic_conn[0]}    msg=Profile management ip '${mngt_ip_after_creating_sp[0]}' not changed after changing NIC connection

OVF1135_TC109 Verify whether mgmt ip is released and new ip is assigned when changed the deployment plan from DP1 having AUTO option to DP2 having AUTO option.
    [Documentation]    Verify whether mgmt ip is released and new ip is assigned
    ...    when changed the deployment plan from DP1 having AUTO option to DP2 having AUTO option.
    [Tags]    1-nic    TC109

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    Set to Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    #Get the mgmt ip address
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_before_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    # Edit profile and change OSDP
    Set to Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp2With1Nic_StaticAndDhcpNic
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

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

OVF1135_TC110 Verify whether mgmt ip is released and user provided ip is assigned when changed the deployment plan from DP1 having AUTO option to DP2 having USER-SPECIFIED option
    [Documentation]    Verify whether mgmt ip is released and user provided ip is assigned when changed the deployment plan from DP1 having AUTO option to DP2 having USER-SPECIFIED option
    [Tags]    1-nic    TC110

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
    ${mngt_ip_before_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_before_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_before_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp2With1Nic_StaticAndDhcpNic
    ${sp_body} =    Update Profile request body with free Ipaddress    ${sp_body}    192.169.75.124

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
    Run Keyword If    ${mngt_ip_before_changing_dp}!=${mngt_ip_after_changing_dp}    Log    \nProfile management IP changed after changing DP    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10

OVF1135_TC112 Verify whether user provided mgmt ip is released and new ip from pool is assigned when changed the deployment plan from DP1 having USER-SPECIFIED option to DP2 having AUTO option
    [Documentation]    Verify whether user provided mgmt ip is released and new ip from pool is assigned when changed the deployment plan from DP1 having USER-SPECIFIED option to DP2 having AUTO option
    [Tags]    1-nic    TC112

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

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
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

    # Verify whether Profile management IP changed after changing DP when changed the deployment plan from DP1 having USER-SPECIFIED option to DP2 having USER-SPECIFIED option.
    Run Keyword If    ${mngt_ip_before_changing_dp}!=${mngt_ip_after_changing_dp}    Log    \nProfile management IP changed after changing the connection type    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

    Power On Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10
    # Ping Profile Management IP    ${mngt_ip_after_changing_dp[0]}
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Sleep    10