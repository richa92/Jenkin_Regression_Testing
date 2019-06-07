*** Settings ***
Documentation
...                   Description:  Q2 tests for missing boot entry alerts on BladeSystem. OVF5290 enables the capability to
...                                 check to see if BIOS has discovered the FC/ECoE boot sources for connections configured
...                                 in the server profile and create alerts as appropriate.  Gen9 blades only create alerts
...                                 when a profile is applied or reapplied, Gen10 blades create alerts after every reboot.
...                                 A warning alert is posted if partial connectivity is detected, a critical alert is
...                                 posted if total connectivity loss is detected. This test exercises FC protocol only,
...                                 FC and FCoE in OneView is considered as equivalent by the dev team.
...
...                   Rally:  OVF5290
...
...                   HW Requirements:
...                       Servers Hardware Type(s):
...                           BL * gen 9 blade with FC mezz card (QMH2572,LPe1205A) in appropriate slot
...                           BL * gen 10 blade with FC mezz card (QMH2572,QMH2672,LPe1205A,LPe1605) in appropriate slot
...
...                   Interconnects
...                       2 Virtual Connect FC Modules for BladeSystem with 2 uplinks for 2 SANs
...
...                   Local Storage (BigBird/Natasha): Not needed
...
...                   Uplinks/Connections
...                       FC - uplinks for A and B side SANs ('VSAN20' and 'VSAN30' in the test data)
...
...                   External Storage
...                       Note: ideally this test would use a peer-persisted set of 2 StoreServs. Only 1 was available
...                             during development of both the OVF5290 feature code as well as this Q2 test suite, so
...                             both volumes are created on the same StoreServ. The StoreServ was configured on both the
...                             VSAN20 and VSAN30 SANs simulating 2 separate StoreServs.
...
...                       Storage System Type(s):  StoreServ
...                       Storage Pools: StoreServ: FC_r1
...                       Storage Volumes:
...                           Existing:  None
...                           Created:  StoreServ: OVF5290_C7000_vol1 (Gen9), OVF5290_C7000_vol2 (Gen9),
...                                                OVF5290_C7000_vol1 (Gen10), OVF5290_C7000_vol2 (Gen10)
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

*** Variables ***
${server_profile_gen9}=  Set Variable  ${EMPTY}
${server_profile_gen10}=  Set Variable  ${EMPTY}

*** Test Cases ***

OVF5290 TS1 - First Port Downlink Failure Should Generate Warning Alert For Gen9 UEFI 2 Target 2 Boot Volume FC Boot Profile
    [Documentation]  Verify port 1 downlink failure warning alert on Gen9
    [Tags]  SP  TC1
    Initialize Appliance For Gen9 Test Case
    Disable Gen9 A Side Downlink Port
    Reapply Gen9 Server Profile to Update Boot Sources
    Server Profile Should Have an Active Missing Boot Entry Alert Warning  ${server_profile_gen9}

OVF5290 TS1 - Second Port Downlink Failure Should Generate Warning Alert For Gen9 UEFI 2 Target 2 Boot Volume FC Boot Profile
    [Documentation]  Verify port 2 downlink failure warning alert on Gen9
    [Tags]  SP  TC2
    Initialize Appliance For Gen9 Test Case
    Disable Gen9 B Side Downlink Port
    Reapply Gen9 Server Profile to Update Boot Sources
    Server Profile Should Have an Active Missing Boot Entry Alert Warning  ${server_profile_gen9}

OVF5290 TS1 - All Ports Downlink Failure Should Generate Error Alert For Gen9 UEFI 2 Target 2 Boot Volume FC Boot Profile
    [Documentation]  Verify all port downlink failure critical alert on Gen9
    [Tags]  SP  TC3
    Initialize Appliance For Gen9 Test Case
    Disable Gen9 Downlink Ports
    Reapply Gen9 Server Profile to Update Boot Sources
    Server Profile Should Have a Active Missing Boot Entry Alert Error  ${server_profile_gen9}

