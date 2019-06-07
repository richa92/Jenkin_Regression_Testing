import pprint

pp = pprint.PrettyPrinter(indent=4)
# APIC Login Data
APIC_URL = "https://15.186.7.16/"
APIC_USERNAME = "admin"
APIC_PASSWORD = "password"

# NOTE: Objects you don't want to create? Just mark them out
# Common variables for both Fabric Access Policies and VM Networking
# L2_INTERFACE_POLICIES = [
#     {
#         "name": "PerPort-VLAN_L2_IP",
#         "descr": "",
#         "qinq": "disabled",
#         "reflectiveRelay": "disabled",
#         "vlanScope": "portlocal"
#     }
# ]
#
# LLDP_INTERFACE_POLICIES = [
#     {
#         "name": "LLDP-Enable-Bidirection",
#         "adminRxSt": "enabled",
#         "adminTxSt": "enabled",
#         "descr": "",
#         "nameAlias": ""
#     }
# ]
#
# CDP_INTERFACE_POLICIES = [
#     {
#         "name": "Disable-CDP",
#         "descr": "",
#         "nameAlias": "",
#         "adminSt": "disabled"
#     }
# ]
#
# PORT_CHANNEL_INTERFACE_POLICIES = [
#     {
#         "name": "LACP-Active",
#         "descr": "",
#         "nameAlias": "",
#         "mode": "active",
#         "ctrl": "fast-sel-hot-stdby,graceful-conv,susp-individual",
#         "minLinks": "1",
#         "maxLinks": "16"
#     }
# ]

VLAN_POOLS_8_COUNTS_10_TO_1000 = [
    {
        "name": "Eagle10-5ME-CL10_vlan_10-200",
        "encapType": "vlan",
        "allocMode": "static",
        "ranges": [
            {
                "startVlan": "10",
                "endVlan": "200"
            }
        ]
    },
    {
        "name": "Eagle10-5ME-CL10_vlan_201-300",
        "encapType": "vlan",
        "allocMode": "static",
        "ranges": [
            {
                "startVlan": "201",
                "endVlan": "300"
            }
        ]
    },
    {
        "name": "Eagle10-5ME-CL10_vlan_301-400",
        "encapType": "vlan",
        "allocMode": "static",
        "ranges": [
            {
                "startVlan": "301",
                "endVlan": "400"
            }
        ]
    },
    {
        "name": "Eagle10-5ME-CL10_vlan_401-500",
        "encapType": "vlan",
        "allocMode": "static",
        "ranges": [
            {
                "startVlan": "401",
                "endVlan": "500"
            }
        ]
    },
    {
        "name": "Eagle10-5ME-CL10_vlan_501-600",
        "encapType": "vlan",
        "allocMode": "static",
        "ranges": [
            {
                "startVlan": "501",
                "endVlan": "600"
            }
        ]
    },
    {
        "name": "Eagle10-5ME-CL10_vlan_601-700",
        "encapType": "vlan",
        "allocMode": "static",
        "ranges": [
            {
                "startVlan": "601",
                "endVlan": "700"
            }
        ]
    },
    {
        "name": "Eagle10-5ME-CL10_vlan_701-800",
        "encapType": "vlan",
        "allocMode": "static",
        "ranges": [
            {
                "startVlan": "701",
                "endVlan": "800"
            }
        ]
    },
    {
        "name": "Eagle10-5ME-CL10_vlan_801-1000",
        "encapType": "vlan",
        "allocMode": "static",
        "ranges": [
            {
                "startVlan": "801",
                "endVlan": "900"
            },
            {
                "startVlan": "901",
                "endVlan": "1000"
            }
        ]
    }
]

