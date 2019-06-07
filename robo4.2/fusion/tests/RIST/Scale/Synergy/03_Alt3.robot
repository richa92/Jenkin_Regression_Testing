*** Settings ***
Resource           resource.txt
Suite Setup                     Scale Suite Setup     ${admin_credentials}
Suite Teardown                  Scale Suite Teardown

*** Test Cases ***

Add San Manager
    [Tags]    ALT3     SAN-MANAGER
    [Documentation]     Add SAN Manager to OneView
    ${responses}=   Add San Managers Async    ${san_managers}
    Run Keyword for List  ${responses}  Wait For Task2
    Verify Scale Resources  ${expected_san_managers}

Add Ethernet Networks Bulk
    [Tags]    ALT3     bulk
    [Documentation]        Add Ethernet Networks to OneView in Bulk
    Run Keyword If  ${ethernet_networks} is not ${null}    Create Bulk Ethernet Networks   ${ethernet_networks}     timeout=1000  interval=10
    Verify Scale Resources  ${expected_ethernet_networks}

Add FC networks
    [Tags]    ALT3        FC-NW
    [Documentation]        Add FC Networks to OneView
    ${responses} =    Run Keyword If    ${fc_networks} is not ${null}    Add Non Existing FC Networks  ${fc_networks}
    Run Keyword If     ${responses} is not ${null}  Run Keyword for List  ${responses}  Wait For Task2
    Verify Scale Resources  ${expected_fc_networks}

Add FCoE networks
    [Tags]    ALT3        FCoE-NW
    [Documentation]        Add FCoE Networks to OneView
    Run Keyword If    ${fcoe_networks} is not ${null}      Add FCoE Networks from variable async  ${fcoe_networks}  ${VERIFY}  ${expected_fcoe_networks}
    Verify Scale Resources  ${expected_fcoe_networks}

Add Network Sets
    [Tags]    ALT3        NW-SETS
    [Documentation]        Add Network Sets to OneView
    Run Keyword If    ${networksets} is not ${null}      Add Networks Sets from variable async  ${network_sets}  ${VERIFY}  ${expected_network_sets}
    Verify Scale Resources  ${expected_network_sets}

Add Storage Systems and Verify
    [Tags]    ALT3        S-SYS
    [Documentation]        Add Storage Systems to OneView
    ${responses}=  Connect and Add Storage Systems  ${storage_systems}
    Run Keyword If     ${responses} is not ${null}  Run Keyword for List  ${responses}  Wait For Task2
    Verify Scale Resources  ${expected_storage_systems}

Add Storage Pools
    [Tags]    ALT3     S-POOL
    [Documentation]     Add Storage Pools to OneView
    ${responses}=  Edit Storage Pools Async  ${storage_pools}
    Run Keyword for List  ${responses}  Wait For Task2
    Verify Storage Pool is Managed      ${storage_pools}

Add Storage Volumes
    [Tags]    ALT3        SV
    [Documentation]        Add Storage VOLUMES to OneView
    ${responses}=    Add Storage Volumes Async    ${d_storage_volume}
    Run Keyword for List  ${responses}  Wait For Task2
    Verify Scale Resources  ${d_expected_storage_volume}

Edit Logical Interconnect Groups
    [Tags]      ALT3   EDITLIG
    [Documentation]     Edit Logical Interconnect Group
    ${responses} =      Edit LIG    ${update_ligs}
    Run Keyword If  ${responses} is not ${null}  Run Keyword for List    ${responses}     Wait For Task2    timeout=200    interval=5
    Verify Scale Resources  ${expected_ligs_updated}

Update LE From Group
    [Tags]    ALT3     UPDATELE
    [Documentation]        Invoke update from group on LE
    Update Logical Enclosure from Group from list   ${logical_enclosure}    timeout=2000    interval=10
    Verify Scale Resources  ${expected_logical_enclosure}

Verify Logical Interconnects
    [Tags]  ALT3    VERIFYLOGICINTERCONNECTS
    Verify All Logical Interconnects
