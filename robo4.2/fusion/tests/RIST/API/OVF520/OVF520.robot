*** Settings ***
Documentation
...                   Description:  Q2 tests for initial support of Gen10 DL servers with non-VC SAN switches. OVF520
...                                 does not include support for DL adapter programming.  The user is expected to
...                                 manually both the DL adapters as well as the non-VC SAN switch. As such, these tests
...                                 do not verify adapter programming on the DL. A subsequent feature will enable DL
...                                 adapter programming, at which time these tests will need to be updated.
...
...                                 Requires OneView 5.0 or later release, X-API 1200 or later
...
...                   Rally:  OVF520
...
...                   HW Requirements:
...                       Servers Hardware Type(s):
...                           2 DL gen 10 servers.  Note that 1 or both servers can use DCS since OVF520 does not
...                                                 do any configuration of the DLs.  The 2 DLs are required to have
...                                                 different Server Hardware Types in order to to transformation API
...                                                 testing.
...                           1 C7000 enclosure with a Gen10 blade.  Needed for transformation API testing
...
...                   Interconnects: Not needed
...
...                   Local Storage (BigBird/Natasha): Not needed
...
...                   Uplinks/Connections: Not needed
...
...                   External Storage
...                       Storage System Type(s):  StoreServ
...                       Storage Pools: StoreServ: FC_r1
...                       Storage Volumes:
...                           Existing:  None
...                           Created:  StoreServ: OVF520_vol1 (DL1), OVF520_vol1 (DL2)
...
...                   Other External Systems needed
...                       None
...
...                   Special Algorithms, Conversions, "Python Helpers" or Scripts
...                        Explain any "specials" that were created for this test or list: None
...                        All created Helpers and Scripts are in the repo:  .\Tools\Some_New_Tool
...
...                   Shared Keywords Created (Resources\api)
...                       If any New Keywords were created, list those here or list: None

Library             FusionLibrary
Library             BuiltIn
Library             Collections

Resource            ../global_variables.robot
Resource            ./../../../../Resources/api/fusion_api_resource.txt

Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Initialize the Variables and Log In as Administrator
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
...                 AND  Initialize Appliance for Test Suite Setup

Suite Teardown      Run Keywords  Restore Appliance for Test Suite Teardown
...                 AND  Fusion Api Logout Appliance

Test Setup          ${None}
Test Teardown       Teardown Test Case

*** Variables ***

*** Test Cases ***

# 1 connection test cases
#########################

OVF520 TS1 - create unassigned gen10 SP from gen10 SPT without WWPN (1 connection)
    [Documentation]  SPTs don't specify WWPNs. When adding a Server Profile, the user can optionally specify WWPNs.
    ...              This test does not specify WWPNs for a SP with 1 connection
    [Tags]  SP  TC1
    ${task}=  Add Server Profile  ${dl1_1_connection_unassigned_sp_from_spt}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_1_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  1
    Should Be Equal  ${connections[0]["wwpn"]}  ${None}

OVF520 TS1 - create unassigned gen10 SP from gen10 SPT with WWPN (1 connection)
    [Documentation]  SPTs don't specify WWPNs. When adding a Server Profile, the user can optionally specify WWPNs.
    ...              This test specifies WWPNs for a SP with 1 connection
    [Tags]  SP  TC2
    ${task}=  Add Server Profile  ${dl1_1_connection_unassigned_sp_from_spt_with_wwpn}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_1_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  1
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}

OVF520 TS1 - create unassigned gen10 SP without WWPN (1 connection)
    [Documentation]  An unassigned Server Profile can be created without specifying WWPNs.
    [Tags]  SP  TC3
    ${my_sp}=  Copy Dictionary  ${dl1_1_connection_unassigned_sp}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${None}

    ${task}=  Add Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_1_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  1
    Should Be Equal  ${connections[0]["wwpn"]}  ${None}

