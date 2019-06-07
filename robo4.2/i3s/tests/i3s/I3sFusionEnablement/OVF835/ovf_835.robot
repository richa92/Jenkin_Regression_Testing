*** Settings ***
Documentation     OVF835: i3S - Artifact - Improved Server Profile and artifact UX for configuration of NIC teaming

Resource          resource.robot
Test Setup        Login To Appliance And Verify Oneview Prerequisites    ${fusion_ip}    ${serveradmin}
Test Teardown     I3S Suite Teardown


*** Test Cases ***
OVF835_TC01
    [Documentation]    As a Server Administrator,
    ...    I want to deploy a server profile that contains 4 NIC ports out which two of them are teamed.
    [Tags]    TC01

    ${sp_body} =    copy.deepcopy    ${tc01_sp}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

OVF835_TC02
    [Documentation]    As a Server Administrator,
    ...    I want to create a server profile that contains 4 NIC ports. Two ports of the same NIC are teamed.
    [Tags]    TC02

    ${sp_body} =    copy.deepcopy    ${tc02_sp}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'=='True'    Fail    Server profile created profile '${sp_body['name']}' successfully which is not expected

OVF835_TC03
    [Documentation]    As a Server Administrator,
    ...    I want to create a server profile with network ports teamed with one port configured and the other set to None
    [Tags]    TC03

    ${sp_body} =    copy.deepcopy    ${tc03_sp}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

OVF835_TC04
    [Documentation]    As a Server Administrator,
    ...    I want to reuse a Deployment plan having NICs bonded but set their connection to None during server profile creation.
    [Tags]    TC04

    ${sp_body} =    copy.deepcopy    ${tc04_sp}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

OVF835_TC05
    [Documentation]    As a Server Administrator,
    ...    I want to create a server profile with the network ports teamed. They are configured for reciving DHCP IPv4 addresses.
    [Tags]    TC05

    ${sp_body} =    copy.deepcopy    ${tc05_sp}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

OVF835_TC06
    [Documentation]    As a Server Administrator,
    ...    I want to create a server profile with the network ports teamed. The networks are set to Auto
    [Tags]    TC06

    ${sp_body} =    copy.deepcopy    ${tc01_sp}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpNicTeaming_StaticAndDhcp
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

OVF835_TC07
    [Documentation]    As a Server Administrator,
    ...    I want to create a server profile with the network ports teamed. The IPv4 address is provided by the user
    [Tags]    TC07

    ${sp_body} =    copy.deepcopy    ${tc01_sp}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

OVF835_TC10
    [Documentation]    As a Server Administrator,
    ...    I want to enable FlexNIC functions for the NIC adapters and team two FlexNICs of different NICs.
    [Tags]    TC10

    ${sp_body} =    copy.deepcopy    ${tc10_sp}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

OVF835_TC11
    [Documentation]    As a server administrator,
    ...    I would like to deploy a server profile using a deployment plan that uses active-active NIC bonding
    ...    with each NIC port having a different IP address. (multiple paths)
    [Tags]    TC11

    ${sp_body} =    copy.deepcopy    ${tc07_sp}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

OVF835_TC12
    [Documentation]    As a server administrator,
    ...    I would like to reuse the deployment plan that holds active-active NIC bonding however,
    ...    only one NIC will be assigned an IP address
    [Tags]    TC12

    ${sp_body} =    copy.deepcopy    ${tc03_sp}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpNicTeaming_StaticDhcpAndNoNwTeaming
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

OVF835_TC13
    [Documentation]    As a server administrator,
    ...    I would like to reuse the deployment plan that holds active-active NIC bonding however,
    ...    only one NIC will be assigned an IP address. (Allow no network teaming is not enabled.)
    [Tags]    TC13

    ${sp_body} =    copy.deepcopy    ${tc03_sp}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpNicTeaming_StaticAndDhcp
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'=='True'    Fail    Server profile created profile '${sp_body['name']}' successfully which is not expected

OVF835_TC14
    [Documentation]    As a server administrator,
    ...    I need to deploy a server with highly available management, vmotion and data ports
    [Tags]    TC14

    ${sp_body} =    copy.deepcopy    ${tc01_sp}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpNicTeaming_StaticAndDhcp
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}

OVF835_TC20
    [Documentation]    As a server administrator,
    ...    I would like to create a server profile template from an existing server profile that uses NIC teaming for the guest network
    [Tags]    TC20

    ${sp_body} =    copy.deepcopy    ${tc01_sp}
    Set To Dictionary    ${sp_body['osDeploymentSettings']}    osDeploymentPlanUri=dpNicTeaming_StaticAndDhcp
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    ${resp} =    Create Server Profile Template from Profile    ${sp_body}    ovf835_spt
    ${blnStatus} =    Capture Task Status    ${resp}
    Run Keyword If    '${blnStatus}'!='True'    Fail    Failed to create SPT 'ovf835_spt' from SP "${sp_body['name']}"

    Remove SPT And Server Profiles by SPT    ovf835_spt

OVF835_TC25
    [Documentation]    As a server administrator,
    ...    I need to deploy a server profile that requires the management network (single port) and a network port team to be on DHCP
    [Tags]    TC25

    ${sp_body} =    copy.deepcopy    ${tc25_sp}
    ${blnCreateProf}=    Create I3S Server Profile    ${sp_body}
    Run Keyword If    '${blnCreateProf}'!='True'    Fail    Failed to create profile '${sp_body['name']}'

    ${os_vol}=    Get OS Volume From Server Profile    ${sp_body['name']}
    Should not be equal as strings    '${os_vol}'    'None'    msg=OS volume should be assigned to server profile '${sp_body['name']}'

    ${sp_response} =    Get Server Profile    ${sp_body['name']}
    ${attributes} =  Create List    ipaddress
    ${mngt_ip} =   Get OS Attribute Values from Profile Response    ${sp_response}    ${attributes}
    Should Not Be Equal as Strings    ${mngt_ip[0]}    None    msg=Mgmt ip address should be assigned.
    # Power On Profile Server    ${sp_body['serverHardwareUri']}
    # Ping Profile Management IP    ${mngt_ip[0]}
