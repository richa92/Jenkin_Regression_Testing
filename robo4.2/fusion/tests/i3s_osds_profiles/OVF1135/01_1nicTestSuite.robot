*** Settings ***
Documentation     i3S  - Lifecycle - OS Deployment supports IP pools for NIC settings
Resource          resource.robot

Suite Setup        Login To Appliance And Verify Oneview Prerequisites    ${fusion_ip}    ${admin_credentials}
Suite Teardown     I3S Suite Teardown
Test Setup         I3S Test Setup

*** Test Cases ***
OVTC53051
    [Documentation]    Verify that only ipv4 address should be provided by user
    ...    when enabled USER-SPECIFIED for a connection associated with SUBNET.
    [Tags]    1-nic    OVF1135_TC02

    # Create Server Profile with User-Specified option...
    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

    # Verify profile body should have netmask, gateway, dns1, dns2 attributes
    Log    \nVerify profile body should have netmask, gateway, dns1, dns2 attributes    console=True
    ${resp_attributes} =    Create List    ipaddress    netmask    gateway    dns1    dns2
    ${resp_attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_response}    ${resp_attributes}
    list should not contain value    ${resp_attrib_values}    None    msg=All Custom attribute should be auto-filled after SP creation.

OVTC53052
    [Documentation]    Verify that all the values should be obtained automatically
    ...    when enabled AUTO for a connection associated with SUBNET.
    [Tags]    1-nic    OVF1135_TC03

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    #Checking subnet of management NIC connection
    ${attributes} =  Create List  networkuri
    ${mgmt_nic} =    Get OS Attribute Values from Profile Response  ${sp_body}  ${attributes}
    ${subnet_uri} =  Get Subnet Uri of network  ${mgmt_nic[0]}
    Should Not Be Equal as Strings  ${subnet_uri}  None  msg=Nic connection should have subnet.

    # Create Server Profile with Auto option...
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

    # Verify profile body should have netmask, gateway, dns1, dns2 attributes
    Log    \nVerify profile body should have netmask, gateway, dns1, dns2 attributes    console=True
    ${resp_attributes} =    Create List    ipaddress    netmask    gateway    dns1    dns2
    ${resp_attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_response}    ${resp_attributes}
    list should not contain value    ${resp_attrib_values}    None    msg=All Custom attribute should be auto-filled after SP creation.

OVTC53055
    [Documentation]  Verify that all the values like ipv4 address, netmask & gateway
    ...    should be provided by user when enabled USER-SPECIFIED for a connection NOT associated with SUBNET.
    [Tags]    1-nic  TC06    OVF1135_TC06

    ${sp_body} =    copy.deepcopy    ${sp_tc06}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

    Log    \nVerify profile body should have netmask, gateway, dns1, dns2 attributes  console=True
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${resp_attributes} =    Create List    ipaddress    netmask    gateway    dns1    dns2
    ${resp_attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_response}    ${resp_attributes}
    list should not contain value    ${resp_attrib_values}    None    msg=All Custom attribute should be auto-filled after SP creation.

OVTC53056
    [Documentation]    Verify that Sp creation fails when only ip address is provided by user and
    ...    enabled User-specified for a connection NOT associated with SUBNET.
    [Tags]    1-nic    OVF1135_TC07

    ${sp_body} =    copy.deepcopy    ${sp_tc06}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${sp_body} =    Remove Network attributes except Ipaddress for osCutomAttributes    ${sp_body}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='False'  Fail  \nServer profile '${sp_body['name']}' created successfully which is unexpected

OVTC53058
    [Documentation]    Verify that all the values are obtained
    ...    from DHCP server when enabled DHCP for a connection associated with SUBNET.
    [Tags]    1-nic    OVF1135_TC09

    ${sp_body} =    copy.deepcopy    ${sp_tc09}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_DhcpNic
    Delete Server Profile    ${sp_body['name']}

    # Create Server Profile with User-Specified option
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  Failed to create server profile '${sp_body['name']}' which is unexpected