VLAN_POOLS_1_COUNT_10_TO_1000 = [
    {
        "name": "Eagle10-5ME-CL10_vlan_10-1000",
        "encapType": "vlan",
        "allocMode": "static",
        "ranges": [
            {
                "startVlan": "10",
                "endVlan": "200"
            },
            {
                "startVlan": "201",
                "endVlan": "300"
            },
            {
                "startVlan": "301",
                "endVlan": "400"
            },
            {
                "startVlan": "401",
                "endVlan": "500"
            },
            {
                "startVlan": "501",
                "endVlan": "600"
            },
            {
                "startVlan": "601",
                "endVlan": "700"
            },
            {
                "startVlan": "701",
                "endVlan": "800"
            },
            {
                "startVlan": "801",
                "endVlan": "900"
            },
            {
                "startVlan": "901",
                "endVlan": "1000"
            }
        ]
    }
]

VLAN_POOLS = VLAN_POOLS_1_COUNT_10_TO_1000

# VM Networking
# VCENTER_DOMAINS = [
#     {
#         "name": "vDS_ESXi-jason",
# aka epRetTime
#         "endPointRetentionTime": "0",
# aka vmmCtrlrP
#         "vCenterController": [
#             {
#                 "name": "OV-VC1-jason",
#                 "hostOrIp": "15.186.9.63",
#                 "dvsVersion": "unmanaged",
#                 "rootContName": "ESXI_DATACENTER-jason",
# aka n1kvStatsMode
#                 "statsCollection": "enabled",
# aka vmmUsrAccP
#                 "vmmCredential" : {
#                     "name": "JasonPernito",
#                     "descr": "",
# aka usr
#                     "userName": "jpernito",
# aka pwd
#                     "password": "password"
#                 }
#             }
#         ],
# aka aaaDomainRef
#         "securityDomains": [],
#         "vlanPool": VLAN_POOLS[0],
# aka vmmVSwitchPolicyCont
#         "vSwitchPolicies": {
# aka vmmRsVswitchOverrideLacpPol
#                 "portChannelPolicy": "LACP-Active-jason",
# aka vmmRsVswitchOverrideLldpIfPol
#                 "lldpPolicy": "LLDP-Enable-Bidirection-jason",
# vmmRsVswitchOverrideCdpIfPol
#                 "cdpPolicy": "Disable-CDP-jason"
#         },
#         "attachableEntityProfile": "Eagle10-5ME-CL10-jason_attachableAEP"
#     }
# ]
#
# Fabric
PHYSICAL_DOMAINS = [
    {
        "name": "Eagle10-5ME-CL10-PD_10-TO-1000",
        "vlanPool": VLAN_POOLS[0]
    }
]

AAEPS = [
    {
        "name": "Eagle10-5ME-CL10_attachableAEP",
        "physicalDomain": PHYSICAL_DOMAINS[0]['name']
    }
]

POLICY_GROUPS = [
    {
        "name": "Eagle10-5ME-CL10_accPortGrp",
        "aepName": AAEPS[0]['name'],
        "cdpPolicy": "Disable-CDP",
        "lldpPolicy": "LLDP-Enable-Bidirection",
        "l2Policy": "PerPort-VLAN_L2_IP",
        "type": "accessPort"
    },
    {
        "name": "Eagle10-5ME-CL10_vpcPolicyGrp",
        "aepName": AAEPS[0]['name'],
        "cdpPolicy": "Disable-CDP",
        "lldpPolicy": "LLDP-Enable-Bidirection",
        "l2Policy": "PerPort-VLAN_L2_IP",
        "lacpLagPolicy": "LACP-Active",
        "type": "vPC"
    }
]

# Leaf Interface Profile (and Access Port Selector)
LEAF_INTERFACE_PROFILES = [
    {
        "name": "Eagle10-5ME-CL10_leafInterfaceProfile",
        "accessPortSelector": [
            {
                "name": "Eagle10-5ME-CL10_accessPortSelector",
                "policyGroup": POLICY_GROUPS[1],
                "interfaces": [
                    {
                        "blockName": "block1_17-to-20",
                        "fromCard": "1",
                        "toCard": "1",
                        "fromPort": "17",
                        "toPort": "20"
                    }
                ]
            }
        ]
    },
    {
        "name": "Eagle10-5ME-CL10-TCS_leafInterfaceProfile",
        "accessPortSelector": [
            {
                "name": "Eagle10-5ME-CL10_TCS_accessPortSelector",
                "policyGroup": POLICY_GROUPS[0],
                "interfaces": [
                    {
                        "blockName": "block1_14",
                        "fromCard": "1",
                        "toCard": "1",
                        "fromPort": "14",
                        "toPort": "14"
                    }
                ]
            }
        ]
    }
]

