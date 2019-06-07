*** Settings ***
Documentation          This script is to setup Cisco APIC for CI-FIT using REST API.
...                    Example: Configure APIC's VM Networking, Fabric, and Tenants
...                    pybot -d /var/www/html/logs/apic-setup/Eagle62/configure -L TRACE -V ../resources/Eagle62-APIC_multi_data_variable.py -i CONFIGURE setup.robot

Library                ../../../tests/robustness/resources/robustness-helper.py
Library                ../resources/APICOperations.py
Library                APICOperations
Library                json
Resource               ../resources/common.robot

Suite Setup            Login To APIC And Set Session

*** Variables ***

*** Test cases ***
Create Vlan Pools
    [Tags]   CONFIGURE   FABRIC   VLAN_POOLS
    ${VLAN_POOLS} =   Get Variable Value   ${VLAN_POOLS}
    Create Vlan Pool In APIC   ${VLAN_POOLS}

Create Physical Domains
    [Tags]   CONFIGURE    FABRIC  PD   PHYSICAL_DOMAINS
    ${PHYSICAL_DOMAINS} =   Get Variable Value   ${PHYSICAL_DOMAINS}
    Create Physical Domain In APIC   ${PHYSICAL_DOMAINS}

Create Attachable Access Entity Profiles
    [Tags]   CONFIGURE    FABRIC  AAEP   ATTACHABLE_ACCESS_ENTITY_PROFILES
    ${AAEPS} =   Get Variable Value   ${AAEPS}
    Create Attachable Access Entity Profile In APIC   ${AAEPS}

Create Interface Policy Groups
    [Tags]   CONFIGURE    FABRIC  IPG   INTERFACE_POLICY_GROUPS
    ${POLICY_GROUPS} =   Get Variable Value   ${POLICY_GROUPS}
    Create Policy Group In APIC   ${POLICY_GROUPS}

Create Leaf Interface Profiles
    [Tags]   CONFIGURE    FABRIC  LIP   LEAF_IP   LEAF_INTERFACE_PROFILES
    ${LEAF_INTERFACE_PROFILES} =   Get Variable Value   ${LEAF_INTERFACE_PROFILES}
    Create Leaf Interface Profile In APIC   ${LEAF_INTERFACE_PROFILES}

Create Leaf Profiles
    [Tags]   CONFIGURE    FABRIC  LP   LEAF_PROFILES
    ${LEAF_PROFILES} =   Get Variable Value   ${LEAF_PROFILES}
    Create Leaf Profile In APIC   ${LEAF_PROFILES}

Create L2 Interface Policies
    [Tags]   CONFIGURE    FABRIC  L2_IP   L2_INTERFACE_POLICIES
    ${L2_INTERFACE_POLICIES} =   Get Variable Value   ${L2_INTERFACE_POLICIES}
    Create L2 Interface Policy In APIC   ${L2_INTERFACE_POLICIES}

Create LLDP Interface Policies
    [Tags]   CONFIGURE    FABRIC  LLDP_IP   LLDP_INTERFACE_POLICIES
    ${LLDP_INTERFACE_POLICIES} =   Get Variable Value   ${LLDP_INTERFACE_POLICIES}
    Create LLDP Interface Policy In APIC   ${LLDP_INTERFACE_POLICIES}

Create CDP Interface Policies
    [Tags]   CONFIGURE    FABRIC  CDP_IP   CDP_INTERFACE_POLICIES
    ${CDP_INTERFACE_POLICIES} =   Get Variable Value   ${CDP_INTERFACE_POLICIES}
    Create CDP Interface Policy In APIC   ${CDP_INTERFACE_POLICIES}

Create Port Channel Interface Policies
    [Tags]   CONFIGURE    FABRIC  PC_IP   PORT_CHANNEL_INTERFACE_POLICIES
    ${PORT_CHANNEL_INTERFACE_POLICIES} =   Get Variable Value   ${PORT_CHANNEL_INTERFACE_POLICIES}
    Create Port Channel Interface Policy In APIC   ${PORT_CHANNEL_INTERFACE_POLICIES}

Create vCenter Domains
    [Tags]   CONFIGURE   VM_NETWORKING   VC_DOMAINS
    ${VCENTER_DOMAINS} =   Get Variable Value   ${VCENTER_DOMAINS}
    Log To Console   \nCreating vCenter Domain...
    Create vCenter Domain In APIC   ${VCENTER_DOMAINS}

Create EPGs
    [Tags]   CONFIGURE   MINIMAL   EPG   ENDPOINT_GROUPS
    ${TENANTS} =   Get Variable Value   ${TENANTS}
    Log To Console   \nCreating Tenants...
    Create Tenant In APIC   ${TENANTS}
    Log To Console   Creating EPGs...
    Create EPGs In APIC   ${TENANTS}
    Log To Console   Attach EPGs to VLAN and associate Physical Domain...
    Attach EPG To VLAN In APIC   ${TENANTS}

*** Keywords ***

