*** Settings ***

*** Keywords ***
################
# General Purpose
################
Login To APIC And Set Session
    [Documentation]   Login to APIC and set session variable
    Variable File Should Be Passed
    Get ACI APIC Session   ${APIC_URL}   ${APIC_USERNAME}   ${APIC_PASSWORD}

Get ACI APIC Session
    [Documentation]  Get ACI APIC login session with the given URL, username, password
    [Arguments]  ${url}  ${username}  ${password}
    ${session} =  Get APIC Session  ${url}  ${username}  ${password}
    Set Suite Variable  ${session}
    Run Keyword If   '${session}' == '${null}'   Fail   msg=Authentication token not found. Make sure you are able to get APIC session.

################
# Tenant Create
################
Create Tenant In APIC
    [Documentation]  Create a tenant in APIC.
    [Arguments]  ${tenant_names}
    Run Keyword If   ${tenant_names} is ${null}   Create Tenant  ${session}  ${tenant_names}

Create EPGs In APIC
    [Arguments]  ${tenants}
    [Documentation]   Create EPG in APIC.
    Return From Keyword If   ${tenants} is ${null}
    :FOR   ${tenant}   IN   @{tenants}
    \   ${profile} =   Get Variable Value   ${APP_PROFILES['${tenant}']}
    \   ${vrf} =   Get Variable Value   ${VRFS['${tenant}']}
    \   ${epg} =   Get Variable Value   ${EPGS['${tenant}']}
    \   Run Keyword If   '${profile}' is not ${null} and '${vrf}' is not ${null} and ${epg} is not ${null}   Create EPGs    ${session}   ${tenant}   ${profile}   ${vrf}   ${epg}

Create Bridge Domains In APIC
    [Documentation]  Create Bridge Domain in APIC.
    [Arguments]  ${tenants}
    Return From Keyword If   ${tenants} is ${null}
    :FOR   ${tenant}   IN   @{tenants}
    \   ${bd} =  Get Variable Value  ${BRIDGE_DOMAINS['${tenant}']}
    \   ${vrf} =  Get Variable Value  ${VRFS['${tenant}']}
    \   Create Bridge Domains    ${session}   ${tenant}   ${vrf}   ${bd}

Attach EPG To VLAN In APIC
    [Documentation]  Attach EPG to VLAN in APIC.
    [Arguments]  ${tenants}
    Return From Keyword If   ${tenants} is ${null}
    :FOR   ${tenant}   IN   @{tenants}
    \   ${epg} =  Get Variable Value  ${EPGS['${tenant}']}
    \   ${profile} =  Get Variable Value  ${APP_PROFILES['${tenant}']}
    \   ${vrf} =  Get Variable Value  ${VRFS['${tenant}']}
    \   Run Keyword If   ${epg} is not ${null} and '${profile}' is not ${null} and '${vrf}' is not ${null}   Attach EPG To VLAN    ${session}   ${tenant}   ${profile}   ${vrf}   ${epg}

################
# Tenant Delete
################
Delete Tenant In APIC
    [Documentation]  Delete a tenant in APIC.
    [Arguments]  ${tenant}
    Delete Tenant  ${session}  ${tenant}

Delete All Tenants
    [Documentation]   Delete all Tenants listed in the data variable file.
    [Arguments]   ${tenants}
    Return From Keyword If   ${tenants} is ${null}
    :FOR   ${tenant}   IN   @{TENANTS}
    \   Log To Console   Deleting Tenant: ${tenant}
    \   Delete Tenant In APIC   ${tenant}

Delete Application Profile In APIC
    [Documentation]   Delete Application Profile in APIC.
    [Arguments]   ${tenant}   ${profile}
    Delete Application Profile   ${session}   ${tenant}   ${profile}

Delete All Application Profiles From Tenants In Data File
    [Documentation]   Delete all Application Profiles from Tenants listed in data variable file.
    [Arguments]   ${tenants}
    Return From Keyword If   ${tenants} is ${null}
    :FOR   ${tenant}   IN   @{tenants}
    \   Log To Console   Deleting Application Profile in Tenant: ${tenant}
    \   ${profile} =   Get Variable Value   ${APP_PROFILES['${tenant}']}
    \   Run Keyword If   '${profile}' is not ${null}   Delete Application Profile In APIC   ${tenant}   ${profile}

Delete EPGs In APIC
    [Documentation]   Delete EPGs in APIC.
    [Arguments]  ${tenant}   ${profile}   ${epgs}
    Delete EPGs    ${session}   ${tenant}   ${profile}   ${epgs}

Delete All EPGs From Tenants In Data File
    [Documentation]   Delete all EPGs from Tenants listed in data variable file.
    [Arguments]   ${tenants}
    Return From Keyword If   ${tenants} is ${null}
    :FOR   ${tenant}   IN   @{tenants}
    \   Log To Console   Deleting EPGs in Tenant: ${tenant}
    \   ${profile} =   Get Variable Value   ${APP_PROFILES['${tenant}']}
    \   ${epg} =   Get Variable Value   ${EPGS['${tenant}']}
    \   Run Keyword If   '${profile}' is not ${null} and ${epg} is not ${null}   Delete EPGs In APIC   ${tenant}   ${profile}   ${epg}

Delete Bridge Domains In APIC
    [Documentation]   Delete Bridge Domains in APIC.
    [Arguments]  ${tenant}   ${bridgeDomains}
    Delete Bridge Domains    ${session}   ${tenant}   ${bridgeDomains}

