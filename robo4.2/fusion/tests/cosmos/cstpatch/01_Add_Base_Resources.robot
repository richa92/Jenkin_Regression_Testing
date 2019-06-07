*** Settings ***
Documentation           Tests to add base resources along with logical enclosure
Resource                resource.txt
Suite Setup             Patch Suite Setup    ${admin_credentials}
Suite Teardown          Patch Suite Teardown
*** Test Cases ***
Add Licenses
    [Tags]    SETUP     LICENSES   TBIRD   C7000
    [Documentation]     Add Licenses to OneView
    ${licenses} =   Get Variable Value  ${licenses}
    Run Keyword If  ${licenses} is not ${null}      Add Licenses from variable  ${licenses}  ${VERIFY}

Add Users
    [Tags]    SETUP        USERS   TBIRD   C7000
    [Documentation]        Add users to OneView (roles - Infrastructure administrator, Full, Server administrator, Network administrator, Backup administrator, Read only and Storage administrator)
    ${users} =    Get Variable Value    ${users}
    Run Keyword If  ${users} is not ${null}     Add Users from variable async  ${users}    ${VERIFY}  expected_users=${expected_users}

Register IP subnet
    [Documentation]     Add IP subnets to OneView
    [Tags]  SETUP  I3S    ADD-SUBNET   TBIRD
    Add IP Subnets to Oneview        ${ipv4_subnet}

Enable ALL Generated ID Ranges
    [Documentation]     Add IP subnets to OneView
    [Tags]  SETUP  I3S    EN-RNG   TBIRD
    Enable ALL Generated ID Ranges   /rest/id-pools/VMAC
    Enable ALL Generated ID Ranges   /rest/id-pools/VWWN
    Enable ALL Generated ID Ranges    /rest/id-pools/VSN

Register IP pools ranges
    [Documentation]     Add IP Ranges to OneView
    [Tags]  SETUP  I3S    ADD-POOL   TBIRD
    Register IP pools ranges    ${ipv4_ranges}

Add Address Range
    [Documentation]     Add address range to OneView
    [Tags]  SETUP  I3S    ADD-RNG  TBIRD
    Run Keyword If    ${ranges} is not ${null}        Add Ranges From variable    ${ranges}

Add San Manager
    [Documentation]     Add SAN Manager to OneView
    [Tags]  SETUP  ADD-SM   TBIRD   C7000
    Run Keyword If  ${san_managers} is not ${null}     Add San Managers Async    ${san_managers}    ${VERIFY}  ${expected_san_managers}

Add Ethernet Networks
    [Documentation]     Add Ethernet Networks to OneView
    [Tags]  SETUP  ADD-ENW   TBIRD   C7000
    Run Keyword If  ${ethernet_networks} is not ${null}     Add Ethernet Networks from variable async  ${ethernet_networks}  ${VERIFY}  ${expected_ethernet_networks}

Add I3S Networks
    [Documentation]     Add I3S Networks to OneView
    [Tags]  SETUP  I3S   ADD-I3S    TBIRD
    Run Keyword If  ${i3s_networks} is not ${null}     Add Ethernet Networks from variable async  ${i3s_networks}  ${VERIFY}  ${expected_i3s_networks}

Associate subnet
    [Documentation]     Associate Subnet to networks
    [Tags]  SETUP  I3S    ASS-SUBNET  TBIRD
    :FOR    ${sub_assc}    in    @{subnet_association}
    \    Edit network    ${sub_assc}

Add FCOE Networks
    [Documentation]     Add FCoE Networks to OneView
    [Tags]  SETUP  ADD-FCOE  TBIRD   C7000
    Run Keyword If  ${fcoe_networks} is not ${null}    Add FCoE Networks from variable async    ${fcoe_networks}    ${VERIFY}   ${expected_fcoe_networks}

Add FC networks
    [Documentation]        Add FC Networks to OneView
    [Tags]    SETUP  ADD-FC  TBIRD   C7000
    Run Keyword If  ${fc_networks} is not ${null}    Add FC Networks from variable async    ${fc_networks}    ${VERIFY}    ${expected_fc_networks}

