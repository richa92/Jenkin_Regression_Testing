*** Settings ***
Documentation           Tests to add base resources, add enclosure, upload SPP and initiate BigBang firmware update for BFS.
Resource                resource.txt
Suite Setup             BFS OV Suite Setup    ${admin_credentials}
Suite Teardown          BFS OV Suite Teardown

*** Test Cases ***
Add San Manager
    [Documentation]     Add SAN Manager to OneView
    [Tags]  SETUP  ADD-SM  C7K  Synergy
    Run Keyword If  ${san_managers} is not ${null}     Add San Managers Async    ${san_managers}    ${VERIFY}  ${expected_san_managers}

Add Ethernet Networks
    [Documentation]     Add Ethernet Networks to OneView
    [Tags]  SETUP  ADD-ETH  C7K  Synergy
    Run Keyword If  ${ethernet_networks} is not ${null}     Add Ethernet Networks from variable async  ${ethernet_networks}  ${VERIFY}  ${expected_ethernet_networks}

Add FCOE Networks
    [Documentation]     Add FCoE Networks to OneView
    [Tags]  SETUP  ADD-FCOE  C7K  Synergy
    Run Keyword If  ${fcoe_networks} is not ${null}    Add FCoE Networks from variable async    ${fcoe_networks}    ${VERIFY}   ${expected_fcoe_networks}

Add FC networks
    [Documentation]        Add FC Networks to OneView
    [Tags]    SETUP  ADD-FC  C7K  Synergy
    Run Keyword If  ${fc_networks} is not ${null}    Add FC Networks from variable async    ${fc_networks}    ${VERIFY}    ${expected_fc_networks}

Add ISCSI Networks
    [Documentation]     Add Iscsi Networks to OneView
    [Tags]  SETUP  ADD-ISCSI  C7K  Synergy
    Run Keyword If  ${iscsi_networks} is not ${null}     Add Ethernet Networks from variable async  ${iscsi_networks}  ${VERIFY}  ${expected_iscsi_networks}

Add LIG
    [Documentation]     Add LIG to OneView
    [Tags]  SETUP  ADD-LIG  C7K  Synergy
    Run Keyword If    ${ligs} is not ${null}   Add LIG async   ${ligs}  ${VERIFY}  ${expected_lig}

Add EG
    [Documentation]     Add Enclosure Group to OneView
    [Tags]  SETUP  ADD-EG  C7K  Synergy
    Run Keyword If  ${encgroups_add} is not ${null}     Add Enclosure Group from variable async    ${encgroups_add}  ${VERIFY}  ${expected_encgroups_add}

Add Enclosure
    [Documentation]     Add Enclosures to OneView
    [Tags]  SETUP  ADD-ENCS  C7K
    ${responses} =  Run Keyword If   ${enclosures} is not ${null}    Add Non-Existing Enclosures from variable Async  ${enclosures}
    ${reslength} =  get length   ${responses}
    Run Keyword If    '${reslength}' is not '${0}'   Wait For Task2  ${responses}     timeout=1500    interval=10
    Run Keyword If  ${expected_enclosures} is not ${null}   Verify Enclosures from list  ${expected_enclosures}

Add Licenses
    [Tags]    LICENSES  Synergy
    [Documentation]     Add Licenses to OneView
    ${licenses} =   Get Variable Value  ${licenses}
    Run Keyword If  ${licenses} is not ${null}      Add Licenses from variable  ${licenses}  ${VERIFY}

Add Logical Enclosure
    [Documentation]     Add Logical Enclosure
    [Tags]      ADD-LE  Synergy
    Add Logical Enclosure from lists Async    ${logical_enclosure}  ${VERIFY}    expected_logical_enclosure=${expected_logical_enclosure}

Add Storage System Async
    [Documentation]     Connect and Add Storage System to OneView
    [Tags]  SV  ADD-SS  C7K  Synergy
    ${responses} =  Connect and Add Storage Systems  ${storage_systems}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_storage_systems}

Edit the Storage Pools to Managed
    [Documentation]     Edit Storage Pool to change it from Discovered to Managed Status
    [Tags]  SV  EDIT-SPOOLS  C7K  Synergy
    Run Keyword If  '${PREV TEST STATUS}' == 'FAIL'     Pause Execution    message = Add StorageSystem Async failed. Press OK to continue..
    ${responses} =  Edit Storage Pools Async    ${storage_pools}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Storage Pool is Managed      ${storage_pools}

Add Already Existing Storage Volumes From Storage Systems
    [Tags]  SV  ADD-EX-SV  C7K  Synergy
    [Documentation]     Add Already Existing Storage Volumes to OneView
    ${responses} =  Add Existing Storage Volumes Async  ${existing_storage_volumes}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_existing_storage_volumes}

Add SPP Bundle
    [Documentation]     Add SPP bundle to OneView
    [Tags]    FW  ADD-SPP  C7K  Synergy
    Upload Firmware Bundle Async    ${spp_path}

Add SPP Bundle and Hill Module
    [Documentation]     Add SPP bundle and Hill Module to OneView
    [Tags]    FW  ADD-SPP-HILL
    :FOR  ${spp_path}  IN  @{spp_paths}
    \    Upload Firmware Bundle Async    ${spp_path}

Create SPP Custom build
    [Documentation]   Create SPP custom build
    [Tags]  FW  C7K-HILL  C-SPP
    :FOR  ${baseline_spp_name}  IN  @{baseline_spp_names}
    \  Create SPP Custom Build for C7K  ${baseline_spp_name}

BigBang Firmware Update For Synergy
    [Documentation]     Retrieve LE name and initiate BigBang Firmware update
    ...                 selected force option as True with SharedInfrastructureAndServerProfiles option
    [Tags]    FW  SY-UPD-BB-FW  Synergy
    Power off ALL servers  PressAndHold
    ${spp_version}=  Get Firmware Bundle Version
    Update Logical Enclosure Firmware Async   ${le_names_firmware_update}  ${spp_version}  ${True}  SharedInfrastructureAndServerProfiles

BigBang Firmware Update For C-Series
    [Documentation]     Retrieve LE name and initiate BigBang Firmware update
    ...                 selected force option as True with SharedInfrastructureAndServerProfiles option
    [Tags]    FW  C7K-UPD-BB-FW  C7K-NO-HILL  C7K
    Power off ALL servers  PressAndHold
    ${spp_version}=  Get Firmware Bundle Version
    Update Logical Enclosure Firmware Async   ${encl_names_firmware_update}  ${spp_version}  ${True}  SharedInfrastructureAndServerProfiles

BigBang Firmware Update For C-Series with hill module
    [Documentation]     Retrieve LE name and initiate BigBang Firmware update
    ...                 selected force option as True with SharedInfrastructureAndServerProfiles option
    [Tags]    FW  C7K-UPD-BB-FW  C7K-HILL  Synergy
    Power off ALL servers  PressAndHold
    ${spp_version}=  Get Firmware Bundle Version from custom spp  ${custom_spp['customBaselineName']}
    Update Logical Enclosure Firmware Async   ${encl_names_firmware_update}  ${spp_version}  ${True}  SharedInfrastructureAndServerProfiles