OVTC53061
    [Documentation]  Verify that all the values are obtained
    ...    from DHCP server when enabled DHCP for a connection NOT associated with SUBNET.
    [Tags]    1-nic    OVF1135_TC12

    ${sp_body} =    copy.deepcopy    ${sp_tc12}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_DhcpNic
    Delete Server Profile    ${sp_body['name']}

    # check that user should not provide ipaddress, netmask, gateway, dns1, dns2 attributes in SP body
    ${attributes} =    Create List    ipaddress    netmask    gateway    dns1    dns2
    ${attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_body}    ${attributes}
    should contain x times    ${attrib_values}    None    5    msg=Custom attributes should not be provided in SP body

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

OVTC53063
    [Documentation]    Verify that all the values like ipv4 address, netmask & gateway should be obtained automatically
    ...    when enabled AUTO for a connection associated with SUBNET.
    [Tags]    1-nic    OVF1135_TC14

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
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

    # Create Server Profile with User-Specified option
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  Failed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

    Log    \nVerify profile body should have netmask, gateway, dns1, dns2 attributes  console=True
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${resp_attributes} =    Create List    ipaddress    netmask    gateway    dns1    dns2
    ${resp_attrib_values} =    Get OS Attribute Values from Profile Response    ${sp_response}    ${resp_attributes}
    list should not contain value    ${resp_attrib_values}    None    msg=All Custom attribute should be auto-filled after SP creation.

OVTC53064
    [Documentation]    Verify that all the values are obtained from DHCP server
    ...    when enabled DHCP for a connection associated with SUBNET.
    [Tags]    1-nic    OVF1135_TC15

    ${sp_body} =    copy.deepcopy    ${sp_tc09}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    # Create Server Profile with User-Specified option
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

OVTC53066
    [Documentation]    Verify the DHCP option appears for a connection NOT associated with SUBNET
    ...    when enabled both STATIC & DHCP in NIC settings of build plan.
    [Tags]    1-nic    OVF1135_TC17

    ${sp_body} =    copy.deepcopy    ${sp_tc17}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    # Create Server Profile with User-Specified option
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

OVTC53067
    [Documentation]    Verify the USER-SPECIFIED option appears
    ...    for a connection NOT associated with SUBNET when enabled both STATIC & DHCP in build plan
    [Tags]    1-nic    OVF1135_TC18

    ${sp_body} =    copy.deepcopy    ${sp_tc18}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    # ${free_pool_ip} =    Get Free IP From Subnet IP Pool    ${ip_pool}
    # Log    \nUpdating profile request body with free IP '${free_pool_ip}'   console=True
    # ${sp_body} =    Update Profile request body with free Ipaddress    ${sp_body}    ${free_pool_ip}

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

OVTC53068
    [Documentation]    Verify the SP creation fails with a validation error
    ...    when selected NONE as a connection when NOT DISABLED NETWORK CONFIGURATION in NIC settings of build plan.
    [Tags]    1-nic    OVF1135_TC19

    ${sp_body} =    copy.deepcopy    ${sp_tc19}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='False'  Fail  \nServer profile '${sp_body['name']}' created successfully which is unexpected

OVTC53069
    [Documentation]    Verify the SP creation is successful when selected NONE as a connection
    ...    when DISABLED NETWORK CONFIGURATION in NIC settings of build plan.
    [Tags]    1-nic    OVF1135_TC20

    ${sp_body} =    copy.deepcopy    ${sp_tc19}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_DisabledNWConfig
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should not be assigned.

OVTC53071
    [Documentation]    Verify the mgmt ip is released if
    ...    deployment plan is removed in SP created with AUTO connection.
    [Tags]    1-nic    OVF1135_TC22

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
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
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
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

OVTC53072
    [Documentation]    Verify the mgmt ip is released if SP with AUTO option is deleted.
    [Tags]    1-nic    OVF1135_TC23

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
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

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

    # check free ips after sp create
    ${free_ips_after_sp} =    Get Available IP Count In Subnet Of Network    ${mgmt_nic[0]}
    Should Not Be Equal as Strings    ${free_ips_before_sp}    ${free_ips_after_sp}    msg=Mgmt ip picked from pool and so free ip count decreased

    # Delete Server Profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    Delete Server Profile    ${sp_body['name']}

    ${free_ips_after_sp_delete} =    Get Available IP Count In Subnet Of Network    ${Mgmt_nic[0]}
    Should Be Equal as Strings    ${free_ips_before_sp}    ${free_ips_after_sp_delete}    msg=mgmt ip released back to pool and so free ip count increased

