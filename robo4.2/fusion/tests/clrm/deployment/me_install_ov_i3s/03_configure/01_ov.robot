*** Settings ***
Documentation    I3S Enablement Prerequisites
...              Usage =
...              cmdline: pybot -d ../logs  --timestampoutputs -t <target test case> <target test file>
...              Workflows:
...              pybot -v fusion_api_resource:"C:/new_src/fusion/Resources/api/fusion_api_resource.txt"
...              "C:\new_src\i3s\tests\i3s\I3sFusionEnablement\prerequisites\ov_prerequisites.robot"

Resource         ../resource.robot
Suite Setup      Login to Fusion Via REST    ${fusion_ip}    ${admin_credentials}


*** Test Cases ***
Do hardware setup
    [Documentation]    Do hardware setup
    [Tags]    critical    MAT    HW-SETUP    TC14
    Invoke Hardware Setup    timeout=300    interval=20
    Sleep    1000s
    Wait Until Keyword Succeeds    15min    50sec    All Enclosures Status Should Be OK or Warning

Add License to the appliance
    [Documentation]    Add license to the appliance
    [Tags]    LICENSES
    Add Licenses from variable    ${newLicenses}

Create Ethernet Networks and Associate Subnet Pools
    [Documentation]    Add IPV4 Subnet and Add Address Range
    ...                Create Ethernet Networks With Subnet ID
    [Tags]    P0    ADD-ETHERNET    OV-SETUP

    :FOR    ${ethernet}    IN    @{ethernets}
    \    ${dns_status}=    Run keyword and return status    Dictionary Should Contain Key   ${ethernet}     dnsServers
    \    ${subnetUri}=    Run Keyword If    ${dns_status}!=False    Create Fusion IPv4 SubnetV4    ${ethernet}
    \    ${status}=    Run keyword and return status    Dictionary Should Contain Key   ${ethernet}     ranges
    \    Run Keyword If    ${status}!=False    Create Fusion IPv4 Pools    ${subnetUri}    @{ethernet['ranges']}
    \    Create Fusion Ethernet Network V4    ${ethernet}    ${subnetUri}

Create Fusion Fc Networks
    [Documentation]    Creates the required networks based on the list
    [Tags]    P0    ADD-FC    OV-SETUP

    ${responses}=  Add Non Existing FC Networks  ${fc_networks}
    #Run Keyword for List  ${responses}  Wait For Task2    ${responses}
    Wait For task2    ${responses}    timeout=1200    interval=60

Add Network Sets
    [Tags]    ADD-NW-SETS    OV-SETUP    P0
    [Documentation]     Add Network Sets to OneView
    Add Network Sets from variable    ${networksets}

Add Osds Server
    [Tags]      ADD-OSDS    OV-SETUP    P0
    ${osds_body} =    Create Deployment Server Payload    ${osdeploymentserver}    OSDS-3enc
    ${response} =    Fusion Api Create OS DeploymentServer    ${osds_body}
    Wait For task2    ${response}    timeout=1200    interval=60

Add LIG
    [Documentation]     Add LIG to OneView
    [Tags]      ADD-LIG    OV-SETUP    P0
    Add LIG from list   ${ligs}

Add Enclosure Group
    [Tags]   ADD-EG    OV-SETUP    P0
    Add Enclosure Group from Variable    ${eg}

Create Logical Enclosure
    [Documentation]    ADD-LE   P0  OV-SETUP
    [Tags]    critical    ADD-LE    P0
    Add Logical Enclosure from variable    ${le}


Add Storage Systems and Pools
    [Documentation]    Connect and Add Storage System to OneView
    [Tags]    P0    ADD-SS    OV-SETUP
    ${responses}=  Connect and Add Storage Systems  ${storage_systems}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}    timeout=1200    interval=60

Edit the Storage Pools to Managed
    [Documentation]     Edit Storage Pool to change it from Discovered to Managed Status
    [Tags]  SV  EDIT-SPOOLS
    Run Keyword If  '${PREV TEST STATUS}' == 'FAIL'     Fatal Error    message=StorageSystem not added.
    ${responses} =  Edit Storage Pools Async    ${storage_pools}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}    timeout=1200    interval=60
    Verify Storage Pool is Managed      ${storage_pools}