OVF520 TS1 - assign an unassigned gen10 SP to gen10 DL including specifying WWPN value (1 connection)
    [Documentation]  An unassigned Server Profile must specify WWPNs when being assigned to hardware.
    [Tags]  SP  TC4
    ${task}=  Add Server Profile  ${dl1_1_connection_unassigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${task}=  Edit Server Profile  ${dl1_1_connection_edit_assign_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_1_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  1
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}
    Verify Storage Paths  ${sp["sanStorage"]["volumeAttachments"][0]["storagePaths"]}  1

OVF520 TS1 - assign an unassigned gen10 SP to gen10 DL including specifying incorrectly formatted WWPN (1 connection)
    [Documentation]  WWPN formatting is validated when assigning an unassigned Server Profile to hardware
    [Tags]  SP  TC5
    ${task}=  Add Server Profile  ${dl1_1_connection_unassigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${my_sp}=  Copy Dictionary  ${dl1_1_connection_edit_assign_sp}
    :FOR  ${wwpn}  IN  @{BAD_WWPNS}
    \   Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${wwpn}
    \   ${task}=  Edit Server Profile  ${my_sp}
    \   Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=InvalidWwpn

OVF520 TS1 - create assigned gen10 SP on gen10 DL including specifying WWPN (1 connection)
    [Documentation]  Creating assigned Server Profile must specify WWPNs
    [Tags]  SP  TC6
    ${task}=  Add Server Profile  ${dl1_1_connection_assigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${sp}=  Get Resource  SP:${DL1_1_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  1
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}
    Verify Storage Paths  ${sp["sanStorage"]["volumeAttachments"][0]["storagePaths"]}  1

OVF520 TS1 - create assigned gen10 SP on gen10 DL including specifying incorrectly formatted WWPN (1 connection)
    [Documentation]  WWPN formatting is validated when creating an assigned Server Profile
    [Tags]  SP  TC7
    ${my_sp}=  Copy Dictionary  ${dl1_1_connection_assigned_sp}
    :FOR  ${wwpn}  IN  @{BAD_WWPNS}
    \   Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${wwpn}
    \   ${task}=  Add Server Profile  ${my_sp}
    \   Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=InvalidWwpn

OVF520 TS1 - unassign assigned gen10 SP keeping WWPN (1 connection)
    [Documentation]  WWPNs are allowed to be retained when unassigning an assigned Server Profile
    [Tags]  SP  TC8
    ${task}=  Add Server Profile  ${dl1_1_connection_assigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${task}=  Edit Server Profile  ${dl1_1_connection_edit_unassign_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_1_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  1
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}

OVF520 TS1 - unassign assigned gen10 SP clearing WWPN (1 connection)
    [Documentation]  WWPNs are allowed to be cleared when unassigning an assigned Server Profile
    [Tags]  SP  TC9
    ${task}=  Add Server Profile  ${dl1_1_connection_assigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${my_sp}=  Copy Dictionary  ${dl1_1_connection_edit_unassign_sp}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${None}
    ${task}=  Edit Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_1_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  1
    Should Be Equal  ${connections[0]["wwpn"]}  ${None}

OVF520 TS1 - Assigning SP with dup WWPN on already assigned SP fails (1 connection)
    [Documentation]  An appliance cannot have 2 Server Profiles with the same WWPN
    [Tags]  SP  TC10
    ${task}=  Add Server Profile  ${dl1_1_connection_assigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${my_sp}=  Copy Dictionary  ${dl2_1_connection_assigned_sp}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${dl1_1_connection_assigned_sp["connectionSettings"]["connections"][0]["wwpn"]}
    ${task}=  Add Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=DuplicateWwpnForAssignedProfiles

OVF520 TS1 - Unassigned SP can have dup WWPN with other unassigned or assigned SPs (1 connection)
    [Documentation]  An appliance can have multiple unassigned Server Profiles with duplicate WWPNs
    [Tags]  SP  TC11
    ${task}=  Add Server Profile  ${dl1_1_connection_assigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${task}=  Edit Server Profile  ${dl1_1_connection_edit_unassign_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_1_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  1
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}

    ${my_sp}=  Copy Dictionary  ${dl2_1_connection_assigned_sp}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${DL1_WWPN["port1"]}
    ${task}=  Add Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${my_sp}=  Copy Dictionary  ${dl2_1_connection_edit_unassign_sp}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${DL1_WWPN["port1"]}
    ${task}=  Edit Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL2_1_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  1
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}

    ${task}=  Edit Server Profile  ${dl1_1_connection_edit_assign_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_1_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  1
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}
    Verify Storage Paths  ${sp["sanStorage"]["volumeAttachments"][0]["storagePaths"]}  1

    ${my_sp}=  Copy Dictionary  ${dl2_1_connection_edit_assign_sp}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${DL1_WWPN["port1"]}
    ${task}=  Edit Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=DuplicateWwpnForAssignedProfiles

OVF520 TS1 - transformation to another DL SHT should clear connection WWPN (1 connection)
    [Documentation]  Connection WWPNs are cleared when using the transformation API to another DL Server Hardware Type
    [Tags]  SP  TC12
    ${task}=  Add Server Profile  ${dl1_1_connection_assigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_1_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  1
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}

    ${dl2_sht}=  Get Resource  SHT:${DL2_SHT_NAME}
    ${my_sp}=  Copy Dictionary  ${dl1_1_connection_assigned_sp}
    Set To Dictionary  ${my_sp}  serverHardwareTypeUri=${dl2_sht["uri"]}
    Set To Dictionary  ${my_sp}  enclosureGroupUri=${None}
    ${tsp_uri}=  Get Server Profile Transformation URI  ${my_sp}
    ${tsp}=  Get Server Profile Transformation  ${tsp_uri}
    ${connections}=  Set Variable  ${tsp["serverProfile"]["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  1
    Should Be Equal  ${connections[0]["wwpn"]}  ${None}

OVF520 TS1 - transformation to a C7000 SHT should clear connection WWPN (1 connection)
    [Documentation]  Connections are cleared when using the transformation API to tranfer a DL Server Profile to a C7000
    ...              server
    [Tags]  SP  TC13
    ${task}=  Add Server Profile  ${dl1_1_connection_assigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_1_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  1
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}

    ${c7000_sht}=  Get Resource  SHT:${C7000_SHT_NAME}
    ${c7000_eg}=  Get Resource  EG:${C7000_EG_NAME}
    ${my_sp}=  Copy Dictionary  ${dl1_1_connection_assigned_sp}
    Set To Dictionary  ${my_sp}  serverHardwareTypeUri=${c7000_sht["uri"]}
    Set To Dictionary  ${my_sp}  enclosureGroupUri=${c7000_eg["uri"]}
    ${tsp_uri}=  Get Server Profile Transformation URI  ${my_sp}
    ${tsp}=  Get Server Profile Transformation  ${tsp_uri}
    ${connections}=  Set Variable  ${tsp["serverProfile"]["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  0  # connections are cleared on DL to C7000 transformations

# 2 connection test cases
#########################

OVF520 TS1 - create unassigned gen10 SP from gen10 SPT without WWPN (2 connection)
    [Documentation]  SPTs don't specify WWPNs. When adding a Server Profile, the user can optionally specify WWPNs.
    ...              This test does not specify WWPNs for a SP with 2 connections
    [Tags]  SP  TC14
    ${task}=  Add Server Profile  ${dl1_2_connection_unassigned_sp_from_spt}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_2_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  2
    Should Be Equal  ${connections[0]["wwpn"]}  ${None}
    Should Be Equal  ${connections[1]["wwpn"]}  ${None}

OVF520 TS1 - create unassigned gen10 SP from gen10 SPT with WWPN (2 connection)
    [Documentation]  SPTs don't specify WWPNs. When adding a Server Profile, the user can optionally specify WWPNs.
    ...              This test specifies WWPNs for a SP with 2 connections
    [Tags]  SP  TC15
    ${task}=  Add Server Profile  ${dl1_2_connection_unassigned_sp_from_spt_with_wwpn}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_2_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  2
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}
    WWNs Should Be Equal  ${connections[1]["wwpn"]}  ${DL1_WWPN["port2"]}

OVF520 TS1 - create unassigned gen10 SP without WWPN (2 connection)
    [Documentation]  An unassigned Server Profile can be created without specifying WWPNs.
    [Tags]  SP  TC16
    ${my_sp}=  Copy Dictionary  ${dl1_2_connection_unassigned_sp}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${None}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][1]}  wwpn=${None}

    ${task}=  Add Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_2_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  2
    Should Be Equal  ${connections[0]["wwpn"]}  ${None}
    Should Be Equal  ${connections[1]["wwpn"]}  ${None}

OVF520 TS1 - assign an unassigned gen10 SP to gen10 DL including specifying WWPN value (2 connection)
    [Documentation]  An unassigned Server Profile must specify WWPNs when being assigned to hardware.
    [Tags]  SP  TC17
    ${task}=  Add Server Profile  ${dl1_2_connection_unassigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${task}=  Edit Server Profile  ${dl1_2_connection_edit_assign_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_2_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  2
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}
    WWNs Should Be Equal  ${connections[1]["wwpn"]}  ${DL1_WWPN["port2"]}
    Verify Storage Paths  ${sp["sanStorage"]["volumeAttachments"][0]["storagePaths"]}  2

OVF520 TS1 - assign an unassigned gen10 SP to gen10 DL including specifying incorrectly formatted WWPN (2 connection)
    [Documentation]  WWPN formatting is validated when assigning an unassigned Server Profile to hardware
    [Tags]  SP  TC18
    ${task}=  Add Server Profile  ${dl1_2_connection_unassigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${my_sp}=  Copy Dictionary  ${dl1_2_connection_edit_assign_sp}
    :FOR  ${wwpn}  IN  @{BAD_WWPNS}
    \   Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${wwpn}
    \   ${task}=  Edit Server Profile  ${my_sp}
    \   Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=InvalidWwpn

    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${DL1_WWPN["port1"]}

    :FOR  ${wwpn}  IN  @{BAD_WWPNS}
    \   Set To Dictionary  ${my_sp["connectionSettings"]["connections"][1]}  wwpn=${wwpn}
    \   ${task}=  Edit Server Profile  ${my_sp}
    \   Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=InvalidWwpn

    :FOR  ${wwpn}  IN  @{BAD_WWPNS}
    \   Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${wwpn}
    \   ${task}=  Edit Server Profile  ${my_sp}
    \   Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=InvalidWwpn

OVF520 TS1 - create assigned gen10 SP on gen10 DL including specifying WWPN (2 connection)
    [Documentation]  Creating assigned Server Profile must specify WWPNs
    [Tags]  SP  TC19
    ${task}=  Add Server Profile  ${dl1_2_connection_assigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${sp}=  Get Resource  SP:${DL1_2_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  2
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}
    WWNs Should Be Equal  ${connections[1]["wwpn"]}  ${DL1_WWPN["port2"]}
    Verify Storage Paths  ${sp["sanStorage"]["volumeAttachments"][0]["storagePaths"]}  2

OVF520 TS1 - create assigned gen10 SP on gen10 DL including specifying incorrectly formatted WWPN (2 connection)
    [Documentation]  WWPN formatting is validated when creating an assigned Server Profile
    [Tags]  SP  TC20
    ${my_sp}=  Copy Dictionary  ${dl1_2_connection_assigned_sp}
    :FOR  ${wwpn}  IN  @{BAD_WWPNS}
    \   Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${wwpn}
    \   ${task}=  Add Server Profile  ${my_sp}
    \   Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=InvalidWwpn

    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${DL1_WWPN["port1"]}

    :FOR  ${wwpn}  IN  @{BAD_WWPNS}
    \   Set To Dictionary  ${my_sp["connectionSettings"]["connections"][1]}  wwpn=${wwpn}
    \   ${task}=  Add Server Profile  ${my_sp}
    \   Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=InvalidWwpn

    :FOR  ${wwpn}  IN  @{BAD_WWPNS}
    \   Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${wwpn}
    \   ${task}=  Add Server Profile  ${my_sp}
    \   Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=InvalidWwpn

OVF520 TS1 - unassign assigned gen10 SP keeping WWPN (2 connection)
    [Documentation]  WWPNs are allowed to be retained when unassigning an assigned Server Profile
    [Tags]  SP  TC21
    ${task}=  Add Server Profile  ${dl1_2_connection_assigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${task}=  Edit Server Profile  ${dl1_2_connection_edit_unassign_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_2_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  2
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}
    WWNs Should Be Equal  ${connections[1]["wwpn"]}  ${DL1_WWPN["port2"]}

OVF520 TS1 - unassign assigned gen10 SP clearing WWPN (2 connection)
    [Documentation]  WWPNs are allowed to be cleared when unassigning an assigned Server Profile
    [Tags]  SP  TC22
    ${task}=  Add Server Profile  ${dl1_2_connection_assigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${my_sp}=  Copy Dictionary  ${dl1_2_connection_edit_unassign_sp}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${None}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][1]}  wwpn=${None}
    ${task}=  Edit Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_2_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  2
    Should Be Equal  ${connections[0]["wwpn"]}  ${None}
    Should Be Equal  ${connections[1]["wwpn"]}  ${None}

OVF520 TS1 - Assigning SP with dup WWPN on already assigned SP fails (2 connection)
    [Documentation]  An appliance cannot have 2 Server Profiles with the same WWPN
    [Tags]  SP  TC23
    ${task}=  Add Server Profile  ${dl1_2_connection_assigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${my_sp}=  Copy Dictionary  ${dl2_2_connection_assigned_sp}

    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${dl1_2_connection_assigned_sp["connectionSettings"]["connections"][0]["wwpn"]}
    ${task}=  Add Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=DuplicateWwpnForAssignedProfiles

    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${dl1_2_connection_assigned_sp["connectionSettings"]["connections"][1]["wwpn"]}
    ${task}=  Add Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=DuplicateWwpnForAssignedProfiles

    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${DL2_WWPN["port1"]}

    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][1]}  wwpn=${dl1_2_connection_assigned_sp["connectionSettings"]["connections"][0]["wwpn"]}
    ${task}=  Add Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=DuplicateWwpnForAssignedProfiles

    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][1]}  wwpn=${dl1_2_connection_assigned_sp["connectionSettings"]["connections"][1]["wwpn"]}
    ${task}=  Add Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=DuplicateWwpnForAssignedProfiles

OVF520 TS1 - Unassigned SP can have dup WWPN with other unassigned or assigned SPs (2 connection)
    [Documentation]  An appliance can have multiple unassigned Server Profiles with duplicate WWPNs
    [Tags]  SP  TC24
    ${task}=  Add Server Profile  ${dl1_2_connection_assigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${task}=  Edit Server Profile  ${dl1_2_connection_edit_unassign_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_2_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  2
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}
    WWNs Should Be Equal  ${connections[1]["wwpn"]}  ${DL1_WWPN["port2"]}

    ${my_sp}=  Copy Dictionary  ${dl2_2_connection_assigned_sp}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${DL1_WWPN["port1"]}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][1]}  wwpn=${DL1_WWPN["port2"]}
    ${task}=  Add Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${my_sp}=  Copy Dictionary  ${dl2_2_connection_edit_unassign_sp}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${DL1_WWPN["port1"]}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][1]}  wwpn=${DL1_WWPN["port2"]}
    ${task}=  Edit Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL2_2_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  2
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}
    WWNs Should Be Equal  ${connections[1]["wwpn"]}  ${DL1_WWPN["port2"]}

    ${task}=  Edit Server Profile  ${dl1_2_connection_edit_assign_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_2_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  2
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}
    WWNs Should Be Equal  ${connections[1]["wwpn"]}  ${DL1_WWPN["port2"]}
    Verify Storage Paths  ${sp["sanStorage"]["volumeAttachments"][0]["storagePaths"]}  2

    ${my_sp}=  Copy Dictionary  ${dl2_2_connection_edit_assign_sp}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][0]}  wwpn=${DL1_WWPN["port1"]}
    Set To Dictionary  ${my_sp["connectionSettings"]["connections"][1]}  wwpn=${DL1_WWPN["port2"]}
    ${task}=  Edit Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error  errorMessage=DuplicateWwpnForAssignedProfiles

OVF520 TS1 - transformation to another DL SHT should clear connection WWPN (2 connection)
    [Documentation]  Connection WWPNs are cleared when using the transformation API to another DL Server Hardware Type
    [Tags]  SP  TC25
    ${task}=  Add Server Profile  ${dl1_2_connection_assigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_2_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  2
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}
    WWNs Should Be Equal  ${connections[1]["wwpn"]}  ${DL1_WWPN["port2"]}

    ${dl2_sht}=  Get Resource  SHT:${DL2_SHT_NAME}
    ${my_sp}=  Copy Dictionary  ${dl1_2_connection_assigned_sp}
    Set To Dictionary  ${my_sp}  serverHardwareTypeUri=${dl2_sht["uri"]}
    Set To Dictionary  ${my_sp}  enclosureGroupUri=${None}
    ${tsp_uri}=  Get Server Profile Transformation URI  ${my_sp}
    ${tsp}=  Get Server Profile Transformation  ${tsp_uri}
    ${connections}=  Set Variable  ${tsp["serverProfile"]["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  2  # connections are cleared on DL to C7000 transformations

OVF520 TS1 - transformation to a C7000 SHT should clear connection WWPN (2 connection)
    [Documentation]  Connections are cleared when using the transformation API to tranfer a DL Server Profile to a C7000
    ...              server
    [Tags]  SP  TC26
    ${task}=  Add Server Profile  ${dl1_2_connection_assigned_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${DL1_2_CONNECTION_SP_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  2
    WWNs Should Be Equal  ${connections[0]["wwpn"]}  ${DL1_WWPN["port1"]}
    WWNs Should Be Equal  ${connections[1]["wwpn"]}  ${DL1_WWPN["port2"]}

    ${c7000_sht}=  Get Resource  SHT:${C7000_SHT_NAME}
    ${c7000_eg}=  Get Resource  EG:${C7000_EG_NAME}
    ${my_sp}=  Copy Dictionary  ${dl1_2_connection_assigned_sp}
    Set To Dictionary  ${my_sp}  serverHardwareTypeUri=${c7000_sht["uri"]}
    Set To Dictionary  ${my_sp}  enclosureGroupUri=${c7000_eg["uri"]}
    ${tsp_uri}=  Get Server Profile Transformation URI  ${my_sp}
    ${tsp}=  Get Server Profile Transformation  ${tsp_uri}
    ${connections}=  Set Variable  ${tsp["serverProfile"]["connectionSettings"]["connections"]}
    Length Should Be  ${connections}  0  # connections are cleared on DL to C7000 transformations

*** Keywords ***

Collect Storage System FC Port WWPN
    [Documentation]  Collect storage sytem port WWPNs to verify against server profile storagePath targets
    [Arguments]  ${port}
    Return From Keyword If  "${port["protocolType"]}" != "FC" and "${port["protocolType"]}" != "Fcoe"
    ${nwwn}=  Normalize WWN  ${port["address"]}
    ${tl}=  Set Variable  ${storage_system_connection_WWPNs[0]}
    Run Keyword If  '${port["actualSanName"]}' == '${FC_SAN_1_NAME}'  Append to List  ${storage_system_connection_WWPNs[0]}  ${nwwn}
    Run Keyword If  '${port["actualSanName"]}' == "${FC_SAN_2_NAME}"  Append to List  ${storage_system_connection_WWPNs[1]}  ${nwwn}

Initialize the Variables and Log In as Administrator
    [Documentation]  Set the log level to TRACE, initialize the variables and, login to appliance
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${appliance_credentials}

Initialize Appliance for Test Suite Setup
    [Documentation]  Initialize the appliance for the test suite

    ${ssys}=  Get Resource  SSYS:${STORESERV_NAME}
    :FOR  ${port}  IN  @{ssys["ports"]}
    \   Collect Storage System FC Port WWPN  ${port}

    Teardown Test Case

    ${task}=  Add Server Profile Template  ${dl1_1_connection_spt}
    Wait For Task2  ${task}  timeout=60  interval=2

    ${task}=  Add Server Profile Template  ${dl1_2_connection_spt}
    Wait For Task2  ${task}  timeout=60  interval=2

Restore Appliance for Test Suite Teardown
    [Documentation]  Clean up the appliance following test suite execution
    Power Off Server  ${DL1_NAME}  powerControl=PressAndHold

    ${task}=  Remove Server Profile Template  ${dl1_1_connection_spt}
    Wait For Task2  ${task}  timeout=60  interval=2

    ${task}=  Remove Server Profile Template  ${dl1_2_connection_spt}
    Wait For Task2  ${task}  timeout=60  interval=2

Teardown Test Case
    [Documentation]  Clean up the appliance following test case execution
    Power Off Server  ${DL1_NAME}  powerControl=PressAndHold
    Power Off Server  ${DL2_NAME}  powerControl=PressAndHold

    ${task}=  Remove Server Profile  ${dl1_1_connection_assigned_sp}
    Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=600  interval=10
    ${task}=  Remove Server Profile  ${dl2_1_connection_assigned_sp}
    Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=600  interval=10
    ${task}=  Remove Server Profile  ${dl1_2_connection_assigned_sp}
    Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=600  interval=10
    ${task}=  Remove Server Profile  ${dl2_2_connection_assigned_sp}
    Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=600  interval=10

    ${task}=  Remove Server Profiles by Server Hardware  ${server_hardware_uris}
    Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=600  interval=10

Normalize WWN
    [Documentation]  Given a WWN string, normalize it to be all uppercase and remove all ':' separators
    [Arguments]  ${wwn}
    ${ret}=  Remove String  ${wwn}  :
    ${ret}=  Convert To Uppercase  ${ret}
    [Return]  ${ret}

WWNs Should Be Equal
    [Documentation]  compare 2 WWNs after normalizing them
    [Arguments]  ${wwn1}  ${wwn2}
    ${nwwn1}=  Normalize WWN  ${wwn1}
    ${nwwn2}=  Normalize WWN  ${wwn2}
    Should Be Equal  ${nwwn1}  ${nwwn2}

Verify Storage Path Targets
    [Documentation]  verify the targets in a server profile storagePath element
    [Arguments]  ${targets}  ${valid_targets}
    :FOR  ${target}  IN  @{targets}
    \   ${nwwpn}=  Normalize WWN  ${target["name"]}
    \   List Should Contain Value  ${valid_targets}  ${nwwpn}

Verify Storage Paths
    [Documentation]  verify server profile storagePath information
    [Arguments]  ${storage_paths}  ${num_expected_storage_paths}

    Length Should Be  ${storage_paths}  ${num_expected_storage_paths}
    :FOR  ${sp}  IN  @{storage_paths}
    \   ${i}=  Evaluate  ${sp["connectionId"]} - 1
    \   Verify Storage Path Targets  ${sp["targets"]}  ${storage_system_connection_WWPNs[${i}]}