Add Network Sets
    [Tags]    SETUP        NW-SETS   TBIRD   C7000
    [Documentation]        Add Network Sets to OneView
    Run Keyword If    ${networksets} is not ${null}      Add Networks Sets from variable async  ${networksets}  ${VERIFY}  expected_network_sets=${expected_networksets}

Add LIG
    [Documentation]     Add LIG to OneView
    [Tags]  SETUP  ADD-LIG  TBIRD   C7000
    Run Keyword If    ${ligs} is not ${null}   Add LIG async   ${ligs}  ${VERIFY}  ${expected_lig}

Add SAS LIG
    [Tags]   SETUP        SAS   TBIRD   C7000
    [Documentation]       Add SAS LIG to OneView
    Run Keyword If  ${sas_lig} is not ${null}    Add SAS LIG from variable async    ${sas_lig}    ${VERIFY}    expected_sas_lig=${expected_sas_lig}

Add Deployment Server
    [Documentation]     Add Deployment server to OneView
    [Tags]  SETUP  I3S  ADD-DS   TBIRD
    Add Deployment Server    ${deployment_server}

Add EG
    [Documentation]     Add Enclosure Group to OneView
    [Tags]  SETUP  ADD-EG  TBIRD   C7000
    Run Keyword If  ${encgroups_add} is not ${null}     Add Enclosure Group from variable async    ${encgroups_add}  ${VERIFY}  ${expected_encgroups_add}

Add Logical Enclosure
    [Tags]      ADDLE   TBIRD
    Add Logical Enclosure from lists Async    ${logical_enclosure}  ${VERIFY}    expected_logical_enclosure=${expected_logical_enclosure}
    Log All Warning and Critical Alerts

Verify Enclosure
    [Tags]      VERIFY   TBIRD1
    ${verify_enc_statuses} =   Create List
    ${enc_status} =     Create List
    :FOR    ${enc}  IN  @{configured_enclosures}
    \   ${verify_enc}=   Verify TBird Resource     ${enc}
    \   Append To List  ${verify_enc_statuses}  ${verify_enc}
    :FOR    ${verify_enc}   IN  @{verify_enc_statuses}
    \   Run Keyword If  '${verify_enc['status']}'=='False'  Log   Verify Enclosure Failed for Enclosure ${verify_enc['name']}     WARN
    \   Run Keyword If  '${verify_enc['status']}'=='False'  Append to List    ${enc_status}     OK
    ${len} =   Get Length  ${enc_status}
    Run Keyword Unless  ${len}==0   Fail     msg=Enclosure Verification Failed

Add Enclosure
    [Documentation]     Add Enclosures to OneView
    [Tags]  SETUP  ADD-ENCS  C7000
    ${responses} =  Run Keyword If   ${enclosures} is not ${null}    Add Non-Existing Enclosures from variable Async  ${enclosures}
    ${reslength} =  get length   ${responses}
    Run Keyword If    '${reslength}' is not '${0}'   Wait For Task2  ${responses}     timeout=2000    interval=10
    Run Keyword If  ${expected_enclosures} is not ${null}   Verify Enclosures from list  ${expected_enclosures}

Add Storage System Async
    [Documentation]     Connect and Add Storage System to OneView
    [Tags]  SV  ADD-SS   TBIRD   C7000
    ${responses} =  Connect and Add Storage Systems  ${storage_systems_with_pools}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_storage_systems_with_pools}

Edit the Storage Pools to Managed
    [Documentation]     Edit Storage Pool to change it from Discovered to Managed Status
    [Tags]  SV  EDIT-SPOOLS   TBIRD   C7000
    ${responses} =  Edit Storage Pools Async    ${storage_pools_toedit}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Storage Pool is Managed      ${storage_pools_toedit}

Add Storage Volume Templates
    [Tags]    SVT  TBIRD  C7000
    [Documentation]        Add Storage VOLUME TEMPLATES to OneView
    ${responses} =  Run Keyword If  ${storage_volume_templates} is not ${null}    Add Storage Volume Templates Async   ${storage_volume_templates}
    Verify Resources for List  ${expected_storage_volume_templates}

Add Storage Volumes
    [Tags]  SV  ADD-SV   TBIRD   C7000
    [Documentation]     Add Storage Volumes to OneView
    ${responses} =  Add Storage Volumes Async  ${storage_volumes}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_storage_volumes}