OVTC53073
    [Documentation]    Verify whether the mgmt ip is assigned
    ...    when created an unassigned server profile with deployment plan
    [Tags]    1-nic    OVF1135_TC24

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
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
    Should Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.

OVTC53074
    [Documentation]    Verify that mgmt ip is not assigned
    ...    when created an unassigned server profile without deployment plan
    [Tags]    1-nic    OVF1135_TC25

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

OVTC53075
    [Documentation]    Create a SP with USER-SPECIFIED option.
    ...    Verify the ip count is same when Server Profile is created and deleted.
    [Tags]    1-nic    OVF1135_TC26

    # Create Server Profile with User-Specified option...
    ${sp_body} =    copy.deepcopy    ${sp_tc02}
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

    # Ping Profile management IP
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
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

OVTC53077
    [Documentation]    Verify the server profile creation fails
    ...    when created SP with AUTO enabled for mgmt connection having no free ip's left in ip pools.
    [Tags]    1-nic    OVF1135_TC28

    ${sp_body} =    copy.deepcopy    ${sp_tc28}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    ${blnUnassignProf}=    Unassign I3S Server Profile    ${sp_body['name']}
    Run Keyword If  '${blnUnassignProf}'!='True'  Fail  Failed to unassign server profile '${sp_body['name']}'

    ${sp2_body} =    copy.deepcopy    ${sp_tc28}
    Set To Dictionary    ${sp2_body}    name=sp2
    ${blnCreateProf}=  Create I3S Server Profile  ${sp2_body}
    Run Keyword If  '${blnCreateProf}'!='False'  Fail  \nServer profile '${sp2_body['name']}' created successfully which is unexpected

OVTC53078
    [Documentation]    Verify that the ip's are allocated from multiple ip pools under one subnet
    ...    when created SP with AUTO enabled for mgmt connection.
    [Tags]    1-nic    OVF1135_TC29

    ${sp_body} =    copy.deepcopy    ${sp_tc29}
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

OVTC53079
    [Documentation]    Verify whether the server profile creation fails
    ...    when tried to create SP with user specified option and assign ip address within the range
    [Tags]    1-nic    OVF1135_TC30

    ${sp_body} =    copy.deepcopy    ${sp_tc30}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpWith1Nic_StaticNic
    Delete Server Profile    ${sp_body['name']}

    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='False'  Log  \nServer Profile '${sp_body['name']}' failed as per expected    console=True
    ...    ELSE IF  '${blnCreateProf}'!='False'  Fail  \Server profile '${sp_body['name']}' created successfully which is not expected

OVTC53080
    [Documentation]    Verify whether the mgmt ip of SP is released and new ip is assigned
    ...    when changed the NIC connection of existing server profile configured with AUTO option.
    [Tags]    1-nic    OVF1135_TC31

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
    ${mngt_ip_after_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response2}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.

    Should Not Be Equal as Strings    ${mngt_ip_after_creating_sp[0]}    ${mngt_ip_after_changing_dp[0]}    msg=Profile '${sp_body['name']}' management ip '${mngt_ip_after_creating_sp[0]}' not changed to different IP after changing NIC connection

OVTC53093
    [Documentation]    Verify that SP is created successfully and mgmt ip is assigned and actual vlan id should be displayed
    ...    when selected a tagged network from Netset to mgmt Nic in server profile page.
    [Tags]    1-nic    OVF1135_TC48

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

OVTC53094
    [Documentation]    Verify that SP is created successfully and mgmt ip is assigned and check the vlan id displayed as zero
    ...    when selected a untagged network from Netset to mgmt Nic in server profile page.
    [Tags]    1-nic    OVF1135_TC49

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

OVTC53097
    [Documentation]    Verify whether mgmt ip is released and new ip is assigned when selected another network in the Network set to nic connection.
    [Tags]    1-nic    OVF1135_TC53

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

OVTC53098
    [Documentation]    Verify that SP is updated successfully and mgmt ip is assigned when updated the NIC connection from NONE to Netset.
    [Tags]    1-nic    OVF1135_TC54

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