Delete All Bridge Domains From Tenants In Data File
    [Documentation]   Delete all Bridge Domains from Tenants listed in data variable file.
    [Arguments]   ${tenants}
    Return From Keyword If   ${tenants} is ${null}
    :FOR   ${tenant}   IN   @{tenants}
    \   Log To Console   Deleting Bridge Domains in Tenant: ${tenant}
    \   ${bd} =   Get Variable Value   ${BRIDGE_DOMAINS['${tenant}']}
    \   Run Keyword If   ${bd} is not ${null}   Delete Bridge Domains In APIC   ${tenant}   ${bd}

Delete VRF In APIC
    [Documentation]   Delete VRF in APIC.
    [Arguments]   ${tenant}   ${vrf}
    Delete VRF    ${session}   ${tenant}   ${vrf}

Delete All VRFs From Tenants In Data File
    [Documentation]   Delete all VRFs or Contexts from Tenants listed in data variable file.
    [Arguments]   ${tenants}
    Return From Keyword If   ${tenants} is ${null}
    :FOR   ${tenant}   IN   @{tenants}
    \   Log To Console   Deleting VRFs in Tenant: ${tenant}
    \   ${vrf} =   Get Variable Value   ${VRFS['${tenant}']}
    \   Run Keyword If   '${vrf}' is not ${null}   Delete VRF In APIC   ${tenant}   ${vrf}

################
# Fabric Create
################
Create Vlan Pool In APIC
    [Documentation]   Create Vlan Pool in APIC's Fabric.
    [Arguments]   ${vlanPools}
    Return From Keyword If   ${vlanPools} is ${null}
    :FOR   ${vlanPool}   IN   @{vlanPools}
    \   Create Vlan Pool   ${session}   ${vlanPool}

Create Physical Domain In APIC
    [Documentation]   Create Physical Domain in APIC's Fabric Access Policies.
    [Arguments]   ${physicalDomains}
    Return From Keyword If   ${physicalDomains} is ${null}
    :FOR   ${pd}   IN   @{physicalDomains}
    \   Create Physical Domain   ${session}   ${pd}

Create Attachable Access Entity Profile in APIC
    [Documentation]   Create Attachable Access Entity Profile in APIC's Fabric Access Policies.
    [Arguments]   ${attachableAEPS}
    Return From Keyword If   ${attachableAEPS} is ${null}
    :FOR   ${aep}   IN   @{attachableAEPS}
    \   Create Attachable Access Entity Profile   ${session}   ${aep}

Create Policy Group In APIC
    [Documentation]   Create Policy Group in APIC's Fabric Access Policies.
    ...               Accept a list of dictionary of pre-defined attributes in data variable file.
    [Arguments]   ${policyGroups}
    Return From Keyword If   ${policyGroups} is ${null}
    :FOR   ${pg}   IN   @{policyGroups}
    \   Run Keyword If   '${pg['type']}' == 'accessPort'   Create Access Port Interface Policy Group   ${session}   ${pg}
    \   ...   ELSE IF   '${pg['type']}' == 'vPC'   Create VPC Interface Policy Group   ${session}   ${pg}
    \   ...   ELSE   Fail   msg=Invalid type in POLICY_GROUPS variable. Check your data variable file and try again.

Create Leaf Interface Profile In APIC
    [Documentation]   Create Leaf Interface Profile in APIC's Fabric Access Policies.
    [Arguments]   ${leafInterfaceProfiles}
    Return From Keyword If   ${leafInterfaceProfiles} is ${null}
    :FOR   ${lip}   IN   @{leafInterfaceProfiles}
    \   Create Leaf Interface Profile   ${session}   ${lip}

Create Leaf Profile In APIC
    [Documentation]   Create Leaf Profile in APIC's Fabric Access Policies with Leaf Selector and Leaf Interface Profile associated.
    [Arguments]   ${leafProfiles}
    Return From Keyword If   ${leafProfiles} is ${null}
    :FOR   ${lp}   IN   @{leafProfiles}
    \   Create Leaf Profile   ${session}   ${lp}

Create L2 Interface Policy In APIC
    [Documentation]   Create L2 Interface Policy in APIC's Fabric Access Policies.
    [Arguments]   ${l2InterfacePolicies}
    Return From Keyword If   ${l2InterfacePolicies} is ${null}
    :FOR   ${l2ip}   IN   @{l2InterfacePolicies}
    \   Create L2 Interface Policy   ${session}   ${l2ip}

Create LLDP Interface Policy In APIC
    [Documentation]   Create LLDP Interface Policy in APIC's Fabric Access Policies.
    [Arguments]   ${lldpInterfacePolicies}
    Return From Keyword If   ${lldpInterfacePolicies} is ${null}
    :FOR   ${lldpip}   IN   @{lldpInterfacePolicies}
    \   Create LLDP Interface Policy   ${session}   ${lldpip}

Create CDP Interface Policy In APIC
    [Documentation]   Create CDP Interface Policy in APIC's Fabric Access Policies
    [Arguments]   ${cdpInterfacePolicies}
    Return From Keyword If   ${cdpInterfacePolicies} is ${null}
    :FOR   ${cdpip}   IN   @{cdpInterfacePolicies}
    \   Create CDP Interface Policy   ${session}   ${cdpip}

Create Port Channel Interface Policy In APIC
    [Documentation]   Create Port Channel Interface Policy in APIC's Fabric Access Policies
    [Arguments]   ${pcInterfacePolicies}
    Return From Keyword If   ${pcInterfacePolicies} is ${null}
    :FOR   ${pcip}   IN   @{pcInterfacePolicies}
    \   Create Port Channel Interface Policy   ${session}   ${pcip}

Create vCenter Domain In APIC
    [Documentation]   Create vCenter Domain in APIC's VM Networking.
    [Arguments]   ${vCenterDomains}
    Return From Keyword If   ${vCenterDomains} is ${null}
    :FOR   ${vCenter}   IN   @{vCenterDomains}
    \   Create vCenter Domain   ${session}   ${vCenter}