LEAF_PROFILES = [
    {
        "name": "Eagle10-5ME-CL10_leafProfile_101",
        "leafSelectors": [
            {
                "name": "Eagle10-5ME-CL10_leafSelector_101",
                "blocks": [
                    {
                        "name": "block_101",
                        "from_": "101",
                        "to_": "101"
                    }
                ]
            }
        ],
        "leafInterfaceProfile": "Eagle10-5ME-CL10_leafInterfaceProfile"
    },
    {
        "name": "Eagle10-5ME-CL10_leafProfile_103",
        "leafSelectors": [
            {
                "name": "Eagle10-5ME-CL10_leafSelector_103",
                "blocks": [
                    {
                        "name": "block_103",
                        "from_": "103",
                        "to_": "103"
                    }
                ]
            }
        ],
        "leafInterfaceProfile": "Eagle10-5ME-CL10_leafInterfaceProfile"
    },
    {
        "name": "Eagle10-5ME-CL10_TCS_leafProfile",
        "leafSelectors": [
            {
                "name": "Eagle10-5ME-CL10_TCS_leafSelector",
                "blocks": [
                    {
                        "name": "block_101",
                        "from_": "101",
                        "to_": "101"
                    }
                ]
            }
        ],
        "leafInterfaceProfile": "Eagle10-5ME-CL10-TCS_leafInterfaceProfile"
    }
]

# Tenant and App Details for the Test Environment.


def create_x_tenants(prefix, count):
    """
    Create x number of tenants.
    Arguments:
        prefix - tenants name prefix
        count - x number of tenants
    Return:
        list of tenants in prefix + '_' + count format
    """
    tenants = []
    for x in xrange(0, count):
        tenants.append(prefix + '_' + str(x))
    return tenants

TENANT_PREFIX = "Eagle10-5ME-CL10"
TENANT_COUNT = 50
TENANTS = create_x_tenants(TENANT_PREFIX, TENANT_COUNT)

# Application Profiles


def define_application_profiles(tenant_prefix, profile_prefix, count):
    """
    Define application profiles. This assumes 1:1 profile to tenant ratio.
    Arguments:
        tenant_prefix - tenants name prefix
        profile_prefix - profile name prefix
        count - x number of profiles
    Return:
        dictionary of tenant-profile key-value pair
    """
    profiles = {}
    for x in xrange(0, count):
        profiles[tenant_prefix + '_' + str(x)] = profile_prefix + '_' + str(x)
    return profiles

PROFILE_PREFIX = "Eagle10-ApplicationProfile"
APP_PROFILES = define_application_profiles(TENANT_PREFIX, PROFILE_PREFIX, TENANT_COUNT)

STATIC_PORTS = {
    'US1': [
        {'pod': '1', 'node': 'paths-101', 'path': 'eth1/13'},
        {'pod': '1', 'node': 'protpaths-101-103', 'path': 'Eagle10-5ME-CL10_vpcPolicyGrp'}
    ]
}

# VLAN Ranges to configure on ACI/APIC