OVTC53099
    [Documentation]    Verify that SP is updated successfully and mgmt ip is released when updated the NIC connection from Netset to NONE.
    [Tags]    1-nic    OVF1135_TC55

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

OVTC53100
    [Documentation]    Verify that SP is updated successfully and new mgmt ip is assigned
    ...    when updated the nic connection from tagged network in Netset to individual mgmt network.
    [Tags]    1-nic    OVF1135_TC56

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

OVTC53101
    [Documentation]    Verify that SP is updated successfully and new mgmt ip is assigned
    ...    when updated the nic connection from untagged network in Netset to individual mgmt network.
    [Tags]    1-nic    OVF1135_TC57

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

OVTC53107
    [Documentation]    Verify that SP is updated successfully and all vlan ids are properly reflected on host
    ...    when changed the NIC connection from one Netset to another Netset.
    [Tags]    1-nic    OVF1135_TC63

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

OVTC53108
    [Documentation]    Verify whether mgmt ip is released and new ip is assigned
    ...    when changed the deployment plan from DP1 having AUTO option to DP2 having AUTO option.
    [Tags]    1-nic    OVF1135_TC64

    ${sp_body} =    copy.deepcopy    ${sp_tc03}
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    Set to Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    # Ping Profile Management IP
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_before_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip_before_changing_dp[0]}

    # Edit profile and change OSDP
    Set to Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp2With1Nic_StaticAndDhcpNic
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    # Ping Profile Management IP
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip_after_changing_dp[0]}

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_dp}!=${mngt_ip_after_changing_dp}    Log    \nProfile management IP changed after changing DP    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

OVTC53109
    [Documentation]    Verify whether user provided mgmt ip is released and new ip is assigned
    ...    when changed the deployment plan from DP1 having USER-SPECIFIED option to DP2 having USER-SPECIFIED option.
    [Tags]    1-nic    OVF1135_TC65

    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    Power Off Profile Server    ${sp_body['serverHardwareUri']}
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    # Ping Profile Management IP
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_before_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip_before_changing_dp[0]}

    ${sp_body} =    copy.deepcopy    ${sp_tc02}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp2With1Nic_StaticAndDhcpNic
    ${sp_body} =    Update Profile request body with free Ipaddress    ${sp_body}    192.169.75.124

    # Edit profile and change OSDP
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DP    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    # Ping Profile Management IP
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip_after_changing_dp[0]}

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_dp}!=${mngt_ip_after_changing_dp}    Log    \nProfile management IP changed after changing DP    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP

OVTC53110
    [Documentation]    Verify whether mgmt ip is released and new ip is assigned
    ...    when changed the deployment plan from DP1 having DHCP option to DP2 having DHCP option.
    [Tags]    1-nic    OVF1135_TC66

    ${sp_body} =    copy.deepcopy    ${sp_tc66}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp1With1Nic_StaticAndDhcpNic
    Delete Server Profile    ${sp_body['name']}

    # Create server profile
    ${blnCreateProf}=  Create I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnCreateProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' created successfully    console=True
    ...    ELSE IF  '${blnCreateProf}'!='True'  Fail  \nFailed to create profile '${sp_body['name']}'

    # Ping Profile Management IP
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_before_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_before_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip_before_changing_dp[0]}

    # Edit profile and change OSDP
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dp2With1Nic_StaticAndDhcpNic
    ${blnEditProf}=  Edit I3S Server Profile  ${sp_body}
    Run Keyword If  '${blnEditProf}'=='True'  Log  \nServer Profile '${sp_body['name']}' updated successfully with different DO    console=True
    ...    ELSE IF  '${blnEditProf}'!='True'  Fail    Failed to update profile '${sp_body['name']}' with different DP

    # Ping Profile Management IP
    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip_after_changing_dp} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip_after_changing_dp[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip_after_changing_dp[0]}

    # Verify whether Profile management IP changed after changing DP
    Run Keyword If    ${mngt_ip_before_changing_dp}!=${mngt_ip_after_changing_dp}    Log    \nProfile management IP changed after changing DP    console=True
    ...    ELSE    Fail    msg=ERROR: Profile management IP not changed after changing DP
