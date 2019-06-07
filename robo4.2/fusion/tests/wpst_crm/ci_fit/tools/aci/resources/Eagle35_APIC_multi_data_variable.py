# APIC related data
APIC_URL = "https://15.186.7.16/"
APIC_USERNAME = "admin"
APIC_PASSWORD = "password"

TENANTS = [
    "Eagle35-H8_1",
    "Eagle35-H8_2",
    "Eagle35-H8_3_VMM",
    "Eagle35-H8_4",
    "Eagle35-H8_5",
    "Eagle35-H8_6",
    "Eagle35-H8_7",
]
APP_PROFILES = {
    TENANTS[0]: "Eagle35_APP_1",
    TENANTS[1]: "Eagle35_APP_2",
    TENANTS[2]: "Eagle35_APP_3_VMM",
    TENANTS[3]: "Eagle35_APP_4",
    TENANTS[4]: "Eagle35_APP_5",
    TENANTS[5]: "Eagle35_APP_6",
    TENANTS[6]: "Eagle35_APP_7",
}
# EPGs
STATIC_PORTS = {
    TENANTS[0]: [
        {'pod': '1', 'node': 'paths-101', 'path': 'eth1/16'},
        {'pod': '1', 'node': 'protpaths-101-103', 'path': 'Switch101_103_1-ports-33_PolGrp'}
    ],
    TENANTS[1]: [
        {'pod': '1', 'node': 'paths-101', 'path': 'eth1/16'},
        {'pod': '1', 'node': 'protpaths-101-103', 'path': 'Switch101_103_1-ports-33_PolGrp'}
    ],
    TENANTS[2]: [
        {'pod': '1', 'node': 'paths-101', 'path': 'eth1/10'},
        {'pod': '1', 'node': 'protpaths-101-103', 'path': 'Switch101_103_1-ports-32_PolGrp'}
    ],
    TENANTS[3]: [
        {'pod': '1', 'node': 'paths-101', 'path': 'eth1/16'},
        {'pod': '1', 'node': 'protpaths-101-103', 'path': 'Switch101_103_1-ports-33_PolGrp'}
    ],
    TENANTS[4]: [
        {'pod': '1', 'node': 'paths-101', 'path': 'eth1/16'},
        {'pod': '1', 'node': 'protpaths-101-103', 'path': 'Switch101_103_1-ports-33_PolGrp'}
    ],
    TENANTS[5]: [
        {'pod': '1', 'node': 'paths-101', 'path': 'eth1/16'},
        {'pod': '1', 'node': 'protpaths-101-103', 'path': 'Switch101_103_1-ports-33_PolGrp'}
    ],
    TENANTS[6]: [
        {'pod': '1', 'node': 'paths-101', 'path': 'eth1/16'},
        {'pod': '1', 'node': 'protpaths-101-103', 'path': 'Switch101_103_1-ports-33_PolGrp'}
    ],
}
VLAN_RANGES = {
    TENANTS[0]: [
        {'start': 101, 'end': 200, 'encap': 'vlan'}
    ],
    TENANTS[1]: [
        {'start': 201, 'end': 300, 'encap': 'vlan'}
    ],
    TENANTS[2]: [
        {'start': 301, 'end': 500, 'encap': 'vlan'}
    ],
    TENANTS[3]: [
        {'start': 501, 'end': 700, 'encap': 'vlan'}
    ],
    TENANTS[4]: [
        {'start': 701, 'end': 800, 'encap': 'vlan'}
    ],
    TENANTS[5]: [
        {'start': 801, 'end': 1000, 'encap': 'vlan'}
    ],
    TENANTS[6]: [
        {'start': 1005, 'end': 2004, 'encap': 'vlan'}
    ],
}
BRIDGE_DOMAINS = {
    TENANTS[0]:
        {
            "namePrefix": "BD-VLAN_", "vlanRange": VLAN_RANGES[TENANTS[0]][0], "scope": None, "subnetIPv4Addr": None, "arpFlood": "yes", "unkMacUcastAct": "flood",
    },
    TENANTS[1]:
        {
            "namePrefix": "BD-VLAN_", "vlanRange": VLAN_RANGES[TENANTS[1]][0], "scope": None, "subnetIPv4Addr": None, "arpFlood": "yes", "unkMacUcastAct": "flood",
    },
    TENANTS[2]:
        {
            "namePrefix": "BD-VLAN_VMM_", "vlanRange": VLAN_RANGES[TENANTS[2]][0], "scope": None, "subnetIPv4Addr": None, "arpFlood": "yes", "unkMacUcastAct": "flood",
    },
    TENANTS[3]:
        {
            "namePrefix": "BD-VLAN_", "vlanRange": VLAN_RANGES[TENANTS[3]][0], "scope": None, "subnetIPv4Addr": None, "arpFlood": "yes", "unkMacUcastAct": "flood",
    },
    TENANTS[4]:
        {
            "namePrefix": "BD-VLAN_", "vlanRange": VLAN_RANGES[TENANTS[4]][0], "scope": None, "subnetIPv4Addr": None, "arpFlood": "yes", "unkMacUcastAct": "flood",
    },
    TENANTS[5]:
        {
            "namePrefix": "BD-VLAN_VMM_", "vlanRange": VLAN_RANGES[TENANTS[5]][0], "scope": None, "subnetIPv4Addr": None, "arpFlood": "yes", "unkMacUcastAct": "flood",
    },
    TENANTS[6]:
        {
            "namePrefix": "BD-VLAN_VMM_", "vlanRange": VLAN_RANGES[TENANTS[6]][0], "scope": None, "subnetIPv4Addr": None, "arpFlood": "yes", "unkMacUcastAct": "flood",
    },
}
EPGS = {
    TENANTS[0]: [
        {
            "namePrefix": "EPG-VLAN_", "bridgeDomain": BRIDGE_DOMAINS[TENANTS[0]], 'staticPorts': STATIC_PORTS[TENANTS[0]], "domain": {"type": "phys", "profile": "Eagle35-PD"}
        }
    ],
    TENANTS[1]: [
        {
            "namePrefix": "EPG-VLAN_", "bridgeDomain": BRIDGE_DOMAINS[TENANTS[1]], 'staticPorts': STATIC_PORTS[TENANTS[1]], "domain": {"type": "phys", "profile": "Eagle35-PD"}
        }
    ],
    TENANTS[2]: [
        {
            "namePrefix": "EPG-VLAN_VMM_", "bridgeDomain": BRIDGE_DOMAINS[TENANTS[2]], 'staticPorts': STATIC_PORTS[TENANTS[2]], "domain": {"type": "vmmp", "vmType": "VMware", "profile": "vDS_ESXi"}
        }
    ],
    TENANTS[3]: [
        {
            "namePrefix": "EPG-VLAN_", "bridgeDomain": BRIDGE_DOMAINS[TENANTS[3]], 'staticPorts': STATIC_PORTS[TENANTS[3]], "domain": {"type": "phys", "profile": "Eagle35-PD"}
        }
    ],
    TENANTS[4]: [
        {
            "namePrefix": "EPG-VLAN_", "bridgeDomain": BRIDGE_DOMAINS[TENANTS[4]], 'staticPorts': STATIC_PORTS[TENANTS[4]], "domain": {"type": "phys", "profile": "Eagle35-PD"}
        }
    ],
    TENANTS[5]: [
        {
            "namePrefix": "EPG-VLAN_", "bridgeDomain": BRIDGE_DOMAINS[TENANTS[5]], 'staticPorts': STATIC_PORTS[TENANTS[5]], "domain": {"type": "phys", "profile": "Eagle35-PD"}
        }
    ],
    TENANTS[6]: [
        {
            "namePrefix": "EPG-VLAN_", "bridgeDomain": BRIDGE_DOMAINS[TENANTS[6]], 'staticPorts': STATIC_PORTS[TENANTS[6]], "domain": {"type": "phys", "profile": "Eagle35-PD"}
        }
    ],
}
# Bridge Domain has to map with EPG and vice versa
VRFS = {
    TENANTS[0]: "Eagle35-VRF_1",
    TENANTS[1]: "Eagle35-VRF_2",
    TENANTS[2]: "Eagle35-VRF_3",
    TENANTS[3]: "Eagle35-VRF_4",
    TENANTS[4]: "Eagle35-VRF_5",
    TENANTS[5]: "Eagle35-VRF_6",
    TENANTS[6]: "Eagle35-VRF_7",
}
