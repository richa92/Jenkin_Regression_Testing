"""
    Eagle110 APIC setup/teardown data file.
"""
# APIC related data
APIC_URL = "https://15.186.7.19/"
APIC_USERNAME = "admin"
APIC_PASSWORD = "password"

TENANTS = [
    "Eagle110_1",
    "Eagle110_2",
    "Eagle110_3",
    "Eagle110_4",
    "Eagle110_5",
]
APP_PROFILES = {
    TENANTS[0]: "Eagle110_APP_1",
    TENANTS[1]: "Eagle110_APP_2",
    TENANTS[2]: "Eagle110_APP_3",
    TENANTS[3]: "Eagle110_APP_4",
    TENANTS[4]: "Eagle110_APP_5",
}
# EPGs
STATIC_PORTS = {
    TENANTS[0]: [
        {'pod': '1', 'node': 'paths-102', 'path': 'eth1/43'},
        {'pod': '1', 'node': 'protpaths-102-103', 'path': 'Eagle110-2ME-Nitro-vPC_PolicyGrp'}
    ],
    TENANTS[1]: [
        {'pod': '1', 'node': 'paths-102', 'path': 'eth1/43'},
        {'pod': '1', 'node': 'protpaths-102-103', 'path': 'Eagle110-2ME-Nitro-vPC_PolicyGrp'}
    ],
    TENANTS[2]: [
        {'pod': '1', 'node': 'paths-102', 'path': 'eth1/43'},
        {'pod': '1', 'node': 'protpaths-102-103', 'path': 'Eagle110-2ME-Nitro-vPC_PolicyGrp'}
    ],
    TENANTS[3]: [
        {'pod': '1', 'node': 'paths-102', 'path': 'eth1/43'},
        {'pod': '1', 'node': 'protpaths-102-103', 'path': 'Eagle110-2ME-Nitro-vPC_PolicyGrp'}
    ],
    TENANTS[4]: [
        {'pod': '1', 'node': 'paths-102', 'path': 'eth1/43'},
        {'pod': '1', 'node': 'protpaths-102-103', 'path': 'Eagle110-2ME-Nitro-vPC_PolicyGrp'}
    ],
}
VLAN_RANGES = {
    TENANTS[0]: [
        {'start': 2000, 'end': 2199, 'encap': 'vlan'}
    ],
    TENANTS[1]: [
        {'start': 2200, 'end': 2399, 'encap': 'vlan'}
    ],
    TENANTS[2]: [
        {'start': 2400, 'end': 2599, 'encap': 'vlan'}
    ],
    TENANTS[3]: [
        {'start': 2600, 'end': 2799, 'encap': 'vlan'}
    ],
    TENANTS[4]: [
        {'start': 2800, 'end': 3000, 'encap': 'vlan'}
    ],
}
BRIDGE_DOMAINS = {
    TENANTS[0]: [
        {
            "namePrefix": "BD-VLAN_", "vlanRange": VLAN_RANGES[TENANTS[0]][0], "scope": None, "subnetIPv4Addr": None, "arpFlood": "yes", "unkMacUcastAct": "flood",
        }
    ],
    TENANTS[1]: [
        {
            "namePrefix": "BD-VLAN_", "vlanRange": VLAN_RANGES[TENANTS[1]][0], "scope": None, "subnetIPv4Addr": None, "arpFlood": "yes", "unkMacUcastAct": "flood",
        }
    ],
    TENANTS[2]: [
        {
            "namePrefix": "BD-VLAN_", "vlanRange": VLAN_RANGES[TENANTS[2]][0], "scope": None, "subnetIPv4Addr": None, "arpFlood": "yes", "unkMacUcastAct": "flood",
        }
    ],
    TENANTS[3]: [
        {
            "namePrefix": "BD-VLAN_", "vlanRange": VLAN_RANGES[TENANTS[3]][0], "scope": None, "subnetIPv4Addr": None, "arpFlood": "yes", "unkMacUcastAct": "flood",
        }
    ],
    TENANTS[4]: [
        {
            "namePrefix": "BD-VLAN_", "vlanRange": VLAN_RANGES[TENANTS[4]][0], "scope": None, "subnetIPv4Addr": None, "arpFlood": "yes", "unkMacUcastAct": "flood",
        }
    ],
}
EPGS = {
    TENANTS[0]: {
        "namePrefix": "EPG-VLAN_", "bridgeDomain": BRIDGE_DOMAINS[TENANTS[0]][0], 'staticPorts': STATIC_PORTS[TENANTS[0]], "domain": {"type": "phys", "profile": "Eagle110-2ME-Nitro-PD_2000-To-3000"}
    },
    TENANTS[1]: {
        "namePrefix": "EPG-VLAN_", "bridgeDomain": BRIDGE_DOMAINS[TENANTS[1]][0], 'staticPorts': STATIC_PORTS[TENANTS[1]], "domain": {"type": "phys", "profile": "Eagle110-2ME-Nitro-PD_2000-To-3000"}
    },
    TENANTS[2]: {
        "namePrefix": "EPG-VLAN_", "bridgeDomain": BRIDGE_DOMAINS[TENANTS[2]][0], 'staticPorts': STATIC_PORTS[TENANTS[2]], "domain": {"type": "phys", "profile": "Eagle110-2ME-Nitro-PD_2000-To-3000"}
    },
    TENANTS[3]: {
        "namePrefix": "EPG-VLAN_", "bridgeDomain": BRIDGE_DOMAINS[TENANTS[3]][0], 'staticPorts': STATIC_PORTS[TENANTS[3]], "domain": {"type": "phys", "profile": "Eagle110-2ME-Nitro-PD_2000-To-3000"}
    },
    TENANTS[4]: {
        "namePrefix": "EPG-VLAN_", "bridgeDomain": BRIDGE_DOMAINS[TENANTS[4]][0], 'staticPorts': STATIC_PORTS[TENANTS[4]], "domain": {"type": "phys", "profile": "Eagle110-2ME-Nitro-PD_2000-To-3000"}
    },
}
# Bridge Domain has to map with EPG and vice versa
VRFS = {
    TENANTS[0]: "Eagle110-VRF_1",
    TENANTS[1]: "Eagle110-VRF_2",
    TENANTS[2]: "Eagle110-VRF_3",
    TENANTS[3]: "Eagle110-VRF_4",
    TENANTS[4]: "Eagle110-VRF_5",
}