def define_tenant_vlan_range(tenant_prefix, tenant_count, start_vlan, end_vlan):
    """
    Define tenant vlan ranges by distributing total_vlans tenant_count.
    Argument:
        tenant_prefix - tenants name prefix
        tenant_count - x number of tenants
        total_vlans - x number of vlans
    Return:
        dictionary of tenants vlan ranges like this:
        TENANTS[0]: [
            {'start': 10, 'end': 200, 'encap': 'vlan'},
            {'start': 201, 'end': 300, 'encap': 'vlan'},
            {'start': 301, 'end': 400, 'encap': 'vlan'},
            {'start': 401, 'end': 500, 'encap': 'vlan'},
            {'start': 501, 'end': 600, 'encap': 'vlan'},
            {'start': 601, 'end': 700, 'encap': 'vlan'},
            {'start': 701, 'end': 800, 'encap': 'vlan'},
            {'start': 801, 'end': 1000, 'encap': 'vlan'}
        ]
    """
    tenant_vlans = {}
    # calculate total vlans
    total_vlans = (end_vlan - start_vlan) + 1
    est_vlan = int(total_vlans / tenant_count)
    for x in xrange(0, tenant_count):
        if x != (tenant_count - 1):
            tenant_vlans[tenant_prefix + '_' + str(x)] = [{'start': start_vlan, 'end': start_vlan + est_vlan, 'encap': 'vlan'}]
        else:
            tenant_vlans[tenant_prefix + '_' + str(x)] = [{'start': start_vlan, 'end': end_vlan, 'encap': 'vlan'}]
        start_vlan = start_vlan + est_vlan + 1
    return tenant_vlans

VLAN_RANGES = define_tenant_vlan_range(TENANT_PREFIX, TENANT_COUNT, 10, 1000)

# Bridge Domain has to map with EPG and vice versa


def define_bridge_domains(tenant_prefix, bd_prefix, tenant_count):
    """
    Define bridge domains.
    Arguments:
        tenant_prefix - tenant name prefix
        bd_prefix - bridge domain name prefix
        tenant_count - x number of tenants
    Return:
        dictionary of bridge domains
    """
    bridge_domains = {}
    for x in xrange(0, tenant_count):
        bridge_domains[tenant_prefix + '_' + str(x)] = [{"namePrefix": bd_prefix, "vlanRange": VLAN_RANGES[TENANTS[x]][0], "scope": None, "subnetIPv4Addr": None, "arpFlood": "yes", "unkMacUcastAct": "flood"}]
    return bridge_domains

BD_PREFIX = "BD_Vlan-"
BRIDGE_DOMAINS = define_bridge_domains(TENANT_PREFIX, BD_PREFIX, TENANT_COUNT)

# EPGs
# NOTE: Since we are using 1:1 mapping of BD and EPG, we will be using the same vlanRange defined in BD.


def define_epgs(tenant_prefix, epg_prefix, tenant_count):
    """
    Define EPGS.
    Argument:
        tenant_prefix - tenant name prefix
        epg_prefix - EPG name prefix
        tenant_count - x number of tenants
    Return:
       dictionary of EPGs
    """
    epgs = {}
    for x in xrange(0, tenant_count):
        epgs[tenant_prefix + '_' + str(x)] = [{"namePrefix": epg_prefix, "bridgeDomain": BRIDGE_DOMAINS[TENANTS[x]][0], 'staticPorts': STATIC_PORTS['US1'], "domain": {"profile": "Eagle10-5ME-CL10-PD_10-TO-1000", "type": "phys"}}]
    return epgs

EPG_PREFIX = "EPG_vlan-"
EPGS = define_epgs(TENANT_PREFIX, EPG_PREFIX, TENANT_COUNT)

# VRF can be 1 to many BD


def define_vrfs(tenant_prefix, vrf_prefix, count):
    """
    Define VRFs. This assumes 1:1 vrf to tenant ratio.
    Arguments:
        tenant_prefix - tenants name prefix
        profile_prefix - profile name prefix
        count - x number of profiles
    Return:
        dictionary of tenant-profile key-value pair
    """
    vrfs = {}
    for x in xrange(0, count):
        vrfs[tenant_prefix + '_' + str(x)] = vrf_prefix + '_' + str(x)
    return vrfs

VRF_PREFIX = "Eagle10-VRF"
VRFS = define_vrfs(TENANT_PREFIX, VRF_PREFIX, TENANT_COUNT)