OVF5290 TS1 - First Port Downlink Failure Should Generate Warning Alert For Gen10 UEFI 2 Target 2 Boot Volume FC Boot Profile
    [Documentation]  Verify port 1 downlink failure warning alert on Gen10
    [Tags]  SP  TC4
    Initialize Appliance For Gen10 Test Case
    Disable Gen10 A Side Downlink Port
    Power on Server  ${SERVER_GEN10}
    Wait for Server to reach POST State  ${SERVER_GEN10}  post_state=IN_POST_DISCOVERY_COMPLETE  timeout=600
    Server Profile Should Have an Active Missing Boot Entry Alert Warning  ${server_profile_gen10}

OVF5290 TS1 - Second Port Downlink Failure Should Generate Warning Alert For Gen10 UEFI 2 Target 2 Boot Volume FC Boot Profile
    [Documentation]  Verify port 2 downlink failure warning alert on Gen10
    [Tags]  SP  TC5
    Initialize Appliance For Gen10 Test Case
    Disable Gen10 B Side Downlink Port
    Power on Server  ${SERVER_GEN10}
    Wait for Server to reach POST State  ${SERVER_GEN10}  post_state=IN_POST_DISCOVERY_COMPLETE  timeout=600
    Server Profile Should Have an Active Missing Boot Entry Alert Warning  ${server_profile_gen10}

OVF5290 TS1 - All Ports Downlink Failure Should Generate Error Alert For Gen10 UEFI 2 Target 2 Boot Volume FC Boot Profile
    [Documentation]  Verify all port downlink failure critical alert on Gen10
    [Tags]  SP  TC6
    Initialize Appliance For Gen10 Test Case
    Disable Gen10 Downlink Ports
    Power on Server  ${SERVER_GEN10}
    Wait for Server to reach POST State  ${SERVER_GEN10}  post_state=IN_POST_DISCOVERY_COMPLETE  timeout=600
    Server Profile Should Have a Active Missing Boot Entry Alert Error  ${server_profile_gen10}

OVF5290 TS1 - Multiple Reboots on Blade With Connectivity Issues Should Only Have One Alert
    [Documentation]  Verify that there is only one active alert on a server profile after multiple checks
    [Tags]  SP  TC7
    Initialize Appliance For Gen10 Test Case
    Disable Gen10 Downlink Ports
    Power on Server  ${SERVER_GEN10}
    Wait for Server to reach POST State  ${SERVER_GEN10}  post_state=IN_POST_DISCOVERY_COMPLETE  timeout=600
    Server Profile Should Have a Active Missing Boot Entry Alert Error  ${server_profile_gen10}
    Reset Server  ${SERVER_GEN10}
    Wait for Server to reach POST State  ${SERVER_GEN10}  post_state=IN_POST_DISCOVERY_COMPLETE  timeout=600
    Server Profile Should Have a Active Missing Boot Entry Alert Error  ${server_profile_gen10}

OVF5290 TS1 - Editing a Server Profile Should Not Clear Alerts
    [Documentation]  Editing a server profile should not clear previously existing active boot entry alerts
    [Tags]  SP  TC8
    Initialize Appliance For Gen10 Test Case
    Disable Gen10 Downlink Ports
    Power on Server  ${SERVER_GEN10}
    Wait for Server to reach POST State  ${SERVER_GEN10}  post_state=IN_POST_DISCOVERY_COMPLETE  timeout=600
    Server Profile Should Have a Active Missing Boot Entry Alert Error  ${server_profile_gen10}

    Power Off Server  ${SERVER_GEN10}  powerControl=PressAndHold
    ${server_profile_gen10["description"]}=  Set Variable  "This profile has been edited"
    Remove From Dictionary  ${server_profile_gen10}  status_code  headers
    ${task} =  Fusion Api Edit Server Profile  body=${server_profile_gen10}  uri=${server_profile_gen10["uri"]}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${sp}=  Get Resource  SP:${PROFILE1_GEN10_NAME}
    Set Suite Variable  ${server_profile_gen10}  ${sp}

    Server Profile Should Have a Active Missing Boot Entry Alert Error  ${server_profile_gen10}

*** Keywords ***
Initialize the Variables and Log In as Administrator
    [Documentation]  Set the log level to TRACE, initialize the variables and, login to appliance
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${appliance_credentials}

Initialize Appliance for Test Suite Setup
    [Documentation]  Initialize the appliance for the test suite

    Power Off Server  ${SERVER_GEN9}  powerControl=PressAndHold
    Power Off Server  ${SERVER_GEN10}  powerControl=PressAndHold

    ${task}=  Remove Server Profiles by Server Hardware  ${server_hardware_uris}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${task}=  Add Server Profile  ${ts1_gen9_2_target_2_boot_volume_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${PROFILE1_GEN9_NAME}
    Set Suite Variable  ${server_profile_gen9}  ${sp}

    ${task}=  Add Server Profile  ${ts1_gen10_2_target_2_boot_volume_sp}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${sp}=  Get Resource  SP:${PROFILE1_GEN10_NAME}
    Set Suite Variable  ${server_profile_gen10}  ${sp}

Restore Appliance for Test Suite Teardown
    [Documentation]  Clean up the appliance following test suite execution
    Enable Gen9 Downlink Ports
    Enable Gen10 Downlink Ports
    Power Off Server  ${SERVER_GEN9}  powerControl=PressAndHold
    Power Off Server  ${SERVER_GEN10}  powerControl=PressAndHold
    ${task}=  Remove Server Profiles by Server Hardware  ${server_hardware_uris}
    Wait For Task2  ${task}  timeout=600  interval=10

Initialize Appliance For Gen9 Test Case
    [Documentation]  Initialize the appliance state for a Gen9 test case
    Enable Gen9 Downlink Ports
    Power Off Server  ${SERVER_GEN9}  powerControl=PressAndHold
    Reapply Gen9 Server Profile to Update Boot Sources
    Server Profile Should Not Have Active Missing Boot Entry Warnings or Errors  ${server_profile_gen9}

Initialize Appliance For Gen10 Test Case
    [Documentation]  Initialize the appliance state for a Gen10 test case
    Enable Gen10 Downlink Ports
    Power Off Server  ${SERVER_GEN10}  powerControl=PressAndHold
    Power On Server  ${SERVER_GEN10}
    Wait for Server to reach POST State  ${SERVER_GEN10}  post_state=IN_POST_DISCOVERY_COMPLETE  timeout=600
    Server Profile Should Not Have Active Missing Boot Entry Warnings or Errors  ${server_profile_gen10}
    Power Off Server  ${SERVER_GEN10}  powerControl=PressAndHold

Reconfigure Downlink Port Enablement
    [Documentation]  enable/disable a given downlink port. This only works when a server profile is applied to the port.
    [Arguments]  ${server_gen}  ${side}  ${state}
    Set to Dictionary  ${downlink_DTO[${server_gen}][${side}]}  associatedUplinkSetUri=${FC_UPLINK_SET[${side}]}
    Set to Dictionary  ${downlink_DTO[${server_gen}][${side}]}  enabled=${state}
    Update IC Port  ${downlink_DTO[${server_gen}][${side}]["interconnectName"]}  ${downlink_DTO[${server_gen}][${side}]["portName"]}  ${downlink_DTO[${server_gen}][${side}]}

Disable Gen10 A Side Downlink Port
    [Documentation]  Disable the A side SAN Gen10 UUT ICM downlink port
    Reconfigure Downlink Port Enablement  "gen10"  "A"  false

Disable Gen10 B Side Downlink Port
    [Documentation]  Disable the B side SAN Gen10 UUT ICM downlink port
    Reconfigure Downlink Port Enablement  "gen10"  "B"  false

Enable Gen10 A Side Downlink Port
    [Documentation]  Enable the A side SAN Gen10 UUT ICM downlink port
    Reconfigure Downlink Port Enablement  "gen10"  "A"  true

Enable Gen10 B Side Downlink Port
    [Documentation]  Enable the B side SAN Gen10 UUT ICM downlink port
    Reconfigure Downlink Port Enablement  "gen10"  "B"  true

Disable Gen10 Downlink Ports
    [Documentation]  Disable all SAN Gen10 UUT downlink ports
    Disable Gen10 A Side Downlink Port
    Disable Gen10 B Side Downlink Port

Enable Gen10 Downlink Ports
    [Documentation]  Enable all SAN Gen10 UUT downlink ports
    Enable Gen10 A Side Downlink Port
    Enable Gen10 B Side Downlink Port

Disable Gen9 A Side Downlink Port
    [Documentation]  Disable the A side SAN Gen9 UUT ICM downlink port
    Reconfigure Downlink Port Enablement  "gen9"  "A"  false

Disable Gen9 B Side Downlink Port
    [Documentation]  Disable the B side SAN Gen9 UUT ICM downlink port
    Reconfigure Downlink Port Enablement  "gen9"  "B"  false

Enable Gen9 A Side Downlink Port
    [Documentation]  Enable the A side SAN Gen9 UUT ICM downlink port
    Reconfigure Downlink Port Enablement  "gen9"  "A"  true

Enable Gen9 B Side Downlink Port
    [Documentation]  Enable the B side SAN Gen9 UUT ICM downlink port
    Reconfigure Downlink Port Enablement  "gen9"  "B"  true

Disable Gen9 Downlink Ports
    [Documentation]  Disable all SAN Gen9 UUT downlink ports
    Disable Gen9 A Side Downlink Port
    Disable Gen9 B Side Downlink Port

Enable Gen9 Downlink Ports
    [Documentation]  Enable all SAN Gen9 UUT downlink ports
    Enable Gen9 A Side Downlink Port
    Enable Gen9 B Side Downlink Port

Poll For Active Alert
    [Documentation]  A given alert may not be immediately available after an action on a blade.  There is an asynchronous SNMP trap sent to OneView
    ...              from the blade when a condition such as missing boot source is detected. There doesn't appear to be a good way to deterministically
    ...              detect when this SNMP trap has been processed, so do polling to detect alert.  Fail if alert is not found after polling.
    [Arguments]  ${sp}  ${alertType}
    :FOR  ${iteration}  IN  1  2  3  4  5  6  7  8  9  10
    \   ${alerts}=  Get All Alerts By Param   param=?filter=alertTypeID EQ '${alertType}' and alertState EQ 'Active' and resourceUri EQ '${sp["uri"]}'
    \   Return From Keyword If  ${alerts["count"]} >= 1
    \   Sleep  5s
    Fail  Did not find expected alert after polling

Server Profile Should Not Have Active Missing Boot Entry Warnings or Errors
    [Documentation]  The given server profile should not have any active alert warnings or errors for missing boot entries
    [Arguments]  ${sp}
    ${alerts}=  Get All Alerts By Param   param=?filter=alertTypeID EQ 'server-hardware.profile.boot.device.*missing' and alertState NE 'Cleared' and resourceUri EQ '${sp["uri"]}'
    Should be Equal as Integers  ${alerts["count"]}  0

Server Profile Should Have an Active Missing Boot Entry Alert Warning
    [Documentation]  The given server profile uri should have 1 active alert warning for missing boot entries
    [Arguments]  ${sp}
    Poll For Active Alert  ${sp}  server-hardware.profile.boot.device.somemissing

Server Profile Should Have a Active Missing Boot Entry Alert Error
    [Documentation]  The given server profile uri should have 1 locked alert error for missing boot entries
    [Arguments]  ${sp}
    Poll For Active Alert  ${sp}  server-hardware.profile.boot.device.allmissing

Reapply Gen9 Server Profile to Update Boot Sources
    [Documentation]  Perform a reapply of a Gen9 server profile to update iLO's Boot Sources
    ${task}=  Patch Server Profile  ${server_profile_gen9}  op=replace  path=/serverHardwareReapplyState  value=ApplyPending
    Wait For Task2  ${task}  timeout=600  interval=10
